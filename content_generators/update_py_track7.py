import json

TECHNICAL_IO_SCENARIOS = {
    "python_basics": [
        ("Q1: Basic Print", "Write a python script to output the exact string below.\n\nInput:\nNone\n\nExpected Output:\nHello World", "print('Hello World')"),
        ("Q2: Variable Assignment", "Assign the value 100 to a variable 'score' and print it.\n\nInput:\n100\n\nExpected Output:\n100", "score = 100\nprint(score)"),
        ("Q3: Type Casting (Str to Int)", "Convert the string '50' into an integer and print the result completely.\n\nInput:\n'50'\n\nExpected Output:\n50", "num_str = '50'\nnum_int = int(num_str)\nprint(num_int)"),
        ("Q4: Type Checking", "Initialize x = 3.14. Print the type of x.\n\nInput:\nNone\n\nExpected Output:\n<class 'float'>", "x = 3.14\nprint(type(x))"),
        ("Q5: Simple Input Simulation", "Initialize name='Alice'. Print a greeting.\n\nInput:\nname = 'Alice'\n\nExpected Output:\nHello, Alice", "name = 'Alice'\nprint('Hello, ' + name)")
    ],
    "operators": [
        ("Q1: Basic Addition", "Add numbers 15 and 25.\n\nInput:\n15, 25\n\nExpected Output:\n40", "print(15 + 25)"),
        ("Q2: Modulo Operation", "Find the remainder of 10 divided by 3.\n\nInput:\n10, 3\n\nExpected Output:\n1", "print(10 % 3)"),
        ("Q3: Assignment and Increment", "Initialize x=5, then use += to add 10, then print x.\n\nInput:\nNone\n\nExpected Output:\n15", "x = 5\nx += 10\nprint(x)"),
        ("Q4: Comparison Operator", "Check if 100 > 50 and print the boolean result.\n\nInput:\nNone\n\nExpected Output:\nTrue", "print(100 > 50)"),
        ("Q5: Logical Operators", "Check if 5 > 3 AND 8 < 10.\n\nInput:\nNone\n\nExpected Output:\nTrue", "x = 5\ny = 3\na = 8\nb = 10\nprint(x > y and a < b)")
    ],
    "control_flow": [
        ("Q1: Basic If Statement", "If x=10, print 'Positive' if x > 0.\n\nInput:\nx = 10\n\nExpected Output:\nPositive", "x = 10\nif x > 0:\n    print('Positive')"),
        ("Q2: If-Else Even/Odd", "Check if a number is even or odd.\n\nInput:\nx = 7\n\nExpected Output:\nOdd", "x = 7\nif x % 2 == 0:\n    print('Even')\nelse:\n    print('Odd')"),
        ("Q3: Elif Grading", "If score > 90 print A, > 80 B, else C.\n\nInput:\nscore = 85\n\nExpected Output:\nB", "score = 85\nif score > 90:\n    print('A')\nelif score > 80:\n    print('B')\nelse:\n    print('C')"),
        ("Q4: Nested If", "If x > 0, check if x > 50. If so, print 'Large Positive'.\n\nInput:\nx = 60\n\nExpected Output:\nLarge Positive", "x = 60\nif x > 0:\n    if x > 50:\n        print('Large Positive')"),
        ("Q5: Boolean State", "If is_active is False, print 'Offline'.\n\nInput:\nis_active = False\n\nExpected Output:\nOffline", "is_active = False\nif not is_active:\n    print('Offline')")
    ],
    "loops": [
        ("Q1: For Loop Range", "Use a for loop to print numbers from 0 to 4.\n\nInput:\nrange(5)\n\nExpected Output:\n0\n1\n2\n3\n4", "for i in range(5):\n    print(i)"),
        ("Q2: While Loop", "Iterate while i < 3, starting from i=0.\n\nInput:\nNone\n\nExpected Output:\n0\n1\n2", "i = 0\nwhile i < 3:\n    print(i)\n    i += 1"),
        ("Q3: Iterating List", "Print each element in the list.\n\nInput:\n['A', 'B', 'C']\n\nExpected Output:\nA\nB\nC", "for char in ['A', 'B', 'C']:\n    print(char)"),
        ("Q4: Break Statement", "Loop from 1 to 5. Break if i == 3. Print the numbers.\n\nInput:\nNone\n\nExpected Output:\n1\n2", "for i in range(1, 6):\n    if i == 3:\n        break\n    print(i)"),
        ("Q5: Continue Statement", "Loop 1 to 4. Skip printing if i == 2.\n\nInput:\nNone\n\nExpected Output:\n1\n3\n4", "for i in range(1, 5):\n    if i == 2:\n        continue\n    print(i)")
    ],
    "strings": [
        ("Q1: String Length", "Find the length of the string.\n\nInput:\n'Python'\n\nExpected Output:\n6", "s = 'Python'\nprint(len(s))"),
        ("Q2: String Indexing", "Print the first and last character of the given string.\n\nInput:\n'Hello'\n\nExpected Output:\nH\no", "s = 'Hello'\nprint(s[0])\nprint(s[-1])"),
        ("Q3: String Slicing", "Extract characters from index position 0 to 3.\n\nInput:\n'Programming'\n\nExpected Output:\nProg", "s = 'Programming'\nprint(s[0:4])"),
        ("Q4: Upper Case", "Convert string completely to uppercase.\n\nInput:\n'python'\n\nExpected Output:\nPYTHON", "s = 'python'\nprint(s.upper())"),
        ("Q5: F-String Formatting", "Inject explicit variables into a string.\n\nInput:\nlang = 'Python', ver = 3\n\nExpected Output:\nLanguage: Python, Version: 3", "lang = 'Python'\nver = 3\nprint(f'Language: {lang}, Version: {ver}')")
    ],
    "lists": [
        ("Q1: Modify One Element", "Update the 2nd element of the list to 200.\n\nInput:\n[10, 20, 30]\n\nExpected Output:\n[10, 200, 30]", "lst = [10, 20, 30]\nlst[1] = 200\nprint(lst)"),
        ("Q2: Add Element at the End", "Append number 4 to the list.\n\nInput:\n[1, 2, 3]\n\nExpected Output:\n[1, 2, 3, 4]", "lst = [1, 2, 3]\nlst.append(4)\nprint(lst)"),
        ("Q3: Add Element at the Beginning", "Insert 5 at index 0.\n\nInput:\n[10, 15, 20]\n\nExpected Output:\n[5, 10, 15, 20]", "lst = [10, 15, 20]\nlst.insert(0, 5)\nprint(lst)"),
        ("Q4: Insert in the Middle", "Insert 25 at index 2.\n\nInput:\n[10, 20, 30, 40]\n\nExpected Output:\n[10, 20, 25, 30, 40]", "lst = [10, 20, 30, 40]\nlst.insert(2, 25)\nprint(lst)"),
        ("Q5: Remove List Element", "Remove the number 25 from the list.\n\nInput:\n[10, 20, 25, 30]\n\nExpected Output:\n[10, 20, 30]", "lst = [10, 20, 25, 30]\nlst.remove(25)\nprint(lst)")
    ],
    "tuples": [
        ("Q1: Create Tuple", "Create and print a tuple of ints.\n\nInput:\n1, 2, 3\n\nExpected Output:\n(1, 2, 3)", "t = (1, 2, 3)\nprint(t)"),
        ("Q2: Tuple Indexing", "Extract the 2nd element.\n\nInput:\n('a', 'b', 'c')\n\nExpected Output:\nb", "t = ('a', 'b', 'c')\nprint(t[1])"),
        ("Q3: Unpacking", "Unpack tuple to x, y and print like dictionary.\n\nInput:\n(10, 20)\n\nExpected Output:\nx: 10, y: 20", "t = (10, 20)\nx, y = t\nprint(f'x: {x}, y: {y}')"),
        ("Q4: Concatenation", "Add two tuples structurally.\n\nInput:\n(1,) and (2, 3)\n\nExpected Output:\n(1, 2, 3)", "t1 = (1,)\nt2 = (2, 3)\nprint(t1 + t2)"),
        ("Q5: Tuple Length", "Measure number of elements.\n\nInput:\n(5, 10, 15, 20)\n\nExpected Output:\n4", "t = (5, 10, 15, 20)\nprint(len(t))")
    ],
    "sets": [
        ("Q1: Create Set", "Initialize set with duplicates.\n\nInput:\n[1, 2, 2, 3, 3]\n\nExpected Output:\n{1, 2, 3}", "s = set([1, 2, 2, 3, 3])\nprint(s)"),
        ("Q2: Add Element", "Add an element to the set.\n\nInput:\n{1, 2}\nAdd: 3\n\nExpected Output:\n{1, 2, 3}", "s = {1, 2}\ns.add(3)\nprint(s)"),
        ("Q3: Remove Element", "Remove specific item entirely.\n\nInput:\n{10, 20, 30}\nRemove: 20\n\nExpected Output:\n{10, 30}", "s = {10, 20, 30}\ns.remove(20)\nprint(s)"),
        ("Q4: Set Union", "Combine two sets.\n\nInput:\n{1, 2} | {2, 3}\n\nExpected Output:\n{1, 2, 3}", "print({1, 2} | {2, 3})"),
        ("Q5: Set Intersection", "Find common elements.\n\nInput:\n{1, 2, 3} & {3, 4, 5}\n\nExpected Output:\n{3}", "print({1, 2, 3} & {3, 4, 5})")
    ]
}

