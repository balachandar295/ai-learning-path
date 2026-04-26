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

# TOPIC 1: Java Basics
jv['java_basics'] = {
    "title": "Java Basics",
    "explanation": explanation("Java Basics", [
        ("What is Java?",
         "Java is a high-level, class-based, object-oriented language. It follows the principle of WORA — Write Once, Run Anywhere. Java code compiles to bytecode that runs on the JVM (Java Virtual Machine).",
         [("Hello World", "public class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n        System.out.print(\"No newline\");\n        System.out.printf(\"Formatted: %d%n\", 42);\n    }\n}"),
          ("JVM / JDK / JRE", "// JDK = Java Development Kit (for developers)\n// JRE = Java Runtime Environment (to run Java)\n// JVM = Java Virtual Machine (executes bytecode)\n\n// Compile:  javac Main.java  -> produces Main.class\n// Run:      java Main        -> JVM executes Main.class")]),
        ("Java Program Structure",
         "Every Java program must have a class. The entry point is always public static void main(String[] args). Java is case-sensitive.",
         [("Structure explained", "// 1. Package declaration (optional)\npackage com.example;\n\n// 2. Imports\nimport java.util.Scanner;\n\n// 3. Class definition (filename must match class name)\npublic class Main {\n\n    // 4. Main method - entry point\n    public static void main(String[] args) {\n        System.out.println(\"Java runs here!\");\n    }\n}"),
          ("Comments", "// Single-line comment\n\n/*\n   Multi-line\n   comment\n*/\n\n/**\n * Javadoc comment\n * @param args command line arguments\n */\npublic static void main(String[] args) { }")]),
        ("Input with Scanner",
         "Use the Scanner class (from java.util) to read user input from console.",
         [("Reading input", "import java.util.Scanner;\n\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        System.out.print(\"Enter your name: \");\n        String name = sc.nextLine();\n        System.out.println(\"Hello, \" + name + \"!\");\n        sc.close();\n    }\n}"),
          ("Different input types", "Scanner sc = new Scanner(System.in);\nint age      = sc.nextInt();     // read integer\ndouble price = sc.nextDouble();  // read decimal\nString word  = sc.next();        // read one word\nsc.nextLine();                   // consume newline\nString line  = sc.nextLine();    // read full line")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Java's 'Write Once Run Anywhere' is possible because of?", ["Compiler", "JVM", "IDE", "OS"], "JVM"),
        ("Java source files have extension?", [".class", ".jav", ".java", ".jar"], ".java"),
        ("Which method is the entry point of a Java program?", ["start()", "run()", "main()", "init()"], "main()"),
        ("Which class is used for console input?", ["System.in", "BufferedReader", "Scanner", "Console"], "Scanner"),
        ("Java is?", ["Interpreted only", "Compiled only", "Both compiled and interpreted", "Neither"], "Both compiled and interpreted"),
    ]),
    "hands_on": task("Personal Info Program", "Write a Java program that takes name and age from user and prints a greeting.", "Use Scanner for input, System.out.println for output.", "import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        System.out.print(\"Name: \");\n        String name = sc.nextLine();\n        System.out.print(\"Age: \");\n        int age = sc.nextInt();\n        System.out.println(\"Hello \" + name + \"! You are \" + age + \" years old.\");\n        sc.close();\n    }\n}"),
    "problem_solving": problems([
        ("Sum Two Numbers", "Take two integers as input and print their sum.", "import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int a = sc.nextInt(), b = sc.nextInt();\n        System.out.println(\"Sum: \" + (a + b));\n    }\n}"),
        ("Area of Circle", "Calculate area of circle given radius from user. Area = PI * r * r.", "import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        double r = sc.nextDouble();\n        System.out.printf(\"Area: %.2f%n\", Math.PI * r * r);\n    }\n}"),
        ("Swap Two Numbers", "Swap two numbers and print them.", "int a = 10, b = 20;\nint temp = a;\na = b;\nb = temp;\nSystem.out.println(\"a=\" + a + \", b=\" + b);"),
    ])
}

# TOPIC 2: Variables & Types
jv['java_variables'] = {
    "title": "Variables & Data Types",
    "explanation": explanation("Variables & Data Types", [
        ("Primitive Data Types",
         "Java has 8 primitive types: byte, short, int, long, float, double, char, boolean. They store values directly.",
         [("All primitives", "byte   b = 127;           // -128 to 127\nshort  s = 32767;         // -32768 to 32767\nint    i = 2147483647;    // most common integer\nlong   l = 9999999999L;   // needs L suffix\nfloat  f = 3.14f;         // needs f suffix\ndouble d = 3.14159265;    // default decimal\nchar   c = 'A';           // single character\nboolean flag = true;      // true or false"),
          ("Variable declaration", "// Declare and assign\nint age = 25;\nString name = \"Alice\";    // String is a class (not primitive)\n\n// Constants with final\nfinal double PI = 3.14159;\n// PI = 3; // ERROR! cannot reassign final\n\n// Multiple declaration\nint x = 1, y = 2, z = 3;")]),
        ("Type Casting",
         "Widening conversion (int to double) is automatic. Narrowing (double to int) needs explicit cast.",
         [("Widening (automatic)", "int i = 100;\nlong l = i;        // int -> long (auto)\ndouble d = l;      // long -> double (auto)\nSystem.out.println(d); // 100.0"),
          ("Narrowing (explicit)", "double d = 9.99;\nint i = (int) d;   // double -> int (loses .99)\nSystem.out.println(i); // 9\n\n// String to int\nString s = \"42\";\nint n = Integer.parseInt(s);\n\n// Int to String\nString result = String.valueOf(42);\nString result2 = Integer.toString(42);")]),
        ("var keyword (Java 10+)",
         "Local variable type inference — Java automatically infers the type from the initializer value.",
         [("var examples", "var name = \"Alice\";    // inferred as String\nvar age  = 25;         // inferred as int\nvar list = new java.util.ArrayList<>();\n\n// var must be initialized\n// var x; // ERROR!\n\nSystem.out.println(name + \" is \" + age);"),
          ("Wrapper Classes", "// Primitives can be wrapped as objects\nInteger num    = 42;       // auto-boxing\nDouble  price  = 9.99;\nBoolean active = true;\n\n// Useful methods\nSystem.out.println(Integer.MAX_VALUE); // 2147483647\nSystem.out.println(Integer.toBinaryString(10)); // 1010\nSystem.out.println(Double.parseDouble(\"3.14\")); // 3.14")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which is NOT a primitive type in Java?", ["int", "boolean", "String", "double"], "String"),
        ("What suffix does a long literal need?", ["l or L", "d or D", "f or F", "b or B"], "l or L"),
        ("What does (int) 9.7 produce?", ["10", "9", "9.7", "Error"], "9"),
        ("final keyword means?", ["Variable is private", "Variable cannot be reassigned", "Variable is static", "Variable is global"], "Variable cannot be reassigned"),
        ("Integer.parseInt() converts?", ["int to String", "String to int", "double to int", "char to int"], "String to int"),
    ]),
    "hands_on": task("Type Converter", "Declare variables of int, double, char, boolean. Print their types using getClass() or instanceof.", "Use wrapper classes. Integer x = 5; x.getClass().getSimpleName()", "int i = 42;\ndouble d = 3.14;\nchar c = 'J';\nboolean b = true;\n\nSystem.out.println(((Integer)i).getClass().getSimpleName()); // Integer\nSystem.out.println(((Double)d).getClass().getSimpleName());  // Double\nSystem.out.println(((Character)c).getClass().getSimpleName()); // Character\nSystem.out.println(((Boolean)b).getClass().getSimpleName());  // Boolean"),
    "problem_solving": problems([
        ("Temperature Converter", "Convert 100 degrees Celsius to Fahrenheit. F = C * 9/5 + 32.", "double celsius = 100;\ndouble fahrenheit = celsius * 9.0/5 + 32;\nSystem.out.printf(\"%.1f C = %.1f F%n\", celsius, fahrenheit);"),
        ("Character to Uppercase", "Take a lowercase char and convert to uppercase without toUpperCase().", "char lower = 'a';\nchar upper = (char)(lower - 32);\nSystem.out.println(upper); // A"),
        ("Largest of Two", "Compare two doubles and print the larger using ternary.", "double a = 3.8, b = 7.2;\ndouble max = (a > b) ? a : b;\nSystem.out.printf(\"Larger: %.1f%n\", max);"),
    ])
}

# TOPIC 3: Operators
jv['java_operators'] = {
    "title": "Operators",
    "explanation": explanation("Operators", [
        ("Arithmetic & Assignment Operators",
         "Java supports standard math operations. Assignment operators like +=, -= modify and reassign in one step.",
         [("Arithmetic", "int a = 17, b = 5;\nSystem.out.println(a + b);   // 22\nSystem.out.println(a - b);   // 12\nSystem.out.println(a * b);   // 85\nSystem.out.println(a / b);   // 3  (integer division!)\nSystem.out.println(a % b);   // 2  (remainder)\nSystem.out.println((double)a / b); // 3.4 (force double)"),
          ("Assignment operators", "int n = 10;\nn += 5;  // n = 15\nn -= 3;  // n = 12\nn *= 2;  // n = 24\nn /= 4;  // n = 6\nn %= 4;  // n = 2\nSystem.out.println(n); // 2\n\n// Pre/Post increment\nint x = 5;\nSystem.out.println(x++); // 5 (use then increment)\nSystem.out.println(x);   // 6\nSystem.out.println(++x); // 7 (increment then use)")]),
        ("Comparison & Logical Operators",
         "Comparison operators return boolean. Logical operators combine conditions. Use && (AND), || (OR), ! (NOT).",
         [("Comparison", "int x = 10, y = 20;\nSystem.out.println(x == y);  // false\nSystem.out.println(x != y);  // true\nSystem.out.println(x <  y);  // true\nSystem.out.println(x >= y);  // false\n\n// For objects, == checks reference!\nString a = new String(\"hi\");\nString b = new String(\"hi\");\nSystem.out.println(a == b);       // false (different objects)\nSystem.out.println(a.equals(b)); // true  (same content)"),
          ("Logical operators", "int age = 20;\nboolean hasID = true;\n\n// AND: both must be true\nif (age >= 18 && hasID) System.out.println(\"Entry allowed\");\n\n// OR: at least one true\nboolean isWeekend = true;\nif (isWeekend || age > 25) System.out.println(\"Enjoy!\");\n\n// NOT: flip the boolean\nSystem.out.println(!hasID);  // false")]),
        ("Bitwise & Ternary",
         "Bitwise operators work at binary level. Ternary is a compact if-else in one line.",
         [("Ternary operator", "int score = 75;\nString grade = (score >= 90) ? \"A\" :\n               (score >= 75) ? \"B\" :\n               (score >= 60) ? \"C\" : \"D\";\nSystem.out.println(\"Grade: \" + grade); // Grade: B"),
          ("Bitwise basics", "int a = 5;  // 0101\nint b = 3;  // 0011\nSystem.out.println(a & b);  // 1 (AND:  0001)\nSystem.out.println(a | b);  // 7 (OR:   0111)\nSystem.out.println(a ^ b);  // 6 (XOR:  0110)\nSystem.out.println(~a);     // -6 (NOT)\nSystem.out.println(a << 1); // 10 (left shift)\nSystem.out.println(a >> 1); // 2  (right shift)")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What is 17 / 5 in Java (int division)?", ["3.4", "3", "4", "2"], "3"),
        ("How to compare String content in Java?", ["==", ".equals()", ".compare()", "==="], ".equals()"),
        ("Ternary syntax is?", ["if(c) a else b", "c ? a : b", "c -> a : b", "c then a else b"], "c ? a : b"),
        ("What does % operator return?", ["Quotient", "Remainder", "Power", "Percentage"], "Remainder"),
        ("5 & 3 in binary equals?", ["7", "6", "1", "0"], "1"),
    ]),
    "hands_on": task("Grade Calculator", "Take score as input, determine grade using ternary: A>=90, B>=75, C>=60, else F.", "Use nested ternary or if-else. Print grade.", "import java.util.Scanner;\npublic class Main {\n    public static void main(String[] args) {\n        Scanner sc = new Scanner(System.in);\n        int score = sc.nextInt();\n        String grade = score>=90?\"A\":score>=75?\"B\":score>=60?\"C\":\"F\";\n        System.out.println(\"Grade: \" + grade);\n    }\n}"),
    "problem_solving": problems([
        ("Odd or Even", "Check if a number is odd or even using %.", "int n = 17;\nSystem.out.println(n % 2 == 0 ? \"Even\" : \"Odd\");"),
        ("Simple Interest", "Calculate SI: P=1000, R=5, T=2. SI = P*R*T/100.", "double p=1000, r=5, t=2;\ndouble si = p*r*t/100;\nSystem.out.printf(\"SI = %.2f%n\", si);"),
        ("Power without Math.pow", "Calculate 2^8 using bit shift.", "int result = 2 << 7;  // 2 * 2^7 = 256\nSystem.out.println(result);"),
    ])
}

# TOPIC 4: Control Flow
jv['java_control_flow'] = {
    "title": "Control Flow",
    "explanation": explanation("Control Flow", [
        ("if / else if / else",
         "Control flow determines which statements execute based on conditions. Java uses curly braces {} to define blocks.",
         [("If-else chain", "int temp = 35;\nif (temp > 40) {\n    System.out.println(\"Extreme heat!\");\n} else if (temp > 30) {\n    System.out.println(\"Hot day\");\n} else if (temp > 20) {\n    System.out.println(\"Warm\");\n} else {\n    System.out.println(\"Cool\");\n}"),
          ("Nested if", "int age = 20;\nboolean hasID = true;\n\nif (age >= 18) {\n    if (hasID) {\n        System.out.println(\"Access granted\");\n    } else {\n        System.out.println(\"Show ID first\");\n    }\n} else {\n    System.out.println(\"Too young\");\n}")]),
        ("switch Statement",
         "switch tests one variable against multiple constant values. Java 14+ supports switch expressions.",
         [("Classic switch", "int day = 3;\nswitch (day) {\n    case 1: System.out.println(\"Monday\");    break;\n    case 2: System.out.println(\"Tuesday\");   break;\n    case 3: System.out.println(\"Wednesday\"); break;\n    case 6:\n    case 7: System.out.println(\"Weekend!\");  break;\n    default: System.out.println(\"Weekday\");\n}"),
          ("Switch Expression (Java 14+)", "int month = 4;\nint days = switch (month) {\n    case 1,3,5,7,8,10,12 -> 31;\n    case 4,6,9,11        -> 30;\n    case 2               -> 28;\n    default              -> throw new IllegalArgumentException(\"Invalid\");\n};\nSystem.out.println(\"Days: \" + days); // Days: 30")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What happens if break is missing in switch?", ["Compile error", "Fall-through to next case", "Program stops", "Default runs"], "Fall-through to next case"),
        ("switch works with which types?", ["Only int", "int, char, String, enum", "float and double", "All types"], "int, char, String, enum"),
        ("Can if work without else?", ["No", "Yes", "Only with else if", "Only in methods"], "Yes"),
        ("Java 14 switch expression uses?", ["colon :", "arrow ->", "equals =", "pipe |"], "arrow ->"),
        ("if(1) in Java is?", ["Valid (1 is true)", "Invalid (must be boolean)", "Compilation warning", "Runtime error"], "Invalid (must be boolean)"),
    ]),
    "hands_on": task("Traffic Light", "Use switch to print action for traffic light color: red=STOP, yellow=SLOW, green=GO.", "Use switch on String color.", "String color = \"green\";\nswitch (color) {\n    case \"red\":    System.out.println(\"STOP!\");      break;\n    case \"yellow\": System.out.println(\"SLOW DOWN!\"); break;\n    case \"green\":  System.out.println(\"GO!\");        break;\n    default:       System.out.println(\"Invalid\");\n}"),
    "problem_solving": problems([
        ("Leap Year", "Check if year 2024 is a leap year. (div by 4 AND (not div by 100 OR div by 400)).", "int year = 2024;\nboolean leap = (year%4==0 && year%100!=0) || year%400==0;\nSystem.out.println(year + \" is \" + (leap?\"\":\"not \") + \"a leap year\");"),
        ("Calculator using switch", "Simple calculator: take two numbers and an operator (+,-,*,/) and print result.", "double a=10, b=3;\nchar op = '/';\nswitch(op) {\n    case '+': System.out.println(a+b); break;\n    case '-': System.out.println(a-b); break;\n    case '*': System.out.println(a*b); break;\n    case '/': System.out.println(b!=0?a/b:\"Error\"); break;\n}"),
        ("Max of Three", "Find maximum of three numbers using if-else.", "int a=45, b=78, c=23;\nint max = a;\nif(b>max) max=b;\nif(c>max) max=c;\nSystem.out.println(\"Max: \"+max);"),
    ])
}

# TOPIC 5: Loops
jv['java_loops'] = {
    "title": "Loops",
    "explanation": explanation("Loops", [
        ("for and while loops",
         "for loop: use when you know iteration count. while: use when condition-based. do-while: always runs at least once.",
         [("for loop", "// Basic for loop\nfor (int i = 1; i <= 5; i++) {\n    System.out.println(\"Count: \" + i);\n}\n\n// Reverse\nfor (int i = 10; i >= 1; i--) {\n    System.out.print(i + \" \");\n}\n// 10 9 8 7 6 5 4 3 2 1"),
          ("while & do-while", "// while\nint n = 1;\nwhile (n <= 5) {\n    System.out.println(n);\n    n++;\n}\n\n// do-while (runs at least once)\nint x = 10;\ndo {\n    System.out.println(\"x = \" + x);\n    x++;\n} while (x < 5); // condition false but body ran once!")]),
        ("Enhanced for & Nested loops",
         "Enhanced for-each loop iterates over arrays/collections cleanly. Nested loops handle 2D problems.",
         [("Enhanced for", "int[] nums = {10, 20, 30, 40, 50};\n\nfor (int num : nums) {\n    System.out.println(num);\n}\n\nString[] fruits = {\"Apple\", \"Banana\", \"Cherry\"};\nfor (String fruit : fruits) {\n    System.out.println(fruit);\n}"),
          ("Nested loops (pattern)", "// Print multiplication table of 3\nfor (int i = 1; i <= 10; i++) {\n    System.out.printf(\"3 x %2d = %2d%n\", i, 3*i);\n}\n\n// Star pattern\nfor (int i = 1; i <= 5; i++) {\n    for (int j = 1; j <= i; j++) {\n        System.out.print(\"* \");\n    }\n    System.out.println();\n}")]),
        ("break, continue, labels",
         "break exits the loop. continue skips current iteration. Labels allow break/continue on outer loops.",
         [("break & continue", "// break: exit loop\nfor (int i = 1; i <= 10; i++) {\n    if (i == 5) break;\n    System.out.print(i + \" \"); // 1 2 3 4\n}\n\n// continue: skip iteration\nfor (int i = 1; i <= 10; i++) {\n    if (i % 2 == 0) continue;\n    System.out.print(i + \" \"); // 1 3 5 7 9\n}"),
          ("Labeled break", "outer:\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        if (j == 1) break outer; // breaks BOTH loops\n        System.out.println(i + \",\" + j);\n    }\n}\n// Only prints: 0,0")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which loop always executes at least once?", ["for", "while", "do-while", "for-each"], "do-while"),
        ("Enhanced for-each works with?", ["Only arrays", "Arrays and Iterables (List, Set etc.)", "Only List", "Only int arrays"], "Arrays and Iterables (List, Set etc.)"),
        ("break in nested loop breaks?", ["All loops", "Only innermost loop (unless labeled)", "Outer loop only", "Program exits"], "Only innermost loop (unless labeled)"),
        ("Infinite loop is created by?", ["for(;;)", "while(true)", "Both A and B", "do-while(true)"], "Both A and B"),
        ("continue does what?", ["Exits loop", "Skips current iteration, goes to next", "Restarts loop", "Pauses loop"], "Skips current iteration, goes to next"),
    ]),
    "hands_on": task("Multiplication Table", "Print multiplication table of 7 from 1 to 12 using a for loop.", "Use printf for formatting.", "for (int i = 1; i <= 12; i++) {\n    System.out.printf(\"7 x %2d = %2d%n\", i, 7*i);\n}"),
    "problem_solving": problems([
        ("Sum 1 to N", "Calculate sum of numbers from 1 to 100.", "int sum = 0;\nfor (int i = 1; i <= 100; i++) sum += i;\nSystem.out.println(\"Sum = \" + sum);"),
        ("Reverse a Number", "Reverse digits of number 12345.", "int n = 12345, rev = 0;\nwhile (n != 0) {\n    rev = rev * 10 + n % 10;\n    n /= 10;\n}\nSystem.out.println(\"Reversed: \" + rev);"),
        ("Fibonacci Series", "Print first 10 Fibonacci numbers.", "int a=0, b=1;\nSystem.out.print(a + \" \" + b);\nfor (int i=2; i<10; i++) {\n    int c = a+b; System.out.print(\" \"+c);\n    a=b; b=c;\n}"),
    ])
}

print("Java Topics 1-5 done!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
