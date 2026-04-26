import json

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

def ex(title, code, output, explanation):
    return {"title": title, "code": code, "output": output, "explanation": explanation}

JAVA = {
"java_basics": {
    "introduction": "<p><strong>Java</strong> is one of the world's most widely used programming languages. Created by James Gosling at Sun Microsystems in 1995, Java follows the principle of <strong>'Write Once, Run Anywhere' (WORA)</strong> - compile your code once and it runs on any platform with a Java Virtual Machine (JVM).</p><p>Java is <strong>statically typed</strong>, <strong>object-oriented</strong>, and <strong>compiled</strong>. Unlike Python, Java requires you to declare variable types explicitly, and every piece of code must live inside a class. This strictness catches errors at compile time rather than runtime.</p>",
    "subtopics": [
        {"title": "1. How Java Works (JVM)", "content": "<p>When you write Java code (.java file), the compiler (<code>javac</code>) converts it to <strong>bytecode</strong> (.class file). The JVM then interprets this bytecode for your specific operating system. This two-step process is why Java is platform-independent.</p><p>The JVM also handles <strong>garbage collection</strong> automatically, freeing memory that is no longer in use - unlike C/C++ where you must manage memory manually.</p>"},
        {"title": "2. The main() Method", "content": "<p>Every Java program starts executing from the <code>public static void main(String[] args)</code> method. Let's break it down:</p><ul><li><code>public</code> - accessible from anywhere</li><li><code>static</code> - can be called without creating an object</li><li><code>void</code> - returns nothing</li><li><code>String[] args</code> - accepts command-line arguments</li></ul>"},
        {"title": "3. Compilation & Execution", "content": "<p>To run a Java program: first compile with <code>javac MyProgram.java</code>, then execute with <code>java MyProgram</code>. The file name must match the public class name exactly. Java is case-sensitive - <code>MyProgram</code> and <code>myprogram</code> are different!</p>"}
    ],
    "key_concepts": "<ul><li><strong>JVM:</strong> Java Virtual Machine executes bytecode on any platform</li><li><strong>Static Typing:</strong> Every variable must declare its type before use</li><li><strong>Object-Oriented:</strong> Everything must be inside a class</li><li><strong>Garbage Collection:</strong> JVM automatically manages memory allocation and deallocation</li></ul>",
    "examples": [
        ex("Hello World", 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n        System.out.println("Welcome to Java!");\n    }\n}', "Hello, World!\nWelcome to Java!", "System.out.println() prints a line to the console. Every statement ends with a semicolon. The class name must match the filename."),
        ex("Basic Input", 'import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        System.out.print("Enter name: ");\n        String name = sc.nextLine();\n        System.out.println("Hello, " + name);\n    }\n}', "Enter name: Alice\nHello, Alice", "Scanner reads user input from the console. nextLine() reads a full line, nextInt() reads an integer.")
    ]
},

