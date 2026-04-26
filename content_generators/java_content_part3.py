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
    for lbl, code in examples: h += card(lbl, code)
    return h

def explanation(title, sections):
    h = f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #f89820;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections: h += section(*s)
    return h + "</div>"

def quiz(items): return [{"q":q,"options":o,"answer":a} for q,o,a in items]
def task(t,d,h,c): return {"title":t,"description":d,"hint":h,"code":c}
def problems(items): return [{"title":t,"description":d,"code":c} for t,d,c in items]

jv = data['java']['content']

# TOPIC 10: Inheritance
jv['java_inheritance'] = {
    "title": "Inheritance",
    "explanation": explanation("Inheritance", [
        ("extends & super",
         "Inheritance allows a child class to reuse code from a parent class using 'extends'. super() calls parent constructor.",
         [("Basic inheritance", "class Animal {\n    String name;\n    Animal(String name) { this.name = name; }\n    void eat()  { System.out.println(name + \" is eating\"); }\n    void sleep(){ System.out.println(name + \" is sleeping\"); }\n}\n\nclass Dog extends Animal {\n    String breed;\n    Dog(String name, String breed) {\n        super(name);  // call parent constructor\n        this.breed = breed;\n    }\n    void bark() { System.out.println(name + \" says: Woof!\"); }\n}\n\nDog d = new Dog(\"Rex\", \"Labrador\");\nd.eat();   // inherited\nd.sleep(); // inherited\nd.bark();  // Dog's own method"),
          ("Method overriding", "class Shape {\n    String color;\n    Shape(String color) { this.color = color; }\n    double area() { return 0; }\n    void display() {\n        System.out.printf(\"%s area=%.2f%n\", color, area());\n    }\n}\n\nclass Circle extends Shape {\n    double radius;\n    Circle(String color, double r) { super(color); radius=r; }\n    @Override\n    double area() { return Math.PI * radius * radius; }\n}\n\nclass Rectangle extends Shape {\n    double w, h;\n    Rectangle(String c, double w, double h) { super(c); this.w=w; this.h=h; }\n    @Override\n    double area() { return w * h; }\n}\n\nShape c = new Circle(\"Red\", 5);\nShape r = new Rectangle(\"Blue\", 4, 6);\nc.display();\nr.display();")]),
        ("final class/method & Object class",
         "final class cannot be extended. final method cannot be overridden. All Java classes implicitly extend Object.",
         [("final keyword", "// final class - can't extend\nfinal class Immutable {\n    private final int value;\n    Immutable(int v) { value = v; }\n    int getValue() { return value; }\n}\n\n// String is final in Java!\n// class MyString extends String {} // ERROR!"),
          ("Object class methods", "// Every class inherits from Object\nclass Person {\n    String name; int age;\n    Person(String n, int a) { name=n; age=a; }\n\n    @Override\n    public String toString() {\n        return name + \"(\" + age + \")\";\n    }\n    @Override\n    public boolean equals(Object o) {\n        if(!(o instanceof Person)) return false;\n        return name.equals(((Person)o).name);\n    }\n}\n\nPerson p1 = new Person(\"Alice\", 25);\nSystem.out.println(p1);          // Alice(25)\nSystem.out.println(p1.equals(new Person(\"Alice\",30))); // true")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which keyword is used for inheritance?", ["implements", "extends", "inherits", "uses"], "extends"),
        ("super() must be the first statement in constructor?", ["No", "Yes", "Only in abstract classes", "Optional"], "Yes"),
        ("@Override annotation is?", ["Required", "Optional but recommended for safety", "Deprecated", "Only for interfaces"], "Optional but recommended for safety"),
        ("Every Java class extends?", ["Object", "Class", "Base", "Root"], "Object"),
        ("final method means?", ["Cannot be called", "Cannot be overridden", "Cannot be inherited", "Cannot be private"], "Cannot be overridden"),
    ]),
    "hands_on": task("Vehicle Hierarchy", "Create Vehicle (brand, speed). Car extends Vehicle (numDoors). Truck extends Vehicle (payload). Override toString().", "Use super(brand, speed) in child constructors.", "class Vehicle {\n    String brand; int speed;\n    Vehicle(String b, int s){ brand=b; speed=s; }\n    public String toString(){ return brand+\" @ \"+speed+\"km/h\"; }\n}\nclass Car extends Vehicle {\n    int doors;\n    Car(String b,int s,int d){ super(b,s); doors=d; }\n    public String toString(){ return super.toString()+\" [\"+doors+\" doors]\"; }\n}\nnew Car(\"Toyota\",120,4);\nSystem.out.println(new Car(\"Toyota\",120,4));"),
    "problem_solving": problems([
        ("instanceof check", "Check if object is instance of parent or child class.", "Animal a = new Dog(\"Rex\",\"Lab\");\nSystem.out.println(a instanceof Animal); // true\nSystem.out.println(a instanceof Dog);    // true"),
        ("Calling super method", "In child override, also call parent's method using super.", "class Parent {\n    void show(){ System.out.println(\"Parent show\"); }\n}\nclass Child extends Parent {\n    void show(){\n        super.show();  // call parent\n        System.out.println(\"Child show\");\n    }\n}\nnew Child().show();"),
        ("Abstract factory", "Create abstract Shape with area(). Implement Circle and Square.", "abstract class Shape { abstract double area(); }\nclass Circle extends Shape {\n    double r; Circle(double r){this.r=r;}\n    double area(){return Math.PI*r*r;}\n}\nclass Square extends Shape {\n    double s; Square(double s){this.s=s;}\n    double area(){return s*s;}\n}\nShape[] shapes={new Circle(5),new Square(4)};\nfor(Shape sh:shapes) System.out.printf(\"%.2f%n\",sh.area());"),
    ])
}

# TOPIC 11: Polymorphism
jv['java_polymorphism'] = {
    "title": "Polymorphism",
    "explanation": explanation("Polymorphism", [
        ("Runtime Polymorphism (Dynamic dispatch)",
         "Polymorphism = 'many forms'. At runtime, JVM decides which overridden method to call based on actual object type, not reference type.",
         [("Runtime polymorphism", "class Animal {\n    void sound() { System.out.println(\"Some sound\"); }\n}\nclass Cat extends Animal {\n    @Override void sound() { System.out.println(\"Meow!\"); }\n}\nclass Dog extends Animal {\n    @Override void sound() { System.out.println(\"Woof!\"); }\n}\nclass Duck extends Animal {\n    @Override void sound() { System.out.println(\"Quack!\"); }\n}\n\n// Array of parent type holding child objects\nAnimal[] animals = { new Cat(), new Dog(), new Duck() };\nfor (Animal a : animals) {\n    a.sound(); // JVM calls the ACTUAL object's method\n}"),
          ("Compile-time polymorphism (overloading)", "class Printer {\n    static void print(int n)    { System.out.println(\"Int: \"   +n); }\n    static void print(String s) { System.out.println(\"String: \"+s); }\n    static void print(double d) { System.out.println(\"Double: \"+d); }\n    // Compiler picks method based on argument type\n}\nPrinter.print(42);\nPrinter.print(\"Hello\");\nPrinter.print(3.14);")]),
        ("Upcasting & Downcasting",
         "Upcasting = child object assigned to parent reference (automatic). Downcasting = casting parent back to child (explicit, may throw ClassCastException).",
         [("Upcasting (safe)", "Dog dog = new Dog();\nAnimal animal = dog;   // upcast: automatic, safe\nanimal.sound();        // \"Woof!\" (runtime polymorphism)\n// animal.bark();      // ERROR: Animal ref can't see Dog methods"),
          ("Downcasting (careful)", "Animal a = new Dog();\n\nif (a instanceof Dog) {     // check before downcast!\n    Dog d = (Dog) a;         // explicit downcast\n    d.bark();                // now can use Dog methods\n}\n\n// Pattern matching (Java 16+)\nif (a instanceof Dog d) {\n    d.bark(); // no explicit cast needed!\n}")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Polymorphism means?", ["One class", "Many forms — same name, different behavior", "Multiple constructors", "Static methods"], "Many forms — same name, different behavior"),
        ("Runtime polymorphism is achieved by?", ["Overloading", "Overriding + Inheritance", "final methods", "static methods"], "Overriding + Inheritance"),
        ("Upcasting is?", ["Explicit cast", "Automatic — child to parent", "Only for interfaces", "Dangerous"], "Automatic — child to parent"),
        ("ClassCastException occurs when?", ["Upcast fails", "Invalid downcast", "Overloading fails", "Abstract class instantiated"], "Invalid downcast"),
        ("Compile-time polymorphism is achieved by?", ["Overriding", "Overloading", "Inheritance", "Abstraction"], "Overloading"),
    ]),
    "hands_on": task("Payment Processor", "Create Payment class with process(). CreditCard, DebitCard, UPI extend it. Loop through different types.", "Use array of Payment type with child objects.", "class Payment {\n    String type;\n    Payment(String t){ type=t; }\n    void process(double amount){\n        System.out.println(type+\": Processing Rs.\"+amount);\n    }\n}\nclass UPI extends Payment {\n    UPI(){ super(\"UPI\"); }\n    void process(double a){ System.out.println(\"UPI: Scan QR for Rs.\"+a); }\n}\nPayment[] p={new Payment(\"Card\"),new UPI()};\nfor(Payment pay:p) pay.process(1000);"),
    "problem_solving": problems([
        ("instanceof pattern matching", "Use Java 16+ instanceof pattern matching to process mixed array.", "Object[] items={\"Hello\",42,3.14,true};\nfor(Object o: items){\n    if(o instanceof String s) System.out.println(\"String: \"+s);\n    else if(o instanceof Integer i) System.out.println(\"Int: \"+i);\n    else System.out.println(\"Other: \"+o);\n}"),
        ("Overloaded area()", "Create overloaded area() for circle(r), rectangle(l,w), triangle(b,h).", "static double area(double r){ return Math.PI*r*r; }\nstatic double area(double l,double w){ return l*w; }\nstatic double area(double b,double h,boolean t){ return 0.5*b*h; }\nSystem.out.printf(\"%.2f%n\",area(5));\nSystem.out.printf(\"%.2f%n\",area(4,6));"),
        ("Covariant return type", "Child overrides parent method but returns child type.", "class Animal { Animal create(){ return new Animal(); } }\nclass Dog extends Animal {\n    @Override Dog create(){ return new Dog(); } // covariant\n}\nAnimal a=new Dog().create();\nSystem.out.println(a.getClass().getSimpleName()); // Dog"),
    ])
}

# TOPIC 12: Interfaces & Abstract
jv['java_interfaces'] = {
    "title": "Interfaces & Abstract Classes",
    "explanation": explanation("Interfaces & Abstract Classes", [
        ("Abstract Classes",
         "An abstract class cannot be instantiated. It can have both abstract (no body) and concrete (with body) methods.",
         [("Abstract class", "abstract class Vehicle {\n    String brand;\n    Vehicle(String brand) { this.brand = brand; }\n\n    // Abstract: must implement in subclass\n    abstract void startEngine();\n\n    // Concrete: available to all subclasses\n    void info() { System.out.println(\"Brand: \" + brand); }\n}\n\nclass ElectricCar extends Vehicle {\n    ElectricCar(String brand) { super(brand); }\n    @Override\n    void startEngine() { System.out.println(brand + \": Silent electric start!\"); }\n}\n\nVehicle v = new ElectricCar(\"Tesla\");\nv.info();\nv.startEngine();"),
          ("Abstract vs Concrete", "// abstract class: 0 to 100% abstract methods\n// Cannot use 'new AbstractClass()'\n// abstract Vehicle v = new Vehicle(); // ERROR!\n\n// But can use as reference type:\nVehicle ev = new ElectricCar(\"Tesla\"); // OK!\n\n// Template Method pattern:\nabstract class DataProcessor {\n    final void process() {  // final: can't override order\n        readData();\n        processData();\n        writeData();\n    }\n    abstract void readData();\n    abstract void processData();\n    abstract void writeData();\n}")]),
        ("Interfaces",
         "Interfaces define a contract of methods that implementing classes must provide. Java supports multiple interface implementation.",
         [("Interface basics", "interface Drawable {\n    void draw();  // implicitly public abstract\n    default void display() {  // Java 8: default method\n        System.out.println(\"Displaying: \");\n        draw();\n    }\n}\n\ninterface Resizable {\n    void resize(double factor);\n}\n\n// Multiple interface implementation!\nclass Circle implements Drawable, Resizable {\n    double radius;\n    Circle(double r) { radius = r; }\n    public void draw()   { System.out.println(\"Circle r=\"+radius); }\n    public void resize(double f) { radius *= f; }\n}\n\nCircle c = new Circle(5);\nc.display();\nc.resize(2);\nc.draw();"),
          ("Functional Interfaces & lambdas", "// Functional interface = exactly 1 abstract method\n@FunctionalInterface\ninterface Greeting {\n    String greet(String name);\n}\n\n// Lambda expression implements the interface\nGreeting formal = name -> \"Dear \" + name;\nGreeting casual = name -> \"Hey \" + name + \"!\";\n\nSystem.out.println(formal.greet(\"Alice\"));\nSystem.out.println(casual.greet(\"Bob\"));\n\n// Common built-in: Runnable, Comparator, Predicate")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Can you instantiate an abstract class?", ["Yes", "No", "Only with default constructor", "Only statically"], "No"),
        ("Interface methods are implicitly?", ["private and final", "public and abstract", "protected and static", "None"], "public and abstract"),
        ("Java allows implements for?", ["Only one interface", "Multiple interfaces", "Only abstract classes", "Only functional interfaces"], "Multiple interfaces"),
        ("default method in interface is?", ["Abstract method", "Method with body (Java 8+)", "Static initializer", "Private method"], "Method with body (Java 8+)"),
        ("Functional interface has exactly?", ["0 abstract methods", "1 abstract method", "2 abstract methods", "Any number"], "1 abstract method"),
    ]),
    "hands_on": task("Shape Interface", "Create Drawable interface with draw() and area(). Implement with Circle and Triangle classes.", "interface Drawable { void draw(); double area(); }", "interface Drawable {\n    void draw();\n    double area();\n}\nclass Circle implements Drawable {\n    double r;\n    Circle(double r){ this.r=r; }\n    public void draw(){ System.out.println(\"Circle r=\"+r); }\n    public double area(){ return Math.PI*r*r; }\n}\nDrawable d=new Circle(7);\nd.draw();\nSystem.out.printf(\"Area: %.2f%n\",d.area());"),
    "problem_solving": problems([
        ("Comparable implementation", "Make Student class Comparable by GPA.", "class Student implements Comparable<Student>{\n    String name; double gpa;\n    Student(String n,double g){name=n;gpa=g;}\n    public int compareTo(Student o){return Double.compare(o.gpa,gpa);}\n    public String toString(){return name+\"(\"+gpa+\")\";}\n}\njava.util.List<Student> list=new java.util.ArrayList<>();\nlist.add(new Student(\"A\",3.2)); list.add(new Student(\"B\",3.8));\njava.util.Collections.sort(list);\nSystem.out.println(list);"),
        ("Interface default method", "Add default log() to Printable interface that prints timestamp.", "interface Printable {\n    void print();\n    default void log(){\n        System.out.println(\"[\"+java.time.LocalTime.now()+\"] \");\n        print();\n    }\n}\nclass Report implements Printable {\n    public void print(){ System.out.println(\"Report content\"); }\n}\nnew Report().log();"),
        ("Strategy Pattern", "Use interface to switch sorting strategy at runtime.", "interface SortStrategy { void sort(int[] arr); }\nclass BubbleSort implements SortStrategy {\n    public void sort(int[] a){\n        for(int i=0;i<a.length-1;i++)\n            for(int j=0;j<a.length-1-i;j++)\n                if(a[j]>a[j+1]){int t=a[j];a[j]=a[j+1];a[j+1]=t;}\n    }\n}\nint[] data={5,2,8,1};\nnew BubbleSort().sort(data);\nSystem.out.println(java.util.Arrays.toString(data));"),
    ])
}

# TOPIC 13: Exception Handling
jv['java_exceptions'] = {
    "title": "Exception Handling",
    "explanation": explanation("Exception Handling", [
        ("try-catch-finally",
         "Exceptions are runtime errors. Java uses try-catch-finally to handle them gracefully without crashing.",
         [("Basic exception handling", "public class Main {\n    public static void main(String[] args) {\n        try {\n            int[] arr = {1, 2, 3};\n            System.out.println(arr[10]); // ArrayIndexOutOfBoundsException\n        } catch (ArrayIndexOutOfBoundsException e) {\n            System.out.println(\"Index error: \" + e.getMessage());\n        } catch (Exception e) {\n            System.out.println(\"General: \" + e.getMessage());\n        } finally {\n            System.out.println(\"Finally always runs!\");\n        }\n    }\n}"),
          ("Multiple exceptions & try-with-resources", "// Multi-catch (Java 7+)\ntry {\n    String s = null;\n    s.length(); // NullPointerException\n} catch (NullPointerException | IllegalArgumentException e) {\n    System.out.println(\"Caught: \" + e.getClass().getSimpleName());\n}\n\n// try-with-resources (auto-close)\ntry (java.io.StringReader r = new java.io.StringReader(\"test\")) {\n    System.out.println((char) r.read());\n} catch (java.io.IOException e) {\n    e.printStackTrace();\n}")]),
        ("Checked vs Unchecked & Custom Exceptions",
         "Checked exceptions (must handle or declare): IOException, SQLException. Unchecked: NullPointerException, ArithmeticException. You can create custom exceptions.",
         [("Checked vs Unchecked", "// CHECKED: must handle or declare with throws\nvoid readFile() throws java.io.IOException {\n    // compiler forces you to handle this\n}\n\n// UNCHECKED: extends RuntimeException\nvoid divide(int a, int b) {\n    if (b == 0) throw new ArithmeticException(\"Zero division\");\n    System.out.println(a / b);\n}"),
          ("Custom exception", "class InsufficientFundsException extends Exception {\n    double amount;\n    InsufficientFundsException(double amount) {\n        super(\"Need Rs. \" + amount + \" more\");\n        this.amount = amount;\n    }\n}\n\nclass Account {\n    double balance = 1000;\n    void withdraw(double amt) throws InsufficientFundsException {\n        if (amt > balance)\n            throw new InsufficientFundsException(amt - balance);\n        balance -= amt;\n    }\n}\n\ntry { new Account().withdraw(1500); }\ncatch (InsufficientFundsException e) {\n    System.out.println(e.getMessage());\n}")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("finally block runs?", ["Only on success", "Only on exception", "Always — success or failure", "Only with return"], "Always — success or failure"),
        ("NullPointerException is?", ["Checked", "Unchecked (RuntimeException)", "Error", "Custom"], "Unchecked (RuntimeException)"),
        ("IOException is?", ["Unchecked", "Checked (must handle)", "Error", "Warning"], "Checked (must handle)"),
        ("Custom exception should extend?", ["Throwable", "Exception or RuntimeException", "Object", "Error"], "Exception or RuntimeException"),
        ("try-with-resources is used for?", ["Faster code", "Auto-closing resources like files/connections", "Catching checked exceptions", "Multiple catches"], "Auto-closing resources like files/connections"),
    ]),
    "hands_on": task("Safe Division", "Write a method safeDivide(a, b) that handles ArithmeticException and returns 0 on division by zero.", "Use try-catch inside the method.", "static double safeDivide(double a, double b) {\n    try {\n        return a / b;\n    } catch (ArithmeticException e) {\n        System.out.println(\"Cannot divide by zero!\");\n        return 0;\n    }\n}\nSystem.out.println(safeDivide(10, 2));  // 5.0\nSystem.out.println(safeDivide(10, 0)); // 0 (but double returns Infinity not exception)"),
    "problem_solving": problems([
        ("Stack Overflow", "Demonstrate StackOverflowError with infinite recursion (don't fix, just catch it).", "try {\n    infiniteRecursion();\n} catch (StackOverflowError e) {\n    System.out.println(\"Stack overflow caught!\");\n}"),
        ("Number Format Exception", "Parse user input safely — catch NumberFormatException if not a number.", "String input = \"abc\";\ntry {\n    int n = Integer.parseInt(input);\n    System.out.println(\"Number: \" + n);\n} catch (NumberFormatException e) {\n    System.out.println(\"Not a valid number!\");\n}"),
        ("Chained Exceptions", "Throw a custom exception caused by another exception.", "try {\n    try { int r=1/0; }\n    catch (ArithmeticException e) {\n        throw new RuntimeException(\"Calc failed\", e);\n    }\n} catch (RuntimeException e) {\n    System.out.println(e.getMessage());\n    System.out.println(\"Caused by: \"+e.getCause());\n}"),
    ])
}

# TOPIC 14: Collections Framework
jv['java_collections'] = {
    "title": "Collections Framework",
    "explanation": explanation("Collections Framework", [
        ("List — ArrayList & LinkedList",
         "List is an ordered, duplicate-allowed collection. ArrayList (backed by array, fast access). LinkedList (doubly-linked, fast insert/delete).",
         [("ArrayList", "import java.util.*;\n\nArrayList<String> list = new ArrayList<>();\nlist.add(\"Apple\");\nlist.add(\"Banana\");\nlist.add(\"Cherry\");\nlist.add(1, \"Blueberry\"); // insert at index\nlist.remove(\"Apple\");\n\nSystem.out.println(list.get(0));    // Blueberry\nSystem.out.println(list.size());    // 3\nSystem.out.println(list.contains(\"Cherry\")); // true\nCollections.sort(list);\nSystem.out.println(list);"),
          ("HashMap", "HashMap<String, Integer> scores = new HashMap<>();\nscores.put(\"Alice\", 95);\nscores.put(\"Bob\",   87);\nscores.put(\"Carol\", 92);\n\nSystem.out.println(scores.get(\"Bob\"));         // 87\nSystem.out.println(scores.containsKey(\"Alice\")); // true\nscores.putIfAbsent(\"Dave\", 80);\n\n// Iterate entries\nfor (Map.Entry<String,Integer> e : scores.entrySet()) {\n    System.out.println(e.getKey() + \" -> \" + e.getValue());\n}")]),
        ("Set & Queue",
         "Set: no duplicates. HashSet (unordered), TreeSet (sorted). Queue: FIFO. LinkedList implements Queue. PriorityQueue for ordering.",
         [("HashSet & TreeSet", "Set<Integer> hashSet = new HashSet<>();\nhashSet.add(3); hashSet.add(1); hashSet.add(2); hashSet.add(1);\nSystem.out.println(hashSet);         // {1,2,3} or similar (no order)\nSystem.out.println(hashSet.size()); // 3 (duplicate removed)\n\nTreeSet<Integer> sorted = new TreeSet<>(hashSet);\nSystem.out.println(sorted);          // [1, 2, 3] (sorted!)"),
          ("Queue & Stack", "Queue<String> queue = new LinkedList<>();\nqueue.offer(\"First\");\nqueue.offer(\"Second\");\nqueue.offer(\"Third\");\nSystem.out.println(queue.poll());   // First (FIFO)\nSystem.out.println(queue.peek());   // Second (look without remove)\n\nDeque<Integer> stack = new ArrayDeque<>();\nstack.push(1); stack.push(2); stack.push(3);\nSystem.out.println(stack.pop());  // 3 (LIFO)")]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("ArrayList allows duplicates?", ["No", "Yes", "Only for primitives", "Only for Strings"], "Yes"),
        ("HashSet guarantees ordering?", ["Yes, insertion order", "Yes, sorted", "No ordering", "Only with Comparator"], "No ordering"),
        ("HashMap key must be?", ["Unique", "Sorted", "Comparable", "String only"], "Unique"),
        ("Queue follows which principle?", ["LIFO", "FIFO", "Random", "Sorted"], "FIFO"),
        ("Which is fastest for random access?", ["LinkedList", "TreeSet", "ArrayList", "HashMap"], "ArrayList"),
    ]),
    "hands_on": task("Student Score Tracker", "Use HashMap to store student names and marks. Print sorted by name using TreeMap.", "TreeMap sorts by key automatically.", "import java.util.*;\nHashMap<String,Integer> scores=new HashMap<>();\nscores.put(\"Zara\",88); scores.put(\"Alice\",95); scores.put(\"Bob\",76);\n\n// Sort by name (key)\nnew TreeMap<>(scores).forEach((name,score)->\n    System.out.println(name+\": \"+score));"),
    "problem_solving": problems([
        ("Remove Duplicates using Set", "Remove duplicates from list [1,2,2,3,3,4,5,5].", "List<Integer> list=new ArrayList<>(Arrays.asList(1,2,2,3,3,4,5,5));\nSet<Integer> unique=new LinkedHashSet<>(list);\nSystem.out.println(new ArrayList<>(unique));"),
        ("Word Frequency Counter", "Count frequency of each word in 'the cat sat on the mat'.", "String[] words=\"the cat sat on the mat\".split(\" \");\nMap<String,Integer> freq=new HashMap<>();\nfor(String w:words) freq.merge(w,1,Integer::sum);\nfreq.forEach((w,c)->System.out.println(w+\":\"+c));"),
        ("Priority Queue min/max", "Find top 3 scores from list using PriorityQueue.", "int[] scores={78,92,55,88,45,95,67};\nPriorityQueue<Integer> pq=new PriorityQueue<>(Collections.reverseOrder());\nfor(int s:scores) pq.offer(s);\nSystem.out.print(\"Top 3: \");\nfor(int i=0;i<3;i++) System.out.print(pq.poll()+\" \");"),
    ])
}

print("Java Topics 10-14 done!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
