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
# KOTLIN TRACK
# ══════════════════════════════════════════════
kt_nodes_raw = [
    ("kt_basics",       "Kotlin Basics",        1),
    ("kt_variables",    "Variables & Types",    1),
    ("kt_operators",    "Operators",             1),
    ("kt_control",      "Control Flow",          1),
    ("kt_loops",        "Loops",                 1),
    ("kt_functions",    "Functions",             2),
    ("kt_arrays",       "Arrays & Lists",        2),
    ("kt_strings",      "Strings",               2),
    ("kt_nullsafety",   "Null Safety",           2),
    ("kt_oop",          "OOP Basics",            3),
    ("kt_inheritance",  "Inheritance",           3),
    ("kt_data_class",   "Data Classes",          3),
    ("kt_lambdas",      "Lambdas & HOF",         3),
    ("kt_collections",  "Collections",           4),
    ("kt_coroutines",   "Coroutines",            4),
    ("kt_extensions",   "Extension Functions",   4),
    ("kt_advanced",     "Advanced Kotlin",       4),
    ("kt_interview",    "Kotlin Interview Guide",5),
]

kt_nodes = []
for i,(nid,title,phase) in enumerate(kt_nodes_raw):
    node = {"id":nid,"title":title,"x":1250 if i%2==0 else 1530,"y":150+i*160,
            "status":"available" if i==0 else "locked","phase":phase}
    if i>0: node["parent"] = kt_nodes_raw[i-1][0]
    kt_nodes.append(node)

kt = {}

