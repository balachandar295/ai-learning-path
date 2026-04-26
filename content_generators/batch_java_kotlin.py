
"""
Batch: Java + Kotlin
Fixes generic/template content with accurate, topic-specific textbook-quality explanations.
"""
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

FILEPATH = os.path.join(os.path.dirname(__file__), '..', 'core', 'static', 'tracks_data.js')

def make_topic(intro, subtopics, key_concepts, examples, quiz, hands_on=None, problems=None):
    s = {"introduction": intro, "subtopics": subtopics, "key_concepts": key_concepts, "examples": examples}
    return {
        "structured": s,
        "concept_quiz": quiz,
        "hands_on": hands_on or {"title": "Try it!", "description": "Practice the concept above.", "hint": "Use the examples as a guide.", "code": ""},
        "problem_solving": problems or []
    }

# ─────────────────────────────────────────────
# JAVA TOPICS (java_basics is the only generic one found)
# ─────────────────────────────────────────────
JAVA_FIXES = {
    "java_basics": make_topic(
        intro="""<p><strong>Java</strong> is a high-level, class-based, object-oriented programming language created by James Gosling at Sun Microsystems in 1995. Its famous motto — <em>"Write Once, Run Anywhere"</em> — is made possible by the <strong>Java Virtual Machine (JVM)</strong>. You compile your source code (<code>.java</code>) into platform-neutral <strong>bytecode</strong> (<code>.class</code>), which the JVM executes on any operating system. Java powers Android apps, enterprise backends (Spring Boot), big-data tools (Hadoop), and is one of the most popular languages in the world.</p>""",
        subtopics=[
            {"title": "Program Structure & the Main Method", "content": "<p>Every Java program lives inside a <strong>class</strong>. Execution begins at the special entry point <code>public static void main(String[] args)</code>. The keyword <code>public</code> lets the JVM call it from outside, <code>static</code> means no object is needed, <code>void</code> means it returns nothing, and <code>String[] args</code> captures command-line arguments.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;overflow-x:auto;'>public class Hello {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}</pre>"},
            {"title": "Strong Static Typing", "content": "<p>Java is <strong>statically typed</strong> — every variable must declare its type at compile time. Common types include <code>int</code>, <code>double</code>, <code>boolean</code>, <code>char</code>, and <code>String</code>. The compiler catches type mismatches <em>before</em> your program runs, preventing entire classes of runtime bugs.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>int age = 25;\ndouble salary = 45000.50;\nboolean isActive = true;\nString name = \"Alice\";</pre>"},
            {"title": "Compiling & Running Java", "content": "<p>The Java workflow has two distinct steps: <strong>compile</strong> then <strong>run</strong>. The <code>javac</code> compiler produces a <code>.class</code> bytecode file; the <code>java</code> command passes it to the JVM for execution.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>$ javac Hello.java   # produces Hello.class\n$ java Hello         # JVM executes bytecode</pre>"},
        ],
        key_concepts="<ul><li><strong>JVM (Java Virtual Machine)</strong> — executes bytecode, provides platform independence.</li><li><strong>JDK vs JRE</strong> — JDK = developer kit (includes compiler); JRE = runtime only.</li><li><strong>Garbage Collection</strong> — Java automatically manages memory; you don't call <code>free()</code>.</li><li><strong>Reference Types</strong> — Objects are accessed via references (pointers under the hood).</li><li><strong>Packages</strong> — Namespaces like <code>com.example.app</code> that organise classes.</li></ul>",
        examples=[
            {"title": "Hello World", "code": 'public class Hello {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}', "output": "Hello, World!", "explanation": "<p>The simplest Java program. <code>System.out.println</code> prints a line to the console.</p>"},
            {"title": "Variables & Arithmetic", "code": 'public class Arithmetic {\n    public static void main(String[] args) {\n        int a = 10, b = 3;\n        System.out.println("Sum: " + (a + b));\n        System.out.println("Quotient: " + (a / b));\n        System.out.println("Remainder: " + (a % b));\n    }\n}', "output": "Sum: 13\nQuotient: 3\nRemainder: 1", "explanation": "<p>Integer division truncates the decimal part. The <code>%</code> operator gives the remainder.</p>"},
        ],
        quiz=[
            {"q": "Which command compiles a Java source file?", "options": ["java", "javac", "jvm", "run"], "answer": "javac"},
            {"q": "What is the entry point of every Java program?", "options": ["start()", "run()", "main()", "init()"], "answer": "main()"},
            {"q": "Java bytecode is executed by the:", "options": ["OS kernel", "CPU directly", "JVM", "Browser"], "answer": "JVM"},
        ],
        hands_on={"title": "Your First Java Program", "description": "Write a Java class called 'Greeting' that prints your name and age on separate lines.", "hint": "Use System.out.println() twice. Declare a String variable for name and an int for age.", "code": 'public class Greeting {\n    public static void main(String[] args) {\n        String name = "Alice";\n        int age = 20;\n        System.out.println("Name: " + name);\n        System.out.println("Age: " + age);\n    }\n}'},
    ),
}

