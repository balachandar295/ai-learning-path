import json

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

json_start = text.find('{')
json_end = text.rfind('}') + 1
data = json.loads(text[json_start:json_end])

# ========== JAVASCRIPT TRACK ==========
js_nodes_raw = [
    ("js_basics", "JS Basics", 1),
    ("js_variables", "Variables & Data Types", 1),
    ("js_operators", "Operators", 1),
    ("js_control_flow", "Control Flow", 1),
    ("js_loops", "Loops", 1),
    ("js_functions", "Functions", 2),
    ("js_arrays", "Arrays", 2),
    ("js_objects", "Objects", 2),
    ("js_strings", "Strings", 2),
    ("js_dom", "DOM Manipulation", 2),
    ("js_events", "Events", 3),
    ("js_es6", "ES6+ Features", 3),
    ("js_promises", "Promises & Async", 3),
    ("js_modules", "Modules", 3),
    ("js_oop", "OOP in JS", 3),
    ("js_error", "Error Handling", 4),
    ("js_advanced", "Advanced Concepts", 4),
    ("js_interview", "JS Interview Guide", 5),
]

js_nodes = []
for i, (nid, title, phase) in enumerate(js_nodes_raw):
    node = {
        "id": nid, "title": title,
        "x": 1250 if i % 2 == 0 else 1530,
        "y": 150 + i * 160,
        "status": "available" if i == 0 else "locked",
        "phase": phase
    }
    if i > 0:
        node["parent"] = js_nodes_raw[i-1][0]
    js_nodes.append(node)

def make_explanation(title, subtopics):
    html = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.8rem;border-bottom:2px solid #e0f2fe;padding-bottom:12px;margin-bottom:20px;'>{title}</h3>"
    for sub_title, sub_text, examples in subtopics:
        html += f"<h4 style='color:#0ea5e9;font-size:1.35rem;margin-top:35px;'>{sub_title}</h4>"
        html += f"<p style='color:#475569;font-size:1.05rem;margin-bottom:15px;'>{sub_text}</p>"
        for ex_label, ex_code in examples:
            html += f"<div style='background:#f8fafc;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #e0f2fe;'><div style='background:linear-gradient(to right,#0ea5e9,#3b82f6);padding:8px 15px;color:white;font-size:0.85rem;font-weight:600;font-family:monospace;'>{ex_label}</div><pre style='margin:0;padding:15px 20px;color:#0f172a;font-family:monospace;font-size:0.95rem;overflow-x:auto;'><code>{ex_code}</code></pre></div>"
    html += "</div>"
    return html

