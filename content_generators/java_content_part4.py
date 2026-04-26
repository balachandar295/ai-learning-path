import json

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
json_start = text.find('{')
data = json.loads(text[json_start:text.rfind('}')+1])

def card(label, code):
    return f"<div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'><div style='background:linear-gradient(to right,#f89820,#e65c00);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>{label}</div><pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>{code}</pre></div>"

def section(t, d, exs):
    h = f"<h4 style='color:#f89820;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #f89820;padding-left:12px;'>{t}</h4>"
    h += f"<p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>{d}</p>"
    for l, c in exs: h += card(l, c)
    return h

def explanation(title, sections):
    h = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #f89820;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections: h += section(*s)
    return h + "</div>"

def quiz(items): return [{"q":q,"options":o,"answer":a} for q,o,a in items]
def task(t,d,h,c): return {"title":t,"description":d,"hint":h,"code":c}
def problems(items): return [{"title":t,"description":d,"code":c} for t,d,c in items]

jv = data['java']['content']

# TOPIC 15: Generics
jv['java_generics'] = {
    "title": "Generics",
    "explanation": explanation("Generics", [
        ("Generic Classes & Methods",
         "Generics provide type safety at compile time. They eliminate the need for casting and prevent ClassCastException.",
         [("Generic class", "// T is type placeholder (any name: T, E, K, V)\nclass Box<T> {\n    private T value;\n    Box(T value) { this.value = value; }\n    T get()      { return value; }\n    void set(T v){ value = v; }\n}\n\nBox<String>  strBox = new Box<>(\"Hello\");\nBox<Integer> intBox = new Box<>(42);\n\nSystem.out.println(strBox.get()); // Hello\nSystem.out.println(intBox.get()); // 42\n// No casting needed!"),
          ("Generic method", "// Generic method - works with any type\nstatic <T extends Comparable<T>> T max(T a, T b) {\n    return (a.compareTo(b) >= 0) ? a : b;\n}\n\nSystem.out.println(max(10, 25));         // 25\nSystem.out.println(max(\"Apple\", \"Mango\")); // Mango\nSystem.out.println(max(3.14, 2.71));      // 3.14")]),
        ("Bounded Wildcards",
         "Wildcards (?) allow flexibility. Upper bounded (? extends T) — read only. Lower bounded (? super T) — write only.",
         [("Wildcards", "// Upper bounded: accept List of Number or its subclasses\nstatic double sumList(List<? extends Number> list) {\n    double sum = 0;\n    for (Number n : list) sum += n.doubleValue();\n    return sum;\n}\n\nList<Integer> ints    = Arrays.asList(1, 2, 3);\nList<Double>  doubles = Arrays.asList(1.5, 2.5, 3.5);\nSystem.out.println(sumList(ints));    // 6.0\nSystem.out.println(sumList(doubles)); // 7.5"),
          ("Generic pair", "class Pair<K, V> {\n    K key; V value;\n    Pair(K k, V v){ key=k; value=v; }\n    public String toString(){ return key+\"=\"+value; }\n}\n\nPair<String,Integer> age = new Pair<>(\"Alice\", 25);\nPair<Integer,Boolean> flag = new Pair<>(1, true);\nSystem.out.println(age);   // Alice=25\nSystem.out.println(flag);  // 1=true")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Generics provide?", ["Runtime flexibility", "Compile-time type safety", "Faster execution", "Dynamic typing"], "Compile-time type safety"),
        ("List<?> means?", ["List of Object", "List of unknown type (wildcard)", "List of any primitive", "Null list"], "List of unknown type (wildcard)"),
        ("T extends Number means?", ["T can be any type", "T must be Number or its subclass", "T must be Number only", "T is optional"], "T must be Number or its subclass"),
        ("Can generics use primitives?", ["Yes", "No, use wrapper classes", "Only int and double", "Only with <>"], "No, use wrapper classes"),
        ("What is type erasure?", ["Deleting type info at runtime", "Removing generics at compile time to bytecode", "Casting types", "Erasing null values"], "Removing generics at compile time to bytecode"),
    ]),
    "hands_on": task("Generic Stack", "Implement a generic Stack<T> class with push(), pop(), peek(), isEmpty() methods.", "Use ArrayList<T> internally.", "import java.util.*;\nclass Stack<T> {\n    private ArrayList<T> list = new ArrayList<>();\n    void push(T item) { list.add(item); }\n    T pop()  { return list.remove(list.size()-1); }\n    T peek() { return list.get(list.size()-1); }\n    boolean isEmpty() { return list.isEmpty(); }\n    int size() { return list.size(); }\n}\nStack<Integer> s = new Stack<>();\ns.push(1); s.push(2); s.push(3);\nSystem.out.println(s.pop());  // 3\nSystem.out.println(s.peek()); // 2"),
    "problem_solving": problems([
        ("Generic swap", "Write generic swap method that swaps two elements in an array.", "static <T> void swap(T[] arr, int i, int j){\n    T t=arr[i]; arr[i]=arr[j]; arr[j]=t;\n}\nInteger[] a={1,2,3,4};\nswap(a,0,3);\nSystem.out.println(Arrays.toString(a));"),
        ("Triple generic", "Create class Triple<A,B,C> holding three different types.", "class Triple<A,B,C>{\n    A first; B second; C third;\n    Triple(A a,B b,C c){first=a;second=b;third=c;}\n    public String toString(){return \"(\"+first+\",\"+second+\",\"+third+\")\";}\n}\nSystem.out.println(new Triple<>(\"Name\",42,true));"),
        ("Generic min/max", "Write generic method to find min in Comparable list.", "static <T extends Comparable<T>> T findMin(List<T> list){\n    T min=list.get(0);\n    for(T item:list) if(item.compareTo(min)<0) min=item;\n    return min;\n}\nSystem.out.println(findMin(Arrays.asList(3,1,4,1,5)));"),
    ])
}

# TOPIC 16: Streams & Lambda
jv['java_streams'] = {
    "title": "Streams & Lambda Expressions",
    "explanation": explanation("Streams & Lambda Expressions", [
        ("Lambda Expressions",
         "Lambdas are anonymous functions. They implement functional interfaces in a concise way. Syntax: (params) -> expression",
         [("Lambda basics", "// Before lambdas (anonymous class)\nRunnable r1 = new Runnable() {\n    public void run() { System.out.println(\"Old way\"); }\n};\n\n// With lambda\nRunnable r2 = () -> System.out.println(\"Lambda way\");\n\n// Comparator with lambda\njava.util.List<String> names = java.util.Arrays.asList(\"Charlie\",\"Alice\",\"Bob\");\nnames.sort((a, b) -> a.compareTo(b));\nSystem.out.println(names); // [Alice, Bob, Charlie]"),
          ("Method references", "// Instead of: x -> System.out.println(x)\n// Use method reference:\njava.util.Arrays.asList(\"Alice\",\"Bob\",\"Carol\")\n    .forEach(System.out::println);\n\n// Static method ref\njava.util.Arrays.asList(\"3\",\"1\",\"4\")\n    .stream()\n    .map(Integer::parseInt)  // String -> int\n    .forEach(System.out::println);")]),
        ("Stream API",
         "Streams process collections declaratively. Operations: filter, map, reduce, collect, sorted, distinct, limit, findFirst.",
         [("Stream pipeline", "import java.util.*;\nimport java.util.stream.*;\n\nList<Integer> nums = Arrays.asList(1,2,3,4,5,6,7,8,9,10);\n\n// Filter even, square, sum\nint result = nums.stream()\n    .filter(n -> n % 2 == 0)     // 2,4,6,8,10\n    .map(n -> n * n)             // 4,16,36,64,100\n    .reduce(0, Integer::sum);    // 220\nSystem.out.println(result);"),
          ("Collectors", "List<String> names=Arrays.asList(\"Alice\",\"Bob\",\"Anna\",\"Charlie\",\"Aaron\");\n\n// Filter names starting with A, sort, collect to list\nList<String> filtered = names.stream()\n    .filter(n -> n.startsWith(\"A\"))\n    .sorted()\n    .collect(Collectors.toList());\nSystem.out.println(filtered); // [Aaron, Alice, Anna]\n\n// Count\nlong count = names.stream().filter(n->n.length()>3).count();\nSystem.out.println(\"Long names: \" + count);\n\n// Group by first char\nMap<Character,List<String>> grouped = names.stream()\n    .collect(Collectors.groupingBy(n->n.charAt(0)));\nSystem.out.println(grouped);")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Lambda syntax is?", ["fn(x) => x", "(x) -> x", "lambda x: x", "def x -> x"], "(x) -> x"),
        ("Streams are?", ["Mutable", "Lazy and functional — they don't modify source", "Same as Collections", "Always parallel"], "Lazy and functional — they don't modify source"),
        ("filter() returns?", ["Single element", "New stream with matching elements", "Modified source", "Boolean"], "New stream with matching elements"),
        ("collect(Collectors.toList()) does?", ["Sorts the stream", "Gathers stream elements into a List", "Counts elements", "Maps elements"], "Gathers stream elements into a List"),
        ("Method reference System.out::println is equivalent to?", ["()->System.out.println()", "x->System.out.println(x)", "System.out.print(x)", "println::System.out"], "x->System.out.println(x)"),
    ]),
    "hands_on": task("Stream Analytics", "Given list of student marks [78,92,55,88,45,67,95], use streams to find: average, max, count passing(>=60), sorted list.", "Use stream().average(), max(), filter().count(), sorted().", "import java.util.*;\nimport java.util.stream.*;\nList<Integer> marks=Arrays.asList(78,92,55,88,45,67,95);\nSystem.out.println(\"Avg: \"+marks.stream().mapToInt(i->i).average().getAsDouble());\nSystem.out.println(\"Max: \"+marks.stream().mapToInt(i->i).max().getAsInt());\nSystem.out.println(\"Pass: \"+marks.stream().filter(m->m>=60).count());\nSystem.out.println(\"Sorted: \"+marks.stream().sorted().collect(Collectors.toList()));"),
    "problem_solving": problems([
        ("Distinct & limit", "From [1,3,2,3,4,1,5,2], get distinct values, sort, take first 3.", "Arrays.asList(1,3,2,3,4,1,5,2).stream()\n    .distinct().sorted().limit(3)\n    .forEach(System.out::println);"),
        ("String stream operations", "From list of names, get names longer than 4 chars, uppercase, sorted.", "Arrays.asList(\"Bob\",\"Alice\",\"Charlie\",\"Tom\",\"David\").stream()\n    .filter(n->n.length()>4)\n    .map(String::toUpperCase)\n    .sorted()\n    .collect(Collectors.toList())\n    .forEach(System.out::println);"),
        ("FlatMap", "Flatten [[1,2],[3,4],[5,6]] using flatMap.", "List<List<Integer>> nested=Arrays.asList(\n    Arrays.asList(1,2),Arrays.asList(3,4),Arrays.asList(5,6));\nList<Integer> flat=nested.stream()\n    .flatMap(Collection::stream)\n    .collect(Collectors.toList());\nSystem.out.println(flat);"),
    ])
}

# TOPIC 17: Advanced Java
jv['java_advanced'] = {
    "title": "Advanced Java Concepts",
    "explanation": explanation("Advanced Java", [
        ("Multithreading",
         "Java supports concurrency through threads. Use Thread class or Runnable interface. synchronized prevents race conditions.",
         [("Thread basics", "// Method 1: Extend Thread\nclass MyThread extends Thread {\n    public void run() {\n        for (int i=1; i<=5; i++) {\n            System.out.println(getName() + \": \" + i);\n            try { Thread.sleep(100); } catch (Exception e) {}\n        }\n    }\n}\n\n// Method 2: Implement Runnable (preferred)\nRunnable task = () -> {\n    System.out.println(\"Running: \"+Thread.currentThread().getName());\n};\n\nnew MyThread().start();\nnew Thread(task, \"Worker-1\").start();"),
          ("ExecutorService", "import java.util.concurrent.*;\n\n// Thread pool (better than raw threads)\nExecutorService executor = Executors.newFixedThreadPool(3);\n\nfor (int i=1; i<=5; i++) {\n    int taskId = i;\n    executor.submit(() -> {\n        System.out.println(\"Task \"+taskId+\" by \"+Thread.currentThread().getName());\n    });\n}\nexecutor.shutdown();")]),
        ("Enums & Records (Java 16+)",
         "Enums are special classes with fixed constants. Records are immutable data carriers with auto-generated constructor, getters, equals, hashCode, toString.",
         [("Enums", "enum Day {\n    MON, TUE, WED, THU, FRI, SAT, SUN;\n    public boolean isWeekend() {\n        return this == SAT || this == SUN;\n    }\n}\n\nDay today = Day.WED;\nSystem.out.println(today.isWeekend());  // false\nSystem.out.println(today.name());       // WED\nSystem.out.println(today.ordinal());    // 2\n\nfor (Day d : Day.values()) {\n    System.out.print(d + \" \");\n}"),
          ("Records (Java 16+)", "// Immutable data class with zero boilerplate!\nrecord Point(int x, int y) {\n    // Custom method\n    double distanceTo(Point other) {\n        return Math.hypot(this.x-other.x, this.y-other.y);\n    }\n}\n\nPoint p1 = new Point(0, 0);\nPoint p2 = new Point(3, 4);\nSystem.out.println(p1.x());              // 0\nSystem.out.println(p2);                  // Point[x=3, y=4]\nSystem.out.println(p1.distanceTo(p2));   // 5.0\nSystem.out.println(p1.equals(new Point(0,0))); // true")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Thread.sleep() pauses for?", ["Seconds", "Milliseconds", "Microseconds", "Minutes"], "Milliseconds"),
        ("synchronized keyword prevents?", ["Deadlock", "Race conditions (concurrent modification)", "Thread creation", "Memory leaks"], "Race conditions (concurrent modification)"),
        ("Enum constants are?", ["Variables", "Fixed, named instances of the enum", "Methods", "Primitive values"], "Fixed, named instances of the enum"),
        ("Java 16 record is?", ["Mutable data class", "Immutable data carrier with auto-generated methods", "Abstract class", "Interface"], "Immutable data carrier with auto-generated methods"),
        ("ExecutorService is better than raw threads because?", ["Simpler syntax", "It manages a thread pool efficiently", "Faster to create", "No synchronization needed"], "It manages a thread pool efficiently"),
    ]),
    "hands_on": task("Day Enum", "Create Day enum with isWeekend() method. Print all days and mark weekends.", "enum Day { MON,...,SUN; add isWeekend() method. }", "enum Day {\n    MON,TUE,WED,THU,FRI,SAT,SUN;\n    public boolean isWeekend(){\n        return this==SAT||this==SUN;\n    }\n}\nfor(Day d: Day.values()){\n    System.out.println(d + (d.isWeekend()? \" [Weekend]\" : \"\"));\n}"),
    "problem_solving": problems([
        ("Producer Consumer", "Simulate producer-consumer using two threads.", "// Simplified version\nint[] shared={0};\nThread producer=new Thread(()->{\n    shared[0]=42;\n    System.out.println(\"Produced: \"+shared[0]);\n});\nThread consumer=new Thread(()->{\n    try{producer.join();}catch(Exception e){}\n    System.out.println(\"Consumed: \"+shared[0]);\n});\nproducer.start(); consumer.start();"),
        ("Enum with switch", "Use enum Season {SPRING,SUMMER,AUTUMN,WINTER} in switch to print activity.", "enum Season{SPRING,SUMMER,AUTUMN,WINTER}\nSeason s=Season.SUMMER;\nswitch(s){\n    case SPRING->System.out.println(\"Plant flowers\");\n    case SUMMER->System.out.println(\"Go swimming\");\n    case AUTUMN->System.out.println(\"Rake leaves\");\n    case WINTER->System.out.println(\"Build snowman\");\n}"),
        ("Record with validation", "Create Student record(name, gpa) with compact constructor validating gpa 0-4.", "record Student(String name, double gpa){\n    Student{\n        if(gpa<0||gpa>4) throw new IllegalArgumentException(\"GPA out of range\");\n    }\n}\nSystem.out.println(new Student(\"Alice\",3.8));\ntry{new Student(\"Bad\",5.0);}catch(Exception e){System.out.println(e.getMessage());}"),
    ])
}

print("Java Topics 15-17 done!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved! All Java topics complete!")
