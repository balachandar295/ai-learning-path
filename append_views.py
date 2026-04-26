import os

EXTRA_VIEWS = '''
# ==========================================
# 25 CAREER PATHS & ROADMAPS
# ==========================================

DEVELOPER_ROLES = [
    {"name": "Frontend Developer", "slug": "frontend-developer", "tech": ["HTML", "CSS", "JavaScript", "React", "Angular", "Vue"], "icon": "fa-laptop-code"},
    {"name": "Backend Developer", "slug": "backend-developer", "tech": ["Python", "Java", "Node.js", "PHP", "Ruby", "MySQL"], "icon": "fa-server"},
    {"name": "Full-Stack Developer", "slug": "full-stack-developer", "tech": ["HTML", "CSS", "JavaScript", "Python", "Django", "SQL"], "icon": "fa-layer-group"},
    {"name": "Mobile App Developer", "slug": "mobile-app-developer", "tech": ["Kotlin", "Java", "Swift", "Flutter", "React Native"], "icon": "fa-mobile-alt"},
    {"name": "Android Developer", "slug": "android-developer", "tech": ["Kotlin", "Java", "Android Studio"], "icon": "fa-android"},
    {"name": "iOS Developer", "slug": "ios-developer", "tech": ["Swift", "Objective-C", "Xcode"], "icon": "fa-apple"},
    {"name": "Game Developer", "slug": "game-developer", "tech": ["C++", "C#", "Unity", "Unreal Engine"], "icon": "fa-gamepad"},
    {"name": "Data Scientist", "slug": "data-scientist", "tech": ["Python", "R", "Pandas", "NumPy", "SQL"], "icon": "fa-chart-pie"},
    {"name": "Machine Learning Developer", "slug": "machine-learning-developer", "tech": ["Python", "TensorFlow", "PyTorch", "Scikit-learn"], "icon": "fa-brain"},
    {"name": "AI Developer", "slug": "ai-developer", "tech": ["Python", "Deep Learning", "NLP", "Computer Vision"], "icon": "fa-robot"},
    {"name": "DevOps Engineer", "slug": "devops-engineer", "tech": ["Docker", "Kubernetes", "Jenkins", "Git"], "icon": "fa-infinity"},
    {"name": "Cloud Developer", "slug": "cloud-developer", "tech": ["AWS", "Azure", "Google Cloud", "Terraform"], "icon": "fa-cloud"},
    {"name": "Cybersecurity Developer", "slug": "cybersecurity-developer", "tech": ["Python", "Kali Linux", "Ethical Hacking Tools"], "icon": "fa-shield-alt"},
    {"name": "Blockchain Developer", "slug": "blockchain-developer", "tech": ["Solidity", "Ethereum", "Web3", "JavaScript"], "icon": "fa-link"},
    {"name": "Embedded Systems Developer", "slug": "embedded-systems-developer", "tech": ["C", "C++", "Arduino", "Raspberry Pi"], "icon": "fa-microchip"},
    {"name": "Desktop Application Developer", "slug": "desktop-application-developer", "tech": ["Python", "Java", "C#", "Electron"], "icon": "fa-desktop"},
    {"name": "AR / VR Developer", "slug": "ar-vr-developer", "tech": ["Unity", "Unreal Engine", "C#"], "icon": "fa-vr-cardboard"},
    {"name": "Database Developer", "slug": "database-developer", "tech": ["SQL", "MySQL", "PostgreSQL", "Oracle"], "icon": "fa-database"},
    {"name": "API Developer", "slug": "api-developer", "tech": ["Python (Django REST)", "Node.js", "Flask", "GraphQL"], "icon": "fa-plug"},
    {"name": "WordPress Developer", "slug": "wordpress-developer", "tech": ["PHP", "WordPress", "HTML", "CSS"], "icon": "fa-wordpress"},
    {"name": "Shopify Developer", "slug": "shopify-developer", "tech": ["Shopify", "Liquid", "JavaScript"], "icon": "fa-shopping-cart"},
    {"name": "Salesforce Developer", "slug": "salesforce-developer", "tech": ["Apex", "Lightning", "Salesforce Platform"], "icon": "fa-cloud-meatball"},
    {"name": "Automation Developer", "slug": "automation-developer", "tech": ["Python", "Selenium", "RPA Tools"], "icon": "fa-cogs"},
    {"name": "Software Engineer", "slug": "software-engineer", "tech": ["Java", "C++", "Python", "System Design"], "icon": "fa-code-branch"},
    {"name": "UI Developer", "slug": "ui-developer", "tech": ["HTML", "CSS", "JavaScript", "UI frameworks"], "icon": "fa-paint-brush"}
]

def developer_roles_view(request):
    return render(request, 'developer_roles.html', {'roles': DEVELOPER_ROLES})

def detailed_roadmap_view(request, role_slug):
    role = next((r for r in DEVELOPER_ROLES if r['slug'] == role_slug), None)
    if not role:
        return redirect('developer_roles')
    
    techs = role['tech']
    
    phases = [
        {"title": "Fundamentals", "desc": "Understand the basics of " + role['name'] + ".", "items": techs[:2] if len(techs) > 1 else techs},
        {"title": "Core Technologies", "desc": "Master the essential tools required.", "items": techs[1:4] if len(techs) > 3 else techs},
        {"title": "Advanced Frameworks", "desc": "Learn industry standard frameworks and libraries.", "items": techs[3:] if len(techs) > 3 else []},
        {"title": "Projects & Portfolio", "desc": "Build real-world applications using these technologies.", "items": ["Mini Project", "Capstone Project", "GitHub Portfolio"]},
        {"title": "Interview Preparation", "desc": "Get ready for " + role['name'] + " job interviews.", "items": ["System Design", "Data Structures", "Mock Interviews"]}
    ]
    
    return render(request, 'detailed_roadmap.html', {'role': role, 'phases': phases})
'''

with open('core/views.py', 'a', encoding='utf-8') as f:
    f.write(EXTRA_VIEWS)

print('Updated views.py successfully')
