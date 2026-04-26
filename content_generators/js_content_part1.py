import json

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

json_start = text.find('{')
json_end = text.rfind('}') + 1
data = json.loads(text[json_start:json_end])

def card(label, code):
    return f"<div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'><div style='background:linear-gradient(to right,#0ea5e9,#3b82f6);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>{label}</div><pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>{code}</pre></div>"

def section(title, desc, examples):
    html = f"<h4 style='color:#0ea5e9;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #0ea5e9;padding-left:12px;'>{title}</h4>"
    html += f"<p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>{desc}</p>"
    for lbl, code in examples:
        html += card(lbl, code)
    return html

def explanation(title, sections):
    html = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections:
        html += section(*s)
    html += "</div>"
    return html

def quiz(items):
    return [{"q": q, "options": opts, "answer": ans} for q, opts, ans in items]

def task(title, desc, hint, code):
    return {"title": title, "description": desc, "hint": hint, "code": code}

def problems(items):
    return [{"title": t, "description": d, "code": c} for t, d, c in items]

# ────────────────────────────────────────────────
# TOPIC 1: JS Basics
# ────────────────────────────────────────────────
data['javascript']['content']['js_basics'] = {
    "title": "JavaScript Basics",
    "explanation": explanation("JavaScript Basics", [
        ("What is JavaScript?",
         "JavaScript (JS) is a lightweight, interpreted programming language. It runs in the browser and on servers (Node.js). JS adds interactivity to web pages — animations, form validation, dynamic content, etc.",
         [("What JS does", "// Without JS: Static HTML\n// With JS: Dynamic, Interactive Web Pages\n\nconsole.log('JavaScript is running!');\nalert('Welcome to JS!');"),
          ("JS versions", "// ES5 (2009) - basic JS\n// ES6 (2015) - modern JS (let/const, arrow functions)\n// ES2020+ - optional chaining, nullish coalescing")]),
        ("Where to Write JS?",
         "You can write JS inline in HTML using &lt;script&gt; tags, or in a separate .js file linked with src attribute.",
         [("Inline JS in HTML", "<!-- Inside HTML file -->\n<script>\n  console.log('Hello from inline JS!');\n</script>"),
          ("External JS file", "<!-- In HTML -->\n<script src='app.js'></script>\n\n// In app.js file:\nconsole.log('Hello from external file!');")]),
        ("console.log() and Variables",
         "console.log() prints output to the browser's developer console. Use F12 → Console tab to see it.",
         [("Basic output", "console.log('Hello, World!');\nconsole.log(42);\nconsole.log(true);\nconsole.log(3.14);"),
          ("Multiple values", "let name = 'Alice';\nlet age = 20;\nconsole.log('Name:', name, '| Age:', age);\n// Output: Name: Alice | Age: 20")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does console.log() do?", ["Creates a variable", "Prints to browser console", "Shows an alert", "Closes the tab"], "Prints to browser console"),
        ("Which tag is used to write JS in HTML?", ["<js>", "<code>", "<script>", "<java>"], "<script>"),
        ("JavaScript runs in which environment?", ["Only browser", "Only server", "Both browser and server (Node.js)", "Only desktop apps"], "Both browser and server (Node.js)"),
        ("What does ES6 introduce?", ["alert()", "let and const", "console.log", "HTML tags"], "let and const"),
        ("Which company created JavaScript?", ["Microsoft", "Google", "Netscape", "Apple"], "Netscape"),
    ]),
    "hands_on": task("Hello World Program", "Write a JavaScript program that logs 'Hello, World!' and your name to the console.", "Use console.log() twice or use a template literal.", "console.log('Hello, World!');\nlet name = 'Your Name';\nconsole.log('My name is: ' + name);"),
    "problem_solving": problems([
        ("Print Greeting", "Print 'Good Morning, JavaScript!' to the console.", "console.log('Good Morning, JavaScript!');"),
        ("Sum of Two", "Store 15 and 25 in variables. Print their sum.", "let a = 15;\nlet b = 25;\nconsole.log('Sum:', a + b);"),
        ("Personal Info", "Print your name, city, and age in one console.log using + operator.", "let name='Bala', city='Chennai', age=21;\nconsole.log('Name: '+name+', City: '+city+', Age: '+age);"),
    ])
}

# ────────────────────────────────────────────────
# TOPIC 2: Variables & Data Types
# ────────────────────────────────────────────────
data['javascript']['content']['js_variables'] = {
    "title": "Variables & Data Types",
    "explanation": explanation("Variables & Data Types", [
        ("var, let, const",
         "<b>var</b>: function-scoped, hoisted (old way — avoid it). <b>let</b>: block-scoped, can be reassigned. <b>const</b>: block-scoped, cannot be reassigned (use it by default).",
         [("Declaring variables", "var oldWay = 'avoid this';\nlet score = 100;        // can change\nconst PI = 3.14159;     // cannot change\n\nscore = 200;            // OK\n// PI = 3;              // ERROR!"),
          ("Block scope example", "{\n  let x = 10;\n  const y = 20;\n  console.log(x, y);  // 10 20\n}\n// console.log(x);  // ERROR - not accessible outside block")]),
        ("Primitive Data Types",
         "JS has 7 primitive types. They are immutable and stored by value.",
         [("6 common primitives", "let str    = 'Hello';      // String\nlet num    = 42;           // Number\nlet float  = 3.14;         // Number (no separate float)\nlet bool   = true;         // Boolean\nlet empty  = null;         // Null (intentional empty)\nlet undef  = undefined;    // Undefined (not assigned)\nlet big    = 9007199n;     // BigInt"),
          ("typeof operator", "console.log(typeof 'hi');        // 'string'\nconsole.log(typeof 42);         // 'number'\nconsole.log(typeof true);       // 'boolean'\nconsole.log(typeof undefined);  // 'undefined'\nconsole.log(typeof null);       // 'object' (JS bug!)\nconsole.log(typeof {});         // 'object'")]),
        ("Type Conversion",
         "JavaScript can convert types automatically (implicit) or you can do it manually (explicit).",
         [("Explicit conversion", "// String to Number\nlet n = Number('42');       // 42\nlet n2 = parseInt('10px');  // 10\n\n// Number to String\nlet s = String(100);        // '100'\nlet s2 = (100).toString();  // '100'\n\n// To Boolean\nlet b = Boolean(0);         // false\nlet b2 = Boolean('hello');  // true"),
          ("Implicit coercion (tricky!)", "console.log('5' + 2);   // '52' (string concat)\nconsole.log('5' - 2);   // 3  (numeric)\nconsole.log(true + 1);  // 2\nconsole.log(false + 1); // 1\nconsole.log('' == false); // true (loose ==)")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which keyword creates a block-scoped constant?", ["var", "let", "const", "define"], "const"),
        ("What is typeof null in JavaScript?", ["null", "undefined", "object", "string"], "object"),
        ("Which is NOT a primitive type?", ["string", "boolean", "object", "number"], "object"),
        ("What does Number('abc') return?", ["0", "null", "NaN", "Error"], "NaN"),
        ("What is the result of '5' + 3?", ["8", "'53'", "53", "Error"], "'53'"),
    ]),
    "hands_on": task("Type Explorer", "Create variables of 5 different types. Print each with its typeof result.", "Use a template literal: `${typeof x}`", "const str  = 'Hello';\nconst num  = 42;\nconst bool = true;\nconst nothing = null;\nconst undef = undefined;\n\nconsole.log(`str: ${typeof str}`);\nconsole.log(`num: ${typeof num}`);\nconsole.log(`bool: ${typeof bool}`);\nconsole.log(`null: ${typeof nothing}`);\nconsole.log(`undef: ${typeof undef}`);"),
    "problem_solving": problems([
        ("Swap Variables", "Swap two variables a=5, b=10 without a third variable. Print both.", "let a = 5, b = 10;\n[a, b] = [b, a];\nconsole.log('a:', a, 'b:', b);"),
        ("Check Type", "Ask user type of a variable. Store 42.5 and tell if it's integer or float.", "let n = 42.5;\nif (Number.isInteger(n)) {\n  console.log('It is an integer');\n} else {\n  console.log('It is a float');\n}"),
        ("String to Number", "Convert '25' and '30' to numbers, add them, print result.", "let a = Number('25');\nlet b = Number('30');\nconsole.log('Sum:', a + b);"),
    ])
}

# ────────────────────────────────────────────────
# TOPIC 3: Operators
# ────────────────────────────────────────────────
data['javascript']['content']['js_operators'] = {
    "title": "Operators",
    "explanation": explanation("Operators", [
        ("Arithmetic Operators",
         "Used for mathematical calculations: + (add), - (subtract), * (multiply), / (divide), % (modulus), ** (power), ++ (increment), -- (decrement).",
         [("Basic math", "let a = 10, b = 3;\nconsole.log(a + b);  // 13\nconsole.log(a - b);  // 7\nconsole.log(a * b);  // 30\nconsole.log(a / b);  // 3.333...\nconsole.log(a % b);  // 1 (remainder)\nconsole.log(a ** b); // 1000 (10^3)"),
          ("Increment / Decrement", "let x = 5;\nconsole.log(x++); // 5 (post: use then increment)\nconsole.log(x);   // 6\nconsole.log(++x); // 7 (pre: increment then use)\nconsole.log(x--); // 7 (post: use then decrement)\nconsole.log(x);   // 6")]),
        ("Comparison & Logical Operators",
         "<b>Comparison</b>: == (loose equal), === (strict equal), !=, !==, &gt;, &lt;, &gt;=, &lt;=. <b>Logical</b>: && (AND), || (OR), ! (NOT).",
         [("Comparison", "console.log(5 == '5');   // true  (loose: type coercion)\nconsole.log(5 === '5');  // false (strict: type must match)\nconsole.log(10 > 5);    // true\nconsole.log(10 !== 5);  // true\n\n// Always prefer === over =="),
          ("Logical operators", "let age = 20;\nlet hasID = true;\n\nif (age >= 18 && hasID) {\n  console.log('Allowed');\n}\n\nconsole.log(false || true);  // true\nconsole.log(!true);          // false")]),
        ("Assignment & Ternary",
         "Assignment: = (assign), +=, -=, *=, /=. Ternary is a one-line if-else: condition ? valueIfTrue : valueIfFalse.",
         [("Assignment operators", "let n = 10;\nn += 5;  // n = 15\nn -= 3;  // n = 12\nn *= 2;  // n = 24\nn /= 4;  // n = 6\nn %= 4;  // n = 2\nconsole.log(n);"),
          ("Ternary operator", "let age = 20;\nlet status = age >= 18 ? 'Adult' : 'Minor';\nconsole.log(status); // Adult\n\nlet score = 75;\nlet grade = score >= 90 ? 'A' : score >= 75 ? 'B' : 'C';\nconsole.log(grade); // B")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does % operator do?", ["Divide", "Multiply", "Return remainder", "Power"], "Return remainder"),
        ("What is the result of 5 === '5'?", ["true", "false", "undefined", "Error"], "false"),
        ("What does && mean?", ["OR", "NOT", "AND", "XOR"], "AND"),
        ("What does the ternary operator use?", ["if/else keywords", "? and : symbols", "switch/case", "&&and||"], "? and : symbols"),
        ("What is 2 ** 3?", ["6", "8", "9", "5"], "8"),
    ]),
    "hands_on": task("Calculator", "Write a JS program that takes two numbers and prints results of all arithmetic operations.", "Use +, -, *, /, %, ** operators.", "let a = 12, b = 4;\nconsole.log('Add:', a + b);\nconsole.log('Sub:', a - b);\nconsole.log('Mul:', a * b);\nconsole.log('Div:', a / b);\nconsole.log('Mod:', a % b);\nconsole.log('Pow:', a ** b);"),
    "problem_solving": problems([
        ("Odd or Even", "Given n=17, print whether it is odd or even using ternary operator.", "let n = 17;\nconsole.log(n % 2 === 0 ? 'Even' : 'Odd');"),
        ("Grade System", "Given score=82, print grade: A(>=90), B(>=75), C(>=60), D(below 60).", "let score = 82;\nlet grade = score>=90?'A':score>=75?'B':score>=60?'C':'D';\nconsole.log('Grade:', grade);"),
        ("BMI Calculator", "Calculate BMI: weight=70kg, height=1.75m. BMI = weight / (height*height).", "let weight = 70, height = 1.75;\nlet bmi = weight / (height ** 2);\nconsole.log('BMI:', bmi.toFixed(2));"),
    ])
}

# ────────────────────────────────────────────────
# TOPIC 4: Control Flow
# ────────────────────────────────────────────────
data['javascript']['content']['js_control_flow'] = {
    "title": "Control Flow",
    "explanation": explanation("Control Flow", [
        ("if / else if / else",
         "Control flow decides which code block runs based on a condition. It makes your program smart and responsive.",
         [("Basic if-else", "let temperature = 35;\n\nif (temperature > 40) {\n  console.log('Very Hot!');\n} else if (temperature > 30) {\n  console.log('Hot day');\n} else if (temperature > 20) {\n  console.log('Warm');\n} else {\n  console.log('Cool');\n}\n// Output: Hot day"),
          ("Nested if", "let age = 20;\nlet hasLicense = true;\n\nif (age >= 18) {\n  if (hasLicense) {\n    console.log('Can drive!');\n  } else {\n    console.log('Need a license first');\n  }\n} else {\n  console.log('Too young to drive');\n}")]),
        ("switch Statement",
         "switch is cleaner than multiple if-else when checking one variable against many exact values. Don't forget break!",
         [("switch example", "let day = 'Monday';\n\nswitch (day) {\n  case 'Monday':\n    console.log('Start of work week'); break;\n  case 'Friday':\n    console.log('End of work week'); break;\n  case 'Saturday':\n  case 'Sunday':\n    console.log('Weekend!'); break;\n  default:\n    console.log('Regular weekday');\n}"),
          ("switch with numbers", "let choice = 2;\nswitch (choice) {\n  case 1: console.log('Option 1'); break;\n  case 2: console.log('Option 2'); break;\n  case 3: console.log('Option 3'); break;\n  default: console.log('Invalid choice');\n}\n// Output: Option 2")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What keyword handles multiple conditions on same variable cleanly?", ["if", "for", "switch", "while"], "switch"),
        ("What happens if you forget break in switch?", ["Error occurs", "Code stops", "Falls through to next case", "Nothing"], "Falls through to next case"),
        ("if (0) runs the block?", ["Yes", "No", "Sometimes", "Error"], "No"),
        ("What is the else block?", ["Runs when condition is true", "Runs when condition is false", "Always runs", "Never runs"], "Runs when condition is false"),
        ("&& means code runs when?", ["Either condition true", "Both conditions true", "First condition false", "Always"], "Both conditions true"),
    ]),
    "hands_on": task("Traffic Light", "Given a color variable ('red', 'yellow', 'green'), use switch to print the correct traffic instruction.", "Use switch with case for each color.", "let color = 'green';\nswitch (color) {\n  case 'red':    console.log('STOP');  break;\n  case 'yellow': console.log('SLOW DOWN'); break;\n  case 'green':  console.log('GO!');   break;\n  default:       console.log('Invalid color');\n}"),
    "problem_solving": problems([
        ("Voting Eligibility", "Check if age=17 can vote (18+). Print appropriate message.", "let age = 17;\nif (age >= 18) {\n  console.log('You can vote!');\n} else {\n  console.log(`You need ${18 - age} more year(s) to vote.`);\n}"),
        ("Season Finder", "Given month number 1-12, print the season (Spring: 3-5, Summer: 6-8, Autumn: 9-11, Winter: 12,1,2).", "let month = 7;\nif (month>=3 && month<=5) console.log('Spring');\nelse if (month>=6 && month<=8) console.log('Summer');\nelse if (month>=9 && month<=11) console.log('Autumn');\nelse console.log('Winter');"),
        ("Max of Three", "Find the largest among three numbers: a=45, b=78, c=23.", "let a=45, b=78, c=23;\nlet max = a;\nif (b > max) max = b;\nif (c > max) max = c;\nconsole.log('Largest:', max);"),
    ])
}

# ────────────────────────────────────────────────
# TOPIC 5: Loops
# ────────────────────────────────────────────────
data['javascript']['content']['js_loops'] = {
    "title": "Loops",
    "explanation": explanation("Loops", [
        ("for Loop",
         "The for loop runs a block of code a specific number of times. Best when you know how many iterations you need.",
         [("Basic for loop", "for (let i = 1; i <= 5; i++) {\n  console.log('Count:', i);\n}\n// Output: 1, 2, 3, 4, 5"),
          ("Loop with array", "const fruits = ['Apple', 'Banana', 'Cherry'];\nfor (let i = 0; i < fruits.length; i++) {\n  console.log(i + ': ' + fruits[i]);\n}\n// 0: Apple\n// 1: Banana\n// 2: Cherry")]),
        ("while and do...while",
         "while runs as long as condition is true. do...while always runs at least once, then checks condition.",
         [("while loop", "let count = 1;\nwhile (count <= 5) {\n  console.log('Count:', count);\n  count++;\n}\n// Prints 1 through 5"),
          ("do...while", "let n = 1;\ndo {\n  console.log('Number:', n);\n  n++;\n} while (n <= 3);\n// Always runs body first, then checks condition")]),
        ("for...of and for...in",
         "for...of iterates over values of iterable (array, string). for...in iterates over keys of an object.",
         [("for...of (array/string)", "const colors = ['red','green','blue'];\nfor (const color of colors) {\n  console.log(color);\n}\n\nfor (const char of 'Hello') {\n  console.log(char);\n}"),
          ("for...in (object keys)", "const student = {name:'Alice', age:20, city:'Delhi'};\nfor (const key in student) {\n  console.log(`${key}: ${student[key]}`);\n}\n// name: Alice\n// age: 20\n// city: Delhi")]),
        ("break and continue",
         "break exits the loop immediately. continue skips the current iteration and moves to the next.",
         [("break example", "for (let i = 1; i <= 10; i++) {\n  if (i === 5) break;   // stop loop at 5\n  console.log(i);\n}\n// Prints: 1, 2, 3, 4"),
          ("continue example", "for (let i = 1; i <= 6; i++) {\n  if (i % 2 === 0) continue;  // skip even\n  console.log(i);\n}\n// Prints: 1, 3, 5")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which loop always executes at least once?", ["for", "while", "do...while", "for...of"], "do...while"),
        ("for...of iterates over?", ["Object keys", "Array values", "Object values", "Nothing"], "Array values"),
        ("What does break do in a loop?", ["Skips one iteration", "Exits the loop", "Pauses the loop", "Restarts the loop"], "Exits the loop"),
        ("for...in iterates over?", ["Array indexes", "Array values", "Object keys", "Object values"], "Object keys"),
        ("What is the output of: for(let i=0;i<3;i++) console.log(i)?", ["0 1 2 3", "1 2 3", "0 1 2", "0 1 2 3 4"], "0 1 2"),
    ]),
    "hands_on": task("Multiplication Table", "Print the multiplication table of 7 from 1 to 10 using a for loop.", "Use template literal: `7 x ${i} = ${7*i}`", "for (let i = 1; i <= 10; i++) {\n  console.log(`7 x ${i} = ${7 * i}`);\n}"),
    "problem_solving": problems([
        ("Sum 1 to N", "Calculate the sum of numbers from 1 to 100 using a loop.", "let sum = 0;\nfor (let i = 1; i <= 100; i++) sum += i;\nconsole.log('Sum 1 to 100:', sum);"),
        ("Print Even Numbers", "Print all even numbers from 1 to 20 using continue.", "for (let i = 1; i <= 20; i++) {\n  if (i % 2 !== 0) continue;\n  console.log(i);\n}"),
        ("Find Factorial", "Calculate 6! (6 factorial) using a loop.", "let n = 6, factorial = 1;\nfor (let i = 1; i <= n; i++) factorial *= i;\nconsole.log(`${n}! =`, factorial);"),
    ])
}

print("Topics 1-5 done!")

# Write back
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
