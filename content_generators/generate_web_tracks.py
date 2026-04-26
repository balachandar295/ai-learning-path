import json
import os

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
json_start = text.find('{')
data = json.loads(text[json_start:text.rfind('}')+1])

def card(label, code):
    return f"<div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'><div style='background:linear-gradient(to right,#0ea5e9,#3b82f6);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>{label}</div><pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>{code}</pre></div>"

def section(title, desc, examples):
    h = f"<h4 style='color:#0ea5e9;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #0ea5e9;padding-left:12px;'>{title}</h4>"
    h += f"<p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>{desc}</p>"
    for lbl, code in examples: h += card(lbl, code)
    return h

def explanation(title, sections):
    h = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections: h += section(*s)
    return h + "</div>"

def quiz(items): return [{"q":q,"options":o,"answer":a} for q,o,a in items]
def task(t,d,h,c): return {"title":t,"description":d,"hint":h,"code":c}
def problems(items): return [{"title":t,"description":d,"code":c} for t,d,c in items]

# =====================================================================
# HTML TRACK - 18 Topics
# =====================================================================
html_nodes_raw = [
    ("html_basics", "HTML Basics", 1),
    ("html_text", "Text Formatting", 1),
    ("html_links", "Links & Nav", 1),
    ("html_images", "Images", 1),
    ("html_lists", "Lists", 1),
    ("html_tables", "Tables", 2),
    ("html_forms", "Forms & Inputs", 2),
    ("html_semantic", "Semantic HTML", 2),
    ("html_media", "Audio & Video", 2),
    ("html_meta", "Attributes & Meta", 3),
    ("html_iframe", "iFrames", 3),
    ("html_canvas", "Canvas & SVG", 3),
    ("html_api", "HTML5 APIs", 3),
    ("html_a11y", "Accessibility", 4),
    ("html_seo", "SEO Basics", 4),
    ("html_responsive", "Viewport", 4),
    ("html_practices", "Best Practices", 4),
    ("html_interview", "Interview Guide", 5),
]

html_nodes = []
for i, (nid, title, phase) in enumerate(html_nodes_raw):
    node = {"id": nid, "title": title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase}
    if i > 0: node["parent"] = html_nodes_raw[i-1][0]
    html_nodes.append(node)

