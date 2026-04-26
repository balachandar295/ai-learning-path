import os
import re

base_dir = r"c:\Users\ELCOT\Desktop\final_yr_project - Copy"

# 1. Update arithmetic_topics.html
file_path = os.path.join(base_dir, 'core', 'templates', 'arithmetic_topics.html')
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Topics in order of appearance in HTML
topics_keys = [
    'simplification', 'number_system', 'lcm_hcf', 'averages', 'percentages', 'ratio_proportion',
    'profit_loss', 'si_ci', 'time_work', 'time_distance', 'ages', 'partnership',
    'pc', 'probability', 'mensuration', 'alligation', 'trains', 'boats_streams'
]

# We need to replace the action-group divs.
# The regex finds <div class="topic-card"> ... <div class="action-group">...</div> </div>
# But it's easier to just find all <div class="action-group">...</div> and replace them in order.

action_group_pattern = re.compile(r'<div class="action-group">.*?</div>', re.DOTALL)
matches = action_group_pattern.findall(html)

if len(matches) == 18:
    for i in range(18):
        key = topics_keys[i]
        new_action_group = f'''<div class="action-group">
    <a href="{{% url 'topic_detail' %}}?topic={key}" class="btn btn-learn"><i class="fas fa-graduation-cap"></i> Learn</a>
    <a href="{{% url 'aptitude_test_view' %}}?topic={key}&mode=practice" class="btn btn-practice">Practice</a>
    <a href="{{% url 'aptitude_test_view' %}}?topic={key}&mode=test" class="btn btn-test">Test</a>
</div>'''
        html = html.replace(matches[i], new_action_group, 1)

    # Also fix the progress bars to load from localStorage using the new format
    # Instead of progress bar script logic for local storage at the bottom, we might not need to touch it if progress.html is what matters.
    # Actually, arithmetic_topics.html has a script at the bottom: saveProgress(topicName, percentage)...
    # Let's replace the script at the bottom of arithmetic_topics.html with proper fetching logic
    script_fix = """<script>
    document.addEventListener('DOMContentLoaded', () => {
        const topicKeys = ['simplification', 'number_system', 'lcm_hcf', 'averages', 'percentages', 'ratio_proportion', 'profit_loss', 'si_ci', 'time_work', 'time_distance', 'ages', 'partnership', 'pc', 'probability', 'mensuration', 'alligation', 'trains', 'boats_streams'];
        const progressFills = document.querySelectorAll('.progress-fill');
        const progressLabels = document.querySelectorAll('.progress-label span:nth-child(2)');
        
        topicKeys.forEach((key, index) => {
            const progress = localStorage.getItem('aptitude_progress_' + key) || 0;
            if (progressFills[index]) {
                progressFills[index].style.width = progress + '%';
            }
            if (progressLabels[index]) {
                progressLabels[index].innerText = progress + '%';
            }
        });
    });
</script>"""
    html = re.sub(r'<script>\s*function saveProgress.*?<\/script>', script_fix, html, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("arithmetic_topics.html updated!")
else:
    print(f"Error: Found {len(matches)} action groups instead of 18")

# 2. Update views.py for topic_detail_view to use topic_map
views_path = os.path.join(base_dir, 'core', 'views.py')
with open(views_path, 'r', encoding='utf-8') as f:
    views_content = f.read()

topic_detail_replacement = """def topic_detail_view(request):
    topic_key = request.GET.get('topic', '').strip().lower()
    questions = []
    file_path = os.path.join(settings.BASE_DIR, 'aptitude_questions.csv')
    
    topic_map = {
        'simplification': 'Simplification', 'number_system': 'Number System', 'lcm_hcf': 'LCM & HCF',
        'averages': 'Average', 'percentages': 'Percentage', 'ratio_proportion': 'Ratio & Proportion',
        'profit_loss': 'Profit & Loss', 'si_ci': 'SI & CI', 'time_work': 'Time & Work',
        'time_distance': 'Time & Distance', 'ages': 'Problems on Ages', 'partnership': 'Partnership',
        'pc': 'P and C', 'probability': 'Probability', 'mensuration': 'Mensuration',
        'alligation': 'Alligation', 'trains': 'Train', 'boats_streams': 'Boat & Stream'
    }
    csv_topic = topic_map.get(topic_key, topic_key.replace('_', ' ').title())

    if topic_key:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['topic'].strip().lower() == csv_topic.lower():
                        questions.append(row)
        except FileNotFoundError:
            print("aptitude_questions.csv not found!")

    return render(request, 'topic_detail.html', {
        'topic_name': csv_topic,
        'topic_key': topic_key,
        'questions': questions,
    })"""

views_content = re.sub(
    r'def topic_detail_view\(request\):.*?return render\(request, \'topic_detail\.html\',\s*{.*?}\)', 
    topic_detail_replacement, 
    views_content, 
    flags=re.DOTALL
)

with open(views_path, 'w', encoding='utf-8') as f:
    f.write(views_content)
print("views.py updated for topic_detail_view!")

# 3. Update topic_detail.html
td_path = os.path.join(base_dir, 'core', 'templates', 'topic_detail.html')
with open(td_path, 'r', encoding='utf-8') as f:
    td_html = f.read()

td_html = td_html.replace(
    '''<a href="{% url 'assessment_view' %}?topic={{ topic_name }}&mode=practice" class="practice-btn">''',
    '''<a href="{% url 'aptitude_test_view' %}?topic={{ topic_key }}&mode=practice" class="practice-btn">'''
)

td_script_replace = """function toggleComplete() {
            const isChecked = document.getElementById('mark-complete').checked;
            if(isChecked) {
                localStorage.setItem('aptitude_progress_{{ topic_key }}', 100);
                alert("Great job! Topic marked as completed.");
            }
        }"""
td_html = re.sub(r'function toggleComplete\(\).*?\}', td_script_replace, td_html, flags=re.DOTALL)

with open(td_path, 'w', encoding='utf-8') as f:
    f.write(td_html)
print("topic_detail.html updated!")

# 4. Update progress.html
# Replace entire file content for a clean, working version
progress_path = os.path.join(base_dir, 'core', 'templates', 'progress.html')

progress_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Learning Progress | AI Learning Path</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    {% load static %}
    <style>
        /* --- Base Styles --- */
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Poppins', sans-serif; }
        body { background-color: #f8fafc; color: #1e1e2f; line-height: 1.6; }
        .navbar { display: flex; justify-content: space-between; align-items: center; padding: 18px 8%; background: #1e1e2f; color: white; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        .logo { font-size: 24px; font-weight: 700; color:#00d4ff; }
        .nav-links { display: flex; align-items: center; gap: 25px; }
        .nav-links a { color: white; text-decoration: none; font-weight: 500; opacity: 0.8; transition: 0.3s; font-size: 17px; }
        .nav-links a:hover, .nav-links a.active-link { opacity: 1; color: #00d4ff; }
        .active-link { border-bottom: 2px solid #00d4ff; padding-bottom: 5px; }
        .exit-btn { color: red !important; padding: 8px 22px; border-radius: 25px; font-weight: 600 !important; opacity: 1 !important; }
        .container { max-width: 1000px; margin: 50px auto; padding: 0 20px; }
        .main-title { font-size: 32px; font-weight: 700; margin-bottom: 40px; position: relative; display: inline-block; }
        .main-title::after { content: ""; position: absolute; left: 0; bottom: -8px; width: 50%; height: 5px; background: #00d4ff; border-radius: 10px; }
        .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 25px; margin-bottom: 50px; }
        .stat-card { background: #ffffff; padding: 35px 20px; border-radius: 20px; box-shadow: 0 10px 30px rgba(0,0,0,0.04); text-align: center; border-bottom: 4px solid #6c63ff; transition: 0.3s ease; }
        .stat-card h2 { font-size: 40px; color: #1e1e2f; margin-bottom: 5px; }
        .stat-card p { color: #718096; font-size: 14px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }
        .progress-section { background: white; padding: 40px; border-radius: 24px; box-shadow: 0 10px 40px rgba(0,0,0,0.03); }
        .section-title { font-size: 22px; margin-bottom: 35px; color: #2d3748; font-weight: 700; }
        .topic-row { margin-bottom: 35px; border-radius: 15px; }
        .topic-info { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
        .topic-name { font-weight: 600; color: #1e1e2f; font-size: 16px; }
        .status-label { font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 12px; background: #edf2f7; color: #4a5568; }
        .bar-bg { width: 100%; height: 12px; background: #e2e8f0; border-radius: 20px; overflow: hidden; }
        .bar-fill { height: 100%; background: linear-gradient(90deg, #00d4ff, #6c63ff); border-radius: 20px; transition: 1.5s ease-in-out; box-shadow: 0 0 10px rgba(0, 212, 255, 0.3); }
        .percentage-text { text-align: right; font-size: 13px; margin-top: 8px; color: #718096; font-weight: 500; }
        .focus-box { margin-top: 45px; padding: 30px; background: #1e1e2f; border-radius: 20px; color: white; border-left: 6px solid #00d4ff; }
        .focus-box h3 { font-size: 18px; margin-bottom: 10px; color: #00d4ff; }
        .focus-box p { color: #cbd5e0; font-size: 15px; }
    </style>
</head>
<body>
    <nav class="navbar">
        <div class="logo">AI LEARNING PATH</div>
        <div class="nav-links">
            <a href="/dashboard/">Dashboard</a>
            <a href="{% url 'arithmetic_topics' %}">Topics</a>
            <a href="{% url 'progress_view' %}" class="active-link">Progress</a>
            <a href="{% url 'aptitude_categories' %}" class="exit-btn">Exit</a>
        </div>
    </nav>

    <div class="container">
        <h1 class="main-title">Aptitude Mastery Progress</h1>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h2 id="completed-count">0</h2>
                <p>Completed Topics</p>
            </div>
            <div class="stat-card">
                <h2 id="total-topics-count">18</h2>
                <p>Total Topics</p>
            </div>
            <div class="stat-card" style="border-bottom-color: #00d4ff;">
                <h2 id="overall-progress">0%</h2>
                <p>Overall Mastery</p>
            </div>
        </div>

        <div class="progress-section">
            <h3 class="section-title"><i class="fas fa-tasks" style="margin-right: 10px; color: #6c63ff;"></i> Topic-wise Progress</h3>
            <div id="topics-container"></div>
        </div>

        <div class="focus-box">
            <h3><i class="fas fa-lightbulb" style="margin-right: 10px;"></i> AI Recommendation</h3>
            <p id="focus-message">Keep going! Start from the basics like Simplification and Number System.</p>
        </div>
    </div>

    <script src="{% static 'data.js' %}"></script>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const container = document.getElementById('topics-container');
            let completed = 0;
            let totalProgress = 0;
            let totalTopics = 0;

            for (const key in topicsData) {
                if (topicsData.hasOwnProperty(key)) {
                    totalTopics++;
                    const topicName = topicsData[key].title;
                    const progressValue = parseInt(localStorage.getItem('aptitude_progress_' + key)) || 0;
                    
                    if (progressValue >= 100) completed++;
                    totalProgress += progressValue;

                    const row = document.createElement('div');
                    row.className = 'topic-row';
                    row.innerHTML = `
                        <div class="topic-info">
                            <span class="topic-name">${topicName}</span>
                            <span class="status-label" style="${progressValue >= 100 ? 'background:#c6f6d5; color:#22543d;' : ''}">
                                ${progressValue >= 100 ? 'Completed' : 'In Progress'}
                            </span>
                        </div>
                        <div class="bar-bg">
                            <div class="bar-fill" style="width: ${progressValue}%"></div>
                        </div>
                        <div class="percentage-text">Progress: ${progressValue}%</div>
                    `;
                    container.appendChild(row);
                }
            }

            document.getElementById('completed-count').innerText = completed;
            document.getElementById('total-topics-count').innerText = totalTopics;
            
            const overall = totalTopics > 0 ? Math.round(totalProgress / totalTopics) : 0;
            document.getElementById('overall-progress').innerText = overall + "%";

            if (overall >= 100) {
                document.getElementById('focus-message').innerText = "Excellent! You have mastered all aptitude topics.";
            } else if (overall > 50) {
                document.getElementById('focus-message').innerText = "Great progress! Keep tackling the advanced topics.";
            } else {
                document.getElementById('focus-message').innerText = "Keep going! Focus on the remaining fundamentals.";
            }
        });
    </script>
</body>
</html>"""

with open(progress_path, 'w', encoding='utf-8') as f:
    f.write(progress_html)
print("progress.html updated!")