kt["kt_basics"] = {
    "title": "Kotlin Basics",
    "explanation": explanation("Kotlin Basics", [
        ("What is Kotlin?",
         "Kotlin is a modern, statically-typed language by JetBrains. It runs on JVM (fully interoperable with Java), Android, and can compile to JavaScript or native code. Official language for Android since 2017.",
         [("Hello World", 'fun main() {\n    println("Hello, World!")        // auto newline\n    print("No newline ")             // no newline\n    println("Kotlin is concise!")\n}'),
          ("Kotlin vs Java", '// Java: System.out.println("Hi");\n// Kotlin: println("Hi")   <- much cleaner!\n\n// Kotlin: No semicolons needed!\n// Kotlin: Type inference (val x = 42 -> inferred as Int)\n// Kotlin: Null safety built in\n// Kotlin: Data classes, extension functions, coroutines')]),
        ("Running Kotlin",
         "Use IntelliJ IDEA, Android Studio, or the online Kotlin Playground at play.kotlinlang.org.",
         [("Program structure", '// File: Main.kt\n// No class needed for top-level main!\n\nfun main(args: Array<String>) {\n    val name = "Alice"\n    val age  = 25\n    println("Name: $name, Age: $age")\n    println("Next year: ${age + 1}")\n}'),
          ("String templates", 'val brand = "Kotlin"\nval ver   = 1.9\n\nprintln("Using $brand version $ver")\nprintln("${brand.length} chars in name")\nprintln("${if (ver > 1.5) "Modern" else "Old"}")')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Kotlin was created by?", ["Google", "JetBrains", "Oracle", "Apple"], "JetBrains"),
        ("Kotlin uses semicolons?", ["Always", "Sometimes", "Never (optional)", "Only in loops"], "Never (optional)"),
        ("String template syntax?", ["#{var}", "${var}", "%(var)", "&{var}"], "${var}"),
        ("Kotlin is official language for?", ["iOS", "Android", "Windows apps", "Web apps only"], "Android"),
        ("println() in Kotlin is equivalent to?", ["System.out.print()", "System.out.println()", "Console.log()", "printf()"], "System.out.println()"),
    ]),
    "hands_on": task("Intro Program", "Write a Kotlin program that prints your name, age, and a fun fact using string templates.", "Use val for name and age. Use $name inside println.", 'fun main() {\n    val name = "Alice"\n    val age  = 20\n    val city = "Chennai"\n    println("Name: $name")\n    println("Age:  $age")\n    println("City: $city")\n    println("In 5 years I will be ${age + 5}")\n}'),
    "problem_solving": problems([
        ("Quadratic Formula", "Calculate discriminant of ax²+bx+c=0 for a=1,b=-5,c=6.", 'fun main(){\n    val a=1.0;val b=-5.0;val c=6.0\n    val d=b*b-4*a*c\n    println("Discriminant: $d")\n    if(d>=0) println("Roots: ${(-b+Math.sqrt(d))/(2*a)}, ${(-b-Math.sqrt(d))/(2*a)}")\n}'),
        ("Greet User", "Read name with readLine(), greet them.", 'fun main(){\n    print("Enter name: ")\n    val name=readLine()??"Guest"\n    println("Hello, $name!")\n}'),
        ("Circle Area", "Print area of circle with radius 7.", 'import kotlin.math.PI\nfun main(){\n    val r=7.0\n    println("Area: ${PI*r*r}")\n}'),
    ])
}

kt["kt_variables"] = {
    "title": "Variables & Data Types",
    "explanation": explanation("Variables & Data Types", [
        ("val vs var",
         "<b>val</b>: immutable (like Java final, JS const) — preferred by default. <b>var</b>: mutable. Kotlin infers types automatically.",
         [("val and var", 'val name = "Alice"    // immutable — cannot reassign\nvar score = 0         // mutable — can change\nscore = 100           // OK\n// name = "Bob"       // ERROR! val is final\n\n// Explicit type annotation\nval pi: Double = 3.14159\nvar count: Int    = 0\nval active: Boolean = true'),
          ("All basic types", '// Numbers (no primitives — all are objects)\nval byte:    Byte    = 127\nval short:   Short   = 32767\nval int:     Int     = 2_147_483_647  // underscore for readability\nval long:    Long    = 9_999_999_999L\nval float:   Float   = 3.14f\nval double:  Double  = 3.14159265\nval char:    Char    = \'A\'\nval bool:    Boolean = true\nval str:     String  = "Kotlin"\n\nprintln(int.javaClass)  // int (JVM)'),
          ]),
        ("Type Conversion",
         "Kotlin does NOT allow implicit numeric conversion. Use explicit .toInt(), .toDouble() etc.",
         [("Explicit conversion", 'val i: Int = 42\nval d: Double = i.toDouble()  // must be explicit!\nval s: String = i.toString()\nval b: Long   = i.toLong()\n\n// String to number\nval n = "123".toInt()\nval f = "3.14".toFloat()\n\n// Safe: returns null if fails\nval safe = "abc".toIntOrNull()  // null (no exception!)\nprintln(safe ?: "Parse failed")'),
          ("Range check", 'val x = 15\nif (x in 1..20)  println("In range 1-20")\nif (x !in 5..10) println("NOT in 5-10")\n\n// Ranges\nval range = 1..10          // inclusive\nval until = 1 until 10     // 1..9\nval step  = 1..20 step 2   // 1,3,5...19'),
          ]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("val in Kotlin is?", ["Mutable variable", "Immutable variable (like final)", "Constant only", "Global variable"], "Immutable variable (like final)"),
        ("Kotlin allows implicit int→double?", ["Yes", "No — must use .toDouble()", "Sometimes", "Only in expressions"], "No — must use .toDouble()"),
        ("'abc'.toIntOrNull() returns?", ["Exception", "0", "null", "-1"], "null"),
        ("2_000_000 in Kotlin means?", ["2 to 6", "Syntax error", "2000000 (underscore for readability)", "2 million range"], "2000000 (underscore for readability)"),
        ("x in 1..10 checks?", ["x > 1 and x < 10", "x >= 1 and x <= 10", "x == 1 or x == 10", "Syntax error"], "x >= 1 and x <= 10"),
    ]),
    "hands_on": task("Temperature Converter", "Create val for Celsius. Convert to Fahrenheit and Kelvin. Print all using string templates.", "F = C*9/5+32, K = C+273.15", 'fun main() {\n    val celsius = 100.0\n    val fahrenheit = celsius * 9/5 + 32\n    val kelvin     = celsius + 273.15\n    println("Celsius:    $celsius °C")\n    println("Fahrenheit: $fahrenheit °F")\n    println("Kelvin:     $kelvin K")\n}'),
    "problem_solving": problems([
        ("Safe Parse", "Read a string, safely parse to Int, default to 0 if invalid.", 'val input = "abc"\nval num = input.toIntOrNull() ?: 0\nprintln("Number: $num")'),
        ("Range check", "Check if score=72 is in A(90-100), B(75-89), C(60-74).", 'val score=72\nval grade=when(score){\n    in 90..100->"A"\n    in 75..89->"B"\n    in 60..74->"C"\n    else->"F"\n}\nprintln("Grade: $grade")'),
        ("Max of three", "Find max of three numbers using maxOf().", 'val a=45;val b=78;val c=23\nprintln("Max: ${maxOf(a,b,c)}")'),
    ])
}

kt["kt_operators"] = {
    "title": "Operators",
    "explanation": explanation("Operators", [
        ("Arithmetic & Comparison",
         "Kotlin operators are similar to Java/C#. All comparison operators return Boolean.",
         [("Arithmetic", 'val a=17; val b=5\nprintln(a+b)   // 22\nprintln(a-b)   // 12\nprintln(a*b)   // 85\nprintln(a/b)   // 3  (Int division)\nprintln(a%b)   // 2\nprintln(a.toDouble()/b) // 3.4\n\n// Power\nimport kotlin.math.pow\nprintln(2.0.pow(10))  // 1024.0'),
          ("Elvis & safe call", 'val name: String? = null\n\n// ?: Elvis operator — fallback if null\nval display = name ?: "Anonymous"\nprintln(display)  // Anonymous\n\n// Safe call ?. — null-safe access\nprintln(name?.length)   // null (no crash!)\nprintln(name?.uppercase()) // null')]),
        ("when Expression",
         "when is Kotlin's powerful switch replacement. It can match values, ranges, types — and returns a value.",
         [("when as expression", 'val score = 82\nval grade = when {\n    score >= 90 -> "A"\n    score >= 75 -> "B"\n    score >= 60 -> "C"\n    else        -> "F"\n}\nprintln("Grade: $grade")'),
          ("when with types", 'fun describe(obj: Any): String = when (obj) {\n    is Int    -> "Integer: $obj"\n    is String -> "String of len ${obj.length}"\n    is List<*>-> "List of ${obj.size} items"\n    else      -> "Unknown"\n}\nprintln(describe(42))\nprintln(describe("Hello"))\nprintln(describe(listOf(1,2,3)))')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Elvis operator ?: returns?", ["Left if null", "Right if left is null", "Always right", "Boolean"], "Right if left is null"),
        ("what does ?. mean?", ["Ternary operator", "Safe call — returns null if object is null", "Optional parameter", "Nullable declaration"], "Safe call — returns null if object is null"),
        ("when replaces what in Kotlin?", ["if-else", "try-catch", "switch-case", "for loop"], "switch-case"),
        ("is keyword in Kotlin checks?", ["Equality", "Type (instanceof in Java)", "Null", "Range"], "Type (instanceof in Java)"),
        ("Kotlin's === checks?", ["Value equality", "Structural equality", "Reference equality", "Type equality"], "Reference equality"),
    ]),
    "hands_on": task("Grade Classifier", "Use when expression to classify a score into grade. Also print if it's a pass (>=60).", "Use when { score >= 90 -> ... } without subject.", 'fun main(){\n    val score=77\n    val grade=when{\n        score>=90->"A - Excellent"\n        score>=75->"B - Good"\n        score>=60->"C - Average"\n        else->"F - Fail"\n    }\n    println("Score: $score")\n    println("Grade: $grade")\n    println(if(score>=60)"PASS" else "FAIL")\n}'),
    "problem_solving": problems([
        ("Type describer", "Write describe(Any) using when to print type.", 'fun describe(o:Any)=when(o){\n    is Int->"Int: $o"\n    is String->"String: $o"\n    is Boolean->"Bool: $o"\n    else->"Other"\n}\nprintln(describe(42))\nprintln(describe("Hi"))'),
        ("Seasonal greeting", "Given month 1-12, print season using when.", 'val m=7\nval season=when(m){\n    in 3..5->"Spring"\n    in 6..8->"Summer"\n    in 9..11->"Autumn"\n    else->"Winter"\n}\nprintln(season)'),
        ("BMI category", "Classify BMI using when ranges.", 'val bmi=22.5\nval cat=when{\n    bmi<18.5->"Underweight"\n    bmi<25.0->"Normal"\n    bmi<30.0->"Overweight"\n    else->"Obese"\n}\nprintln("BMI: $bmi -> $cat")'),
    ])
}

kt["kt_control"] = {
    "title": "Control Flow",
    "explanation": explanation("Control Flow", [
        ("if as expression & when",
         "In Kotlin, if and when are EXPRESSIONS — they return a value! This eliminates ternary operator need.",
         [("if expression", 'val a = 10; val b = 20\n\n// if as expression (replaces ternary!)\nval max = if (a > b) a else b\nprintln("Max: $max")  // 20\n\n// Multi-line if expression\nval msg = if (a > 0) {\n    println("Positive")\n    "Positive"   // last line = return value\n} else {\n    "Non-positive"\n}\nprintln(msg)'),
          ("when expression deep", 'fun classifyNumber(n: Int): String = when {\n    n < 0    -> "Negative"\n    n == 0   -> "Zero"\n    n in 1..9 -> "Single digit"\n    n in 10..99 -> "Double digit"\n    else     -> "Large number"\n}\n\nlistOf(-5, 0, 7, 42, 1000).forEach {\n    println("$it -> ${classifyNumber(it)}")\n}')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("In Kotlin, if is?", ["Only a statement", "An expression that returns a value", "A function", "A keyword only"], "An expression that returns a value"),
        ("val x = if(a>b) a else b is?", ["Invalid", "Valid — x gets max value", "Only works with var", "Needs semicolon"], "Valid — x gets max value"),
        ("when without argument matches?", ["First case always", "Conditions (like if-else chain)", "Variable types only", "Nothing"], "Conditions (like if-else chain)"),
        ("Does Kotlin have ternary operator ?:", ["Yes", "No — use if-else expression instead", "Only for nulls", "Only in Java interop"], "No — use if-else expression instead"),
        ("Kotlin when can match?", ["Only integers", "Values, ranges, types, conditions", "Only strings", "Only booleans"], "Values, ranges, types, conditions"),
    ]),
    "hands_on": task("Number Classifier", "Take a number, use when expression to classify and print its type and category.", "Return value from when expression and store in val.", 'fun main(){\n    val n=42\n    val result=when{\n        n<0->"Negative"\n        n==0->"Zero"\n        n%2==0->"Positive Even"\n        else->"Positive Odd"\n    }\n    println("$n is $result")\n    val abs=if(n<0)-n else n\n    println("Absolute value: $abs")\n}'),
    "problem_solving": problems([
        ("Max of three", "Use if expression to find max of three numbers.", 'fun max3(a:Int,b:Int,c:Int)=if(a>=b&&a>=c)a else if(b>=c)b else c\nprintln(max3(10,30,20))'),
        ("Voting check", "Check if age>=18, print eligibility using if expression.", 'val age=17\nval msg=if(age>=18)"Can vote!" else "Cannot vote, wait ${18-age} years"\nprintln(msg)'),
        ("Number sign", "Print positive/negative/zero using when.", 'val n=-7\nprintln(when{ n>0->"Positive"; n<0->"Negative"; else->"Zero" })'),
    ])
}

kt["kt_loops"] = {
    "title": "Loops",
    "explanation": explanation("Loops", [
        ("for, while, repeat",
         "Kotlin's for loop iterates over ranges and collections. repeat(n) runs a block n times. while/do-while work as expected.",
         [("for with ranges", 'for (i in 1..5)       print("$i ")  // 1 2 3 4 5\nfor (i in 5 downTo 1) print("$i ")  // 5 4 3 2 1\nfor (i in 1..10 step 2) print("$i ") // 1 3 5 7 9\nfor (i in 1 until 5) print("$i ")  // 1 2 3 4\n\n// forEach on collection\nlistOf("a","b","c").forEach { println(it) }\n\n// forEachIndexed\nlistOf("X","Y","Z").forEachIndexed { i,v -> println("$i:$v") }'),
          ("repeat & while", '// repeat\nrepeat(3) { println("Hello #${it+1}") }\n\n// while\nvar n = 10\nwhile (n > 0) { print("$n "); n -= 3 }  // 10 7 4 1\n\n// do-while (runs at least once)\nvar x = 0\ndo { println("x=$x"); x++ } while (x < 3)')]),
        ("break, continue, labels",
         "Kotlin supports labeled break/continue to exit/skip outer loops.",
         [("break & continue", 'for (i in 1..10) {\n    if (i == 6) break     // stop at 6\n    if (i % 2 == 0) continue  // skip evens\n    print("$i ")  // 1 3 5\n}'),
          ("Labeled loops", 'outer@ for (i in 1..3) {\n    for (j in 1..3) {\n        if (j == 2) continue@outer  // skip rest of inner\n        println("$i,$j")\n    }\n}')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("1..5 in Kotlin is?", ["1 to 4", "1 to 5 inclusive", "1 to 5 exclusive", "Array of 5"], "1 to 5 inclusive"),
        ("1 until 5 generates?", ["1,2,3,4,5", "1,2,3,4", "2,3,4,5", "0,1,2,3,4"], "1,2,3,4"),
        ("repeat(3) { } runs how many times?", ["2", "3", "4", "0"], "3"),
        ("downTo creates?", ["Ascending range", "Descending range", "Random order", "Step range"], "Descending range"),
        ("forEachIndexed gives?", ["Value only", "Index only", "Both index and value", "Key-value pairs"], "Both index and value"),
    ]),
    "hands_on": task("Pattern Printer", "Print a right-angled star triangle with 5 rows using nested for loops.", "Outer loop for rows, inner for stars. Use print and println.", 'fun main(){\n    for(i in 1..5){\n        for(j in 1..i) print("* ")\n        println()\n    }\n}'),
    "problem_solving": problems([
        ("Sum 1 to N", "Calculate sum of 1 to 100 using for loop.", 'var sum=0\nfor(i in 1..100) sum+=i\nprintln("Sum: $sum")'),
        ("FizzBuzz", "Print 1-20: Fizz(3), Buzz(5), FizzBuzz(both).", 'for(i in 1..20){\n    println(when{\n        i%15==0->"FizzBuzz"\n        i%3==0->"Fizz"\n        i%5==0->"Buzz"\n        else->"$i"\n    })\n}'),
        ("Factorial", "Calculate 8! using repeat.", 'var fact=1L\nrepeat(8){i->fact*=(i+1)}\nprintln("8! = $fact")'),
    ])
}

# Topics 6-17 for Kotlin
kt_topic_codes = {
    "kt_functions": ('// Default & named args\nfun greet(name: String, msg: String = "Hello") =\n    "$msg, $name!"\n\nprintln(greet("Alice"))\nprintln(greet(name="Bob", msg="Hi"))\n\n// Single-expression function\nfun square(n: Int) = n * n\nprintln(square(7))  // 49\n\n// Vararg\nfun sum(vararg nums: Int) = nums.sum()\nprintln(sum(1,2,3,4,5))  // 15\n\n// Higher-order function\nfun operate(a:Int,b:Int,op:(Int,Int)->Int)=op(a,b)\nprintln(operate(10,3){x,y->x+y})  // 13', "Functions: default params, single-expr, vararg, HOF"),
    "kt_arrays": ('// Array\nval arr = intArrayOf(5,3,8,1,9)\narr.sort()\nprintln(arr.toList())  // [1,3,5,8,9]\n\n// List (immutable)\nval colors = listOf("red","green","blue")\nprintln(colors[1])  // green\n\n// MutableList\nval names = mutableListOf("Alice","Bob")\nnames.add("Carol")\nnames.remove("Bob")\nprintln(names)  // [Alice, Carol]\n\n// Map\nval scores = mapOf("Alice" to 90, "Bob" to 85)\nprintln(scores["Alice"])  // 90\n\nval mutableMap = mutableMapOf("x" to 1)\nmutableMap["y"] = 2\nprintln(mutableMap)', "Array, List, MutableList, Map"),
    "kt_strings": ('val s = "  Hello, Kotlin!  "\nprintln(s.trim())\nprintln(s.trim().uppercase())\nprintln(s.contains("Kotlin"))\nprintln(s.replace("Kotlin","World"))\nprintln(s.trim().split(" ").size)\n\n// Multi-line string (trimIndent)\nval json = """\n    {\n        "name": "Alice",\n        "age": 25\n    }\n""".trimIndent()\nprintln(json)\n\n// Reverse a string\nprintln("Kotlin".reversed())\nprintln("hello world".split(" ").joinToString(" "){it.replaceFirstChar{c->c.uppercase()}})', "String methods + multi-line + reverse"),
    "kt_nullsafety": ('// Kotlin prevents NullPointerException!\nvar name: String  = "Alice"   // non-nullable\nvar nick: String? = null       // nullable (? suffix)\n\n// Won\'t compile:\n// name = null   // ERROR!\n\n// Safe access\nprintln(nick?.length)          // null (no crash)\nprintln(nick?.uppercase())     // null\n\n// Elvis operator ?:\nval display = nick ?: "Anonymous"\nprintln(display)               // Anonymous\n\n// !! (force — throws NPE if null, avoid it)\n// println(nick!!)             // throws NPE!\n\n// let — run block only if not null\nnick?.let { println("Nick is: $it") }  // not printed\nname.let { println("Name is: $it") }   // Name is: Alice', "Null safety: ?, ?., ?:, !!"),
    "kt_oop": ('class Person(val name: String, var age: Int) {\n    // init block\n    init { require(age >= 0) { "Age must be positive" } }\n\n    // Property with getter\n    val isAdult: Boolean get() = age >= 18\n\n    // Method\n    fun introduce() = "Hi, I am $name, age $age"\n\n    // Companion object (like static)\n    companion object {\n        fun create(name: String) = Person(name, 0)\n    }\n}\n\nval p = Person("Alice", 25)\nprintln(p.introduce())\nprintln(p.isAdult)  // true\n\nval baby = Person.create("Bob")\nprintln(baby.age)   // 0', "Class, properties, companion object"),
    "kt_inheritance": ('open class Animal(val name: String) {\n    open fun sound() = "..."\n    override fun toString() = "$name says ${sound()}"\n}\n\nclass Dog(name: String) : Animal(name) {\n    override fun sound() = "Woof!"\n    fun fetch() = "$name fetches the ball!"\n}\n\nclass Cat(name: String) : Animal(name) {\n    override fun sound() = "Meow!"\n}\n\nval animals: List<Animal> = listOf(Dog("Rex"),Cat("Mimi"))\nanimals.forEach { println(it) }\n// Rex says Woof!\n// Mimi says Meow!', "open class, override, polymorphism"),
    "kt_data_class": ('// data class: auto-generates equals, hashCode, toString, copy\ndata class Student(val name: String, val gpa: Double, val year: Int)\n\nval s1 = Student("Alice", 3.8, 2)\nval s2 = s1.copy(name="Bob", gpa=3.5)  // copy with changes\n\nprintln(s1)          // Student(name=Alice, gpa=3.8, year=2)\nprintln(s2)          // Student(name=Bob, gpa=3.5, year=2)\nprintln(s1 == s2)    // false\nprintln(s1 == Student("Alice",3.8,2))  // true!\n\n// Destructuring\nval (name, gpa, year) = s1\nprintln("$name: $gpa in year $year")', "data class: toString, copy, equals, destructuring"),
    "kt_lambdas": ('// Lambda syntax\nval add: (Int,Int)->Int = { a,b -> a+b }\nprintln(add(3,4))  // 7\n\n// it — implicit param for single-arg lambda\nval double = { x: Int -> x*2 }\nlistOf(1,2,3,4,5).map(double).also { println(it) } // [2,4,6,8,10]\n\n// Trailing lambda\nlistOf(1,2,3,4,5)\n    .filter { it % 2 == 0 }    // [2,4]\n    .map    { it * it }         // [4,16]\n    .forEach{ println(it) }\n\n// Function references\nfun isEven(n:Int) = n%2==0\nlistOf(1,2,3,4).filter(::isEven).also{println(it)}', "Lambdas, it, trailing lambdas, function refs"),
    "kt_collections": ('val nums = listOf(3,1,4,1,5,9,2,6,5,3)\n\n// Filter, map, reduce\nval evens = nums.filter{it%2==0}\nval squares = nums.map{it*it}\nval sum = nums.reduce{acc,n->acc+n}\n\nprintln(evens)    // [4,2,6]\nprintln(sum)      // 39\n\n// Distinct, sorted, groupBy\nprintln(nums.distinct().sorted())\nprintln(nums.groupBy{it%2==0}.mapKeys{if(it.key)"even" else "odd"})\n\n// Zip, flatten, partition\nval (pass,fail) = nums.partition{it>=5}\nprintln("Pass: $pass")\nprintln("Fail: $fail")\n\nprintln(nums.count{it>3})\nprintln(nums.maxOrNull())', "filter, map, reduce, groupBy, partition"),
    "kt_coroutines": ('import kotlinx.coroutines.*\n\nfun main() = runBlocking {\n    println("Start")\n\n    // launch — fire and forget\n    launch {\n        delay(500L)  // non-blocking wait\n        println("Coroutine 1 done")\n    }\n\n    // async — returns Deferred (like Future)\n    val result = async {\n        delay(300L)\n        "Result from async"\n    }\n\n    println("Middle")  // prints before coroutines finish\n    println(result.await())  // waits for async result\n    delay(600L)  // wait for launch\n    println("End")\n}', "runBlocking, launch, async/await, delay"),
    "kt_extensions": ('// Extension functions — add methods to existing classes!\nfun String.isPalindrome() = this == this.reversed()\nfun Int.isEven() = this % 2 == 0\nfun List<Int>.average() = if(isEmpty()) 0.0 else sum().toDouble()/size\n\nprintln("racecar".isPalindrome())  // true\nprintln("hello".isPalindrome())    // false\nprintln(4.isEven())               // true\nprintln(listOf(1,2,3,4,5).average()) // 3.0\n\n// Extension property\nval String.wordCount: Int get() = trim().split("\\\\s+".toRegex()).size\nprintln("Hello World Kotlin".wordCount)  // 3', "Extension functions & properties"),
    "kt_advanced": ('// Sealed class — restricted class hierarchy\nsealed class Result<out T>\ndata class Success<T>(val data: T) : Result<T>()\ndata class Error(val msg: String) : Result<Nothing>()\n\nfun processResult(r: Result<Int>) = when(r) {\n    is Success -> "Got: ${r.data}"\n    is Error   -> "Error: ${r.msg}"\n}\n\nprintln(processResult(Success(42)))       // Got: 42\nprintln(processResult(Error("no data"))) // Error: no data\n\n// Object declaration (Singleton)\nobject Config {\n    const val VERSION = "1.0"\n    val port = 8080\n}\nprintln(Config.VERSION)\n\n// Inline function\ninline fun measure(block: () -> Unit): Long {\n    val start = System.currentTimeMillis()\n    block()\n    return System.currentTimeMillis() - start\n}', "Sealed class, object, inline functions"),
}

for nid, title, phase in kt_nodes_raw[5:]:
    if nid == "kt_interview":
        kt[nid] = {
            "title": "Kotlin Interview Guide",
            "explanation": "<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;'>Top Kotlin Interview Questions</h3><p style='color:#475569;margin-bottom:30px;'>Most asked Kotlin questions in Android/backend interviews — Google, JetBrains, Flipkart, Zomato, etc.</p>" +
                "".join([f"<div style='background:#f8fafc;border-left:4px solid #0ea5e9;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#0ea5e9;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
                for i,(q,a) in enumerate([
                    ("val vs var?","val is immutable (read-only after initialization), var is mutable. Prefer val for safety."),
                    ("What is null safety in Kotlin?","Kotlin eliminates NullPointerException by making null illegal by default. Use String? for nullable types, ?. for safe calls, ?: for fallback."),
                    ("What is a data class?","A class that auto-generates: toString, equals, hashCode, copy, componentN functions. Used for simple data holding."),
                    ("What are coroutines?","Lightweight concurrent units of execution. launch for fire-and-forget, async for returning Deferred result. Non-blocking alternative to threads."),
                    ("What is a sealed class?","A class with restricted subclass hierarchy — all subclasses must be in same file. Perfect for expressing restricted states (Result, NetworkState)."),
                    ("What is an extension function?","A function that adds behavior to existing classes without inheriting them. fun String.hello() = 'Hello $this'"),
                    ("What is the difference between List and MutableList?","List is read-only. MutableList supports add, remove, set. Both are interfaces backed by ArrayList internally."),
                    ("What is companion object?","Object inside a class that acts like static members in Java. Access via ClassName.member without needing an instance."),
                    ("What is a higher-order function?","A function that takes another function as parameter or returns a function. Enables functional programming patterns."),
                    ("Kotlin vs Java?","Kotlin: concise, null-safe, extension functions, coroutines, data classes, no semicolons. 100% interoperable with Java."),
                ])]) + "</div>",
            "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
        }
    elif nid in kt_topic_codes:
        code, lbl = kt_topic_codes[nid]
        kt[nid] = {
            "title": title,
            "explanation": explanation(title, [("Key Concepts", f"{title} is a powerful feature of Kotlin.", [(lbl, code)])]),
            "examples": [],
            "concept_quiz": quiz([
                (f"Is {title} unique to Kotlin?", ["Yes", "No, also in other languages", "Only in Android", "Only in Java"], "No, also in other languages"),
                ("Kotlin targets which platforms?", ["JVM only", "JVM, Android, JS, Native", "Android only", "iOS only"], "JVM, Android, JS, Native"),
            ]),
            "hands_on": task(f"Practice {title}", f"Write a Kotlin program applying {title} concepts.", "Refer to example above.", code),
            "problem_solving": problems([
                (f"{title} Example", f"Implement a working example of {title}.", code),
                ("Fibonacci", "Print first 8 Fibonacci numbers.", 'var a=0;var b=1\nrepeat(8){print("$a ");val c=a+b;a=b;b=c}'),
            ])
        }

data['kotlin'] = {"title":"Kotlin - Beginner to Advanced","description":"Master Kotlin for Android, JVM, and backend with coroutines, null safety, and modern features.","nodes":kt_nodes,"content":kt}
print(f"Kotlin track: {len(kt_nodes)} nodes")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path,'w',encoding='utf-8') as f: f.write(new_text)
print("Saved!")
