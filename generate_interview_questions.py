import json

file_path = r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

json_start = text.find('{')
json_end = text.rfind('}') + 1

data = json.loads(text[json_start:json_end])

# Generate 40 questions
questions = {
    "Beginner": [
        ("What is Python and why is it so popular?", "Python is a high-level, dynamically typed, interpreted programming language known for its extreme readability, massive ecosystem, and multi-paradigm approach."),
        ("What is a PEP 8?", "PEP 8 is the official Python Enhancement Proposal that provides coding conventions and style guidelines for writing readable Python code."),
        ("What is the difference between a list and a tuple?", "Lists are mutable (can be changed after creation), while tuples are immutable (cannot be modified). Lists use [] and tuples use ()."),
        ("What are namespaces in Python?", "A namespace is a naming system to ensure all object names are unique and can be used without conflict. Examples: Built-in, Global, Local."),
        ("What is a dictionary in Python?", "A dictionary is an unordered, mutable collection of key-value pairs where keys must be unique and immutable."),
        ("Explain how Python handles memory management.", "Python uses a private heap containing all objects and relies heavily on an automatic garbage collector utilizing reference counting and generational cyclic garbage collection."),
        ("What is the difference between break, continue, and pass?", "`break` terminates the loop entirely. `continue` skips the rest of the current iteration. `pass` is an empty null operation used as a placeholder."),
        ("What is slicing in Python?", "Slicing is a mechanism to extract a range of items from sequences like lists, tuples, or strings using the `[start:stop:step]` syntax."),
        ("How do you convert a string to an integer?", "By using the built-in `int()` function, provided the string contains exclusively numeric characters."),
        ("What is the difference between == and is?", "`==` checks for value equality, whereas `is` checks for object identity (if they point to the exact same memory address)."),
        ("What is 'self' in Python?", "`self` represents the instance of the class. It binds the attributes with the given arguments to the object natively."),
        ("What are local and global variables?", "Local variables are defined inside a function and isolated there. Global variables are defined outside and accessible everywhere."),
        ("Is Python strongly or weakly typed?", "Python is strongly typed (it won't implicitly coerce a string and int together) and dynamically typed (types are assigned at runtime)."),
        ("What is a docstring?", "A docstring is a multi-line string literal (`\"\"\"...\"\"\"`) specifically written as the first statement in a module or function to serve as documentation document."),
        ("How can you reverse a string in Python?", "The most Pythonic way is by using slicing: `reversed_string = original_string[::-1]`.")
    ],
    "Intermediate": [
        ("What are Python decorators?", "A decorator is a design pattern that allows you to dynamically modify or wrap the behavior of a function or class without permanently modifying its source code."),
        ("What is a lambda function?", "A lambda function is a small, anonymous inline function defined with the `lambda` keyword. It can take any number of arguments but only contains one expression."),
        ("What is the difference between *args and **kwargs?", "`*args` passes a variable number of positional arguments as a tuple. `**kwargs` passes a variable number of keyword arguments as a dictionary."),
        ("What are generators in Python?", "Generators are functions that use the `yield` keyword instead of `return` to return an iterator object, calculating values sequentially to save massive memory."),
        ("What is list comprehension?", "It's an elegant and concise syntax to create a new list from an existing iterable, typically utilizing a single line like `[x**2 for x in nums if x > 0]`."),
        ("What is the GIL (Global Interpreter Lock)?", "A mutex in CPython that ensures only one thread executes Python bytecodes at any given time, limiting true parallel multithreading capability."),
        ("Explain Python's __init__ method.", "It is the constructor method natively called when an object is instantiated from a class, primarily used to initialize the object's core attributes."),
        ("How does exception handling work in Python?", "By utilizing the `try`, `except`, `else`, and `finally` blocks to gracefully catch runtime errors without catastrophically crashing the program."),
        ("What are deep copy and shallow copy?", "A shallow copy constructs a new object but references inner objects. A deep copy fully recursively clones everything, creating an entirely isolated copy of all nested objects."),
        ("Explain map(), filter(), and reduce().", "`map` applies a function over an iterable. `filter` removes elements evaluating to False. `reduce` (from functools) cumulatively applies a rolling computation over an iterable."),
        ("What is monkey patching?", "Monkey patching refers to dynamically modifying or replacing a class or module's behavior at runtime without altering its original source file."),
        ("What is a context manager?", "An object that explicitly controls resources utilizing the `with` statement, reliably configuring `__enter__` and `__exit__` methods (like file handling)."),
        ("What is the difference between append() and extend()?", "`append` adds its argument as a single element to the end of a list. `extend` iterates over its argument and adds each element sequentially to the list."),
        ("How do you manage dependencies in Python?", "By utilizing virtual environments (using `venv` or `virtualenv`) and generating a `requirements.txt` file tracked via tools like `pip`."),
        ("What is duck typing in Python?", "The concept that an object's suitability is determined by the presence of certain methods and properties, rather than strictly its structural type ('If it walks and quacks like a duck, it is a duck').")
    ],
    "Advanced": [
        ("How does Python's Garbage Collection explicitly handle circular references?", "The Generational Garbage Collector actively scans for isolated cycles of objects that reference each other but are dead to the main program, systematically breaking the cycle and clearing memory."),
        ("What are metaclasses?", "Metaclasses are the 'classes of classes'. They dictate how a class itself behaves and is instantiated, often extending `type` to intercept class creation."),
        ("How can you mitigate the GIL bottleneck in CPU-bound Python tasks?", "By bypassing threading entirely and utilizing the `multiprocessing` module, which spawns independent OS processes, each with its own independent Python interpreter and GIL."),
        ("Explain __new__ vs __init__ in Python.", "`__new__` strictly orchestrates object creation and returns the new instance. `__init__` takes that returned instance and initializes its physical attributes."),
        ("What are coroutines in Asyncio?", "Coroutines are specialized generator functions defined with `async def` that cooperatively yield execution control via `await` to manage highly concurrent IO tasks on a single thread."),
        ("How do Python slots (`__slots__`) work?", "By explicitly defining `__slots__` inside a class, Python fundamentally avoids allocating a dynamic `__dict__` for instances, catastrophically reducing memory footprint for millions of objects."),
        ("What is method resolution order (MRO)?", "MRO dictates the exact hierarchical order in which base classes are systematically searched when executing a method in multiple inheritance, utilizing the C3 Linearization algorithm."),
        ("What are descriptors in Python?", "Classes that implement `__get__`, `__set__`, or `__delete__` methods. They are used under the hood to implement properties, methods, nested object bounds, and `@classmethod`."),
        ("Explain the difference between @staticmethod and @classmethod.", "`@classmethod` natively receives the class context itself (`cls`) as the first argument, heavily used to create alternative constructors. `@staticmethod` receives nothing and is purely a generic utility function confined to a class namespace."),
        ("What is the purpose of the `functools.wraps` decorator?", "It meticulously updates a wrapper function to look functionally identical to the wrapped function by copying over essential metadata like `__name__`, `__doc__`, and signature traces.")
    ]
}

