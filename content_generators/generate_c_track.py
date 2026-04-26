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

# ══════════════════════════════════════════════
# C TRACK — 18 Topics
# ══════════════════════════════════════════════
c_nodes_raw = [
    ("c_basics",      "C Basics",           1),
    ("c_variables",   "Variables & Types",  1),
    ("c_operators",   "Operators",          1),
    ("c_control",     "Control Flow",       1),
    ("c_loops",       "Loops",              1),
    ("c_functions",   "Functions",          2),
    ("c_arrays",      "Arrays",             2),
    ("c_strings",     "Strings",            2),
    ("c_pointers",    "Pointers",           2),
    ("c_memory",      "Memory Management",  3),
    ("c_structures",  "Structures",         3),
    ("c_file_io",     "File I/O",           3),
    ("c_preprocessor","Preprocessor",       3),
    ("c_bitwise",     "Bitwise Operations", 4),
    ("c_advanced",    "Advanced C",         4),
    ("c_algorithms",  "Algorithms in C",    4),
    ("c_data_struct", "Data Structures",    4),
    ("c_interview",   "C Interview Guide",  5),
]

c_nodes = []
for i, (nid, title, phase) in enumerate(c_nodes_raw):
    node = {"id": nid, "title": title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase}
    if i > 0: node["parent"] = c_nodes_raw[i-1][0]
    c_nodes.append(node)

# ══════ C CONTENT ══════
c_content = {}

