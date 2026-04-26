import json
import re

css_style = """<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); min-height: 100vh; padding: 40px 20px; }
.container { max-width: 900px; margin: 0 auto; background: white; border-radius: 15px; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3); overflow: hidden; }
.header { background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 100%); color: white; padding: 50px 40px; text-align: center; border-bottom: 4px solid #0ea5e9; }
.header h1 { font-size: 3em; margin-bottom: 10px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); }
.header p { font-size: 1.2rem; opacity: 0.9; font-style: italic; }
.content { padding: 40px; }
.intro { background: #f0f9ff; padding: 20px; border-left: 5px solid #0ea5e9; margin-bottom: 30px; border-radius: 8px; }
.intro p { color: #475569; font-size: 1.05rem; line-height: 1.8; }
.topic { margin-bottom: 40px; }
.topic-title { color: #0f172a; font-size: 1.8rem; border-bottom: 2px solid #e0f2fe; padding-bottom: 12px; margin-bottom: 20px; display: flex; align-items: center; gap: 10px; }
.topic-title i { color: #38bdf8; font-size: 1.6rem; }
.explanation { color: #475569; font-size: 1.05rem; margin-bottom: 15px; line-height: 1.8; }
.key-points { background: #f8fafc; padding: 15px 20px; border-radius: 8px; margin: 15px 0; border-left: 4px solid #0ea5e9; }
.key-points strong { color: #0f172a; display: block; margin-bottom: 10px; font-size: 1.05rem; }
.key-points ul { list-style-position: inside; color: #475569; }
.key-points li { margin-bottom: 8px; line-height: 1.6; }
.example-block { background: #f8fafc; border-radius: 12px; margin: 20px 0; overflow: hidden; border: 1px solid #e0f2fe; box-shadow: 0 4px 6px rgba(14, 165, 233, 0.05); }
.example-header { background: linear-gradient(to right, #0ea5e9, #3b82f6); padding: 8px 15px; color: white; font-size: 0.85rem; font-weight: 600; font-family: 'Courier New', monospace; display: flex; align-items: center; gap: 8px; }
.example-header i { font-size: 1rem; }
.example-code { margin: 0; padding: 15px 20px; color: #0f172a; font-family: 'Courier New', monospace; font-size: 0.95rem; overflow-x: auto; background: white; border-bottom: 1px solid #e0f2fe; }
.example-code code { color: #7c3aed; font-weight: 500; }
.example-output { padding: 12px 20px; background: #f0f9ff; color: #0f172a; font-family: 'Courier New', monospace; font-size: 0.9rem; border-top: 1px solid #e0f2fe; }
.output-label { font-weight: 600; color: #0ea5e9; margin-bottom: 5px; }
.sub-heading { color: #0ea5e9; font-size: 1.35rem; margin-top: 35px; margin-bottom: 15px; display: flex; align-items: center; gap: 8px; }
.sub-heading i { color: #38bdf8; }
.highlight { background: #fef3c7; padding: 2px 6px; border-radius: 3px; font-weight: 500; color: #92400e; }
</style>
"""

