import json, re

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

# --- STEP 1: Remove Key Insight filler from ALL subtopics globally ---
key_insight_pattern = r"<p style='padding: 12px.*?Key Insight:.*?</p>"

count_removed = 0
for lang, langData in d.items():
    if 'nodes' not in langData:
        continue
    for node in langData['nodes']:
        content = langData['content'].get(node['id'], {})
        if not content.get('structured') or not content['structured'].get('subtopics'):
            continue
        for sub in content['structured']['subtopics']:
            if 'Key Insight' in sub['content']:
                sub['content'] = re.sub(key_insight_pattern, '', sub['content'])
                count_removed += 1

print(f"Removed {count_removed} Key Insight boxes globally")

# --- STEP 2: Replace the filler subtopics that are JUST Key Insight with real content ---

# Kotlin fixes - replace generic subtopics with real content
kt_fixes = {
    "kt_variables": [
        {"title": "1. val vs var", "content": "<p><code>val</code> declares an immutable variable (like Java's <code>final</code> or JS's <code>const</code>) and is preferred by default. <code>var</code> declares a mutable variable that can be reassigned.</p><p>Kotlin encourages immutability. Always start with <code>val</code> and only switch to <code>var</code> when mutation is truly needed. This reduces bugs caused by unexpected state changes.</p><p>Type inference works with both: <code>val name = \"Alice\"</code> is inferred as <code>String</code>. You can also be explicit: <code>val age: Int = 25</code>.</p>"},
        {"title": "2. Type Conversion", "content": "<p>Kotlin does NOT allow implicit numeric conversion (unlike Java). You must use explicit conversion functions: <code>.toInt()</code>, <code>.toLong()</code>, <code>.toDouble()</code>, <code>.toString()</code>.</p><p>For example, <code>val x: Long = 10</code> is a compile error. You need <code>val x: Long = 10.toLong()</code>. This strictness prevents subtle data loss bugs that occur with implicit widening in Java.</p><p>String to number conversion: <code>\"42\".toInt()</code> works, but <code>\"hello\".toInt()</code> throws an exception. Use <code>\"hello\".toIntOrNull()</code> for safe conversion that returns null on failure.</p>"}
    ],
    "kt_operators": [
        {"title": "1. Arithmetic & Comparison", "content": "<p>Kotlin operators are similar to Java/C#. All comparison operators (<code>==</code>, <code>!=</code>, <code>></code>, <code><</code>) return Boolean values. A critical difference: <code>==</code> in Kotlin checks <strong>structural equality</strong> (like Java's <code>.equals()</code>), while <code>===</code> checks <strong>referential equality</strong> (same object in memory).</p><p>Kotlin also supports operator overloading: you can define what <code>+</code>, <code>-</code>, <code>*</code> do for your custom classes using operator functions like <code>operator fun plus(other: MyType)</code>.</p>"},
        {"title": "2. when Expression", "content": "<p><code>when</code> is Kotlin's powerful replacement for Java's switch statement. Unlike switch, <code>when</code> is an <strong>expression</strong> that returns a value. It can match values, ranges, types, and arbitrary conditions.</p><p>Example: <code>when (x) { in 1..10 -> \"small\"; is String -> \"text\"; else -> \"other\" }</code>. No <code>break</code> needed - only the matching branch executes.</p><p>You can also use <code>when</code> without an argument as a replacement for long <code>if-else</code> chains: <code>when { x > 0 -> \"positive\"; x < 0 -> \"negative\"; else -> \"zero\" }</code></p>"}
    ],
    "kt_control": [
        {"title": "1. if as Expression & when", "content": "<p>In Kotlin, <code>if</code> and <code>when</code> are EXPRESSIONS - they return a value! This eliminates the need for ternary operators (which Kotlin doesn't have). Write: <code>val max = if (a > b) a else b</code>.</p><p>This makes assignments cleaner and more readable. You can also use multi-line if expressions with blocks: <code>val result = if (score >= 90) { println(\"Great!\"); \"A\" } else { \"B\" }</code> - the last expression in each block is the return value.</p><p>Combined with <code>when</code> expressions, Kotlin's control flow is both powerful and concise. No more verbose switch-case-break patterns from Java.</p>"}
    ],
    "kt_loops": [
        {"title": "1. for, while, repeat", "content": "<p>Kotlin's <code>for</code> loop iterates over ranges and collections - there is no C-style <code>for(i=0; i<n; i++)</code>. Use ranges: <code>for (i in 1..10)</code> or <code>for (i in 0 until list.size)</code>. Step through: <code>for (i in 0..100 step 5)</code>. Count down: <code>for (i in 10 downTo 1)</code>.</p><p><code>repeat(n)</code> runs a block n times without creating a loop variable: <code>repeat(3) { println(\"Hello\") }</code>. <code>while</code> and <code>do-while</code> work as expected.</p><p>For collections, prefer functional methods: <code>list.forEach { }</code>, <code>list.forEachIndexed { index, value -> }</code>.</p>"},
        {"title": "2. break, continue, labels", "content": "<p>Kotlin supports labeled <code>break</code>/<code>continue</code> to exit or skip outer loops. Define a label with <code>@</code>: <code>outer@ for (...)</code>, then <code>break@outer</code> exits the outer loop from inside an inner loop.</p><p>This is especially useful with nested loops where you need to break out of the entire structure, not just the inner loop. Labels also work with <code>return</code> from lambdas: <code>list.forEach { if (it == 5) return@forEach }</code> skips just one iteration instead of returning from the whole function.</p>"}
    ],
    "kt_functions": [
        {"title": "1. Function Syntax", "content": "<p>Kotlin functions use the <code>fun</code> keyword: <code>fun add(a: Int, b: Int): Int = a + b</code>. Single-expression functions can use <code>=</code> instead of curly braces.</p><p>Kotlin supports <strong>default parameter values</strong>: <code>fun greet(name: String = \"World\")</code>. This eliminates Java's need for multiple overloaded methods.</p>"},
        {"title": "2. Named Arguments & Lambdas", "content": "<p>Call functions with named arguments for clarity: <code>createUser(name = \"Alice\", age = 25)</code>. This is especially useful when functions have multiple parameters of the same type.</p><p>Kotlin has first-class support for lambdas (anonymous functions): <code>val double = { x: Int -> x * 2 }</code>. When a lambda is the last argument, it can go outside the parentheses: <code>list.filter { it > 5 }</code>. The implicit <code>it</code> parameter refers to the single lambda argument.</p>"},
        {"title": "3. Extension Functions", "content": "<p>Kotlin's unique feature: add new functions to existing classes without inheriting them! <code>fun String.addExclamation() = this + \"!\"</code>. Now call: <code>\"Hello\".addExclamation()</code>. This is how Kotlin's standard library adds hundreds of useful methods to basic types.</p>"}
    ],
    "kt_arrays": [
        {"title": "1. Arrays vs Lists", "content": "<p>Kotlin has both <code>Array</code> (fixed-size, like Java arrays) and <code>List</code> (from collections). <code>arrayOf(1, 2, 3)</code> creates an array. <code>listOf(1, 2, 3)</code> creates an immutable list. <code>mutableListOf(1, 2, 3)</code> creates a mutable list.</p><p>In practice, <code>List</code> is used far more often than <code>Array</code>. Lists integrate better with Kotlin's collection functions and are safer (immutable by default).</p>"},
        {"title": "2. Collection Operations", "content": "<p>Kotlin provides powerful functional operations on collections: <code>.filter { }</code> (select matching), <code>.map { }</code> (transform each), <code>.reduce { }</code> (accumulate), <code>.sortedBy { }</code> (sort), <code>.groupBy { }</code> (categorize).</p><p>These can be chained: <code>people.filter { it.age >= 18 }.sortedBy { it.name }.map { it.name }</code>. This functional style is clean, readable, and eliminates most manual loop code.</p>"},
        {"title": "3. Destructuring", "content": "<p>Kotlin lets you destructure collections and data classes: <code>val (first, second) = listOf(\"a\", \"b\")</code>. With maps: <code>for ((key, value) in map)</code>. Data classes automatically support destructuring for all their properties.</p>"}
    ],
    "kt_strings": [
        {"title": "1. String Templates", "content": "<p>Kotlin uses <code>$variable</code> or <code>${expression}</code> for string interpolation (called string templates). Example: <code>\"Hello, $name! You are ${age + 1} next year.\"</code>. This replaces Java's cumbersome String.format() and concatenation.</p><p>Raw strings use triple quotes <code>\"\"\"</code> for multi-line text without escape characters. Great for regex, JSON templates, and SQL queries.</p>"},
        {"title": "2. String Methods", "content": "<p>Common operations: <code>.uppercase()</code>, <code>.lowercase()</code>, <code>.trim()</code>, <code>.split()</code>, <code>.replace()</code>, <code>.contains()</code>, <code>.startsWith()</code>, <code>.toIntOrNull()</code>.</p><p>Kotlin adds extension functions like <code>.isNullOrEmpty()</code>, <code>.isNullOrBlank()</code>, <code>.substringBefore()</code>, <code>.substringAfter()</code> that make string handling more expressive than Java.</p>"},
        {"title": "3. String Building", "content": "<p>For building strings efficiently in loops, use <code>buildString { }</code>: <code>val result = buildString { append(\"Hello\"); append(\" World\") }</code>. This is Kotlin's idiomatic alternative to Java's StringBuilder.</p><p><code>joinToString()</code> converts a collection to a formatted string: <code>listOf(1, 2, 3).joinToString(\", \")</code> gives <code>\"1, 2, 3\"</code>.</p>"}
    ],
    "kt_oop": [
        {"title": "1. Classes & Constructors", "content": "<p>Kotlin classes have a primary constructor in the class header: <code>class Person(val name: String, var age: Int)</code>. <code>val</code>/<code>var</code> in the constructor automatically creates properties. No need for boilerplate getter/setter code!</p><p>Secondary constructors use <code>constructor</code> keyword and must delegate to the primary: <code>constructor(name: String) : this(name, 0)</code>. Init blocks run as part of the primary constructor.</p>"},
        {"title": "2. Data Classes", "content": "<p><code>data class User(val name: String, val age: Int)</code> automatically generates <code>equals()</code>, <code>hashCode()</code>, <code>toString()</code>, <code>copy()</code>, and destructuring. This replaces hundreds of lines of Java boilerplate.</p><p>The <code>copy()</code> function creates a modified clone: <code>val older = user.copy(age = user.age + 1)</code>. Perfect for immutable data patterns.</p>"},
        {"title": "3. Object Declarations", "content": "<p>Kotlin's <code>object</code> keyword creates singletons: <code>object Database { fun connect() {} }</code>. Call directly: <code>Database.connect()</code>. <code>companion object</code> adds static-like members to a class, replacing Java's <code>static</code> keyword.</p>"}
    ],
    "kt_inheritance": [
        {"title": "1. open & override", "content": "<p>Kotlin classes are <code>final</code> by default - you must explicitly mark them as <code>open</code> to allow inheritance: <code>open class Animal</code>. Same for methods: <code>open fun speak()</code>. This is the opposite of Java where everything is inheritable by default.</p><p>Override with: <code>override fun speak() { ... }</code>. The <code>override</code> keyword is mandatory, not optional like Java's @Override annotation.</p>"},
        {"title": "2. Abstract & Sealed Classes", "content": "<p><code>abstract class Shape</code> cannot be instantiated and can have abstract methods. <code>sealed class Result</code> restricts inheritance to classes defined in the same file - perfect for representing a fixed set of states like Success/Error.</p><p>Sealed classes with <code>when</code> expressions provide exhaustive type-checking: the compiler warns you if you miss a subtype.</p>"},
        {"title": "3. Interfaces", "content": "<p>Kotlin interfaces can have abstract methods AND default implementations (like Java 8+). A class can implement multiple interfaces: <code>class Dog : Animal(), Trainable</code>.</p><p>When two interfaces have the same method, you resolve the conflict with <code>super&lt;InterfaceName&gt;.method()</code>. Interface properties can be abstract or have default getters.</p>"}
    ]
}

