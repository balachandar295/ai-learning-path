import json

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
json_start = text.find('{')
data = json.loads(text[json_start:text.rfind('}')+1])

def explanation(title, desc, code):
    return f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3><p style='color:#475569;font-size:1.05rem;'>{desc}</p><div style='background:#1e1e2f;border-radius:12px;margin-top:20px;padding:16px;'><pre style='margin:0;color:#e2e8f0;font-family:monospace;'>{code}</pre></div></div>"

def build_track(key, track_title, track_desc, root_icon, topics):
    nodes = []
    content = {}
    
    for i, (nid, title, desc, code) in enumerate(topics):
        phase = (i // 4) + 1
        x = 1250 if i % 2 == 0 else 1530
        y = 150 + i * 160
        
        node = {
            "id": f"{key}_{nid}",
            "title": title,
            "x": x,
            "y": y,
            "status": "available" if i == 0 else "locked",
            "phase": phase
        }
        if i > 0:
            node["parent"] = f"{key}_{topics[i-1][0]}"
        nodes.append(node)
        
        if title == "Interview Guide":
            content[f"{key}_{nid}"] = {
                "title": title,
                "explanation": f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3><p style='color:#475569;font-size:1.05rem;'>Top interview questions for {track_title}. {desc}</p></div>",
                "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
            }
        else:
            content[f"{key}_{nid}"] = {
                "title": title,
                "explanation": explanation(title, desc, code),
                "examples": [],
                "concept_quiz": [{"q": f"What is the core purpose of {title} in {track_title}?", "options": ["Functionality", "UI Styling", "Database", "Networking"], "answer": "Functionality"}],
                "hands_on": {"title": f"Practice {title}", "description": f"Implement the concept of {title}.", "hint": "Use the example code.", "code": code},
                "problem_solving": [{"title": f"Solve using {title}", "description": f"Create a real-world scenario applying {title}.", "code": code}]
            }

    data[key] = {
        "title": track_title,
        "description": track_desc,
        "nodes": nodes,
        "content": content
    }

# Flask
flask_topics = [
    ("basics", "Flask Basics", "Setup a minimalistic Flask web app.", "from flask import Flask\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Hello Flask!'\n\nif __name__=='__main__':\n    app.run()"),
    ("routing", "Routing", "Define application routes.", "@app.route('/user/<username>')\ndef profile(username):\n    return f'User: {username}'"),
    ("templates", "Templates", "Render HTML files.", "from flask import render_template\n@app.route('/')\ndef index():\n    return render_template('index.html')"),
    ("jinja", "Jinja2", "Template engine for dynamic HTML.", "<!-- In template -->\n<h1>Hello {{ name }}</h1>\n{% if is_admin %}<p>Admin Area</p>{% endif %}"),
    ("forms", "Forms", "Handling incoming form data.", "from flask import request\n@app.route('/login', methods=['POST'])\ndef login():\n    user = request.form['username']\n    return 'Logged in'"),
    ("sqlalchemy", "SQLAlchemy", "ORM setup.", "from flask_sqlalchemy import SQLAlchemy\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'\ndb = SQLAlchemy(app)"),
    ("crud", "CRUD", "Create, read, update, delete in database.", "new_user = User(name='Alice')\ndb.session.add(new_user)\ndb.session.commit()"),
    ("auth", "Authentication", "User login sessions.", "from flask_login import login_user\nlogin_user(user)"),
    ("blueprints", "Blueprints", "Modularize Flask apps.", "from flask import Blueprint\nauth_bp = Blueprint('auth', __name__)\n@auth_bp.route('/login'):\n   pass"),
    ("rest", "REST API", "Building APIs.", "from flask import jsonify\n@app.route('/api/data')\ndef api(): return jsonify({'status': 'ok'})"),
    ("errors", "Error Handling", "Custom error pages.", "@app.errorhandler(404)\ndef not_found(e):\n    return render_template('404.html'), 404"),
    ("context", "App Context", "Application vs Request context.", "with app.app_context():\n    db.create_all()"),
    ("deployment", "Deployment", "Gunicorn and production setup.", "pip install gunicorn\ngunicorn wsgi:app"),
    ("testing", "Testing", "Unit testing Flask.", "def test_home(client):\n    res = client.get('/')\n    assert res.status_code == 200"),
    ("cookies", "Cookies", "Session and cookies.", "from flask import session\nsession['user_id'] = 1"),
    ("sockets", "WebSockets", "Flask-SocketIO.", "from flask_socketio import SocketIO\n@socketio.on('message')\ndef handle(msg): pass"),
    ("practices", "Best Practices", "Config structures and factories.", "def create_app():\n    app = Flask(__name__)\n    return app"),
    ("interview", "Interview Guide", "Common questions regarding Flask lifecycle and WSGI.", ""),
]

# TypeScript
ts_topics = [
    ("basics", "TypeScript Basics", "Strict syntactical superset of JavaScript.", "let isDone: boolean = false;\nlet score: number = 100;"),
    ("types", "Static Types", "Basic typing.", "let name: string = 'Alice';\nlet list: number[] = [1, 2, 3];"),
    ("interfaces", "Interfaces", "Object structure definitions.", "interface User {\n    id: number;\n    name: string;\n}\nlet u: User = { id: 1, name: 'Alice' };"),
    ("classes", "Classes", "OOP classes with types.", "class Animal {\n    name: string;\n    constructor(n: string) { this.name = n; }\n}"),
    ("generics", "Generics", "Reusable components for different types.", "function identity<T>(arg: T): T {\n    return arg;\n}"),
    ("enums", "Enums", "Named constants.", "enum Direction {\n    Up = 1,\n    Down,\n    Left,\n    Right\n}"),
    ("assertions", "Type Assertions", "Casting a type.", "let someValue: any = 'this is a string';\nlet strLength: number = (someValue as string).length;"),
    ("advanced", "Advanced Types", "Unions and Intersections.", "let variable: string | number;\nvariable = 'ok'; variable = 1;"),
    ("modules", "Modules", "Importing and exporting.", "export interface Validator { isAcceptable(s: string): boolean; }"),
    ("decorators", "Decorators", "Meta-programming.", "@sealed\nclass BugReport { type = 'report'; }"),
    ("utility", "Utility Types", "Partial, Readonly, Pick.", "type PartialUser = Partial<User>;"),
    ("tsconfig", "tsconfig.json", "Configuring the compiler.", "{\n  \"compilerOptions\": {\n    \"strict\": true\n  }\n}"),
    ("dom", "DOM Typing", "Typing HTML elements.", "const img = document.getElementById('image') as HTMLImageElement;"),
    ("react", "React + TS", "Props and State typing.", "type Props = { title: string };\nconst MyComp: React.FC<Props> = ({title}) => <div>{title}</div>;"),
    ("typeguards", "Type Guards", "Narrowing types.", "if (typeof element === 'string') { element.toUpperCase(); }"),
    ("strict", "Strict Mode", "Preventing implicit any.", "// noImplicitAny: true"),
    ("practices", "Best Practices", "Code organization.", "Always define return types for complex functions."),
    ("interview", "Interview Guide", "Common TS questions.", ""),
]

# Flutter
flutter_topics = [
    ("basics", "Flutter Basics", "UI toolkit for mobile.", "import 'package:flutter/material.dart';\nvoid main() => runApp(MyApp());"),
    ("dart", "Dart Primer", "Dart basics.", "int age = 20;\nString name = 'Alice';"),
    ("widgets", "Widgets", "Everything is a widget.", "Text('Hello World',\n  style: TextStyle(fontSize: 20),\n)"),
    ("layouts", "Layouts", "Rows, Columns, Stacks.", "Column(\n  children: [\n    Text('Top'),\n    Text('Bottom'),\n  ],\n)"),
    ("stateful", "Stateful UI", "Widgets with changing state.", "class Counter extends StatefulWidget { ... }"),
    ("forms", "Forms", "TextFormFields and Validation.", "TextFormField(\n  validator: (val) => val.isEmpty ? 'Required' : null,\n)"),
    ("routes", "Navigation", "Navigating screens.", "Navigator.push(context, MaterialPageRoute(builder: (context) => SecondScreen()));"),
    ("state", "State Management", " setState and beyond.", "setState(() { _counter++; });"),
    ("provider", "Provider", "App-wide state.", "ChangeNotifierProvider(\n  create: (context) => MyModel(),\n)"),
    ("http", "HTTP Requests", "Fetching data from network.", "final res = await http.get('myapi.com/users');"),
    ("json", "JSON Parsing", "Converting map to Dart objects.", "User.fromJson(Map<String,dynamic> json) { ... }"),
    ("sharedpref", "SharedPrefs", "Local storage.", "prefs.setString('token', 'xyz');"),
    ("firebase", "Firebase", "Backend as service integration.", "Firebase.initializeApp();"),
    ("animations", "Animations", "Implicit animations.", "AnimatedContainer(duration: Duration(seconds: 1)...)"),
    ("responsive", "Responsive", "Media queries.", "var width = MediaQuery.of(context).size.width;"),
    ("platform", "Platform Channels", "Calling native code.", "MethodChannel('channel_name').invokeMethod('action');"),
    ("deploy", "Deployment", "Building APKs and AppBundles.", "flutter build apk --release"),
    ("interview", "Interview Guide", "Common Dart/Flutter questions.", ""),
]

# Ruby
ruby_topics = [
    ("basics", "Ruby Basics", "Dynamic, open source language.", "puts 'Hello World'"),
    ("strings", "Strings", "String interpolation.", "name = 'Alice'\nputs \"Hello #{name}\""),
    ("control", "Control Flow", "If, unless, loops.", "if age > 18\n  puts 'Adult'\nend"),
    ("arrays", "Arrays & Hashes", "Data structures.", "arr = [1, 2, 3]\nhash = {name: 'Alice', age: 20}"),
    ("blocks", "Blocks & Yield", "Passing code chunks.", "def do_twice\n  yield\n  yield\nend\ndo_twice { puts 'Hello' }"),
    ("procs", "Procs/Lambdas", "Saved blocks.", "my_proc = Proc.new { puts 'Hi' }\nmy_proc.call"),
    ("classes", "Classes", "OOP in Ruby.", "class User\n  attr_accessor :name\n  def initialize(n)\n    @name = n\n  end\nend"),
    ("modules", "Modules", "Mixins and namespaces.", "module Swimmable\n  def swim; puts 'Swimming'; end\nend"),
    ("exceptions", "Exceptions", "Error handling.", "begin\n  1 / 0\nrescue ZeroDivisionError => e\n  puts e.message\nend"),
    ("file", "File I/O", "Reading files.", "File.open('test.txt', 'w') { |f| f.write('Data') }"),
    ("regex", "Regular Expressions", "Pattern matching.", "if text =~ /[a-z]/ \n  puts 'Has lowercase'\nend"),
    ("rails", "Ruby on Rails", "Web framework.", "rails new blog\nrails server"),
    ("activerecord", "ActiveRecord", "ORM magic.", "user = User.find_by(name: 'Alice')"),
    ("mvc", "MVC Pattern", "Rails standard.", "class UsersController < ApplicationController\nend"),
    ("gems", "Gems", "Ruby packaging.", "gem install bundler"),
    ("rspec", "Testing (RSpec)", "TDD.", "expect(2 + 2).to eq(4)"),
    ("metaprogramming", "Metaprogramming", "Writing code that writes code.", "define_method(:say_hi) { 'Hi!' }"),
    ("interview", "Interview Guide", "Ruby top questions.", ""),
]

build_track('flask', 'Flask - Micro Python Framework', 'Learn the lightweight WSGI web application framework.', 'fa-flask', flask_topics)
build_track('typescript', 'TypeScript - Superset of JS', 'Learn static typing for massive Javascript scale.', 'fa-js-square', ts_topics)
build_track('flutter', 'Flutter - UI Toolkit', 'Build natively compiled applications for mobile.', 'fa-mobile-alt', flutter_topics)
build_track('ruby', 'Ruby - Elegant Language', 'A programmer\'s best friend.', 'fa-gem', ruby_topics)

new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Flask, TypeScript, Flutter, Ruby content globally generated!")
