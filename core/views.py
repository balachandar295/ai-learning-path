# core/views.py — CLEAN MERGED VERSION

import json
import csv
import os
import random
import io
import requests
from datetime import date, timedelta
from contextlib import redirect_stdout

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.cache import cache

from .models import UserPreference, UserActivity, Question, AptitudeQuestion, JobApplication
from .roadmap_data import DEVELOPER_ROADMAPS

from groq import Groq

# Initialize Groq Client
GROQ_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_KEY)


# ═══════════════════════════════════════
# 1. ENTRY POINT
# ═══════════════════════════════════════
def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home_view')
    return redirect('login')


# ═══════════════════════════════════════
# 2. AUTHENTICATION
# ═══════════════════════════════════════
def register_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.create_user(
                username=data.get('email'),
                email=data.get('email'),
                password=data.get('password'),
                first_name=data.get('full_name')
            )
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return JsonResponse({'status': 'success', 'redirect_url': '/profile/'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        
        user = authenticate(request, username=username_input, password=password_input)
        
        if not user:
            # Fallback: check if the user entered their email instead of username
            user_obj = User.objects.filter(email__iexact=username_input).first()
            if user_obj:
                user = authenticate(request, username=user_obj.username, password=password_input)

        if user:
            login(request, user)
            return redirect('home_view')
            
        messages.error(request, "Invalid Username or Password!")
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@csrf_protect
def forgot_password_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = random.randint(100000, 999999)
            request.session['reset_otp'] = str(otp)
            request.session['reset_email'] = email
            send_mail(
                'Your Password Reset OTP',
                f'Hello {user.username},\n\nYour OTP is: {otp}',
                'bchandar295@gmail.com',
                [email],
                fail_silently=False,
            )
            return JsonResponse({'status': 'success'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Email not found.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Failed to send email.'})
    return render(request, 'forgot_password.html')


def verify_otp(request):
    return render(request, 'verify_otp.html')


@csrf_protect
def reset_password_logic(request):
    if request.method == "POST":
        user_otp = request.POST.get('otp')
        new_pass = request.POST.get('new_password')
        confirm_pass = request.POST.get('confirm_password')
        stored_otp = request.session.get('reset_otp')
        stored_email = request.session.get('reset_email')

        if stored_otp and str(user_otp) == str(stored_otp):
            if new_pass == confirm_pass:
                try:
                    user = User.objects.get(email=stored_email)
                    user.set_password(new_pass)
                    user.save()
                    del request.session['reset_otp']
                    del request.session['reset_email']
                    return JsonResponse({'status': 'success', 'message': 'Password updated!'})
                except Exception:
                    return JsonResponse({'status': 'error', 'message': 'Database error.'})
            return JsonResponse({'status': 'error', 'message': 'Passwords do not match.'})
        return JsonResponse({'status': 'error', 'message': 'Invalid OTP.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})


# ═══════════════════════════════════════
# 3. PROFILE & ASSESSMENT
# ═══════════════════════════════════════
@login_required
def profile_view(request):
    return render(request, 'proinfo.html')


@csrf_exempt
@login_required
def update_profile(request):
    if request.method == 'POST':
        pref, _ = UserPreference.objects.get_or_create(user=request.user)
        pref.language = request.POST.get('language')
        pref.level = request.POST.get('skill')
        pref.save()
        return JsonResponse({'status': 'success', 'redirect_url': '/assessment/'})


@login_required
def assessment_view(request):
    pref, _ = UserPreference.objects.get_or_create(user=request.user)
    questions = Question.objects.filter(language=pref.language, level=pref.level).order_by('?')[:20]
    return render(request, 'assessment.html', {
        'language': pref.language,
        'level': pref.level,
        'questions': questions
    })


@csrf_exempt
@login_required
def submit_test(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        pref, _ = UserPreference.objects.get_or_create(user=request.user)
        pref.last_score = data.get('score')
        pref.save()
        return JsonResponse({'status': 'success', 'redirect_url': '/dashboard/'})


# ═══════════════════════════════════════
# 4. HOME & DASHBOARD
# ═══════════════════════════════════════
@login_required
def home_view(request):
    pref, _ = UserPreference.objects.get_or_create(user=request.user)
    return render(request, 'basic.html', {
        'username': request.user.first_name or request.user.username,
        'language': pref.language or "Not Selected",
        'score': pref.last_score or 0
    })


@login_required
def dashboard_view(request):
    pref, _ = UserPreference.objects.get_or_create(user=request.user)
    today = date.today()
    score = pref.last_score or 0

    # Check if streak broke because they missed yesterday
    last_act = UserActivity.objects.filter(user=request.user, task_completed=True).order_by('-date').first()
    if not last_act or last_act.date < today - timedelta(days=1):
        pref.streak = 0
        
    pref.last_login_date = today
    pref.save()

    # Heatmap
    completed_dates = list(UserActivity.objects.filter(
        user=request.user, task_completed=True
    ).values_list('date', flat=True))
    activity_data = [{'is_done': (today - timedelta(days=i)) in completed_dates} for i in range(50, -1, -1)]

    # Roadmap
    if pref.level in ['Fresher', 'Beginner'] or not pref.level:
        titles = ['Campus Prep & Aptitude', 'Programming Fundamentals', 'Data Structures Basics', 'Mini Projects & Internships', 'Interview Prep']
        descs = ['Quantitative and Logical reasoning.', 'Mastering a core programming language.', 'Learning basic DSA concepts.', 'Building portfolio projects.', 'Mock interviews and Resume prep.']
    elif score < 50:
        titles = ["Syntax & Basics", "Logic Building", "Data Structures", "OOPs Concepts", "Final Project"]
        descs = ["Mastering variables and loops.", "Solving 50+ basic problems.", "Understanding Lists and Dicts.", "Learning Classes and Objects.", "Building a CLI application."]
    else:
        titles = ["Advanced Logic", "Algorithm Design", "Database Integration", "API Development", "Full-stack Project"]
        descs = ["Solving LeetCode medium problems.", "Big O and Optimization.", "SQL and NoSQL connectivity.", "Building RESTful services.", "Deploying a complete AI app."]

    roadmap_data = [{'title': f"Phase {i+1}: {titles[i]}", 'description': descs[i], 'week': f"Week {i+1}", 'completed': False} for i in range(5)]

    return render(request, 'dashboard.html', {
        'username': request.user.first_name or request.user.username,
        'language': pref.language or "Python",
        'score': score,
        'level': pref.level or "Beginner",
        'streak': pref.streak,
        'activity_data': activity_data,
        'roadmap': roadmap_data,
    })


# ═══════════════════════════════════════
# 5. APTITUDE SECTION
# ═══════════════════════════════════════
def aptitude_categories(request):
    return render(request, 'aptitude_categories.html')


def arithmetic_topics(request):
    return render(request, 'arithmetic_topics.html')


def logical_reasoning_topics(request):
    return render(request, 'logical_reasoning_topics.html')


def data_interpretation_topics(request):
    return render(request, 'data_interpretation_topics.html')


def verbal_reasoning_topics(request):
    return render(request, 'verbal_reasoning_topics.html')


def non_verbal_reasoning_topics(request):
    return render(request, 'non_verbal_reasoning_topics.html')


def puzzle_topics(request):
    return render(request, 'puzzle_topics.html')


def progress_view(request):
    return render(request, 'progress.html')


def topic_detail_view(request):
    topic_key = request.GET.get('topic', '').strip().lower()
    questions = []
    file_path = os.path.join(settings.BASE_DIR, 'aptitude_questions.csv')
    
    topic_map = {
        'simplification': 'Simplification', 'number_system': 'Number System', 'lcm_hcf': 'LCM & HCF',
        'averages': 'Average', 'percentages': 'Percentage', 'ratio_proportion': 'Ratio & Proportion',
        'profit_loss': 'Profit & Loss', 'si_ci': 'SI & CI', 'time_work': 'Time & Work',
        'time_distance': 'Time & Distance', 'ages': 'Problems on Ages', 'partnership': 'Partnership',
        'pc': 'P and C', 'probability': 'Probability', 'mensuration': 'Mensuration',
        'alligation': 'Alligation', 'trains': 'Train', 'boats_streams': 'Boat & Stream',
        'number_series': 'Number Series', 'alphabet_series': 'Alphabet Series',
        'alphanumeric_series': 'Alphanumeric Series', 'coding_decoding': 'Coding – Decoding (Basic pattern)',
        'blood_relations': 'Blood Relations', 'direction_sense': 'Direction Sense Test',
        'syllogism': 'Syllogism', 'venn_diagrams': 'Venn Diagrams',
        'order_ranking': 'Order & Ranking', 'linear_seating': 'Seating Arrangement (Linear)',
        'circular_seating': 'Circular Seating Arrangement', 'statement_conclusion': 'Statement & Conclusion',
        'logical_puzzles': 'Logical Puzzles (Floor / Box / Scheduling)', 'data_sufficiency': 'Data Sufficiency',
        'input_output': 'Input – Output', 'critical_reasoning': 'Critical Reasoning',
        'statement_assumption': 'Statement & Assumption / Course of Action', 'analytical_reasoning': 'Analytical Reasoning (Multiple Variables)',
        'tabular_di': 'Tabular Data Interpretation', 'bar_graph': 'Bar Graph',
        'pie_chart': 'Pie Chart', 'line_graph': 'Line Graph',
        'simple_caselet': 'Simple Caselet DI', 'percentage_di': 'Percentage-based DI',
        'multiple_bar_graph': 'Multiple Bar Graph DI', 'multiple_pie_chart': 'Multiple Pie Chart DI',
        'mixed_graph': 'Mixed Graph DI', 'ratio_di': 'Ratio-based DI',
        'average_di': 'Average-based DI', 'data_comparison': 'Data Comparison DI',
        'complex_caselet': 'Complex Caselet DI', 'missing_data': 'Missing Data DI',
        'arithmetic_di': 'Arithmetic-based DI', 'data_sufficiency_di': 'Data Sufficiency (DI)',
        'logical_di': 'Logical DI', 'advanced_mixed_di': 'Advanced Mixed DI',
        'spotting_errors': 'Spotting Errors', 'synonyms': 'Synonyms',
        'antonyms': 'Antonyms', 'spellings': 'Spellings',
        'selecting_words': 'Selecting Words', 'one_word_substitution': 'One Word Substitution',
        'sentence_formation': 'Sentence Formation', 'sentence_correction': 'Sentence Correction',
        'sentence_improvement': 'Sentence Improvement', 'completing_statements': 'Completing Statements',
        'ordering_words': 'Ordering of Words', 'ordering_sentences': 'Ordering of Sentences',
        'paragraph_formation': 'Paragraph Formation', 'cloze_test': 'Cloze Test',
        'reading_comprehension': 'Reading Comprehension', 'idioms_phrases': 'Idioms and Phrases',
        'change_of_voice': 'Change of Voice', 'change_of_speech': 'Change of Speech',
        'sudoku': 'Sudoku', 'number_puzzles': 'Number Puzzles', 'missing_letters': 'Missing Letters Puzzles',
        'picture_puzzles': 'Picture Puzzles', 'pattern_puzzles': 'Pattern Puzzles', 'odd_figure': 'Odd Figure Puzzles',
        'clock_puzzles': 'Clock Puzzles', 'calendar_puzzles': 'Calendar Puzzles', 'math_puzzles': 'Mathematical Puzzles',
        'dice_puzzles': 'Dice Puzzles', 'matchstick_puzzles': 'Matchstick Puzzles', 'grid_puzzles': 'Grid Puzzles',
        'sequence_puzzles': 'Sequence Puzzles', 'arrangement_puzzles': 'Arrangement Puzzles',
        'symbol_puzzles': 'Symbol Puzzles', 'cross_number': 'Cross Number Puzzles', 'brain_teasers': 'Brain Teaser Puzzles'
    }
    csv_topic = topic_map.get(topic_key, topic_key.replace('_', ' ').title())

    if topic_key:
        db_qs = AptitudeQuestion.objects.filter(topic__iexact=csv_topic)
        for q in db_qs:
            questions.append({
                'topic': q.topic,
                'question': q.question,
                'option_a': q.option_a,
                'option_b': q.option_b,
                'option_c': q.option_c,
                'option_d': q.option_d,
                'correct': q.correct,
                'explanation': q.explanation,
                'difficulty': q.difficulty
            })

    return render(request, 'topic_detail.html', {
        'topic_name': csv_topic,
        'topic_key': topic_key,
        'questions': questions,
    })

@login_required
def aptitude_test_view(request):
    topic_key = request.GET.get('topic', '').strip().lower()
    mode = request.GET.get('mode', 'practice')
    
    questions = []
    file_path = os.path.join(settings.BASE_DIR, 'aptitude_questions.csv')
    
    topic_map = {
        'simplification': 'Simplification', 'number_system': 'Number System', 'lcm_hcf': 'LCM & HCF',
        'averages': 'Average', 'percentages': 'Percentage', 'ratio_proportion': 'Ratio & Proportion',
        'profit_loss': 'Profit & Loss', 'si_ci': 'SI & CI', 'time_work': 'Time & Work',
        'time_distance': 'Time & Distance', 'ages': 'Problems on Ages', 'partnership': 'Partnership',
        'pc': 'P and C', 'probability': 'Probability', 'mensuration': 'Mensuration',
        'alligation': 'Alligation', 'trains': 'Train', 'boats_streams': 'Boat & Stream',
        'number_series': 'Number Series', 'alphabet_series': 'Alphabet Series',
        'alphanumeric_series': 'Alphanumeric Series', 'coding_decoding': 'Coding – Decoding (Basic pattern)',
        'blood_relations': 'Blood Relations', 'direction_sense': 'Direction Sense Test',
        'syllogism': 'Syllogism', 'venn_diagrams': 'Venn Diagrams',
        'order_ranking': 'Order & Ranking', 'linear_seating': 'Seating Arrangement (Linear)',
        'circular_seating': 'Circular Seating Arrangement', 'statement_conclusion': 'Statement & Conclusion',
        'logical_puzzles': 'Logical Puzzles (Floor / Box / Scheduling)', 'data_sufficiency': 'Data Sufficiency',
        'input_output': 'Input – Output', 'critical_reasoning': 'Critical Reasoning',
        'statement_assumption': 'Statement & Assumption / Course of Action', 'analytical_reasoning': 'Analytical Reasoning (Multiple Variables)',
        'tabular_di': 'Tabular Data Interpretation', 'bar_graph': 'Bar Graph',
        'pie_chart': 'Pie Chart', 'line_graph': 'Line Graph',
        'simple_caselet': 'Simple Caselet DI', 'percentage_di': 'Percentage-based DI',
        'multiple_bar_graph': 'Multiple Bar Graph DI', 'multiple_pie_chart': 'Multiple Pie Chart DI',
        'mixed_graph': 'Mixed Graph DI', 'ratio_di': 'Ratio-based DI',
        'average_di': 'Average-based DI', 'data_comparison': 'Data Comparison DI',
        'complex_caselet': 'Complex Caselet DI', 'missing_data': 'Missing Data DI',
        'arithmetic_di': 'Arithmetic-based DI', 'data_sufficiency_di': 'Data Sufficiency (DI)',
        'logical_di': 'Logical DI', 'advanced_mixed_di': 'Advanced Mixed DI',
        'spotting_errors': 'Spotting Errors', 'synonyms': 'Synonyms',
        'antonyms': 'Antonyms', 'spellings': 'Spellings',
        'selecting_words': 'Selecting Words', 'one_word_substitution': 'One Word Substitution',
        'sentence_formation': 'Sentence Formation', 'sentence_correction': 'Sentence Correction',
        'sentence_improvement': 'Sentence Improvement', 'completing_statements': 'Completing Statements',
        'ordering_words': 'Ordering of Words', 'ordering_sentences': 'Ordering of Sentences',
        'paragraph_formation': 'Paragraph Formation', 'cloze_test': 'Cloze Test',
        'reading_comprehension': 'Reading Comprehension', 'idioms_phrases': 'Idioms and Phrases',
        'change_of_voice': 'Change of Voice', 'change_of_speech': 'Change of Speech',
        'nv_series': 'Non-Verbal Series', 'nv_analogy': 'Non-Verbal Analogy',
        'nv_classification': 'Non-Verbal Classification', 'nv_mirror_images': 'Mirror Images',
        'nv_water_images': 'Water Images', 'nv_embedded_images': 'Embedded Images',
        'nv_figure_matrix': 'Figure Matrix', 'nv_pattern_completion': 'Pattern Completion',
        'nv_paper_folding': 'Paper Folding', 'nv_paper_cutting': 'Paper Cutting',
        'nv_grouping_images': 'Grouping of Images', 'nv_shape_construction': 'Shape Construction',
        'nv_cubes_dice': 'Cubes and Dice', 'nv_analytical_reasoning': 'Analytical Reasoning (Non-Verbal)',
        'nv_rule_detection': 'Rule Detection', 'nv_dot_situation': 'Dot Situation',
        'nv_image_analysis': 'Image Analysis', 'nv_figure_matrix_problems': 'Figure Matrix Problems',
        'sudoku': 'Sudoku', 'number_puzzles': 'Number Puzzles', 'missing_letters': 'Missing Letters Puzzles',
        'picture_puzzles': 'Picture Puzzles', 'pattern_puzzles': 'Pattern Puzzles', 'odd_figure': 'Odd Figure Puzzles',
        'clock_puzzles': 'Clock Puzzles', 'calendar_puzzles': 'Calendar Puzzles', 'math_puzzles': 'Mathematical Puzzles',
        'dice_puzzles': 'Dice Puzzles', 'matchstick_puzzles': 'Matchstick Puzzles', 'grid_puzzles': 'Grid Puzzles',
        'sequence_puzzles': 'Sequence Puzzles', 'arrangement_puzzles': 'Arrangement Puzzles',
        'symbol_puzzles': 'Symbol Puzzles', 'cross_number': 'Cross Number Puzzles', 'brain_teasers': 'Brain Teaser Puzzles'
    }
    
    csv_topic = topic_map.get(topic_key, topic_key.replace('_', ' ').title())
    
    if topic_key:
        all_qs = list(AptitudeQuestion.objects.filter(topic__iexact=csv_topic))
        random.shuffle(all_qs)
        
        for idx, row in enumerate(all_qs[:20]):
            correct_opt_letter = row.correct.strip().lower()
            if correct_opt_letter == 'a': correct_val = row.option_a
            elif correct_opt_letter == 'b': correct_val = row.option_b
            elif correct_opt_letter == 'c': correct_val = row.option_c
            elif correct_opt_letter == 'd': correct_val = row.option_d
            else: correct_val = row.correct
                
            questions.append({
                'id': f"q_{idx}",
                'question_text': row.question,
                'option1': row.option_a,
                'option2': row.option_b,
                'option3': row.option_c,
                'option4': row.option_d,
                'correct_answer': correct_val,
                'explanation': row.explanation
            })

    return render(request, 'aptitude_assessment.html', {
        'language': 'Aptitude',
        'level': csv_topic,
        'topic_key': topic_key,
        'mode': mode,
        'questions': questions
    })


# ═══════════════════════════════════════
# 6. AI MENTOR & MOCK INTERVIEW
# ═══════════════════════════════════════
INTERVIEWER_SYSTEM_PROMPT = """You are Priya, a Senior HR Manager conducting a real technical screening interview. You are a human, not a chatbot. You ONLY ASK QUESTIONS — you NEVER explain concepts, never give answers, never teach, never correct answers with explanations.

══════════════════════════════════════════
CRITICAL RULES — NEVER BREAK THESE:
══════════════════════════════════════════
1. YOU ONLY ASK QUESTIONS. Period. Never explain, never answer, never teach.
2. ONE question per response. Always.
3. DETECT THE ROLE from the resume filename/content and ask ONLY role-specific questions.
4. NEVER ask about skills NOT in their domain. 
5. NEVER repeat a question already asked.
6. NEVER break character. You are Priya. Always.
7. If answer is short: ask "Could you elaborate more on that?"
8. If answer is off-topic: say "Let me bring us back — I was asking about [X]." then re-ask.
9. React warmly but briefly: "Got it, thanks!" / "Interesting!" / "Okay, great." — then move to next question.
10. DO NOT give hints, do not answer for them, do not explain what the correct answer is.

PHASES: Intro -> Technical (5 Qs) -> Project Deep Dive (3 Qs) -> Coding Challenge -> Wrap Up.
Output format: === MOCK INTERVIEW RESULTS === ... === END ==="""


@login_required
def mock_interview_view(request):
    resume_name = request.GET.get('resume', 'Resume')
    pref, _ = UserPreference.objects.get_or_create(user=request.user)
    request.session['interview_history'] = []

    # Detect role from resume filename
    fname = resume_name.lower()
    if any(k in fname for k in ['java', 'spring', 'fullstack']):
        detected_role = 'Java Fullstack Developer'
    elif any(k in fname for k in ['data_analyst', 'sql', 'tableau']):
        detected_role = 'Data Analyst'
    elif any(k in fname for k in ['ml', 'machine_learning', 'ai', 'data_science']):
        detected_role = 'Machine Learning / Data Science'
    elif any(k in fname for k in ['react', 'frontend', 'angular']):
        detected_role = 'Frontend Developer'
    elif any(k in fname for k in ['devops', 'cloud', 'docker']):
        detected_role = 'DevOps / Cloud Engineer'
    elif any(k in fname for k in ['android', 'mobile', 'kotlin']):
        detected_role = 'Mobile Developer'
    elif any(k in fname for k in ['python', 'django', 'flask']):
        detected_role = 'Python / Django Developer'
    else:
        detected_role = 'Software Developer (General)'

    return render(request, 'mock_interview.html', {
        'username': request.user.first_name or request.user.username,
        'resume_name': resume_name,
        'detected_role': detected_role,
        'language': pref.language or 'Python',
    })


@csrf_exempt
@login_required
def interview_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()
            resume_name = data.get("resume_name", "Resume")
            action = data.get("action", "chat")
            history = request.session.get('interview_history', [])

            if action == "start":
                history = []
                role = data.get("detected_role", "Software Developer")
                user_message = f"START INTERVIEW. Role: {role}. Resume: {resume_name}. Begin opening."

            if not user_message:
                return JsonResponse({"error": "Empty message"}, status=400)

            messages = [{"role": "system", "content": INTERVIEWER_SYSTEM_PROMPT}]
            for h in history:
                messages.append(h)
            messages.append({"role": "user", "content": user_message})

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                temperature=0.75,
                max_tokens=800
            )
            ai_reply = response.choices[0].message.content

            history.append({"role": "user", "content": user_message})
            history.append({"role": "assistant", "content": ai_reply})
            if len(history) > 20: history = history[-20:]
            request.session['interview_history'] = history
            request.session.modified = True

            return JsonResponse({"response": ai_reply})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"status": "Invalid request"}, status=400)


@csrf_exempt
@login_required
def ai_mentor_chat(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_query = data.get("message")
            if not user_query:
                return JsonResponse({"error": "Empty message"}, status=400)
            user_name = request.user.first_name or request.user.username if request.user.is_authenticated else "Guest"
            # Allow optional custom system prompt (used by AI Video Tutor for JSON responses)
            custom_system = data.get("system", "")
            system_prompt = custom_system if custom_system else f"You are a helpful AI Mentor for {user_name}. Use bullet points. Keep answers short."
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_query}
                ],
                temperature=0.7,
                max_tokens=1200
            )
            return JsonResponse({"response": response.choices[0].message.content})
        except Exception as e:
            import traceback
            print("AI Chat Error:", traceback.format_exc())
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"status": "Invalid request"}, status=400)