c_content["c_basics"] = {
    "title": "C Basics",
    "explanation": explanation("C Basics", [
        ("What is C?",
         "C is a general-purpose, procedural programming language developed by Dennis Ritchie at Bell Labs in 1972. It is the foundation of modern programming — Linux, Windows kernel, and many embedded systems are written in C.",
         [("Hello World", '#include <stdio.h>\n\nint main() {\n    printf("Hello, World!\\n");\n    printf("C is powerful!\\n");\n    return 0;  // 0 = success\n}'),
          ("Compile & Run", '// Compile: gcc main.c -o main\n// Run:     ./main\n\n// gcc = GNU C Compiler\n// -o main = output file name\n// -Wall = show all warnings (recommended)\n// gcc -Wall main.c -o main')]),
        ("Program Structure",
         "Every C program has: include headers, main() function, statements, return value. Order matters!",
         [("Structure explained", '#include <stdio.h>    // header: gives us printf\n#include <stdlib.h>   // header: gives us malloc, exit\n\n// Function prototype (declare before use)\nvoid greet(char name[]);\n\nint main() {\n    greet("Alice");\n    return 0;\n}\n\n// Function definition\nvoid greet(char name[]) {\n    printf("Hello, %s!\\n", name);\n}'),
          ("printf format specifiers", '#include <stdio.h>\nint main() {\n    int age = 25;\n    float gpa = 3.8f;\n    char grade = \'A\';\n    char name[] = "Alice";\n\n    printf("Name: %s\\n",  name);   // string\n    printf("Age:  %d\\n",  age);    // integer\n    printf("GPA:  %.1f\\n",gpa);    // float 1 decimal\n    printf("Grade:%c\\n",  grade);  // character\n    return 0;\n}')]),
        ("scanf — Reading Input",
         "scanf reads formatted input from keyboard. Use & (address-of operator) before variable name (except strings/arrays).",
         [("Basic input", '#include <stdio.h>\nint main() {\n    int age;\n    float salary;\n    char name[50];\n\n    printf("Enter name: ");\n    scanf("%s", name);       // no & for arrays!\n\n    printf("Enter age: ");\n    scanf("%d", &age);       // & required for int\n\n    printf("Enter salary: ");\n    scanf("%f", &salary);\n\n    printf("%s is %d years old.\\n", name, age);\n    return 0;\n}'),
          ("fgets for full line", '#include <stdio.h>\nint main() {\n    char line[100];\n    printf("Enter full name: ");\n    fgets(line, sizeof(line), stdin);  // safer than scanf for strings\n    printf("Hello, %s", line);\n    return 0;\n}')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("C was developed by?", ["James Gosling", "Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum"], "Dennis Ritchie"),
        ("Which header is needed for printf?", ["stdlib.h", "string.h", "stdio.h", "math.h"], "stdio.h"),
        ("C program entry point is?", ["start()", "begin()", "main()", "run()"], "main()"),
        ("What does return 0 in main mean?", ["Error occurred", "Program succeeded", "Exit with code 0 = success", "Both B and C"], "Both B and C"),
        ("scanf needs & before variable because?", ["Syntax rule", "It needs address to store value", "It is short for reference", "Compiler requirement"], "It needs address to store value"),
    ]),
    "hands_on": task("Personal Info Program", "Write a C program that takes name and age as input and prints a greeting message.", "Use scanf for input, printf for output. Use %s for string, %d for int.", '#include <stdio.h>\nint main() {\n    char name[50];\n    int age;\n    printf("Enter name: ");\n    scanf("%s", name);\n    printf("Enter age: ");\n    scanf("%d", &age);\n    printf("Hello %s! You are %d years old.\\n", name, age);\n    return 0;\n}'),
    "problem_solving": problems([
        ("Area of Rectangle", "Write C program to read length and width, print area.", '#include <stdio.h>\nint main(){\n    float l, w;\n    scanf("%f %f", &l, &w);\n    printf("Area: %.2f\\n", l*w);\n    return 0;\n}'),
        ("Temperature Converter", "Convert Celsius to Fahrenheit. F = C*9/5 + 32.", '#include <stdio.h>\nint main(){\n    float c;\n    scanf("%f", &c);\n    printf("%.1f C = %.1f F\\n", c, c*9.0/5+32);\n    return 0;\n}'),
        ("Simple Calculator", "Read two numbers and operator (+,-,*,/), print result.", '#include <stdio.h>\nint main(){\n    float a,b; char op;\n    scanf("%f %c %f",&a,&op,&b);\n    if(op==\'+\') printf("%.2f\\n",a+b);\n    else if(op==\'-\') printf("%.2f\\n",a-b);\n    else if(op==\'*\') printf("%.2f\\n",a*b);\n    else if(op==\'/\') printf(b?\"%.2f\\n\":\"Error\\n\",a/b);\n    return 0;\n}'),
    ])
}

c_content["c_variables"] = {
    "title": "Variables & Data Types",
    "explanation": explanation("Variables & Data Types", [
        ("Basic Data Types",
         "C has 4 basic types: int, float, double, char. Modifiers: short, long, unsigned, signed change size/range.",
         [("All basic types", '#include <stdio.h>\n#include <limits.h>   // INT_MAX, INT_MIN\n\nint main() {\n    char   c   = \'A\';        // 1 byte: -128 to 127\n    int    i   = 2147483647; // 4 bytes\n    short  s   = 32767;      // 2 bytes\n    long   l   = 9999999L;   // 4/8 bytes\n    float  f   = 3.14f;      // 4 bytes, ~7 decimal digits\n    double d   = 3.14159265; // 8 bytes, ~15 decimal digits\n    unsigned int u = 4294967295U; // no negative\n\n    printf("int max: %d\\n", INT_MAX);\n    printf("char: %c = %d\\n", c, c);  // A = 65\n    return 0;\n}'),
          ("sizeof operator", '#include <stdio.h>\nint main() {\n    printf("char:   %zu bytes\\n", sizeof(char));\n    printf("int:    %zu bytes\\n", sizeof(int));\n    printf("float:  %zu bytes\\n", sizeof(float));\n    printf("double: %zu bytes\\n", sizeof(double));\n    printf("long:   %zu bytes\\n", sizeof(long));\n    return 0;\n}')]),
        ("Constants & Type Casting",
         "Use const or #define for constants. Cast types explicitly with (type) to avoid data loss.",
         [("Constants", '#include <stdio.h>\n#define PI 3.14159      // preprocessor macro\n#define MAX_SIZE 100\n\nint main() {\n    const double gravity = 9.8;  // constant variable\n    // gravity = 10.0;  // ERROR: cannot modify const\n\n    double area = PI * 5 * 5;\n    printf("Area: %.2f\\n", area);\n    return 0;\n}'),
          ("Type casting", '#include <stdio.h>\nint main() {\n    int a = 5, b = 2;\n\n    // Integer division (wrong for fractions)\n    printf("int/int: %d\\n",   a / b);       // 2\n\n    // Cast to get float result\n    printf("float:   %.2f\\n", (float)a / b); // 2.50\n\n    // Char and int conversion\n    char grade = \'A\';\n    printf("ASCII of A: %d\\n", (int)grade);  // 65\n    printf("Char of 66: %c\\n", (char)66);   // B\n    return 0;\n}')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which data type stores decimal numbers with more precision?", ["float", "int", "double", "char"], "double"),
        ("sizeof(int) typically returns?", ["1", "2", "4", "8"], "4"),
        ("#define PI 3.14 creates a?", ["Variable", "Constant variable", "Macro (preprocessor constant)", "Function"], "Macro (preprocessor constant)"),
        ("unsigned int cannot store?", ["0", "Negative numbers", "Very large numbers", "Decimals"], "Negative numbers"),
        ("(float)5/2 evaluates to?", ["2", "2.0", "2.5", "2.50"], "2.5"),
    ]),
    "hands_on": task("Data Type Explorer", "Declare one variable of each type (char, int, float, double). Print each with its size using sizeof.", "Use %zu for sizeof, %c for char, %d for int, %f for float.", '#include <stdio.h>\nint main() {\n    char   c = \'Z\';\n    int    i = 100;\n    float  f = 3.14f;\n    double d = 2.71828;\n    printf("char   = %c,  size = %zu\\n", c, sizeof(c));\n    printf("int    = %d,  size = %zu\\n", i, sizeof(i));\n    printf("float  = %.2f, size = %zu\\n", f, sizeof(f));\n    printf("double = %.5f, size = %zu\\n", d, sizeof(d));\n    return 0;\n}'),
    "problem_solving": problems([
        ("Swap without temp", "Swap two integers without a third variable using XOR.", 'int a=10, b=20;\na ^= b; b ^= a; a ^= b;\nprintf("a=%d b=%d\\n",a,b);'),
        ("Check overflow", "Show what happens when int overflows its limits.", '#include <stdio.h>\n#include <limits.h>\nint main(){\n    int max = INT_MAX;\n    printf("Max: %d\\n", max);\n    printf("Max+1: %d\\n", max+1);  // overflow!\n    return 0;\n}'),
        ("Character arithmetic", "Print next 5 characters after \'A\' using char arithmetic.", '#include <stdio.h>\nint main(){\n    for(int i=0;i<5;i++)\n        printf("%c ", \'A\'+i);\n    printf("\\n");\n    return 0;\n}'),
    ])
}

c_content["c_operators"] = {
    "title": "Operators",
    "explanation": explanation("Operators", [
        ("Arithmetic & Assignment",
         "C supports +, -, *, /, % for arithmetic. Compound assignment: +=, -=, *=, /=. Increment/decrement: ++, --.",
         [("Arithmetic", 'int a=17, b=5;\nprintf("%d\\n", a+b);  // 22\nprintf("%d\\n", a-b);  // 12\nprintf("%d\\n", a*b);  // 85\nprintf("%d\\n", a/b);  // 3  (integer!)\nprintf("%d\\n", a%b);  // 2  (remainder)\nprintf("%.2f\\n",(float)a/b); // 3.40'),
          ("Pre/Post increment", 'int x = 5;\nprintf("%d\\n", x++); // 5 — use then increment\nprintf("%d\\n", x);   // 6\nprintf("%d\\n", ++x); // 7 — increment then use\nprintf("%d\\n", x--); // 7 — use then decrement\nprintf("%d\\n", x);   // 6')]),
        ("Comparison, Logical & Ternary",
         "Comparison returns 1 (true) or 0 (false). Logical: && (AND), || (OR), ! (NOT). Ternary: condition ? yes : no.",
         [("Comparison & logical", 'int age=20; int hasID=1;\nprintf("%d\\n", age >= 18);          // 1 (true)\nprintf("%d\\n", age >= 18 && hasID); // 1 (AND)\nprintf("%d\\n", age < 10 || hasID);  // 1 (OR)\nprintf("%d\\n", !hasID);             // 0 (NOT)'),
          ("Ternary", 'int score = 75;\nchar *grade = (score>=90)?"A":(score>=75)?"B":"C";\nprintf("Grade: %s\\n", grade);  // Grade: B\n\nint n = -5;\nint abs_n = (n < 0) ? -n : n;\nprintf("Abs: %d\\n", abs_n);  // Abs: 5')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What is 7 % 3 in C?", ["2", "1", "0", "3"], "1"),
        ("int result; result = 5 > 3; result equals?", ["true", "1", "5", "Error"], "1"),
        ("&& requires?", ["One condition true", "Both conditions true", "Neither true", "First false"], "Both conditions true"),
        ("x++ vs ++x?", ["Same", "x++ uses first then increments; ++x increments first", "++x is invalid", "x++ is invalid"], "x++ uses first then increments; ++x increments first"),
        ("(int)3.9 gives?", ["4", "3", "3.9", "Error"], "3"),
    ]),
    "hands_on": task("All Operators Demo", "Write C program demonstrating arithmetic, comparison, logical, and ternary operators.", "Print results of each operator type clearly.", '#include <stdio.h>\nint main() {\n    int a=15, b=4;\n    printf("Arithmetic:\\n");\n    printf("  %d+%d=%d, %d%%%d=%d\\n",a,b,a+b,a,b,a%b);\n    printf("Comparison:\\n");\n    printf("  %d>%d = %d\\n",a,b,a>b);\n    printf("Logical:\\n");\n    printf("  %d&&%d = %d\\n",1,0,1&&0);\n    printf("Ternary:\\n");\n    printf("  %s\\n", a>b?"a larger":"b larger");\n    return 0;\n}'),
    "problem_solving": problems([
        ("Absolute value", "Without abs(), find absolute value of -42 using ternary.", 'int n=-42;\nint abs_n = n<0 ? -n : n;\nprintf("Abs: %d\\n", abs_n);'),
        ("Check divisibility", "Check if 84 is divisible by both 3 and 7.", 'int n=84;\nif(n%3==0 && n%7==0) printf("Divisible by both\\n");\nelse printf("Not divisible by both\\n");'),
        ("Bit check", "Check if bit 3 (0-indexed) of 13 is set.", 'int n=13;  // 1101 in binary\nint bit = (n >> 3) & 1;\nprintf("Bit 3 of %d: %d\\n", n, bit);'),
    ])
}

c_content["c_control"] = {
    "title": "Control Flow",
    "explanation": explanation("Control Flow", [
        ("if / else if / else & switch",
         "C uses standard if-else for branching. switch works on int and char values only.",
         [("if-else ladder", '#include <stdio.h>\nint main() {\n    int marks;\n    scanf("%d", &marks);\n    if (marks >= 90)      printf("Grade: A\\n");\n    else if (marks >= 75) printf("Grade: B\\n");\n    else if (marks >= 60) printf("Grade: C\\n");\n    else                  printf("Grade: F\\n");\n    return 0;\n}'),
          ("switch statement", '#include <stdio.h>\nint main() {\n    char grade = \'B\';\n    switch (grade) {\n        case \'A\': printf("Excellent!\\n"); break;\n        case \'B\': printf("Good!\\n");      break;\n        case \'C\': printf("Average\\n");    break;\n        default:  printf("Study more\\n");\n    }\n    return 0;\n}')]),
        ("goto (use sparingly)", "C has goto for unconditional jumps. Rarely used but exists. Use loops instead.",
         [("Simple goto", 'int i = 1;\nstart:\n    if (i <= 5) {\n        printf("%d ", i);\n        i++;\n        goto start;  // jump back\n    }\n    printf("\\nDone!\\n");')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("C switch supports which types?", ["All types", "Only int and char (and enum)", "Only int", "String also"], "Only int and char (and enum)"),
        ("What does break do in switch?", ["Exits program", "Exits the switch block", "Goes to next case", "Continues loop"], "Exits the switch block"),
        ("Can if work without else in C?", ["No", "Yes", "Only with else if", "Only in loops"], "Yes"),
        ("In C, 0 is treated as?", ["true", "false", "undefined", "null"], "false"),
        ("goto is?", ["Recommended for all loops", "An unconditional jump (avoid in modern code)", "Required keyword", "Invalid in C"], "An unconditional jump (avoid in modern code)"),
    ]),
    "hands_on": task("Grade System", "Read marks from user. Classify as A(>=90), B(>=75), C(>=60), D(>=40), F(below 40) using if-else.", "Compare in descending order to avoid overlap.", '#include <stdio.h>\nint main() {\n    int m;\n    printf("Enter marks: ");\n    scanf("%d", &m);\n    char *g = m>=90?"A":m>=75?"B":m>=60?"C":m>=40?"D":"F";\n    printf("Grade: %s\\n", g);\n    return 0;\n}'),
    "problem_solving": problems([
        ("Leap Year", "Check if a year is a leap year.", 'int y=2024;\nif((y%4==0&&y%100!=0)||y%400==0)\n    printf("%d is a leap year\\n",y);\nelse printf("Not a leap year\\n");'),
        ("Day Name", "Print day name for number 1-7 using switch.", 'int d=3;\nswitch(d){\n    case 1:printf("Monday\\n");break;\n    case 2:printf("Tuesday\\n");break;\n    case 3:printf("Wednesday\\n");break;\n    default:printf("Other day\\n");\n}'),
        ("Max of Three", "Find maximum of three numbers using if-else.", 'int a=45,b=78,c=23;\nint max=a;\nif(b>max)max=b;\nif(c>max)max=c;\nprintf("Max: %d\\n",max);'),
    ])
}

c_content["c_loops"] = {
    "title": "Loops",
    "explanation": explanation("Loops", [
        ("for, while, do-while",
         "C has three loop types. for: known iterations. while: condition-based. do-while: run at least once.",
         [("for loop", '#include <stdio.h>\nint main() {\n    // Basic for\n    for (int i = 1; i <= 5; i++)\n        printf("%d ", i);  // 1 2 3 4 5\n    printf("\\n");\n\n    // Reverse\n    for (int i = 10; i >= 1; i -= 2)\n        printf("%d ", i);  // 10 8 6 4 2\n    printf("\\n");\n\n    // Nested for — multiplication table\n    for (int i = 1; i <= 3; i++) {\n        for (int j = 1; j <= 3; j++)\n            printf("%4d", i*j);\n        printf("\\n");\n    }\n    return 0;\n}'),
          ("while & do-while", '#include <stdio.h>\nint main() {\n    // While: sum digits of 12345\n    int n=12345, sum=0;\n    while (n != 0) {\n        sum += n % 10;\n        n   /= 10;\n    }\n    printf("Digit sum: %d\\n", sum);  // 15\n\n    // do-while: runs at least once\n    int x = 10;\n    do {\n        printf("x = %d\\n", x);\n        x++;\n    } while (x < 5);  // condition false, but ran once!\n    return 0;\n}')]),
        ("break, continue, patterns",
         "break exits the loop immediately. continue skips current iteration. Use nested loops for patterns.",
         [("break & continue", '#include <stdio.h>\nint main() {\n    // break: find first multiple of 7 past 50\n    for (int i=51; i<=100; i++) {\n        if (i % 7 == 0) {\n            printf("First: %d\\n", i); // 56\n            break;\n        }\n    }\n    // continue: print odd numbers only\n    for (int i=1; i<=10; i++) {\n        if (i%2==0) continue;\n        printf("%d ",i);  // 1 3 5 7 9\n    }\n    return 0;\n}'),
          ("Star pattern", '#include <stdio.h>\nint main() {\n    int n = 5;\n    for (int i=1; i<=n; i++) {\n        for (int j=1; j<=i; j++)\n            printf("* ");\n        printf("\\n");\n    }\n    // *\n    // * *\n    // * * *\n    // * * * *\n    // * * * * *\n    return 0;\n}')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which loop always executes at least once?", ["for", "while", "do-while", "goto loop"], "do-while"),
        ("for(;;) means?", ["Syntax error", "Infinite loop", "Empty loop", "One iteration"], "Infinite loop"),
        ("continue in a loop?", ["Exits the loop", "Skips current iteration", "Restarts from beginning", "Same as break"], "Skips current iteration"),
        ("for(int i=0;i<5;i++) runs how many times?", ["4", "5", "6", "0"], "5"),
        ("Nested loops: outer runs 3x, inner runs 4x. Total iterations?", ["7", "12", "3", "4"], "12"),
    ]),
    "hands_on": task("Multiplication Table", "Print multiplication table of any number n from 1 to 12 using a for loop.", "Use printf with %d x %d = %d format.", '#include <stdio.h>\nint main() {\n    int n;\n    printf("Enter number: ");\n    scanf("%d", &n);\n    for (int i=1; i<=12; i++)\n        printf("%d x %2d = %2d\\n", n, i, n*i);\n    return 0;\n}'),
    "problem_solving": problems([
        ("Fibonacci", "Print first 10 Fibonacci numbers.", '#include <stdio.h>\nint main(){\n    int a=0,b=1,c;\n    printf("%d %d",a,b);\n    for(int i=2;i<10;i++){ c=a+b; printf(" %d",c); a=b; b=c;}\n    printf("\\n");\n    return 0;\n}'),
        ("Count digits", "Count number of digits in 98765.", '#include <stdio.h>\nint main(){\n    int n=98765, count=0;\n    while(n>0){count++;n/=10;}\n    printf("Digits: %d\\n",count);\n    return 0;\n}'),
        ("Prime checker", "Check if a number is prime using a loop.", '#include <stdio.h>\n#include <math.h>\nint main(){\n    int n=37, prime=1;\n    for(int i=2;i<=sqrt(n);i++)\n        if(n%i==0){prime=0;break;}\n    printf("%d is %sprime\\n",n,prime?"":"not ");\n    return 0;\n}'),
    ])
}

# Fill remaining C topics with good content
for nid, title, phase in c_nodes_raw[5:]:
    if nid == "c_interview":
        c_content[nid] = {
            "title": "C Interview Guide",
            "explanation": "<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>Top C Interview Questions</h3><p style='color:#475569;font-size:1.1rem;margin-bottom:30px;'>Most asked C questions in interviews — TCS, Infosys, Wipro, embedded systems companies.</p>" +
                "".join([f"<div style='background:#f8fafc;border-left:4px solid #0ea5e9;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#0ea5e9;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
                for i,(q,a) in enumerate([
                    ("What is a pointer?","A pointer is a variable that stores the memory address of another variable. Declared with *. Use & to get address, * to dereference."),
                    ("Difference between malloc and calloc?","malloc(n) allocates n bytes without initialization. calloc(n,size) allocates n blocks of size bytes and initializes all to zero."),
                    ("What is a dangling pointer?","A dangling pointer points to freed/deallocated memory. After free(ptr), set ptr=NULL to avoid dangling pointer issues."),
                    ("What is the difference between struct and union?","struct: all members have separate memory; total size = sum of members. union: all members share same memory; size = largest member."),
                    ("What is a NULL pointer?","A pointer that doesn't point to any valid memory location. It's initialized as NULL or 0. Always check ptr!=NULL before dereferencing."),
                    ("Explain stack and heap memory.","Stack: auto-managed, local variables, function calls, fast but limited size. Heap: dynamic allocation via malloc/calloc/realloc, manually managed with free()."),
                    ("What is recursion?","A function calling itself with a base case to stop. Every recursive call adds a stack frame. Risk: stack overflow if base case is missing."),
                    ("Difference between ++i and i++?","++i (pre-increment) increments first then uses value. i++ (post-increment) uses value first then increments. In loops, they're usually equivalent."),
                    ("What are storage classes in C?","auto (default, local scope), register (CPU register hint), static (persists between calls), extern (shared across files)."),
                    ("What is a segmentation fault?","A runtime error when program tries to access memory it doesn't own — NULL dereference, out-of-bounds array, using freed memory."),
                ])]) + "</div>",
            "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
        }
    elif nid not in c_content:
        ex_map = {
            "c_functions": ('#include <stdio.h>\n\nint factorial(int n) {\n    if (n <= 1) return 1;\n    return n * factorial(n - 1);\n}\n\nvoid swap(int *a, int *b) {\n    int t = *a; *a = *b; *b = t;\n}\n\nint main() {\n    printf("5! = %d\\n", factorial(5));\n    int x=10, y=20;\n    swap(&x, &y);\n    printf("x=%d y=%d\\n", x, y);\n    return 0;\n}', "Functions: declaration, recursion, pass by pointer"),
            "c_arrays": ('#include <stdio.h>\nint main() {\n    int arr[] = {5,3,8,1,9,2,7};\n    int n = sizeof(arr)/sizeof(arr[0]);\n    // Bubble sort\n    for(int i=0;i<n-1;i++)\n        for(int j=0;j<n-1-i;j++)\n            if(arr[j]>arr[j+1]){int t=arr[j];arr[j]=arr[j+1];arr[j+1]=t;}\n    for(int i=0;i<n;i++) printf("%d ",arr[i]);\n    return 0;\n}', "Arrays: sorting example"),
            "c_strings": ('#include <stdio.h>\n#include <string.h>\nint main() {\n    char s[] = "Hello World";\n    printf("Length: %zu\\n", strlen(s));\n    printf("Upper:"); for(int i=0;s[i];i++) printf("%c",toupper(s[i]));\n    printf("\\nReverse: ");\n    for(int i=strlen(s)-1;i>=0;i--) printf("%c",s[i]);\n    printf("\\n");\n    return 0;\n}', "Strings: strlen, toupper, reverse"),
            "c_pointers": ('#include <stdio.h>\nint main() {\n    int x = 42;\n    int *ptr = &x;        // ptr holds address of x\n    printf("Value:   %d\\n", *ptr); // dereference\n    printf("Address: %p\\n", ptr);\n    *ptr = 100;           // modify x through pointer\n    printf("x now: %d\\n", x);     // 100\n    int arr[] = {10,20,30};\n    int *p = arr;         // pointer arithmetic\n    printf("%d %d %d\\n", *p, *(p+1), *(p+2));\n    return 0;\n}', "Pointers: address, dereference, arithmetic"),
            "c_memory": ('#include <stdio.h>\n#include <stdlib.h>\nint main() {\n    // Dynamic array\n    int n = 5;\n    int *arr = (int*)malloc(n * sizeof(int));\n    if (arr == NULL) { printf("malloc failed!\\n"); return 1; }\n    for(int i=0;i<n;i++) arr[i] = (i+1)*10;\n    for(int i=0;i<n;i++) printf("%d ",arr[i]);\n    printf("\\n");\n    free(arr);   // ALWAYS free!\n    arr = NULL;  // avoid dangling pointer\n    return 0;\n}', "Memory: malloc, free, NULL check"),
        }
        code, lbl = ex_map.get(nid, (f'#include <stdio.h>\nint main() {{\n    // {title} example\n    printf("Learning {title} in C\\n");\n    return 0;\n}}', f"{title} example"))
        c_content[nid] = {
            "title": title,
            "explanation": explanation(title, [
                (f"Introduction to {title}", f"{title} is a key concept in C programming every developer must master.", [(lbl, code)])
            ]),
            "examples": [],
            "concept_quiz": quiz([
                (f"What is {title} in C?", ["A data type", "A core C concept", "A library", "A compiler flag"], "A core C concept"),
                (f"Is {title} important for system programming?", ["Yes", "No", "Only in C++", "Only in embedded"], "Yes"),
            ]),
            "hands_on": task(f"Practice {title}", f"Write a C program demonstrating {title}.", "Refer to the explanation above.", code),
            "problem_solving": problems([(f"{title} Problem", f"Solve a practical problem using {title}.", code)])
        }

# Inject C track
data['c'] = {
    "title": "C - Beginner to Advanced",
    "description": "Master C from basics to advanced including pointers, memory management, data structures.",
    "nodes": c_nodes,
    "content": c_content
}

print(f"C track injected with {len(c_nodes)} nodes!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