topics_data = {
    "operators": {
        "title": "Python Operators",
        "intro": "Operators are special symbols that perform operations on variables and values. Python provides several types of operators to perform arithmetic, logical, and comparison tasks efficiently.",
        "sections": [
            {
                "title": "Arithmetic Operators", "icon": "fa-calculator",
                "explanation": "Used with numeric values to perform common mathematical operations (+, -, *, /, //, %, **). Note that in Python 3, normal division (/) always returns a float, and floor division (//) returns an integer (rounded down).",
                "points": ["Addition (+), Subtraction (-)", "Multiplication (*), True Division (/)", "Floor Division (//), Modulus (%)", "Exponentiation (**)"],
                "examples": [
                    {"t": "Basic Arithmetic", "c": "a = 15\\nb = 4\\nprint(a / b)\\nprint(a // b)\\nprint(a % b)\\nprint(a ** 2)", "o": "3.75\\n3\\n3\\n225"}
                ]
            },
            {
                "title": "Comparison & Logical Operators", "icon": "fa-balance-scale",
                "explanation": "Comparison operators compare two values and return a boolean (True/False). Logical operators (and, or, not) are used to combine multiple conditions.",
                "points": ["Comparison: ==, !=, >, <, >=, <=", "Logical: and, or, not"],
                "examples": [
                    {"t": "Comparing Attributes", "c": "x = 10\\nprint(x > 5 and x < 15)\\nprint(not(x == 10))", "o": "True\\nFalse"}
                ]
            },
            {
                "title": "Identity & Membership Operators", "icon": "fa-search",
                "explanation": "Identity operators (is, is not) compare the memory locations of two objects. Membership operators (in, not in) test if a sequence is presented in an object.",
                "points": ["Identity check if objects are the exact same instance in memory.", "Membership evaluates inclusion in lists, strings, etc."],
                "examples": [
                    {"t": "Identity and Membership", "c": "nums = [1, 2, 3]\\nprint(2 in nums)\\nprint('a' not in 'hello')\\nx = [1,2,3]\\ny = x\\nprint(x is y)", "o": "True\\nTrue\\nTrue"}
                ]
            }
        ]
    },
    "control_flow": {
        "title": "Control Flow in Python",
        "intro": "Control flow is the order in which statements are evaluated or executed. Using conditional statements, you dictate how your program responds to different inputs or states.",
        "sections": [
            {
                "title": "If...Elif...Else Statements", "icon": "fa-code-branch",
                "explanation": "The block of code inside the `if` statement executes only when the condition meets `True`. Using `elif` allows multiple conditions sequentially, while `else` acts as the catch-all.",
                "points": ["Python relies on indentation to group blocks.", "Conditions are evaluated top to bottom; only the first True block runs."],
                "examples": [
                    {"t": "Age Verification", "c": "age = 20\\nif age < 13:\\n    print('Child')\\nelif age < 20:\\n    print('Teenager')\\nelse:\\n    print('Adult')", "o": "Adult"}
                ]
            },
            {
                "title": "Nested Conditionals", "icon": "fa-sitemap",
                "explanation": "You can have `if` statements inside `if` statements, this is called nesting. It allows for more precise sub-conditions.",
                "points": ["Indent nested branches consistently.", "Deeply nested blocks can be hard to read—consider combining expressions logic logically if it goes too deep."],
                "examples": [
                    {"t": "Nested Auth Check", "c": "logged_in = True\\nis_admin = False\\nif logged_in:\\n    if is_admin:\\n        print('Access Granted to Dashboard.')\\n    else:\\n        print('Welcome User.')\\nelse:\\n    print('Please Log In.')", "o": "Welcome User."}
                ]
            },
            {
                "title": "Match Case (Python 3.10+)", "icon": "fa-list-ol",
                "explanation": "Python 3.10 introduced the `match` statement, acting much like switch cases in other languages, allowing for structural pattern matching.",
                "points": ["Uses `match` and `case`.", "The underscore `_` acts as a wildcard (default)."],
                "examples": [
                    {"t": "HTTP Status Match", "c": "status = 404\\nmatch status:\\n    case 200:\\n        print('OK')\\n    case 404:\\n        print('Not Found')\\n    case _:\\n        print('Unknown Status')", "o": "Not Found"}
                ]
            }
        ]
    },
    "loops": {
        "title": "Loops and Iteration",
        "intro": "Loops allow you to run a block of code repeatedly. Python handles repetition primarily through `for` loops (iterating over sequences) and `while` loops (based on evolving conditions).",
        "sections": [
            {
                "title": "The For Loop", "icon": "fa-redo-alt",
                "explanation": "A for loop acts as an iterator in Python; it goes through items that are in a sequence or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries.",
                "points": ["Often used with `range(start, stop, step)`.", "Automatically stops when the sequence is exhausted."],
                "examples": [
                    {"t": "Iterating lists and ranges", "c": "for i in range(1, 6, 2):\\n    print(i)\\n\\nfruits = ['apple', 'pear']\\nfor f in fruits:\\n    print(f)", "o": "1\\n3\\n5\\napple\\npear"}
                ]
            },
            {
                "title": "The While Loop", "icon": "fa-sync",
                "explanation": "A while loop executes a block of code as long as its condition remains True. Be careful to ensure the variable in the condition is eventually modified within the loop to avoid infinite loops.",
                "points": ["Condition checked at the start of every iteration.", "Needs an explicit exit mechanism or decrement/increment."],
                "examples": [
                    {"t": "While Implementation", "c": "count = 3\\nwhile count > 0:\\n    print(f'Countdown: {count}')\\n    count -= 1\\nprint('Lift off!')", "o": "Countdown: 3\\nCountdown: 2\\nCountdown: 1\\nLift off!"}
                ]
            },
            {
                "title": "Break, Continue & Else", "icon": "fa-stop-circle",
                "explanation": "Loop control statements change execution from its normal sequence. `Break` steps out of the loop completely. `Continue` skips the remainder of the current loop and goes to the next iteration.",
                "points": ["Break exits loop instantly.", "Continue skips to the next iteration directly.", "An `else` block on a loop runs only if the loop wasn't terminated by a `break`."],
                "examples": [
                    {"t": "Skipping and Stopping", "c": "for val in 'string':\\n    if val == 'i':\\n        continue\\n    if val == 'n':\\n        break\\n    print(val)", "o": "s\\nt\\nr"}
                ]
            }
        ]
    },
    "strings": {
        "title": "String Manipulation",
        "intro": "Strings in Python are arrays of bytes representing unicode characters. Python has endless powerful built-in methods to easily format and manipulate strings.",
        "sections": [
            {
                "title": "Slicing and Indexing", "icon": "fa-cut",
                "explanation": "You can return a range of characters by using the slice syntax `[start:stop:step]`. Indexing is 0-based. Negative indices count backward from the end.",
                "points": ["Indexing starts at 0, backward starts at -1.", "Strings are immutable, you cannot assign a character to a specific index directly."],
                "examples": [
                    {"t": "Slicing Examples", "c": "s = 'Hello World'\\nprint(s[6:11])\\nprint(s[-5:])\\nprint(s[::-1])", "o": "World\\nWorld\\ndlroW olleH"}
                ]
            },
            {
                "title": "String Methods", "icon": "fa-tools",
                "explanation": "Python has a set of built-in methods that you can use on strings, like altering casing, replacing characters, and splitting.",
                "points": ["`split()` breaks string into a list.", "`strip()` removes trailing/leading whitespaces.", "`replace()` swops sequences in strings.", "`.lower() / .upper()` modify casing."],
                "examples": [
                    {"t": "Common Manipulations", "c": "val = '   Python Course   '\\nclean = val.strip().upper()\\nprint(clean)\\nprint(clean.split('ON'))", "o": "PYTHON COURSE\\n['PYTH', ' COURSE']"}
                ]
            },
            {
                "title": "F-Strings (Formatting)", "icon": "fa-pen",
                "explanation": "F-Strings (Literal String Interpolation) provide a concise, readable way to embed python expressions inside string literals.",
                "points": ["Add an `f` before the string quotes.", "Expressions go inside curly braces `{}`.", "You can execute code (funcs/math) inside the braces too."],
                "examples": [
                    {"t": "F-string formatting", "c": "lang = 'Python'\\nvers = 3.10\\nprint(f'{lang} version {vers} is awesome!')\\nprint(f'2 * 3 = {2 * 3}')", "o": "Python version 3.1 is awesome!\\n2 * 3 = 6"}
                ]
            }
        ]
    },
    "lists": {
        "title": "Python Lists",
        "intro": "Lists are versatile, ordered, and mutable collections. They can store multiple items (of different data types) inside a single variable.",
        "sections": [
            {
                "title": "Creation and Access", "icon": "fa-list",
                "explanation": "Created using square brackets `[]`. Lists maintain their order and allow duplicates. Accessed exactly like strings with indexing and slicing.",
                "points": ["Mutable: Items can be modified, added or removed after creation.", "Supports negative indexing."],
                "examples": [
                    {"t": "List access and mod", "c": "my_list = ['a', 'b', 'c']\\nmy_list[1] = 'z'\\nprint(my_list)\\nprint(len(my_list))", "o": "['a', 'z', 'c']\\n3"}
                ]
            },
            {
                "title": "List Methods", "icon": "fa-plus-circle",
                "explanation": "Lists come with numerous powerful in-built methods allowing dynamic modifications like sorting, appending, inserting, and popping elements.",
                "points": ["`append(x)` adds x to end.", "`insert(i, x)` inserts x at index i.", "`pop()` removes and returns last item.", "`remove(x)` removes first matching value."],
                "examples": [
                    {"t": "Adding and Removing", "c": "nums = [1, 2]\\nnums.append(3)\\nnums.insert(0, 0)\\nnums.pop()\\nprint(nums)", "o": "[0, 1, 2]"}
                ]
            },
            {
                "title": "List Comprehensions", "icon": "fa-bolt",
                "explanation": "A very Pythonic way to create a list from an iterable cleanly and efficiently in a single elegant line of code.",
                "points": ["Syntax: `[expression for item in iterable if condition]`", "Highly readable and faster than standard loops."],
                "examples": [
                    {"t": "Comprehension Examples", "c": "squares = [x**2 for x in range(4)]\\nevens = [x for x in range(10) if x % 2 == 0]\\nprint(squares)\\nprint(evens)", "o": "[0, 1, 4, 9]\\n[0, 2, 4, 6, 8]"}
                ]
            }
        ]
    },
    "tuples": {
        "title": "Python Tuples",
        "intro": "Tuples are structurally identical to lists, functioning as ordered sequences of elements. The crucial difference: Tuples are completely immutable.",
        "sections": [
            {
                "title": "Creation & Immutability", "icon": "fa-lock",
                "explanation": "Created using parentheses `()`. Due to immutability, operations that change size (append) or alter assignments are forbidden. This guarantees data integrity and offers slight performance boosts.",
                "points": ["To create a 1-item tuple, use a trailing comma: `(item,)`.", "Attempting to assign values like `tup[0] = 1` raises a TypeError."],
                "examples": [
                    {"t": "Tuple assignment error", "c": "t = ('Red', 'Green')\\nprint(t[0])\\n# t[0] = 'Blue' raises TypeError!\\nt_one = (5,)\\nprint(type(t_one))", "o": "Red\\n<class 'tuple'>"}
                ]
            },
            {
                "title": "Tuple Unpacking", "icon": "fa-box-open",
                "explanation": "When we create a tuple, we normally assign values to it. This is called 'packing'. But, we are also allowed to extract those values heavily efficiently back into variables.",
                "points": ["Number of variables must exactly match tuple length.", "The `*` asterisk can collect remaining values as a list if variables don't match."],
                "examples": [
                    {"t": "Unpacking variables", "c": "fruits = ('apple', 'banana', 'cherry', 'date')\\n(a, b, *rest) = fruits\\nprint(a)\\nprint(rest)", "o": "apple\\n['cherry', 'date']"}
                ]
            }
        ]
    },
    "sets": {
        "title": "Python Sets",
        "intro": "Sets are unordered collections with no duplicate elements. They are modeled after mathematical sets, making them incredible for membership testing and eliminating duplicates.",
        "sections": [
            {
                "title": "Unordered & Unique", "icon": "fa-fingerprint",
                "explanation": "Defined with `{}` or the `set()` constructor. Since sets are unordered, they don't support indexing/slicing. Any duplicates provided on creation are automatically scrubbed.",
                "points": ["Sets are mutable but their items must be immutable.", "Instantly removes duplicates from any iterable passed to it."],
                "examples": [
                    {"t": "Set Creation", "c": "s = {1, 2, 2, 3, 3}\\nprint(s)\\nnames = set(['Bob', 'Alice', 'Bob'])\\nprint(names)", "o": "{1, 2, 3}\\n{'Alice', 'Bob'}"}
                ]
            },
            {
                "title": "Set Operations", "icon": "fa-project-diagram",
                "explanation": "Python sets are highly optimized for mathematical operations like unions, intersections, differences, and symmetric differences.",
                "points": ["Union (`|`): All unique items from both sets.", "Intersection (`&`): Only items present in both.", "Difference (`-`): Items in A but not B."],
                "examples": [
                    {"t": "Math Operations", "c": "A = {1, 2, 3}\\nB = {3, 4, 5}\\nprint(A | B)  # Union\\nprint(A & B)  # Intersection\\nprint(A - B)  # Difference", "o": "{1, 2, 3, 4, 5}\\n{3}\\n{1, 2}"}
                ]
            }
        ]
    },
    "dictionaries": {
        "title": "Python Dictionaries",
        "intro": "Dictionaries are powerful collections mapping unique Keys to Values. They are extremely fast, flexible, and pivotal for nearly all complex Python scripts.",
        "sections": [
            {
                "title": "Key-Value Pairs", "icon": "fa-book",
                "explanation": "Created using `{key: value}` format. Keys must be immutable (strings, integers, tuples). As of Python 3.7, dictionaries maintain insertion order.",
                "points": ["Values are accessed by their specified Key via `dict[key]`.", "`dict.get(key)` is safer as it avoids KeyError if key doesn't exist."],
                "examples": [
                    {"t": "Retrieving data", "c": "user = {'name': 'Alice', 'role': 'Admin'}\\nprint(user['name'])\\nprint(user.get('age', 'Not specified'))", "o": "Alice\\nNot specified"}
                ]
            },
            {
                "title": "Keys, Values & Items", "icon": "fa-sitemap",
                "explanation": "Dictionaries provide dedicated view-objects to seamlessly iterate over keys, values, or comprehensively over both simultaneously.",
                "points": ["`keys()`: iterable of keys.", "`values()`: iterable of values.", "`items()`: iterable of (key, value) tuple pairs."],
                "examples": [
                    {"t": "Iteration methods", "c": "scores = {'P1': 100, 'P2': 85}\\nfor key, val in scores.items():\\n    print(f'{key} scored {val}')", "o": "P1 scored 100\\nP2 scored 85"}
                ]
            },
            {
                "title": "Dictionary Manipulation", "icon": "fa-cogs",
                "explanation": "It's easy to add, update, and remove pairs. You can also utilize Dictionary Comprehensions matching list comprehension mechanics.",
                "points": ["Assign `dict[new_key] = val` to append/update.", "`update()` merges another dict.", "`pop(key)` removes & fetches value."],
                "examples": [
                    {"t": "Updates & Pops", "c": "d = {'x': 1}\\nd['y'] = 2\\nd.update({'z': 3, 'x': 5})\\nprint(d)\\nprint(d.pop('y'))", "o": "{'x': 5, 'y': 2, 'z': 3}\\n2"}
                ]
            }
        ]
    },
    "functions": {
        "title": "Functions",
        "intro": "Functions are reusable blocks of code that perform exactly one primary task. They prevent repetitive code, promote modularity, and clean project architecture.",
        "sections": [
            {
                "title": "Definition and Invocation", "icon": "fa-cog",
                "explanation": "Declared using the `def` keyword. Variables passed initially are 'Parameters', processing inside uses those labels, and the output is dispatched via the `return` statement.",
                "points": ["Use informative names.", "If there's no explicit `return`, it implicitly returns `None`."],
                "examples": [
                    {"t": "Basic Function Setup", "c": "def greet(name):\\n    return f'Hello {name}!'\\n\\nres = greet('Alice')\\nprint(res)", "o": "Hello Alice!"}
                ]
            },
            {
                "title": "Default & Keyword Arguments", "icon": "fa-tags",
                "explanation": "You can assign default fallback parameter values. When calling, you can also specify parameter names outright out-of-order, bypassing strict position dependencies.",
                "points": ["Position arguments must precede Keyword arguments.", "Never use mutable types (like lists) as default arguments."],
                "examples": [
                    {"t": "Defaults & Keywords", "c": "def power(base, exp=2):\\n    return base ** exp\\n\\nprint(power(3))\\nprint(power(exp=3, base=2))", "o": "9\\n8"}
                ]
            },
            {
                "title": "Args and Kwargs (* / **)", "icon": "fa-asterisk",
                "explanation": "The asterisk syntax unpacks dynamic lengths of inputs. `*args` captures unbound positional arguments into a tuple. `**kwargs` captures dynamic keyword assignments into a dictionary.",
                "points": ["Provides ultimate flexibility for helper functions.", "The terms args/kwargs are naming conventions, solely the `*` matters."],
                "examples": [
                    {"t": "Dynamic unpacking", "c": "def gather(*args, **kwargs):\\n    print(args)\\n    print(kwargs)\\n\\ngather(1, 2, tag='test')", "o": "(1, 2)\\n{'tag': 'test'}"}
                ]
            }
        ]
    },
    "modules_packages": {
        "title": "Modules & Packages",
        "intro": "As projects grow, writing all code inside one massive file becomes impossible to manage. Modules allow distributing code into categorized files, maximizing reusability.",
        "sections": [
            {
                "title": "Importing Modules", "icon": "fa-file-import",
                "explanation": "Any Python file ending in `.py` is automatically a module. Leveraging the `import` system links one file logically to another, or pulls in the Python Standard Library tools.",
                "points": ["`import math` imports the entire math scope.", "`from math import pi` imports solely pi directly.", "`import foo as f` creates an alias."],
                "examples": [
                    {"t": "Standard Library Import", "c": "import math\\nfrom random import randint\\n\\nprint(math.sqrt(16))\\nprint(randint(1, 10)) # Ex: 7", "o": "4.0\\n7"}
                ]
            },
            {
                "title": "Packages", "icon": "fa-folder-open",
                "explanation": "A Package is basically a directory containing multiple modules and a special `__init__.py` file (acting as the package constructor/identifier). It establishes a hierarchical module structure.",
                "points": ["Use dotted paths like `from package.subpackage import module`.", "Installing third-party packages relies on Pip (`pip install package_name`)."],
                "examples": [
                    {"t": "Package concept visual", "c": "print('from my_project.utils.math_tools import calculate')\\nprint('calculate(10)')", "o": "from my_project.utils.math_tools import calculate\\ncalculate(10)"}
                ]
            }
        ]
    },
    "file_handling": {
        "title": "File Handling",
        "intro": "The capability to read inputs and write outputs to server side text/binary files effectively grants long-term permanence to the data of your application scripts.",
        "sections": [
            {
                "title": "Opening & Reading files", "icon": "fa-book-open",
                "explanation": "Files are opened via the `open(filename, mode)` function. Modes dictate permission sets: `r` (read), `w` (write overwrite), `a` (append), `b` (binary).",
                "points": ["`read()` reads the whole file as a string.", "`readlines()` grabs lines into a list.", "Always use the `with` Context Manager — it auto-closes resources safely."],
                "examples": [
                    {"t": "Using with Context", "c": "with open('demo.txt', 'w') as file:\\n    file.write('Line 1')\\n\\nwith open('demo.txt', 'r') as file:\\n    print(file.read())", "o": "Line 1"}
                ]
            },
            {
                "title": "Writing and Appending", "icon": "fa-save",
                "explanation": "The 'w' command creates the file or immediately deletes existing content. The 'a' command writes incoming strings purely at the tail end of the file context.",
                "points": ["Watch out: `w` immediately destroys old file properties before writing.", "Remember manual newline `\\n` when appending strings."],
                "examples": [
                    {"t": "Appending text", "c": "with open('demo.txt', 'a') as file:\\n    file.write('\\nLine 2')\\n\\nwith open('demo.txt', 'r') as file:\\n    print(file.read())", "o": "Line 1\\nLine 2"}
                ]
            }
        ]
    },
    "exception_handling": {
        "title": "Exception Handling",
        "intro": "Errors discovered during execution are called Exceptions. Handling them cleanly ensures program continuity and controls the fallback outputs instead of outright terminating.",
        "sections": [
            {
                "title": "Try, Except Blocks", "icon": "fa-shield-alt",
                "explanation": "Sensitive code is placed inside the `try` block. If an error surfaces, control falls safely to the matching `except` block logic instead of crashing universally.",
                "points": ["Do not leave broad `except:` commands open, target specific errors (ValueError).", "`Exception as e` catches the error signature dynamically."],
                "examples": [
                    {"t": "Protecting against Zero Division", "c": "try:\\n    result = 10 / 0\\nexcept ZeroDivisionError:\\n    print('Cannot divide by zero!')\\nexcept Exception as e:\\n    print(f'General error: {e}')", "o": "Cannot divide by zero!"}
                ]
            },
            {
                "title": "Finally & Raise", "icon": "fa-exclamation-triangle",
                "explanation": "The `finally` block runs regardless if exceptions fired or not. Crucial for releasing persistent resources. The `raise` keyword manually invokes artificial exceptions.",
                "points": ["`finally` runs 100% of the time seamlessly.", "`raise ValueError('Bad inputs')` throws manual flags internally."],
                "examples": [
                    {"t": "Finally Execution", "c": "try:\\n    value = int('NotANumber')\\nexcept ValueError:\\n    print('Invalid format')\\nfinally:\\n    print('Audit Log Closed.')", "o": "Invalid format\\nAudit Log Closed."}
                ]
            }
        ]
    },
    "oop": {
        "title": "Object Oriented Programming",
        "intro": "OOP groups data and associated behaviors into logical constructs matching real-world models. Python has robust native OOP frameworks via 'Classes' and 'Objects'.",
        "sections": [
            {
                "title": "Classes and Objects", "icon": "fa-cubes",
                "explanation": "A Class is a blueprint (ex: Car constructor). An Object is an independent instance of that blueprint (ex: A Red Ford Mustang). Classes bind states via attributes and abilities via methods.",
                "points": ["`__init__` acts as standard constructor method initializing attributes.", "`self` signifies the current targeted instance running the logic."],
                "examples": [
                    {"t": "Basic Class Design", "c": "class Dog:\\n    def __init__(self, name):\\n        self.name = name\\n    def bark(self):\\n        return f'{self.name} says Woof!'\\n\\npet = Dog('Rex')\\nprint(pet.bark())", "o": "Rex says Woof!"}
                ]
            },
            {
                "title": "Inheritance & Polymorphism", "icon": "fa-bezier-curve",
                "explanation": "Sub-classes inherit all characteristics of their Parent class. This establishes hierarchy. Polymorphism implies functions processing differing inherited objects seamlessly based upon the shared parent interface.",
                "points": ["Pass parent classes explicitly `class Child(Parent):`.", "`super().__init__()` hooks into parent constructor properly inside children structures."],
                "examples": [
                    {"t": "Inheritance Implementation", "c": "class Animal:\\n    def speak(self): return 'Sound'\\n\\nclass Cat(Animal):\\n    def speak(self): return 'Meow'\\n\\nc = Cat()\\nprint(c.speak())", "o": "Meow"}
                ]
            }
        ]
    },
    "advanced_python": {
        "title": "Advanced Python Patterns",
        "intro": "Elevate scripts from working concepts to production grade efficiency through advanced iteration logic and deep metagaming of the interpreter context.",
        "sections": [
            {
                "title": "Generators & Yield", "icon": "fa-magic",
                "explanation": "Generators behave like iterators holding zero memory footprint. Instead of retaining giant arrays sequentially, they logically `yield` a variable, pause operation context, and resume automatically.",
                "points": ["Utilize `yield` rather than `return`.", "Massively mitigates RAM bottlenecks generating millions of entries in tight sequences."],
                "examples": [
                    {"t": "Using Yield", "c": "def count_up(n):\\n    i = 1\\n    while i <= n:\\n        yield i\\n        i += 1\\n\\nfor val in count_up(3):\\n    print(val)", "o": "1\\n2\\n3"}
                ]
            },
            {
                "title": "Decorators", "icon": "fa-gift",
                "explanation": "Decorators accept an existing function explicitly, wrap it dynamically around secondary shell logic, and return improved modifications seamlessly. Often marked visually utilizing `@name` formatting.",
                "points": ["Excellent for globally tagging logs or enforcing standard authentications.", "Closures form the underlying backbone mechanism."],
                "examples": [
                    {"t": "Logging Decorator", "c": "def uppercase(func):\\n    def wrapper():\\n        res = func()\\n        return res.upper()\\n    return wrapper\\n\\n@uppercase\\ndef greet():\\n    return 'hi'\\n\\nprint(greet())", "o": "HI"}
                ]
            }
        ]
    },
    "data_structures": {
        "title": "Advanced Data Structures",
        "intro": "Optimizing search or scaling demands explicit understanding beyond standard implementations targeting heavy computational throughput.",
        "sections": [
            {
                "title": "Stacks and Queues", "icon": "fa-layer-group",
                "explanation": "Linear patterns mapping execution. Stacks use LIFO (Last In, First Out). Queues map strictly FIFO (First In, First Out).",
                "points": ["Lists work ok for Stacks via `.append()` / `.pop()`.", "For rigorous Queues, exclusively utilize `collections.deque`."],
                "examples": [
                    {"t": "Deque Implementation", "c": "from collections import deque\\nq = deque(['a', 'b'])\\nq.append('c')\\nprint(q.popleft())\\nprint(q)", "o": "a\\ndeque(['b', 'c'])"}
                ]
            },
            {
                "title": "Linked Lists & Trees", "icon": "fa-network-wired",
                "explanation": "Advanced referencing schema relying purely on isolated nodes tracking logical neighbors. Highly powerful logic models for AI mapping implementations.",
                "points": ["Lists map linear connections (next/prev nodes).", "Trees map multi-faceted hierarchical architectures (binary trees)."],
                "examples": [
                    {"t": "Node Skeleton", "c": "class Node:\\n    def __init__(self, data):\\n        self.data = data\\n        self.next = None\\n\\nn1 = Node(1)\\nnn2 = Node(2)\\nn1.next = nn2\\nprint(n1.next.data)", "o": "2"}
                ]
            }
        ]
    },
    "python_libraries": {
        "title": "Crucial Python Libraries",
        "intro": "The real strength of Python is its absurdly prolific package library architecture dictating global standards across practically every scientific or computational sector currently tracked globally.",
        "sections": [
            {
                "title": "Data Science & Mathematics", "icon": "fa-chart-pie",
                "explanation": "The NumPy and Pandas ecosystems practically run modern data infrastructures. They map heavy C-tier optimizations onto intuitive multi-dimensional manipulations seamlessly.",
                "points": ["NumPy: High-Performance parallel array architectures.", "Pandas: Intuitive dataset visualizations mapping relational structures natively."],
                "examples": [
                    {"t": "Library Abstract Conceptualization", "c": "import numpy as np\\narr = np.array([1, 2, 3])\\nprint(arr * 2)", "o": "[2 4 6]"}
                ]
            },
            {
                "title": "Web & Scripting", "icon": "fa-globe",
                "explanation": "Request handling frameworks interface Python backends dynamically against global web protocols and APIs natively. Django and Requests rank dominant.",
                "points": ["Requests: Simple API query architectures handling protocol layers underneath.", "Django/Flask: Scaling web applications via structured route injections."],
                "examples": [
                    {"t": "Abstract HTTP mapping", "c": "import requests\\n# res = requests.get('url')\\nprint('Successfully mapped GET.')", "o": "Successfully mapped GET."}
                ]
            }
        ]
    },
    "python_interview": {
        "title": "Developer Interview Guide",
        "intro": "Mastering technical evaluations heavily emphasizes conveying core patterns explicitly and showcasing clear logic mapping isolated against deep technical traps systematically evaluated.",
        "sections": [
            {
                "title": "Core Nuances (Mutable vs Immutable)", "icon": "fa-gavel",
                "explanation": "Variables operate natively by-reference internally. The crucial question always hinges explicitly recognizing if passing specific variables functions isolated or alters global states.",
                "points": ["Immutable (Int, Str, Tuple) generate isolated memory layers upon modification attempts.", "Mutable (Lists, Dicts, Sets) natively manipulate identical tracked targets constantly."],
                "examples": [
                    {"t": "Mutation Trap Execution", "c": "a = [1]\\nb = a\\nb.append(2)\\nprint(a)", "o": "[1, 2]"}
                ]
            },
            {
                "title": "Time Complexity (Big O Notation)", "icon": "fa-tachometer-alt",
                "explanation": "You map execution metrics strictly charting infinite sequence scaling boundaries isolating computational limits relative towards isolated dataset growth strictly.",
                "points": ["Lookup dictionaries (Hashmaps) scale uniformly natively O(1).", "Nested logical loops globally risk heavy quadratic processing overheads O(N^2)."],
                "examples": [
                    {"t": "Complexity Abstraction", "c": "# O(1) Fetching\\ndict_map = {1: 'x'}\\nres = dict_map[1]\\nprint('O(1) Complete', res)", "o": "O(1) Complete x"}
                ]
            }
        ]
    }
}


