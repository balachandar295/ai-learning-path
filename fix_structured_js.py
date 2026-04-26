import json

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

def make_struct(intro, subtopics, key_concepts, examples):
    return {
        "introduction": intro,
        "subtopics": subtopics,
        "key_concepts": key_concepts,
        "examples": examples
    }

def ex(title, code, output, explanation):
    return {"title": title, "code": code, "output": output, "explanation": explanation}

JS = {
"js_basics": make_struct(
    "<p><strong>JavaScript</strong> is the world's most popular programming language and the backbone of web interactivity. Every website you interact with - from clicking buttons to loading dynamic content - is powered by JavaScript running in your browser.</p><p>Originally created in just 10 days by Brendan Eich in 1995, JavaScript has evolved into a powerful, versatile language used for front-end, back-end (Node.js), mobile apps (React Native), and even desktop applications (Electron).</p>",
    [
        {"title": "1. What is JavaScript?", "content": "<p>JavaScript is a <strong>high-level, interpreted, dynamically-typed</strong> programming language. Unlike C or Java, you don't need to compile JavaScript - the browser's engine (like V8 in Chrome) interprets and executes your code in real-time.</p><p>JavaScript is <strong>single-threaded</strong> but uses an <strong>event loop</strong> to handle asynchronous operations efficiently, meaning it can manage multiple tasks without blocking the main thread.</p>"},
        {"title": "2. Running JavaScript", "content": "<p>You can run JavaScript in two main environments:</p><ul><li><strong>Browser Console:</strong> Open DevTools (F12) and type code directly in the Console tab</li><li><strong>Node.js:</strong> Install Node.js to run JavaScript outside the browser using <code>node filename.js</code></li></ul><p>In HTML, JavaScript is embedded using the <code>&lt;script&gt;</code> tag, either inline or by linking an external <code>.js</code> file.</p>"},
        {"title": "3. Your First Program", "content": "<p>The classic first program outputs text to the console. In JavaScript, we use <code>console.log()</code> to print output. Unlike Python's <code>print()</code>, JavaScript uses dot notation because <code>console</code> is an object and <code>log</code> is its method.</p><p>JavaScript statements end with semicolons (optional but recommended) and are case-sensitive - <code>Console.Log</code> would throw an error!</p>"}
    ],
    "<ul><li><strong>Interpreted Language:</strong> No compilation needed - code runs directly in the browser engine</li><li><strong>Dynamic Typing:</strong> Variables can hold any type of data without declaration</li><li><strong>Event-Driven:</strong> JavaScript responds to user actions like clicks, scrolls, and keystrokes</li><li><strong>Prototype-Based OOP:</strong> Uses prototypal inheritance instead of classical class-based inheritance</li></ul>",
    [
        ex("Hello World", 'console.log("Hello, World!");\nconsole.log("Welcome to JavaScript!");', "Hello, World!\nWelcome to JavaScript!", "console.log() prints output to the browser console or terminal. You can pass strings, numbers, or any expression."),
        ex("Embedding in HTML", '<!DOCTYPE html>\n<html>\n<body>\n  <h1 id="demo">Original</h1>\n  <script>\n    document.getElementById("demo").innerHTML = "Changed by JS!";\n  </script>\n</body>\n</html>', "The heading text changes to: Changed by JS!", "JavaScript can directly manipulate HTML elements using the DOM API. getElementById selects an element and innerHTML changes its content."),
        ex("Basic Arithmetic", "let a = 10;\nlet b = 3;\nconsole.log(a + b);  // Addition\nconsole.log(a % b);  // Modulus (remainder)", "13\n1", "JavaScript supports all arithmetic operators. The modulus operator (%) returns the remainder of division.")
    ]
),

"js_variables": make_struct(
    "<p><strong>Variables</strong> in JavaScript are containers that store data values. Think of them as labeled boxes where you can put different types of information - numbers, text, lists, or even functions.</p><p>JavaScript provides three ways to declare variables: <code>var</code> (old way), <code>let</code> (modern, block-scoped), and <code>const</code> (for constants that never change). Understanding the differences between these is crucial for writing bug-free code.</p>",
    [
        {"title": "1. var, let, and const", "content": "<p><code>var</code> was the original way to declare variables but has quirks like function-scoping and hoisting. <code>let</code> (introduced in ES6) is block-scoped and safer. <code>const</code> creates variables whose reference cannot be reassigned.</p><ul><li><code>var</code> - Function scoped, can be redeclared, hoisted</li><li><code>let</code> - Block scoped, cannot be redeclared in same scope</li><li><code>const</code> - Block scoped, must be initialized, cannot be reassigned</li></ul>"},
        {"title": "2. Data Types", "content": "<p>JavaScript has <strong>7 primitive types</strong>: <code>string</code>, <code>number</code>, <code>boolean</code>, <code>null</code>, <code>undefined</code>, <code>symbol</code>, <code>bigint</code>. Plus the <code>object</code> type for complex data.</p><p>JavaScript is dynamically typed - a variable can hold a string now and a number later. Use <code>typeof</code> to check a variable's current type.</p>"},
        {"title": "3. Type Coercion", "content": "<p>JavaScript automatically converts types in certain situations (implicit coercion). For example, <code>'5' + 3</code> gives <code>'53'</code> (string concatenation), but <code>'5' - 3</code> gives <code>2</code> (numeric subtraction). This is one of JavaScript's most confusing features for beginners.</p><p>Use <code>===</code> (strict equality) instead of <code>==</code> to avoid coercion bugs.</p>"}
    ],
    "<ul><li><strong>let vs const:</strong> Use <code>const</code> by default, <code>let</code> only when you need to reassign</li><li><strong>Hoisting:</strong> <code>var</code> declarations are moved to the top of their scope</li><li><strong>typeof:</strong> Returns the type of a value as a string</li><li><strong>Naming Rules:</strong> Variables must start with a letter, underscore, or dollar sign</li></ul>",
    [
        ex("Variable Declarations", 'var oldWay = "I am var";\nlet modern = "I am let";\nconst constant = "I cannot change";\n\nconsole.log(oldWay, modern, constant);', "I am var I am let I cannot change", "var is function-scoped, let and const are block-scoped. Always prefer const, then let. Avoid var in modern code."),
        ex("Data Types", 'let name = "Alice";       // string\nlet age = 25;              // number\nlet isStudent = true;      // boolean\nlet nothing = null;        // null\nlet notDefined;            // undefined\n\nconsole.log(typeof name);  // "string"\nconsole.log(typeof age);   // "number"', '"string"\n"number"', "typeof operator returns the data type as a string. Note that typeof null returns 'object' - this is a known JS bug."),
        ex("Type Coercion Gotchas", 'console.log("5" + 3);     // "53" (string concat)\nconsole.log("5" - 3);     // 2 (numeric subtraction)\nconsole.log("5" === 5);    // false (strict equality)\nconsole.log("5" == 5);     // true (loose equality)', '"53"\n2\nfalse\ntrue', "The + operator prefers string concatenation when one operand is a string. Use === to avoid unexpected type conversions.")
    ]
),

"js_operators": make_struct(
    "<p><strong>Operators</strong> are special symbols that perform operations on values and variables. JavaScript has arithmetic operators (+, -, *, /), comparison operators (==, ===, <, >), logical operators (&&, ||, !), and assignment operators (=, +=, -=).</p><p>Mastering operators is essential because they form the building blocks of every expression and condition in your code.</p>",
    [
        {"title": "1. Arithmetic Operators", "content": "<p>JavaScript supports standard math operators: <code>+</code> (addition), <code>-</code> (subtraction), <code>*</code> (multiplication), <code>/</code> (division), <code>%</code> (modulus/remainder), <code>**</code> (exponentiation).</p><p>The increment (<code>++</code>) and decrement (<code>--</code>) operators add or subtract 1. They can be prefix (<code>++x</code>) or postfix (<code>x++</code>), which affects when the operation happens.</p>"},
        {"title": "2. Comparison & Logical", "content": "<p>Comparison operators return <code>true</code> or <code>false</code>. The key distinction is <code>==</code> (loose, with type coercion) vs <code>===</code> (strict, no coercion).</p><p>Logical operators: <code>&&</code> (AND - both must be true), <code>||</code> (OR - at least one true), <code>!</code> (NOT - inverts boolean). These are used extensively in if-statements and conditional rendering.</p>"},
        {"title": "3. Ternary & Nullish Coalescing", "content": "<p>The ternary operator <code>condition ? valueIfTrue : valueIfFalse</code> is a shorthand for simple if/else. It's widely used in React for conditional rendering.</p><p>The nullish coalescing operator <code>??</code> returns the right operand when the left is <code>null</code> or <code>undefined</code>, unlike <code>||</code> which also catches <code>0</code>, <code>''</code>, and <code>false</code>.</p>"}
    ],
    "<ul><li><strong>=== vs ==:</strong> Always use strict equality (===) to avoid type coercion bugs</li><li><strong>Short-circuit:</strong> && and || stop evaluating as soon as the result is determined</li><li><strong>Ternary:</strong> Great for simple conditionals, avoid nesting them</li><li><strong>??:</strong> Nullish coalescing only catches null/undefined, not falsy values</li></ul>",
    [
        ex("Comparison Operators", 'console.log(5 === "5");   // false (strict)\nconsole.log(5 == "5");    // true (loose)\nconsole.log(10 > 5);      // true\nconsole.log(10 !== 10);   // false', "false\ntrue\ntrue\nfalse", "Strict equality (===) checks both value AND type. Loose equality (==) converts types before comparing."),
        ex("Ternary Operator", 'let age = 20;\nlet status = age >= 18 ? "Adult" : "Minor";\nconsole.log(status);\n\nlet score = 85;\nlet grade = score >= 90 ? "A" : score >= 80 ? "B" : "C";\nconsole.log(grade);', "Adult\nB", "The ternary operator provides a concise way to write if/else expressions in a single line.")
    ]
),

"js_control_flow": make_struct(
    "<p><strong>Control flow</strong> determines the order in which statements are executed in your program. Without control flow, code would run linearly from top to bottom. With if/else statements and switch cases, your program can make decisions and take different paths based on conditions.</p><p>JavaScript's control flow structures are similar to C and Java, using curly braces <code>{}</code> to define blocks of code.</p>",
    [
        {"title": "1. if, else if, else", "content": "<p>The <code>if</code> statement evaluates a condition. If it's truthy, the block executes. <code>else if</code> provides additional conditions, and <code>else</code> catches everything that didn't match.</p><p>JavaScript considers these values as <strong>falsy</strong>: <code>false</code>, <code>0</code>, <code>''</code>, <code>null</code>, <code>undefined</code>, <code>NaN</code>. Everything else is truthy.</p>"},
        {"title": "2. switch Statement", "content": "<p>When you have many conditions checking the same variable, <code>switch</code> is cleaner than multiple if/else blocks. Each <code>case</code> is compared using strict equality (===).</p><p>Don't forget the <code>break</code> statement! Without it, execution 'falls through' to the next case. The <code>default</code> case handles unmatched values.</p>"},
        {"title": "3. Truthy and Falsy Values", "content": "<p>Understanding truthy/falsy is critical in JavaScript. An empty array <code>[]</code> and empty object <code>{}</code> are truthy! Only 6 values are falsy: <code>false, 0, '', null, undefined, NaN</code>.</p><p>This is commonly used for checking if a variable has a value: <code>if (username) { ... }</code> will skip if username is empty, null, or undefined.</p>"}
    ],
    "<ul><li><strong>Falsy values:</strong> false, 0, '', null, undefined, NaN - everything else is truthy</li><li><strong>switch uses ===:</strong> Cases are checked with strict equality</li><li><strong>break in switch:</strong> Always include break to prevent fall-through</li><li><strong>Optional chaining:</strong> Use ?. to safely access nested properties</li></ul>",
    [
        ex("if/else Statement", 'let temperature = 30;\n\nif (temperature > 35) {\n  console.log("Too hot!");\n} else if (temperature > 25) {\n  console.log("Nice weather!");\n} else {\n  console.log("A bit cold.");\n}', "Nice weather!", "The conditions are checked top-to-bottom. Once a condition is true, its block runs and the rest are skipped."),
        ex("switch Statement", 'let day = "Monday";\n\nswitch (day) {\n  case "Monday":\n  case "Tuesday":\n    console.log("Start of the week");\n    break;\n  case "Friday":\n    console.log("TGIF!");\n    break;\n  default:\n    console.log("Midweek");\n}', "Start of the week", "Multiple cases can share the same block. Fall-through (no break) lets Monday and Tuesday execute the same code.")
    ]
),

"js_loops": make_struct(
    "<p><strong>Loops</strong> allow you to repeat a block of code multiple times. Instead of writing the same line 100 times, a loop executes it automatically. JavaScript provides several loop types: <code>for</code>, <code>while</code>, <code>do...while</code>, <code>for...of</code>, and <code>for...in</code>.</p><p>Choosing the right loop type makes your code more readable and efficient. Modern JavaScript favors <code>for...of</code> for arrays and array methods like <code>.forEach()</code>, <code>.map()</code> over traditional for loops.</p>",
    [
        {"title": "1. for Loop", "content": "<p>The classic <code>for</code> loop has three parts: initialization, condition, and increment. It's ideal when you know exactly how many times to iterate.</p><p>Syntax: <code>for (let i = 0; i < n; i++) { ... }</code></p>"},
        {"title": "2. while and do...while", "content": "<p><code>while</code> loops run as long as the condition is true - useful when you don't know the iteration count in advance. <code>do...while</code> guarantees at least one execution because the condition is checked after the block runs.</p>"},
        {"title": "3. for...of and for...in", "content": "<p><code>for...of</code> iterates over iterable values (arrays, strings, Maps, Sets). <code>for...in</code> iterates over object keys/properties. A common mistake is using <code>for...in</code> on arrays - it iterates over indices as strings, not values!</p>"}
    ],
    "<ul><li><strong>for...of:</strong> Best for arrays and iterables - gives you values directly</li><li><strong>for...in:</strong> Best for objects - gives you property keys</li><li><strong>break:</strong> Exits the loop immediately</li><li><strong>continue:</strong> Skips the current iteration and moves to the next</li></ul>",
    [
        ex("for Loop", "for (let i = 1; i <= 5; i++) {\n  console.log(`Count: ${i}`);\n}", "Count: 1\nCount: 2\nCount: 3\nCount: 4\nCount: 5", "Template literals (backticks) allow embedding expressions with ${...}. The loop runs 5 times, incrementing i each time."),
        ex("for...of vs for...in", 'let fruits = ["apple", "banana", "cherry"];\n\n// for...of gives VALUES\nfor (let fruit of fruits) {\n  console.log(fruit);\n}\n\n// for...in gives INDICES\nfor (let index in fruits) {\n  console.log(index);\n}', "apple\nbanana\ncherry\n0\n1\n2", "for...of iterates over the actual values in the array. for...in iterates over the property keys (indices for arrays).")
    ]
),

"js_functions": make_struct(
    "<p><strong>Functions</strong> are the fundamental building blocks of JavaScript. They are reusable blocks of code that perform a specific task. Functions help you organize code, avoid repetition, and build modular applications.</p><p>JavaScript offers multiple ways to define functions: function declarations, function expressions, and arrow functions (ES6). Functions are <strong>first-class citizens</strong> in JavaScript, meaning they can be stored in variables, passed as arguments, and returned from other functions.</p>",
    [
        {"title": "1. Function Declarations vs Expressions", "content": "<p>A <strong>function declaration</strong> uses the <code>function</code> keyword and is hoisted (can be called before it's defined). A <strong>function expression</strong> assigns a function to a variable and is NOT hoisted.</p><p>Function declarations: <code>function greet() { ... }</code><br>Function expressions: <code>const greet = function() { ... }</code></p>"},
        {"title": "2. Arrow Functions (ES6)", "content": "<p>Arrow functions (<code>=></code>) provide a shorter syntax and don't have their own <code>this</code> binding. They're perfect for callbacks and short operations.</p><p>If the function body is a single expression, you can omit the curly braces and the <code>return</code> keyword: <code>const double = x => x * 2;</code></p>"},
        {"title": "3. Parameters & Default Values", "content": "<p>Functions can accept parameters with default values: <code>function greet(name = 'World') { ... }</code>. The rest parameter (<code>...args</code>) collects remaining arguments into an array.</p><p>JavaScript doesn't enforce parameter count - extra arguments are ignored, and missing ones become <code>undefined</code>.</p>"}
    ],
    "<ul><li><strong>First-class functions:</strong> Functions can be passed around like any other value</li><li><strong>Arrow functions:</strong> Shorter syntax, no own 'this' binding</li><li><strong>Closures:</strong> Functions remember the scope they were created in</li><li><strong>Callback:</strong> A function passed as an argument to another function</li></ul>",
    [
        ex("Arrow Functions", "const add = (a, b) => a + b;\nconst square = x => x * x;\n\nconsole.log(add(3, 4));\nconsole.log(square(5));", "7\n25", "Arrow functions with a single expression can omit braces and return. With one parameter, parentheses are optional."),
        ex("Higher-Order Function", "function operate(a, b, operation) {\n  return operation(a, b);\n}\n\nconst result = operate(10, 5, (x, y) => x * y);\nconsole.log(result);", "50", "A higher-order function takes another function as a parameter. This is the foundation of functional programming in JavaScript.")
    ]
),

"js_arrays": make_struct(
    "<p><strong>Arrays</strong> are ordered collections of values in JavaScript. They can hold any type of data - numbers, strings, objects, even other arrays. Arrays are one of the most used data structures and come with powerful built-in methods.</p><p>Modern JavaScript emphasizes functional array methods like <code>map()</code>, <code>filter()</code>, and <code>reduce()</code> over traditional for-loops, making code more declarative and easier to read.</p>",
    [
        {"title": "1. Creating and Accessing Arrays", "content": "<p>Create arrays with square brackets: <code>let colors = ['red', 'green', 'blue'];</code>. Access elements by index (0-based): <code>colors[0]</code> gives 'red'.</p><p>Arrays are dynamic - they automatically grow or shrink. Use <code>.length</code> to get the size, and <code>.push()</code>/<code>.pop()</code> to add/remove from the end.</p>"},
        {"title": "2. Array Methods (map, filter, reduce)", "content": "<p><code>map()</code> transforms each element and returns a new array. <code>filter()</code> returns elements that pass a test. <code>reduce()</code> combines all elements into a single value.</p><p>These methods don't modify the original array - they create new ones. This immutability principle is fundamental in React and modern JavaScript.</p>"},
        {"title": "3. Destructuring and Spread", "content": "<p>Array destructuring lets you extract values into variables: <code>const [first, second] = [10, 20];</code>. The spread operator (<code>...</code>) expands an array: <code>[...arr1, ...arr2]</code> merges two arrays.</p>"}
    ],
    "<ul><li><strong>map():</strong> Transform every element - returns new array of same length</li><li><strong>filter():</strong> Select elements matching a condition - returns subset</li><li><strong>reduce():</strong> Accumulate elements into a single value</li><li><strong>Spread (...):</strong> Clone or merge arrays immutably</li></ul>",
    [
        ex("map, filter, reduce", "const numbers = [1, 2, 3, 4, 5];\n\nconst doubled = numbers.map(n => n * 2);\nconsole.log(doubled);\n\nconst evens = numbers.filter(n => n % 2 === 0);\nconsole.log(evens);\n\nconst sum = numbers.reduce((acc, n) => acc + n, 0);\nconsole.log(sum);", "[2, 4, 6, 8, 10]\n[2, 4]\n15", "map transforms each element, filter selects matching elements, and reduce accumulates all elements into one value."),
        ex("Destructuring & Spread", 'const [first, ...rest] = [1, 2, 3, 4];\nconsole.log(first); // 1\nconsole.log(rest);  // [2, 3, 4]\n\nconst arr1 = [1, 2];\nconst arr2 = [3, 4];\nconst merged = [...arr1, ...arr2];\nconsole.log(merged);', "1\n[2, 3, 4]\n[1, 2, 3, 4]", "Destructuring extracts values into named variables. The rest operator (...rest) collects remaining elements. Spread creates shallow copies.")
    ]
),

"js_objects": make_struct(
    "<p><strong>Objects</strong> are the fundamental data structure in JavaScript. They store data as key-value pairs (properties) and can include functions (methods). Almost everything in JavaScript is an object - arrays, functions, dates, and even regular expressions.</p><p>Objects are used to model real-world entities. A 'user' object might have properties like name, age, and email, plus methods like login() and logout().</p>",
    [
        {"title": "1. Creating and Accessing Objects", "content": "<p>Objects are created with curly braces: <code>let user = { name: 'Alice', age: 25 };</code>. Access properties with dot notation (<code>user.name</code>) or bracket notation (<code>user['name']</code>).</p><p>Bracket notation is useful for dynamic keys stored in variables: <code>let key = 'name'; user[key];</code></p>"},
        {"title": "2. Object Methods & 'this'", "content": "<p>Methods are functions stored as object properties. Inside a method, <code>this</code> refers to the object the method belongs to.</p><p>Warning: Arrow functions don't have their own <code>this</code> - they inherit it from the enclosing scope. Use regular functions for object methods.</p>"},
        {"title": "3. Destructuring & Spread", "content": "<p>Object destructuring extracts properties into variables: <code>const { name, age } = user;</code>. The spread operator copies properties: <code>const updated = { ...user, age: 26 };</code></p><p>The spread operator creates a shallow copy - nested objects are still shared by reference!</p>"}
    ],
    "<ul><li><strong>Dot vs Bracket:</strong> Use dot for known keys, brackets for dynamic keys</li><li><strong>this keyword:</strong> Refers to the calling object in regular functions</li><li><strong>Object.keys():</strong> Returns an array of property names</li><li><strong>Spread:</strong> Creates shallow copies of objects</li></ul>",
    [
        ex("Object Methods", 'const car = {\n  brand: "Toyota",\n  speed: 0,\n  accelerate() {\n    this.speed += 10;\n    console.log(`Speed: ${this.speed}`);\n  }\n};\n\ncar.accelerate();\ncar.accelerate();', "Speed: 10\nSpeed: 20", "Methods defined using shorthand syntax automatically bind 'this' to the object. Each call increases the speed property."),
        ex("Destructuring", 'const user = { name: "Alice", age: 25, city: "NYC" };\nconst { name, ...rest } = user;\n\nconsole.log(name);\nconsole.log(rest);', 'Alice\n{ age: 25, city: "NYC" }', "Destructuring extracts named properties. The rest operator collects remaining properties into a new object.")
    ]
),

"js_strings": make_struct(
    "<p><strong>Strings</strong> in JavaScript are sequences of characters used to represent text. They can be created with single quotes, double quotes, or backticks (template literals). Strings are immutable - once created, individual characters cannot be changed.</p><p>Template literals (backticks) are the modern way to work with strings, supporting multi-line text and embedded expressions via <code>${expression}</code>.</p>",
    [
        {"title": "1. String Methods", "content": "<p>JavaScript strings have dozens of built-in methods: <code>.toUpperCase()</code>, <code>.toLowerCase()</code>, <code>.trim()</code>, <code>.split()</code>, <code>.includes()</code>, <code>.indexOf()</code>, <code>.slice()</code>, <code>.replace()</code>.</p><p>Since strings are immutable, all methods return new strings without modifying the original.</p>"},
        {"title": "2. Template Literals", "content": "<p>Template literals (backticks) solve two problems: <strong>string interpolation</strong> (<code>${variable}</code>) and <strong>multi-line strings</strong>. They completely replace messy string concatenation with + operators.</p>"},
        {"title": "3. Regular Expressions", "content": "<p>JavaScript supports regex patterns for advanced string matching: <code>/pattern/flags</code>. Common methods include <code>.match()</code>, <code>.replace()</code>, and <code>.test()</code>.</p><p>Regex is essential for form validation (emails, phone numbers) and text processing.</p>"}
    ],
    "<ul><li><strong>Immutable:</strong> String methods return new strings, never modify the original</li><li><strong>Template Literals:</strong> Use backticks for interpolation and multi-line strings</li><li><strong>.split():</strong> Converts a string into an array by splitting on a delimiter</li><li><strong>.includes():</strong> Returns true if a substring is found</li></ul>",
    [
        ex("String Methods", 'let text = "  Hello, World!  ";\nconsole.log(text.trim());\nconsole.log(text.trim().toUpperCase());\nconsole.log(text.trim().split(", "));', 'Hello, World!\nHELLO, WORLD!\n["Hello", "World!"]', "trim() removes whitespace from both ends. toUpperCase() converts to uppercase. split() breaks a string into an array."),
        ex("Template Literals", 'const name = "Alice";\nconst age = 25;\n\n// Old way (concatenation)\nconsole.log("Hi, " + name + "! Age: " + age);\n\n// New way (template literal)\nconsole.log(`Hi, ${name}! Age: ${age}`);', "Hi, Alice! Age: 25\nHi, Alice! Age: 25", "Template literals are cleaner and support expressions inside ${}. They can span multiple lines without escape characters.")
    ]
),

"js_dom": make_struct(
    "<p>The <strong>Document Object Model (DOM)</strong> is a tree-structured representation of your HTML document. JavaScript can access and modify any element, attribute, or text in the DOM. This is what makes web pages interactive and dynamic.</p><p>The DOM bridges HTML and JavaScript: HTML defines the structure, CSS styles it, and JavaScript manipulates it through the DOM API.</p>",
    [
        {"title": "1. Selecting Elements", "content": "<p>Modern DOM selection methods: <code>document.getElementById()</code>, <code>document.querySelector()</code> (first match), <code>document.querySelectorAll()</code> (all matches).</p><p><code>querySelector</code> accepts CSS selectors like <code>'.class'</code>, <code>'#id'</code>, <code>'div > p'</code>, making it extremely flexible.</p>"},
        {"title": "2. Modifying Elements", "content": "<p>Change content with <code>.innerHTML</code> (parses HTML) or <code>.textContent</code> (plain text, safer). Modify styles with <code>.style.property</code> or toggle CSS classes with <code>.classList.add/remove/toggle()</code>.</p>"},
        {"title": "3. Creating & Removing Elements", "content": "<p>Create new elements with <code>document.createElement()</code>, set their properties, then append them with <code>.appendChild()</code> or <code>.append()</code>. Remove elements with <code>.remove()</code>.</p>"}
    ],
    "<ul><li><strong>querySelector:</strong> Select any element using CSS selectors</li><li><strong>textContent vs innerHTML:</strong> textContent is safer (no XSS risk)</li><li><strong>classList:</strong> Modern way to manipulate CSS classes</li><li><strong>createElement:</strong> Dynamically create HTML elements via JavaScript</li></ul>",
    [
        ex("DOM Manipulation", 'const heading = document.querySelector("h1");\nheading.textContent = "New Title";\nheading.style.color = "blue";\nheading.classList.add("highlighted");', "(The h1 element text changes to 'New Title', turns blue, and gets a CSS class)", "querySelector finds elements using CSS selectors. We then modify its text, inline style, and CSS classes."),
        ex("Creating Elements", 'const list = document.querySelector("ul");\nconst newItem = document.createElement("li");\nnewItem.textContent = "New Item";\nlist.appendChild(newItem);', "(A new li element appears inside the ul)", "createElement makes a new DOM node. appendChild adds it as the last child of the selected parent element.")
    ]
),

"js_events": make_struct(
    "<p><strong>Events</strong> are actions that happen in the browser - clicks, key presses, mouse movements, form submissions, page loads. JavaScript lets you 'listen' for these events and respond with custom code. This is the core of web interactivity.</p><p>The modern approach uses <code>addEventListener()</code> which allows multiple handlers per event and provides fine-grained control over event propagation.</p>",
    [
        {"title": "1. Event Listeners", "content": "<p><code>element.addEventListener('click', callbackFunction)</code> is the modern way to handle events. It's superior to inline handlers (<code>onclick</code>) because you can add multiple listeners and remove them later.</p>"},
        {"title": "2. Event Object", "content": "<p>Every event handler receives an <code>event</code> object with useful properties: <code>event.target</code> (the element that triggered the event), <code>event.type</code>, <code>event.preventDefault()</code> (stops default behavior like form submission).</p>"},
        {"title": "3. Event Bubbling & Delegation", "content": "<p>Events <strong>bubble up</strong> from the target to the document root. Event delegation leverages this: instead of adding listeners to 100 list items, add one listener to the parent <code>ul</code> and check <code>event.target</code>.</p>"}
    ],
    "<ul><li><strong>addEventListener:</strong> Modern, supports multiple handlers per event</li><li><strong>event.preventDefault():</strong> Stops the browser's default action</li><li><strong>Event Delegation:</strong> One parent listener handles all child events</li><li><strong>Bubbling:</strong> Events propagate from target up to document root</li></ul>",
    [
        ex("Click Event", 'const btn = document.querySelector("#myBtn");\n\nbtn.addEventListener("click", function(event) {\n  console.log("Clicked!", event.target.textContent);\n  event.target.style.background = "green";\n});', "(Clicking the button logs its text and turns it green)", "addEventListener attaches a handler that runs each time the button is clicked. event.target refers to the clicked element."),
        ex("Event Delegation", 'document.querySelector("ul").addEventListener("click", (e) => {\n  if (e.target.tagName === "LI") {\n    console.log("Clicked:", e.target.textContent);\n  }\n});', "(Clicking any li inside the ul logs its text)", "One listener on the parent handles clicks on all children. This is efficient and works for dynamically added elements too.")
    ]
),

"js_es6": make_struct(
    "<p><strong>ES6 (ECMAScript 2015)</strong> was the biggest update to JavaScript ever. It introduced game-changing features like arrow functions, template literals, destructuring, classes, modules, promises, let/const, and the spread/rest operators.</p><p>Understanding ES6+ features is essential for modern JavaScript development, especially for React, Vue, and Node.js projects.</p>",
    [
        {"title": "1. let/const, Arrow Functions, Template Literals", "content": "<p>These three features alone transformed how JavaScript is written daily. <code>let/const</code> replaced <code>var</code>, arrow functions simplified callbacks, and template literals eliminated string concatenation.</p>"},
        {"title": "2. Destructuring & Spread/Rest", "content": "<p>Destructuring extracts values from arrays and properties from objects into distinct variables. Spread (<code>...</code>) expands iterables; Rest (<code>...</code>) collects remaining elements. Same syntax, different context.</p>"},
        {"title": "3. Classes & Modules", "content": "<p>ES6 classes provide syntactic sugar over prototypal inheritance, making OOP in JavaScript look familiar to Java/C# developers. ES6 modules (<code>import/export</code>) enable code splitting and dependency management.</p>"}
    ],
    "<ul><li><strong>Arrow Functions:</strong> Shorter syntax, lexical 'this' binding</li><li><strong>Destructuring:</strong> Extract values from arrays/objects concisely</li><li><strong>Spread/Rest:</strong> Clone, merge, or collect elements</li><li><strong>Modules:</strong> import/export for organizing code across files</li></ul>",
    [
        ex("ES6 Features Combined", 'const users = [\n  { name: "Alice", age: 25 },\n  { name: "Bob", age: 17 },\n  { name: "Charlie", age: 30 }\n];\n\n// Arrow + Destructuring + Filter + Template Literal\nconst adults = users\n  .filter(({ age }) => age >= 18)\n  .map(({ name }) => `${name} is an adult`);\n\nconsole.log(adults);', '["Alice is an adult", "Charlie is an adult"]', "This example combines destructuring in parameters, arrow functions, array methods, and template literals - the essence of modern JavaScript.")
    ]
),

"js_promises": make_struct(
    "<p><strong>Promises</strong> represent the eventual completion (or failure) of an asynchronous operation. Before promises, JavaScript used callbacks which led to deeply nested 'callback hell'. Promises provide a cleaner way to chain asynchronous operations.</p><p><code>async/await</code> (ES2017) makes promise-based code look synchronous, dramatically improving readability.</p>",
    [
        {"title": "1. Promise Basics", "content": "<p>A Promise has three states: <strong>pending</strong> (initial), <strong>fulfilled</strong> (resolved successfully), <strong>rejected</strong> (failed). Use <code>.then()</code> for success, <code>.catch()</code> for errors, and <code>.finally()</code> for cleanup.</p>"},
        {"title": "2. async/await", "content": "<p><code>async</code> functions always return a promise. Inside them, <code>await</code> pauses execution until the promise resolves. Error handling uses standard <code>try/catch</code> blocks, making async code feel synchronous.</p>"},
        {"title": "3. Promise.all & Promise.race", "content": "<p><code>Promise.all()</code> waits for ALL promises to resolve (fails fast on any rejection). <code>Promise.race()</code> resolves/rejects with the first settled promise. <code>Promise.allSettled()</code> waits for all, regardless of outcome.</p>"}
    ],
    "<ul><li><strong>async/await:</strong> Modern syntax for handling promises - replaces .then() chains</li><li><strong>try/catch:</strong> Error handling for async/await code</li><li><strong>Promise.all():</strong> Run multiple async operations in parallel</li><li><strong>fetch():</strong> Built-in API for making HTTP requests (returns a Promise)</li></ul>",
    [
        ex("async/await", 'async function fetchUser() {\n  try {\n    const response = await fetch("https://api.example.com/user");\n    const data = await response.json();\n    console.log(data.name);\n  } catch (error) {\n    console.log("Error:", error.message);\n  }\n}\n\nfetchUser();', "(Logs the user's name from the API response)", "async/await makes asynchronous code read like synchronous code. await pauses until the promise resolves, and try/catch handles errors."),
        ex("Promise.all", 'const p1 = fetch("/api/users");\nconst p2 = fetch("/api/posts");\n\nconst [users, posts] = await Promise.all([p1, p2]);\nconsole.log("Both loaded!");', "Both loaded!", "Promise.all runs multiple promises in parallel and waits for all to complete. Much faster than awaiting sequentially.")
    ]
),

"js_modules": make_struct(
    "<p><strong>Modules</strong> allow you to split your JavaScript code into separate files, each with its own scope. Before ES6 modules, all JavaScript shared a global scope, leading to naming conflicts and hard-to-maintain code.</p><p>ES6 modules use <code>export</code> to expose values and <code>import</code> to consume them. This is the foundation of modern JavaScript project structure.</p>",
    [
        {"title": "1. Named Exports & Imports", "content": "<p>Named exports allow multiple values per file: <code>export const PI = 3.14;</code>. Import them by name: <code>import { PI } from './math.js';</code>. You can rename during import: <code>import { PI as pi } from './math.js';</code></p>"},
        {"title": "2. Default Exports", "content": "<p>Each module can have one default export: <code>export default class App { }</code>. Import it with any name: <code>import MyApp from './App.js';</code>. Default exports are common for React components.</p>"},
        {"title": "3. Dynamic Imports", "content": "<p>Dynamic <code>import()</code> loads modules on demand (lazy loading), improving initial page load performance. It returns a promise: <code>const module = await import('./heavyModule.js');</code></p>"}
    ],
    "<ul><li><strong>Named Export:</strong> Multiple exports per file, imported by exact name</li><li><strong>Default Export:</strong> One per file, imported with any name</li><li><strong>Dynamic Import:</strong> Load modules on demand for performance</li><li><strong>Module Scope:</strong> Each module has its own scope - no global pollution</li></ul>",
    [
        ex("Module Pattern", '// math.js\nexport const add = (a, b) => a + b;\nexport const subtract = (a, b) => a - b;\n\n// app.js\nimport { add, subtract } from "./math.js";\nconsole.log(add(5, 3));\nconsole.log(subtract(10, 4));', "8\n6", "Named exports let you share specific functions between files. Import only what you need to keep bundles small.")
    ]
),

"js_oop": make_struct(
    "<p><strong>Object-Oriented Programming</strong> in JavaScript uses prototypal inheritance under the hood, but ES6 classes provide a familiar syntax. Classes are templates for creating objects with predefined properties and methods.</p><p>JavaScript supports encapsulation, inheritance, and polymorphism - the pillars of OOP - though with some unique characteristics compared to languages like Java or C++.</p>",
    [
        {"title": "1. Classes & Constructors", "content": "<p>A class is defined with the <code>class</code> keyword. The <code>constructor()</code> method initializes new instances. Create instances with <code>new</code>: <code>const dog = new Animal('Buddy');</code></p>"},
        {"title": "2. Inheritance (extends)", "content": "<p>Use <code>extends</code> to create a child class. Call <code>super()</code> in the constructor to invoke the parent's constructor. Override methods by redefining them in the child class.</p>"},
        {"title": "3. Getters, Setters & Static", "content": "<p>Getters (<code>get</code>) and setters (<code>set</code>) let you define computed properties. Static methods (<code>static</code>) belong to the class itself, not instances - useful for utility functions like <code>Array.isArray()</code>.</p>"}
    ],
    "<ul><li><strong>class:</strong> Syntactic sugar over prototypal inheritance</li><li><strong>extends:</strong> Creates a child class that inherits from a parent</li><li><strong>super():</strong> Calls the parent class constructor</li><li><strong>static:</strong> Methods that belong to the class, not instances</li></ul>",
    [
        ex("Class Inheritance", 'class Animal {\n  constructor(name) {\n    this.name = name;\n  }\n  speak() {\n    console.log(`${this.name} makes a sound.`);\n  }\n}\n\nclass Dog extends Animal {\n  speak() {\n    console.log(`${this.name} barks!`);\n  }\n}\n\nconst d = new Dog("Rex");\nd.speak();', "Rex barks!", "Dog extends Animal, inheriting the constructor. The speak() method is overridden in the child class (polymorphism).")
    ]
),

"js_error": make_struct(
    "<p><strong>Error handling</strong> in JavaScript uses <code>try...catch...finally</code> blocks. Without proper error handling, a single runtime error can crash your entire application. Defensive programming means anticipating what can go wrong and handling it gracefully.</p><p>JavaScript has built-in error types: <code>TypeError</code>, <code>ReferenceError</code>, <code>SyntaxError</code>, <code>RangeError</code>, and you can create custom errors by extending the <code>Error</code> class.</p>",
    [
        {"title": "1. try/catch/finally", "content": "<p><code>try</code> wraps code that might fail. <code>catch</code> handles the error. <code>finally</code> runs regardless - perfect for cleanup like closing connections. The error object has <code>.message</code> and <code>.stack</code> properties.</p>"},
        {"title": "2. Throwing Custom Errors", "content": "<p>Use <code>throw new Error('message')</code> to create your own errors. You can throw anything, but Error objects include stack traces for debugging. Create custom error classes by extending Error.</p>"},
        {"title": "3. Async Error Handling", "content": "<p>For promises, use <code>.catch()</code>. For async/await, wrap in <code>try/catch</code>. Unhandled promise rejections can crash Node.js applications - always handle async errors!</p>"}
    ],
    "<ul><li><strong>try/catch:</strong> Catches runtime errors without crashing the program</li><li><strong>throw:</strong> Manually trigger an error when business logic fails</li><li><strong>finally:</strong> Runs cleanup code regardless of success or failure</li><li><strong>Custom Errors:</strong> Extend Error class for application-specific error types</li></ul>",
    [
        ex("try/catch", 'try {\n  let result = JSON.parse("invalid json");\n} catch (error) {\n  console.log("Error:", error.message);\n} finally {\n  console.log("Cleanup done.");\n}', "Error: Unexpected token i in JSON at position 0\nCleanup done.", "try/catch prevents the invalid JSON from crashing the program. finally always executes for cleanup operations.")
    ]
),

"js_advanced": make_struct(
    "<p><strong>Advanced JavaScript</strong> covers the deeper concepts that separate beginners from professionals: closures, the event loop, prototypal inheritance, generators, proxies, and WeakMaps. These topics are frequently asked in technical interviews.</p><p>Understanding how JavaScript works under the hood (call stack, heap, event loop, microtasks vs macrotasks) is crucial for writing performant applications.</p>",
    [
        {"title": "1. Closures", "content": "<p>A <strong>closure</strong> is a function that retains access to its outer scope's variables, even after the outer function has returned. Closures power data privacy, function factories, and module patterns.</p>"},
        {"title": "2. The Event Loop", "content": "<p>JavaScript is single-threaded but non-blocking. The <strong>event loop</strong> continuously checks the call stack and task queue. Microtasks (Promises) have higher priority than macrotasks (setTimeout). This explains why <code>Promise.resolve().then(() => console.log('A'))</code> runs before <code>setTimeout(() => console.log('B'), 0)</code>.</p>"},
        {"title": "3. Prototypal Inheritance", "content": "<p>Every JavaScript object has a hidden <code>[[Prototype]]</code> link. When you access a property, JavaScript walks up the prototype chain until it finds it or reaches <code>null</code>. ES6 classes are syntactic sugar over this mechanism.</p>"}
    ],
    "<ul><li><strong>Closures:</strong> Functions remember their creation scope</li><li><strong>Event Loop:</strong> Manages async execution in single-threaded JavaScript</li><li><strong>Prototype Chain:</strong> How JavaScript implements inheritance</li><li><strong>WeakMap/WeakSet:</strong> Collections that allow garbage collection of keys</li></ul>",
    [
        ex("Closure", "function counter() {\n  let count = 0;\n  return {\n    increment: () => ++count,\n    getCount: () => count\n  };\n}\n\nconst c = counter();\nc.increment();\nc.increment();\nconsole.log(c.getCount());", "2", "The inner functions retain access to 'count' even after counter() has returned. This creates private state - count cannot be accessed directly from outside.")
    ]
)
}

# Apply all JS structured content
for topic_id, structured in JS.items():
    if topic_id in d['javascript']['content']:
        d['javascript']['content'][topic_id]['structured'] = structured

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print("JavaScript: All 17 topics now have structured content!")