# ─────────────────────────────────────────────
# KOTLIN TOPICS (all 10 generic ones)
# ─────────────────────────────────────────────
KOTLIN_FIXES = {
    "kt_basics": make_topic(
        intro="""<p><strong>Kotlin</strong> is a modern, statically typed programming language developed by JetBrains and officially supported by Google for <strong>Android development</strong> since 2017. It compiles to JVM bytecode, JavaScript, and native binaries, making it truly multi-platform. Kotlin is designed to be 100% interoperable with Java — you can call Java libraries from Kotlin and vice versa — while offering a far more concise and expressive syntax. Its biggest wins over Java: no <code>NullPointerException</code> crashes by default, shorter boilerplate, and modern language features baked in.</p>""",
        subtopics=[
            {"title": "val vs var", "content": "<p>Kotlin uses <code>val</code> for <strong>immutable</strong> (read-only) variables and <code>var</code> for <strong>mutable</strong> ones. Prefer <code>val</code> by default — it signals intent and prevents accidental reassignment.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val pi = 3.14159     // immutable — cannot reassign\nvar counter = 0      // mutable — can reassign\ncounter++</pre>"},
            {"title": "Type Inference", "content": "<p>Kotlin's compiler infers types, so you rarely need to annotate them explicitly. You <em>can</em> annotate for clarity: <code>val name: String = \"Kotlin\"</code>. The compiler will catch any type mismatch at compile time.</p>"},
            {"title": "String Templates", "content": "<p>Instead of string concatenation, Kotlin supports <strong>string templates</strong> using <code>$variable</code> or <code>${expression}</code> directly inside double-quoted strings — a feature borrowed from modern shell scripting and Groovy.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val name = \"Kotlin\"\nprintln(\"Hello, $name!\")\nprintln(\"1 + 1 = ${1 + 1}\")</pre>"},
        ],
        key_concepts="<ul><li><strong>Null Safety</strong> — Types are non-nullable by default. Use <code>String?</code> to allow null.</li><li><strong>Smart Cast</strong> — After an <code>is</code> check, Kotlin automatically casts the type.</li><li><strong>Top-Level Functions</strong> — Functions don't need to be inside a class.</li><li><strong>Semicolons Optional</strong> — Unlike Java, Kotlin doesn't require semicolons.</li><li><strong>Range Expressions</strong> — <code>1..10</code> creates an inclusive range for loops or checks.</li></ul>",
        examples=[
            {"title": "Hello Kotlin", "code": 'fun main() {\n    val name = "Kotlin"\n    println("Hello, $name!")\n}', "output": "Hello, Kotlin!", "explanation": "<p>A top-level <code>main</code> function — no class wrapper needed. String template substitutes the variable inline.</p>"},
            {"title": "val vs var Demo", "code": 'fun main() {\n    val city = "Chennai"\n    var count = 0\n    count += 5\n    println("City: $city, Count: $count")\n}', "output": "City: Chennai, Count: 5", "explanation": "<p><code>val city</code> is fixed; reassigning it would be a compile error. <code>var count</code> can be updated freely.</p>"},
        ],
        quiz=[
            {"q": "Which keyword declares an immutable variable in Kotlin?", "options": ["var", "val", "let", "const"], "answer": "val"},
            {"q": "Kotlin was officially adopted by Google for which platform?", "options": ["iOS", "Web", "Android", "Windows"], "answer": "Android"},
            {"q": "How do you embed a variable in a Kotlin string?", "options": ["${name}", "%(name)", "#name", "&name"], "answer": "${name}"},
        ],
    ),
    "kt_nullsafety": make_topic(
        intro="""<p>Kotlin's most celebrated feature is its <strong>compile-time null safety</strong> system. In Java (and many languages), calling a method on a <code>null</code> reference causes a <code>NullPointerException</code> at runtime — one of the most common and costly bugs in software. Kotlin eliminates this by making nullability part of the <em>type system</em>. A variable of type <code>String</code> can <strong>never</strong> be null. You must explicitly declare <code>String?</code> to permit null, forcing you to handle the null case at compile time.</p>""",
        subtopics=[
            {"title": "Nullable vs Non-Nullable Types", "content": "<p>A non-nullable type like <code>String</code> will never hold null — the compiler prevents it. Add <code>?</code> to create a nullable type <code>String?</code>. Any access to a nullable type must be guarded.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>var name: String = \"Alice\"   // cannot be null\nvar nick: String? = null     // allowed to be null\n// name = null  // 🚫 Compile Error!</pre>"},
            {"title": "Safe Call Operator ?.", "content": "<p>The <strong>safe call operator</strong> <code>?.</code> calls a method only if the receiver is not null. If it is null, the expression returns <code>null</code> instead of throwing an exception.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val nick: String? = null\nprintln(nick?.length)   // prints: null (no crash!)</pre>"},
            {"title": "Elvis Operator ?:", "content": "<p>The <strong>Elvis operator</strong> <code>?:</code> provides a default value when an expression evaluates to null. Think of it as a concise <code>if (x != null) x else default</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val nick: String? = null\nval displayName = nick ?: \"Anonymous\"\nprintln(displayName)  // Anonymous</pre>"},
            {"title": "Non-Null Assertion !!", "content": "<p>The <code>!!</code> operator tells the compiler: <em>\"Trust me, this is not null.\"</em> If it is null at runtime, a <code>KotlinNullPointerException</code> is thrown. Use sparingly — it defeats the purpose of null safety.</p>"},
        ],
        key_concepts="<ul><li><code>String</code> — never null. <code>String?</code> — may be null.</li><li><code>?.</code> — safe call, returns null if receiver is null.</li><li><code>?:</code> — Elvis operator, provides fallback for null.</li><li><code>!!</code> — force unwrap; crashes if null.</li><li><code>let</code> — run a block only if the value is non-null: <code>nick?.let { println(it) }</code></li></ul>",
        examples=[
            {"title": "Safe Call & Elvis", "code": 'fun main() {\n    val input: String? = null\n    val length = input?.length ?: 0\n    println("Length: $length")  // Length: 0\n\n    val name: String? = "Kotlin"\n    println(name?.uppercase())  // KOTLIN\n}', "output": "Length: 0\nKOTLIN", "explanation": "<p>When <code>input</code> is null, <code>?.</code> short-circuits to null and <code>?:</code> supplies 0. When <code>name</code> is non-null, <code>?.uppercase()</code> works normally.</p>"},
        ],
        quiz=[
            {"q": "What symbol marks a type as nullable in Kotlin?", "options": ["!", "*", "?", "#"], "answer": "?"},
            {"q": "What does the Elvis operator ?: do?", "options": ["Throws an exception", "Provides a default when null", "Converts type to non-null", "Calls a lambda"], "answer": "Provides a default when null"},
        ],
    ),
    "kt_data_class": make_topic(
        intro="""<p>A <strong>data class</strong> in Kotlin is a concise way to create classes whose primary purpose is to <em>hold data</em>. With a single <code>data class</code> declaration, Kotlin automatically generates: <code>equals()</code> and <code>hashCode()</code> for structural equality, <code>toString()</code> that prints all fields, <code>copy()</code> for creating modified copies, and <code>componentN()</code> functions for destructuring. What takes 50 lines of boilerplate in Java takes 1 line in Kotlin.</p>""",
        subtopics=[
            {"title": "Declaring a Data Class", "content": "<pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>data class User(val name: String, val age: Int)</pre><p>That's it! Kotlin auto-generates <code>equals</code>, <code>hashCode</code>, <code>toString</code>, and <code>copy</code>.</p>"},
            {"title": "copy() Function", "content": "<p>The <code>copy()</code> function creates a new instance with some properties changed, leaving others at their original values. This is perfect for immutable data updates.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val user1 = User(\"Alice\", 25)\nval user2 = user1.copy(age = 26)\nprintln(user2)  // User(name=Alice, age=26)</pre>"},
            {"title": "Destructuring Declarations", "content": "<p>Data classes support <strong>destructuring</strong> — you can unpack properties into local variables automatically.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val (name, age) = User(\"Bob\", 30)\nprintln(\"$name is $age years old\")</pre>"},
        ],
        key_concepts="<ul><li>Auto-generated <code>equals()</code> compares fields, not references.</li><li><code>toString()</code> prints <code>ClassName(field=value, ...)</code>.</li><li><code>copy()</code> allows partial updates without mutation.</li><li>Data classes cannot be abstract, sealed, or inner.</li><li>Primary constructor must have at least one parameter.</li></ul>",
        examples=[
            {"title": "Data Class in Action", "code": 'data class Point(val x: Int, val y: Int)\n\nfun main() {\n    val p1 = Point(3, 4)\n    val p2 = p1.copy(y = 10)\n    println(p1)          // Point(x=3, y=4)\n    println(p2)          // Point(x=3, y=10)\n    println(p1 == p2)    // false\n    val (x, y) = p1\n    println("x=$x y=$y") // x=3 y=4\n}', "output": "Point(x=3, y=4)\nPoint(x=3, y=10)\nfalse\nx=3 y=4", "explanation": "<p>Kotlin auto-generates all the boilerplate that Java requires manually.</p>"},
        ],
        quiz=[
            {"q": "Which method does Kotlin auto-generate for data classes to allow partial updates?", "options": ["clone()", "copy()", "update()", "mutate()"], "answer": "copy()"},
            {"q": "Data class equals() compares:", "options": ["Object references", "Field values", "Hash codes only", "Class names"], "answer": "Field values"},
        ],
    ),
    "kt_lambdas": make_topic(
        intro="""<p><strong>Lambdas</strong> (also called anonymous functions or function literals) are a core functional programming feature in Kotlin. A lambda is a function without a name that can be stored in a variable, passed as an argument, or returned from another function. Kotlin's syntax for lambdas is clean and concise, and the standard library is built around higher-order functions like <code>map</code>, <code>filter</code>, and <code>reduce</code> that accept lambdas as parameters.</p>""",
        subtopics=[
            {"title": "Lambda Syntax", "content": "<p>A lambda expression is enclosed in curly braces <code>{ }</code>. Parameters are listed before <code>-></code>, and the last expression is the return value.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val double = { x: Int -> x * 2 }\nprintln(double(5))  // 10</pre>"},
            {"title": "it — The Implicit Parameter", "content": "<p>When a lambda has exactly one parameter, you can skip naming it and use the implicit name <code>it</code>.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val square = { it: Int -> it * it }  // explicit\nval cube: (Int) -> Int = { it * it * it } // using implicit 'it'</pre>"},
            {"title": "Trailing Lambda Syntax", "content": "<p>If the last argument of a function is a lambda, Kotlin lets you move it outside the parentheses. This makes DSL-style code very readable.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>listOf(1, 2, 3).forEach {\n    println(it)\n}</pre>"},
        ],
        key_concepts="<ul><li><strong>Higher-order function</strong> — a function that takes a function as parameter or returns one.</li><li><strong>Function type</strong> — <code>(Int) -> String</code> describes a lambda taking an Int and returning a String.</li><li><code>map</code> transforms each element, <code>filter</code> keeps matching elements, <code>reduce</code> combines all.</li><li><strong>Closure</strong> — lambdas capture variables from the surrounding scope.</li></ul>",
        examples=[
            {"title": "map, filter, reduce", "code": 'fun main() {\n    val nums = listOf(1, 2, 3, 4, 5)\n    val evens = nums.filter { it % 2 == 0 }\n    val doubled = evens.map { it * 2 }\n    val sum = doubled.reduce { acc, n -> acc + n }\n    println(evens)   // [2, 4]\n    println(doubled) // [4, 8]\n    println(sum)     // 12\n}', "output": "[2, 4]\n[4, 8]\n12", "explanation": "<p>Chain of functional operations: filter even numbers, double them, then sum.</p>"},
        ],
        quiz=[
            {"q": "What is the implicit parameter name when a lambda has one parameter?", "options": ["self", "this", "it", "arg"], "answer": "it"},
            {"q": "A function that accepts another function as an argument is called a:", "options": ["Lambda function", "Higher-order function", "Closure", "Extension function"], "answer": "Higher-order function"},
        ],
    ),
    "kt_collections": make_topic(
        intro="""<p>Kotlin provides a rich collections API that distinguishes between <strong>immutable</strong> (read-only) and <strong>mutable</strong> collections. This distinction at the type level prevents accidental modification — a critical design choice for safe, concurrent code. Kotlin collections interoperate seamlessly with Java collections while offering dozens of extension functions like <code>map</code>, <code>filter</code>, <code>groupBy</code>, <code>sortedBy</code>, and more that make data processing elegant.</p>""",
        subtopics=[
            {"title": "List, Set, Map — Immutable vs Mutable", "content": "<p>Use <code>listOf()</code>, <code>setOf()</code>, <code>mapOf()</code> for read-only collections, and <code>mutableListOf()</code>, <code>mutableSetOf()</code>, <code>mutableMapOf()</code> for modifiable ones.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val fruits = listOf(\"Apple\", \"Banana\", \"Cherry\")\nval scores = mutableMapOf(\"Alice\" to 95, \"Bob\" to 87)\nscores[\"Charlie\"] = 92</pre>"},
            {"title": "Powerful Extension Functions", "content": "<p>Kotlin's standard library adds dozens of functions to collections. Common ones:</p><ul><li><code>filter { predicate }</code> — keep matching items</li><li><code>map { transform }</code> — transform each item</li><li><code>groupBy { key }</code> — group into a Map</li><li><code>sortedBy { property }</code> — sort by a field</li><li><code>any { } / all { } / none { }</code> — boolean checks</li></ul>"},
        ],
        key_concepts="<ul><li><code>listOf()</code> returns a read-only <code>List</code>; <code>mutableListOf()</code> returns an <code>ArrayList</code>.</li><li>Sets guarantee uniqueness; Maps store key-value pairs.</li><li><code>to</code> infix function creates <code>Pair</code> for map entries.</li><li>Kotlin collections are backed by Java collections — zero overhead interop.</li></ul>",
        examples=[
            {"title": "Collections in Practice", "code": 'fun main() {\n    val students = listOf("Alice", "Bob", "Anna", "Charlie")\n    val aNames = students.filter { it.startsWith("A") }\n    val upper = aNames.map { it.uppercase() }\n    println(aNames)  // [Alice, Anna]\n    println(upper)   // [ALICE, ANNA]\n    println(students.sorted())  // alphabetical\n}', "output": "[Alice, Anna]\n[ALICE, ANNA]\n[Alice, Anna, Bob, Charlie]", "explanation": "<p>Chaining <code>filter</code> and <code>map</code> is idiomatic Kotlin — clean, readable, and zero boilerplate.</p>"},
        ],
        quiz=[
            {"q": "Which function creates a read-only list in Kotlin?", "options": ["ArrayList()", "mutableListOf()", "listOf()", "arrayOf()"], "answer": "listOf()"},
            {"q": "Which operator creates a key-value pair for a Map?", "options": ["->", "=>", "to", ":"], "answer": "to"},
        ],
    ),
    "kt_coroutines": make_topic(
        intro="""<p><strong>Coroutines</strong> are Kotlin's approach to <strong>asynchronous, non-blocking programming</strong>. They let you write async code that looks sequential — no callback hell, no complex reactive chains. Under the hood, coroutines are lightweight threads managed by the Kotlin runtime; you can launch thousands of coroutines consuming only a few megabytes of memory, whereas OS threads would exhaust resources. Coroutines are the foundation of modern Android networking, Firebase operations, and any Kotlin backend async work.</p>""",
        subtopics=[
            {"title": "suspend Functions", "content": "<p>A <code>suspend</code> function is one that can <em>pause</em> without blocking the thread. It can only be called from another <code>suspend</code> function or a coroutine builder. The <code>suspend</code> keyword signals that the function may do async work.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>suspend fun fetchData(): String {\n    delay(1000)  // non-blocking 1 second pause\n    return \"Data loaded!\"\n}</pre>"},
            {"title": "launch & async", "content": "<p><code>launch</code> starts a coroutine and returns a <code>Job</code>. <code>async</code> starts a coroutine that returns a <code>Deferred<T></code> — use <code>await()</code> to get the result. Use <code>launch</code> for fire-and-forget; use <code>async</code> when you need the return value.</p>"},
            {"title": "Coroutine Scope & Dispatchers", "content": "<p>Every coroutine runs within a <strong>CoroutineScope</strong>. The <strong>Dispatcher</strong> controls which thread pool runs the coroutine:</p><ul><li><code>Dispatchers.Main</code> — UI thread (Android)</li><li><code>Dispatchers.IO</code> — network/disk operations</li><li><code>Dispatchers.Default</code> — CPU-heavy work</li></ul>"},
        ],
        key_concepts="<ul><li><strong>Non-blocking</strong> — <code>delay()</code> suspends without blocking the OS thread.</li><li><strong>Structured Concurrency</strong> — child coroutines are bound to parent scope; cancelling parent cancels all children.</li><li><code>runBlocking</code> bridges blocking code to coroutine world; use only in tests or <code>main()</code>.</li><li>Kotlin coroutines require the <code>kotlinx-coroutines</code> dependency.</li></ul>",
        examples=[
            {"title": "Basic Coroutine", "code": 'import kotlinx.coroutines.*\n\nfun main() = runBlocking {\n    launch {\n        delay(500)\n        println("Coroutine finished")\n    }\n    println("Main thread continues")\n    delay(1000)\n}', "output": "Main thread continues\nCoroutine finished", "explanation": "<p>The coroutine runs concurrently alongside main. <code>delay</code> suspends without blocking, so \"Main thread continues\" prints first.</p>"},
        ],
        quiz=[
            {"q": "Which keyword marks a function that can be paused and resumed?", "options": ["async", "suspend", "coroutine", "await"], "answer": "suspend"},
            {"q": "Which dispatcher should you use for network calls?", "options": ["Dispatchers.Main", "Dispatchers.CPU", "Dispatchers.IO", "Dispatchers.UI"], "answer": "Dispatchers.IO"},
        ],
    ),
    "kt_extensions": make_topic(
        intro="""<p><strong>Extension functions</strong> let you add new functions to existing classes — even classes you don't own, like <code>String</code>, <code>Int</code>, or Android's <code>View</code> — without inheriting from them or modifying their source code. This is one of Kotlin's most powerful and elegant features. You simply define a function with the class you're extending as the <em>receiver type</em>. The result: cleaner APIs, more readable code, and zero inheritance overhead.</p>""",
        subtopics=[
            {"title": "Defining Extension Functions", "content": "<p>Prefix the function name with the receiver type followed by a dot. Inside the function, <code>this</code> refers to the receiver object.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>fun String.isPalindrome(): Boolean {\n    return this == this.reversed()\n}\n\nprintln(\"racecar\".isPalindrome())  // true\nprintln(\"kotlin\".isPalindrome())   // false</pre>"},
            {"title": "Extension Properties", "content": "<p>You can also define extension <em>properties</em> (computed; no backing field).</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>val String.wordCount: Int\n    get() = this.split(\" \").size\n\nprintln(\"Hello World Kotlin\".wordCount)  // 3</pre>"},
        ],
        key_concepts="<ul><li>Extensions are resolved <strong>statically</strong> — they don't override member functions.</li><li>Extensions can't access private members of the class.</li><li>They are a syntactic convenience compiled to static utility functions.</li><li>Widely used in Android: <code>View.gone()</code>, <code>Context.toast()</code> patterns.</li></ul>",
        examples=[
            {"title": "Extending Int", "code": 'fun Int.isEven() = this % 2 == 0\nfun Int.squared() = this * this\n\nfun main() {\n    println(4.isEven())   // true\n    println(5.isEven())   // false\n    println(7.squared())  // 49\n}', "output": "true\nfalse\n49", "explanation": "<p>We added methods to the built-in <code>Int</code> class without touching its source.</p>"},
        ],
        quiz=[
            {"q": "Extension functions in Kotlin are dispatched:", "options": ["Dynamically at runtime", "Statically at compile time", "Via reflection", "Through interfaces"], "answer": "Statically at compile time"},
            {"q": "Inside an extension function, 'this' refers to:", "options": ["The file", "The outer class", "The extension function itself", "The receiver object"], "answer": "The receiver object"},
        ],
    ),
    "kt_advanced": make_topic(
        intro="""<p>Kotlin's advanced features — <strong>sealed classes</strong>, <strong>inline functions</strong>, <strong>delegation</strong>, <strong>DSLs</strong>, and <strong>type aliases</strong> — are what separate experienced Kotlin developers from beginners. These concepts allow you to write extremely expressive, type-safe APIs, eliminate performance overhead of higher-order functions, and model complex domain logic with precision. Mastering these turns Kotlin into one of the most powerful languages on the JVM.</p>""",
        subtopics=[
            {"title": "Sealed Classes", "content": "<p>A <code>sealed class</code> restricts class hierarchies to a closed set of subclasses defined in the same file. This makes <code>when</code> expressions exhaustive — the compiler tells you if you've missed a case.</p><pre style='background:#1e1e2f;color:#e2e8f0;padding:15px;border-radius:8px;'>sealed class Result\ndata class Success(val data: String) : Result()\ndata class Error(val msg: String) : Result()\n\nfun handle(r: Result) = when(r) {\n    is Success -> println(\"Data: ${r.data}\")\n    is Error   -> println(\"Error: ${r.msg}\")\n}</pre>"},
            {"title": "Inline Functions", "content": "<p><code>inline</code> functions eliminate the overhead of lambda calls by copying (inlining) the function body at each call site. This is critical for performance in hot paths like collection operators.</p>"},
            {"title": "Delegation (by keyword)", "content": "<p>Kotlin supports <strong>class delegation</strong> via the <code>by</code> keyword, implementing an interface by delegating to another object without manual forwarding methods. Also applies to lazy property initialization: <code>val data by lazy { heavyComputation() }</code>.</p>"},
        ],
        key_concepts="<ul><li><strong>Sealed classes</strong> enable exhaustive <code>when</code> matching — like algebraic data types.</li><li><strong>object declaration</strong> creates singletons without boilerplate.</li><li><strong>companion object</strong> replaces Java's <code>static</code> members.</li><li><strong>Type aliases</strong> (<code>typealias UserMap = Map&lt;String, User&gt;</code>) improve readability.</li><li><strong>Reified type parameters</strong> (with <code>inline</code>) let you access generic type info at runtime.</li></ul>",
        examples=[
            {"title": "Sealed Class State Machine", "code": 'sealed class State\nobject Loading : State()\ndata class Success(val data: String) : State()\ndata class Failure(val error: String) : State()\n\nfun render(state: State) = when (state) {\n    is Loading  -> println("Loading...")\n    is Success  -> println("Got: ${state.data}")\n    is Failure  -> println("Oops: ${state.error}")\n}\n\nfun main() {\n    render(Loading)\n    render(Success("Hello!"))\n    render(Failure("Network timeout"))\n}', "output": "Loading...\nGot: Hello!\nOops: Network timeout", "explanation": "<p>Sealed classes model UI states perfectly — each state is a distinct type handled exhaustively.</p>"},
        ],
        quiz=[
            {"q": "What does a sealed class guarantee in a 'when' expression?", "options": ["All cases are handled (exhaustive)", "Only one case can match", "Cases are sorted", "Runtime polymorphism"], "answer": "All cases are handled (exhaustive)"},
            {"q": "The 'by lazy' delegate evaluates its block:", "options": ["At class instantiation", "On first access", "On every access", "At compile time"], "answer": "On first access"},
        ],
    ),
    "kt_interview": make_topic(
        intro="""<p>Kotlin interview questions test your depth of understanding across the language's core features: null safety, coroutines, data classes, sealed classes, extension functions, and Android-specific patterns. Interviewers distinguish candidates who've memorised syntax from those who understand <em>why</em> Kotlin makes these design decisions and can discuss tradeoffs vs Java. This section covers the most commonly asked questions with detailed answers.</p>""",
        subtopics=[
            {"title": "Kotlin vs Java — Key Differences", "content": "<ul><li><strong>Null Safety</strong>: Kotlin prevents NPE at compile time; Java doesn't.</li><li><strong>Conciseness</strong>: data classes, string templates, extension functions drastically reduce boilerplate.</li><li><strong>Coroutines</strong>: Kotlin's built-in async model vs Java's complex CompletableFuture/threads.</li><li><strong>Interop</strong>: 100% interoperable — they compile to the same JVM bytecode.</li><li><strong>Functional</strong>: First-class functions, lambdas, higher-order functions baked in.</li></ul>"},
            {"title": "Common Interview Questions", "content": "<ul><li>What is the difference between <code>val</code> and <code>const val</code>? (<code>const val</code> is a compile-time constant for primitives/strings only)</li><li>How does <code>lateinit var</code> differ from a nullable type? (lateinit avoids null checks for properties initialized later, but crashes if accessed before init)</li><li>What is the scope of a coroutine launched with <code>GlobalScope</code>? (Dangerous — lives as long as the app, not managed)</li><li>Explain <code>@JvmStatic</code> and why it's needed. (Makes companion object methods accessible as true Java static methods)</li></ul>"},
        ],
        key_concepts="<ul><li>Know <code>val</code> vs <code>var</code> vs <code>const val</code> vs <code>lateinit var</code>.</li><li>Understand <code>by lazy</code> vs <code>lateinit</code>.</li><li>Be able to explain structured concurrency and coroutine cancellation.</li><li>Understand operator overloading (<code>operator fun plus()</code>).</li><li>Know difference between <code>==</code> (structural) and <code>===</code> (referential) equality.</li></ul>",
        examples=[
            {"title": "Common Kotlin Patterns", "code": '// Singleton\nobject AppConfig {\n    const val VERSION = "1.0"\n}\n\n// Lazy initialization\nclass HeavyClass {\n    val expensiveResource by lazy {\n        println("Initializing...")\n        "Resource ready"\n    }\n}\n\nfun main() {\n    println(AppConfig.VERSION)\n    val obj = HeavyClass()\n    println(obj.expensiveResource)  // triggers init\n    println(obj.expensiveResource)  // cached, no re-init\n}', "output": "1.0\nInitializing...\nResource ready\nResource ready", "explanation": "<p>Singleton via <code>object</code> and lazy delegation are extremely common interview topics.</p>"},
        ],
        quiz=[
            {"q": "What is the difference between == and === in Kotlin?", "options": ["No difference", "== is structural equality, === is referential", "=== is structural, == is referential", "Both check references"], "answer": "== is structural equality, === is referential"},
            {"q": "const val can only be used with:", "options": ["Any type", "Nullable types", "Primitive types and String", "Collections"], "answer": "Primitive types and String"},
        ],
    ),
}