def build_html(topic_data):
    html = f"<div class='container'>\\n"
    html += f"  <div class='header'>\\n    <h1>{topic_data['title']}</h1>\\n"
    html += "    <p>A Comprehensive Guide with Clear Explanations and Examples</p>\\n  </div>\\n"
    html += "  <div class='content'>\\n"
    
    html += "    <div class='intro'>\\n"
    html += f"      <p><strong>Overview:</strong> {topic_data['intro']}</p>\\n"
    html += "    </div>\\n"
    
    for sec in topic_data['sections']:
        html += f"    <div class='topic'>\\n"
        html += f"      <h2 class='topic-title'><i class='fas {sec.get('icon', 'fa-code')}'></i> {sec['title']}</h2>\\n"
        html += f"      <p class='explanation'>{sec['explanation']}</p>\\n"
        
        # points
        html += f"      <div class='key-points'>\\n        <strong>Key Points:</strong>\\n        <ul>\\n"
        for p in sec.get('points', []):
            html += f"          <li>{p}</li>\\n"
        html += "        </ul>\\n      </div>\\n"
        
        # examples
        for i, ex in enumerate(sec.get('examples', [])):
            html += "      <div class='example-block'>\\n"
            html += f"        <div class='example-header'><i class='fas fa-terminal'></i> Example {i+1}: {ex['t']}</div>\\n"
            html += f"        <pre class='example-code'><code>{ex['c']}</code></pre>\\n"
            if ex.get('o'):
                html += f"        <div class='example-output'><div class='output-label'>Output:</div>{ex['o'].replace(chr(10), '<br>')}</div>\\n"
            html += "      </div>\\n"
            
        html += "    </div>\\n"
        
    html += "  </div>\\n"
    html += "  <div class='footer'><p>&copy; 2026 Python Learning Track</p></div>\\n</div>\\n"
    
    return css_style + html