# MySQL fixes
mysql_fixes = {
    "mysql_datatypes": [
        {"title": "1. Numeric Types", "content": "<p>MySQL provides several numeric types for different needs: <code>INT</code> (whole numbers, -2 billion to +2 billion), <code>BIGINT</code> (larger range), <code>TINYINT</code> (0-255, perfect for flags), <code>DECIMAL(precision, scale)</code> (exact decimals for money), <code>FLOAT</code>/<code>DOUBLE</code> (approximate decimals for scientific data).</p><p>Always use <code>DECIMAL</code> for financial data - FLOAT/DOUBLE can have rounding errors. <code>UNSIGNED</code> modifier doubles the positive range by removing negative values.</p>"},
        {"title": "2. String Types", "content": "<p><code>CHAR(n)</code> stores fixed-length strings (padded with spaces). <code>VARCHAR(n)</code> stores variable-length strings up to n characters. <code>TEXT</code> stores large text blocks (up to 65KB). <code>LONGTEXT</code> for very large text (up to 4GB).</p><p>Use <code>CHAR</code> for fixed-length data like country codes (CHAR(2)). Use <code>VARCHAR</code> for variable data like names (VARCHAR(100)). Use <code>TEXT</code> only when you need to store large amounts of text like articles or descriptions.</p>"},
        {"title": "3. Date & Time Types", "content": "<p><code>DATE</code> stores dates (YYYY-MM-DD). <code>DATETIME</code> stores date and time (YYYY-MM-DD HH:MM:SS). <code>TIMESTAMP</code> auto-updates on row modification (useful for 'last_modified' columns). <code>TIME</code> stores time only.</p><p>Use <code>TIMESTAMP</code> for tracking creation/modification times. Use <code>DATE</code> for birthdays, deadlines. Functions like <code>NOW()</code>, <code>CURDATE()</code>, <code>DATEDIFF()</code> make date calculations easy.</p>"}
    ],
    "mysql_functions": [
        {"title": "1. String Functions", "content": "<p>MySQL provides powerful string manipulation: <code>CONCAT()</code> joins strings, <code>UPPER()</code>/<code>LOWER()</code> change case, <code>LENGTH()</code> counts characters, <code>SUBSTRING(str, start, length)</code> extracts parts, <code>TRIM()</code> removes whitespace, <code>REPLACE()</code> substitutes text.</p><p>Example: <code>SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM users;</code></p>"},
        {"title": "2. Aggregate Functions", "content": "<p><code>COUNT()</code> counts rows, <code>SUM()</code> totals values, <code>AVG()</code> calculates average, <code>MAX()</code>/<code>MIN()</code> find extremes. Used with <code>GROUP BY</code> to aggregate data by categories.</p><p>Example: <code>SELECT department, AVG(salary) FROM employees GROUP BY department HAVING AVG(salary) > 50000;</code></p>"},
        {"title": "3. Date & Math Functions", "content": "<p>Date functions: <code>NOW()</code>, <code>CURDATE()</code>, <code>DATE_ADD()</code>, <code>DATEDIFF()</code>, <code>DATE_FORMAT()</code>. Math functions: <code>ROUND()</code>, <code>CEIL()</code>, <code>FLOOR()</code>, <code>ABS()</code>, <code>MOD()</code>, <code>RAND()</code>.</p><p>Example: <code>SELECT name, DATEDIFF(CURDATE(), hire_date) AS days_employed FROM employees;</code></p>"}
    ]
}