def load_data():
    with open(FILEPATH, 'r', encoding='utf-8') as f:
        content = f.read()
    prefix = 'window.tracksData = '
    idx = content.find(prefix)
    raw_json = content[idx + len(prefix):]
    suffix = ''
    if raw_json.strip().endswith(';'):
        raw_json = raw_json.strip()[:-1]
        suffix = ';'
    return content[:idx + len(prefix)], json.loads(raw_json), suffix

def save_data(prefix_content, data, suffix):
    with open(FILEPATH, 'w', encoding='utf-8') as f:
        f.write(prefix_content)
        f.write(json.dumps(data, ensure_ascii=False, separators=(',', ':')))
        f.write(suffix)

def apply_fixes(data, lang_key, fixes):
    fixed = 0
    for topic_key, new_content in fixes.items():
        if topic_key in data.get(lang_key, {}).get('content', {}):
            # Preserve existing title, phase, and other metadata
            existing = data[lang_key]['content'][topic_key]
            new_content['title'] = existing.get('title', topic_key)
            new_content['phase'] = existing.get('phase', 1)
            data[lang_key]['content'][topic_key] = new_content
            fixed += 1
            print(f"  OK {lang_key}/{topic_key}")
        else:
            print(f"  MISS {lang_key}/{topic_key}")
    return fixed

if __name__ == '__main__':
    print("Loading tracks_data.js...")
    prefix_content, data, suffix = load_data()
    
    total = 0
    print("\n--- Fixing Java ---")
    total += apply_fixes(data, 'java', JAVA_FIXES)
    print("\n--- Fixing Kotlin ---")
    total += apply_fixes(data, 'kotlin', KOTLIN_FIXES)
    
    print(f"\nSaving {total} fixes to tracks_data.js...")
    save_data(prefix_content, data, suffix)
    print("Done!")