def process_file():
    js_file = r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\tracks_data.js'
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()

    for sub_id, data in topics_data.items():
        new_html = build_html(data)
        escaped_str = json.dumps(new_html)
        
        # We need to replace the explanation field of this sub_id inside "python".
        # Format in tracks_data.js: "sub_id": { ... "explanation": "...", "examples": ...
        # Assuming the order is preserved
        pattern = r'(\"' + sub_id + r'\":\s*\{\s*\"title\":\s*\"[^\"]*\",\s*\"explanation\":\s*)\"(?:\\\\\"|[^\"])*\"(.*)'
        
        # Because replacing directly via regex on the whole huge file might be slow or mismatch, 
        # let's try a safer split approach.
        parts = js_content.split('"{sub_id}": {{'.format(sub_id=sub_id))
        if len(parts) == 1:
            # Maybe single quotes or different spacing
            parts = re.split(rf'\"{sub_id}\":\s*\{{', js_content)
        
        if len(parts) > 1:
            # We found the block!
            right_part = parts[1]
            # Find the explanation key
            sub_parts = re.split(rf'\"explanation\":\s*', right_part, maxsplit=1)
            if len(sub_parts) > 1:
                # The trailing string starts with a double quote and goes until the end of the string
                # let's regex replace just that
                subpattern = r'^\"(?:\\\\\"|[^\"])*\"'
                new_right_part = sub_parts[0] + '"explanation": ' + re.sub(subpattern, escaped_str.replace('\\', r'\\'), sub_parts[1], count=1)
                
                parts[1] = new_right_part
                js_content = f'"{sub_id}": {{'.join(parts)
            else:
                print(f"Skipping {sub_id}, no explanation key found inside block")
        else:
            print(f"Skipping {sub_id}, not found")
            

    with open(js_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("Successfully updated all topics!")

if __name__ == "__main__":
    process_file()
