import json

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

django_topics = [
    ("django_basics", "Django Setup", "Django is a high-level Python web framework.", "pip install django\ndjango-admin startproject myproject\ncd myproject\npython manage.py runserver"),
    ("django_apps", "Apps Structure", "Django projects are split into reusable apps.", "python manage.py startapp core\n\n# settings.py\nINSTALLED_APPS = [\n    'core',\n    ...\n]"),
    ("django_urls", "URLs & Routing", "URLconfs map URLs to specific view functions.", "from django.urls import path\nfrom . import views\n\nurlpatterns = [\n    path('home/', views.home, name='home'),\n]"),
    ("django_views", "Views", "Views process requests and return HttpResponse objects.", "from django.http import HttpResponse\n\ndef home(request):\n    return HttpResponse('Hello Django')"),
    ("django_templates", "Templates", "Dynamic HTML rendering injecting variables and logic.", "from django.shortcuts import render\n\ndef my_view(request):\n    context = {'name': 'Alice'}\n    return render(request, 'index.html', context)"),
    ("django_models", "Models & ORM", "Defining database architecture via Python classes.", "from django.db import models\n\nclass Book(models.Model):\n    title = models.CharField(max_length=200)\n    pages = models.IntegerField()\n    created = models.DateTimeField(auto_now_add=True)"),
    ("django_admin", "Admin Panel", "Auto-generated admin interface to manage database records.", "from django.contrib import admin\nfrom .models import Book\n\nadmin.site.register(Book)"),
    ("django_forms", "Forms", "Rendering forms and validating user input reliably.", "from django import forms\n\nclass ContactForm(forms.Form):\n    name = forms.CharField(max_length=100)\n    message = forms.CharField(widget=forms.Textarea)"),
    ("django_modelforms", "ModelForms", "Auto-generating forms directly based on Models.", "from django.forms import ModelForm\nfrom .models import Book\n\nclass BookForm(ModelForm):\n    class Meta:\n        model = Book\n        fields = ['title', 'pages']"),
    ("django_auth", "Authentication", "Built-in User models, handling login, logout, and permissions.", "from django.contrib.auth.decorators import login_required\n\n@login_required\ndef secure_view(request):\n    return HttpResponse('Classified Info')"),
    ("django_cbv", "Class-Based Views", "Structuring views as classes to reuse logic via inheritance.", "from django.views.generic import ListView\nfrom .models import Book\n\nclass BookListView(ListView):\n    model = Book\n    template_name = 'book_list.html'"),
    ("django_static", "Static & Media", "Serving CSS, JS, images, and user-uploaded media files.", "# settings.py\nSTATIC_URL = '/static/'\nMEDIA_URL = '/media/'\n\n# In templates:\n{% load static %}\n<img src='{% static \"logo.png\" %}' />"),
    ("django_middleware", "Middleware", "A framework of hooks into Django's request/response processing.", "class SimpleMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n\n    def __call__(self, request):\n        # Logic before view is called\n        response = self.get_response(request)\n        # Logic after view is called\n        return response"),
    ("django_drf", "REST API", "Using Django Rest Framework (DRF) to serialize data and build APIs.", "from rest_framework import serializers\n\nclass BookSerializer(serializers.ModelSerializer):\n    class Meta:\n        model = Book\n        fields = '__all__'"),
    ("django_testing", "Testing", "Writing automated unit and integration tests.", "from django.test import TestCase\nfrom .models import Book\n\nclass BookTestCase(TestCase):\n    def test_book_creation(self):\n        b = Book.objects.create(title='Test', pages=100)\n        self.assertEqual(b.title, 'Test')"),
    ("django_security", "Security", "Mitigating CSRF, XSS, and SQL Injection attacks.", "<!-- Securing Forms against CSRF -->\n<form method='POST'>\n    {% csrf_token %}\n    {{ form.as_p }}\n    <button type='submit'>Save</button>\n</form>"),
    ("django_deploy", "Deployment", "Gunicorn, WSGI, Whitenoise, and serving databases in production.", "pip install gunicorn\ngunicorn myproject.wsgi:application"),
]

for nid, title, desc, code in django_topics:
    data['django']['content'][nid] = {
        "title": title,
        "explanation": explanation(title, [
            (f"Understanding {title}", desc, [(f"{title} Usage", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([(f"What is the primary role of {title.lower()}?", ["Specific Django Component Role", "Frontend rendering", "Database design", "General Python syntax"], "Specific Django Component Role")]),
        "hands_on": task(f"Implement {title}", f"Write the Python code demonstrating {title}.", "Follow Django standards.", code),
        "problem_solving": problems([(f"{title} Solution", f"Adjust structure relying on {title}.", code)])
    }

data['django']['content']['django_interview'] = {
    "title": "Django Interview Guide",
    "explanation": explanation("Django Interview Questions", [
        ("Common Questions", "Top Django questions asked in interviews.", [
            ("What architectural pattern does Django follow?", "MVT (Model-View-Template) which is roughly equivalent to MVC."),
            ("What is Django ORM?", "Object-Relational Mapping lets you interact with your database, like you would with SQL. In other words, it's a way to create, retrieve, update, and delete records in your database using object-oriented Python code."),
            ("What are signals in Django?", "Signals allow decoupled applications get notified when actions occur elsewhere in the framework (e.g. pre_save, post_save).")
        ])
    ]),
    "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
}

new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Django content updated fully!")
