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
    for lbl, code in examples:
        h += card(lbl, code)
    return h

def explanation(title, sections):
    h = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections:
        h += section(*s)
    return h + "</div>"

def quiz(items):
    return [{"q": q, "options": o, "answer": a} for q, o, a in items]

def task(title, desc, hint, code):
    return {"title": title, "description": desc, "hint": hint, "code": code}

def problems(items):
    return [{"title": t, "description": d, "code": c} for t, d, c in items]

js = data['javascript']['content']

# TOPIC 11: Events
js['js_events'] = {
    "title": "Events",
    "explanation": explanation("Events", [
        ("Event Listeners", "Events are actions like clicks, keypresses, mouse moves. Use addEventListener() to respond to them.",
         [("Click event", "const btn = document.querySelector('#myBtn');\nbtn.addEventListener('click', function() {\n  alert('Button clicked!');\n});\n\n// Arrow function version\nbtn.addEventListener('click', () => {\n  console.log('Clicked!');\n});"),
          ("Common events", "// Mouse events\nelement.addEventListener('mouseover', () => {});\nelement.addEventListener('mouseout', () => {});\n\n// Keyboard events\ndocument.addEventListener('keydown', (e) => {\n  console.log('Key:', e.key);\n});\n\n// Form events\nform.addEventListener('submit', (e) => {\n  e.preventDefault(); // stop page reload\n  console.log('Form submitted!');\n});\n\n// Input event\ninput.addEventListener('input', (e) => {\n  console.log('Typed:', e.target.value);\n});")]),
        ("Event Object", "Every event handler receives an event object with info about what happened.",
         [("Event object properties", "document.addEventListener('click', (event) => {\n  console.log('Type:',    event.type);       // 'click'\n  console.log('Target:',  event.target);     // clicked element\n  console.log('X:',       event.clientX);    // mouse X position\n  console.log('Y:',       event.clientY);    // mouse Y position\n});"),
          ("Event delegation", "// Instead of adding listener to EACH item,\n// add ONE listener to the parent:\nconst list = document.querySelector('ul');\nlist.addEventListener('click', (e) => {\n  if (e.target.tagName === 'LI') {\n    console.log('Clicked:', e.target.textContent);\n  }\n}};")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which method adds an event listener?", ["element.on()", "element.listen()", "element.addEventListener()", "element.bind()"], "element.addEventListener()"),
        ("What does e.preventDefault() do?", ["Stops event propagation", "Prevents default browser behaviour", "Triggers the event", "Removes listener"], "Prevents default browser behaviour"),
        ("Which event fires when typing in input?", ["change", "input", "keyup", "Both input and keyup"], "Both input and keyup"),
        ("event.target refers to?", ["Parent element", "Clicked/triggered element", "Document object", "Window object"], "Clicked/triggered element"),
        ("Event delegation means?", ["Listen on every child", "Listen on parent to handle child events", "Prevent all events", "Delegate to server"], "Listen on parent to handle child events"),
    ]),
    "hands_on": task("Click Counter", "Create a button that counts how many times it has been clicked and displays the count.", "Use a variable outside to track count. Update textContent.", "let count = 0;\nconst btn = document.createElement('button');\nbtn.textContent = 'Clicks: 0';\nbtn.addEventListener('click', () => {\n  count++;\n  btn.textContent = `Clicks: ${count}`;\n});\ndocument.body.appendChild(btn);"),
    "problem_solving": problems([
        ("Enter Key Submit", "Log 'Submitted!' when user presses Enter key in an input.", "document.querySelector('input').addEventListener('keydown', (e) => {\n  if (e.key === 'Enter') console.log('Submitted!');\n});"),
        ("Hover Color Change", "Change a div's background color to blue on mouseover and back to white on mouseout.", "const div = document.querySelector('div');\ndiv.addEventListener('mouseover', () => div.style.background='blue');\ndiv.addEventListener('mouseout',  () => div.style.background='white');"),
        ("Double Click", "Log 'Double clicked!' on dblclick event, and 'Single click' on click event.", "document.addEventListener('click',    () => console.log('Single click'));\ndocument.addEventListener('dblclick', () => console.log('Double clicked!'));"),
    ])
}

# TOPIC 12: ES6+
js['js_es6'] = {
    "title": "ES6+ Features",
    "explanation": explanation("ES6+ Modern JavaScript", [
        ("Destructuring & Spread/Rest", "ES6 introduced elegant ways to extract data and work with variable-length arguments.",
         [("Destructuring", "// Array destructuring\nconst [a, b, ...rest] = [1, 2, 3, 4, 5];\nconsole.log(a, b, rest); // 1 2 [3,4,5]\n\n// Object destructuring with rename + default\nconst { name: n, age = 18 } = { name: 'Alice' };\nconsole.log(n, age); // Alice 18"),
          ("Spread & Rest", "// Spread: expand\nconst arr1 = [1, 2], arr2 = [3, 4];\nconst merged = [...arr1, ...arr2]; // [1,2,3,4]\n\nconst obj1 = {a:1}, obj2 = {b:2};\nconst combined = {...obj1, ...obj2}; // {a:1,b:2}\n\n// Rest: collect into array\nfunction sum(...nums) {\n  return nums.reduce((t, n) => t + n, 0);\n}\nconsole.log(sum(1,2,3,4,5)); // 15")]),
        ("Template Literals, Classes & Modules", "ES6 added template literals, class syntax, and native module support.",
         [("Classes", "class Animal {\n  constructor(name, sound) {\n    this.name = name;\n    this.sound = sound;\n  }\n  speak() {\n    return `${this.name} says ${this.sound}`;\n  }\n}\n\nclass Dog extends Animal {\n  constructor(name) {\n    super(name, 'Woof');\n  }\n  fetch() { return `${this.name} fetches the ball!`; }\n}\n\nconst dog = new Dog('Rex');\nconsole.log(dog.speak());  // Rex says Woof\nconsole.log(dog.fetch());  // Rex fetches the ball!"),
          ("Nullish Coalescing & Optional Chaining", "const user = { name: 'Bob', address: null };\n\n// ?. — don't crash on null/undefined\nconsole.log(user.address?.city);    // undefined\n\n// ?? — fallback only on null/undefined (not 0 or '')\nconst port = user.port ?? 3000;\nconsole.log(port); // 3000\n\n// vs || which also falls back on 0 and ''\nconst x = 0 || 'default';  // 'default' (wrong!)\nconst y = 0 ?? 'default';  // 0 (correct!)")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does ...rest collect?", ["First argument", "Last argument", "All remaining arguments into array", "Nothing"], "All remaining arguments into array"),
        ("Nullish coalescing (??) returns right side when left is?", ["0 or ''", "false", "null or undefined only", "Any falsy value"], "null or undefined only"),
        ("Which keyword defines a class method that initializes properties?", ["init", "constructor", "setup", "build"], "constructor"),
        ("extends keyword is used for?", ["Copying an object", "Class inheritance", "Adding methods", "Importing modules"], "Class inheritance"),
        ("super() is called to?", ["Override parent method", "Call parent constructor", "Create new instance", "Delete parent class"], "Call parent constructor"),
    ]),
    "hands_on": task("Shape Classes", "Create a Rectangle class with width, height and methods area() and perimeter().", "Use constructor. Area = w*h. Perimeter = 2*(w+h).", "class Rectangle {\n  constructor(width, height) {\n    this.width = width;\n    this.height = height;\n  }\n  area() { return this.width * this.height; }\n  perimeter() { return 2 * (this.width + this.height); }\n}\n\nconst rect = new Rectangle(5, 3);\nconsole.log('Area:', rect.area());        // 15\nconsole.log('Perimeter:', rect.perimeter()); // 16"),
    "problem_solving": problems([
        ("Merge and Deduplicate", "Merge [1,2,3] and [2,3,4,5] and remove duplicates.", "const a=[1,2,3], b=[2,3,4,5];\nconst result = [...new Set([...a,...b])];\nconsole.log(result); // [1,2,3,4,5]"),
        ("Sum Any Args", "Write a function using rest params that sums any number of arguments.", "const sumAll = (...nums) => nums.reduce((t,n)=>t+n, 0);\nconsole.log(sumAll(1,2,3,4,5)); // 15"),
        ("Class Inheritance", "Create Animal class with speak(). Dog extends it and adds fetch() method.", "class Animal {\n  speak() { return 'Some sound'; }\n}\nclass Dog extends Animal {\n  speak() { return 'Woof!'; }\n  fetch() { return 'Fetching!'; }\n}\nconst d = new Dog();\nconsole.log(d.speak(), d.fetch());"),
    ])
}

# TOPIC 13: Promises & Async
js['js_promises'] = {
    "title": "Promises & Async/Await",
    "explanation": explanation("Promises & Async/Await", [
        ("Callbacks & Promises", "Asynchronous code doesn't block execution. Callbacks were old way. Promises are cleaner.",
         [("Promise basics", "// A Promise is either: pending, fulfilled, or rejected\nconst fetchData = new Promise((resolve, reject) => {\n  setTimeout(() => {\n    const success = true;\n    if (success) resolve('Data loaded!');\n    else reject('Error loading data');\n  }, 1000);\n});\n\nfetchData\n  .then(data => console.log(data))    // 'Data loaded!'\n  .catch(err => console.error(err))\n  .finally(() => console.log('Done'));"),
          ("Promise.all & Promise.race", "const p1 = Promise.resolve(1);\nconst p2 = Promise.resolve(2);\nconst p3 = Promise.resolve(3);\n\n// Wait for ALL to complete\nPromise.all([p1, p2, p3]).then(values => {\n  console.log(values); // [1, 2, 3]\n});\n\n// Return the FIRST that resolves\nPromise.race([p1, p2, p3]).then(first => {\n  console.log(first);  // 1\n});")]),
        ("async/await", "async/await makes asynchronous code look synchronous. async functions always return a Promise.",
         [("Basic async/await", "async function loadUser(id) {\n  try {\n    const res = await fetch(`/api/users/${id}`);\n    const user = await res.json();\n    console.log(user.name);\n  } catch (err) {\n    console.error('Error:', err);\n  }\n}\n\nloadUser(1);"),
          ("Parallel async calls", "async function loadAll() {\n  // Sequential (slow - waits one by one)\n  const a = await fetch('/api/a');\n  const b = await fetch('/api/b');\n\n  // Parallel (fast - fires both at once)\n  const [resA, resB] = await Promise.all([\n    fetch('/api/a'),\n    fetch('/api/b')\n  ]);\n}")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("A Promise starts in which state?", ["fulfilled", "rejected", "pending", "resolved"], "pending"),
        ("What does async before a function do?", ["Makes it run faster", "Makes it return a Promise", "Blocks execution", "Adds error handling"], "Makes it return a Promise"),
        ("await can only be used inside?", ["Any function", "async function", "try block", "Promise"], "async function"),
        ("Promise.all() resolves when?", ["First promise resolves", "All promises resolve", "Any promise rejects", "Timer completes"], "All promises resolve"),
        (".catch() handles?", ["Resolved promises", "Rejected promises", "Both", "setTimeout"], "Rejected promises"),
    ]),
    "hands_on": task("Simulated API Fetch", "Simulate an API call using Promise with setTimeout. Resolve with user data after 500ms.", "Use new Promise with setTimeout. Use .then to handle.", "function getUser(id) {\n  return new Promise((resolve) => {\n    setTimeout(() => {\n      resolve({ id, name: 'Alice', age: 25 });\n    }, 500);\n  });\n}\n\ngetUser(1).then(user => {\n  console.log(`User: ${user.name}, Age: ${user.age}`);\n});"),
    "problem_solving": problems([
        ("Async with Error", "Write an async function that throws error if id < 0.", "async function fetchUser(id) {\n  if (id < 0) throw new Error('Invalid ID');\n  return { id, name: 'Bob' };\n}\n\nfetchUser(-1).catch(e => console.error(e.message));"),
        ("Sequential Async", "Simulate 3 async steps in sequence using async/await.", "const step = (n) => new Promise(r => setTimeout(() => r(`Step ${n}`), 200));\nasync function run() {\n  console.log(await step(1));\n  console.log(await step(2));\n  console.log(await step(3));\n}\nrun();"),
        ("Promise.all Example", "Run 3 fake API calls in parallel and log all results.", "const api = (v) => Promise.resolve(v * 10);\nasync function main() {\n  const results = await Promise.all([api(1), api(2), api(3)]);\n  console.log(results); // [10,20,30]\n}\nmain();"),
    ])
}

# Topics 14-17: Modules, OOP, Error Handling, Advanced — detailed
for key, title, desc, ex1, ex2, qitems, hand, probs in [
    ("js_modules", "Modules", "ES6 Modules allow splitting code into separate files. Export from one file, import in another.",
     ("Export / Import", "// math.js\nexport const PI = 3.14;\nexport function add(a,b) { return a+b; }\nexport default class Calculator { /*...*/ }\n\n// app.js\nimport Calculator, { PI, add } from './math.js';\nconsole.log(PI);       // 3.14\nconsole.log(add(2,3)); // 5"),
     ("Named vs Default", "// Named exports (many per file)\nexport const foo = 1;\nexport function bar() {}\n\n// Default export (one per file)\nexport default function main() {}\n\n// Import named\nimport { foo, bar } from './module.js';\n\n// Import default (any name)\nimport main from './module.js';"),
     [("Named vs default export", ["Named: many, Default: one", "Named: one, Default: many", "Both same", "No difference"], "Named: many, Default: one"),
      ("Keyword to export?", ["module.exports", "export", "send", "provide"], "export"),
      ("Keyword to import?", ["include", "require", "import", "load"], "import"),
      ("Can a file have multiple default exports?", ["Yes", "No", "Yes with alias", "Depends on bundler"], "No"),
      ("What is tree shaking?", ["Removing dead code", "Sorting imports", "Bundling files", "Caching modules"], "Removing dead code")],
     task("Math Module", "Create a module that exports add, subtract, multiply. Import and use them.", "Use named exports.", "// math.js (export)\nexport const add = (a,b) => a+b;\nexport const sub = (a,b) => a-b;\nexport const mul = (a,b) => a*b;\n\n// app.js (import)\n// import { add, sub, mul } from './math.js';\nconsole.log(add(10,5)); // test"),
     [("Re-export", "Re-export from an index.js file aggregating multiple modules.", "// index.js\nexport { add } from './math.js';\nexport { greet } from './greet.js';"),
      ("Dynamic Import", "Load a module only when needed using dynamic import().", "// Dynamic (lazy) import\nbtn.addEventListener('click', async () => {\n  const { heavyFunc } = await import('./heavy.js');\n  heavyFunc();\n});"),
      ("Namespace Import", "Import all named exports under one namespace.", "import * as Math from './math.js';\nconsole.log(Math.add(2,3));\nconsole.log(Math.mul(4,5));")]),

    ("js_oop", "OOP in JavaScript", "OOP in JS uses classes (ES6+) or prototype chains. JS is prototype-based — classes are syntactic sugar.",
     ("Classes & Encapsulation", "class BankAccount {\n  #balance = 0;  // private field (#)\n\n  constructor(owner) {\n    this.owner = owner;\n  }\n  deposit(amount) {\n    if (amount > 0) this.#balance += amount;\n  }\n  get balance() { return this.#balance; }\n}\n\nconst acc = new BankAccount('Alice');\nacc.deposit(1000);\nconsole.log(acc.balance); // 1000\n// console.log(acc.#balance); // ERROR! private"),
     ("Inheritance & Polymorphism", "class Shape {\n  area() { return 0; }\n  toString() { return `Area: ${this.area()}`; }\n}\n\nclass Circle extends Shape {\n  constructor(r) { super(); this.r = r; }\n  area() { return Math.PI * this.r ** 2; } // override\n}\n\nclass Rect extends Shape {\n  constructor(w,h) { super(); this.w=w; this.h=h; }\n  area() { return this.w * this.h; }\n}\n\n[new Circle(5), new Rect(4,6)].forEach(s => console.log(s.toString()));"),
     [("Private fields use?", ["_prefix", "#prefix", "private keyword", "__prefix"], "#prefix"),
      ("OOP stands for?", ["Object Order Programming", "Object Oriented Programming", "Open Object Protocol", "Output Order Processing"], "Object Oriented Programming"),
      ("Polymorphism means?", ["One class", "Many classes with same method name behaving differently", "Private properties", "Static methods"], "Many classes with same method name behaving differently"),
      ("Encapsulation means?", ["Hiding implementation details", "Copying objects", "Inheriting from parent", "Exporting modules"], "Hiding implementation details"),
      ("static method belongs to?", ["Instance", "Class itself", "Prototype", "Parent class"], "Class itself")],
     task("Vehicle Class", "Create Vehicle class with brand, speed. Add accelerate(n) method that adds n to speed.", "Use constructor and a method that modifies this.speed.", "class Vehicle {\n  constructor(brand) {\n    this.brand = brand;\n    this.speed = 0;\n  }\n  accelerate(n) {\n    this.speed += n;\n    console.log(`${this.brand} speed: ${this.speed} km/h`);\n  }\n}\nconst car = new Vehicle('Toyota');\ncar.accelerate(50);\ncar.accelerate(30);"),
     [("Static Method", "Add a static compare method to a class that compares two values.", "class Util {\n  static max(a,b) { return a > b ? a : b; }\n}\nconsole.log(Util.max(5,3)); // 5"),
      ("Getters & Setters", "Use get/set to control property access.", "class Temp {\n  constructor(c) { this._c = c; }\n  get fahrenheit() { return this._c*9/5+32; }\n  set celsius(v) { this._c = v; }\n}\nconst t = new Temp(100);\nconsole.log(t.fahrenheit); // 212"),
      ("Mixin Pattern", "Add behaviour from multiple sources using mixins.", "const Swim = (Base) => class extends Base {\n  swim() { return 'Swimming!'; }\n};\nclass Animal {}\nclass Duck extends Swim(Animal) {}\nconsole.log(new Duck().swim());")]),
]:
    js[key] = {
        "title": title,
        "explanation": f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>{section('Introduction', desc, [ex1, ex2])}</div>",
        "examples": [],
        "concept_quiz": quiz(qitems),
        "hands_on": hand,
        "problem_solving": problems([(t,d,c) for t,d,c in probs])
    }

# TOPIC 16: Error Handling
js['js_error'] = {
    "title": "Error Handling",
    "explanation": explanation("Error Handling", [
        ("try / catch / finally", "Use try-catch to handle runtime errors gracefully without crashing the program.",
         [("Basic try-catch", "try {\n  const x = null;\n  x.name; // TypeError: Cannot read property\n} catch (err) {\n  console.error('Error type:', err.name);\n  console.error('Message:', err.message);\n} finally {\n  console.log('Always runs!');\n}"),
          ("throw custom error", "function divide(a, b) {\n  if (b === 0) throw new Error('Division by zero!');\n  return a / b;\n}\n\ntry {\n  console.log(divide(10, 0));\n} catch (e) {\n  console.error(e.message); // Division by zero!\n}")]),
        ("Error Types & Custom Errors", "JS has built-in error types. You can also create custom error classes.",
         [("Error types", "// TypeError: wrong type\n// ReferenceError: undefined variable\n// SyntaxError: invalid syntax\n// RangeError: out of range\n\ntry {\n  null.property;       // TypeError\n  undeclaredVar;       // ReferenceError\n  eval('{{{');         // SyntaxError\n} catch(e) {\n  console.log(e instanceof TypeError); // true (first one)\n}"),
          ("Custom error class", "class ValidationError extends Error {\n  constructor(field, message) {\n    super(message);\n    this.name = 'ValidationError';\n    this.field = field;\n  }\n}\n\nfunction validateAge(age) {\n  if (age < 0) throw new ValidationError('age', 'Age must be positive');\n  return age;\n}\n\ntry {\n  validateAge(-5);\n} catch(e) {\n  console.log(`${e.name} on [${e.field}]: ${e.message}`);\n}")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which block always runs regardless of error?", ["catch", "try", "finally", "error"], "finally"),
        ("How do you throw a custom error?", ["error(msg)", "throw new Error(msg)", "raise Error(msg)", "reject(msg)"], "throw new Error(msg)"),
        ("TypeError occurs when?", ["Variable is undefined", "Wrong data type used", "Syntax mistake", "Array out of bounds"], "Wrong data type used"),
        ("Can you have try without catch?", ["No", "Yes, with finally", "Only with throw", "Never"], "Yes, with finally"),
        ("Custom errors should extend?", ["Object", "Error", "Exception", "TypeError"], "Error"),
    ]),
    "hands_on": task("Safe JSON Parser", "Write a safeParseJSON(str) function that returns parsed object or null on invalid JSON.", "Use try-catch around JSON.parse.", "function safeParseJSON(str) {\n  try {\n    return JSON.parse(str);\n  } catch {\n    return null;\n  }\n}\n\nconsole.log(safeParseJSON('{\"a\":1}'));  // {a:1}\nconsole.log(safeParseJSON('invalid!'));  // null"),
    "problem_solving": problems([
        ("Input Validator", "Validate that a name is a non-empty string, else throw ValidationError.", "function validate(name) {\n  if (typeof name !== 'string' || !name.trim())\n    throw new TypeError('Name must be non-empty string');\n  return name.trim();\n}\ntry { validate(''); } catch(e) { console.error(e.message); }"),
        ("Fetch with error handling", "Simulate fetch with error handling for both network error and bad status.", "async function safeFetch(url) {\n  try {\n    const res = await fetch(url);\n    if (!res.ok) throw new Error(`HTTP ${res.status}`);\n    return await res.json();\n  } catch(e) {\n    console.error('Fetch failed:', e.message);\n    return null;\n  }\n}"),
        ("Re-throwing errors", "Catch only TypeError, re-throw others.", "function run() {\n  try {\n    undeclaredVar;\n  } catch(e) {\n    if (e instanceof ReferenceError) {\n      console.error('Ref error handled:', e.message);\n    } else {\n      throw e; // re-throw others\n    }\n  }\n}\nrun();"),
    ])
}

# TOPIC 17: Advanced Concepts
js['js_advanced'] = {
    "title": "Advanced JavaScript Concepts",
    "explanation": explanation("Advanced JavaScript", [
        ("Closures", "A closure is a function that retains access to its outer (enclosing) scope even after the outer function has finished executing.",
         [("Closure basics", "function counter() {\n  let count = 0;  // enclosed variable\n  return {\n    increment() { count++; },\n    decrement() { count--; },\n    value()     { return count; }\n  };\n}\n\nconst c = counter();\nc.increment(); c.increment(); c.increment();\nc.decrement();\nconsole.log(c.value()); // 2"),
          ("Practical closure: memoize", "function memoize(fn) {\n  const cache = {};\n  return function(n) {\n    if (n in cache) return cache[n];\n    return (cache[n] = fn(n));\n  };\n}\n\nconst slowDouble = n => { /* heavy calc */ return n * 2; };\nconst fastDouble = memoize(slowDouble);\nconsole.log(fastDouble(5)); // runs fn\nconsole.log(fastDouble(5)); // returns from cache")]),
        ("Hoisting & IIFE", "Variable/function declarations are moved to the top of their scope. IIFE = Immediately Invoked Function Expression.",
         [("Hoisting", "// Function declaration is hoisted\nconsole.log(greet()); // Works!\nfunction greet() { return 'Hello!'; }\n\n// var is hoisted (but not value)\nconsole.log(x); // undefined (not error)\nvar x = 5;\n\n// let/const NOT hoisted\n// console.log(y); // ReferenceError\nlet y = 10;"),
          ("IIFE", "// Runs immediately — creates private scope\n(function() {\n  const secret = 'hidden';\n  console.log('IIFE runs!');\n})();\n// console.log(secret); // ERROR - not accessible\n\n// Arrow IIFE\n(() => console.log('Arrow IIFE'))();")]),
        ("The Event Loop", "JS is single-threaded. The event loop handles async operations using Call Stack, Web APIs, Callback Queue, and Microtask Queue.",
         [("Event loop order", "console.log('1 - Sync start');\n\nsetTimeout(() => console.log('3 - setTimeout'), 0);\n\nPromise.resolve().then(() => console.log('2 - Promise (microtask)'));\n\nconsole.log('4 - Sync end');\n\n// Output order:\n// 1 - Sync start\n// 4 - Sync end\n// 2 - Promise (microtask) ← runs before setTimeout!\n// 3 - setTimeout"),
          ("Microtask vs Macrotask", "// Microtasks (higher priority): Promise.then, queueMicrotask\n// Macrotasks (lower priority): setTimeout, setInterval, I/O\n\n// Microtask queue empties BEFORE next macrotask\nsetTimeout(() => console.log('macro'), 0);\nPromise.resolve().then(() => console.log('micro'));\n// Output: micro → macro")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What is a closure?", ["A function with no parameters", "A function that accesses outer scope variables after outer fn returns", "An async function", "A class method"], "A function that accesses outer scope variables after outer fn returns"),
        ("IIFE stands for?", ["Immediately Invoked Function Expression", "Inline If Function", "Internal Invoked Function Event", "Indirect Function Expression"], "Immediately Invoked Function Expression"),
        ("What runs before setTimeout in event loop?", ["Other setTimeouts", "Synchronous code and Promise microtasks", "DOM events", "fetch calls"], "Synchronous code and Promise microtasks"),
        ("var is hoisted with its value?", ["Yes", "No - undefined until assignment", "Only in strict mode", "Always"], "No - undefined until assignment"),
        ("Memoization is used for?", ["Error handling", "Caching function results to avoid recomputation", "Async coding", "Module loading"], "Caching function results to avoid recomputation"),
    ]),
    "hands_on": task("Private Counter with Closure", "Using closure, create a counter with increment, decrement, reset, and value methods.", "Return an object of functions. They all share the same count variable via closure.", "function makeCounter(initial = 0) {\n  let count = initial;\n  return {\n    increment: () => ++count,\n    decrement: () => --count,\n    reset:     () => { count = initial; return count; },\n    value:     () => count\n  };\n}\nconst c = makeCounter(10);\nconsole.log(c.increment()); // 11\nconsole.log(c.increment()); // 12\nconsole.log(c.decrement()); // 11\nconsole.log(c.reset());     // 10"),
    "problem_solving": problems([
        ("Debounce Function", "Implement debounce(fn, delay) — executes fn only after delay ms of no calls.", "function debounce(fn, delay) {\n  let timer;\n  return (...args) => {\n    clearTimeout(timer);\n    timer = setTimeout(() => fn(...args), delay);\n  };\n}\nconst log = debounce(() => console.log('called!'), 300);\nlog(); log(); log(); // Only fires once after 300ms"),
        ("Once Function", "Create once(fn) — fn can only be called once, subsequent calls return first result.", "function once(fn) {\n  let called = false, result;\n  return (...args) => {\n    if (!called) { called = true; result = fn(...args); }\n    return result;\n  };\n}\nconst init = once(() => 'Initialized!');\nconsole.log(init()); // 'Initialized!'\nconsole.log(init()); // 'Initialized!' (cached)"),
        ("Currying", "Convert add(a,b,c) to curried form add(a)(b)(c).", "const curry = fn => a => b => c => fn(a,b,c);\nconst add = (a,b,c) => a+b+c;\nconst curriedAdd = curry(add);\nconsole.log(curriedAdd(1)(2)(3)); // 6"),
    ])
}

print("Topics 11-17 done!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
