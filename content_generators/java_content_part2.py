import json

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
json_start = text.find('{')
data = json.loads(text[json_start:text.rfind('}')+1])

def card(label, code):
    return f"<div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'><div style='background:linear-gradient(to right,#f89820,#e65c00);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>{label}</div><pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>{code}</pre></div>"

def section(title, desc, examples):
    h = f"<h4 style='color:#f89820;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #f89820;padding-left:12px;'>{title}</h4>"
    h += f"<p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>{desc}</p>"
    for lbl, code in examples:
        h += card(lbl, code)
    return h

def explanation(title, sections):
    h = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #f89820;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections:
        h += section(*s)
    return h + "</div>"

def quiz(items):
    return [{"q": q, "options": o, "answer": a} for q, o, a in items]
def task(title, desc, hint, code):
    return {"title": title, "description": desc, "hint": hint, "code": code}
def problems(items):
    return [{"title": t, "description": d, "code": c} for t, d, c in items]

jv = data['java']['content']

# TOPIC 6: Arrays
jv['java_arrays'] = {
    "title": "Arrays",
    "explanation": explanation("Arrays", [
        ("Declaring & Initializing Arrays",
         "Arrays store fixed-size, same-type elements. Index starts at 0. Java arrays are objects.",
         [("Declare and use", "// Declare + allocate\nint[] nums = new int[5];\nnums[0] = 10;\nnums[1] = 20;\n\n// Declare + initialize inline\nint[] arr = {10, 20, 30, 40, 50};\nSystem.out.println(arr[2]);        // 30\nSystem.out.println(arr.length);    // 5\n\n// Loop through\nfor (int i = 0; i < arr.length; i++) {\n    System.out.print(arr[i] + \" \");\n}"),
          ("Enhanced for & Arrays utility", "import java.util.Arrays;\n\nint[] arr = {5, 2, 8, 1, 9};\n\n// Sort\nArrays.sort(arr);\nSystem.out.println(Arrays.toString(arr)); // [1,2,5,8,9]\n\n// Binary search (array must be sorted)\nint idx = Arrays.binarySearch(arr, 8);\nSystem.out.println(\"Found at: \" + idx); // 3\n\n// Copy\nint[] copy = Arrays.copyOf(arr, arr.length);\n\n// Fill\nArrays.fill(new int[5], 0);")]),
        ("2D Arrays",
         "2D arrays are arrays of arrays. Used for matrices, grids, tables.",
         [("2D array basics", "// 3x3 matrix\nint[][] matrix = {\n    {1, 2, 3},\n    {4, 5, 6},\n    {7, 8, 9}\n};\n// Access element at row 1, col 2\nSystem.out.println(matrix[1][2]); // 6"),
          ("Traverse 2D array", "int[][] grid = {{1,2,3},{4,5,6},{7,8,9}};\n\nfor (int i = 0; i < grid.length; i++) {\n    for (int j = 0; j < grid[i].length; j++) {\n        System.out.printf(\"%3d\", grid[i][j]);\n    }\n    System.out.println();\n}\n//   1  2  3\n//   4  5  6\n//   7  8  9")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Array index starts at?", ["1", "0", "-1", "Depends"], "0"),
        ("arr.length gives?", ["Last index", "Number of elements", "First element", "Empty slots"], "Number of elements"),
        ("Which import is needed for Arrays.sort()?", ["java.lang.Arrays", "java.util.Arrays", "java.io.Arrays", "No import needed"], "java.util.Arrays"),
        ("int[] arr = new int[5]; arr[5] = 1; throws?", ["NullPointerException", "IndexOutOfBoundsException", "ArrayIndexOutOfBoundsException", "TypeError"], "ArrayIndexOutOfBoundsException"),
        ("2D array matrix[2][3] means?", ["2 rows 3 cols at index", "Row 2 Col 3 element", "Invalid", "2x3 matrix"], "Row 2 Col 3 element"),
    ]),
    "hands_on": task("Array Statistics", "Given array {78,92,55,88,45,67}, find sum, average, min, max.", "Use a loop for sum. Use Math.min/max or compare manually.", "int[] marks = {78, 92, 55, 88, 45, 67};\nint sum = 0, min = marks[0], max = marks[0];\nfor (int m : marks) {\n    sum += m;\n    if (m < min) min = m;\n    if (m > max) max = m;\n}\nSystem.out.println(\"Sum: \" + sum);\nSystem.out.printf(\"Avg: %.1f%n\", (double)sum/marks.length);\nSystem.out.println(\"Min: \" + min + \", Max: \" + max);"),
    "problem_solving": problems([
        ("Reverse Array", "Reverse {1,2,3,4,5} in place and print.", "int[] arr = {1,2,3,4,5};\nfor (int i=0,j=arr.length-1; i<j; i++,j--) {\n    int t=arr[i]; arr[i]=arr[j]; arr[j]=t;\n}\nSystem.out.println(java.util.Arrays.toString(arr));"),
        ("Count Even/Odd", "Count even and odd numbers in {1,2,3,4,5,6,7,8,9,10}.", "int[] a={1,2,3,4,5,6,7,8,9,10};\nint even=0, odd=0;\nfor(int n:a) { if(n%2==0) even++; else odd++; }\nSystem.out.println(\"Even:\"+even+\" Odd:\"+odd);"),
        ("Matrix Diagonal Sum", "Find sum of diagonal elements in 3x3 matrix.", "int[][] m={{1,2,3},{4,5,6},{7,8,9}};\nint sum=0;\nfor(int i=0;i<3;i++) sum+=m[i][i];\nSystem.out.println(\"Diagonal sum: \"+sum); // 15"),
    ])
}

# TOPIC 7: Strings
jv['java_strings'] = {
    "title": "Strings",
    "explanation": explanation("Strings", [
        ("String Basics",
         "String in Java is an immutable class (not primitive). Strings are stored in the String Pool for memory efficiency.",
         [("String creation", "String s1 = \"Hello\";          // String literal (pool)\nString s2 = new String(\"Hello\"); // heap object\n\n// == compares references, equals() compares content\nSystem.out.println(s1 == s2);        // false\nSystem.out.println(s1.equals(s2));   // true\nSystem.out.println(\"Hello\" == s1);   // true (same pool)\n\n// String concatenation\nString full = \"Hello, \" + \"World!\";\nSystem.out.println(full.length());   // 13"),
          ("String methods", "String s = \"  Hello, Java World!  \";\nSystem.out.println(s.trim());                   // no spaces\nSystem.out.println(s.trim().toUpperCase());     // HELLO...\nSystem.out.println(s.trim().toLowerCase());     // hello...\nSystem.out.println(s.contains(\"Java\"));         // true\nSystem.out.println(s.indexOf(\"Java\"));          // 8\nSystem.out.println(s.replace(\"Java\",\"Python\")); // ...\nSystem.out.println(s.trim().substring(0, 5));   // Hello\nSystem.out.println(s.trim().split(\",\").length); // 2")]),
        ("StringBuilder & String.format",
         "String is immutable. Use StringBuilder for repeated modifications (much faster). String.format creates formatted strings.",
         [("StringBuilder", "StringBuilder sb = new StringBuilder();\n\nsb.append(\"Hello\");\nsb.append(\", \");\nsb.append(\"World\");\nsb.insert(5, \"!!!\");\nsb.reverse();\n\nSystem.out.println(sb.length());\nSystem.out.println(sb.toString());\n\n// String.join\nString joined = String.join(\"-\", \"2026\",\"04\",\"01\");\nSystem.out.println(joined); // 2026-04-01"),
          ("String.format & compareTo", "String name = \"Alice\";\nint age = 25;\nString msg = String.format(\"Name: %s, Age: %d\", name, age);\nSystem.out.println(msg);\n\n// Compare alphabetically\nSystem.out.println(\"Apple\".compareTo(\"Banana\")); // negative\nSystem.out.println(\"Hello\".equalsIgnoreCase(\"HELLO\")); // true\nSystem.out.println(\"   \".isBlank());  // true (Java 11+)\nSystem.out.println(\"hi\".repeat(3));   // hihihi (Java 11+)")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("String in Java is?", ["Primitive", "Immutable class", "Mutable class", "Interface"], "Immutable class"),
        ("Which compares String CONTENT?", ["==", "equals()", "compareTo()", "contains()"], "equals()"),
        ("What does StringBuilder provide over String?", ["Immutability", "Mutable string (better for concatenation)", "Thread safety", "Larger capacity"], "Mutable string (better for concatenation)"),
        ("str.indexOf('X') returns when not found?", ["0", "-1", "null", "Exception"], "-1"),
        ("String.format(\"%d + %d = %d\", 1,2,3)?", ["1 + 2 = 3", "d + d = d", "%1+%2=%3", "Error"], "1 + 2 = 3"),
    ]),
    "hands_on": task("String Analyzer", "Analyze the string 'Hello Java World': print length, reverse, uppercase, word count.", "Use split(' ').length for word count. StringBuilder for reverse.", "String s = \"Hello Java World\";\nSystem.out.println(\"Length: \" + s.length());\nSystem.out.println(\"Upper: \" + s.toUpperCase());\nSystem.out.println(\"Words: \" + s.split(\" \").length);\nSystem.out.println(\"Reverse: \" + new StringBuilder(s).reverse());"),
    "problem_solving": problems([
        ("Count Vowels", "Count vowels in 'Hello World'.", "String s=\"Hello World\"; int count=0;\nfor(char c: s.toLowerCase().toCharArray())\n    if(\"aeiou\".indexOf(c)>=0) count++;\nSystem.out.println(\"Vowels: \"+count);"),
        ("Palindrome Check", "Check if 'racecar' is a palindrome.", "String s=\"racecar\";\nString rev=new StringBuilder(s).reverse().toString();\nSystem.out.println(s.equals(rev)?\"Palindrome\":\"Not palindrome\");"),
        ("Count Word Occurrences", "Count how many times 'the' appears in 'the cat sat on the mat'.", "String text=\"the cat sat on the mat\";\nint count=0;\nfor(String w: text.split(\" \"))\n    if(w.equals(\"the\")) count++;\nSystem.out.println(\"'the' appears: \"+count);"),
    ])
}

# TOPIC 8: Methods
jv['java_methods'] = {
    "title": "Methods",
    "explanation": explanation("Methods", [
        ("Method Syntax & Overloading",
         "A method is a reusable block of code. Java supports method overloading — same name, different parameters.",
         [("Method syntax", "public class Calculator {\n\n    // Return type, name, parameters\n    static int add(int a, int b) {\n        return a + b;\n    }\n\n    // void = no return value\n    static void greet(String name) {\n        System.out.println(\"Hello, \" + name + \"!\");\n    }\n\n    public static void main(String[] args) {\n        System.out.println(add(5, 3)); // 8\n        greet(\"Alice\");                // Hello, Alice!\n    }\n}"),
          ("Method overloading", "static double area(double r) {\n    return Math.PI * r * r;  // circle\n}\nstatic double area(double l, double w) {\n    return l * w;            // rectangle\n}\nstatic double area(double b, double h, boolean isTriangle) {\n    return 0.5 * b * h;     // triangle\n}\n\n// Same name, different parameters — compiler decides which to call\nSystem.out.println(area(5.0));           // circle\nSystem.out.println(area(4.0, 6.0));      // rectangle")]),
        ("Recursion & varargs",
         "Recursion = method calling itself. varargs = variable number of arguments using ellipsis (...).",
         [("Recursion - factorial", "static long factorial(int n) {\n    if (n <= 1) return 1;           // base case\n    return n * factorial(n - 1);    // recursive call\n}\n\nSystem.out.println(factorial(6));   // 720\nSystem.out.println(factorial(10));  // 3628800"),
          ("varargs", "static int sum(int... numbers) {\n    int total = 0;\n    for (int n : numbers) total += n;\n    return total;\n}\n\nSystem.out.println(sum(1, 2, 3));         // 6\nSystem.out.println(sum(10, 20, 30, 40)); // 100\nSystem.out.println(sum());               // 0")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Method overloading is determined by?", ["Return type", "Parameter list (type/count)", "Access modifier", "Method body"], "Parameter list (type/count)"),
        ("void method returns?", ["null", "0", "Nothing (no return)", "Empty string"], "Nothing (no return)"),
        ("Recursion must have?", ["Loop inside", "Base case to stop", "Static keyword", "Multiple parameters"], "Base case to stop"),
        ("varargs syntax is?", ["type[] name", "type... name", "type* name", "list<type> name"], "type... name"),
        ("Can Java method return multiple values?", ["Yes", "No, return object/array instead", "Only with varargs", "Yes with void"], "No, return object/array instead"),
    ]),
    "hands_on": task("Fibonacci with Recursion", "Write a recursive method fibonacci(n) that returns nth Fibonacci number. Test with n=7.", "Base case: n<=1 return n. Else return fib(n-1)+fib(n-2).", "static int fibonacci(int n) {\n    if (n <= 1) return n;\n    return fibonacci(n-1) + fibonacci(n-2);\n}\n\npublic static void main(String[] args) {\n    for (int i = 0; i < 10; i++) {\n        System.out.print(fibonacci(i) + \" \");\n    }\n}"),
    "problem_solving": problems([
        ("isPrime method", "Write static boolean isPrime(int n). Test for 7, 10, 13.", "static boolean isPrime(int n) {\n    if (n<2) return false;\n    for(int i=2;i<=Math.sqrt(n);i++)\n        if(n%i==0) return false;\n    return true;\n}\n// Test\nSystem.out.println(isPrime(7));  // true\nSystem.out.println(isPrime(10)); // false"),
        ("Power without Math.pow", "Write power(base, exp) using recursion.", "static long power(int base, int exp) {\n    if(exp==0) return 1;\n    return base * power(base, exp-1);\n}\nSystem.out.println(power(2,8)); // 256"),
        ("Overloaded print", "Create print(int), print(double), print(String) - all print with prefix.", "static void print(int n)    { System.out.println(\"Int: \"+n); }\nstatic void print(double d) { System.out.println(\"Double: \"+d); }\nstatic void print(String s) { System.out.println(\"String: \"+s); }\n// Call all three\nprint(42); print(3.14); print(\"Java\");"),
    ])
}

# TOPIC 9: OOP Basics
jv['java_oop_basics'] = {
    "title": "OOP Basics — Classes & Objects",
    "explanation": explanation("OOP Basics: Classes & Objects", [
        ("Classes & Objects",
         "A class is a blueprint. An object is an instance. Java OOP has 4 pillars: Encapsulation, Inheritance, Polymorphism, Abstraction.",
         [("Class & Object", "public class Student {\n    // Fields (attributes)\n    String name;\n    int age;\n    double gpa;\n\n    // Constructor\n    Student(String name, int age, double gpa) {\n        this.name = name;\n        this.age  = age;\n        this.gpa  = gpa;\n    }\n\n    // Method\n    void introduce() {\n        System.out.println(\"Hi, I'm \" + name +\n                           \", GPA: \" + gpa);\n    }\n\n    // main\n    public static void main(String[] args) {\n        Student s = new Student(\"Alice\", 20, 3.8);\n        s.introduce();\n    }\n}"),
          ("Constructors", "class Box {\n    double width, height, depth;\n\n    // No-arg constructor\n    Box() { this(1.0, 1.0, 1.0); } // calls other constructor\n\n    // Parameterized\n    Box(double w, double h, double d) {\n        width=w; height=h; depth=d;\n    }\n\n    double volume() { return width * height * depth; }\n}\n\nBox unit = new Box();          // 1x1x1 = 1.0\nBox big  = new Box(3,4,5);    // 3x4x5 = 60.0\nSystem.out.println(big.volume());")]),
        ("Encapsulation with getters/setters",
         "Make fields private. Provide public getter/setter methods. This protects data from direct access.",
         [("Private fields + getters/setters", "class BankAccount {\n    private double balance;  // hidden!\n    private String owner;\n\n    BankAccount(String owner, double balance) {\n        this.owner   = owner;\n        this.balance = balance;\n    }\n\n    // Getter\n    public double getBalance() { return balance; }\n\n    // Setter with validation\n    public void deposit(double amount) {\n        if (amount > 0) balance += amount;\n    }\n\n    public boolean withdraw(double amount) {\n        if (amount > 0 && amount <= balance) {\n            balance -= amount;\n            return true;\n        }\n        return false;\n    }\n}\n\nBankAccount acc = new BankAccount(\"Alice\", 1000);\nacc.deposit(500);\nacc.withdraw(200);\nSystem.out.println(acc.getBalance()); // 1300.0"),
          ("static members", "class Counter {\n    private static int count = 0; // shared across all objects\n    private int id;\n\n    Counter() { id = ++count; }\n\n    static int getCount() { return count; }\n    int getId()           { return id; }\n}\n\nnew Counter(); new Counter(); new Counter();\nSystem.out.println(Counter.getCount()); // 3")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("OOP stands for?", ["Object Oriented Programming", "Output Order Processing", "Object Open Protocol", "Operational Object Programming"], "Object Oriented Programming"),
        ("'new' keyword is used to?", ["Declare a class", "Create an object", "Define a method", "Import a class"], "Create an object"),
        ("Encapsulation is enforced using?", ["public fields", "private fields + getters/setters", "static methods", "final classes"], "private fields + getters/setters"),
        ("'this' keyword refers to?", ["Parent class", "Current object", "Static member", "Return value"], "Current object"),
        ("static method belongs to?", ["Object instance", "Class itself", "Constructor", "Interface"], "Class itself"),
    ]),
    "hands_on": task("Employee Class", "Create an Employee class with private fields: name, salary, department. Add constructor, getters, a raise(percent) method.", "Use private fields. raise() should increase salary by percent.", "class Employee {\n    private String name, department;\n    private double salary;\n\n    Employee(String name, String dept, double salary) {\n        this.name=name; this.department=dept; this.salary=salary;\n    }\n    String getName()   { return name; }\n    double getSalary() { return salary; }\n    void raise(double pct) { salary += salary*pct/100; }\n    void info() {\n        System.out.printf(\"%s [%s] Salary: %.2f%n\",name,department,salary);\n    }\n}\n// Test\nEmployee e = new Employee(\"Ravi\",\"IT\",50000);\ne.raise(10);\ne.info();"),
    "problem_solving": problems([
        ("Rectangle Class", "Create Rectangle with width, height. Add area() and perimeter() methods.", "class Rectangle {\n    double w, h;\n    Rectangle(double w, double h){this.w=w;this.h=h;}\n    double area(){return w*h;}\n    double perimeter(){return 2*(w+h);}\n}\nRectangle r=new Rectangle(5,3);\nSystem.out.println(r.area()+\", \"+r.perimeter());"),
        ("Singleton Pattern", "Create a class where only one instance can exist.", "class Singleton {\n    private static Singleton instance;\n    private Singleton(){}\n    static Singleton getInstance(){\n        if(instance==null) instance=new Singleton();\n        return instance;\n    }\n}\nSingleton a=Singleton.getInstance();\nSingleton b=Singleton.getInstance();\nSystem.out.println(a==b); // true"),
        ("toString Override", "Override toString() to print object as string.", "class Point {\n    int x, y;\n    Point(int x,int y){this.x=x;this.y=y;}\n    public String toString(){return \"(\"+x+\",\"+y+\")\";}\n}\nSystem.out.println(new Point(3,4)); // (3,4)"),
    ])
}

print("Java Topics 6-10 done!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