# DSA fixes  
dsa_fixes = {
    "dsa_arrays": [
        {"title": "1. Array Fundamentals", "content": "<p>An array stores elements in <strong>contiguous memory locations</strong>. This means accessing any element by index takes O(1) time - the computer calculates the exact memory address using: <code>base_address + (index * element_size)</code>.</p><p>Trade-offs: O(1) access but O(n) insertion/deletion (elements must shift). Arrays have fixed size in most languages (except Python lists, JavaScript arrays which are dynamic).</p>"},
        {"title": "2. Common Array Algorithms", "content": "<p>Essential algorithms: <strong>Two Pointer</strong> technique (finding pairs, reversing), <strong>Sliding Window</strong> (subarray problems), <strong>Prefix Sum</strong> (range sum queries in O(1)), <strong>Kadane's Algorithm</strong> (maximum subarray sum in O(n)).</p><p>Most array interview problems can be solved optimally using one of these patterns. Practice identifying which pattern fits the problem.</p>"},
        {"title": "3. Matrix Operations", "content": "<p>A matrix is a 2D array. Key operations: traversal (row-major vs column-major), rotation (90/180/270 degrees), spiral traversal, transpose, and search in a sorted matrix.</p><p>For matrix problems, always clarify dimensions and whether the matrix is sorted. Sorted matrices can be searched in O(m + n) using the staircase approach starting from the top-right corner.</p>"}
    ]
}

# Apply Kotlin fixes
for topic_id, subtopics in kt_fixes.items():
    if topic_id in d['kotlin']['content']:
        d['kotlin']['content'][topic_id]['structured']['subtopics'] = subtopics

# Apply MySQL fixes
for topic_id, subtopics in mysql_fixes.items():
    if topic_id in d['mysql']['content']:
        d['mysql']['content'][topic_id]['structured']['subtopics'] = subtopics

# Apply DSA fixes
for topic_id, subtopics in dsa_fixes.items():
    if topic_id in d['dsa']['content']:
        d['dsa']['content'][topic_id]['structured']['subtopics'] = subtopics

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print(f"Done! Removed {count_removed} Key Insight boxes and replaced 12 topics with real content.")