js_content = {
    "js_basics": {
        "title": "JavaScript Basics",
        "explanation": make_explanation("JavaScript Basics", [
            ("What is JavaScript?", "JavaScript is a lightweight, interpreted programming language with first-class functions. It is most well-known as the scripting language for Web pages.", [
                ("Example 1", "console.log('Hello, World!');"),
                ("Example 2", "// JS runs in browser or Node.js\nalert('Welcome to JavaScript!');")
            ]),
            ("Where to write JS?", "JavaScript can be written in HTML \\<script\\> tags or in external .js files.", [
                ("Example 1", "<script>\\n  console.log('Inline JS');\\n</script>"),
                ("Example 2", "// external file: script.js\\nconsole.log('External JS file');")
            ])
        ]),
        "examples": [],
        "concept_quiz": [
            {"q": "What does console.log() do?", "options": ["Opens browser console", "Prints output to console", "Logs errors only", "Creates a variable"], "answer": "Prints output to console"},
            {"q": "JavaScript is primarily used for?", "options": ["Database design", "Server configuration", "Web interactivity", "Hardware programming"], "answer": "Web interactivity"},
            {"q": "Which tag includes JS in HTML?", "options": ["<js>", "<javascript>", "<script>", "<code>"], "answer": "<script>"},
            {"q": "JS is a __ language.", "options": ["Compiled", "Interpreted", "Assembly", "Binary"], "answer": "Interpreted"},
            {"q": "Who created JavaScript?", "options": ["Bjarne Stroustrup", "Guido van Rossum", "Brendan Eich", "James Gosling"], "answer": "Brendan Eich"},
        ],
        "hands_on": {"title": "Your First JS Program", "description": "Write a JS program that logs your name and age to the console.", "hint": "Use console.log() with a template literal.", "code": "const name = 'Alice';\nconst age = 20;\nconsole.log(`My name is ${name} and I am ${age} years old.`);"},
        "problem_solving": [
            {"title": "Hello World", "description": "Write a JS program that outputs 'Hello, World!' to the console.", "code": "console.log('Hello, World!');"},
            {"title": "Sum of Two Numbers", "description": "Given a=5 and b=10, print their sum.", "code": "const a = 5, b = 10;\nconsole.log('Sum:', a + b);"},
        ]
    },
    "js_variables": {
        "title": "Variables & Data Types",
        "explanation": make_explanation("Variables & Data Types", [
            ("var, let, const", "JavaScript has three ways to declare variables. 'var' is function-scoped. 'let' and 'const' are block-scoped. Always prefer 'const' by default.", [
                ("Example 1", "let name = 'John';\nconst PI = 3.14;\nvar age = 25;"),
                ("Example 2", "const city = 'Chennai';\n// city = 'Delhi'; // Error! const can't reassign")
            ]),
            ("Data Types", "JavaScript has 7 primitive types: string, number, boolean, null, undefined, symbol, bigint. Plus objects.", [
                ("Example 1", "let str = 'hello';    // string\nlet num = 42;         // number\nlet bool = true;      // boolean\nlet n = null;         // null\nlet u = undefined;    // undefined"),
                ("Example 2", "console.log(typeof 'hi');   // string\nconsole.log(typeof 42);    // number\nconsole.log(typeof true);  // boolean"),
            ])
        ]),
        "examples": [],
        "concept_quiz": [
            {"q": "Which keyword creates a block-scoped constant?", "options": ["var", "let", "const", "def"], "answer": "const"},
            {"q": "What is the output of typeof null?", "options": ["null", "undefined", "object", "string"], "answer": "object"},
            {"q": "Which is NOT a JavaScript primitive?", "options": ["string", "number", "array", "boolean"], "answer": "array"},
            {"q": "let vs var difference is?", "options": ["Speed", "Scope", "Syntax", "None"], "answer": "Scope"},
            {"q": "What does undefined mean?", "options": ["Variable deleted", "Variable declared but not assigned", "Variable is null", "Variable is zero"], "answer": "Variable declared but not assigned"},
        ],
        "hands_on": {"title": "Variables Practice", "description": "Create variables for your name, age, and isStudent. Print them using a template literal.", "hint": "Use const for name, let for age, const for isStudent.", "code": "const name = 'Bala';\nlet age = 21;\nconst isStudent = true;\nconsole.log(`${name} is ${age} years old. Student: ${isStudent}`);"},
        "problem_solving": [
            {"title": "Type Checker", "description": "Create 3 variables of different types and print typeof for each.", "code": "const a = 'hello';\nconst b = 42;\nconst c = true;\nconsole.log(typeof a, typeof b, typeof c);"},
            {"title": "Swap Variables", "description": "Swap the values of two variables without a third.", "code": "let x = 5, y = 10;\n[x, y] = [y, x];\nconsole.log('x:', x, 'y:', y);"},
        ]
    },
}

# Fill remaining JS nodes with minimal content
for nid, title, phase in js_nodes_raw[2:]:
    if nid not in js_content:
        js_content[nid] = {
            "title": title,
            "explanation": make_explanation(title, [
                (f"Introduction to {title}", f"{title} is a key JavaScript concept that every developer must master.", [
                    ("Example 1", f"// {title} example\nconsole.log('Learning {title}');"),
                    ("Example 2", f"// Practice {title}\n// Write your code here")
                ])
            ]),
            "examples": [],
            "concept_quiz": [
                {"q": f"What is {title} in JavaScript?", "options": ["A data type", "A core JS concept", "A library", "A framework"], "answer": "A core JS concept"},
                {"q": f"Is {title} important for web dev?", "options": ["Yes", "No", "Maybe", "Not relevant"], "answer": "Yes"},
            ],
            "hands_on": {"title": f"Practice {title}", "description": f"Practice the {title} concept in JavaScript.", "hint": f"Refer to the explanation above.", "code": f"// {title} solution\nconsole.log('{title} practice complete!');"},
            "problem_solving": [
                {"title": f"{title} Problem", "description": f"Solve a practical problem related to {title}.", "code": f"// Solution for {title}\nconsole.log('Solved!');"}
            ]
        }