@csrf_exempt
def ai_video_tutor_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            system_prompt = data.get("system", "")
            user_prompt = data.get("user", "")

            if not system_prompt or not user_prompt:
                return JsonResponse({"error": "Missing prompts"}, status=400)

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,
                max_tokens=3500
            )
            reply = response.choices[0].message.content
            return JsonResponse({"response": reply})
        except Exception as e:
            import traceback
            print("AI Video Tutor Error:", traceback.format_exc())
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"status": "Invalid request"}, status=400)


@csrf_exempt
def run_python_code(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            code = data.get("code", "")
            f = io.StringIO()
            with redirect_stdout(f):
                try:
                    exec(code, {})
                    output = f.getvalue()
                    error = ""
                except Exception as eval_err:
                    output = f.getvalue()
                    error = str(eval_err)
            return JsonResponse({"output": output, "error": error})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"status": "Invalid request"}, status=400)


@login_required
def roadmap_view(request, track_name):
    return render(request, 'roadmap.html', {'track_name': track_name.lower()})


def coding_problems_view(request):
    return render(request, 'coding_problems.html')


def problem_solve_view(request):
    return render(request, 'problem_solve.html')


@login_required
def jobs_view(request):
    return render(request, 'jobs.html')


@login_required
def job_apply_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        linkedin = request.POST.get('linkedin', '')
        job_title = request.POST.get('job_title', 'Unknown Role')
        company = request.POST.get('company', 'Unknown Company')

        JobApplication.objects.create(
            user=request.user,
            full_name=full_name,
            email=email,
            phone=phone,
            linkedin=linkedin,
            job_title=job_title,
            company=company
        )
        return JsonResponse({'status': 'success', 'message': 'Application saved!'})
    return render(request, 'job_apply.html')