"java_variables": {
    "introduction": "<p><strong>Variables</strong> in Java are strictly typed containers for data. Unlike JavaScript or Python, you must declare what type of data a variable will hold before using it. This is called <strong>static typing</strong> and is one of Java's core safety features.</p><p>Java has two categories of data types: <strong>primitive types</strong> (int, double, boolean, char, etc.) that hold actual values, and <strong>reference types</strong> (String, Arrays, Objects) that hold memory addresses pointing to data on the heap.</p>",
    "subtopics": [
        {"title": "1. Primitive Data Types", "content": "<p>Java has 8 primitive types:</p><ul><li><code>byte</code> (8-bit), <code>short</code> (16-bit), <code>int</code> (32-bit), <code>long</code> (64-bit) - integer types</li><li><code>float</code> (32-bit), <code>double</code> (64-bit) - decimal types</li><li><code>char</code> - single character (16-bit Unicode)</li><li><code>boolean</code> - true or false</li></ul><p><code>int</code> and <code>double</code> are the most commonly used numeric types.</p>"},
        {"title": "2. Type Casting", "content": "<p><strong>Widening</strong> (automatic): smaller to larger type (int to double). <strong>Narrowing</strong> (manual): larger to smaller type requires explicit casting: <code>int x = (int) 3.14;</code>. Narrowing can lose data!</p>"},
        {"title": "3. Constants (final)", "content": "<p>Use the <code>final</code> keyword to create constants that cannot be reassigned: <code>final double PI = 3.14159;</code>. By convention, constants use UPPER_SNAKE_CASE.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Static Typing:</strong> Variable types are declared at compile time</li><li><strong>Primitives vs References:</strong> Primitives hold values; references hold memory addresses</li><li><strong>Type Casting:</strong> Converting between types (widening is automatic, narrowing is manual)</li><li><strong>final:</strong> Creates immutable variables (constants)</li></ul>",
    "examples": [
        ex("Variable Types", 'int age = 25;\ndouble salary = 50000.50;\nchar grade = \'A\';\nboolean isActive = true;\nString name = "Alice";\n\nSystem.out.println(name + " is " + age + " years old");\nSystem.out.println("Salary: $" + salary);', "Alice is 25 years old\nSalary: $50000.5", "Each variable is declared with its type. String is a reference type (capital S), while int, double, char, boolean are primitives."),
        ex("Type Casting", 'double pi = 3.14159;\nint rounded = (int) pi;  // Narrowing (loses decimal)\n\nint x = 100;\ndouble y = x;  // Widening (automatic)\n\nSystem.out.println(rounded);\nSystem.out.println(y);', "3\n100.0", "Narrowing (double to int) requires explicit cast and drops the decimal. Widening (int to double) happens automatically.")
    ]
},

"java_operators": {
    "introduction": "<p><strong>Operators</strong> in Java perform operations on variables and values. Java supports arithmetic, comparison, logical, bitwise, and assignment operators - similar to C/C++ syntax.</p><p>Understanding operator precedence is critical - multiplication happens before addition unless you use parentheses. Java also supports shorthand operators like <code>+=</code>, <code>-=</code>, <code>*=</code> for concise code.</p>",
    "subtopics": [
        {"title": "1. Arithmetic Operators", "content": "<p>Standard operators: <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>, <code>%</code> (modulus). Note: dividing two integers gives an integer result! <code>5 / 2</code> gives <code>2</code>, not <code>2.5</code>. To get a decimal result, at least one operand must be a double.</p>"},
        {"title": "2. Comparison & Logical", "content": "<p>Comparison operators (<code>==</code>, <code>!=</code>, <code>></code>, <code><</code>, <code>>=</code>, <code><=</code>) return boolean values. For objects like Strings, use <code>.equals()</code> instead of <code>==</code> (which compares memory addresses, not content).</p><p>Logical operators: <code>&&</code> (AND), <code>||</code> (OR), <code>!</code> (NOT). They use short-circuit evaluation.</p>"},
        {"title": "3. Increment/Decrement", "content": "<p>Pre-increment (<code>++x</code>): increments then returns. Post-increment (<code>x++</code>): returns then increments. This distinction matters when used in expressions: <code>int y = x++;</code> assigns the old value to y.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Integer Division:</strong> 5/2 = 2 in Java (use 5.0/2 for 2.5)</li><li><strong>.equals() for Strings:</strong> Never use == to compare String content</li><li><strong>Short-circuit:</strong> && stops if first is false, || stops if first is true</li><li><strong>Ternary:</strong> condition ? valueIfTrue : valueIfFalse</li></ul>",
    "examples": [
        ex("Arithmetic", 'int a = 17, b = 5;\nSystem.out.println("Division: " + a / b);\nSystem.out.println("Modulus: " + a % b);\nSystem.out.println("Decimal: " + (double) a / b);', "Division: 3\nModulus: 2\nDecimal: 3.4", "Integer division truncates. Modulus gives remainder. Casting one operand to double gives decimal result."),
        ex("String Comparison", 'String s1 = new String("Hello");\nString s2 = new String("Hello");\n\nSystem.out.println(s1 == s2);      // false!\nSystem.out.println(s1.equals(s2)); // true', "false\ntrue", "== compares memory addresses (different objects). .equals() compares actual string content. Always use .equals() for Strings!")
    ]
},

"java_control_flow": {
    "introduction": "<p><strong>Control flow</strong> statements in Java determine which code blocks execute based on conditions. Java uses <code>if/else if/else</code> for branching and <code>switch</code> for multi-way selection.</p><p>Java 14+ introduced <strong>switch expressions</strong> with arrow syntax, making switch statements more concise and less error-prone (no fall-through by default).</p>",
    "subtopics": [
        {"title": "1. if/else Statements", "content": "<p>The <code>if</code> statement evaluates a boolean condition. Java requires the condition to be strictly boolean - <code>if (1)</code> is a compile error unlike JavaScript/Python. Use <code>else if</code> for multiple branches and <code>else</code> for the default case.</p>"},
        {"title": "2. switch Statement", "content": "<p>Switch in Java works with <code>byte</code>, <code>short</code>, <code>int</code>, <code>char</code>, <code>String</code>, and enums. Each case needs a <code>break</code> to prevent fall-through (or use arrow syntax in Java 14+).</p>"},
        {"title": "3. Ternary Operator", "content": "<p>The ternary operator <code>condition ? expr1 : expr2</code> is a concise one-line if/else. It's useful for simple assignments: <code>String result = score >= 50 ? \"Pass\" : \"Fail\";</code></p>"}
    ],
    "key_concepts": "<ul><li><strong>Boolean conditions only:</strong> Unlike JS, Java requires true/false in if statements</li><li><strong>Switch fall-through:</strong> Always include break unless intentional</li><li><strong>Arrow switch (14+):</strong> No fall-through, can return values</li><li><strong>Ternary:</strong> Compact inline conditional expression</li></ul>",
    "examples": [
        ex("if/else", 'int score = 85;\n\nif (score >= 90) {\n    System.out.println("Grade: A");\n} else if (score >= 80) {\n    System.out.println("Grade: B");\n} else if (score >= 70) {\n    System.out.println("Grade: C");\n} else {\n    System.out.println("Grade: F");\n}', "Grade: B", "Conditions are checked top-to-bottom. Once a condition is true, its block runs and remaining else-if blocks are skipped."),
        ex("switch Statement", 'String day = "Monday";\n\nswitch (day) {\n    case "Monday":\n    case "Tuesday":\n        System.out.println("Start of week");\n        break;\n    case "Friday":\n        System.out.println("TGIF!");\n        break;\n    default:\n        System.out.println("Midweek");\n}', "Start of week", "Multiple cases can share the same block. Without break, execution falls through to the next case.")
    ]
},

"java_loops": {
    "introduction": "<p><strong>Loops</strong> in Java repeat a block of code while a condition is true. Java provides <code>for</code>, <code>while</code>, <code>do-while</code>, and the enhanced <code>for-each</code> loop. Choosing the right loop type makes your code cleaner and more efficient.</p><p>The enhanced for-each loop (<code>for (Type item : collection)</code>) is the preferred way to iterate over arrays and collections in modern Java.</p>",
    "subtopics": [
        {"title": "1. for Loop", "content": "<p>The classic <code>for</code> loop: <code>for (int i = 0; i < n; i++)</code>. Perfect when you know the exact number of iterations. The loop variable is scoped to the loop block.</p>"},
        {"title": "2. while and do-while", "content": "<p><code>while</code> checks the condition before each iteration. <code>do-while</code> checks after, guaranteeing at least one execution. Use while for input validation loops where you don't know how many attempts the user needs.</p>"},
        {"title": "3. Enhanced for-each", "content": "<p>The for-each loop simplifies iterating over arrays and collections: <code>for (String s : names)</code>. It's cleaner and less error-prone than index-based loops, but you can't modify the array or access the index directly.</p>"}
    ],
    "key_concepts": "<ul><li><strong>for-each:</strong> Cleanest way to iterate arrays/collections</li><li><strong>break:</strong> Exits the loop immediately</li><li><strong>continue:</strong> Skips to the next iteration</li><li><strong>Labeled break:</strong> Exits nested loops with a label</li></ul>",
    "examples": [
        ex("for and for-each", 'int[] numbers = {10, 20, 30, 40, 50};\n\n// Classic for loop\nfor (int i = 0; i < numbers.length; i++) {\n    System.out.print(numbers[i] + " ");\n}\nSystem.out.println();\n\n// Enhanced for-each\nfor (int num : numbers) {\n    System.out.print(num + " ");\n}', "10 20 30 40 50\n10 20 30 40 50", "Both produce the same output. The for-each loop is cleaner when you don't need the index variable."),
        ex("while Loop", 'int count = 1;\nwhile (count <= 5) {\n    System.out.println("Count: " + count);\n    count++;\n}', "Count: 1\nCount: 2\nCount: 3\nCount: 4\nCount: 5", "The while loop checks the condition before each iteration. Don't forget to update the counter to avoid infinite loops!")
    ]
},

"java_arrays": {
    "introduction": "<p><strong>Arrays</strong> in Java are fixed-size, ordered collections of elements of the same type. Unlike JavaScript arrays, Java arrays cannot grow or shrink after creation, and they can only hold one data type.</p><p>For dynamic collections, Java provides <code>ArrayList</code> from the Collections framework. Understanding both arrays and ArrayList is essential for Java development.</p>",
    "subtopics": [
        {"title": "1. Declaring & Initializing", "content": "<p>Two ways to create arrays: <code>int[] nums = new int[5];</code> (empty, default values) or <code>int[] nums = {1, 2, 3, 4, 5};</code> (with values). Default values: 0 for numbers, false for booleans, null for objects.</p>"},
        {"title": "2. Multi-Dimensional Arrays", "content": "<p>Java supports 2D arrays (matrices): <code>int[][] matrix = new int[3][4];</code>. Access elements with two indices: <code>matrix[row][col]</code>. 2D arrays are arrays of arrays, so rows can have different lengths (jagged arrays).</p>"},
        {"title": "3. ArrayList", "content": "<p><code>ArrayList&lt;Type&gt;</code> is a resizable array. Key methods: <code>.add()</code>, <code>.get()</code>, <code>.set()</code>, <code>.remove()</code>, <code>.size()</code>. ArrayLists can only hold objects - use Integer instead of int (autoboxing handles conversion).</p>"}
    ],
    "key_concepts": "<ul><li><strong>Fixed Size:</strong> Array length is set at creation and cannot change</li><li><strong>Zero-indexed:</strong> First element is at index 0</li><li><strong>ArrayList:</strong> Dynamic, resizable alternative to arrays</li><li><strong>Arrays.sort():</strong> Built-in sorting utility for arrays</li></ul>",
    "examples": [
        ex("Array Operations", 'int[] nums = {5, 2, 8, 1, 9};\nSystem.out.println("Length: " + nums.length);\nSystem.out.println("First: " + nums[0]);\n\njava.util.Arrays.sort(nums);\nfor (int n : nums) {\n    System.out.print(n + " ");\n}', "Length: 5\nFirst: 5\n1 2 5 8 9", "Arrays.sort() sorts in-place. Access length with .length (no parentheses, it's a field not a method)."),
        ex("ArrayList", 'import java.util.ArrayList;\n\nArrayList<String> names = new ArrayList<>();\nnames.add("Alice");\nnames.add("Bob");\nnames.add("Charlie");\n\nnames.remove("Bob");\nSystem.out.println(names);\nSystem.out.println("Size: " + names.size());', "[Alice, Charlie]\nSize: 2", "ArrayList grows dynamically. Use generics <String> to specify the type. .remove() can take an index or an object.")
    ]
},

"java_strings": {
    "introduction": "<p><strong>Strings</strong> in Java are objects of the <code>String</code> class, not primitives. The most important thing to know: <strong>Strings are immutable</strong>. Every operation that appears to modify a String actually creates a new one in memory.</p><p>For frequent modifications, use <code>StringBuilder</code> (not thread-safe, faster) or <code>StringBuffer</code> (thread-safe, slower) instead.</p>",
    "subtopics": [
        {"title": "1. String Methods", "content": "<p>Common methods: <code>.length()</code>, <code>.charAt()</code>, <code>.substring()</code>, <code>.toUpperCase()</code>, <code>.toLowerCase()</code>, <code>.trim()</code>, <code>.contains()</code>, <code>.indexOf()</code>, <code>.replace()</code>, <code>.split()</code>.</p><p>Remember: these methods return new strings - the original is unchanged!</p>"},
        {"title": "2. String Comparison", "content": "<p>NEVER use <code>==</code> to compare String content. Use <code>.equals()</code> for exact comparison or <code>.equalsIgnoreCase()</code> for case-insensitive. <code>==</code> checks if two variables point to the same object in memory, not the same text.</p>"},
        {"title": "3. StringBuilder", "content": "<p><code>StringBuilder</code> creates a mutable sequence of characters. Use <code>.append()</code> to add text, <code>.insert()</code> to place at position, <code>.reverse()</code> to flip. Convert to String with <code>.toString()</code>. Essential for building strings in loops.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Immutable:</strong> String methods create new objects, never modify the original</li><li><strong>.equals():</strong> Always use this for String comparison, never ==</li><li><strong>String Pool:</strong> Java caches string literals for memory efficiency</li><li><strong>StringBuilder:</strong> Use for building strings in loops (much faster than concatenation)</li></ul>",
    "examples": [
        ex("String Methods", 'String text = "Hello, Java World!";\nSystem.out.println(text.length());\nSystem.out.println(text.toUpperCase());\nSystem.out.println(text.substring(7, 11));\nSystem.out.println(text.contains("Java"));', "18\nHELLO, JAVA WORLD!\nJava\ntrue", "Each method returns a new string. The original text remains unchanged. substring(7,11) extracts characters from index 7 to 10."),
        ex("StringBuilder", 'StringBuilder sb = new StringBuilder();\nfor (int i = 1; i <= 5; i++) {\n    sb.append("Item ").append(i).append("\\n");\n}\nSystem.out.println(sb.toString());', "Item 1\nItem 2\nItem 3\nItem 4\nItem 5", "StringBuilder is far more efficient than string concatenation in loops. Each append() modifies the same buffer in memory.")
    ]
},

"java_methods": {
    "introduction": "<p><strong>Methods</strong> in Java are blocks of code that perform a specific task. They are defined inside a class and are the Java equivalent of functions in other languages. Methods promote code reuse and modular design.</p><p>Every method has a return type, a name, and optional parameters. If a method doesn't return a value, its return type is <code>void</code>.</p>",
    "subtopics": [
        {"title": "1. Method Syntax", "content": "<p>A method declaration: <code>access-modifier return-type name(parameters) { body }</code>. Example: <code>public static int add(int a, int b) { return a + b; }</code>. The <code>static</code> keyword means you can call it without creating an object.</p>"},
        {"title": "2. Method Overloading", "content": "<p>Java allows multiple methods with the same name but different parameter lists. The compiler picks the right one based on arguments. This is called <strong>compile-time polymorphism</strong>: <code>add(int, int)</code> vs <code>add(double, double)</code> vs <code>add(int, int, int)</code>.</p>"},
        {"title": "3. Pass-by-Value", "content": "<p>Java is strictly <strong>pass-by-value</strong>. For primitives, a copy of the value is passed. For objects, a copy of the reference is passed - you can modify the object's contents but can't reassign the reference itself.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Return Type:</strong> Must be declared, use void if no return value</li><li><strong>Overloading:</strong> Same name, different parameters</li><li><strong>Pass-by-Value:</strong> Primitives pass copies; objects pass reference copies</li><li><strong>Varargs:</strong> Variable-length arguments with <code>int... nums</code></li></ul>",
    "examples": [
        ex("Method Overloading", 'public class Main {\n    static int add(int a, int b) {\n        return a + b;\n    }\n    static double add(double a, double b) {\n        return a + b;\n    }\n    public static void main(String[] args) {\n        System.out.println(add(3, 4));\n        System.out.println(add(3.5, 4.5));\n    }\n}', "7\n8.0", "Two add() methods with different parameter types. Java automatically calls the right one based on argument types.")
    ]
},

"java_oop_basics": {
    "introduction": "<p><strong>Object-Oriented Programming (OOP)</strong> is the foundation of Java. Everything in Java revolves around objects and classes. A <strong>class</strong> is a blueprint that defines properties (fields) and behaviors (methods), while an <strong>object</strong> is an instance of that blueprint.</p><p>The four pillars of OOP are: <strong>Encapsulation</strong>, <strong>Inheritance</strong>, <strong>Polymorphism</strong>, and <strong>Abstraction</strong>. Mastering these concepts is essential for Java development.</p>",
    "subtopics": [
        {"title": "1. Classes and Objects", "content": "<p>A class defines the structure: <code>class Car { String brand; int speed; void accelerate() { speed += 10; } }</code>. Create objects with <code>new</code>: <code>Car myCar = new Car();</code>. Each object has its own copy of instance variables.</p>"},
        {"title": "2. Constructors", "content": "<p>A constructor initializes an object when it's created. It has the same name as the class and no return type. Java provides a default no-arg constructor if you don't write one. Use <code>this</code> to refer to the current object's fields.</p>"},
        {"title": "3. Encapsulation", "content": "<p>Encapsulation protects data by making fields <code>private</code> and providing <code>public</code> getter/setter methods. This gives you control over how data is accessed and modified, enabling validation and computed properties.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Class:</strong> Blueprint/template for creating objects</li><li><strong>Object:</strong> Instance of a class with its own state</li><li><strong>Constructor:</strong> Special method called during object creation</li><li><strong>Encapsulation:</strong> Hide fields with private, expose via getters/setters</li></ul>",
    "examples": [
        ex("Class and Object", 'class Student {\n    String name;\n    int age;\n\n    Student(String name, int age) {\n        this.name = name;\n        this.age = age;\n    }\n\n    void display() {\n        System.out.println(name + " - Age: " + age);\n    }\n}\n\nStudent s = new Student("Alice", 20);\ns.display();', "Alice - Age: 20", "The constructor takes parameters and assigns them to fields using 'this'. The display() method accesses instance variables directly."),
        ex("Encapsulation", 'class BankAccount {\n    private double balance = 0;\n\n    public void deposit(double amount) {\n        if (amount > 0) balance += amount;\n    }\n    public double getBalance() {\n        return balance;\n    }\n}\n\nBankAccount acc = new BankAccount();\nacc.deposit(1000);\nSystem.out.println(acc.getBalance());', "1000.0", "balance is private - it can't be accessed directly. The deposit method validates input before modifying the balance.")
    ]
},

"java_inheritance": {
    "introduction": "<p><strong>Inheritance</strong> allows a class to inherit fields and methods from another class. The child class (subclass) gets all non-private members of the parent class (superclass) and can add its own or override existing ones.</p><p>Use the <code>extends</code> keyword: <code>class Dog extends Animal</code>. Java supports single inheritance (one parent), but a class can implement multiple interfaces.</p>",
    "subtopics": [
        {"title": "1. extends & super", "content": "<p>The <code>extends</code> keyword creates a parent-child relationship. Use <code>super()</code> to call the parent's constructor, and <code>super.method()</code> to call the parent's version of an overridden method.</p>"},
        {"title": "2. Method Overriding", "content": "<p>A subclass can provide its own implementation of a parent method using the <code>@Override</code> annotation. The overriding method must have the same signature (name, parameters, return type) as the parent method.</p>"},
        {"title": "3. The Object Class", "content": "<p>Every class in Java implicitly extends <code>Object</code>, the root of the class hierarchy. It provides methods like <code>toString()</code>, <code>equals()</code>, and <code>hashCode()</code> that you can override for custom behavior.</p>"}
    ],
    "key_concepts": "<ul><li><strong>extends:</strong> Creates an inheritance relationship</li><li><strong>super():</strong> Calls the parent constructor (must be first statement)</li><li><strong>@Override:</strong> Annotation marking an overridden method</li><li><strong>Single Inheritance:</strong> Java classes can only extend one parent</li></ul>",
    "examples": [
        ex("Inheritance", 'class Animal {\n    String name;\n    Animal(String name) { this.name = name; }\n    void speak() { System.out.println(name + " makes a sound"); }\n}\n\nclass Dog extends Animal {\n    Dog(String name) { super(name); }\n    @Override\n    void speak() { System.out.println(name + " barks!"); }\n}\n\nAnimal a = new Dog("Rex");\na.speak();', "Rex barks!", "Dog inherits name field from Animal. The speak() method is overridden. Polymorphism allows an Animal reference to hold a Dog object.")
    ]
},

"java_polymorphism": {
    "introduction": "<p><strong>Polymorphism</strong> means 'many forms'. In Java, the same method name can behave differently depending on the object type. There are two types: <strong>compile-time</strong> (method overloading) and <strong>runtime</strong> (method overriding).</p><p>Runtime polymorphism is the most powerful - a parent reference can point to any child object, and the correct overridden method is called at runtime. This is the foundation of flexible, extensible code.</p>",
    "subtopics": [
        {"title": "1. Runtime Polymorphism", "content": "<p>When a parent reference holds a child object (<code>Animal a = new Dog()</code>), and both classes have the same method, Java calls the child's version at runtime. This is also called <strong>dynamic method dispatch</strong>.</p>"},
        {"title": "2. instanceof Operator", "content": "<p>Use <code>instanceof</code> to check an object's actual type at runtime: <code>if (animal instanceof Dog)</code>. This is useful before downcasting a parent reference to a child type.</p>"},
        {"title": "3. Abstract Classes", "content": "<p>An <code>abstract</code> class cannot be instantiated. It can have abstract methods (no body) that subclasses must implement. This enforces a contract while allowing shared code in non-abstract methods.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Overloading:</strong> Same method name, different parameters (compile-time)</li><li><strong>Overriding:</strong> Same signature in parent/child (runtime)</li><li><strong>Dynamic Dispatch:</strong> JVM decides which method to call at runtime</li><li><strong>Abstract:</strong> Classes that can't be instantiated, used as templates</li></ul>",
    "examples": [
        ex("Polymorphism in Action", 'abstract class Shape {\n    abstract double area();\n}\nclass Circle extends Shape {\n    double r;\n    Circle(double r) { this.r = r; }\n    double area() { return Math.PI * r * r; }\n}\nclass Rectangle extends Shape {\n    double w, h;\n    Rectangle(double w, double h) { this.w = w; this.h = h; }\n    double area() { return w * h; }\n}\n\nShape[] shapes = { new Circle(5), new Rectangle(4, 6) };\nfor (Shape s : shapes) {\n    System.out.printf("Area: %.2f%n", s.area());\n}', "Area: 78.54\nArea: 24.00", "The same area() call produces different results based on the actual object type. This is runtime polymorphism in action.")
    ]
},

"java_interfaces": {
    "introduction": "<p><strong>Interfaces</strong> in Java define a contract of methods that implementing classes must fulfill. They are like 100% abstract classes - they specify what a class must do, not how it does it.</p><p>Java 8+ interfaces can also include <code>default</code> methods (with bodies) and <code>static</code> methods. A class can implement multiple interfaces, enabling a form of multiple inheritance.</p>",
    "subtopics": [
        {"title": "1. Defining & Implementing", "content": "<p>Define with <code>interface Drawable { void draw(); }</code>. Implement with <code>class Circle implements Drawable { public void draw() { ... } }</code>. All interface methods are implicitly <code>public abstract</code>.</p>"},
        {"title": "2. Multiple Interfaces", "content": "<p>A class can implement multiple interfaces: <code>class Dog implements Animal, Pet</code>. This solves Java's single-inheritance limitation, allowing a class to fulfill multiple contracts.</p>"},
        {"title": "3. Functional Interfaces & Lambdas", "content": "<p>An interface with exactly one abstract method is a <strong>functional interface</strong>. It can be implemented using a lambda expression: <code>Runnable r = () -> System.out.println(\"Running\");</code></p>"}
    ],
    "key_concepts": "<ul><li><strong>Contract:</strong> Interfaces define what, not how</li><li><strong>Multiple Implementation:</strong> A class can implement many interfaces</li><li><strong>Default Methods:</strong> Interfaces can have method bodies since Java 8</li><li><strong>Functional Interface:</strong> Single abstract method, works with lambdas</li></ul>",
    "examples": [
        ex("Interface Example", 'interface Greetable {\n    void greet();\n    default void wave() {\n        System.out.println("*waves*");\n    }\n}\n\nclass Person implements Greetable {\n    String name;\n    Person(String name) { this.name = name; }\n    public void greet() {\n        System.out.println("Hi, I am " + name);\n    }\n}\n\nPerson p = new Person("Alice");\np.greet();\np.wave();', "Hi, I am Alice\n*waves*", "Person must implement greet(), but inherits the default wave() method. Default methods add behavior without breaking existing implementations.")
    ]
},

"java_exceptions": {
    "introduction": "<p><strong>Exception handling</strong> in Java uses <code>try-catch-finally</code> to gracefully handle runtime errors. Without it, a single error crashes the entire program. Java distinguishes between <strong>checked exceptions</strong> (must be handled) and <strong>unchecked exceptions</strong> (optional).</p><p>Checked exceptions (IOException, SQLException) are enforced by the compiler. Unchecked exceptions (NullPointerException, ArrayIndexOutOfBoundsException) extend RuntimeException.</p>",
    "subtopics": [
        {"title": "1. try-catch-finally", "content": "<p><code>try</code> wraps risky code. <code>catch</code> handles specific exceptions. <code>finally</code> always executes (cleanup). You can catch multiple exceptions: <code>catch (IOException | SQLException e)</code>.</p>"},
        {"title": "2. throw & throws", "content": "<p><code>throw</code> manually raises an exception: <code>throw new IllegalArgumentException(\"Invalid\");</code>. <code>throws</code> declares that a method might throw a checked exception: <code>void read() throws IOException</code>.</p>"},
        {"title": "3. Custom Exceptions", "content": "<p>Create custom exceptions by extending <code>Exception</code> (checked) or <code>RuntimeException</code> (unchecked). Custom exceptions provide meaningful error types for your application's domain.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Checked:</strong> Compiler forces you to handle (IOException, etc.)</li><li><strong>Unchecked:</strong> RuntimeExceptions, optional to catch</li><li><strong>finally:</strong> Always executes, used for resource cleanup</li><li><strong>try-with-resources:</strong> Automatically closes resources like files and streams</li></ul>",
    "examples": [
        ex("try-catch", 'try {\n    int[] arr = {1, 2, 3};\n    System.out.println(arr[10]);\n} catch (ArrayIndexOutOfBoundsException e) {\n    System.out.println("Error: " + e.getMessage());\n} finally {\n    System.out.println("Cleanup done.");\n}', "Error: Index 10 out of bounds for length 3\nCleanup done.", "The catch block handles the exception gracefully. finally runs regardless of whether an exception occurred.")
    ]
},

"java_collections": {
    "introduction": "<p>The <strong>Java Collections Framework</strong> provides ready-to-use data structures: <code>List</code>, <code>Set</code>, <code>Map</code>, <code>Queue</code>. These are far more flexible than arrays, supporting dynamic sizing, searching, sorting, and complex operations.</p><p>Key implementations: <code>ArrayList</code> (dynamic array), <code>LinkedList</code> (doubly-linked), <code>HashSet</code> (unique elements), <code>HashMap</code> (key-value pairs), <code>TreeMap</code> (sorted map).</p>",
    "subtopics": [
        {"title": "1. List (ArrayList, LinkedList)", "content": "<p><code>ArrayList</code> is backed by an array - fast random access O(1), slow inserts/deletes in the middle O(n). <code>LinkedList</code> uses nodes - slow access O(n), fast inserts/deletes O(1). Choose based on your use case.</p>"},
        {"title": "2. Set (HashSet, TreeSet)", "content": "<p>Sets store unique elements only - duplicates are silently ignored. <code>HashSet</code> is unordered O(1), <code>TreeSet</code> is sorted O(log n). Use Set when you need to eliminate duplicates or check membership quickly.</p>"},
        {"title": "3. Map (HashMap, TreeMap)", "content": "<p>Maps store key-value pairs. <code>HashMap</code> is the most used - O(1) lookups by key. <code>TreeMap</code> keeps keys sorted. Use <code>.put(key, value)</code> to add and <code>.get(key)</code> to retrieve.</p>"}
    ],
    "key_concepts": "<ul><li><strong>List:</strong> Ordered, allows duplicates (ArrayList, LinkedList)</li><li><strong>Set:</strong> Unordered, no duplicates (HashSet, TreeSet)</li><li><strong>Map:</strong> Key-value pairs, keys are unique (HashMap, TreeMap)</li><li><strong>Iterator:</strong> Standard way to traverse collections</li></ul>",
    "examples": [
        ex("HashMap", 'import java.util.HashMap;\n\nHashMap<String, Integer> ages = new HashMap<>();\nages.put("Alice", 25);\nages.put("Bob", 30);\nages.put("Charlie", 28);\n\nSystem.out.println(ages.get("Bob"));\n\nfor (var entry : ages.entrySet()) {\n    System.out.println(entry.getKey() + ": " + entry.getValue());\n}', "30\nAlice: 25\nBob: 30\nCharlie: 28", "HashMap stores key-value pairs with O(1) lookup. entrySet() returns all entries for iteration. Keys must be unique.")
    ]
},

"java_generics": {
    "introduction": "<p><strong>Generics</strong> enable you to write classes, interfaces, and methods that work with any type while maintaining type safety. Before generics, collections stored <code>Object</code>, requiring unsafe casting and risking ClassCastException at runtime.</p><p>With generics, the compiler catches type mismatches at compile time: <code>ArrayList&lt;String&gt;</code> only accepts Strings - trying to add an Integer is a compile error.</p>",
    "subtopics": [
        {"title": "1. Generic Classes & Methods", "content": "<p>Define a generic class: <code>class Box&lt;T&gt; { T value; }</code>. The type parameter <code>T</code> is replaced with an actual type at creation: <code>Box&lt;String&gt; box = new Box&lt;&gt;();</code>. Generic methods: <code>&lt;T&gt; void print(T item)</code>.</p>"},
        {"title": "2. Bounded Type Parameters", "content": "<p>Restrict the types that can be used: <code>&lt;T extends Number&gt;</code> means T must be Number or a subclass (Integer, Double, etc.). Upper bounds enable calling methods specific to the bound type.</p>"},
        {"title": "3. Wildcards", "content": "<p><code>?</code> represents an unknown type. <code>? extends T</code> (upper bound), <code>? super T</code> (lower bound). Use <code>extends</code> for reading (producer), <code>super</code> for writing (consumer) - the PECS principle.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Type Safety:</strong> Compiler catches wrong types at compile time</li><li><strong>Type Erasure:</strong> Generic type info is removed at runtime</li><li><strong>Bounded Types:</strong> Restrict generics to specific type hierarchies</li><li><strong>PECS:</strong> Producer Extends, Consumer Super</li></ul>",
    "examples": [
        ex("Generic Class", 'class Pair<A, B> {\n    A first;\n    B second;\n    Pair(A first, B second) {\n        this.first = first;\n        this.second = second;\n    }\n    public String toString() {\n        return "(" + first + ", " + second + ")";\n    }\n}\n\nPair<String, Integer> p = new Pair<>("Alice", 25);\nSystem.out.println(p);', "(Alice, 25)", "The Pair class works with any two types. Type parameters A and B are specified at creation, ensuring type safety throughout.")
    ]
},

"java_streams": {
    "introduction": "<p><strong>Streams</strong> (Java 8+) provide a functional approach to processing collections. Instead of writing loops, you chain operations like <code>filter()</code>, <code>map()</code>, and <code>reduce()</code> to process data declaratively.</p><p>Streams don't modify the source collection - they create a pipeline of operations that produce a new result. They can also run in parallel for improved performance on large datasets.</p>",
    "subtopics": [
        {"title": "1. Stream Operations", "content": "<p><strong>Intermediate</strong> operations (lazy, return a new stream): <code>filter()</code>, <code>map()</code>, <code>sorted()</code>, <code>distinct()</code>. <strong>Terminal</strong> operations (trigger execution): <code>forEach()</code>, <code>collect()</code>, <code>count()</code>, <code>reduce()</code>.</p>"},
        {"title": "2. Collectors", "content": "<p><code>collect(Collectors.toList())</code> gathers results into a List. Other collectors: <code>toSet()</code>, <code>toMap()</code>, <code>joining()</code>, <code>groupingBy()</code>. Collectors are the bridge between streams and concrete collections.</p>"},
        {"title": "3. Optional", "content": "<p><code>Optional&lt;T&gt;</code> is a container that may or may not contain a value. It replaces null checks: <code>Optional.ofNullable(value).orElse(\"default\")</code>. Methods: <code>isPresent()</code>, <code>ifPresent()</code>, <code>orElse()</code>, <code>map()</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Lazy Evaluation:</strong> Intermediate operations don't execute until a terminal operation is called</li><li><strong>Immutable Pipeline:</strong> Streams don't modify the source collection</li><li><strong>Parallel Streams:</strong> .parallelStream() for multi-threaded processing</li><li><strong>Optional:</strong> Elegant null handling without NullPointerException</li></ul>",
    "examples": [
        ex("Stream Pipeline", 'import java.util.*;\nimport java.util.stream.*;\n\nList<String> names = Arrays.asList("Alice", "Bob", "Charlie", "Anna", "David");\n\nList<String> result = names.stream()\n    .filter(n -> n.startsWith("A"))\n    .map(String::toUpperCase)\n    .sorted()\n    .collect(Collectors.toList());\n\nSystem.out.println(result);', "[ALICE, ANNA]", "The stream filters names starting with A, converts to uppercase, sorts, and collects into a List. All without modifying the original list.")
    ]
},

"java_advanced": {
    "introduction": "<p><strong>Advanced Java</strong> covers topics that are essential for professional development: multithreading, lambda expressions, the java.time API, annotations, and design patterns. These concepts appear frequently in technical interviews and real-world applications.</p><p>Mastering these topics takes you from a Java beginner to a confident developer who can build concurrent, robust, and maintainable applications.</p>",
    "subtopics": [
        {"title": "1. Lambda Expressions", "content": "<p>Lambdas provide a concise way to implement functional interfaces: <code>(parameters) -> expression</code>. They replaced anonymous inner classes for simple callbacks. Method references (<code>System.out::println</code>) further simplify lambda syntax.</p>"},
        {"title": "2. Multithreading", "content": "<p>Java supports concurrent execution with <code>Thread</code> class and <code>Runnable</code> interface. The <code>ExecutorService</code> manages thread pools for better resource management. Use <code>synchronized</code> to prevent race conditions when threads share data.</p>"},
        {"title": "3. Java Time API", "content": "<p>The <code>java.time</code> package (Java 8+) replaces the old Date/Calendar mess. Key classes: <code>LocalDate</code>, <code>LocalTime</code>, <code>LocalDateTime</code>, <code>Duration</code>, <code>Period</code>. All immutable and thread-safe.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Lambdas:</strong> Concise syntax for functional interface implementations</li><li><strong>Threads:</strong> Enable concurrent execution of code</li><li><strong>synchronized:</strong> Prevents race conditions in multi-threaded code</li><li><strong>java.time:</strong> Modern, immutable date/time API</li></ul>",
    "examples": [
        ex("Lambda & Streams", 'import java.util.*;\n\nList<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);\n\nint sumOfEvens = nums.stream()\n    .filter(n -> n % 2 == 0)\n    .mapToInt(Integer::intValue)\n    .sum();\n\nSystem.out.println("Sum of evens: " + sumOfEvens);', "Sum of evens: 30", "Lambdas (n -> n % 2 == 0) define inline predicates. Method references (Integer::intValue) are shorthand for simple lambdas.")
    ]
}
}

# Apply to tracks_data.js
for topic_id, structured in JAVA.items():
    if topic_id in d['java']['content']:
        d['java']['content'][topic_id]['structured'] = structured

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print("Java: All 17 topics now have structured content!")