# Interview Guide
js_content["js_interview"] = {
    "title": "JavaScript Interview Guide",
    "explanation": "<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.8rem;'>Top JavaScript Interview Questions</h3><p style='color:#475569;font-size:1.1rem;margin-bottom:30px;'>Most asked JS interview questions from companies like Google, Amazon, Infosys, TCS.</p>" +
        "".join([f"<div style='background:#f8fafc;border-left:4px solid #3b82f6;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#3b82f6;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
        for i, (q, a) in enumerate([
            ("What is hoisting?", "Hoisting is JavaScript's default behavior of moving declarations to the top of the current scope before code execution."),
            ("What is a closure?", "A closure is a function that has access to its outer scope variables even after the outer function has returned."),
            ("Difference between == and ===?", "== compares values with type coercion. === compares values AND types strictly without coercion."),
            ("What is the event loop?", "The event loop is the mechanism that handles asynchronous callbacks in JavaScript, allowing non-blocking execution."),
            ("What is a Promise?", "A Promise is an object representing the eventual completion or failure of an asynchronous operation."),
            ("Explain async/await.", "async/await is syntactic sugar over Promises that makes asynchronous code look and behave like synchronous code."),
            ("What is 'this' in JS?", "'this' refers to the object that is executing the current function. Its value depends on how the function is called."),
            ("What is the prototype chain?", "Every object in JS has a prototype. When a property is not found on an object, JS looks up the prototype chain."),
            ("What is null vs undefined?", "undefined means a variable is declared but not assigned. null is an explicit assignment of 'no value'."),
            ("What is event bubbling?", "Event bubbling is when an event triggered on a child element bubbles up through its parent elements in the DOM."),
        ])]) + "</div>",
    "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
}

# ========== JAVA TRACK ==========
java_nodes_raw = [
    ("java_basics", "Java Basics", 1),
    ("java_variables", "Variables & Types", 1),
    ("java_operators", "Operators", 1),
    ("java_control_flow", "Control Flow", 1),
    ("java_loops", "Loops", 1),
    ("java_arrays", "Arrays", 2),
    ("java_strings", "Strings", 2),
    ("java_methods", "Methods", 2),
    ("java_oop_basics", "OOP Basics", 2),
    ("java_inheritance", "Inheritance", 3),
    ("java_polymorphism", "Polymorphism", 3),
    ("java_interfaces", "Interfaces & Abstract", 3),
    ("java_exceptions", "Exception Handling", 3),
    ("java_collections", "Collections Framework", 4),
    ("java_generics", "Generics", 4),
    ("java_streams", "Streams & Lambda", 4),
    ("java_advanced", "Advanced Java", 4),
    ("java_interview", "Java Interview Guide", 5),
]

java_nodes = []
for i, (nid, title, phase) in enumerate(java_nodes_raw):
    node = {
        "id": nid, "title": title,
        "x": 1250 if i % 2 == 0 else 1530,
        "y": 150 + i * 160,
        "status": "available" if i == 0 else "locked",
        "phase": phase
    }
    if i > 0:
        node["parent"] = java_nodes_raw[i-1][0]
    java_nodes.append(node)

java_content = {
    "java_basics": {
        "title": "Java Basics",
        "explanation": make_explanation("Java Basics", [
            ("What is Java?", "Java is a high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible.", [
                ("Example 1", "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"),
                ("Example 2", "// Java is platform independent via JVM\n// Write Once, Run Anywhere (WORA)")
            ]),
            ("JVM, JDK, JRE", "JDK = Java Development Kit (write + compile). JRE = Java Runtime Environment (run only). JVM = Java Virtual Machine (executes bytecode).", [
                ("Example 1", "// Compile: javac Main.java\n// Run: java Main"),
                ("Example 2", "// Java file structure:\n// package > class > methods")
            ])
        ]),
        "examples": [],
        "concept_quiz": [
            {"q": "Java's compile output is called?", "options": ["Binary", "Bytecode", "Machine code", "Assembly"], "answer": "Bytecode"},
            {"q": "What runs Java bytecode?", "options": ["JDK", "JRE", "JVM", "Compiler"], "answer": "JVM"},
            {"q": "Java entry point method is?", "options": ["start()", "run()", "main()", "init()"], "answer": "main()"},
            {"q": "Java is __ typed.", "options": ["Dynamically", "Statically", "Weakly", "Loosely"], "answer": "Statically"},
            {"q": "Java's OOP paradigm stands for?", "options": ["Object Only Programming", "Object Oriented Programming", "Output Oriented", "None"], "answer": "Object Oriented Programming"},
        ],
        "hands_on": {"title": "Hello World in Java", "description": "Write a Java program that prints 'Hello, World!' to the console.", "hint": "Use System.out.println() inside main method.", "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"},
        "problem_solving": [
            {"title": "Print Your Name", "description": "Write a Java program that prints your name.", "code": "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"My name is Bala\");\n    }\n}"},
            {"title": "Sum Two Numbers", "description": "Write a Java program to print the sum of 5 and 10.", "code": "public class Main {\n    public static void main(String[] args) {\n        int a = 5, b = 10;\n        System.out.println(\"Sum: \" + (a + b));\n    }\n}"},
        ]
    },
}