def fetch_jobs_api(request):
    cached_jobs = cache.get('rapidapi_jsearch_jobs_v4')
    if cached_jobs: return JsonResponse({'jobs': cached_jobs})

    jobs = []
    try:
        url = "https://jsearch.p.rapidapi.com/search"
        querystring = {"query": "software developer in India", "page": "1", "num_pages": "2", "date_posted": "week"}
        headers = {
            "x-rapidapi-key": "1ea4acd95amsh88abded3bc4c7f9p1b588ajsn4d37aff0b984",
            "x-rapidapi-host": "jsearch.p.rapidapi.com"
        }
        res = requests.get(url, headers=headers, params=querystring, timeout=15)
        if res.status_code == 200:
            data = res.json().get('data', [])
            for job in data:
                date_str = job.get('job_posted_at_datetime_utc', date.today().strftime('%Y-%m-%d'))[:10]
                jobs.append({
                    'title': job.get('job_title', 'Software Developer'),
                    'company': job.get('employer_name', 'Tech Company'),
                    'type': job.get('job_employment_type', 'Full-Time').replace('_', ' ').title(),
                    'desc': str(job.get('job_description', ''))[:200] + '...',
                    'link': job.get('job_apply_link') or job.get('job_google_link'),
                    'date': date_str,
                    'location': f"{job.get('job_city', '')}, {job.get('job_country', 'India')}".strip(', ').strip(),
                    'salary': 'Competitive',
                    'tags': [job.get('job_employment_type')]
                })
    except Exception: pass

    if jobs: cache.set('rapidapi_jsearch_jobs_v4', jobs, 3600)
    return JsonResponse({'jobs': jobs[:30]})