html_content = {}
html_content["html_basics"] = {
    "title": "HTML Basics",
    "explanation": explanation("HTML Basics", [
        ("What is HTML?", "HTML stands for HyperText Markup Language. It's the standard language for creating webpages.", [("Basic Structure", "<!DOCTYPE html>\n<html>\n<head>\n    <title>Page Title</title>\n</head>\n<body>\n    <h1>My First Heading</h1>\n    <p>My first paragraph.</p>\n</body>\n</html>")])
    ]),
    "examples": [],
    "concept_quiz": quiz([("What does HTML stand for?", ["HyperText Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "None of these"], "HyperText Markup Language")]),
    "hands_on": task("Create a Header", "Write an h1 header tag with 'Hello World'.", "Use <h1> element.", "<h1>Hello World</h1>"),
    "problem_solving": problems([("Fix the tag", "Fix the unclosed tag: <p>Hello", "<p>Hello</p>")])
}

for nid, title, phase in html_nodes_raw[1:]:
    code = f"<!-- Auto-generated {title} example -->\n<div>{title}</div>"
    html_content[nid] = {
        "title": title,
        "explanation": explanation(title, [
            (f"Understanding {title}", f"{title} is a core concept in modern HTML.", [(f"{title} Example", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([(f"What is {title} used for?", ["Web structure", "Backend logic", "Database management", "Styling"], "Web structure")]),
        "hands_on": task(f"Practice {title}", f"Write valid HTML for {title}.", "Follow HTML syntax.", code),
        "problem_solving": problems([(f"{title} Problem", f"Create a webpage element using {title}.", code)])
    }

# =====================================================================
# CSS TRACK - 18 Topics
# =====================================================================
css_nodes_raw = [
    ("css_basics", "CSS Basics", 1),
    ("css_selectors", "Selectors", 1),
    ("css_colors", "Colors & Backgrounds", 1),
    ("css_box", "Box Model", 1),
    ("css_text", "Typography", 1),
    ("css_float", "Position & Float", 2),
    ("css_flex", "Flexbox", 2),
    ("css_grid", "CSS Grid", 2),
    ("css_responsive", "Media Queries", 2),
    ("css_pseudo", "Pseudo-classes", 3),
    ("css_shadows", "Shadows & Gradients", 3),
    ("css_vars", "CSS Variables", 3),
    ("css_transitions", "Transitions", 3),
    ("css_animations", "Animations", 4),
    ("css_transforms", "Transforms", 4),
    ("css_zindex", "Z-Index", 4),
    ("css_optimization", "Optimization", 4),
    ("css_interview", "Interview Guide", 5),
]

css_nodes = []
for i, (nid, title, phase) in enumerate(css_nodes_raw):
    node = {"id": nid, "title": title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase}
    if i > 0: node["parent"] = css_nodes_raw[i-1][0]
    css_nodes.append(node)

css_content = {}
css_content["css_basics"] = {
    "title": "CSS Basics",
    "explanation": explanation("CSS Basics", [
        ("What is CSS?", "CSS stands for Cascading Style Sheets. It describes how HTML elements should be displayed.", [("CSS Anatomy", "selector {\n    property: value;\n}\n\nh1 {\n    color: blue;\n    text-align: center;\n}")])
    ]),
    "examples": [],
    "concept_quiz": quiz([("What does CSS stand for?", ["Cascading Style Sheets", "Computer Style Sheets", "Colorful Style Sheets", "Creative Style Sheets"], "Cascading Style Sheets")]),
    "hands_on": task("Style a Paragraph", "Make all <p> text red.", "Target 'p' and use color: red.", "p {\n    color: red;\n}"),
    "problem_solving": problems([("Center Text", "Center the text of an <h1> element.", "h1 {\n    text-align: center;\n}")])
}

for nid, title, phase in css_nodes_raw[1:]:
    code = f"/* Auto-generated {title} Example */\n.element {{\n    /* CSS properties below */\n}}"
    css_content[nid] = {
        "title": title,
        "explanation": explanation(title, [
            (f"Understanding {title}", f"{title} is crucial for styling beautiful web pages.", [(f"{title} Example", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([(f"Which applies to {title}?", ["Styling", "Data processing", "Database", "Routing"], "Styling")]),
        "hands_on": task(f"Practice {title}", f"Write valid CSS for {title}.", "Follow CSS syntax.", code),
        "problem_solving": problems([(f"{title} Problem", f"Style an element using {title}.", code)])
    }

# =====================================================================
# DJANGO TRACK - 18 Topics
# =====================================================================
django_nodes_raw = [
    ("django_basics", "Django Setup", 1),
    ("django_apps", "Apps Structure", 1),
    ("django_urls", "URLs & Routing", 1),
    ("django_views", "Views", 1),
    ("django_templates", "Templates", 1),
    ("django_models", "Models & ORM", 2),
    ("django_admin", "Admin Panel", 2),
    ("django_forms", "Forms", 2),
    ("django_modelforms", "ModelForms", 2),
    ("django_auth", "Authentication", 3),
    ("django_cbv", "Class-Based Views", 3),
    ("django_static", "Static & Media", 3),
    ("django_middleware", "Middleware", 3),
    ("django_drf", "REST API", 4),
    ("django_testing", "Testing", 4),
    ("django_security", "Security", 4),
    ("django_deploy", "Deployment", 4),
    ("django_interview", "Interview Guide", 5),
]

django_nodes = []
for i, (nid, title, phase) in enumerate(django_nodes_raw):
    node = {"id": nid, "title": title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase}
    if i > 0: node["parent"] = django_nodes_raw[i-1][0]
    django_nodes.append(node)

django_content = {}
django_content["django_basics"] = {
    "title": "Django Setup",
    "explanation": explanation("Django Setup", [
        ("What is Django?", "Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.", [("Install & Project", "pip install django\n\ndjango-admin startproject myproject\ncd myproject\npython manage.py runserver")])
    ]),
    "examples": [],
    "concept_quiz": quiz([("What is Django written in?", ["Python", "JavaScript", "C++", "Java"], "Python")]),
    "hands_on": task("Start a Project", "Command to start a Django project named 'core'.", "Use django-admin.", "django-admin startproject core"),
    "problem_solving": problems([("Run Server", "Command to run the local server.", "python manage.py runserver")])
}

for nid, title, phase in django_nodes_raw[1:]:
    code = f"# Auto-generated {title} example\n# Python code for {title}\npass"
    django_content[nid] = {
        "title": title,
        "explanation": explanation(title, [
            (f"Understanding {title}", f"{title} is a core concept in the Django framework.", [(f"{title} Example", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([(f"What is {title} used for in Django?", ["Web development", "Machine Learning", "OS management", "None"], "Web development")]),
        "hands_on": task(f"Practice {title}", f"Write Django code for {title}.", "Follow Python & Django syntax.", code),
        "problem_solving": problems([(f"{title} Problem", f"Solve a backend scenario using {title}.", code)])
    }

# =====================================================================
# INJECT DATA
# =====================================================================

data['html'] = {
    "title": "HTML - Web Structure",
    "description": "Learn the standard markup language for documents designed to be displayed in a web browser.",
    "nodes": html_nodes,
    "content": html_content
}

data['css'] = {
    "title": "CSS - Web Styling",
    "description": "Master Cascading Style Sheets to style and layout beautiful web pages.",
    "nodes": css_nodes,
    "content": css_content
}

data['django'] = {
    "title": "Django - Python Web Framework",
    "description": "Build high-performing, elegant web applications quickly using Django.",
    "nodes": django_nodes,
    "content": django_content
}

new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"HTML, CSS, Django tracks injected successfully!")
