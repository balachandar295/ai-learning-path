
"""
Batch: Flask (all 18) + TypeScript (only ts_basics was generic) + JavaScript (js_functions)
"""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'core', 'static', 'tracks_data.js')

def make_topic(intro, subtopics, key_concepts, examples, quiz, hands_on=None, problems=None):
    s = {"introduction": intro, "subtopics": subtopics, "key_concepts": key_concepts, "examples": examples}
    return {
        "structured": s,
        "concept_quiz": quiz,
        "hands_on": hands_on or {"title": "Try it!", "description": "Practice the concept above.", "hint": "Use the examples as a guide.", "code": ""},
        "problem_solving": problems or []
    }

# ─────────────────────────────────────────────
# FLASK (all 18 topics)
# ─────────────────────────────────────────────
FLASK_FIXES = {
    "flask_basics": make_topic(
        intro="""<p><strong>Flask</strong> is a lightweight Python web framework created by Armin Ronacher in 2010. Unlike Django, Flask follows a <em>"micro-framework"</em> philosophy: it gives you only the core tools (routing, templating, request handling) and lets you choose your own libraries for databases, authentication, and everything else. This makes Flask extremely flexible for APIs, microservices, and small-to-medium web apps. It is used by companies like Netflix, LinkedIn, and Airbnb for internal services.</p>""",
        subtopics=[
            {"title": "Installing Flask & Minimal App", "content": "<p>Install Flask via pip: <code>pip install flask</code>. The minimal Flask app is just a few lines — create an app object, define a route, and run it.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\n\nif __name__ == '__main__':\n    app.run(debug=True)</pre>"},
            {"title": "The Flask App Object", "content": "<p><code>Flask(__name__)</code> creates the application. The <code>__name__</code> argument tells Flask where to find templates and static files relative to the current module. <code>debug=True</code> enables hot-reloading and detailed error pages during development — <strong>never use it in production.</strong></p>"},
            {"title": "Development vs Production", "content": "<p>Flask's built-in server (<code>app.run()</code>) is for development only. In production, use a WSGI server like <strong>Gunicorn</strong> or <strong>uWSGI</strong> behind <strong>Nginx</strong>. Set the environment variable <code>FLASK_ENV=production</code> to disable debug mode.</p>"},
        ],
        key_concepts="<ul><li><strong>WSGI</strong> — Web Server Gateway Interface; Flask is a WSGI application.</li><li><strong>@app.route()</strong> — Decorator that maps a URL path to a Python function.</li><li><strong>Request-Response cycle</strong> — Browser sends HTTP request; Flask routes it to a view function; function returns HTTP response.</li><li><strong>Debug mode</strong> — Auto-reloads server on code changes; shows interactive debugger in browser.</li><li><strong>Application factory</strong> — Pattern to create Flask app inside a function for flexible configuration and testing.</li></ul>",
        examples=[
            {"title": "Minimal Flask App", "code": "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef index():\n    return '<h1>Welcome to Flask!</h1>'\n\n@app.route('/about')\ndef about():\n    return '<p>This is the about page.</p>'\n\nif __name__ == '__main__':\n    app.run(debug=True)", "output": "* Running on http://127.0.0.1:5000", "explanation": "<p>Two routes registered. Flask maps GET / to <code>index()</code> and GET /about to <code>about()</code>.</p>"},
        ],
        quiz=[
            {"q": "Flask is classified as a:", "options": ["Full-stack framework", "Micro-framework", "CMS", "Template engine"], "answer": "Micro-framework"},
            {"q": "What does debug=True do in Flask?", "options": ["Enables HTTPS", "Enables hot-reload and error pages", "Disables logging", "Runs production server"], "answer": "Enables hot-reload and error pages"},
        ],
    ),
    "flask_routing": make_topic(
        intro="""<p><strong>Routing</strong> is the mechanism by which Flask maps incoming HTTP requests (URLs) to specific Python view functions. Flask uses the <code>@app.route()</code> decorator to define routes. Routes can be static (<code>/about</code>) or dynamic (<code>/user/&lt;username&gt;</code>), can restrict accepted HTTP methods, and can generate URLs programmatically using <code>url_for()</code> — making your URLs refactor-proof.</p>""",
        subtopics=[
            {"title": "Dynamic URL Parameters", "content": "<p>Angle brackets in the route path define <strong>variable rules</strong>. Flask captures the URL segment and passes it as a function argument. You can optionally specify the type: <code>&lt;int:id&gt;</code>, <code>&lt;float:price&gt;</code>, <code>&lt;path:filename&gt;</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/user/&lt;username&gt;')\ndef profile(username):\n    return f'Profile: {username}'\n\n@app.route('/post/&lt;int:post_id&gt;')\ndef post(post_id):\n    return f'Post #{post_id}'</pre>"},
            {"title": "HTTP Methods", "content": "<p>By default, routes only respond to GET. Add the <code>methods</code> argument to accept POST, PUT, DELETE, etc. This is how you handle form submissions and REST API endpoints.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/login', methods=['GET', 'POST'])\ndef login():\n    if request.method == 'POST':\n        return 'Processing login...'\n    return 'Show login form'</pre>"},
            {"title": "url_for() — Reverse URL Generation", "content": "<p><code>url_for('function_name')</code> generates the URL for a given view function. This is essential — if you ever change a URL pattern, <code>url_for()</code> updates all references automatically, preventing broken links.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import url_for\nwith app.test_request_context():\n    print(url_for('profile', username='Alice'))\n    # /user/Alice</pre>"},
        ],
        key_concepts="<ul><li>Route decorators map URL patterns to view functions.</li><li>Dynamic segments use <code>&lt;variable&gt;</code> or typed <code>&lt;int:id&gt;</code>.</li><li><code>url_for()</code> generates URLs from function names — always prefer it over hardcoded URLs.</li><li>A trailing slash in the route (<code>/about/</code>) enables redirect from <code>/about</code>.</li><li>Blueprints prefix all their routes with a URL prefix (e.g., <code>/api/</code>).</li></ul>",
        examples=[
            {"title": "Dynamic Routes", "code": "from flask import Flask, url_for\napp = Flask(__name__)\n\n@app.route('/greet/&lt;name&gt;')\ndef greet(name):\n    return f'Hello, {name}!'\n\n@app.route('/square/&lt;int:n&gt;')\ndef square(n):\n    return f'{n} squared = {n**2}'\n\nif __name__ == '__main__':\n    app.run(debug=True)", "output": "GET /greet/Alice  →  Hello, Alice!\nGET /square/7    →  7 squared = 49", "explanation": "<p>Type converters in routes ensure Flask passes the right Python type to the function.</p>"},
        ],
        quiz=[
            {"q": "How do you capture a URL segment as an integer named 'id'?", "options": ["<id>", "[int:id]", "<int:id>", "{id:int}"], "answer": "<int:id>"},
            {"q": "What does url_for() do?", "options": ["Redirects to a URL", "Generates a URL from a view function name", "Validates URL format", "Parses query strings"], "answer": "Generates a URL from a view function name"},
        ],
    ),
    "flask_templates": make_topic(
        intro="""<p>Flask uses the <strong>Jinja2</strong> templating engine to generate dynamic HTML. Instead of building HTML by string concatenation in Python (messy and insecure), you write HTML templates with special Jinja2 syntax that gets filled with data from your view functions. Templates are stored in a <code>templates/</code> folder, and Flask's <code>render_template()</code> function renders them with your context data.</p>""",
        subtopics=[
            {"title": "render_template()", "content": "<p>Pass the template filename and keyword arguments to <code>render_template()</code>. The keyword arguments become variables accessible inside the template.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'># views.py\nfrom flask import render_template\n\n@app.route('/user/&lt;name&gt;')\ndef user(name):\n    return render_template('profile.html', username=name, score=95)</pre>"},
            {"title": "Template Syntax", "content": "<p>Jinja2 uses three special syntaxes:</p><ul><li><code>{{ variable }}</code> — outputs a value</li><li><code>{% if/for/block %}</code> — control logic</li><li><code>{# comment #}</code> — template comments (not rendered)</li></ul><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>&lt;h1&gt;Welcome, {{ username }}!&lt;/h1&gt;\n{% if score &gt;= 90 %}\n  &lt;p&gt;Excellent!&lt;/p&gt;\n{% else %}\n  &lt;p&gt;Keep practising.&lt;/p&gt;\n{% endif %}</pre>"},
            {"title": "Template Inheritance", "content": "<p>A key Jinja2 feature: define a <code>base.html</code> with the common layout (navbar, footer) and use <code>{% block content %}{% endblock %}</code> placeholders. Child templates <code>{% extend 'base.html' %}</code> and fill in only the blocks they override — eliminating duplication.</p>"},
        ],
        key_concepts="<ul><li>Templates live in the <code>templates/</code> directory (relative to your app).</li><li><code>{{ }}</code> for output, <code>{% %}</code> for logic, <code>{# #}</code> for comments.</li><li><strong>Auto-escaping</strong> — Jinja2 escapes HTML by default, preventing XSS attacks.</li><li><strong>Filters</strong> — <code>{{ name|upper }}</code>, <code>{{ items|length }}</code>, <code>{{ date|strftime('%Y') }}</code>.</li><li><strong>Template inheritance</strong> eliminates layout duplication across pages.</li></ul>",
        examples=[
            {"title": "Template Rendering", "code": "# app.py\nfrom flask import Flask, render_template\napp = Flask(__name__)\n\n@app.route('/students')\ndef students():\n    data = ['Alice', 'Bob', 'Charlie']\n    return render_template('students.html', names=data)\n\n# templates/students.html\n'''\n&lt;ul&gt;\n{% for name in names %}\n  &lt;li&gt;{{ name }}&lt;/li&gt;\n{% endfor %}\n&lt;/ul&gt;\n'''", "output": "<ul>\n  <li>Alice</li>\n  <li>Bob</li>\n  <li>Charlie</li>\n</ul>", "explanation": "<p>The Python list is passed to the template and looped with Jinja2's for-tag.</p>"},
        ],
        quiz=[
            {"q": "Which folder does Flask look in for templates by default?", "options": ["static/", "views/", "templates/", "html/"], "answer": "templates/"},
            {"q": "Which Jinja2 syntax outputs a variable?", "options": ["{$ var $}", "{% var %}", "{{ var }}", "{# var #}"], "answer": "{{ var }}"},
        ],
    ),
    "flask_jinja": make_topic(
        intro="""<p><strong>Jinja2</strong> is a full-featured, high-performance template engine for Python, and it's the default engine used by Flask. Beyond simple variable output, Jinja2 provides <strong>filters</strong> (transform values inline), <strong>macros</strong> (reusable template functions similar to Python functions), <strong>inheritance</strong> (override specific blocks in child templates), and <strong>includes</strong> (insert partial templates). Understanding Jinja2 deeply lets you build clean, maintainable front-end templates without mixing Python logic into HTML.</p>""",
        subtopics=[
            {"title": "Filters", "content": "<p>Filters transform values using the pipe <code>|</code> syntax. Built-in filters include <code>upper</code>, <code>lower</code>, <code>title</code>, <code>length</code>, <code>reverse</code>, <code>default</code>, <code>join</code>, and <code>truncate</code>. You can also write custom filters in Python and register them with <code>@app.template_filter()</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>{{ username|upper }}           → ALICE\n{{ items|length }}             → 3\n{{ bio|truncate(100) }}       → first 100 chars...\n{{ value|default('N/A') }}   → shows N/A if None</pre>"},
            {"title": "Macros — Reusable Template Components", "content": "<p>Macros are like functions in Jinja2. Define once, call anywhere. Ideal for form fields, card layouts, pagination, and alert banners.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>{% macro input_field(name, type='text', placeholder='') %}\n  &lt;input type=\"{{ type }}\" name=\"{{ name }}\" placeholder=\"{{ placeholder }}\"&gt;\n{% endmacro %}\n\n{{ input_field('email', 'email', 'Enter your email') }}</pre>"},
            {"title": "Template Inheritance Deep Dive", "content": "<p>Define a <code>base.html</code> with named <code>{% block %}</code>s. Child templates use <code>{% extends 'base.html' %}</code> and redefine only the blocks they need. Use <code>{{ super() }}</code> to include the parent block's content while adding more.</p>"},
        ],
        key_concepts="<ul><li>Filters: <code>|upper</code>, <code>|default('val')</code>, <code>|join(', ')</code>.</li><li>Macros: reusable template snippets, defined with <code>{% macro name(args) %}...{% endmacro %}</code>.</li><li><code>{% include 'partial.html' %}</code> — insert another template inline.</li><li><code>{% set var = value %}</code> — define template variables.</li><li><code>loop.index</code>, <code>loop.first</code>, <code>loop.last</code> — special loop variables.</li></ul>",
        examples=[
            {"title": "Jinja2 Loop Helpers", "code": "# templates/list.html\n{% for item in items %}\n  &lt;div class=\"{{ 'highlight' if loop.first else '' }}\"&gt;\n    {{ loop.index }}: {{ item|title }}\n  &lt;/div&gt;\n{% else %}\n  &lt;p&gt;No items found.&lt;/p&gt;\n{% endfor %}", "output": "1: Apple\n2: Banana\n3: Cherry", "explanation": "<p><code>loop.first</code> and <code>loop.index</code> are auto-provided inside Jinja2 for loops. The <code>{% else %}</code> block renders when the list is empty.</p>"},
        ],
        quiz=[
            {"q": "Which Jinja2 syntax defines a reusable template component?", "options": ["{% include %}", "{% macro %}", "{% block %}", "{% extends %}"], "answer": "{% macro %}"},
            {"q": "How do you apply the 'upper' filter in Jinja2?", "options": ["upper(name)", "name.upper()", "{{ name|upper }}", "{% upper name %}"], "answer": "{{ name|upper }}"},
        ],
    ),
    "flask_forms": make_topic(
        intro="""<p>Handling HTML forms is one of the most common tasks in web development. Flask processes form data through the <code>request</code> object. For more robust form handling with validation and CSRF protection, <strong>Flask-WTF</strong> (an integration of the WTForms library) is the standard approach. It provides form classes, field validation, error messaging, and automatic CSRF token generation — all essential for secure web forms.</p>""",
        subtopics=[
            {"title": "Accessing Form Data with request", "content": "<p>When a form POSTs to a Flask route, data is available in <code>request.form</code> (a dictionary). Always check <code>request.method == 'POST'</code> first.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import request\n\n@app.route('/submit', methods=['GET','POST'])\ndef submit():\n    if request.method == 'POST':\n        name = request.form.get('name', '')\n        return f'Hello, {name}!'\n    return render_template('form.html')</pre>"},
            {"title": "Flask-WTF Forms", "content": "<p>Define a form as a Python class inheriting from <code>FlaskForm</code>. Each field is a class attribute with validators like <code>DataRequired()</code>, <code>Email()</code>, <code>Length(min=3, max=50)</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask_wtf import FlaskForm\nfrom wtforms import StringField, PasswordField, SubmitField\nfrom wtforms.validators import DataRequired, Email\n\nclass LoginForm(FlaskForm):\n    email = StringField('Email', validators=[DataRequired(), Email()])\n    password = PasswordField('Password', validators=[DataRequired()])\n    submit = SubmitField('Login')</pre>"},
            {"title": "CSRF Protection", "content": "<p>Cross-Site Request Forgery (CSRF) attacks trick authenticated users into submitting malicious forms. Flask-WTF automatically generates and validates a hidden CSRF token. In your template, add <code>{{ form.hidden_tag() }}</code> inside every form.</p>"},
        ],
        key_concepts="<ul><li><code>request.form</code> — dict of POST form fields.</li><li><code>request.args</code> — dict of GET query parameters.</li><li><code>request.files</code> — uploaded files.</li><li>Flask-WTF provides server-side validation + CSRF tokens automatically.</li><li>Always validate form inputs; never trust raw user data.</li></ul>",
        examples=[
            {"title": "Simple Contact Form", "code": "# views.py\n@app.route('/contact', methods=['GET', 'POST'])\ndef contact():\n    if request.method == 'POST':\n        name = request.form.get('name')\n        message = request.form.get('message')\n        if not name or not message:\n            return 'All fields are required!', 400\n        return f'Thanks, {name}! We received your message.'\n    return render_template('contact.html')", "output": "Thanks, Alice! We received your message.", "explanation": "<p>Basic validation checks for empty fields and returns a 400 status code if validation fails.</p>"},
        ],
        quiz=[
            {"q": "Where does Flask store POST form data in the request?", "options": ["request.data", "request.params", "request.form", "request.body"], "answer": "request.form"},
            {"q": "What does CSRF protection prevent?", "options": ["SQL injection", "XSS attacks", "Forged cross-site form submissions", "Password sniffing"], "answer": "Forged cross-site form submissions"},
        ],
    ),
    "flask_sqlalchemy": make_topic(
        intro="""<p><strong>Flask-SQLAlchemy</strong> integrates the powerful SQLAlchemy ORM (Object Relational Mapper) with Flask. Instead of writing raw SQL, you define your database schema as Python classes (called <strong>Models</strong>), and SQLAlchemy translates your Python operations into SQL. This means you can switch from SQLite (development) to PostgreSQL (production) with a single config change. SQLAlchemy also manages connections, handles transactions, and prevents SQL injection automatically.</p>""",
        subtopics=[
            {"title": "Setup & Configuration", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>pip install flask-sqlalchemy\n\nfrom flask_sqlalchemy import SQLAlchemy\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'\ndb = SQLAlchemy(app)</pre>"},
            {"title": "Defining Models", "content": "<p>A model is a Python class that maps to a database table. Each class attribute is a column with a type and optional constraints.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>class User(db.Model):\n    id = db.Column(db.Integer, primary_key=True)\n    username = db.Column(db.String(80), unique=True, nullable=False)\n    email = db.Column(db.String(120), unique=True, nullable=False)\n\n    def __repr__(self):\n        return f'&lt;User {self.username}&gt;'</pre>"},
            {"title": "CRUD Operations", "content": "<p>SQLAlchemy provides a session-based API for all database operations:</p><ul><li><code>db.session.add(obj)</code> — stage an INSERT or UPDATE</li><li><code>db.session.commit()</code> — write to database</li><li><code>User.query.all()</code> — SELECT all</li><li><code>User.query.filter_by(username='alice').first()</code> — SELECT WHERE</li><li><code>db.session.delete(obj)</code> then commit — DELETE</li></ul>"},
        ],
        key_concepts="<ul><li><strong>ORM</strong> — maps Python classes to SQL tables; no raw SQL needed.</li><li><code>db.create_all()</code> — creates all tables from models.</li><li><strong>Relationships</strong> — <code>db.relationship()</code> and <code>db.ForeignKey()</code> model table JOIN relationships.</li><li><strong>Migrations</strong> — use Flask-Migrate (Alembic) to version-control schema changes.</li><li>The session acts as a unit of work — all changes are atomic.</li></ul>",
        examples=[
            {"title": "Adding & Querying Records", "code": "# Create a user\nnew_user = User(username='alice', email='alice@example.com')\ndb.session.add(new_user)\ndb.session.commit()\n\n# Query all users\nusers = User.query.all()\nfor u in users:\n    print(u.username)\n\n# Query by filter\nuser = User.query.filter_by(username='alice').first()\nprint(user.email)  # alice@example.com", "output": "alice\nalice@example.com", "explanation": "<p>SQLAlchemy translates <code>.add()</code> to INSERT and <code>.query.filter_by()</code> to SELECT WHERE.</p>"},
        ],
        quiz=[
            {"q": "What does db.session.commit() do?", "options": ["Rolls back changes", "Closes the database connection", "Writes staged changes to the database", "Creates a new table"], "answer": "Writes staged changes to the database"},
            {"q": "Which Flask extension handles database schema version control?", "options": ["Flask-Admin", "Flask-Migrate", "Flask-WTF", "Flask-Login"], "answer": "Flask-Migrate"},
        ],
    ),
    "flask_crud": make_topic(
        intro="""<p><strong>CRUD</strong> — Create, Read, Update, Delete — are the four fundamental operations of any persistent data-driven application. In Flask, CRUD maps naturally to HTTP methods: POST (Create), GET (Read), PUT/PATCH (Update), DELETE (Delete). Building a complete CRUD feature requires wiring together routing, form handling, database operations, and template rendering into a cohesive user experience. This is the backbone of any web app: from a blog to a task manager to an e-commerce platform.</p>""",
        subtopics=[
            {"title": "Create — POST route", "content": "<p>A POST route processes a form submission and inserts a new record into the database.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/tasks/create', methods=['POST'])\ndef create_task():\n    title = request.form.get('title')\n    task = Task(title=title)\n    db.session.add(task)\n    db.session.commit()\n    return redirect(url_for('list_tasks'))</pre>"},
            {"title": "Read — GET route", "content": "<p>A GET route queries the database and passes results to a template.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/tasks')\ndef list_tasks():\n    tasks = Task.query.order_by(Task.created_at.desc()).all()\n    return render_template('tasks.html', tasks=tasks)</pre>"},
            {"title": "Update & Delete", "content": "<p>Update fetches the record by ID, modifies it, and commits. Delete fetches and removes.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/tasks/&lt;int:id&gt;/done', methods=['POST'])\ndef complete_task(id):\n    task = Task.query.get_or_404(id)\n    task.done = True\n    db.session.commit()\n    return redirect(url_for('list_tasks'))\n\n@app.route('/tasks/&lt;int:id&gt;/delete', methods=['POST'])\ndef delete_task(id):\n    task = Task.query.get_or_404(id)\n    db.session.delete(task)\n    db.session.commit()\n    return redirect(url_for('list_tasks'))</pre>"},
        ],
        key_concepts="<ul><li><code>get_or_404(id)</code> — fetches by primary key or returns a 404 response automatically.</li><li><code>redirect(url_for('view'))</code> — Post-Redirect-Get pattern prevents form resubmission.</li><li>HTML forms only support GET and POST; use hidden inputs or JavaScript for PUT/DELETE.</li><li>Always validate and sanitise inputs before database operations.</li></ul>",
        examples=[
            {"title": "Task Manager CRUD", "code": "class Task(db.Model):\n    id = db.Column(db.Integer, primary_key=True)\n    title = db.Column(db.String(200), nullable=False)\n    done = db.Column(db.Boolean, default=False)\n\n@app.route('/')\ndef index():\n    tasks = Task.query.all()\n    return render_template('index.html', tasks=tasks)\n\n@app.route('/add', methods=['POST'])\ndef add():\n    title = request.form['title']\n    db.session.add(Task(title=title))\n    db.session.commit()\n    return redirect(url_for('index'))", "output": "Task added and listed on the home page.", "explanation": "<p>The Post-Redirect-Get pattern: after a POST, always redirect to prevent duplicate submissions on browser refresh.</p>"},
        ],
        quiz=[
            {"q": "What pattern prevents form resubmission on page refresh?", "options": ["Model-View-Controller", "Post-Redirect-Get", "Request-Response", "Observer pattern"], "answer": "Post-Redirect-Get"},
            {"q": "What does get_or_404(id) do if the record isn't found?", "options": ["Returns None", "Raises a Python exception", "Returns a 404 HTTP response", "Redirects to home"], "answer": "Returns a 404 HTTP response"},
        ],
    ),
    "flask_auth": make_topic(
        intro="""<p>Authentication (verifying <em>who you are</em>) and authorisation (checking <em>what you can do</em>) are critical for any real web application. <strong>Flask-Login</strong> is the standard extension for managing user sessions in Flask. It handles login/logout, "remember me" cookies, and the <code>@login_required</code> decorator that protects private routes. Passwords must never be stored as plain text — use <strong>Werkzeug's</strong> <code>generate_password_hash</code> and <code>check_password_hash</code> utilities.</p>""",
        subtopics=[
            {"title": "Password Hashing", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from werkzeug.security import generate_password_hash, check_password_hash\n\nhashed = generate_password_hash('mypassword')\ncheck_password_hash(hashed, 'mypassword')  # True\ncheck_password_hash(hashed, 'wrongpass')  # False</pre><p>Werkzeug uses PBKDF2 with a random salt — even identical passwords produce different hashes.</p>"},
            {"title": "Flask-Login Setup", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required\nlogin_manager = LoginManager(app)\nlogin_manager.login_view = 'login'  # redirect here if not logged in\n\nclass User(db.Model, UserMixin):\n    # UserMixin provides: is_authenticated, is_active, get_id()\n    ...</pre>"},
            {"title": "@login_required Decorator", "content": "<p>Protect any route by adding <code>@login_required</code> above it. Flask-Login redirects unauthenticated users to the login page automatically.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/dashboard')\n@login_required\ndef dashboard():\n    return render_template('dashboard.html')</pre>"},
        ],
        key_concepts="<ul><li>Never store plain-text passwords — always hash with <code>generate_password_hash()</code>.</li><li><code>UserMixin</code> provides the four properties Flask-Login needs on a User model.</li><li><code>login_user(user)</code> starts a session; <code>logout_user()</code> ends it.</li><li><code>current_user</code> — a proxy to the currently logged-in user object.</li><li>Use HTTPS in production — session cookies contain sensitive tokens.</li></ul>",
        examples=[
            {"title": "Login Route", "code": "@app.route('/login', methods=['GET', 'POST'])\ndef login():\n    if request.method == 'POST':\n        email = request.form['email']\n        password = request.form['password']\n        user = User.query.filter_by(email=email).first()\n        if user and check_password_hash(user.password, password):\n            login_user(user)\n            return redirect(url_for('dashboard'))\n        return 'Invalid credentials', 401\n    return render_template('login.html')", "output": "Redirects to /dashboard on success; returns 401 on failure.", "explanation": "<p>Always check both that the user exists AND that the password matches — separate checks can leak information.</p>"},
        ],
        quiz=[
            {"q": "Which function stores a hashed password securely?", "options": ["hash_password()", "md5(password)", "generate_password_hash()", "encrypt(password)"], "answer": "generate_password_hash()"},
            {"q": "What does @login_required do when a user is not authenticated?", "options": ["Returns 403 Forbidden", "Raises an exception", "Redirects to the login page", "Returns an empty response"], "answer": "Redirects to the login page"},
        ],
    ),
    "flask_blueprints": make_topic(
        intro="""<p><strong>Blueprints</strong> are Flask's solution for organising a growing application into modular, reusable components. Without Blueprints, everything lives in one file — routes, models, utilities — which becomes unmanageable. With Blueprints, you split your app into logical sections (e.g., <code>auth</code>, <code>posts</code>, <code>admin</code>), each in its own module with its own routes, templates, and static files. Blueprints are then registered on the main app, optionally with a URL prefix.</p>""",
        subtopics=[
            {"title": "Creating a Blueprint", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'># auth/routes.py\nfrom flask import Blueprint\nauth_bp = Blueprint('auth', __name__, url_prefix='/auth')\n\n@auth_bp.route('/login')\ndef login():\n    return 'Login page'\n\n@auth_bp.route('/logout')\ndef logout():\n    return 'Logged out'</pre>"},
            {"title": "Registering a Blueprint", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'># app/__init__.py\nfrom flask import Flask\nfrom .auth.routes import auth_bp\n\ndef create_app():\n    app = Flask(__name__)\n    app.register_blueprint(auth_bp)\n    return app</pre><p>All routes defined in <code>auth_bp</code> are now accessible at <code>/auth/login</code> and <code>/auth/logout</code>.</p>"},
            {"title": "Application Factory Pattern", "content": "<p>Blueprints work best with the <strong>Application Factory</strong> pattern: define a <code>create_app()</code> function that builds and configures the app. This makes testing easy (create fresh app per test) and allows multiple configs (dev, prod, test).</p>"},
        ],
        key_concepts="<ul><li>Blueprints are registered with <code>app.register_blueprint(bp)</code>.</li><li><code>url_prefix='/auth'</code> prepends all blueprint routes with <code>/auth</code>.</li><li>Each Blueprint can have its own <code>templates/</code> and <code>static/</code> folders.</li><li><code>url_for('auth.login')</code> — reference blueprint routes using <code>blueprint_name.function_name</code>.</li><li>The Application Factory pattern is industry standard for Flask projects.</li></ul>",
        examples=[
            {"title": "Project Structure with Blueprints", "code": "# Typical Flask project layout:\n# ├── app/\n# │   ├── __init__.py      ← create_app()\n# │   ├── auth/\n# │   │   ├── __init__.py\n# │   │   └── routes.py    ← Blueprint('auth')\n# │   ├── blog/\n# │   │   └── routes.py    ← Blueprint('blog')\n# │   └── models.py\n# └── run.py\n\n# run.py\nfrom app import create_app\napp = create_app()\nif __name__ == '__main__':\n    app.run(debug=True)", "output": "Organised, scalable Flask application structure.", "explanation": "<p>Each section of your app becomes independent and testable — the gold standard for mid-to-large Flask projects.</p>"},
        ],
        quiz=[
            {"q": "How do you reference a Blueprint route in url_for()?", "options": ["url_for('login')", "url_for('auth:login')", "url_for('auth.login')", "url_for('/auth/login')"], "answer": "url_for('auth.login')"},
            {"q": "What is the main benefit of using Blueprints?", "options": ["Faster execution", "Automatic caching", "Modular code organisation", "Built-in authentication"], "answer": "Modular code organisation"},
        ],
    ),
    "flask_rest": make_topic(
        intro="""<p>A <strong>REST API</strong> (Representational State Transfer) is a web service that communicates using JSON over HTTP, following conventions: GET to retrieve, POST to create, PUT/PATCH to update, DELETE to remove. Flask is an excellent choice for building REST APIs. The <code>jsonify()</code> function converts Python dicts/lists to JSON responses. For production APIs, <strong>Flask-RESTX</strong> or <strong>Flask-Marshmallow</strong> add schema validation, serialisation, and auto-generated Swagger documentation.</p>""",
        subtopics=[
            {"title": "JSON Responses with jsonify()", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import jsonify, request\n\n@app.route('/api/users', methods=['GET'])\ndef get_users():\n    users = User.query.all()\n    return jsonify([{'id': u.id, 'name': u.username} for u in users])</pre>"},
            {"title": "Handling JSON Request Bodies", "content": "<p>For POST/PUT requests with JSON bodies, use <code>request.get_json()</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.route('/api/users', methods=['POST'])\ndef create_user():\n    data = request.get_json()\n    user = User(username=data['name'], email=data['email'])\n    db.session.add(user)\n    db.session.commit()\n    return jsonify({'id': user.id}), 201</pre>"},
            {"title": "HTTP Status Codes", "content": "<p>Return the correct status code as the second value in the return tuple: <code>200 OK</code>, <code>201 Created</code>, <code>400 Bad Request</code>, <code>401 Unauthorized</code>, <code>404 Not Found</code>, <code>500 Internal Server Error</code>.</p>"},
        ],
        key_concepts="<ul><li><code>jsonify()</code> — converts Python object to JSON response with correct Content-Type header.</li><li><code>request.get_json()</code> — parses JSON request body.</li><li>Return <code>(response, status_code)</code> tuple for custom status codes.</li><li>Use <strong>Flask-CORS</strong> to allow cross-origin requests from a frontend framework.</li><li><strong>Token authentication</strong> — use JWT (Flask-JWT-Extended) for stateless API auth.</li></ul>",
        examples=[
            {"title": "Simple REST CRUD API", "code": "tasks = {}\nn = 0\n\n@app.route('/api/tasks', methods=['GET'])\ndef get_tasks():\n    return jsonify(list(tasks.values()))\n\n@app.route('/api/tasks', methods=['POST'])\ndef create_task():\n    global n\n    data = request.get_json()\n    n += 1\n    tasks[n] = {'id': n, 'title': data['title'], 'done': False}\n    return jsonify(tasks[n]), 201\n\n@app.route('/api/tasks/&lt;int:id&gt;', methods=['DELETE'])\ndef delete_task(id):\n    tasks.pop(id, None)\n    return jsonify({'message': 'deleted'})", "output": "GET /api/tasks → []\nPOST /api/tasks {title:'Buy milk'} → {id:1, title:'Buy milk', done:false}", "explanation": "<p>A minimal in-memory REST API — replace the dict with SQLAlchemy for production.</p>"},
        ],
        quiz=[
            {"q": "What HTTP status code should a successful POST (create) return?", "options": ["200", "204", "201", "301"], "answer": "201"},
            {"q": "How do you read a JSON request body in Flask?", "options": ["request.json_body()", "request.body", "request.get_json()", "request.data['json']"], "answer": "request.get_json()"},
        ],
    ),
    "flask_errors": make_topic(
        intro="""<p>Proper error handling is a hallmark of professional Flask applications. By default, Flask shows a plain HTML error page designed for developers. In production, you should: return structured JSON error responses for APIs, render branded error pages for web apps, log errors to a monitoring service, and never expose stack traces to end users. Flask's <code>@app.errorhandler()</code> decorator lets you customise responses for specific HTTP error codes and Python exceptions.</p>""",
        subtopics=[
            {"title": "Custom Error Handlers", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>@app.errorhandler(404)\ndef not_found(e):\n    return render_template('404.html'), 404\n\n@app.errorhandler(500)\ndef server_error(e):\n    return render_template('500.html'), 500</pre>"},
            {"title": "abort() — Trigger HTTP Errors", "content": "<p>Call <code>abort(404)</code> anywhere in a view to immediately return that HTTP error. Useful for cases like record not found.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import abort\n\n@app.route('/item/&lt;int:id&gt;')\ndef get_item(id):\n    item = Item.query.get(id)\n    if not item:\n        abort(404)\n    return jsonify(item.to_dict())</pre>"},
            {"title": "Logging Errors", "content": "<p>Flask uses Python's <code>logging</code> module. Configure it to write errors to a file or send to services like Sentry for production monitoring.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>import logging\nlogging.basicConfig(filename='error.log', level=logging.ERROR)\napp.logger.error('Something went wrong: %s', str(e))</pre>"},
        ],
        key_concepts="<ul><li><code>@app.errorhandler(code)</code> — register handler for a specific HTTP status code.</li><li><code>abort(code)</code> — immediately raise an HTTP error from any view.</li><li>For APIs, return JSON error responses: <code>jsonify({'error': 'Not found'}), 404</code>.</li><li>Never show stack traces in production — set <code>DEBUG=False</code>.</li><li>Use Sentry or similar for error monitoring in production.</li></ul>",
        examples=[
            {"title": "JSON Error Handlers for APIs", "code": "@app.errorhandler(404)\ndef not_found(e):\n    return jsonify({'error': 'Resource not found', 'code': 404}), 404\n\n@app.errorhandler(400)\ndef bad_request(e):\n    return jsonify({'error': 'Bad request', 'code': 400}), 400\n\n@app.errorhandler(500)\ndef internal_error(e):\n    app.logger.error(str(e))\n    return jsonify({'error': 'Internal server error'}), 500", "output": "GET /api/unknown → {\"error\": \"Resource not found\", \"code\": 404}", "explanation": "<p>Consistent JSON error format makes your API predictable and easy for clients to handle.</p>"},
        ],
        quiz=[
            {"q": "Which decorator registers a custom 404 error handler?", "options": ["@app.route('/404')", "@app.handle_error(404)", "@app.errorhandler(404)", "@app.on_error(404)"], "answer": "@app.errorhandler(404)"},
            {"q": "The abort() function:", "options": ["Closes the database connection", "Terminates the Flask server", "Immediately raises an HTTP error", "Cancels a redirect"], "answer": "Immediately raises an HTTP error"},
        ],
    ),
    "flask_context": make_topic(
        intro="""<p>Flask operates with two types of <strong>context objects</strong> that make request-specific data available without passing it explicitly through every function call. The <strong>Application Context</strong> (<code>g</code>, <code>current_app</code>) stores data for the duration of a request within the app, while the <strong>Request Context</strong> (<code>request</code>, <code>session</code>) stores data specific to the current HTTP request. Understanding contexts is essential for writing extensions, middleware, and correct multi-threaded Flask apps.</p>""",
        subtopics=[
            {"title": "The Request Context: request & session", "content": "<p><code>request</code> — the current HTTP request (method, form data, headers, JSON body). <code>session</code> — a server-side dictionary persisted across requests via a signed cookie. Use <code>session['key'] = value</code> to store data (e.g., user ID after login).</p>"},
            {"title": "The Application Context: g & current_app", "content": "<p><code>g</code> is a temporary storage object tied to a single request — use it to store per-request data like a database connection. <code>current_app</code> is a proxy to the active Flask application, useful inside extensions that don't have direct access to <code>app</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import g\n\n@app.before_request\ndef load_user():\n    user_id = session.get('user_id')\n    g.user = User.query.get(user_id) if user_id else None</pre>"},
        ],
        key_concepts="<ul><li><code>request</code> — HTTP request details; only valid inside a request context.</li><li><code>session</code> — cryptographically signed cookie-based server state.</li><li><code>g</code> — per-request scratch space; cleared after each request.</li><li><code>current_app</code> — proxy to the Flask app; useful in extensions.</li><li><code>@app.before_request</code> — runs before every request (auth checks, DB connections).</li></ul>",
        examples=[
            {"title": "Using g for Per-Request State", "code": "from flask import g, session\n\n@app.before_request\ndef attach_user():\n    uid = session.get('user_id')\n    g.current_user = User.query.get(uid) if uid else None\n\n@app.route('/profile')\ndef profile():\n    if not g.current_user:\n        abort(401)\n    return f'Hello, {g.current_user.username}'", "output": "Hello, Alice", "explanation": "<p><code>g</code> lets you attach the user object once (in before_request) and access it everywhere in the same request without passing it around.</p>"},
        ],
        quiz=[
            {"q": "What is the purpose of Flask's 'g' object?", "options": ["Global app configuration", "Per-request temporary storage", "Database connection pool", "Template context"], "answer": "Per-request temporary storage"},
            {"q": "Which decorator runs code before every request in Flask?", "options": ["@on_request", "@app.middleware", "@app.before_request", "@app.setup"], "answer": "@app.before_request"},
        ],
    ),
    "flask_deployment": make_topic(
        intro="""<p>Deploying a Flask application to production involves several key decisions: choosing a <strong>WSGI server</strong> (Gunicorn, uWSGI), a <strong>reverse proxy</strong> (Nginx), a <strong>hosting platform</strong> (Heroku, AWS EC2, DigitalOcean, Railway), and setting up <strong>environment variables</strong> for secrets. The built-in Flask dev server (<code>flask run</code>) is single-threaded, has no security hardening, and is completely unsuitable for production. This section covers the standard production deployment stack.</p>""",
        subtopics=[
            {"title": "Gunicorn WSGI Server", "content": "<p>Gunicorn is the standard WSGI server for Python web apps. It spawns multiple worker processes to handle concurrent requests.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>pip install gunicorn\ngunicorn -w 4 -b 0.0.0.0:8000 'app:create_app()'</pre><p>The <code>-w 4</code> flag spawns 4 worker processes. A common formula: <code>workers = (2 × CPU cores) + 1</code>.</p>"},
            {"title": "Environment Variables & Config", "content": "<p>Never hardcode secrets (SECRET_KEY, DB passwords, API keys) in source code. Use environment variables, loaded via <code>python-dotenv</code> from a <code>.env</code> file locally, and set as real envvars on the server.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'># .env\nSECRET_KEY=my-very-secret-key\nDATABASE_URL=postgresql://user:pass@host/db\n\n# config.py\nimport os\nSECRET_KEY = os.environ.get('SECRET_KEY')\nSQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')</pre>"},
            {"title": "Nginx as Reverse Proxy", "content": "<p>Nginx sits in front of Gunicorn: it handles SSL termination, serves static files directly (much faster than Python), rate limiting, and proxies dynamic requests to Gunicorn. This is the standard Nginx + Gunicorn + Flask stack used in production.</p>"},
        ],
        key_concepts="<ul><li><strong>WSGI</strong> — the Python web server standard; Gunicorn/uWSGI implement it.</li><li><strong>Reverse proxy</strong> — Nginx forwards requests to Gunicorn, adds SSL, caches static files.</li><li>Keep <code>DEBUG=False</code> and <code>TESTING=False</code> in production.</li><li>Use <strong>Docker</strong> to containerise for consistent deployments.</li><li>Platform-as-a-Service options (Heroku, Railway, Render) handle servers automatically.</li></ul>",
        examples=[
            {"title": "Deployment Checklist", "code": "# Minimal Dockerfile for Flask + Gunicorn\nFROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nEXPOSE 8000\nCMD [\"gunicorn\", \"-w\", \"4\", \"-b\", \"0.0.0.0:8000\", \"app:create_app()\"]", "output": "Container starts and listens on port 8000.", "explanation": "<p>Containerising Flask with Docker ensures identical environments across dev, staging, and production.</p>"},
        ],
        quiz=[
            {"q": "Which WSGI server is most commonly used with Flask in production?", "options": ["Apache", "Flask's built-in server", "Gunicorn", "Tornado"], "answer": "Gunicorn"},
            {"q": "Where should production secrets like SECRET_KEY be stored?", "options": ["In config.py", "In source code", "In environment variables", "In the database"], "answer": "In environment variables"},
        ],
    ),
    "flask_testing": make_topic(
        intro="""<p>Automated testing is essential for any production Flask application. Flask provides a built-in <strong>test client</strong> that simulates HTTP requests without actually starting a server — letting you write fast, isolated unit and integration tests. Combine this with Python's <code>unittest</code> or <code>pytest</code> for a complete test suite. Test your routes, form validation, authentication flows, and database operations to catch regressions before they reach production.</p>""",
        subtopics=[
            {"title": "The Flask Test Client", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>import pytest\nfrom app import create_app\n\n@pytest.fixture\ndef client():\n    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'})\n    with app.test_client() as client:\n        with app.app_context():\n            db.create_all()\n        yield client</pre>"},
            {"title": "Writing Tests", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>def test_home_page(client):\n    response = client.get('/')\n    assert response.status_code == 200\n    assert b'Welcome' in response.data\n\ndef test_create_user(client):\n    response = client.post('/api/users',\n        json={'name': 'Alice', 'email': 'alice@test.com'})\n    assert response.status_code == 201\n    assert response.json['name'] == 'Alice'</pre>"},
        ],
        key_concepts="<ul><li><code>app.test_client()</code> — returns a test client that mimics a browser.</li><li>Set <code>TESTING=True</code> to disable error catching (so exceptions propagate in tests).</li><li>Use an in-memory SQLite DB (<code>sqlite:///:memory:</code>) for fast, isolated test runs.</li><li><code>response.data</code> — raw bytes of the response body.</li><li><code>response.json</code> — parsed JSON response (for API testing).</li></ul>",
        examples=[
            {"title": "Testing a Login Route", "code": "def test_login_success(client):\n    # Register first\n    client.post('/register', data={'email': 'a@b.com', 'password': 'pass123'})\n    # Then login\n    resp = client.post('/login', data={'email': 'a@b.com', 'password': 'pass123'},\n                       follow_redirects=True)\n    assert resp.status_code == 200\n    assert b'Welcome back' in resp.data\n\ndef test_login_fail(client):\n    resp = client.post('/login', data={'email': 'x@y.com', 'password': 'wrong'})\n    assert resp.status_code == 401", "output": "Tests pass in <0.5s using in-memory SQLite.", "explanation": "<p><code>follow_redirects=True</code> makes the test client follow redirect chains, simulating a real browser.</p>"},
        ],
        quiz=[
            {"q": "Which config setting disables Flask's error-catching in tests?", "options": ["DEBUG=True", "TESTING=True", "PROPAGATE_EXCEPTIONS=True", "TEST_MODE=True"], "answer": "TESTING=True"},
            {"q": "What database URI is best for isolated unit tests?", "options": ["postgresql://localhost/test", "mysql://localhost/test", "sqlite:///:memory:", "sqlite:///test.db"], "answer": "sqlite:///:memory:"},
        ],
    ),
    "flask_cookies": make_topic(
        intro="""<p><strong>Cookies</strong> are small pieces of data stored in the user's browser and sent with every subsequent request to the server. Flask provides straightforward APIs to set, read, and delete cookies. The Flask <strong>session</strong> object is a special cookie — cryptographically signed with your <code>SECRET_KEY</code> — making it tamper-proof. Understanding cookies and sessions is fundamental for login state, shopping carts, user preferences, and multi-step forms.</p>""",
        subtopics=[
            {"title": "Setting & Reading Cookies", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import request, make_response\n\n@app.route('/set-theme')\ndef set_theme():\n    resp = make_response('Theme saved!')\n    resp.set_cookie('theme', 'dark', max_age=30*24*3600)  # 30 days\n    return resp\n\n@app.route('/get-theme')\ndef get_theme():\n    theme = request.cookies.get('theme', 'light')\n    return f'Your theme: {theme}'</pre>"},
            {"title": "Flask Sessions", "content": "<p>The <code>session</code> object behaves like a Python dict but is stored in a signed cookie. Set <code>app.secret_key</code> to a strong random string. Session data is visible to the client (base64-encoded JSON) but cannot be tampered with — the signature prevents modification.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>from flask import session\n\nsession['user_id'] = user.id    # set\nuid = session.get('user_id')     # read\nsession.pop('user_id', None)    # delete</pre>"},
        ],
        key_concepts="<ul><li>Cookies: client-side storage, sent automatically with every request to the domain.</li><li>Session: server-managed (via signed cookie); secure against tampering.</li><li><code>max_age</code> — cookie lifetime in seconds; <code>httponly=True</code> — prevents JS access.</li><li><code>secure=True</code> — cookie only sent over HTTPS (required in production).</li><li>Server-side sessions (Flask-Session) store data in Redis/DB for larger payloads.</li></ul>",
        examples=[
            {"title": "Cart Using Session", "code": "@app.route('/cart/add/&lt;item&gt;')\ndef add_to_cart(item):\n    cart = session.get('cart', [])\n    cart.append(item)\n    session['cart'] = cart\n    return f'Cart: {cart}'\n\n@app.route('/cart')\ndef view_cart():\n    cart = session.get('cart', [])\n    return f'Items: {cart}'", "output": "GET /cart/add/apple → Cart: ['apple']\nGET /cart/add/banana → Cart: ['apple', 'banana']\nGET /cart → Items: ['apple', 'banana']", "explanation": "<p>Session persists the cart list across requests without a database — ideal for small, ephemeral state.</p>"},
        ],
        quiz=[
            {"q": "Flask sessions are stored in:", "options": ["Server memory", "A signed cookie", "The database", "localStorage"], "answer": "A signed cookie"},
            {"q": "Which cookie attribute prevents JavaScript from reading the cookie?", "options": ["secure", "httponly", "samesite", "readonly"], "answer": "httponly"},
        ],
    ),
    "flask_sockets": make_topic(
        intro="""<p><strong>WebSockets</strong> provide a persistent, full-duplex communication channel between the browser and server — unlike HTTP's request-response model, WebSockets let the server push data to clients instantly without polling. This powers real-time features: live chat, notifications, collaborative editing, and live dashboards. <strong>Flask-SocketIO</strong> is the standard extension that integrates Socket.IO (a WebSocket abstraction) with Flask, providing fallbacks to long-polling for older browsers.</p>""",
        subtopics=[
            {"title": "Setup & Basic Events", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>pip install flask-socketio\n\nfrom flask_socketio import SocketIO, emit\nsocketio = SocketIO(app, cors_allowed_origins='*')\n\n@socketio.on('connect')\ndef handle_connect():\n    emit('status', {'msg': 'Connected!'})\n\n@socketio.on('message')\ndef handle_message(data):\n    emit('broadcast', {'text': data['text']}, broadcast=True)\n\nif __name__ == '__main__':\n    socketio.run(app, debug=True)</pre>"},
            {"title": "Client-Side (JavaScript)", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>// Browser\nconst socket = io();\nsocket.on('broadcast', (data) => {\n    document.getElementById('chat').innerHTML += `&lt;p&gt;${data.text}&lt;/p&gt;`;\n});\ndocument.getElementById('send').onclick = () => {\n    socket.emit('message', {text: document.getElementById('msg').value});\n};</pre>"},
        ],
        key_concepts="<ul><li><strong>WebSocket</strong> — persistent TCP connection; bidirectional, low-latency.</li><li><strong>Event-based</strong> — <code>@socketio.on('event_name')</code> handles events from clients.</li><li><code>emit('event', data)</code> — send to one client; <code>broadcast=True</code> — send to all clients.</li><li><strong>Rooms</strong> — group clients into named channels; useful for chat rooms.</li><li>Use <code>eventlet</code> or <code>gevent</code> as async worker with <code>socketio.run()</code>.</li></ul>",
        examples=[
            {"title": "Simple Chat Server", "code": "from flask import Flask, render_template\nfrom flask_socketio import SocketIO, emit\n\napp = Flask(__name__)\nsocketio = SocketIO(app)\n\n@socketio.on('chat')\ndef handle_chat(msg):\n    emit('chat', msg, broadcast=True)  # relay to all clients\n\nif __name__ == '__main__':\n    socketio.run(app, debug=True)", "output": "All connected clients receive messages in real time.", "explanation": "<p>Any message sent by one client is instantly broadcast to all others — the foundation of live chat.</p>"},
        ],
        quiz=[
            {"q": "What makes WebSockets different from regular HTTP?", "options": ["They use UDP", "They are persistent bidirectional connections", "They require authentication", "They only work on HTTPS"], "answer": "They are persistent bidirectional connections"},
            {"q": "To send a message to ALL connected clients in Flask-SocketIO:", "options": ["emit('event', data)", "emit('event', data, broadcast=True)", "broadcast('event', data)", "send_all('event', data)"], "answer": "emit('event', data, broadcast=True)"},
        ],
    ),
    "flask_practices": make_topic(
        intro="""<p>Professional Flask development goes beyond getting code to run — it involves applying <strong>design patterns</strong>, following <strong>security best practices</strong>, maintaining <strong>code quality</strong>, and ensuring <strong>performance</strong> at scale. This section covers the patterns and practices used by experienced Flask developers at companies building production APIs and web applications: the Application Factory, configuration management, input validation, rate limiting, caching, and API versioning.</p>""",
        subtopics=[
            {"title": "Application Factory Pattern", "content": "<p>Always create your Flask app inside a function, not at module level. This allows multiple configurations (testing, development, production) and prevents circular import issues.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>def create_app(config='config.ProductionConfig'):\n    app = Flask(__name__)\n    app.config.from_object(config)\n    db.init_app(app)\n    login_manager.init_app(app)\n    app.register_blueprint(auth_bp)\n    return app</pre>"},
            {"title": "Input Validation", "content": "<p>Never trust user input. Validate request data with <strong>Marshmallow</strong> or <strong>Cerberus</strong> schemas. Reject invalid requests with 400 status before they touch the database.</p>"},
            {"title": "Security Essentials", "content": "<ul><li>Set <code>SESSION_COOKIE_SECURE=True</code> and <code>SESSION_COOKIE_HTTPONLY=True</code>.</li><li>Use <strong>Flask-Limiter</strong> for rate limiting (prevent brute force).</li><li>Enable <strong>CSRF protection</strong> (Flask-WTF) for all state-changing forms.</li><li>Use <code>get_or_404()</code> — don't reveal whether records exist to unauthorised users.</li><li>Pin your dependencies with <code>pip freeze > requirements.txt</code>.</li></ul>"},
        ],
        key_concepts="<ul><li>Use environment-specific config classes (Dev, Test, Prod).</li><li>Log errors to Sentry in production; never print sensitive data.</li><li>Use Flask-Caching for expensive query results.</li><li>Version your API: <code>/api/v1/</code> allows breaking changes without disrupting clients.</li><li>Write tests — aim for >80% coverage on your routes and service layer.</li></ul>",
        examples=[
            {"title": "Rate Limiting with Flask-Limiter", "code": "from flask_limiter import Limiter\nfrom flask_limiter.util import get_remote_address\n\nlimiter = Limiter(app, key_func=get_remote_address)\n\n@app.route('/api/login', methods=['POST'])\n@limiter.limit('5 per minute')  # max 5 login attempts per minute\ndef login():\n    ...", "output": "6th request in a minute → 429 Too Many Requests", "explanation": "<p>Rate limiting is essential for login, registration, and any public API to prevent abuse.</p>"},
        ],
        quiz=[
            {"q": "What is the primary benefit of the Application Factory pattern?", "options": ["Faster startup", "Allows multiple app configurations and avoids circular imports", "Automatic database setup", "Built-in rate limiting"], "answer": "Allows multiple app configurations and avoids circular imports"},
            {"q": "Which header attribute prevents cookie access from JavaScript?", "options": ["Secure", "SameSite", "HttpOnly", "CORS"], "answer": "HttpOnly"},
        ],
    ),
    "flask_interview": make_topic(
        intro="""<p>Flask interview questions test your understanding of the framework's design, its ecosystem of extensions, production considerations, and comparison with alternatives like Django FastAPI. Interviewers look for candidates who understand <em>why</em> Flask is minimal and can discuss what that means for architecture choices — not just those who have used it superficially. This section covers the most commonly asked Flask interview questions in backend development roles.</p>""",
        subtopics=[
            {"title": "Flask vs Django vs FastAPI", "content": "<ul><li><strong>Flask</strong>: micro-framework, maximum flexibility, great for APIs and custom architectures. You choose your own ORM, auth library, etc.</li><li><strong>Django</strong>: batteries-included (ORM, admin panel, auth built-in), excellent for data-heavy CRUD apps with a standard structure. Less flexible but faster to scaffold.</li><li><strong>FastAPI</strong>: async-native, automatic OpenAPI docs, type-hint-driven validation, fastest Python web framework. Ideal for high-performance APIs and microservices.</li></ul>"},
            {"title": "Common Flask Interview Questions", "content": "<ul><li><strong>Q:</strong> What is the difference between <code>request.args</code> and <code>request.form</code>?<br><strong>A:</strong> <code>args</code> for GET query parameters; <code>form</code> for POST form data.</li><li><strong>Q:</strong> How do you prevent SQL injection in Flask?<br><strong>A:</strong> Use SQLAlchemy ORM or parameterised queries — never string-interpolate user input into SQL.</li><li><strong>Q:</strong> What is a context processor?<br><strong>A:</strong> A function decorated with <code>@app.context_processor</code> that returns a dict of variables available in all templates automatically (e.g., <code>current_user</code>).</li><li><strong>Q:</strong> How do you handle file uploads?<br><strong>A:</strong> Access via <code>request.files</code>; save with <code>file.save(path)</code>; validate file type and size.</li></ul>"},
        ],
        key_concepts="<ul><li>Know the Flask request lifecycle: request received → context pushed → route matched → view called → response returned → context popped.</li><li>Understand <code>@app.before_request</code>, <code>@app.after_request</code>, <code>@app.teardown_appcontext</code>.</li><li>Know how to create a Flask extension (relies on <code>init_app()</code> pattern).</li><li>Explain the difference between <code>session</code> and <code>g</code>.</li></ul>",
        examples=[
            {"title": "Context Processor Example", "code": "@app.context_processor\ndef inject_user():\n    from flask_login import current_user\n    return dict(user=current_user)\n\n# Now in ANY template:\n# {% if user.is_authenticated %}\n#   Hello, {{ user.username }}!\n# {% endif %}", "output": "User object available in all templates without explicit passing.", "explanation": "<p>Context processors are Flask's elegant solution for globally available template variables — a very common interview topic.</p>"},
        ],
        quiz=[
            {"q": "What does a Flask context processor do?", "options": ["Handles request errors", "Manages database connections", "Injects variables into all templates automatically", "Processes form data"], "answer": "Injects variables into all templates automatically"},
            {"q": "To prevent SQL injection in Flask, you should:", "options": ["Escape all strings manually", "Use parameterised queries or an ORM", "Validate input length only", "Use HTTPS"], "answer": "Use parameterised queries or an ORM"},
        ],
    ),
}

# ─────────────────────────────────────────────
# TYPESCRIPT & JAVASCRIPT FIXES
# ─────────────────────────────────────────────
TYPESCRIPT_FIXES = {
    "typescript_basics": make_topic(
        intro="""<p><strong>TypeScript</strong> is a strongly-typed <em>superset</em> of JavaScript developed by Microsoft. That means all valid JavaScript is also valid TypeScript, but TypeScript adds a powerful optional type system that is stripped away when compiled to plain JavaScript. TypeScript's compiler (<code>tsc</code>) catches type errors, undefined property accesses, and incorrect function calls <strong>at compile time</strong> — before your code ever runs. It's now the de-facto standard for large JavaScript codebases, and is the default language of Angular, NestJS, and heavily adopted in React projects.</p>""",
        subtopics=[
            {"title": "Type Annotations", "content": "<p>Add a <code>: type</code> annotation after any variable, parameter, or return value. TypeScript can also <strong>infer</strong> the type automatically when a value is assigned.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>let name: string = 'TypeScript';\nlet age: number = 5;\nlet isAwesome: boolean = true;\nlet inferred = 42;  // TypeScript infers: number</pre>"},
            {"title": "Compiling TypeScript", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>npm install -g typescript\ntsc hello.ts       # compiles to hello.js\ntsc --watch        # auto-compile on save</pre><p>Configure the compiler via <code>tsconfig.json</code> (target JS version, strictness level, output directory, etc.)</p>"},
            {"title": "TypeScript vs JavaScript", "content": "<p>JavaScript is <em>dynamically typed</em> — a variable can hold anything and type errors happen at runtime. TypeScript is <em>statically typed</em> — the compiler catches type errors at build time. This makes TypeScript safer for large teams, better for IDE autocomplete/refactoring, and much easier to onboard new developers into a complex codebase.</p>"},
        ],
        key_concepts="<ul><li><strong>Type inference</strong> — TypeScript often deduces types without annotations.</li><li><strong>Strict mode</strong> (<code>'strict': true</code> in tsconfig) — enables all safety checks; recommended.</li><li><code>any</code> type — disables type checking; avoid it.</li><li><code>unknown</code> — safer than <code>any</code>; requires type narrowing before use.</li><li><strong>Union types</strong> — <code>string | number</code> means the value can be either type.</li></ul>",
        examples=[
            {"title": "Type Annotations & Functions", "code": 'function greet(name: string, age: number): string {\n    return `Hello, ${name}! You are ${age} years old.`;\n}\n\nconst msg = greet("Alice", 25);\nconsole.log(msg);\n// greet("Bob", "twenty"); // Error: Argument of type \'string\' is not assignable to parameter of type \'number\'', "output": "Hello, Alice! You are 25 years old.", "explanation": "<p>TypeScript catches the wrong argument type at compile time — not at runtime when the damage is done.</p>"},
            {"title": "Union & Literal Types", "code": 'type Direction = "left" | "right" | "up" | "down";\n\nfunction move(dir: Direction, steps: number): void {\n    console.log(`Moving ${dir} by ${steps} steps`);\n}\n\nmove("left", 3);     // OK\n// move("diagonal", 1); // Error: not in union', "output": "Moving left by 3 steps", "explanation": "<p>Union types restrict values to a fixed set — preventing typos and invalid states.</p>"},
        ],
        quiz=[
            {"q": "TypeScript is compiled to:", "options": ["Java bytecode", "Machine code", "JavaScript", "WebAssembly"], "answer": "JavaScript"},
            {"q": "What does TypeScript's 'strict' mode enable?", "options": ["Faster compilation", "All type safety checks", "Automatic testing", "ES6 features"], "answer": "All type safety checks"},
        ],
    ),
}

JAVASCRIPT_FIXES = {
    "js_functions": make_topic(
        intro="""<p><strong>Functions</strong> are the fundamental building blocks of JavaScript programs. A function is a reusable block of code that performs a task and optionally returns a value. JavaScript treats functions as <em>first-class citizens</em> — they can be assigned to variables, passed as arguments to other functions, and returned from functions. This makes JavaScript extremely powerful for functional programming patterns. Modern JavaScript (ES6+) introduced <strong>arrow functions</strong>, <strong>default parameters</strong>, <strong>rest parameters</strong>, and improved <strong>closures</strong> handling.</p>""",
        subtopics=[
            {"title": "Function Declaration vs Expression", "content": "<p><strong>Function declarations</strong> are hoisted — you can call them before they appear in the code. <strong>Function expressions</strong> are not.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>// Declaration (hoisted)\nfunction add(a, b) { return a + b; }\n\n// Expression — NOT hoisted\nconst multiply = function(a, b) { return a * b; };\n\n// Arrow function (ES6)\nconst square = (n) => n * n;</pre>"},
            {"title": "Arrow Functions", "content": "<p>Arrow functions (<code>=></code>) have a concise syntax and <strong>do not have their own <code>this</code></strong> — they inherit <code>this</code> from the surrounding scope. This solves the classic JavaScript <code>this</code> confusion in callbacks and event handlers.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>const greet = name => `Hello, ${name}!`;\nconst add = (a, b) => a + b;\nconst double = n => { return n * 2; }; // multi-line needs {}</pre>"},
            {"title": "Closures", "content": "<p>A <strong>closure</strong> is a function that remembers variables from its parent scope even after the parent function has finished executing. Closures are used for data encapsulation, factory functions, and callback patterns.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>function makeCounter() {\n    let count = 0;\n    return function() {\n        count++;\n        return count;\n    };\n}\nconst counter = makeCounter();\nconsole.log(counter()); // 1\nconsole.log(counter()); // 2</pre>"},
            {"title": "Default & Rest Parameters", "content": "<p><strong>Default parameters</strong> provide fallback values when an argument is undefined. <strong>Rest parameters</strong> (<code>...args</code>) collect all remaining arguments into an array.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>function greet(name = 'Guest') {\n    return `Hello, ${name}!`;\n}\n\nfunction sum(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}\nconsole.log(sum(1, 2, 3, 4, 5));  // 15</pre>"},
        ],
        key_concepts="<ul><li><strong>Hoisting</strong> — function declarations are moved to the top of their scope; expressions are not.</li><li><strong>First-class functions</strong> — functions can be stored in variables, passed as args, returned.</li><li><strong>Higher-order functions</strong> — <code>map</code>, <code>filter</code>, <code>reduce</code> — accept functions as arguments.</li><li><strong>IIFE</strong> — Immediately Invoked Function Expression: <code>(function() {})()</code>.</li><li><strong>Closure</strong> — inner functions retain access to outer scope even after outer returns.</li></ul>",
        examples=[
            {"title": "Closure — Private Counter", "code": "function makeCounter(start = 0) {\n    let count = start;\n    return {\n        increment: () => ++count,\n        decrement: () => --count,\n        value: () => count\n    };\n}\n\nconst c = makeCounter(10);\nconsole.log(c.increment()); // 11\nconsole.log(c.increment()); // 12\nconsole.log(c.decrement()); // 11\nconsole.log(c.value());     // 11", "output": "11\n12\n11\n11", "explanation": "<p>The returned object's methods all close over the same <code>count</code> variable — true private state without a class.</p>"},
            {"title": "Higher-Order Functions", "code": "const numbers = [1, 2, 3, 4, 5, 6];\n\nconst evens = numbers.filter(n => n % 2 === 0);\nconst doubled = evens.map(n => n * 2);\nconst total = doubled.reduce((acc, n) => acc + n, 0);\n\nconsole.log(evens);   // [2, 4, 6]\nconsole.log(doubled); // [4, 8, 12]\nconsole.log(total);   // 24", "output": "[2, 4, 6]\n[4, 8, 12]\n24", "explanation": "<p>Chaining <code>filter</code>, <code>map</code>, and <code>reduce</code> is a core functional programming pattern in modern JavaScript.</p>"},
        ],
        quiz=[
            {"q": "What is a JavaScript closure?", "options": ["A function that closes the browser window", "A function with access to its parent scope's variables after parent returns", "An immediately invoked function", "A function without parameters"], "answer": "A function with access to its parent scope's variables after parent returns"},
            {"q": "Arrow functions differ from regular functions mainly because:", "options": ["They are faster", "They have no 'this' binding of their own", "They can't accept parameters", "They are always async"], "answer": "They have no 'this' binding of their own"},
        ],
    ),
}

def load_data():
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        content = f.read()
    prefix = 'window.tracksData = '
    idx = content.find(prefix)
    raw_json = content[idx + len(prefix):]
    suffix = ''
    if raw_json.strip().endswith(';'):
        raw_json = raw_json.strip()[:-1]
        suffix = ';'
    return content[:idx + len(prefix)], json.loads(raw_json), suffix

def save_data(prefix_content, data, suffix):
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(prefix_content)
        f.write(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
        f.write(suffix)

def apply_fixes(data, lang_key, fixes):
    fixed = 0
    for topic_key, new_content in fixes.items():
        if topic_key in data.get(lang_key, {}).get('content', {}):
            existing = data[lang_key]['content'][topic_key]
            new_content['title'] = existing.get('title', topic_key)
            new_content['phase'] = existing.get('phase', 1)
            data[lang_key]['content'][topic_key] = new_content
            fixed += 1
            print(f"  OK Fixed {lang_key}/{topic_key}")
        else:
            print(f"  ✗ NOT FOUND: {lang_key}/{topic_key}")
    return fixed

if __name__ == '__main__':
    print("Loading tracks_data.js...")
    prefix_content, data, suffix = load_data()
    
    total = 0
    print("\n--- Fixing Flask (18 topics) ---")
    total += apply_fixes(data, 'flask', FLASK_FIXES)
    print("\n--- Fixing TypeScript ---")
    total += apply_fixes(data, 'typescript', TYPESCRIPT_FIXES)
    print("\n--- Fixing JavaScript ---")
    total += apply_fixes(data, 'javascript', JAVASCRIPT_FIXES)
    
    print(f"\nSaving {total} fixes to tracks_data.js...")
    save_data(prefix_content, data, suffix)
    print("Done! OK")