def developer_roles_view(request):
    roles = []
    for slug, data in DEVELOPER_ROADMAPS.items():
        icons = {'frontend-developer': 'fa-laptop-code', 'backend-developer': 'fa-server', 'full-stack-developer': 'fa-layer-group'}
        icon = icons.get(slug, 'fa-code')
        techs = []
        for p in data['phases']:
            techs.extend(p['topics'])
            if len(techs) > 5: break
        roles.append({'name': data['name'], 'slug': slug, 'icon': icon, 'tech': techs[:6]})
    return render(request, 'developer_roles.html', {'roles': roles})


def detailed_roadmap_view(request, role_slug):
    role_data = DEVELOPER_ROADMAPS.get(role_slug)
    if not role_data: return redirect('developer_roles')
    return render(request, 'detailed_roadmap.html', {'role': role_data, 'phases': role_data['phases']})


@login_required(login_url='login')
def skill_test_instructions_view(request, category):
    return render(request, 'skill_test_instructions.html', {'category': category.lower(), 'category_display': category.capitalize()})


@login_required(login_url='login')
def skill_tests_hub_view(request):
    return render(request, 'skill_tests_hub.html')


@login_required(login_url='login')
def comprehensive_test_view(request, category):
    mcqs = []
    category_lower = category.lower()
    
    # Defaults
    num_mcqs = 35
    num_coding = 5
    is_sql = False
    is_js = False
    is_dsa = False
    
    if category_lower == 'aptitude':
        num_mcqs = 40
        num_coding = 0
    elif category_lower == 'dsa':
        num_mcqs = 30
        num_coding = 10
        is_dsa = True
    elif category_lower == 'javascript':
        is_js = True
    elif category_lower == 'sql':
        is_sql = True
        
    if category_lower == 'aptitude':
        all_mcqs = list(AptitudeQuestion.objects.all())
        random.shuffle(all_mcqs)
        mcqs = all_mcqs[:num_mcqs]
        for q in mcqs:
            opts = [('A', q.option_a), ('B', q.option_b), ('C', q.option_c), ('D', q.option_d)]
            random.shuffle(opts)
            q.shuffled_options = opts
        is_aptitude = True
    else:
        mapping = {'python': 'Python', 'java': 'Java', 'c': 'C', 'cpp': 'C++', 'dsa': 'DSA', 'csharp': 'C#', 'sql': 'SQL', 'javascript': 'JavaScript'}
        db_lang = mapping.get(category_lower, category.capitalize())
        all_mcqs = list(Question.objects.filter(language__iexact=db_lang))
        random.shuffle(all_mcqs)
        mcqs = all_mcqs[:num_mcqs]
        for q in mcqs:
            opts = [(q.option1, q.option1), (q.option2, q.option2), (q.option3, q.option3), (q.option4, q.option4)]
            opts = [o for o in opts if o[1] and str(o[1]).strip() != "None"]
            random.shuffle(opts)
            q.shuffled_options = opts
        is_aptitude = False

    return render(request, 'comprehensive_test.html', {
        'category': category_lower, 
        'category_display': category.capitalize(), 
        'mcqs': mcqs, 
        'is_aptitude': is_aptitude,
        'num_coding': num_coding,
        'is_sql': is_sql,
        'is_js': is_js,
        'is_dsa': is_dsa
    })


