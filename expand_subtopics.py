import json

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

# Expand ALL short subtopics across all languages
# Format: { "lang/topic_id": { sub_index: "new_content" } }

expansions = {
    # ============ PYTHON ============
    "python/operators": {0: "<p>Python operators have a clear precedence order: <code>**</code> (exponent) is highest, then <code>*</code>, <code>/</code>, <code>//</code>, <code>%</code>, then <code>+</code>, <code>-</code>. Use parentheses liberally to make your intentions clear and avoid subtle bugs with operator precedence.</p><p>Python also supports augmented assignment operators like <code>+=</code>, <code>-=</code>, <code>*=</code> for concise modification of variables.</p>"},
    "python/control_flow": {0: "<p>Python uses <code>if</code>, <code>elif</code>, and <code>else</code> for branching. Unlike Java/C, Python uses <strong>indentation</strong> (whitespace) to define code blocks instead of curly braces. This enforces readable code structure.</p><p>Python also supports the ternary expression: <code>result = 'even' if x % 2 == 0 else 'odd'</code> for concise inline conditions.</p>"},
    "python/loops": {0: "<p>Python's <code>for</code> loop iterates directly over sequences (lists, strings, ranges) rather than using index counters. <code>for item in mylist:</code> gives you each element directly. Use <code>range(start, stop, step)</code> when you need numeric iteration.</p><p>The <code>while</code> loop runs as long as a condition is True. Both loops support <code>break</code> (exit loop), <code>continue</code> (skip to next iteration), and an optional <code>else</code> clause that runs when the loop completes without breaking.</p>"},
    "python/tuples": {0: "<p>Tuples are created using round parentheses <code>()</code> instead of square brackets. Unlike lists, tuples are <strong>immutable</strong> - once created, elements cannot be added, removed, or changed. This makes them perfect for data that should never be modified, like coordinates, database records, or dictionary keys.</p><p>Tuples are faster than lists due to their immutability, and they can be used as dictionary keys (lists cannot). Unpack tuples easily: <code>x, y, z = (1, 2, 3)</code>.</p>"},
    "python/sets": {
        0: "<p>Sets are created using curly braces <code>{}</code> without key-value pairs, or with <code>set()</code>. They store only <strong>unique elements</strong> - duplicates are silently discarded. Sets are unordered, so you cannot access elements by index.</p><p>Sets are incredibly efficient for membership testing: <code>if item in my_set</code> runs in O(1) time compared to O(n) for lists. Use sets when you need to check 'is this item already present?' frequently.</p>",
        1: "<p>Sets support powerful mathematical operations: <code>union (|)</code> combines two sets, <code>intersection (&)</code> finds common elements, <code>difference (-)</code> finds elements in one but not the other, and <code>symmetric_difference (^)</code> finds elements in either but not both.</p><p>Example: <code>set_a = {1, 2, 3}; set_b = {2, 3, 4}; print(set_a & set_b)</code> outputs <code>{2, 3}</code>. These operations make sets perfect for comparing datasets, finding overlaps, and eliminating duplicates.</p>"
    },
    "python/modules_packages": {
        0: "<p>By using the <code>import</code> keyword, you can grab code written in another file or library and use it in your program. <code>import math</code> gives access to <code>math.sqrt()</code>, <code>math.pi</code>, etc. Use <code>from math import sqrt</code> to import specific functions directly.</p><p>You can also alias imports: <code>import numpy as np</code> is the standard convention. This keeps your code clean while avoiding naming conflicts between modules.</p>",
        1: "<p>Python comes with hundreds of built-in modules (like <code>math</code>, <code>random</code>, <code>os</code>, <code>json</code>, <code>datetime</code>) collectively called the Standard Library. These cover math operations, file handling, system interaction, networking, and more - all without installing anything extra.</p><p>Key modules: <code>os</code> (file system operations), <code>json</code> (JSON parsing), <code>datetime</code> (date/time handling), <code>re</code> (regular expressions), <code>collections</code> (advanced data structures like Counter and defaultdict).</p>"
    },
    "python/file_handling": {
        0: "<p>You use the <code>open()</code> function with mode flags: <code>'r'</code> (read), <code>'w'</code> (write - overwrites), <code>'a'</code> (append), <code>'rb'</code> (read binary). Read methods: <code>.read()</code> (entire file as string), <code>.readline()</code> (one line), <code>.readlines()</code> (all lines as list).</p><p>Writing: <code>f.write('text')</code> writes a string. Always close files after use to free system resources and ensure data is flushed to disk.</p>",
        1: "<p>Always use the <code>with open() as f:</code> syntax (context manager) because it safely and automatically closes the file even if an error occurs. Without <code>with</code>, forgetting to call <code>f.close()</code> can lead to data corruption or resource leaks.</p><p>Example: <code>with open('data.txt', 'r') as f: content = f.read()</code>. The file is guaranteed to close when the block ends, even if an exception is raised inside it.</p>"
    },
    "python/exception_handling": {
        0: "<p>You put risky code inside a <code>try:</code> block. If it crashes, Python immediately jumps to the matching <code>except:</code> block instead of terminating. You can catch specific exceptions: <code>except ValueError:</code> only catches value errors, letting other exceptions propagate.</p><p>Catch multiple exceptions: <code>except (TypeError, ValueError) as e:</code>. Access the error message with <code>str(e)</code>. You can also use bare <code>except:</code> to catch everything, but this is discouraged as it hides bugs.</p>",
        1: "<p>The <code>finally:</code> block runs absolutely no matter what - whether an error occurred or not, whether the error was caught or not. This is crucial for cleanup operations like closing database connections, releasing file locks, or stopping network streams.</p><p>Combine all three: <code>try: ... except: ... else: ... finally: ...</code>. The <code>else:</code> block runs only when NO exception occurred - useful for code that should only execute on success.</p>"
    },
    "python/oop": {
        0: "<p>A <code>Class</code> is a blueprint defining properties and behaviors. An <code>Object</code> is an actual instance created from that blueprint. Think of a class as a cookie cutter and objects as the cookies - same shape, different toppings.</p><p>Define a class: <code>class Dog:</code>. Create an object: <code>my_dog = Dog()</code>. Each object has its own independent data but shares the same methods defined in the class. You can create unlimited objects from a single class.</p>",
        1: "<p>Attributes are variables that belong to the object (like <code>self.color</code>, <code>self.speed</code>). Methods are functions defined inside the class that operate on the object's data. The first parameter of every method is <code>self</code>, which refers to the current object instance.</p><p>Access attributes and call methods with dot notation: <code>my_dog.name</code>, <code>my_dog.bark()</code>. Class attributes (defined outside <code>__init__</code>) are shared by all instances.</p>",
        2: "<p>Also known as the Constructor, the <code>__init__</code> method runs automatically when you create a new object. It initializes the object's attributes with values passed during creation: <code>my_dog = Dog('Rex', 5)</code> calls <code>__init__(self, name, age)</code>.</p><p>Inside <code>__init__</code>, use <code>self.name = name</code> to store the parameter as an object attribute. Without <code>__init__</code>, you'd have to set each attribute manually after creation. Every class should have one.</p>"
    },
    "python/advanced_python": {
        0: "<p>A highly compact way to create lists in just one line of code. Instead of writing a for-loop to build a list, write: <code>squares = [x**2 for x in range(10)]</code>. This creates <code>[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]</code>.</p><p>Add filtering with an if-clause: <code>evens = [x for x in range(20) if x % 2 == 0]</code>. You can even nest them for 2D operations. Comprehensions also work for dictionaries: <code>{k: v for k, v in pairs}</code> and sets: <code>{x for x in items}</code>.</p>",
        1: "<p>Anonymous, tiny, 'throw-away' functions built without using the <code>def</code> keyword. Syntax: <code>lambda parameters: expression</code>. Example: <code>double = lambda x: x * 2</code> is equivalent to <code>def double(x): return x * 2</code>.</p><p>Lambdas are most useful as quick callbacks: <code>sorted(students, key=lambda s: s.grade)</code> sorts students by their grade. They're limited to single expressions - for anything complex, use a regular function.</p>",
        2: "<p>Core functional programming tools that apply logic massively over entire sequences. <code>map(func, iterable)</code> applies a function to every element: <code>list(map(str.upper, names))</code> uppercases all names.</p><p><code>filter(func, iterable)</code> keeps only elements where the function returns True: <code>list(filter(lambda x: x > 0, numbers))</code> keeps only positive numbers. Both return iterators - wrap in <code>list()</code> to see results. In modern Python, list comprehensions are often preferred over map/filter.</p>"
    },
    "python/data_structures": {
        0: "<p>A Stack works like a pile of plates: Last In, First Out (LIFO). The last item added is the first one removed. Python lists act as stacks: <code>.append()</code> pushes, <code>.pop()</code> removes the last item. Stacks are used in undo operations, expression parsing, and recursive algorithms.</p><p>A Queue works like a checkout line: First In, First Out (FIFO). Use <code>collections.deque</code> for efficient queues: <code>deque.append()</code> adds to the right, <code>deque.popleft()</code> removes from the left in O(1) time.</p>",
        1: "<p>Elements are distributed across memory; each item (node) points directly to the next one via a reference. Unlike arrays, linked lists don't need contiguous memory. Insertion and deletion at any position take O(1) if you have a reference to the node.</p><p>Trade-off: random access is slow (O(n)) because you must traverse from the head. Python doesn't have a built-in LinkedList, but you can implement one with a Node class containing <code>data</code> and <code>next</code> attributes.</p>"
    },
    "python/python_libraries": {
        0: "<p>You use <code>pip install package_name</code> in your command terminal to instantly download and install packages from PyPI (Python Package Index, with over 400,000 packages). Use <code>pip list</code> to see installed packages and <code>pip freeze > requirements.txt</code> to save your dependencies.</p><p>Virtual environments (<code>python -m venv myenv</code>) isolate project dependencies, preventing conflicts between projects that need different versions of the same package.</p>",
        1: "<p>Key external libraries: <code>Requests</code> for making HTTP/API calls, <code>Pandas</code> for Data Science and table manipulation, <code>NumPy</code> for numerical computing and matrix operations, <code>Matplotlib</code> for creating charts and graphs, <code>Flask/Django</code> for web development.</p><p>The Python ecosystem is one of the largest in programming. Whatever you need - machine learning (scikit-learn, TensorFlow), web scraping (BeautifulSoup), image processing (Pillow) - there's likely a mature library for it.</p>"
    },
    "python/python_interview": {
        0: "<p>Understanding Big-O notation is crucial for coding interviews. It measures how an algorithm's performance scales with input size. Key complexities: O(1) constant, O(log n) binary search, O(n) linear scan, O(n log n) efficient sorting, O(n^2) nested loops, O(2^n) recursive subsets.</p><p>Practice identifying complexity: a single loop is O(n), nested loops are O(n^2), halving each step is O(log n). Interviewers want you to analyze your solution's time AND space complexity.</p>",
        1: "<p>Learning how to plan out large-scale architectures is essential for senior-level interviews. Topics include: microservices vs monoliths, load balancing, caching (Redis/Memcached), database sharding, message queues (RabbitMQ/Kafka), and CDNs.</p><p>Key patterns: API Gateway, Circuit Breaker, Event-Driven architecture, CQRS. Practice designing systems like URL shorteners, chat applications, social media feeds, and file storage systems. Focus on trade-offs between consistency, availability, and partition tolerance (CAP theorem).</p>"
    },

    # ============ C# ============
    "csharp/cs_variables": {
        1: "<p><code>const</code> values must be known at compile time and cannot change: <code>const double PI = 3.14159;</code>. <code>readonly</code> values can be assigned at runtime in the constructor but cannot change afterwards: <code>readonly DateTime created = DateTime.Now;</code>.</p><p>Use <code>const</code> for truly fixed values (math constants, config keys). Use <code>readonly</code> for values determined at startup (database connections, configuration loaded from files). Both enforce immutability but at different stages.</p>",
        2: "<p>Value types (int, double, bool) can't normally be null. Add <code>?</code> to allow null: <code>int? score = null;</code>. This is essential for database fields where a value might not exist yet. Use <code>??</code> (null-coalescing) to provide defaults: <code>int actual = score ?? 0;</code>.</p><p>Use <code>?.</code> (null-conditional) for safe navigation: <code>user?.Address?.City</code> returns null instead of throwing if any part is null. This eliminates NullReferenceException - one of the most common C# bugs.</p>"
    },
    "csharp/cs_linq": {
        1: "<p>LINQ Query Syntax looks like SQL embedded in C#: <code>var result = from s in students where s.Grade > 80 orderby s.Name select s;</code>. This is compiled to the same method calls as Method Syntax but reads more naturally for complex queries.</p><p>Query syntax is especially readable for joins: <code>from o in orders join c in customers on o.CustomerId equals c.Id select new { o.Total, c.Name }</code>. Most C# developers use Method Syntax for simple operations and Query Syntax for complex queries with multiple joins.</p>"
    },
    "csharp/cs_advanced": {
        2: "<p>Enable in project settings: <code>&lt;Nullable&gt;enable&lt;/Nullable&gt;</code>. The compiler then warns when reference types might be null. Annotate nullable references with <code>?</code>: <code>string? name = null;</code> is allowed, but <code>string name = null;</code> generates a warning.</p><p>This feature dramatically reduces NullReferenceException bugs. The compiler tracks null state through your code flow - if you check <code>if (name != null)</code>, subsequent code knows name is non-null. Combined with the <code>!</code> null-forgiving operator for cases where you know better than the compiler.</p>"
    },

    # ============ C ============
    "c/c_pointers": {
        2: "<p>An array name is a constant pointer to its first element: <code>arr == &arr[0]</code>. This means you can use pointer arithmetic to traverse arrays: <code>*(arr + i)</code> is identical to <code>arr[i]</code>. The compiler uses this equivalence internally.</p><p>Functions receiving arrays actually receive pointers. This is why arrays 'decay' to pointers when passed to functions, and why <code>sizeof(arr)</code> inside a function gives the pointer size (4 or 8 bytes), not the array size. Always pass the array length as a separate parameter.</p>"
    },
    "c/c_structures": {
        1: "<p><code>typedef</code> creates aliases for complex types: <code>typedef struct { int x; int y; } Point;</code>. Now use <code>Point p1;</code> instead of <code>struct Point p1;</code>. This makes code cleaner and more readable, especially with complex nested structures.</p><p>Common convention: <code>typedef unsigned long ulong;</code> simplifies verbose type names. Function pointer typedefs are especially useful: <code>typedef int (*Comparator)(const void*, const void*);</code> makes function pointer parameters readable.</p>"
    },
    "c/c_algorithms": {
        1: "<p>Bubble Sort (O(n<sup>2</sup>)) is great for learning but impractical for large datasets. Selection Sort and Insertion Sort are also O(n<sup>2</sup>) but Insertion Sort performs well on nearly-sorted data. For production, use <code>qsort()</code> from stdlib.h which implements an optimized quicksort.</p><p>Understanding sorting internals helps with optimization: Merge Sort guarantees O(n log n) but uses O(n) extra space. Quicksort averages O(n log n) with O(1) extra space but has O(n<sup>2</sup>) worst case. Choose based on your constraints - space-limited systems favor quicksort, stability requirements favor merge sort.</p>"
    },

    # ============ PHP ============
    "php/php_basics": {
        0: "<p>PHP code is embedded in HTML using <code>&lt;?php ... ?&gt;</code> tags. Variables start with <code>$</code>: <code>$name = 'Alice';</code>. PHP is dynamically typed - variables can change type freely. Output with <code>echo</code> (no return value) or <code>print</code> (returns 1).</p><p>PHP runs on the server, generating HTML that is sent to the browser. The client never sees PHP code. This server-side execution model is what makes PHP suitable for building dynamic websites with database connectivity.</p>"
    },
    "php/php_operators": {
        1: "<p>The null coalescing operator <code>??</code> returns the left operand if it exists and is not null, otherwise the right: <code>$name = $_GET['name'] ?? 'Guest';</code>. This replaces verbose <code>isset()</code> checks. Chain them: <code>$val = $a ?? $b ?? 'default';</code>.</p><p>The null coalescing assignment <code>??=</code> (PHP 7.4+) assigns only if null: <code>$config['debug'] ??= false;</code>. The spaceship operator <code><=></code> returns -1, 0, or 1 for comparisons, perfect for custom sort functions: <code>usort($arr, fn($a, $b) => $a <=> $b);</code>.</p>"
    },
    "php/php_functions": {
        1: "<p>Arrow functions (PHP 7.4+) provide concise anonymous function syntax: <code>$double = fn($x) => $x * 2;</code>. Unlike regular anonymous functions, arrow functions <strong>automatically capture</strong> variables from the parent scope without needing the <code>use</code> keyword.</p><p>Regular closures require explicit capture: <code>$greet = function($name) use ($greeting) { return \"$greeting, $name\"; };</code>. Arrow functions simplify this: <code>$greet = fn($name) => \"$greeting, $name\";</code>. Arrow functions are limited to single expressions.</p>"
    },
    "php/php_json": {
        1: "<p>Building API responses in PHP is straightforward with <code>json_encode()</code>. Set the content type header first: <code>header('Content-Type: application/json');</code>, then echo the encoded data: <code>echo json_encode(['status' => 'success', 'data' => $results]);</code>.</p><p>For receiving JSON input (POST requests), use: <code>$input = json_decode(file_get_contents('php://input'), true);</code>. The <code>true</code> parameter returns an associative array instead of an object. Always validate and sanitize incoming JSON data before processing.</p>"
    },

    # ============ JAVA ============
    "java/java_variables": {
        2: "<p>Use the <code>final</code> keyword to create constants that cannot be reassigned: <code>final double PI = 3.14159;</code>. By convention, constant names use UPPER_SNAKE_CASE. A <code>final</code> reference variable (like <code>final List&lt;String&gt; names</code>) cannot point to a new list, but the list's contents can still be modified.</p><p>Use <code>static final</code> for class-level constants shared by all instances: <code>static final int MAX_SIZE = 100;</code>. These are compiled inline by the JVM for performance.</p>"
    },
    "java/java_control_flow": {
        2: "<p>The ternary operator <code>condition ? expr1 : expr2</code> is a concise one-line if/else expression. It's useful for simple assignments: <code>String result = score >= 50 ? \"Pass\" : \"Fail\";</code>. Unlike if/else statements, the ternary operator is an expression that produces a value.</p><p>Avoid nesting ternary operators (<code>a ? b : c ? d : e</code>) as it becomes unreadable. For complex conditions, prefer standard if/else blocks. The ternary operator is best for simple, clear binary choices.</p>"
    },
    "java/java_loops": {
        0: "<p>The classic <code>for</code> loop has three parts: <code>for (int i = 0; i < n; i++)</code>. The loop variable <code>i</code> is scoped to the loop block. You can modify the step: <code>i += 2</code> for even numbers, or count down: <code>for (int i = n; i > 0; i--)</code>.</p><p>The enhanced for-each loop (<code>for (String name : names)</code>) is cleaner for iterating collections. Use the classic for loop when you need the index, the for-each when you just need the values.</p>"
    },
    "java/java_polymorphism": {
        1: "<p>Use <code>instanceof</code> to check an object's actual type at runtime: <code>if (animal instanceof Dog)</code>. This is necessary before downcasting: <code>Dog d = (Dog) animal;</code>. Without the check, an incorrect cast throws <code>ClassCastException</code>.</p><p>Java 16+ introduced pattern matching: <code>if (animal instanceof Dog d)</code> checks AND casts in one step. This eliminates the separate cast line and is much cleaner for type-checking logic.</p>"
    },
    "java/java_interfaces": {
        1: "<p>A class can implement multiple interfaces: <code>class Dog implements Animal, Pet, Trainable</code>. This solves Java's single-inheritance limitation. Each interface adds a contract the class must fulfill, enabling a class to serve multiple roles.</p><p>If two interfaces define the same default method, the implementing class must override it to resolve the conflict. This is rare in practice but important to understand for interviews.</p>"
    },

    # ============ JAVASCRIPT ============
    "javascript/js_oop": {
        1: "<p>Use <code>extends</code> to create a child class that inherits all properties and methods from a parent. Call <code>super()</code> in the constructor to invoke the parent's constructor (must be called before using <code>this</code>). Override methods simply by redefining them in the child class.</p><p>JavaScript inheritance is prototypal under the hood. The <code>class</code> and <code>extends</code> keywords are syntactic sugar over prototype chains. Understanding prototypes helps debug inheritance issues and is a common interview topic.</p>"
    },
    "javascript/js_error": {
        2: "<p>For promises, use <code>.catch()</code> to handle rejections. For async/await, wrap awaited calls in <code>try/catch</code>. Unhandled promise rejections can silently swallow errors or crash Node.js applications.</p><p>Global handlers: In browsers, <code>window.addEventListener('unhandledrejection', handler)</code> catches missed rejections. In Node.js, <code>process.on('unhandledRejection', handler)</code>. Always add error handling to every async operation, even if it's just logging.</p>"
    },

    # ============ TYPESCRIPT ============
    "typescript/typescript_enums": {
        0: "<p>By default, enum values auto-increment from 0: <code>enum Direction { Up, Down, Left, Right }</code>. Direction.Up is 0, Direction.Down is 1, etc. You can set a custom start value: <code>enum Status { Active = 1, Inactive, Pending }</code> (Inactive becomes 2, Pending becomes 3).</p><p>Numeric enums support <strong>reverse mapping</strong>: <code>Direction[0]</code> returns <code>'Up'</code>. This is useful for debugging and logging where you want the name, not the number.</p>",
        1: "<p>String enums require explicit values for every member: <code>enum Color { Red = 'RED', Blue = 'BLUE' }</code>. They are more readable in logs, debugging, and serialized data since you see meaningful strings instead of opaque numbers.</p><p>String enums do NOT support reverse mapping. Trade-off: more verbose to define, but the output is self-documenting. Many teams prefer string enums over numeric for better debugging experience.</p>",
        2: "<p><code>const enum</code> is completely removed during compilation - the values are inlined directly into the JavaScript output. <code>const enum Dir { Up = 0 }</code> compiles <code>Dir.Up</code> to just <code>0</code> in the output, producing smaller and faster code.</p><p>Trade-off: const enums lose reverse mapping and cannot be iterated. They also don't work well with <code>--isolatedModules</code> (used by Babel/Vite). Use regular enums when you need runtime features, const enums for pure performance.</p>"
    },
    "typescript/typescript_advanced": {
        0: "<p>Intersection types merge multiple types into one: <code>type AdminUser = User & Admin;</code>. The resulting type has ALL properties from both types. If types conflict (same property, different types), the intersection becomes <code>never</code> for that property.</p><p>Intersection is the opposite of union: <code>A | B</code> means 'either A or B', while <code>A & B</code> means 'both A and B'. Use intersections for mixins, combining capabilities, and extending types without inheritance.</p>"
    },
    "typescript/typescript_modules": {
        1: "<p><code>import type { User } from './types';</code> imports ONLY the type information, not any runtime value. This is completely stripped during compilation, meaning zero bytes in the output bundle. TypeScript 3.8+ feature.</p><p>This matters for tree-shaking: regular imports keep the module in the bundle even if you only use types. Type-only imports guarantee the module isn't included. Use them for interfaces, type aliases, and any import used only in type annotations.</p>"
    },
    "typescript/typescript_decorators": {
        1: "<p>Method decorators receive three arguments: the target object (prototype or constructor), the method name (string), and the property descriptor. They can wrap the original method to add logging, caching, authorization, or timing.</p><p>Common patterns: <code>@log</code> (log method calls), <code>@memoize</code> (cache results), <code>@debounce(300)</code> (rate-limit calls), <code>@authorize('admin')</code> (check permissions). Decorator factories (functions returning decorators) enable parameterized decorators.</p>",
        2: "<p>Property decorators observe that a property has been declared on a class. They receive the target and the property name. Combined with the <code>reflect-metadata</code> library, they can store metadata about properties for later retrieval.</p><p>This is the foundation of dependency injection frameworks like Angular's <code>@Inject()</code> and ORMs like TypeORM's <code>@Column()</code>. The decorator registers metadata that the framework reads at runtime to configure behavior automatically.</p>"
    },
    "typescript/typescript_react": {
        2: "<p>Type event handlers explicitly: <code>const handleChange = (e: React.ChangeEvent&lt;HTMLInputElement&gt;) =&gt; { setValue(e.target.value); }</code>. React provides its own synthetic event types that wrap native DOM events for cross-browser consistency.</p><p>Common event types: <code>React.MouseEvent</code> (clicks), <code>React.KeyboardEvent</code> (key presses), <code>React.FormEvent</code> (form submission), <code>React.DragEvent</code> (drag and drop). Each is generic over the element type for precise <code>event.target</code> typing.</p>"
    },
    "typescript/typescript_typeguards": {
        0: "<p><code>typeof x === 'string'</code> narrows the type to string within the if-block. <code>x instanceof Date</code> narrows to the Date class. TypeScript recognizes these patterns and automatically adjusts the type in the narrowed scope.</p><p>typeof works for primitives: <code>'string'</code>, <code>'number'</code>, <code>'boolean'</code>, <code>'undefined'</code>, <code>'object'</code>, <code>'function'</code>. instanceof works for class hierarchies. For interfaces (which don't exist at runtime), use custom type guards with the <code>is</code> keyword.</p>"
    },
    "typescript/typescript_practices": {
        1: "<p>Don't over-annotate: <code>const name = 'Alice';</code> is already typed as string - adding <code>: string</code> is redundant. TypeScript's type inference is powerful. Only annotate when: the type can't be inferred, for function parameters, for function return types (documentation), or when the inferred type is too wide.</p><p>Let the compiler work for you. Over-annotation adds visual noise and maintenance burden. If you change a type, you'd have to update annotations everywhere. Trust inference for variables, annotate at boundaries (function signatures, API responses).</p>"
    },
    "typescript/typescript_interview": {
        2: "<p>Demonstrate knowledge of real-world patterns: <strong>Discriminated unions</strong> for state machines (loading/success/error). <strong>Generic hooks</strong> in React for type-safe <code>useFetch&lt;T&gt;()</code>. <strong>Branded types</strong> for preventing mixing up UserId and PostId. <strong>Result types</strong> (<code>{ ok: true, data: T } | { ok: false, error: E }</code>) for explicit error handling.</p><p>Show awareness of TypeScript's limitations: type erasure at runtime, structural vs nominal typing, and the trade-offs of strict mode. Being able to discuss why certain patterns exist and when NOT to use them shows senior-level understanding.</p>"
    },

    # ============ FLUTTER ============
    "flutter/flutter_widgets": {
        1: "<p>StatelessWidget has a single <code>build()</code> method that returns a widget tree. Once created, it never changes - the framework calls build() once with the given parameters. Use for static UI like labels, icons, fixed layouts, and presentation-only components.</p><p>StatelessWidgets are more performant than StatefulWidgets because the framework doesn't need to track state changes. Always prefer StatelessWidget unless you need mutable state. You can still pass data to them via constructor parameters.</p>",
        2: "<p>Flutter's power comes from composing simple widgets into complex UIs. A custom widget is just a class that assembles other widgets in its <code>build()</code> method. This makes code reusable and testable - build a <code>UserCard</code> widget once, use it everywhere.</p><p>Composition over inheritance: instead of subclassing existing widgets, wrap them inside your custom widget. For example, don't extend ElevatedButton - wrap it in a custom widget that configures its style. This follows Flutter's philosophy and keeps your code flexible.</p>"
    },
    "flutter/flutter_provider": {
        0: "<p>Create a model class extending <code>ChangeNotifier</code>. Store your business data as fields and expose them via getters. When data changes, call <code>notifyListeners()</code> to trigger rebuilds in all listening widgets. This is your business logic layer, separate from UI.</p><p>Keep your ChangeNotifier classes focused - one per feature area. A <code>CartNotifier</code> manages cart items, a <code>ThemeNotifier</code> manages theme settings. Don't create a single massive notifier for everything. Use <code>MultiProvider</code> to provide multiple notifiers simultaneously.</p>"
    },
    "flutter/flutter_http": {
        2: "<p>Wrap network calls in <code>try/catch</code> for connection errors (no internet, timeout, DNS failure). Check <code>response.statusCode</code> for HTTP errors (404 Not Found, 500 Server Error). Use <code>.timeout(Duration(seconds: 10))</code> to prevent requests from hanging indefinitely.</p><p>Best practice: create a centralized API service class that handles all networking, including error transformation. Convert HTTP errors into user-friendly messages. Implement retry logic for transient failures. Show appropriate UI states: loading spinner, error message with retry button, or success data.</p>"
    },
    "flutter/flutter_json": {
        2: "<p>For nested JSON (objects within objects), each nested object needs its own model class with fromJson/toJson. In the parent's fromJson, call the child's factory: <code>address: Address.fromJson(json['address'])</code>. For arrays of objects: <code>(json['items'] as List).map((e) => Item.fromJson(e)).toList()</code>.</p><p>Handle nullable fields carefully: check if the JSON key exists before accessing. Use <code>json['field'] as String?</code> for nullable fields. For complex nested structures with many models, code generation with <code>json_serializable</code> saves significant time and prevents bugs.</p>"
    },
    "flutter/flutter_sharedpref": {
        2: "<p>Delete a specific key: <code>await prefs.remove('key')</code>. Clear all stored data: <code>await prefs.clear()</code>. Always check for null when reading since keys may not exist yet: <code>bool isDark = prefs.getBool('darkMode') ?? false;</code>.</p><p>SharedPreferences is for simple settings only. It stores data in plain text (not encrypted). For sensitive data like tokens, use <code>flutter_secure_storage</code>. For complex relational data, use <code>sqflite</code> (SQLite). For structured object storage, consider <code>hive</code> (fast NoSQL).</p>"
    },
    "flutter/flutter_responsive": {
        1: "<p><code>LayoutBuilder</code> provides the parent widget's constraints (maxWidth, maxHeight) rather than the screen size. It rebuilds whenever these constraints change, making it ideal for responsive components that adapt to their container, not the screen.</p><p>Use LayoutBuilder to switch between layouts at breakpoints: <code>builder: (ctx, constraints) { if (constraints.maxWidth > 600) return WideLayout(); else return NarrowLayout(); }</code>. Unlike MediaQuery (which gives screen size), LayoutBuilder works correctly for widgets inside sidebars, dialogs, or split views.</p>"
    },
    "flutter/flutter_platform": {
        2: "<p>For web vs mobile differences, use conditional imports: <code>import 'stub.dart' if (dart.library.html) 'web.dart';</code>. This lets you provide different implementations for each platform while keeping a unified interface. The compiler selects the correct file at build time.</p><p>For simple platform branching, use <code>kIsWeb</code> (available everywhere) or <code>Platform.isAndroid</code> / <code>Platform.isIOS</code> (not available on web). Organize platform-specific code into separate files/classes to keep your main logic clean and testable.</p>"
    },
    "flutter/flutter_deploy": {
        1: "<p>iOS deployment requires a Mac with Xcode installed, and an Apple Developer account ($99/year). Configure code signing in Xcode (Signing & Capabilities tab). Run <code>flutter build ios --release</code> to create the release build, then archive and upload via Xcode or the Transporter app.</p><p>Key steps: set the Bundle Identifier, configure App Icons, create an App Store Connect listing, set privacy descriptions for camera/location/etc. TestFlight lets you distribute beta builds to testers before the App Store review. The review process typically takes 1-3 days.</p>"
    }
}

# Apply all expansions
applied = 0
for key, subs in expansions.items():
    lang, topic_id = key.split('/')
    if lang not in d or topic_id not in d[lang]['content']:
        print(f"WARNING: {key} not found!")
        continue
    content = d[lang]['content'][topic_id]
    if not content.get('structured') or not content['structured'].get('subtopics'):
        print(f"WARNING: {key} has no structured subtopics!")
        continue
    
    if isinstance(subs, dict):
        for idx, new_content in subs.items():
            if idx < len(content['structured']['subtopics']):
                old_title = content['structured']['subtopics'][idx]['title']
                content['structured']['subtopics'][idx]['content'] = new_content
                applied += 1
    else:
        print(f"WARNING: {key} has invalid format")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print(f"Done! Expanded {applied} short subtopics across all languages.")
