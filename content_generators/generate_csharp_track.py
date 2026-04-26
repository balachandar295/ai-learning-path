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
    for lbl, code in examples: h += card(lbl, code)
    return h

def explanation(title, sections):
    h = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections: h += section(*s)
    return h + "</div>"

def quiz(items): return [{"q":q,"options":o,"answer":a} for q,o,a in items]
def task(t,d,h,c): return {"title":t,"description":d,"hint":h,"code":c}
def problems(items): return [{"title":t,"description":d,"code":c} for t,d,c in items]

# ══════ C# NODES ══════
cs_nodes_raw = [
    ("cs_basics",       "C# Basics",           1),
    ("cs_variables",    "Variables & Types",   1),
    ("cs_operators",    "Operators",            1),
    ("cs_control",      "Control Flow",         1),
    ("cs_loops",        "Loops",                1),
    ("cs_methods",      "Methods",              2),
    ("cs_arrays",       "Arrays & Lists",       2),
    ("cs_strings",      "Strings",              2),
    ("cs_oop",          "OOP Basics",           2),
    ("cs_inheritance",  "Inheritance",          3),
    ("cs_interfaces",   "Interfaces",           3),
    ("cs_exceptions",   "Exceptions",           3),
    ("cs_generics",     "Generics",             3),
    ("cs_linq",         "LINQ",                 4),
    ("cs_async",        "Async / Await",        4),
    ("cs_delegates",    "Delegates & Events",   4),
    ("cs_advanced",     "Advanced C#",          4),
    ("cs_interview",    "C# Interview Guide",   5),
]

cs_nodes = []
for i, (nid, title, phase) in enumerate(cs_nodes_raw):
    node = {"id": nid, "title": title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase}
    if i > 0: node["parent"] = cs_nodes_raw[i-1][0]
    cs_nodes.append(node)

cs_content = {}