# Fill remaining Java nodes with minimal content  
for nid, title, phase in java_nodes_raw[1:]:
    if nid not in java_content:
        java_content[nid] = {
            "title": title,
            "explanation": make_explanation(title, [
                (f"Introduction to {title}", f"{title} is a fundamental Java concept every developer must learn.", [
                    ("Example 1", f"// {title} in Java\nSystem.out.println(\"Learning {title}\");"),
                    ("Example 2", f"// Practice {title}\n// Add your code below")
                ])
            ]),
            "examples": [],
            "concept_quiz": [
                {"q": f"What is {title}?", "options": ["A Java concept", "A Python module", "A database", "A web framework"], "answer": "A Java concept"},
                {"q": f"Is {title} important in Java?", "options": ["Yes", "No", "Only sometimes", "Not sure"], "answer": "Yes"},
            ],
            "hands_on": {"title": f"Practice {title}", "description": f"Write a Java program demonstrating {title}.", "hint": "Refer to the explanation above.", "code": f"// {title} solution\nSystem.out.println(\"{title} done!\");"},
            "problem_solving": [
                {"title": f"{title} Problem", "description": f"Solve a problem related to {title}.", "code": f"// Solution\nSystem.out.println(\"Solved {title}!\");"}
            ]
        }

# Java Interview
java_content["java_interview"] = {
    "title": "Java Interview Guide",
    "explanation": "<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.8rem;'>Top Java Interview Questions</h3><p style='color:#475569;margin-bottom:30px;'>Most asked Java questions in company interviews — TCS, Infosys, Wipro, Amazon, etc.</p>" +
        "".join([f"<div style='background:#f8fafc;border-left:4px solid #f89820;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#f89820;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
        for i, (q, a) in enumerate([
            ("What is OOP?", "Object Oriented Programming is a paradigm based on objects which contain data (fields) and code (methods). Java's 4 pillars are: Encapsulation, Inheritance, Polymorphism, Abstraction."),
            ("What is the difference between JDK, JRE and JVM?", "JDK is for developers (write+compile). JRE is for running Java apps. JVM is the engine that executes bytecode on any platform."),
            ("What is polymorphism?", "Polymorphism means 'many forms'. It allows one interface to be used for different underlying forms (data types). In Java: compile-time (overloading) and runtime (overriding)."),
            ("What is an interface vs abstract class?", "Interface: all methods abstract by default, supports multiple inheritance. Abstract class: can have concrete methods, single inheritance only."),
            ("What is a constructor?", "A constructor is a special method called when an object is created. It initializes the object's state. It has the same name as the class and no return type."),
            ("Explain the Collections Framework.", "Java Collections Framework provides interfaces (List, Set, Map, Queue) and classes (ArrayList, HashSet, HashMap) to store and manipulate groups of objects."),
            ("What is the difference between ArrayList and LinkedList?", "ArrayList uses a dynamic array (fast random access). LinkedList uses doubly-linked nodes (fast insertion/deletion). ArrayList preferred for read-heavy operations."),
            ("What is exception handling?", "Exception handling manages runtime errors using try-catch-finally blocks. Checked exceptions must be declared. Unchecked exceptions extend RuntimeException."),
            ("What are Java 8 Streams?", "Streams provide a functional approach to process collections. They support operations like filter(), map(), reduce(), collect() in a pipeline fashion."),
            ("What is the HashMap internal structure?", "HashMap uses hashing. The key's hashCode() determines the bucket index. In Java 8+, buckets use linked lists (up to 8 elements) then convert to Red-Black trees."),
        ])]) + "</div>",
    "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
}

# ========== INJECT INTO DATA ==========
data['javascript'] = {
    "title": "JavaScript - Beginner to Advanced",
    "description": "Master JavaScript from basics to advanced concepts including ES6+, DOM, Promises and OOP.",
    "nodes": js_nodes,
    "content": js_content
}

data['java'] = {
    "title": "Java - Beginner to Advanced",
    "description": "Learn Java from basics to advanced including OOP, Collections, Generics and Streams.",
    "nodes": java_nodes,
    "content": java_content
}

# Write back
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print(f"Done! JavaScript ({len(js_nodes)} nodes) + Java ({len(java_nodes)} nodes) tracks injected!")