# Provide defaults for the deeply advanced modules to prevent NoneType crash
keys_ordered = [
    "dictionaries", "functions",
    "modules_packages", "file_handling", "exception_handling", "oop", "advanced_python",
    "data_structures", "python_libraries"
]

for k in keys_ordered:
    TECHNICAL_IO_SCENARIOS[k] = [
        ("Q1: Technical Overview", f"Write script for {k}.", "print('Solution block')"),
        ("Q2: Advanced Operations", f"Perform logic for {k}.", "print('Solution block 2')"),
        ("Q3: Data Injection", "Inject structural mapping.", "print('Solution module')"),
        ("Q4: File Validation", "Validate components strictly.", "print('Verified.')"),
        ("Q5: System Testing", "Evaluate final outputs.", "print('Completed')")
    ]

file_path = r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

start_idx = text.find('"python": {')
if start_idx != -1:
    brace_count = 0
    in_python = False
    end_idx = -1
    for idx in range(start_idx + len('"python": '), len(text)):
        char = text[idx]
        if char == '{':
            if not in_python:
                in_python = True
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if in_python and brace_count == 0:
                end_idx = idx + 1
                break
                
    if end_idx != -1:
        python_text = text[start_idx + len('"python": '):end_idx]
        python_obj = json.loads(python_text)
        
        for k in python_obj['content']:
            if k in TECHNICAL_IO_SCENARIOS:
                new_probs = []
                for q_tuple in TECHNICAL_IO_SCENARIOS[k]:
                    title_str = q_tuple[0]
                    desc_str = q_tuple[1]
                    code_ans = q_tuple[2] # Actual Code injected
                    new_probs.append({
                        "title": title_str,
                        "description": desc_str,
                        "hint": "Match the expected output exactly.",
                        "code": code_ans
                    })
                python_obj['content'][k]['problem_solving'] = new_probs
        
        python_json = json.dumps(python_obj, indent=4)
        new_text = text[:start_idx] + '"python": ' + python_json + text[end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Updated JSON. Overwrote problem solving with Explicit CODE Solutions!")
    else:
        print("Failed to find end index.")
else:
    print("Cannot find 'python' block.")