@login_required(login_url='login')
def submit_comprehensive_test(request):
    if request.method == 'POST':
        category = request.POST.get('category', '')
        score = request.POST.get('total_score', '0')
        
        try:
            score_val = int(score)
        except ValueError:
            score_val = 0
            
        if score_val > 45:
            messages.success(request, f'Assessment for {category.upper()} submitted! Score: {score}. Certificate Unlocked!')
            request.session['cert_category'] = category
            request.session['cert_score'] = score
            return redirect('certificate_view')
        else:
            messages.warning(request, f'Score: {score}. You need a score above 45 to earn the certificate. Please practice more and retake the test!')
            return redirect('skill_tests_hub')
            
    return redirect('skill_tests_hub')

@login_required(login_url='login')
def certificate_view(request):
    category = request.session.get('cert_category', 'General Skills')
    score = request.session.get('cert_score', '100')
    return render(request, 'certificate.html', {'category': category, 'score': score})


@csrf_exempt
@login_required
def update_streak_api(request):
    if request.method == "POST":
        try:
            today = date.today()
            activity, created = UserActivity.objects.get_or_create(user=request.user, date=today, defaults={'task_completed': True})
            if not activity.task_completed:
                activity.task_completed = True
                activity.save()
            pref, _ = UserPreference.objects.get_or_create(user=request.user)
            streak_updated = False
            if created:
                yesterday = today - timedelta(days=1)
                had_yesterday = UserActivity.objects.filter(user=request.user, date=yesterday, task_completed=True).exists()
                pref.streak = (pref.streak + 1) if had_yesterday else 1
                pref.save()
                streak_updated = True
            return JsonResponse({"status": "success", "streak": pref.streak, "streak_updated": streak_updated})
        except Exception as e: return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"status": "Invalid request"}, status=400)

from django.core.serializers import deserialize
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def load_data_view(request):
    if request.method == "POST":
        try:
            objects = deserialize("json", request.body)
            for obj in objects:
                obj.save()
            return JsonResponse({"status": "success", "message": "Data loaded successfully!"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return HttpResponse("Send a POST request with JSON dump data.")
