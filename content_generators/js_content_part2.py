import json

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
json_start = text.find('{')
data = json.loads(text[json_start:text.rfind('}')+1])

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
    return html + "</div>"

def quiz(items):
    return [{"q": q, "options": o, "answer": a} for q, o, a in items]

def task(title, desc, hint, code):
    return {"title": title, "description": desc, "hint": hint, "code": code}

def problems(items):
    return [{"title": t, "description": d, "code": c} for t, d, c in items]

# TOPIC 6: Functions
data['javascript']['content']['js_functions'] = {
    "title": "Functions",
    "explanation": explanation("Functions", [
        ("Function Declaration & Expression",
         "A function is a reusable block of code. <b>Declaration</b>: uses the function keyword, hoisted. <b>Expression</b>: assigned to a variable, not hoisted.",
         [("Declaration (hoisted)", "// Can call before definition!\ngreet('Alice');\n\nfunction greet(name) {\n  console.log('Hello, ' + name + '!');\n}\n// Output: Hello, Alice!"),
          ("Expression (not hoisted)", "const add = function(a, b) {\n  return a + b;\n};\nconsole.log(add(5, 3)); // 8\n\n// Arrow function (ES6)\nconst multiply = (a, b) => a * b;\nconsole.log(multiply(4, 5)); // 20")]),
        ("Parameters, Arguments & Return",
         "Parameters are the variable names in the function definition. Arguments are the actual values passed. return sends a value back to the caller.",
         [("Default parameters", "function greet(name = 'Guest') {\n  return `Hello, ${name}!`;\n}\nconsole.log(greet('Bob'));   // Hello, Bob!\nconsole.log(greet());        // Hello, Guest!"),
          ("Multiple return values", "function minMax(arr) {\n  let min = Math.min(...arr);\n  let max = Math.max(...arr);\n  return { min, max };  // return object\n}\nconst result = minMax([3, 1, 8, 2]);\nconsole.log(result.min, result.max); // 1 8")]),
        ("Arrow Functions",
         "Arrow functions (=>) are shorter syntax. They don't have their own 'this'. Best for callbacks and short functions.",
         [("Arrow function syntax", "// Traditional\nfunction square(n) { return n * n; }\n\n// Arrow - full\nconst square2 = (n) => { return n * n; };\n\n// Arrow - implicit return (one expression)\nconst square3 = n => n * n;\n\nconsole.log(square3(5)); // 25"),
          ("Arrow in array methods", "const nums = [1, 2, 3, 4, 5];\n\n// Double each number\nconst doubled = nums.map(n => n * 2);\nconsole.log(doubled); // [2, 4, 6, 8, 10]\n\n// Filter evens\nconst evens = nums.filter(n => n % 2 === 0);\nconsole.log(evens); // [2, 4]")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does a function return if no return statement?", ["0", "null", "undefined", "Error"], "undefined"),
        ("Arrow functions have their own 'this'?", ["Yes", "No", "Sometimes", "Depends"], "No"),
        ("Which is hoisted?", ["Function expression", "Arrow function", "Function declaration", "const function"], "Function declaration"),
        ("What is a default parameter?", ["A mandatory value", "A fallback value if none passed", "A global variable", "A return value"], "A fallback value if none passed"),
        ("What does ...arr spread do in Math.min(...arr)?", ["Copies array", "Passes array elements as arguments", "Reverses array", "Sorts array"], "Passes array elements as arguments"),
    ]),
    "hands_on": task("Reusable Calculator", "Write arrow functions for add, subtract, multiply, divide. Test each with sample values.", "Use const name = (a, b) => a + b; syntax.", "const add = (a, b) => a + b;\nconst sub = (a, b) => a - b;\nconst mul = (a, b) => a * b;\nconst div = (a, b) => a / b;\n\nconsole.log(add(10, 5));  // 15\nconsole.log(sub(10, 5));  // 5\nconsole.log(mul(10, 5));  // 50\nconsole.log(div(10, 5));  // 2"),
    "problem_solving": problems([
        ("Is Prime?", "Write a function isPrime(n) that returns true if n is prime.", "function isPrime(n) {\n  if (n < 2) return false;\n  for (let i = 2; i <= Math.sqrt(n); i++) {\n    if (n % i === 0) return false;\n  }\n  return true;\n}\nconsole.log(isPrime(7));  // true\nconsole.log(isPrime(10)); // false"),
        ("Fibonacci", "Write function fibonacci(n) that returns first n Fibonacci numbers as array.", "function fibonacci(n) {\n  let fib = [0, 1];\n  for (let i = 2; i < n; i++) {\n    fib.push(fib[i-1] + fib[i-2]);\n  }\n  return fib.slice(0, n);\n}\nconsole.log(fibonacci(8)); // [0,1,1,2,3,5,8,13]"),
        ("Palindrome Check", "Write isPalindrome(str) that checks if a string reads the same forwards and backwards.", "const isPalindrome = str => str === str.split('').reverse().join('');\nconsole.log(isPalindrome('racecar')); // true\nconsole.log(isPalindrome('hello'));   // false"),
    ])
}

# TOPIC 7: Arrays
data['javascript']['content']['js_arrays'] = {
    "title": "Arrays",
    "explanation": explanation("Arrays", [
        ("Creating & Accessing Arrays",
         "Arrays store multiple values in a single variable. Access elements with index (0-based). Arrays are dynamic — they grow and shrink.",
         [("Create and access", "const fruits = ['Apple', 'Banana', 'Cherry', 'Date'];\n\nconsole.log(fruits[0]);      // Apple\nconsole.log(fruits[2]);      // Cherry\nconsole.log(fruits.length);  // 4\nconsole.log(fruits[fruits.length - 1]); // Date (last element)"),
          ("Adding and removing", "const arr = [1, 2, 3];\narr.push(4);       // Add to end    → [1,2,3,4]\narr.unshift(0);    // Add to start  → [0,1,2,3,4]\narr.pop();         // Remove from end → [0,1,2,3]\narr.shift();       // Remove from start → [1,2,3]\nconsole.log(arr);  // [1, 2, 3]")]),
        ("Array Methods",
         "JavaScript arrays have powerful built-in methods: map, filter, reduce, find, includes, sort, slice, splice, indexOf.",
         [("map, filter, reduce", "const nums = [1, 2, 3, 4, 5];\n\n// map: transform each element\nconst doubled = nums.map(n => n * 2);\nconsole.log(doubled); // [2,4,6,8,10]\n\n// filter: keep elements matching condition\nconst evens = nums.filter(n => n % 2 === 0);\nconsole.log(evens); // [2,4]\n\n// reduce: accumulate to single value\nconst sum = nums.reduce((acc, n) => acc + n, 0);\nconsole.log(sum); // 15"),
          ("find, includes, sort, slice", "const arr = [3, 1, 4, 1, 5, 9, 2, 6];\n\nconsole.log(arr.includes(5));    // true\nconsole.log(arr.indexOf(4));     // 2\nconsole.log(arr.find(n=>n>4));  // 5 (first match)\n\nconsole.log([...arr].sort((a,b)=>a-b));\n// [1,1,2,3,4,5,6,9]\n\nconsole.log(arr.slice(1, 4)); // [1,4,1]")]),
        ("Destructuring & Spread",
         "Destructuring extracts values from arrays into variables. Spread (...) expands an array into individual elements.",
         [("Destructuring", "const [first, second, ...rest] = [10, 20, 30, 40, 50];\nconsole.log(first);  // 10\nconsole.log(second); // 20\nconsole.log(rest);   // [30, 40, 50]"),
          ("Spread operator", "const a = [1, 2, 3];\nconst b = [4, 5, 6];\n\n// Merge arrays\nconst merged = [...a, ...b];\nconsole.log(merged); // [1,2,3,4,5,6]\n\n// Copy array\nconst copy = [...a];\ncopy.push(99);\nconsole.log(a);    // [1,2,3] - original unchanged\nconsole.log(copy); // [1,2,3,99]")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does arr.push() do?", ["Removes from end", "Adds to end", "Adds to start", "Removes from start"], "Adds to end"),
        ("Which method returns a new array with each element transformed?", ["filter", "find", "map", "reduce"], "map"),
        ("arr.slice(1,3) on [0,1,2,3,4] returns?", ["[0,1,2]", "[1,2]", "[1,2,3]", "[2,3]"], "[1,2]"),
        ("What does ... (spread) do with arrays?", ["Deletes elements", "Expands elements", "Sorts elements", "Reverses elements"], "Expands elements"),
        ("filter() returns?", ["Single value", "Boolean", "New filtered array", "Modified original array"], "New filtered array"),
    ]),
    "hands_on": task("Student Grade Processor", "Given marks array [78, 92, 55, 88, 45, 67], find: average, pass (>=60), fail counts.", "Use reduce for sum, filter for pass/fail.", "const marks = [78, 92, 55, 88, 45, 67];\nconst avg = marks.reduce((s,m) => s+m, 0) / marks.length;\nconst pass = marks.filter(m => m >= 60);\nconst fail = marks.filter(m => m < 60);\nconsole.log('Average:', avg.toFixed(1));\nconsole.log('Passed:', pass.length, pass);\nconsole.log('Failed:', fail.length, fail);"),
    "problem_solving": problems([
        ("Find Max Without Math", "Find the maximum value in [3,9,2,7,5,1,8] without using Math.max.", "const arr = [3,9,2,7,5,1,8];\nlet max = arr[0];\nfor (const n of arr) if (n > max) max = n;\nconsole.log('Max:', max);"),
        ("Remove Duplicates", "Remove duplicates from [1,2,2,3,3,3,4,5,5].", "const arr = [1,2,2,3,3,3,4,5,5];\nconst unique = [...new Set(arr)];\nconsole.log(unique); // [1,2,3,4,5]"),
        ("Flatten Nested Array", "Flatten [[1,2],[3,4],[5,6]] into [1,2,3,4,5,6].", "const nested = [[1,2],[3,4],[5,6]];\nconst flat = nested.flat();\nconsole.log(flat); // [1,2,3,4,5,6]"),
    ])
}

# TOPIC 8: Objects
data['javascript']['content']['js_objects'] = {
    "title": "Objects",
    "explanation": explanation("Objects", [
        ("Creating & Accessing Objects",
         "An object stores data as key-value pairs. Access properties with dot notation (obj.key) or bracket notation (obj['key']).",
         [("Create and access", "const person = {\n  name: 'Alice',\n  age: 25,\n  city: 'Chennai',\n  isStudent: false\n};\n\nconsole.log(person.name);      // Alice\nconsole.log(person['age']);    // 25\nconsole.log(person.city);      // Chennai"),
          ("Add, update, delete", "const car = { brand: 'Toyota', year: 2020 };\n\ncar.color = 'Blue';    // Add new property\ncar.year = 2022;       // Update property\ndelete car.color;      // Remove property\n\nconsole.log(car); // { brand: 'Toyota', year: 2022 }")]),
        ("Methods & 'this'",
         "Objects can have methods (functions as values). 'this' inside a method refers to the object itself.",
         [("Object method", "const student = {\n  name: 'Bob',\n  grade: 'A',\n  introduce() {\n    return `Hi, I am ${this.name} with grade ${this.grade}`;\n  }\n};\n\nconsole.log(student.introduce());\n// Hi, I am Bob with grade A"),
          ("Useful object methods", "const obj = { a: 1, b: 2, c: 3 };\n\nconsole.log(Object.keys(obj));   // ['a','b','c']\nconsole.log(Object.values(obj)); // [1,2,3]\nconsole.log(Object.entries(obj));\n// [['a',1],['b',2],['c',3]]\n\n// Copy object\nconst copy = { ...obj };\nconsole.log(copy);")]),
        ("Destructuring & Optional Chaining",
         "Object destructuring extracts properties into variables. Optional chaining (?.) safely accesses nested properties.",
         [("Object destructuring", "const { name, age, city = 'Unknown' } = {\n  name: 'Alice',\n  age: 25\n};\nconsole.log(name, age, city);\n// Alice 25 Unknown"),
          ("Optional chaining (?.)", "const user = {\n  name: 'Bob',\n  address: { city: 'Delhi' }\n};\n\nconsole.log(user.address?.city);    // Delhi\nconsole.log(user.phone?.number);    // undefined (no error!)\nconsole.log(user.address?.zip ?? 'N/A'); // N/A")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("How do you access 'name' property in obj?", ["obj->name", "obj::name", "obj.name", "obj[name]"], "obj.name"),
        ("What does 'this' refer to in an object method?", ["Global object", "The function itself", "The object the method belongs to", "undefined"], "The object the method belongs to"),
        ("What does Object.keys() return?", ["Values array", "Entries array", "Keys array", "Boolean"], "Keys array"),
        ("What is optional chaining (?.) used for?", ["Strict equality", "Safely access possibly undefined properties", "Assign default values", "Loop through objects"], "Safely access possibly undefined properties"),
        ("What does delete obj.key do?", ["Clears the value to null", "Removes the property", "Throws an error", "Sets to undefined"], "Removes the property"),
    ]),
    "hands_on": task("Student Record System", "Create a student object with name, marks(array), and a method getAverage(). Call the method.", "Use this.marks inside the method, and reduce to sum.", "const student = {\n  name: 'Ravi',\n  marks: [85, 92, 78, 88, 76],\n  getAverage() {\n    const sum = this.marks.reduce((s, m) => s + m, 0);\n    return (sum / this.marks.length).toFixed(1);\n  }\n};\nconsole.log(`${student.name}'s average: ${student.getAverage()}`);"),
    "problem_solving": problems([
        ("Count Properties", "Given an object, count how many properties it has.", "const obj = { a:1, b:2, c:3, d:4 };\nconsole.log('Properties:', Object.keys(obj).length);"),
        ("Merge Objects", "Merge two objects: {a:1, b:2} and {c:3, d:4} into one.", "const obj1 = {a:1, b:2};\nconst obj2 = {c:3, d:4};\nconst merged = { ...obj1, ...obj2 };\nconsole.log(merged);"),
        ("Find Key with Max Value", "In {math:85, sci:92, eng:78}, find the subject with highest marks.", "const scores = {math:85, sci:92, eng:78};\nlet maxKey = Object.keys(scores).reduce((k1,k2) => scores[k1]>scores[k2]?k1:k2);\nconsole.log(`Best subject: ${maxKey} (${scores[maxKey]})`);"),
    ])
}

# TOPIC 9: Strings
data['javascript']['content']['js_strings'] = {
    "title": "Strings",
    "explanation": explanation("Strings", [
        ("String Creation & Access",
         "Strings are sequences of characters. Use single quotes, double quotes, or backticks (template literals). Access characters by index.",
         [("Creating strings", "const s1 = 'Hello';         // single quotes\nconst s2 = \"World\";         // double quotes\nconst name = 'Alice';\nconst s3 = `Hi, ${name}!`;  // template literal\n\nconsole.log(s3); // Hi, Alice!\nconsole.log(s1.length);   // 5\nconsole.log(s1[0]);       // H"),
          ("Escape characters", "console.log('It\\'s great!');    // It's great!\nconsole.log('Line 1\\nLine 2'); // newline\nconsole.log('Tab\\there');      // tab\nconsole.log('He said \\\"Hi\\\"'); // quotes")]),
        ("String Methods",
         "Strings have many built-in methods. Strings are immutable — methods return new strings, they don't modify the original.",
         [("Essential methods", "const str = '  Hello, World!  ';\n\nconsole.log(str.trim());            // 'Hello, World!'\nconsole.log(str.toUpperCase());     // '  HELLO, WORLD!  '\nconsole.log(str.toLowerCase());     // '  hello, world!  '\nconsole.log(str.includes('World')); // true\nconsole.log(str.indexOf('World'));  // 9"),
          ("More methods", "const s = 'JavaScript is amazing';\n\nconsole.log(s.slice(0, 10));         // 'JavaScript'\nconsole.log(s.replace('amazing','fun'));// 'JavaScript is fun'\nconsole.log(s.split(' '));           // ['JavaScript','is','amazing']\nconsole.log('Hi'.repeat(3));         // 'HiHiHi'\nconsole.log('5'.padStart(4, '0'));   // '0005'")]),
        ("Template Literals",
         "Template literals use backticks and support multi-line strings and embedded expressions with ${}.",
         [("Multi-line & expressions", "const name = 'Bob';\nconst age = 25;\n\nconst msg = `\nName: ${name}\nAge:  ${age}\nAdult: ${age >= 18 ? 'Yes' : 'No'}\n`;\nconsole.log(msg);"),
          ("Tagged templates & raw", "const price = 9.99;\nconst qty = 3;\nconsole.log(`Total: $${(price * qty).toFixed(2)}`);\n// Total: $29.97\n\nconsole.log(`5 + 3 = ${5 + 3}`);\n// 5 + 3 = 8")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Strings in JS are?", ["Mutable", "Immutable", "Objects", "Arrays"], "Immutable"),
        ("What do backticks enable?", ["Faster code", "Template literals with ${}  ", "Strict mode", "Comments"], "Template literals with ${}  "),
        ("str.trim() does what?", ["Removes all spaces", "Removes leading/trailing whitespace", "Converts to lowercase", "Splits string"], "Removes leading/trailing whitespace"),
        ("'hello'.toUpperCase() returns?", ["'Hello'", "'HELLO'", "hello", "ERROR"], "'HELLO'"),
        ("str.split(',') on 'a,b,c' returns?", ["'abc'", "['a','b','c']", "3", "a b c"], "['a','b','c']"),
    ]),
    "hands_on": task("String Analyzer", "Given a sentence, count words, reverse it, and check if it contains 'JavaScript'.", "Use split(' '), reverse(), join(), includes().", "const sentence = 'I love JavaScript programming';\nconst words = sentence.split(' ');\nconsole.log('Word count:', words.length);\nconsole.log('Reversed:', words.reverse().join(' '));\nconsole.log('Has JavaScript:', sentence.includes('JavaScript'));"),
    "problem_solving": problems([
        ("Count Vowels", "Count vowels in 'Hello World'.", "const str = 'Hello World';\nconst vowels = str.toLowerCase().split('').filter(c => 'aeiou'.includes(c));\nconsole.log('Vowels:', vowels.length);"),
        ("Capitalize Words", "Capitalize first letter of each word in 'hello world foo'.", "const str = 'hello world foo';\nconst result = str.split(' ').map(w => w[0].toUpperCase() + w.slice(1)).join(' ');\nconsole.log(result);"),
        ("Anagram Check", "Check if 'listen' and 'silent' are anagrams.", "const sort = s => s.split('').sort().join('');\nconsole.log(sort('listen') === sort('silent')); // true"),
    ])
}

# TOPIC 10: DOM Manipulation
data['javascript']['content']['js_dom'] = {
    "title": "DOM Manipulation",
    "explanation": explanation("DOM Manipulation", [
        ("What is the DOM?",
         "The DOM (Document Object Model) is a tree-like representation of an HTML document. JavaScript can read and change the DOM to make pages interactive.",
         [("Select elements", "// Select by ID\nconst title = document.getElementById('main-title');\n\n// Select by class (returns HTMLCollection)\nconst cards = document.getElementsByClassName('card');\n\n// Modern: querySelector (returns first match)\nconst btn = document.querySelector('.btn');\n\n// querySelectorAll (returns NodeList)\nconst allBtns = document.querySelectorAll('button');"),
          ("Modify content & style", "const heading = document.querySelector('h1');\n\n// Change text content\nheading.textContent = 'New Heading!';\n\n// Change HTML content\nheading.innerHTML = '<span>New <b>Bold</b> Heading</span>';\n\n// Change CSS style\nheading.style.color = 'blue';\nheading.style.fontSize = '2rem';\n\n// Add/remove CSS classes\nheading.classList.add('active');\nheading.classList.remove('hidden');\nheading.classList.toggle('highlight');")]),
        ("Create & Remove Elements",
         "You can dynamically create new HTML elements using JavaScript and insert/remove them from the page.",
         [("Create elements", "// Create a new paragraph\nconst p = document.createElement('p');\np.textContent = 'This was created by JS!';\np.style.color = 'green';\n\n// Append to body\ndocument.body.appendChild(p);\n\n// Create and add a list item\nconst li = document.createElement('li');\nli.textContent = 'New Item';\ndocument.querySelector('ul').appendChild(li);"),
          ("Remove elements", "// Remove specific element\nconst old = document.getElementById('old-item');\nold.remove();\n\n// Remove a child\nconst list = document.querySelector('ul');\nconst firstItem = list.firstElementChild;\nlist.removeChild(firstItem);")]),
        ("Get & Set Attributes",
         "HTML attributes like id, class, src, href can be read and changed using getAttribute/setAttribute.",
         [("Attributes example", "const img = document.querySelector('img');\n\n// Get attribute\nconsole.log(img.getAttribute('src'));\n\n// Set attribute\nimg.setAttribute('src', 'new-image.jpg');\nimg.setAttribute('alt', 'New Image');\n\n// Input value\nconst input = document.querySelector('input');\nconst value = input.value;\ninput.value = 'New Value';"),
          ("data attributes", "// HTML: <div data-user-id='42'>...</div>\nconst div = document.querySelector('div');\nconsole.log(div.dataset.userId); // 42\ndiv.dataset.userId = 99;         // Change it")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does document.querySelector() return?", ["All matching elements", "First matching element", "Array of elements", "Node count"], "First matching element"),
        ("Which method adds a class to an element?", ["element.addClassName()", "element.classList.add()", "element.class.push()", "element.style.add()"], "element.classList.add()"),
        ("innerHTML vs textContent?", ["Same thing", "innerHTML parses HTML, textContent is plain text", "textContent is unsafe", "No difference"], "innerHTML parses HTML, textContent is plain text"),
        ("How to create a new HTML element?", ["document.createElement()", "new Element()", "document.newElement()", "HTML.create()"], "document.createElement()"),
        ("element.remove() does what?", ["Hides the element", "Deletes from DOM", "Clears content", "Disables element"], "Deletes from DOM"),
    ]),
    "hands_on": task("Dynamic List Builder", "Using JS, create a ul with 3 li items ('HTML', 'CSS', 'JavaScript') and append to the page body.", "Use createElement, textContent, appendChild.", "const ul = document.createElement('ul');\nconst items = ['HTML', 'CSS', 'JavaScript'];\n\nitems.forEach(item => {\n  const li = document.createElement('li');\n  li.textContent = item;\n  li.style.padding = '8px';\n  ul.appendChild(li);\n});\n\ndocument.body.appendChild(ul);"),
    "problem_solving": problems([
        ("Change Page Title", "Change the document title and h1 text using JS.", "document.title = 'New Page Title';\ndocument.querySelector('h1').textContent = 'Updated Heading';"),
        ("Toggle Visibility", "Create a button that hides/shows a paragraph when clicked.", "// HTML: <button id='btn'>Toggle</button><p id='text'>Hello!</p>\ndocument.getElementById('btn').onclick = () => {\n  const p = document.getElementById('text');\n  p.style.display = p.style.display === 'none' ? 'block' : 'none';\n};"),
        ("Color Changer", "Change the background colour of the page to a random colour on button click.", "function randomColor() {\n  return '#' + Math.floor(Math.random()*16777215).toString(16).padStart(6,'0');\n}\ndocument.getElementById('btn').onclick = () => {\n  document.body.style.backgroundColor = randomColor();\n};"),
    ])
}

print("Topics 6-10 done!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
