import json
filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f: content = f.read()
prefix = 'window.tracksData = '
pi = content.find(prefix); pc = content[:pi+len(prefix)]; js = content[pi+len(prefix):]
sf = ''
if js.strip().endswith(';'): js = js.strip()[:-1]; sf = ';'
data = json.loads(js)

js_ex = {
    "js_basics": [
        {"title":"Hello World in JavaScript","code":"console.log(\"Hello, World!\");\n\nlet name = \"Alice\";\nlet age = 25;\nconsole.log(\"Name: \" + name);\nconsole.log(`Age: ${age}`);","output":"Hello, World!\nName: Alice\nAge: 25","explanation":"console.log() prints output. We use let to declare variables. Template literals (backticks) allow embedding variables with ${} syntax, which is cleaner than string concatenation."}
    ],
    "js_variables": [
        {"title":"var vs let vs const","code":"var x = 10;    // function-scoped, avoid\nlet y = 20;    // block-scoped, reassignable\nconst z = 30;  // block-scoped, NOT reassignable\n\ny = 25;  // OK\n// z = 35; // ERROR: Assignment to constant\n\nconsole.log(\"x:\", x);\nconsole.log(\"y:\", y);\nconsole.log(\"z:\", z);\nconsole.log(\"Type of x:\", typeof x);\nconsole.log(\"Type of 'hello':\", typeof \"hello\");","output":"x: 10\ny: 25\nz: 30\nType of x: number\nType of 'hello': string","explanation":"const should be your default choice. Use let only when the value needs to change. Avoid var due to scoping issues. typeof returns the data type as a string."}
    ],
    "js_operators": [
        {"title":"== vs === Comparison","code":"console.log('5 == 5:', 5 == 5);       // true\nconsole.log('\"5\" == 5:', \"5\" == 5);    // true (type coercion!)\nconsole.log('\"5\" === 5:', \"5\" === 5);  // false (strict)\nconsole.log('null == undefined:', null == undefined);   // true\nconsole.log('null === undefined:', null === undefined); // false\n\n// Nullish coalescing\nlet user = null;\nconsole.log('User:', user ?? 'Guest');","output":"5 == 5: true\n\"5\" == 5: true\n\"5\" === 5: false\nnull == undefined: true\nnull === undefined: false\nUser: Guest","explanation":"== converts types before comparing (loose). === checks type AND value (strict). Always use === to avoid unexpected bugs. The ?? operator returns the right side when left is null/undefined."}
    ],
    "js_control_flow": [
        {"title":"Conditional Logic","code":"const score = 85;\nlet grade;\n\nif (score >= 90) {\n    grade = 'A';\n} else if (score >= 80) {\n    grade = 'B';\n} else if (score >= 70) {\n    grade = 'C';\n} else {\n    grade = 'F';\n}\n\nconsole.log(`Score: ${score}, Grade: ${grade}`);\n\n// Ternary operator\nconst status = score >= 60 ? 'Pass' : 'Fail';\nconsole.log(`Status: ${status}`);","output":"Score: 85, Grade: B\nStatus: Pass","explanation":"The if-else chain checks from top to bottom. Score 85 passes the >= 80 check, so grade is B. The ternary operator is a one-line if-else perfect for simple assignments."}
    ],
    "js_loops": [
        {"title":"Different Loop Types","code":"// for loop\nconsole.log('--- for loop ---');\nfor (let i = 1; i <= 3; i++) {\n    console.log('Count:', i);\n}\n\n// for...of (arrays)\nconst fruits = ['Apple', 'Banana', 'Cherry'];\nconsole.log('--- for...of ---');\nfor (const fruit of fruits) {\n    console.log('Fruit:', fruit);\n}\n\n// for...in (objects)\nconst person = {name: 'Alice', age: 25};\nconsole.log('--- for...in ---');\nfor (const key in person) {\n    console.log(`${key}: ${person[key]}`);\n}","output":"--- for loop ---\nCount: 1\nCount: 2\nCount: 3\n--- for...of ---\nFruit: Apple\nFruit: Banana\nFruit: Cherry\n--- for...in ---\nname: Alice\nage: 25","explanation":"Use for when you need a counter. Use for...of for array values. Use for...in for object keys. This is a common source of confusion for beginners."}
    ],
    "js_functions": [
        {"title":"Function Types","code":"// Function declaration\nfunction add(a, b) {\n    return a + b;\n}\n\n// Arrow function\nconst multiply = (a, b) => a * b;\n\n// Default parameter\nconst greet = (name = 'World') => `Hello, ${name}!`;\n\nconsole.log('add(3, 5):', add(3, 5));\nconsole.log('multiply(4, 6):', multiply(4, 6));\nconsole.log('greet():', greet());\nconsole.log('greet(\"Alice\"):', greet('Alice'));","output":"add(3, 5): 8\nmultiply(4, 6): 24\ngreet(): Hello, World!\ngreet(\"Alice\"): Hello, Alice!","explanation":"Function declarations are hoisted (usable before definition). Arrow functions are concise and don't have their own 'this'. Default parameters provide fallback values when arguments are missing."}
    ],
    "js_arrays": [
        {"title":"Array Methods","code":"const nums = [5, 2, 8, 1, 9, 3];\n\n// map: transform each element\nconst doubled = nums.map(n => n * 2);\nconsole.log('Doubled:', doubled);\n\n// filter: keep matching elements\nconst big = nums.filter(n => n > 4);\nconsole.log('Greater than 4:', big);\n\n// reduce: combine into single value\nconst sum = nums.reduce((total, n) => total + n, 0);\nconsole.log('Sum:', sum);\n\n// find: first match\nconst found = nums.find(n => n > 7);\nconsole.log('First > 7:', found);\n\n// sort\nconst sorted = [...nums].sort((a, b) => a - b);\nconsole.log('Sorted:', sorted);","output":"Doubled: [10, 4, 16, 2, 18, 6]\nGreater than 4: [5, 8, 9]\nSum: 28\nFirst > 7: 8\nSorted: [1, 2, 3, 5, 8, 9]","explanation":"map() creates a new array by transforming each element. filter() keeps elements that pass a test. reduce() combines all elements into one value. These methods are the backbone of modern JavaScript data processing."}
    ],
    "js_objects": [
        {"title":"Working with Objects","code":"const person = {\n    name: 'Alice',\n    age: 30,\n    greet() {\n        return `Hi, I'm ${this.name}`;\n    }\n};\n\nconsole.log(person.name);\nconsole.log(person.greet());\n\n// Destructuring\nconst { name, age } = person;\nconsole.log(`${name} is ${age}`);\n\n// Spread operator\nconst updated = { ...person, age: 31, city: 'NYC' };\nconsole.log(updated);","output":"Alice\nHi, I'm Alice\nAlice is 30\n{ name: 'Alice', age: 31, city: 'NYC', greet: [Function] }","explanation":"Objects store key-value pairs. Methods use 'this' to access the object's own properties. Destructuring extracts properties into variables. The spread operator creates copies with modifications."}
    ],
    "js_strings": [
        {"title":"String Operations","code":"const text = '  Hello, JavaScript!  ';\n\nconsole.log('Trimmed:', text.trim());\nconsole.log('Upper:', text.trim().toUpperCase());\nconsole.log('Includes JS:', text.includes('JavaScript'));\nconsole.log('Replace:', text.trim().replace('JavaScript', 'World'));\nconsole.log('Split:', 'a,b,c'.split(','));\nconsole.log('Repeat:', 'Ha'.repeat(3));\n\n// Template literal\nconst name = 'Alice';\nconsole.log(`Welcome, ${name}!`);","output":"Trimmed: Hello, JavaScript!\nUpper: HELLO, JAVASCRIPT!\nIncludes JS: true\nReplace: Hello, World!\nSplit: ['a', 'b', 'c']\nRepeat: HaHaHa\nWelcome, Alice!","explanation":"Strings are immutable; methods return new strings. Template literals (backticks) embed expressions with ${}. split() converts a string to an array. These methods are used constantly in JavaScript development."}
    ],
    "js_dom": [
        {"title":"DOM Manipulation","code":"// Select element\nconst heading = document.getElementById('title');\nheading.textContent = 'Updated Title';\nheading.style.color = 'blue';\n\n// Create element\nconst para = document.createElement('p');\npara.textContent = 'This paragraph was added by JS!';\ndocument.body.appendChild(para);\n\n// Toggle class\nheading.classList.add('active');\nconsole.log('Classes:', heading.className);","output":"// The heading text changes to 'Updated Title'\n// Its color becomes blue\n// A new paragraph appears on the page\nClasses: active","explanation":"getElementById() finds an element by its ID. textContent changes the text. style changes CSS directly. createElement() and appendChild() add new elements to the page dynamically."}
    ],
    "js_events": [
        {"title":"Event Handling","code":"const button = document.querySelector('#myBtn');\n\nbutton.addEventListener('click', function(event) {\n    console.log('Button clicked!');\n    console.log('Target:', event.target.tagName);\n    event.target.textContent = 'Clicked!';\n});\n\n// Keyboard event\ndocument.addEventListener('keydown', (e) => {\n    console.log(`Key pressed: ${e.key}`);\n});","output":"// When button is clicked:\nButton clicked!\nTarget: BUTTON\n// Button text changes to 'Clicked!'\n// When a key is pressed:\nKey pressed: a","explanation":"addEventListener() attaches a function to run when an event occurs. The event object contains details like target (element that fired it) and key (for keyboard events). This is how all interactive websites work."}
    ],
    "js_es6": [
        {"title":"ES6 Features","code":"// Spread operator\nconst arr1 = [1, 2, 3];\nconst arr2 = [4, 5, 6];\nconst merged = [...arr1, ...arr2];\nconsole.log('Merged:', merged);\n\n// Rest parameters\nfunction sum(...nums) {\n    return nums.reduce((a, b) => a + b, 0);\n}\nconsole.log('Sum:', sum(1, 2, 3, 4, 5));\n\n// Optional chaining\nconst user = { profile: { name: 'Alice' } };\nconsole.log(user.profile?.name);\nconsole.log(user.address?.city);","output":"Merged: [1, 2, 3, 4, 5, 6]\nSum: 15\nAlice\nundefined","explanation":"Spread (...) expands arrays/objects. Rest (...) collects arguments into an array. Optional chaining (?.) safely accesses nested properties without crashing if something is null/undefined."}
    ],
    "js_promises": [
        {"title":"Promises and async/await","code":"// Simulating API call\nfunction fetchUser(id) {\n    return new Promise((resolve, reject) => {\n        setTimeout(() => {\n            if (id > 0) resolve({ id, name: 'Alice' });\n            else reject('Invalid ID');\n        }, 1000);\n    });\n}\n\n// Using async/await\nasync function getUser() {\n    try {\n        const user = await fetchUser(1);\n        console.log('User:', user);\n    } catch (error) {\n        console.log('Error:', error);\n    }\n}\n\ngetUser();","output":"// After 1 second:\nUser: { id: 1, name: 'Alice' }","explanation":"Promises represent future values. async/await makes asynchronous code look synchronous. The await keyword pauses execution until the Promise resolves. try/catch handles errors from rejected Promises."}
    ],
    "js_modules": [
        {"title":"Module Export and Import","code":"// math.js (module file)\nexport function add(a, b) { return a + b; }\nexport function multiply(a, b) { return a * b; }\nexport default function subtract(a, b) { return a - b; }\n\n// main.js (importing)\nimport subtract, { add, multiply } from './math.js';\n\nconsole.log('Add:', add(3, 5));\nconsole.log('Multiply:', multiply(4, 6));\nconsole.log('Subtract:', subtract(10, 3));","output":"Add: 8\nMultiply: 24\nSubtract: 7","explanation":"Named exports use {}  in import. Default export doesn't need {}. Modules keep code organized across files. Each file is its own scope, preventing naming conflicts."}
    ],
    "js_oop": [
        {"title":"Classes and Inheritance","code":"class Animal {\n    constructor(name) {\n        this.name = name;\n    }\n    speak() {\n        return `${this.name} makes a sound`;\n    }\n}\n\nclass Dog extends Animal {\n    speak() {\n        return `${this.name} barks: Woof!`;\n    }\n    fetch(item) {\n        return `${this.name} fetches the ${item}`;\n    }\n}\n\nconst dog = new Dog('Rex');\nconsole.log(dog.speak());\nconsole.log(dog.fetch('ball'));\nconsole.log(dog instanceof Animal);","output":"Rex barks: Woof!\nRex fetches the ball\ntrue","explanation":"Classes define blueprints for objects. extends creates a child class that inherits from a parent. The child can override methods (speak) and add new ones (fetch). instanceof checks the inheritance chain."}
    ],
    "js_error": [
        {"title":"Error Handling","code":"function divide(a, b) {\n    if (b === 0) throw new Error('Cannot divide by zero!');\n    return a / b;\n}\n\ntry {\n    console.log('10 / 2 =', divide(10, 2));\n    console.log('10 / 0 =', divide(10, 0));\n} catch (error) {\n    console.log('Caught:', error.message);\n} finally {\n    console.log('Division complete.');\n}","output":"10 / 2 = 5\nCaught: Cannot divide by zero!\nDivision complete.","explanation":"throw creates a custom error. try wraps risky code. catch handles the error gracefully. finally always runs. Without try-catch, the error would crash the entire program."}
    ],
    "js_advanced": [
        {"title":"Closures","code":"function createCounter() {\n    let count = 0;  // private variable\n    return {\n        increment: () => ++count,\n        decrement: () => --count,\n        getCount: () => count\n    };\n}\n\nconst counter = createCounter();\nconsole.log(counter.increment()); // 1\nconsole.log(counter.increment()); // 2\nconsole.log(counter.decrement()); // 1\nconsole.log(counter.getCount());  // 1\n// console.log(count); // ERROR: count is not accessible","output":"1\n2\n1\n1","explanation":"A closure is a function that remembers variables from its outer scope. The count variable is private - only accessible through the returned methods. This is a powerful pattern for data encapsulation in JavaScript."}
    ],
    "js_interview": [
        {"title":"Debounce Function","code":"function debounce(func, delay) {\n    let timer;\n    return function(...args) {\n        clearTimeout(timer);\n        timer = setTimeout(() => func.apply(this, args), delay);\n    };\n}\n\n// Usage: only executes after user stops typing for 300ms\nconst search = debounce((query) => {\n    console.log('Searching for:', query);\n}, 300);\n\nsearch('h');\nsearch('he');\nsearch('hel');\nsearch('hello');  // Only this one executes","output":"// After 300ms:\nSearching for: hello","explanation":"Debounce prevents rapid-fire function calls. Each new call resets the timer. Only the last call executes after the delay. This is essential for search inputs, window resize handlers, and API calls."}
    ]
}

for k, examples in js_ex.items():
    if k in data['javascript']['content'] and 'structured' in data['javascript']['content'][k]:
        data['javascript']['content'][k]['structured']['examples'] = examples

nj = json.dumps(data, indent=2)
with open(filepath, 'w', encoding='utf-8') as f: f.write(pc + nj + sf)
print("JavaScript examples updated for all 18 topics!")
