import os

VIEWS_FILE = r'core\views.py'

NEW_VIEWS = """

# ==============================================================================
# COMPREHENSIVE SKILL ASSESSMENT HUB
# ==============================================================================

@login_required(login_url='login')
def skill_tests_hub_view(request):
    # Renders the selection hub for multiple languages + aptitude
    return render(request, 'skill_tests_hub.html')

@login_required(login_url='login')
def comprehensive_test_view(request, category):
    import random
    
    mcqs = []
    category_lower = category.lower()
    
    if category_lower == 'aptitude':
        # Fetch 40 Aptitude MCQs
        all_mcqs = list(AptitudeQuestion.objects.all())
        random.shuffle(all_mcqs)
        mcqs = all_mcqs[:40]
        is_aptitude = True
    else:
        # Fetch 35 MCQs for the specific language
        # Match casing safely, assuming DB has 'Python', 'Java', 'C', 'C++', 'C#'
        mapping = {
            'python': 'Python', 'java': 'Java', 'c': 'C', 
            'cpp': 'C++', 'csharp': 'C#'
        }
        db_lang = mapping.get(category_lower, category.capitalize())
        all_mcqs = list(Question.objects.filter(language__iexact=db_lang))
        random.shuffle(all_mcqs)
        mcqs = all_mcqs[:35]
        is_aptitude = False

    context = {
        'category': category_lower,
        'category_display': category.capitalize(),
        'mcqs': mcqs,
        'is_aptitude': is_aptitude,
    }
    return render(request, 'comprehensive_test.html', context)

@login_required(login_url='login')
def submit_comprehensive_test(request):
    if request.method == 'POST':
        category = request.POST.get('category', '')
        score = request.POST.get('total_score', '0')
        messages.success(request, f'Assessment for {category.upper()} submitted successfully! You scored {score}.')
        return redirect('skill_tests_hub')
    return redirect('skill_tests_hub')

"""

with open(VIEWS_FILE, 'a', encoding='utf-8') as f:
    f.write(NEW_VIEWS)

print("Successfully appended comprehensive views.")