html_content = ""
for level, qlist in questions.items():
    html_content += f"<h3 style='color:#1e40af; font-size:1.6rem; margin-top:40px; margin-bottom:15px; border-bottom: 2px solid #bfdbfe; padding-bottom: 10px;'>{level} Level Questions</h3>"
    for i, (q, a) in enumerate(qlist):
        html_content += f"""
        <div style='background:#f8fafc; border-left:4px solid #3b82f6; padding:20px; border-radius:10px; margin-bottom:20px; box-shadow:0 4px 6px rgba(0,0,0,0.02);'>
            <h4 style='color:#0f172a; margin-bottom:10px; font-size:1.15rem;'><span style='color:#3b82f6;'>Q{i+1}:</span> {q}</h4>
            <p style='color:#334155; line-height:1.7; font-size:1.05rem;'>{a}</p>
        </div>
        """

# 2. Append node natively to tracks_data python path
python_nodes = data['python']['nodes']
if python_nodes[-1]['id'] != 'python_interview':
    new_node = {
        "id": "python_interview",
        "title": "Interview Guide",
        "x": 0, # Will be handled by tightening script
        "y": 0,
        "status": "locked",
        "phase": 5,
        "parent": "python_libraries"
    }
    python_nodes.append(new_node)

# 3. Create content object
data['python']['content']['python_interview'] = {
    "title": "Python Developer Interview Guide",
    "explanation": f"<div style='line-height: 1.8;'><h3 style='color:#0f172a; font-size:1.8rem; border-bottom:2px solid #e0f2fe; padding-bottom:12px; margin-bottom:20px;'>Top 40 Python Interview Questions</h3><p style='color:#475569; font-size:1.1rem; margin-bottom:30px;'>Ace your upcoming technical interviews with this systematically curated list of 40 essential Python concepts frequently drilled by top-tier company recruiters!</p>{html_content}</div>",
    "examples": [],
    "concept_quiz": [],
    "hands_on": None,
    "problem_solving": []
}

# Apply tightness
y_coord = 150
for i, node in enumerate(data['python']['nodes']):
    node['x'] = 1250 if i % 2 == 0 else 1530
    node['y'] = y_coord
    y_coord += 160

# Write back
new_text = "const tracksData = " + json.dumps(data, indent=4) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Injected 40 Python Questions seamlessly!")