cs_content["cs_basics"] = {
    "title": "C# Basics",
    "explanation": explanation("C# Basics", [
        ("What is C#?",
         "C# (C-Sharp) is a modern, object-oriented language by Microsoft, designed for the .NET platform. It combines power of C++ with simplicity of Java. Used for Windows apps, web (ASP.NET), games (Unity), and more.",
         [("Hello World", 'using System;\n\nclass Program {\n    static void Main(string[] args) {\n        Console.WriteLine("Hello, World!");\n        Console.Write("No newline here");\n        Console.WriteLine($"Formatted: {42}");\n    }\n}'),
          ("Program structure", '// 1. namespace (optional grouping)\nnamespace MyApp {\n\n    // 2. class\n    class Program {\n\n        // 3. Main — entry point\n        static void Main(string[] args) {\n            // 4. Statements\n            string name = "Alice";\n            Console.WriteLine($"Hello, {name}!");\n        }\n    }\n}')]),
        ("Reading Input & Console",
         "Use Console.ReadLine() to read input as string. Convert to other types using int.Parse(), double.Parse() etc.",
         [("User input", 'using System;\n\nclass Program {\n    static void Main() {\n        Console.Write("Enter your name: ");\n        string name = Console.ReadLine();\n\n        Console.Write("Enter your age: ");\n        int age = int.Parse(Console.ReadLine());\n\n        Console.WriteLine($"Hello {name}! You are {age} years old.");\n    }\n}'),
          ("String interpolation & format", 'string name = "Bob";\ndouble gpa = 3.75;\n\n// $"" — string interpolation (C# 6+)\nConsole.WriteLine($"Name: {name}, GPA: {gpa:F2}");\n\n// String.Format\nConsole.WriteLine(String.Format("Name: {0}, GPA: {1:F2}", name, gpa));\n\n// Console.WriteLine format\nConsole.WriteLine("Score: {0} out of {1}", 85, 100);')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("C# is developed by?", ["Google", "Microsoft", "Oracle", "Apple"], "Microsoft"),
        ("Entry point of C# program is?", ["Start()", "Main()", "Run()", "Init()"], "Main()"),
        ("How is string interpolation done in C#?", ['Concatenation with +', '$"..." with {}', 'format()', 'printf()'], '$"..." with {}'),
        ("Console.ReadLine() returns?", ["int", "char", "string", "double"], "string"),
        ("C# file extension is?", [".cpp", ".cs", ".java", ".c#"], ".cs"),
    ]),
    "hands_on": task("Greeting Program", "Write a C# program that reads name and age, then prints a formatted greeting.", "Use Console.ReadLine() + int.Parse(). Use $\"\" interpolation.", 'using System;\nclass Program {\n    static void Main() {\n        Console.Write("Name: ");\n        string name = Console.ReadLine();\n        Console.Write("Age: ");\n        int age = int.Parse(Console.ReadLine());\n        Console.WriteLine($"Hello, {name}! You are {age} years old.");\n        Console.WriteLine($"In 10 years you will be {age + 10}.");\n    }\n}'),
    "problem_solving": problems([
        ("BMI Calculator", "Calculate BMI from weight and height.", 'Console.Write("Weight(kg): ");\ndouble w = double.Parse(Console.ReadLine());\nConsole.Write("Height(m): ");\ndouble h = double.Parse(Console.ReadLine());\nConsole.WriteLine($"BMI: {w/(h*h):F2}");'),
        ("Swap Numbers", "Read two numbers and swap them.", 'int a = 10, b = 20;\n(a, b) = (b, a);  // C# tuple swap\nConsole.WriteLine($"a={a}, b={b}");'),
        ("Celsius to Fahrenheit", "Convert temperature.", 'double c = 100;\nConsole.WriteLine($"{c}°C = {c*9/5+32}°F");'),
    ])
}

cs_content["cs_variables"] = {
    "title": "Variables & Data Types",
    "explanation": explanation("Variables & Data Types", [
        ("C# Value & Reference Types",
         "Value types (int,double,bool,char,struct) store data directly. Reference types (string,class,array) store memory address.",
         [("Common types", '// Value types\nint i = 42;\ndouble d = 3.14;\nbool b = true;\nchar c = \'A\';\nfloat f = 2.5f;\nlong l = 999999999L;\ndecimal price = 19.99m;  // precise for money!\n\n// Reference types\nstring name = "Alice"; // string is special — acts like value\nint[] arr = {1,2,3};\n\n// var — type inference (C# 3+)\nvar x = 42;        // inferred as int\nvar s = "Hello";   // inferred as string'),
          ("Nullable types & null coalescing", '// Nullable: int? can hold null\nint? age = null;\nif (age.HasValue)\n    Console.WriteLine(age.Value);\nelse\n    Console.WriteLine("No age set");\n\n// ?? — null coalescing operator\nstring name = null;\nstring display = name ?? "Anonymous";\nConsole.WriteLine(display);  // Anonymous\n\n// ??= — null coalescing assignment (C# 8+)\nname ??= "Default";\nConsole.WriteLine(name);  // Default')]),
        ("Type Conversion & Constants",
         "Implicit conversion (safe widening). Explicit cast (narrow). Convert class for string conversions. const for compile-time constants.",
         [("Conversions", '// Implicit (safe)\nint i = 100;\nlong l = i;       // int -> long (auto)\ndouble d = l;     // long -> double (auto)\n\n// Explicit cast (may lose data)\ndouble pi = 3.14159;\nint truncated = (int)pi;  // 3 (loses .14159)\n\n// Convert class\nstring s = "42";\nint n = Convert.ToInt32(s);\nint n2 = int.Parse(s);\nbool ok = int.TryParse("abc", out int result);  // safe parse\nConsole.WriteLine(ok);     // False (no exception!)'),
          ("Constants & readonly", 'const double PI = 3.14159;  // compile-time constant\n// PI = 3; // ERROR!\n\nclass Config {\n    // readonly: set in constructor only\n    public readonly string Version;\n    public Config(string v) { Version = v; }\n}\n// Use const for known values, readonly for runtime constants')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which type is best for monetary calculations?", ["double", "float", "decimal", "int"], "decimal"),
        ("int? means?", ["Always null", "Nullable integer (can hold null)", "Pointer to int", "Integer array"], "Nullable integer (can hold null)"),
        ("What does ?? do?", ["Creates null", "Returns right side if left is null", "Compares nulls", "Throws NullException"], "Returns right side if left is null"),
        ("var keyword does what?", ["Makes variable variant", "Infers type from assigned value", "Creates variant type", "Declares global variable"], "Infers type from assigned value"),
        ("int.TryParse advantage over int.Parse?", ["Faster", "Returns bool, doesn't throw exception on invalid input", "Handles larger numbers", "Works with any type"], "Returns bool, doesn't throw exception on invalid input"),
    ]),
    "hands_on": task("Type Safety Demo", "Demonstrate: var, nullable int?, ?? operator, and int.TryParse. Show what happens with invalid input.", "Try parsing 'abc' with TryParse. Show ?? fallback.", 'using System;\nclass Program {\n    static void Main() {\n        var score = 95;   // inferred int\n        int? optional = null;\n        Console.WriteLine(optional ?? -1);  // -1\n\n        // Safe parsing\n        string input = "abc";\n        if (int.TryParse(input, out int n))\n            Console.WriteLine($"Parsed: {n}");\n        else\n            Console.WriteLine($"Cannot parse: {input}");\n    }\n}'),
    "problem_solving": problems([
        ("Safe Division", "Parse two strings as numbers, divide safely checking for divide by zero.", 'string a="10", b="0";\nif(int.TryParse(a,out int x)&&int.TryParse(b,out int y))\n    Console.WriteLine(y!=0?(object)(x/y):"Divide by zero");\nelse Console.WriteLine("Invalid input");'),
        ("Hours to HH:MM:SS", "Convert 3661 seconds to hours, minutes, seconds.", 'int total=3661;\nConsole.WriteLine($"{total/3600:D2}:{total%3600/60:D2}:{total%60:D2}");'),
        ("Average with decimal", "Calculate average of [85, 92, 78, 95] precisely using decimal.", 'decimal[] marks={85,92,78,95};\ndecimal sum=0;\nforeach(var m in marks) sum+=m;\nConsole.WriteLine($"Average: {sum/marks.Length:F2}");'),
    ])
}

cs_content["cs_variables"]["examples"] = []

# Topics 3-5
for nid, title, phase, ex_code, ex_label, quiz_items, hand_code in [
    ("cs_operators", "Operators", 1,
     'int a=17,b=5;\nConsole.WriteLine($"{a}+{b}={a+b}");\nConsole.WriteLine($"{a}/{b}={a/b} (int)");\nConsole.WriteLine($"{a}/{b}={(double)a/b:F2} (double)");\nConsole.WriteLine($"{a}%{b}={a%b}");\nstring r = a>b ? "a larger" : "b larger";\nConsole.WriteLine(r);',
     "Arithmetic & ternary",
     [("What is 17/5 in C# (int)?", ["3.4","3","4","2"],"3"),
      ("== for strings in C#?", ["Checks reference","Checks value (unlike Java)","Syntax error","Returns int"],"Checks value (unlike Java)"),
      ("?? operator returns?",["Left if not null","Right if left is null","Both","null always"],"Right if left is null"),
      ("What is 2 ** 3 in C#?", ["Not valid syntax","Math.Pow(2,3)","2^3","8 directly"],"Math.Pow(2,3)"),
      ("Ternary syntax?",["if a? b:c","a?b:c","a then b else c","b if a else c"],"a?b:c")],
     'int score=82;\nstring g=score>=90?"A":score>=75?"B":score>=60?"C":"F";\nConsole.WriteLine($"Grade: {g}");'),

    ("cs_control", "Control Flow", 1,
     'int n=75;\nif(n>=90) Console.WriteLine("A");\nelse if(n>=75) Console.WriteLine("B");\nelse if(n>=60) Console.WriteLine("C");\nelse Console.WriteLine("F");\n\nstring day="Monday";\nswitch(day) {\n    case "Monday": Console.WriteLine("Start week"); break;\n    case "Friday": Console.WriteLine("End week");   break;\n    default:       Console.WriteLine("Midweek");\n}',
     "if-else and switch",
     [("switch in C# works with?",["int only","int,string,enum and more","All types","float too"],"int,string,enum and more"),
      ("C# switch expression uses?",["colon :","arrow =>","equals =","pipe |"],"arrow =>"),
      ("C# if condition must be?",["int","bool","any truthy value","string"],"bool"),
      ("fall-through in C# switch?",["Allowed","Not allowed without goto","Always happens","Optional"],"Not allowed without goto"),
      ("Pattern matching in C# uses?",["instanceof","is keyword","typeof","as keyword"],"is keyword")],
     'int x=5;\nstring result = x switch {\n    < 0 => "Negative",\n    0 => "Zero",\n    > 0 => "Positive"\n};\nConsole.WriteLine(result);'),

    ("cs_loops", "Loops", 1,
     '// for loop\nfor(int i=1; i<=5; i++) Console.Write(i+" ");\nConsole.WriteLine();\n\n// foreach (best for collections)\nstring[] langs={"C#","Java","Python"};\nforeach(string l in langs) Console.WriteLine(l);\n\n// while\nint n=1;\nwhile(n<=5){Console.Write(n+" "); n++;}\n\n// LINQ alternative\nvar nums=Enumerable.Range(1,10).Where(x=>x%2==0);\nforeach(var n2 in nums) Console.Write(n2+" ");',
     "for, foreach, while, LINQ range",
     [("foreach iterates?",["Only arrays","Any IEnumerable collection","Only List","Only Dictionary"],"Any IEnumerable collection"),
      ("do-while guarantee?",["Runs n times","Runs at least once","Runs condition times","Never runs if false"],"Runs at least once"),
      ("break does what?",["Skips iteration","Exits loop completely","Restarts loop","Pauses execution"],"Exits loop completely"),
      ("Enumerable.Range(1,5) generates?",["1,2,3,4,5,6","1,2,3,4,5","0,1,2,3,4","2,3,4,5,6"],"1,2,3,4,5"),
      ("continue does?",["Exits loop","Skips current iteration","Restarts loop","Throws exception"],"Skips current iteration")],
     'int sum=0;\nfor(int i=1;i<=100;i++) sum+=i;\nConsole.WriteLine($"Sum 1-100: {sum}");'),
]:
    cs_content[nid] = {
        "title": title,
        "explanation": explanation(title, [
            ("Key Concepts", f"{title} in C# with full examples.", [(ex_label, ex_code)])
        ]),
        "examples": [],
        "concept_quiz": quiz(quiz_items),
        "hands_on": task(f"Practice {title}", f"Apply {title} concepts in a C# program.", "Use what you learned above.", hand_code),
        "problem_solving": problems([
            (f"{title} Challenge 1", f"Fibonacci using {title.lower()}.", 'int a=0,b=1;\nfor(int i=0;i<10;i++){Console.Write(a+" ");int c=a+b;a=b;b=c;}'),
            (f"{title} Challenge 2", f"Sum of digits.", 'int n=12345,s=0;\nwhile(n>0){s+=n%10;n/=10;}\nConsole.WriteLine($"Digit sum: {s}");'),
        ])
    }

# Topics 6-17: C# methods, arrays, strings, OOP, etc.
for nid, title in [("cs_methods","Methods"),("cs_arrays","Arrays & Lists"),("cs_strings","Strings"),
                   ("cs_oop","OOP Basics"),("cs_inheritance","Inheritance"),("cs_interfaces","Interfaces"),
                   ("cs_exceptions","Exceptions"),("cs_generics","Generics"),("cs_linq","LINQ"),
                   ("cs_async","Async / Await"),("cs_delegates","Delegates & Events"),("cs_advanced","Advanced C#")]:
    ex_codes = {
        "cs_methods": ('// Method overloading\nstatic int Add(int a, int b) => a + b;\nstatic double Add(double a, double b) => a + b;\n\n// Optional params\nstatic void Greet(string name, string msg = "Hello") =>\n    Console.WriteLine($"{msg}, {name}!");\n\n// out parameter\nstatic bool Divide(int a, int b, out double result) {\n    if(b == 0) { result = 0; return false; }\n    result = (double)a / b;\n    return true;\n}\n\nGreet("Alice");\nGreet("Bob", "Hi");\nif(Divide(10, 3, out double r)) Console.WriteLine($"Result: {r:F2}");', "Methods: overloading, optional params, out"),
        "cs_arrays": ('using System.Collections.Generic;\n// Array\nint[] arr = {5,3,8,1,9};\nArray.Sort(arr);\nConsole.WriteLine(string.Join(",", arr));\n\n// List<T>\nList<string> names = new List<string>{"Alice","Bob","Charlie"};\nnames.Add("Dave");\nnames.Remove("Bob");\nnames.Sort();\nnames.ForEach(Console.WriteLine);\n\n// Dictionary\nDictionary<string,int> scores = new(){\n    {"Alice",90},{"Bob",85},{"Carol",92}\n};\nforeach(var kv in scores)\n    Console.WriteLine($"{kv.Key}: {kv.Value}");', "Array + List + Dictionary"),
        "cs_strings": ('string s = "  Hello, C# World!  ";\nConsole.WriteLine(s.Trim());\nConsole.WriteLine(s.Trim().ToUpper());\nConsole.WriteLine(s.Contains("C#"));\nConsole.WriteLine(s.Replace("C#","Java"));\nConsole.WriteLine(s.Trim().Split(\' \').Length);\n\n// Verbatim string (no escaping)\nstring path = @"C:\\Users\\Alice\\Desktop";\n\n// Multi-line interpolation\nstring name = "Alice";\nint age = 25;\nstring info = $"""\n    Name: {name}\n    Age:  {age}\n    """;\nConsole.WriteLine(info);', "String methods + verbatim + raw strings"),
        "cs_oop": ('class BankAccount {\n    private decimal _balance;\n    public string Owner { get; }\n\n    public BankAccount(string owner, decimal balance) {\n        Owner = owner;\n        _balance = balance;\n    }\n\n    public bool Deposit(decimal amount) {\n        if(amount <= 0) return false;\n        _balance += amount;\n        return true;\n    }\n\n    public decimal Balance => _balance;  // readonly property\n\n    public override string ToString() =>\n        $"{Owner}: ${_balance:F2}";\n}\n\nvar acc = new BankAccount("Alice", 1000m);\nacc.Deposit(500m);\nConsole.WriteLine(acc);  // Alice: $1500.00', "Classes, properties, encapsulation"),
        "cs_inheritance": ('abstract class Shape {\n    public string Color { get; }\n    protected Shape(string color) => Color = color;\n    public abstract double Area();\n    public override string ToString() =>\n        $"{GetType().Name} [{Color}] area={Area():F2}";\n}\n\nclass Circle : Shape {\n    public double Radius { get; }\n    public Circle(string color, double r) : base(color) => Radius = r;\n    public override double Area() => Math.PI * Radius * Radius;\n}\n\nShape[] shapes = { new Circle("red", 5) };\nforeach(var s in shapes) Console.WriteLine(s);', "Inheritance, abstract, override"),
        "cs_interfaces": ('interface IAnimal {\n    string Name { get; }\n    void Speak();  // must implement\n    void Sleep() => Console.WriteLine($"{Name} is sleeping");  // default\n}\n\nclass Dog : IAnimal {\n    public string Name { get; }\n    public Dog(string name) => Name = name;\n    public void Speak() => Console.WriteLine($"{Name}: Woof!");\n}\n\nIAnimal d = new Dog("Rex");\nd.Speak();\nd.Sleep();', "Interfaces + default methods"),
        "cs_exceptions": ('try {\n    int[] arr = {1,2,3};\n    Console.WriteLine(arr[10]);\n}\ncatch (IndexOutOfRangeException ex) {\n    Console.WriteLine($"Array error: {ex.Message}");\n}\ncatch (Exception ex) {\n    Console.WriteLine($"General: {ex.Message}");\n}\nfinally {\n    Console.WriteLine("Finally always runs!");\n}\n\n// Custom exception\npublic class AgeException : Exception {\n    public AgeException(string msg) : base(msg) {}\n}\n\nstatic void ValidateAge(int age) {\n    if(age < 0) throw new AgeException("Age cannot be negative");\n}', "try-catch-finally, custom exceptions"),
        "cs_generics": ('// Generic class\nclass Stack<T> {\n    private List<T> _items = new();\n    public void Push(T item) => _items.Add(item);\n    public T Pop() { var t=_items[^1]; _items.RemoveAt(_items.Count-1); return t; }\n    public T Peek() => _items[^1];\n    public int Count => _items.Count;\n}\n\nvar s = new Stack<int>();\ns.Push(1); s.Push(2); s.Push(3);\nConsole.WriteLine(s.Pop());   // 3\n\n// Generic method\nstatic T Max<T>(T a, T b) where T : IComparable<T>\n    => a.CompareTo(b) >= 0 ? a : b;\nConsole.WriteLine(Max(10, 25));        // 25\nConsole.WriteLine(Max("Apple","Mango")); // Mango', "Generic class + method + constraints"),
        "cs_linq": ('using System.Linq;\n\nint[] nums = {1,2,3,4,5,6,7,8,9,10};\n\n// Query syntax\nvar evens = from n in nums\n            where n % 2 == 0\n            orderby n descending\n            select n * n;\n\n// Method syntax (same result)\nvar evens2 = nums.Where(n=>n%2==0)\n                 .OrderByDescending(n=>n)\n                 .Select(n=>n*n);\n\nConsole.WriteLine(string.Join(",", evens)); // 100,64,36,16,4\nConsole.WriteLine(nums.Average());  // 5.5\nConsole.WriteLine(nums.Sum());      // 55\nConsole.WriteLine(nums.Max());      // 10', "LINQ query + method syntax"),
        "cs_async": ('using System.Threading.Tasks;\n\nstatic async Task<string> FetchDataAsync(int id) {\n    await Task.Delay(500);  // simulate async work\n    return $"Data for id={id}";\n}\n\nstatic async Task Main() {\n    Console.WriteLine("Starting...");\n\n    // Single await\n    var data = await FetchDataAsync(1);\n    Console.WriteLine(data);\n\n    // Parallel tasks\n    var t1 = FetchDataAsync(2);\n    var t2 = FetchDataAsync(3);\n    var results = await Task.WhenAll(t1, t2);\n    foreach(var r in results) Console.WriteLine(r);\n}', "async/await + Task.WhenAll"),
        "cs_delegates": ('// Delegate type\ndelegate int MathOp(int a, int b);\n\nMathOp add = (a,b) => a+b;\nMathOp mul = (a,b) => a*b;\n\nConsole.WriteLine(add(5,3));  // 8\nConsole.WriteLine(mul(5,3));  // 15\n\n// Action (no return) and Func (with return)\nAction<string> print = msg => Console.WriteLine(msg);\nFunc<int,int,int> sub = (a,b) => a-b;\n\nprint("Hello from Action!");\nConsole.WriteLine(sub(10,4));  // 6\n\n// Event scenario\npublic event Action<string> OnMessage;\nOnMessage += msg => Console.WriteLine($"Handler: {msg}");', "Delegates + Action + Func + Events"),
        "cs_advanced": ('// Records (immutable data)\nrecord Person(string Name, int Age);\nvar p = new Person("Alice", 25);\nConsole.WriteLine(p);  // Person { Name = Alice, Age = 25 }\n\n// Pattern matching\nobject obj = 42;\nif(obj is int n && n > 10)\n    Console.WriteLine($"Large int: {n}");\n\n// Span<T> for zero-allocation\nReadOnlySpan<char> span = "Hello World".AsSpan();\nConsole.WriteLine(span.Slice(0,5).ToString()); // Hello\n\n// init-only properties\nclass Config {\n    public string Host { get; init; } = "localhost";\n    public int Port { get; init; } = 8080;\n}\nvar cfg = new Config { Host="example.com", Port=443 };', "Records, pattern matching, Span, init"),
    }
    code = ex_codes.get(nid, f'// {title} example\nConsole.WriteLine("Learning {title} in C#!");')
    cs_content[nid] = {
        "title": title,
        "explanation": explanation(title, [
            ("Introduction", f"{title} is a key C# concept used in modern application development.", [(f"{title} Example", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([
            (f"Is {title} important in C#?", ["Yes", "No", "Optional", "Only in .NET 5+"], "Yes"),
            (f"C# is primarily used with?", [".NET Framework/.NET Core", "JVM", "GCC", "Python runtime"], ".NET Framework/.NET Core"),
        ]),
        "hands_on": task(f"Practice {title}", f"Apply {title} in a working C# program.", "Use the examples above as reference.", code),
        "problem_solving": problems([
            (f"{title} Problem 1", f"Write a program demonstrating {title}.", code),
            (f"{title} Problem 2", "FizzBuzz — print 1-20, 'Fizz' for 3s, 'Buzz' for 5s.", 'for(int i=1;i<=20;i++)\n    Console.WriteLine(i%15==0?"FizzBuzz":i%3==0?"Fizz":i%5==0?"Buzz":i.ToString());'),
        ])
    }

# Interview guide
cs_content["cs_interview"] = {
    "title": "C# Interview Guide",
    "explanation": "<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>Top C# Interview Questions</h3><p style='color:#475569;font-size:1.1rem;margin-bottom:30px;'>Most asked C# questions in Microsoft, Infosys, TCS, Capgemini interviews.</p>" +
        "".join([f"<div style='background:#f8fafc;border-left:4px solid #0ea5e9;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#0ea5e9;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
        for i,(q,a) in enumerate([
            ("What is the difference between class and struct?","Classes are reference types (heap). Structs are value types (stack). Classes support inheritance; structs don't. Use structs for small, immutable data."),
            ("What is a delegate in C#?","A delegate is a type-safe function pointer. It holds a reference to a method. Used for callbacks, events, and LINQ."),
            ("What is LINQ?","Language Integrated Query. Allows querying collections, databases, XML using C# syntax. Supports both query syntax (from...where...select) and method syntax (.Where().Select())."),
            ("What is async/await?","async marks a method as asynchronous. await suspends execution until a Task completes without blocking the thread. Helps in non-blocking I/O operations."),
            ("Difference between IEnumerable and IList?","IEnumerable: read-only, forward-only iteration. IList extends ICollection and IEnumerable — supports indexing, Add, Remove, Insert."),
            ("What is the difference between == and Equals()?","For strings, both check content equality. For custom objects, == compares references by default. Override Equals() for content comparison."),
            ("What are nullable types?","int? allows int to hold null. Use HasValue, Value, or ?? operator. Useful for database fields that may be null."),
            ("What is boxing and unboxing?","Boxing: converting value type to object (reference type). Unboxing: extracting value type from object. Both have performance costs."),
            ("What is a record in C#?","Records (C# 9+) are immutable reference types with value equality. Auto-generates: constructor, getters, Equals, GetHashCode, ToString, with operator."),
            ("What is the difference between abstract class and interface?","Abstract class: can have impl+state, single inheritance. Interface: contract only (till C# 7), multiple impl, C# 8+ allows default methods."),
        ])]) + "</div>",
    "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
}

data['csharp'] = {
    "title": "C# - Beginner to Advanced",
    "description": "Learn C# from basics to advanced including OOP, LINQ, async/await, generics and more.",
    "nodes": cs_nodes,
    "content": cs_content
}

print(f"C# track injected with {len(cs_nodes)} nodes!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
