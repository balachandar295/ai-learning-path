import json

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

def ex(title, code, output, explanation):
    return {"title": title, "code": code, "output": output, "explanation": explanation}

FLUTTER = {
"flutter_basics": {
    "introduction": "<p><strong>Flutter</strong> is Google's open-source UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase. Unlike React Native (which bridges to native components), Flutter draws every pixel directly on a canvas using the Skia engine.</p><p>Flutter uses the <strong>Dart</strong> programming language and provides a rich set of pre-designed widgets following both Material Design (Android) and Cupertino (iOS) guidelines. Its <strong>hot reload</strong> feature lets you see changes instantly without losing application state.</p>",
    "subtopics": [
        {"title": "1. Why Flutter?", "content": "<p>Flutter's key advantages:</p><ul><li><strong>Single Codebase:</strong> Write once, deploy to iOS, Android, Web, and Desktop</li><li><strong>Hot Reload:</strong> See UI changes in milliseconds without restarting the app</li><li><strong>Custom UI:</strong> Pixel-perfect control over every visual element</li><li><strong>Performance:</strong> Compiles to native ARM code, runs at 60/120fps</li></ul>"},
        {"title": "2. Project Structure", "content": "<p>A Flutter project contains: <code>lib/</code> (your Dart code), <code>pubspec.yaml</code> (dependencies), <code>android/</code> and <code>ios/</code> (platform-specific code). The entry point is <code>lib/main.dart</code> with the <code>main()</code> function.</p>"},
        {"title": "3. Your First App", "content": "<p>Create a new project with <code>flutter create my_app</code>. The <code>main()</code> function calls <code>runApp()</code>, which takes a widget and makes it the root of the widget tree. Every visual element in Flutter is a widget.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Widget Tree:</strong> Flutter UIs are trees of nested widgets</li><li><strong>Hot Reload:</strong> Instant UI updates without losing state</li><li><strong>Dart Language:</strong> Flutter's programming language</li><li><strong>runApp():</strong> Starts the Flutter application with a root widget</li></ul>",
    "examples": [
        ex("Hello Flutter", "import 'package:flutter/material.dart';\n\nvoid main() {\n  runApp(\n    MaterialApp(\n      home: Scaffold(\n        appBar: AppBar(title: Text('My First App')),\n        body: Center(\n          child: Text('Hello, Flutter!',\n            style: TextStyle(fontSize: 24)),\n        ),\n      ),\n    ),\n  );\n}", "(Displays 'Hello, Flutter!' centered on screen with an app bar)", "MaterialApp sets up the Material theme. Scaffold provides the basic page structure with appBar and body. Center positions its child in the middle.")
    ]
},

"flutter_dart": {
    "introduction": "<p><strong>Dart</strong> is the programming language behind Flutter. Created by Google, Dart is object-oriented, strongly typed (with type inference), and uses C-style syntax familiar to Java/JavaScript developers.</p><p>Dart supports both <strong>JIT (Just-In-Time)</strong> compilation for fast development cycles (hot reload) and <strong>AOT (Ahead-Of-Time)</strong> compilation for optimized production apps. This dual compilation model is key to Flutter's developer experience and performance.</p>",
    "subtopics": [
        {"title": "1. Variables & Types", "content": "<p>Dart has type inference: <code>var name = 'Alice';</code> (inferred as String). Explicit types: <code>String name = 'Alice';</code>. Use <code>final</code> for runtime constants and <code>const</code> for compile-time constants.</p><p><code>dynamic</code> allows any type (like JavaScript), but prefer typed variables for safety.</p>"},
        {"title": "2. Functions", "content": "<p>Dart functions can use arrow syntax for single expressions: <code>int add(int a, int b) => a + b;</code>. Named parameters with curly braces: <code>void greet({required String name})</code>. Optional positional parameters with brackets.</p>"},
        {"title": "3. Null Safety", "content": "<p>Dart 2.12+ has sound null safety. Types are non-nullable by default. Add <code>?</code> for nullable: <code>String? name;</code>. Use <code>!</code> to assert non-null, <code>??</code> for default values, <code>?.</code> for safe access.</p>"}
    ],
    "key_concepts": "<ul><li><strong>var/final/const:</strong> Variable declaration keywords</li><li><strong>Null Safety:</strong> Non-nullable by default, use ? for nullable types</li><li><strong>Arrow Functions:</strong> Concise syntax for single-expression functions</li><li><strong>String Interpolation:</strong> Use $variable or ${expression} in strings</li></ul>",
    "examples": [
        ex("Dart Basics", "void main() {\n  var name = 'Alice';        // Type inferred\n  final int age = 25;        // Runtime constant\n  const pi = 3.14159;        // Compile-time constant\n\n  String? nickname;          // Nullable\n  print('$name is $age years old');\n  print(nickname ?? 'No nickname');\n}", "Alice is 25 years old\nNo nickname", "var infers the type. final can't be reassigned. String? is nullable. ?? provides a default when null.")
    ]
},

"flutter_widgets": {
    "introduction": "<p>In Flutter, <strong>everything is a widget</strong>. Buttons, text, padding, margins, layouts - they are all widgets composed together in a tree structure. Widgets are immutable descriptions of a part of the UI.</p><p>There are two main types: <strong>StatelessWidgets</strong> (never change after creation) and <strong>StatefulWidgets</strong> (can change based on user interaction or data). Understanding the widget lifecycle is fundamental to Flutter development.</p>",
    "subtopics": [
        {"title": "1. Common Widgets", "content": "<p>Essential widgets: <code>Text</code> (display text), <code>Container</code> (box with padding/margin/decoration), <code>Image</code> (display images), <code>Icon</code> (material icons), <code>ElevatedButton</code> (clickable button), <code>TextField</code> (text input).</p>"},
        {"title": "2. StatelessWidget", "content": "<p>StatelessWidget has a single <code>build()</code> method that returns a widget tree. It never changes after construction. Use for static content like labels, icons, and fixed layouts.</p>"},
        {"title": "3. Widget Composition", "content": "<p>Flutter's power comes from composing simple widgets into complex UIs. A custom widget is just a class that builds a tree of other widgets. This makes code reusable and testable.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Everything is a Widget:</strong> UI elements, layout, styling - all widgets</li><li><strong>StatelessWidget:</strong> Immutable, doesn't change after creation</li><li><strong>build() method:</strong> Returns the widget tree to render</li><li><strong>Composition:</strong> Build complex UIs by nesting simple widgets</li></ul>",
    "examples": [
        ex("Custom Widget", "class WelcomeCard extends StatelessWidget {\n  final String name;\n  const WelcomeCard({required this.name});\n\n  @override\n  Widget build(BuildContext context) {\n    return Card(\n      child: Padding(\n        padding: EdgeInsets.all(16),\n        child: Column(\n          children: [\n            Icon(Icons.person, size: 48),\n            Text('Welcome, $name!',\n              style: TextStyle(fontSize: 20)),\n          ],\n        ),\n      ),\n    );\n  }\n}", "(Displays a card with an icon and welcome message)", "WelcomeCard is a reusable widget accepting a name parameter. Card, Padding, Column, Icon, Text are all composed together.")
    ]
},

"flutter_layouts": {
    "introduction": "<p><strong>Layouts in Flutter</strong> are built using specialized layout widgets. Unlike CSS with its float/flexbox/grid model, Flutter uses widget-based layouts: <code>Row</code> (horizontal), <code>Column</code> (vertical), <code>Stack</code> (layered), and <code>Wrap</code> (wrapping flow).</p><p><code>Expanded</code> and <code>Flexible</code> control how children share available space. <code>SizedBox</code> adds fixed spacing between elements.</p>",
    "subtopics": [
        {"title": "1. Row & Column", "content": "<p><code>Row</code> arranges children horizontally. <code>Column</code> arranges vertically. Both accept <code>mainAxisAlignment</code> (primary direction) and <code>crossAxisAlignment</code> (perpendicular direction) for positioning.</p>"},
        {"title": "2. Expanded & Flexible", "content": "<p><code>Expanded</code> forces a child to fill all remaining space. <code>Flexible</code> lets a child take up to available space but can be smaller. Use <code>flex</code> property for proportional sizing: flex:2 gets twice the space of flex:1.</p>"},
        {"title": "3. Stack & Positioned", "content": "<p><code>Stack</code> layers widgets on top of each other (like CSS position:absolute). Use <code>Positioned</code> widget to place children at exact positions within the Stack. Great for overlays and badges.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Row/Column:</strong> Primary layout widgets for horizontal/vertical arrangement</li><li><strong>MainAxisAlignment:</strong> Spacing along the primary direction</li><li><strong>Expanded:</strong> Fill all remaining available space</li><li><strong>Stack:</strong> Layer widgets on top of each other</li></ul>",
    "examples": [
        ex("Row & Column Layout", "Column(\n  mainAxisAlignment: MainAxisAlignment.center,\n  children: [\n    Text('Title', style: TextStyle(fontSize: 24)),\n    SizedBox(height: 20),\n    Row(\n      mainAxisAlignment: MainAxisAlignment.spaceEvenly,\n      children: [\n        ElevatedButton(onPressed: () {}, child: Text('Yes')),\n        ElevatedButton(onPressed: () {}, child: Text('No')),\n      ],\n    ),\n  ],\n)", "(Centered title with two evenly spaced buttons below)", "Column centers children vertically. SizedBox adds 20px spacing. Row distributes buttons evenly using spaceEvenly.")
    ]
},

"flutter_stateful": {
    "introduction": "<p><strong>StatefulWidgets</strong> maintain mutable state that can change during the widget's lifetime. When state changes, the widget rebuilds its UI. This is how interactive elements like counters, forms, and animations work in Flutter.</p><p>A StatefulWidget has two classes: the widget itself (immutable) and its State object (mutable, persists across rebuilds). Call <code>setState()</code> to trigger a rebuild when data changes.</p>",
    "subtopics": [
        {"title": "1. StatefulWidget Structure", "content": "<p>Two parts: <code>class MyWidget extends StatefulWidget</code> (creates state) and <code>class _MyWidgetState extends State<MyWidget></code> (holds state and build logic). The underscore makes the State class private.</p>"},
        {"title": "2. setState()", "content": "<p><code>setState(() { counter++; })</code> tells Flutter that state has changed and the widget needs to rebuild. Only call setState for visible state changes. Never call setState in build() or after dispose().</p>"},
        {"title": "3. Lifecycle Methods", "content": "<p>Key lifecycle methods: <code>initState()</code> (called once, for initialization), <code>build()</code> (called on every rebuild), <code>dispose()</code> (cleanup when widget is removed). Override these for setup and teardown logic.</p>"}
    ],
    "key_concepts": "<ul><li><strong>setState():</strong> Triggers a rebuild with updated state</li><li><strong>initState():</strong> Initialize data when widget is first created</li><li><strong>dispose():</strong> Clean up resources when widget is removed</li><li><strong>Widget vs State:</strong> Widget is immutable config; State is mutable data</li></ul>",
    "examples": [
        ex("Counter App", "class CounterApp extends StatefulWidget {\n  @override\n  _CounterAppState createState() => _CounterAppState();\n}\n\nclass _CounterAppState extends State<CounterApp> {\n  int count = 0;\n\n  @override\n  Widget build(BuildContext context) {\n    return Column(\n      mainAxisAlignment: MainAxisAlignment.center,\n      children: [\n        Text('Count: $count', style: TextStyle(fontSize: 32)),\n        ElevatedButton(\n          onPressed: () => setState(() => count++),\n          child: Text('Increment'),\n        ),\n      ],\n    );\n  }\n}", "(Counter increments on each button press)", "setState() updates count and triggers rebuild. The Text widget re-renders with the new value. The button stays the same.")
    ]
},

"flutter_forms": {
    "introduction": "<p><strong>Forms and Input</strong> in Flutter use <code>TextField</code>, <code>TextFormField</code>, and the <code>Form</code> widget for structured input collection and validation. Forms are essential for login screens, registration, settings, and any data entry.</p><p>Use <code>TextEditingController</code> to read/set TextField values programmatically, and <code>GlobalKey&lt;FormState&gt;</code> to validate and save all form fields at once.</p>",
    "subtopics": [
        {"title": "1. TextField & Controller", "content": "<p><code>TextField</code> provides a text input. Attach a <code>TextEditingController</code> to access the value: <code>controller.text</code>. Don't forget to <code>dispose()</code> the controller to prevent memory leaks.</p>"},
        {"title": "2. Form Validation", "content": "<p>Wrap fields in a <code>Form</code> widget and use <code>TextFormField</code> with a <code>validator:</code> callback. Call <code>formKey.currentState!.validate()</code> to check all validators at once. Return null for valid, error string for invalid.</p>"},
        {"title": "3. Input Decoration", "content": "<p><code>InputDecoration</code> customizes appearance: <code>labelText</code>, <code>hintText</code>, <code>prefixIcon</code>, <code>border</code>, <code>errorStyle</code>. Use <code>OutlineInputBorder</code> for bordered fields or <code>UnderlineInputBorder</code> for simple underlines.</p>"}
    ],
    "key_concepts": "<ul><li><strong>TextEditingController:</strong> Read and control text field values</li><li><strong>TextFormField:</strong> TextField with built-in validation support</li><li><strong>GlobalKey&lt;FormState&gt;:</strong> Access form state for validation</li><li><strong>validator:</strong> Returns null (valid) or error string (invalid)</li></ul>",
    "examples": [
        ex("Form Validation", "final _formKey = GlobalKey<FormState>();\nfinal _emailCtrl = TextEditingController();\n\nForm(\n  key: _formKey,\n  child: Column(children: [\n    TextFormField(\n      controller: _emailCtrl,\n      decoration: InputDecoration(labelText: 'Email'),\n      validator: (val) {\n        if (val == null || !val.contains('@'))\n          return 'Enter a valid email';\n        return null;\n      },\n    ),\n    ElevatedButton(\n      onPressed: () {\n        if (_formKey.currentState!.validate()) {\n          print('Valid: ${_emailCtrl.text}');\n        }\n      },\n      child: Text('Submit'),\n    ),\n  ]),\n)", "(Shows error if email is invalid, prints email if valid)", "The validator function validates on submit. TextFormField shows the error message below the field automatically.")
    ]
},

"flutter_routes": {
    "introduction": "<p><strong>Navigation</strong> in Flutter uses a <code>Navigator</code> that manages a stack of <code>Route</code> objects. Push a route to navigate forward, pop to go back. Flutter supports both unnamed routes (inline) and named routes (defined in MaterialApp).</p><p>For complex apps, consider using packages like <code>go_router</code> or <code>auto_route</code> for declarative, URL-based routing.</p>",
    "subtopics": [
        {"title": "1. Basic Navigation", "content": "<p>Push a new screen: <code>Navigator.push(context, MaterialPageRoute(builder: (_) => DetailPage()))</code>. Go back: <code>Navigator.pop(context)</code>. The navigator maintains a LIFO stack of routes.</p>"},
        {"title": "2. Named Routes", "content": "<p>Define routes in MaterialApp: <code>routes: {'/detail': (_) => DetailPage()}</code>. Navigate with <code>Navigator.pushNamed(context, '/detail')</code>. Pass arguments with <code>arguments:</code> parameter.</p>"},
        {"title": "3. Passing Data", "content": "<p>Pass data via constructor: <code>MaterialPageRoute(builder: (_) => DetailPage(item: myItem))</code>. Or via named route arguments: <code>pushNamed(context, '/detail', arguments: myItem)</code> and retrieve with <code>ModalRoute.of(context)!.settings.arguments</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Navigator.push():</strong> Navigate to a new screen</li><li><strong>Navigator.pop():</strong> Go back to the previous screen</li><li><strong>Named Routes:</strong> Define route map in MaterialApp for organized navigation</li><li><strong>Arguments:</strong> Pass data between routes via constructors or settings</li></ul>",
    "examples": [
        ex("Navigation", "// Navigate forward\nNavigator.push(\n  context,\n  MaterialPageRoute(\n    builder: (context) => DetailScreen(title: 'Flutter'),\n  ),\n);\n\n// Navigate back\nNavigator.pop(context);\n\n// Named routes (defined in MaterialApp)\nNavigator.pushNamed(context, '/settings');", "(Navigates between screens)", "push() adds a new screen to the stack. pop() removes the current screen. Named routes provide a centralized route map.")
    ]
},

"flutter_state": {
    "introduction": "<p><strong>State Management</strong> is how your Flutter app manages, shares, and updates data across multiple widgets. Simple apps can use setState(), but as apps grow, you need more structured approaches to avoid prop drilling and spaghetti code.</p><p>Popular state management solutions: <code>Provider</code> (officially recommended), <code>Riverpod</code> (Provider evolution), <code>Bloc</code> (event-driven), <code>GetX</code> (lightweight). Each has trade-offs in complexity, boilerplate, and testability.</p>",
    "subtopics": [
        {"title": "1. The Problem", "content": "<p>Without proper state management, you'd pass data through constructors down many widget layers (prop drilling). Changes at the bottom would require calling setState at the top, rebuilding everything. This is inefficient and hard to maintain.</p>"},
        {"title": "2. InheritedWidget", "content": "<p><code>InheritedWidget</code> is Flutter's built-in mechanism for sharing data down the tree. Widgets below can access data without it being passed through every intermediary. Provider is built on top of InheritedWidget.</p>"},
        {"title": "3. Choosing a Solution", "content": "<p>For simple apps: setState. For medium apps: Provider or Riverpod. For large enterprise apps: Bloc or Redux. The key is to separate UI from business logic and make state changes predictable and testable.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Prop Drilling:</strong> Passing data through many widget layers (antipattern)</li><li><strong>InheritedWidget:</strong> Flutter's built-in data sharing mechanism</li><li><strong>Provider:</strong> Wrapper around InheritedWidget, officially recommended</li><li><strong>Separation:</strong> Keep UI logic separate from business logic</li></ul>",
    "examples": [
        ex("State Management Concept", "// Without state management (prop drilling)\nclass App extends StatelessWidget {\n  final String username = 'Alice';\n  Widget build(ctx) => HomePage(username: username);\n}\nclass HomePage extends StatelessWidget {\n  final String username;\n  // ...passes username to every child\n}\n\n// With Provider (any widget can access)\n// Provider.of<UserModel>(context).username", "(Conceptual - shows prop drilling vs Provider pattern)", "Provider eliminates prop drilling by making data accessible to any widget in the tree without passing through intermediaries.")
    ]
},

"flutter_provider": {
    "introduction": "<p><strong>Provider</strong> is the officially recommended state management solution for Flutter. It wraps InheritedWidget, making it easy to share state across widgets, listen for changes, and rebuild only the parts of the UI that need updating.</p><p>Key concepts: <code>ChangeNotifier</code> (the model), <code>ChangeNotifierProvider</code> (makes model available), <code>Consumer</code> or <code>context.watch()</code> (reads and listens for changes).</p>",
    "subtopics": [
        {"title": "1. ChangeNotifier", "content": "<p>Create a model class extending <code>ChangeNotifier</code>. When data changes, call <code>notifyListeners()</code> to trigger rebuilds in listening widgets. This is your business logic layer.</p>"},
        {"title": "2. Providing State", "content": "<p>Wrap your app (or a subtree) with <code>ChangeNotifierProvider</code>: <code>ChangeNotifierProvider(create: (_) => CartModel(), child: MyApp())</code>. This makes CartModel available to all descendants.</p>"},
        {"title": "3. Consuming State", "content": "<p>Read state with <code>context.watch&lt;CartModel&gt;()</code> (rebuilds on change) or <code>context.read&lt;CartModel&gt;()</code> (one-time read, no rebuild). Consumer widget provides finer control over rebuilds.</p>"}
    ],
    "key_concepts": "<ul><li><strong>ChangeNotifier:</strong> Model class that notifies listeners on changes</li><li><strong>ChangeNotifierProvider:</strong> Makes a model available to the widget tree</li><li><strong>context.watch():</strong> Listens and rebuilds on changes</li><li><strong>context.read():</strong> One-time read without listening</li></ul>",
    "examples": [
        ex("Provider Setup", "class CartModel extends ChangeNotifier {\n  final List<String> _items = [];\n  List<String> get items => _items;\n  int get count => _items.length;\n\n  void add(String item) {\n    _items.add(item);\n    notifyListeners(); // Triggers rebuild\n  }\n}\n\n// In main.dart:\nChangeNotifierProvider(\n  create: (_) => CartModel(),\n  child: MaterialApp(home: ShopPage()),\n)\n\n// In any widget:\nfinal cart = context.watch<CartModel>();\nText('Items: ${cart.count}');", "(Cart count updates automatically when items are added)", "CartModel extends ChangeNotifier. When add() is called, notifyListeners() triggers all watching widgets to rebuild with the new count.")
    ]
},

"flutter_http": {
    "introduction": "<p><strong>Networking</strong> in Flutter uses the <code>http</code> package for REST API calls or the more powerful <code>dio</code> package. All network operations are <strong>asynchronous</strong>, using Dart's <code>async/await</code> syntax with <code>Future</code> objects.</p><p>Handle network states properly: loading, success, and error. Use <code>FutureBuilder</code> to connect async data fetching directly to your widget tree.</p>",
    "subtopics": [
        {"title": "1. HTTP Requests", "content": "<p>Add <code>http</code> package to pubspec.yaml. Use <code>http.get()</code>, <code>http.post()</code>, etc. All return <code>Future&lt;Response&gt;</code>. Check <code>response.statusCode</code> for success (200) and parse <code>response.body</code> as JSON.</p>"},
        {"title": "2. FutureBuilder", "content": "<p><code>FutureBuilder</code> automatically renders different widgets based on the future's state: <code>ConnectionState.waiting</code> (show loading), <code>snapshot.hasError</code> (show error), <code>snapshot.hasData</code> (show data).</p>"},
        {"title": "3. Error Handling", "content": "<p>Wrap network calls in try/catch for connection errors. Check status codes for HTTP errors. Use timeout to prevent hanging requests: <code>http.get(url).timeout(Duration(seconds: 10))</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>async/await:</strong> Handle asynchronous network operations</li><li><strong>FutureBuilder:</strong> Connect async data to widget tree</li><li><strong>jsonDecode:</strong> Parse JSON response body into Dart maps/lists</li><li><strong>Error handling:</strong> try/catch + status code checking</li></ul>",
    "examples": [
        ex("API Call", "import 'package:http/http.dart' as http;\nimport 'dart:convert';\n\nFuture<List<dynamic>> fetchUsers() async {\n  final response = await http.get(\n    Uri.parse('https://jsonplaceholder.typicode.com/users'),\n  );\n  if (response.statusCode == 200) {\n    return jsonDecode(response.body);\n  } else {\n    throw Exception('Failed to load users');\n  }\n}", "(Returns a list of user objects from the API)", "async/await makes the code read sequentially. Check statusCode for success. jsonDecode converts JSON string to Dart objects.")
    ]
},

"flutter_json": {
    "introduction": "<p><strong>JSON Serialization</strong> in Flutter involves converting JSON strings to Dart objects and vice versa. Since Dart is strongly typed, you need to map JSON fields to typed Dart classes for type safety and IDE support.</p><p>For simple projects, use manual serialization with <code>jsonDecode()</code> and factory constructors. For large projects, use code generation with <code>json_serializable</code> package.</p>",
    "subtopics": [
        {"title": "1. Manual Serialization", "content": "<p>Create a model class with a <code>fromJson()</code> factory constructor and a <code>toJson()</code> method. <code>fromJson</code> takes a <code>Map&lt;String, dynamic&gt;</code> and creates an object. <code>toJson</code> does the reverse.</p>"},
        {"title": "2. Code Generation", "content": "<p>For complex models, use <code>json_serializable</code>. Add annotations <code>@JsonSerializable()</code> to your class, run <code>flutter pub run build_runner build</code>, and it generates the serialization code automatically.</p>"},
        {"title": "3. Nested Objects", "content": "<p>For nested JSON (objects within objects), each nested object needs its own model class with fromJson/toJson. In the parent's fromJson, call <code>ChildModel.fromJson(json['child'])</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>jsonDecode():</strong> Converts JSON string to Dart Map</li><li><strong>fromJson():</strong> Factory constructor creating object from Map</li><li><strong>toJson():</strong> Converts object back to Map for serialization</li><li><strong>json_serializable:</strong> Code generation for complex models</li></ul>",
    "examples": [
        ex("JSON Model", "class User {\n  final int id;\n  final String name;\n  final String email;\n\n  User({required this.id, required this.name, required this.email});\n\n  factory User.fromJson(Map<String, dynamic> json) {\n    return User(\n      id: json['id'],\n      name: json['name'],\n      email: json['email'],\n    );\n  }\n\n  Map<String, dynamic> toJson() => {\n    'id': id, 'name': name, 'email': email,\n  };\n}", "(Creates typed User objects from JSON data)", "fromJson maps JSON keys to Dart fields. toJson converts back for API requests. Both ensure type safety throughout.")
    ]
},

"flutter_sharedpref": {
    "introduction": "<p><strong>Shared Preferences</strong> provides persistent key-value storage for simple data like user settings, theme preferences, and login tokens. Data persists across app restarts but is not encrypted or suitable for sensitive data.</p><p>The <code>shared_preferences</code> package wraps platform-specific storage: NSUserDefaults on iOS, SharedPreferences on Android.</p>",
    "subtopics": [
        {"title": "1. Reading & Writing", "content": "<p>Get instance: <code>final prefs = await SharedPreferences.getInstance();</code>. Write: <code>prefs.setString('key', 'value')</code>, <code>prefs.setInt()</code>, <code>prefs.setBool()</code>. Read: <code>prefs.getString('key')</code> (returns null if not set).</p>"},
        {"title": "2. Use Cases", "content": "<p>Perfect for: theme mode (dark/light), language preference, onboarding completion flag, auth token cache. NOT for: large data, sensitive data, or complex relational data (use SQLite or Hive instead).</p>"},
        {"title": "3. Removing Data", "content": "<p>Delete specific key: <code>prefs.remove('key')</code>. Clear all: <code>prefs.clear()</code>. Always check for null when reading since keys may not exist yet.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Key-Value Storage:</strong> Simple string-based keys mapping to typed values</li><li><strong>Persist Across Restarts:</strong> Data survives app closes</li><li><strong>Async API:</strong> getInstance() and all operations are asynchronous</li><li><strong>Limited Types:</strong> Supports String, int, double, bool, List&lt;String&gt;</li></ul>",
    "examples": [
        ex("Save & Load Settings", "final prefs = await SharedPreferences.getInstance();\n\n// Save\nawait prefs.setBool('darkMode', true);\nawait prefs.setString('username', 'Alice');\n\n// Load\nbool? isDark = prefs.getBool('darkMode');\nString? user = prefs.getString('username');\n\nprint('Dark mode: $isDark, User: $user');", "Dark mode: true, User: Alice", "SharedPreferences stores key-value pairs persistently. Values are typed (setBool, getString). Returns null if key doesn't exist.")
    ]
},

"flutter_firebase": {
    "introduction": "<p><strong>Firebase</strong> provides a suite of backend services that integrate seamlessly with Flutter: Authentication (login/signup), Cloud Firestore (real-time database), Storage (file uploads), and Cloud Messaging (push notifications).</p><p>The <code>firebase_core</code> package initializes Firebase, and each service has its own plugin (firebase_auth, cloud_firestore, etc.). FlutterFire is the official set of Firebase plugins for Flutter.</p>",
    "subtopics": [
        {"title": "1. Setup & Initialization", "content": "<p>Install Firebase CLI, run <code>flutterfire configure</code> to generate config files. Call <code>await Firebase.initializeApp()</code> in main() before runApp(). This connects your app to your Firebase project.</p>"},
        {"title": "2. Authentication", "content": "<p>Firebase Auth supports email/password, Google Sign-In, Apple, phone number, and anonymous auth. Use <code>FirebaseAuth.instance.signInWithEmailAndPassword()</code>. Listen to auth state changes with <code>authStateChanges()</code> stream.</p>"},
        {"title": "3. Cloud Firestore", "content": "<p>Firestore is a real-time NoSQL database. Collections contain documents with fields. Use <code>FirebaseFirestore.instance.collection('users').add({...})</code> to write, and <code>.snapshots()</code> to listen for real-time updates.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Firebase.initializeApp():</strong> Must be called before using any Firebase service</li><li><strong>FirebaseAuth:</strong> User authentication and session management</li><li><strong>Cloud Firestore:</strong> Real-time NoSQL database with offline support</li><li><strong>Streams:</strong> Listen to real-time data changes with snapshots()</li></ul>",
    "examples": [
        ex("Firestore CRUD", "// Add a document\nawait FirebaseFirestore.instance\n  .collection('users')\n  .add({'name': 'Alice', 'age': 25});\n\n// Read all documents\nfinal snapshot = await FirebaseFirestore.instance\n  .collection('users')\n  .get();\n\nfor (var doc in snapshot.docs) {\n  print('${doc.id}: ${doc.data()}');\n}", "(Adds a user document and prints all users)", "Firestore uses collections and documents. add() creates a new document with auto-generated ID. get() fetches all documents in a collection.")
    ]
},

"flutter_animations": {
    "introduction": "<p><strong>Animations</strong> in Flutter make your app feel polished and responsive. Flutter provides two animation approaches: <strong>implicit</strong> animations (simple, automatic) and <strong>explicit</strong> animations (full control with AnimationController).</p><p>Implicit animations (AnimatedContainer, AnimatedOpacity) handle the animation automatically when a property changes. Explicit animations use Tween, AnimationController, and AnimatedBuilder for complex sequences.</p>",
    "subtopics": [
        {"title": "1. Implicit Animations", "content": "<p>Simply change a property and the widget animates to the new value. <code>AnimatedContainer</code>, <code>AnimatedOpacity</code>, <code>AnimatedPadding</code>, <code>AnimatedAlign</code>. Set <code>duration:</code> to control animation speed.</p>"},
        {"title": "2. AnimationController", "content": "<p>For explicit animations: create an <code>AnimationController</code> with <code>vsync: this</code> (requires TickerProviderStateMixin). Use <code>.forward()</code>, <code>.reverse()</code>, <code>.repeat()</code> to control playback. Dispose in dispose() method.</p>"},
        {"title": "3. Tween Animations", "content": "<p>A <code>Tween</code> defines the range of values: <code>Tween(begin: 0.0, end: 1.0).animate(controller)</code>. Use <code>CurvedAnimation</code> for easing: <code>CurvedAnimation(parent: controller, curve: Curves.easeInOut)</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Implicit:</strong> Automatic animation when property changes (simple)</li><li><strong>Explicit:</strong> Full control with AnimationController (complex)</li><li><strong>Tween:</strong> Defines the range of animated values</li><li><strong>Curves:</strong> Easing functions like easeIn, easeOut, bounceIn</li></ul>",
    "examples": [
        ex("Implicit Animation", "AnimatedContainer(\n  duration: Duration(milliseconds: 500),\n  curve: Curves.easeInOut,\n  width: _expanded ? 300 : 100,\n  height: _expanded ? 300 : 100,\n  color: _expanded ? Colors.blue : Colors.red,\n  child: Center(child: Text('Tap me')),\n)", "(Container smoothly animates size and color changes)", "When _expanded changes via setState(), AnimatedContainer smoothly transitions between the old and new values over 500ms.")
    ]
},

"flutter_responsive": {
    "introduction": "<p><strong>Responsive Design</strong> ensures your Flutter app looks great on all screen sizes - phones, tablets, and desktops. Use <code>MediaQuery</code> to get screen dimensions, <code>LayoutBuilder</code> to adapt to available space, and <code>OrientationBuilder</code> for portrait/landscape changes.</p><p>Flutter's flexible layout system with Row, Column, Expanded, and Wrap makes building responsive UIs straightforward compared to CSS media queries.</p>",
    "subtopics": [
        {"title": "1. MediaQuery", "content": "<p><code>MediaQuery.of(context).size.width</code> gives the screen width. Use it to choose different layouts: single column on phones, multi-column on tablets. Also provides <code>padding</code>, <code>orientation</code>, and <code>platformBrightness</code>.</p>"},
        {"title": "2. LayoutBuilder", "content": "<p><code>LayoutBuilder</code> provides the parent's constraints (max width/height). It rebuilds when constraints change, making it ideal for adaptive layouts within specific widget areas.</p>"},
        {"title": "3. Adaptive Widgets", "content": "<p>Use <code>Wrap</code> instead of Row for content that should wrap to the next line. <code>AspectRatio</code> maintains proportions. <code>FractionallySizedBox</code> sizes relative to the parent (e.g., 50% width).</p>"}
    ],
    "key_concepts": "<ul><li><strong>MediaQuery:</strong> Access screen size, orientation, and platform info</li><li><strong>LayoutBuilder:</strong> Build based on parent constraints</li><li><strong>Breakpoints:</strong> Switch layouts at specific width thresholds</li><li><strong>Wrap:</strong> Automatically wraps content to next line when space runs out</li></ul>",
    "examples": [
        ex("Responsive Layout", "LayoutBuilder(\n  builder: (context, constraints) {\n    if (constraints.maxWidth > 600) {\n      return Row(children: [\n        Expanded(child: Sidebar()),\n        Expanded(flex: 3, child: Content()),\n      ]);\n    } else {\n      return Column(children: [Content()]);\n    }\n  },\n)", "(Shows sidebar+content on tablets, content-only on phones)", "LayoutBuilder checks available width. Above 600px it shows a two-column layout with sidebar. Below, it shows single column.")
    ]
},

"flutter_platform": {
    "introduction": "<p><strong>Platform-Specific Code</strong> lets you use native iOS and Android APIs that Flutter doesn't expose. Platform channels provide a bridge between Dart and native Swift/Kotlin/Java code. You can also detect the platform to show different UI.</p><p>Use <code>Platform.isIOS</code> / <code>Platform.isAndroid</code> for simple platform checks, and <code>MethodChannel</code> for calling native code.</p>",
    "subtopics": [
        {"title": "1. Platform Detection", "content": "<p>Import <code>dart:io</code> and use <code>Platform.isAndroid</code>, <code>Platform.isIOS</code>, <code>Platform.isWeb</code>. Show Material widgets on Android and Cupertino widgets on iOS for a native feel.</p>"},
        {"title": "2. Platform Channels", "content": "<p><code>MethodChannel</code> sends messages between Dart and native code. Define a channel name, invoke methods from Dart, and handle them in Swift/Kotlin. Used for camera, sensors, biometrics, etc.</p>"},
        {"title": "3. Conditional Imports", "content": "<p>For web vs mobile differences, use conditional imports: <code>import 'stub.dart' if (dart.library.html) 'web.dart';</code>. This lets you use different implementations based on the platform.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Platform.isAndroid/isIOS:</strong> Check the running platform</li><li><strong>MethodChannel:</strong> Bridge between Dart and native code</li><li><strong>Cupertino Widgets:</strong> iOS-style widgets for native iOS look</li><li><strong>kIsWeb:</strong> Check if running on web platform</li></ul>",
    "examples": [
        ex("Platform Check", "import 'dart:io';\n\nWidget buildButton() {\n  if (Platform.isIOS) {\n    return CupertinoButton(\n      child: Text('iOS Button'),\n      onPressed: () {},\n    );\n  } else {\n    return ElevatedButton(\n      child: Text('Android Button'),\n      onPressed: () {},\n    );\n  }\n}", "(Shows iOS-style button on iPhone, Material button on Android)", "Platform detection shows the appropriate native-looking UI. CupertinoButton follows iOS design, ElevatedButton follows Material Design.")
    ]
},

"flutter_deploy": {
    "introduction": "<p><strong>Deployment</strong> is the final step - building your Flutter app for production and distributing it to users. Flutter compiles Dart to native ARM machine code (mobile) or JavaScript (web), producing optimized, fast applications.</p><p>Build commands: <code>flutter build apk</code> (Android), <code>flutter build appbundle</code> (Play Store), <code>flutter build ios</code> (iOS), <code>flutter build web</code> (web deployment).</p>",
    "subtopics": [
        {"title": "1. Android Release", "content": "<p>Generate a signing key, configure <code>android/app/build.gradle</code>, and run <code>flutter build appbundle</code> for Play Store or <code>flutter build apk --release</code> for direct distribution. The bundle is smaller since Play Store generates device-specific APKs.</p>"},
        {"title": "2. iOS Release", "content": "<p>Requires a Mac, Xcode, and an Apple Developer account ($99/year). Configure signing in Xcode, then run <code>flutter build ios</code>. Upload to App Store Connect using Xcode or Transporter.</p>"},
        {"title": "3. Web Deployment", "content": "<p><code>flutter build web</code> generates static files in <code>build/web/</code>. Deploy to any web host: Firebase Hosting, Vercel, Netlify, or GitHub Pages. Consider SEO and initial load time for web apps.</p>"}
    ],
    "key_concepts": "<ul><li><strong>AOT Compilation:</strong> Dart compiles to native code for release builds</li><li><strong>App Bundle:</strong> Preferred format for Google Play (smaller downloads)</li><li><strong>Code Signing:</strong> Required for both Android and iOS releases</li><li><strong>flutter build:</strong> Command for creating production builds</li></ul>",
    "examples": [
        ex("Build Commands", "# Android APK\nflutter build apk --release\n\n# Android App Bundle (Play Store)\nflutter build appbundle\n\n# iOS\nflutter build ios --release\n\n# Web\nflutter build web\n\n# Check available devices\nflutter devices", "(Build artifacts are generated in the build/ directory)", "Each command produces optimized output. --release enables AOT compilation and tree-shaking, removing unused code for smaller binaries.")
    ]
},

"flutter_interview": {
    "introduction": "<p><strong>Flutter Interview Preparation</strong> covers the most commonly asked questions in Flutter developer interviews: widget lifecycle, state management, performance optimization, and Dart language features.</p><p>Interviewers test both theoretical knowledge (widget tree vs element tree vs render tree) and practical skills (building responsive UIs, handling async data, optimizing rebuilds).</p>",
    "subtopics": [
        {"title": "1. Common Questions", "content": "<p>Top topics: StatelessWidget vs StatefulWidget. Widget vs Element vs RenderObject trees. Hot reload vs hot restart. BuildContext explained. Keys and their importance. State management approaches comparison.</p>"},
        {"title": "2. Performance", "content": "<p>Optimization tips: use const constructors, avoid rebuilding entire trees (use Consumer/Selector), cache expensive computations, use ListView.builder for long lists (lazy loading), profile with DevTools.</p>"},
        {"title": "3. Architecture", "content": "<p>Know clean architecture patterns: separate UI, business logic, and data layers. Repository pattern for data access. Dependency injection for testability. Understanding when to use which state management solution.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Three Trees:</strong> Widget tree, Element tree, Render tree</li><li><strong>Keys:</strong> Preserve state when widgets move in the tree</li><li><strong>const Widgets:</strong> Prevent unnecessary rebuilds</li><li><strong>ListView.builder:</strong> Lazy loading for performance</li></ul>",
    "examples": [
        ex("Interview: Widget Lifecycle", "class MyWidget extends StatefulWidget {\n  @override\n  _MyWidgetState createState() => _MyWidgetState();\n}\n\nclass _MyWidgetState extends State<MyWidget> {\n  @override\n  void initState() {\n    super.initState();\n    // Called once when widget is inserted\n  }\n\n  @override\n  Widget build(BuildContext context) {\n    // Called on every rebuild\n    return Container();\n  }\n\n  @override\n  void dispose() {\n    // Called when widget is removed\n    super.dispose();\n  }\n}", "(Lifecycle methods are called in order: initState -> build -> dispose)", "Understanding the widget lifecycle is crucial. initState for setup, build for UI, dispose for cleanup. Key interview topic.")
    ]
}
}

RUBY_EXTRA = {
"ruby_strings": {
    "introduction": "<p><strong>Ruby Strings</strong> are mutable sequences of characters - unlike Python or Java, you can modify a Ruby string in place. Ruby provides both single-quoted strings (literal, no interpolation) and double-quoted strings (support interpolation and escape sequences).</p><p>String manipulation is one of Ruby's strongest features, with dozens of built-in methods like <code>.upcase</code>, <code>.reverse</code>, <code>.gsub</code>, <code>.split</code>, and <code>.strip</code>.</p>",
    "subtopics": [
        {"title": "1. String Interpolation", "content": "<p>Ruby's <code>#{expression}</code> syntax embeds any expression inside double-quoted strings: <code>\"Hello, #{name}!\"</code>. This is cleaner than concatenation and automatically calls <code>.to_s</code> on non-string values.</p>"},
        {"title": "2. String Methods", "content": "<p>Methods ending with <code>!</code> modify the string in place: <code>str.upcase!</code>. Without <code>!</code>, they return a new string.Common methods: <code>.length</code>, <code>.include?</code>, <code>.gsub</code> (global substitute), <code>.split</code>, <code>.chars</code>, <code>.freeze</code>.</p>"},
        {"title": "3. Symbols vs Strings", "content": "<p>Symbols (<code>:name</code>) are immutable, memory-efficient identifiers. Two symbols with the same name are the same object in memory. Use symbols for hash keys and identifiers; strings for text that changes.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Mutable:</strong> Ruby strings can be modified in place (unlike Java/Python)</li><li><strong>Interpolation:</strong> #{expression} in double-quoted strings</li><li><strong>Bang Methods (!):</strong> Modify the string in place</li><li><strong>Symbols:</strong> Immutable identifiers, more efficient than strings for keys</li></ul>",
    "examples": [
        ex("String Operations", 'name = "Alice"\nputs "Hello, #{name}!"\nputs name.upcase\nputs name.reverse\nputs name.chars.to_a.inspect\nputs "hello world".split(" ").inspect', "Hello, Alice!\nALICE\necilA\n[\"A\", \"l\", \"i\", \"c\", \"e\"]\n[\"hello\", \"world\"]", "Interpolation with #{}. upcase returns a new string. reverse flips characters. chars breaks into array of characters. split divides by delimiter.")
    ]
},

"ruby_control": {
    "introduction": "<p><strong>Control Flow</strong> in Ruby is elegant and readable. Beyond standard <code>if/elsif/else</code>, Ruby introduces <code>unless</code> (inverse of if), <code>case/when</code> (pattern matching), and modifier syntax (<code>puts 'hi' if happy</code>).</p><p>Ruby treats everything except <code>false</code> and <code>nil</code> as truthy - even <code>0</code> and empty strings are truthy, unlike JavaScript or Python!</p>",
    "subtopics": [
        {"title": "1. if/elsif/else & unless", "content": "<p><code>if</code> works as expected. <code>unless</code> is the opposite - executes when the condition is false: <code>unless logged_in then redirect end</code>. This reads more naturally for negative conditions.</p><p>Modifier form: <code>puts 'adult' if age >= 18</code> puts the condition after the action.</p>"},
        {"title": "2. case/when", "content": "<p>Ruby's <code>case</code> is more powerful than C/Java switch. It uses <code>===</code> for matching, so it works with ranges (<code>when 1..10</code>), classes (<code>when String</code>), and regex (<code>when /pattern/</code>).</p>"},
        {"title": "3. Ternary & Conditional Assignment", "content": "<p>Ternary operator: <code>result = age >= 18 ? 'adult' : 'minor'</code>. Conditional assignment: <code>name ||= 'default'</code> assigns only if name is nil or false. <code>&&=</code> assigns only if the value is truthy.</p>"}
    ],
    "key_concepts": "<ul><li><strong>unless:</strong> Execute when condition is false (opposite of if)</li><li><strong>Truthy:</strong> Everything except false and nil is truthy (even 0!)</li><li><strong>case/when:</strong> Uses === for matching (ranges, classes, regex)</li><li><strong>Modifier syntax:</strong> Condition after the statement for one-liners</li></ul>",
    "examples": [
        ex("unless & case", "age = 15\nunless age >= 18\n  puts 'Cannot vote yet'\nend\n\nscore = 85\ngrade = case score\n  when 90..100 then 'A'\n  when 80..89 then 'B'\n  when 70..79 then 'C'\n  else 'F'\nend\nputs grade", "Cannot vote yet\nB", "unless executes when condition is false. case/when matches ranges using ===. The then keyword is optional with newlines.")
    ]
},

"ruby_arrays": {
    "introduction": "<p><strong>Ruby Arrays</strong> are ordered, integer-indexed collections of any object. They are dynamic (auto-resize), can hold mixed types, and come with an extraordinarily rich set of built-in methods - over 100 methods for manipulating data.</p><p>Ruby's <code>.each</code>, <code>.map</code>, <code>.select</code>, and <code>.reduce</code> blocks are favored over traditional for-loops. The <strong>shovel operator</strong> (<code>&lt;&lt;</code>) appends elements and is the idiomatic way to add to arrays.</p>",
    "subtopics": [
        {"title": "1. Creating & Accessing", "content": "<p>Create with literals: <code>arr = [1, 'hello', true]</code>. Access by index: <code>arr[0]</code>. Negative indices count from the end: <code>arr[-1]</code> is the last element. Ranges: <code>arr[1..3]</code> gives a sub-array.</p>"},
        {"title": "2. Iteration with Blocks", "content": "<p><code>.each { |item| ... }</code> iterates without creating a new array. <code>.map { |item| ... }</code> transforms each element into a new array. <code>.select { |item| ... }</code> filters elements (like JavaScript's filter).</p>"},
        {"title": "3. Common Methods", "content": "<p>Key methods: <code>.push</code>/<code>&lt;&lt;</code> (append), <code>.pop</code> (remove last), <code>.flatten</code> (nested to flat), <code>.uniq</code> (remove duplicates), <code>.sort</code>, <code>.compact</code> (remove nils), <code>.zip</code> (merge arrays pairwise).</p>"}
    ],
    "key_concepts": "<ul><li><strong>Shovel (&lt;&lt;):</strong> Idiomatic way to append elements</li><li><strong>Blocks:</strong> Inline code passed to methods with { } or do/end</li><li><strong>map/select/reduce:</strong> Functional-style array operations</li><li><strong>Negative Index:</strong> -1 is last element, -2 is second-to-last</li></ul>",
    "examples": [
        ex("Array Methods", "nums = [3, 1, 4, 1, 5, 9]\nnums << 2              # Shovel operator\nputs nums.sort.inspect\nputs nums.uniq.inspect\n\ndoubled = nums.map { |n| n * 2 }\nputs doubled.inspect\n\nevens = nums.select { |n| n.even? }\nputs evens.inspect", "[1, 1, 2, 3, 4, 5, 9]\n[3, 1, 4, 5, 9, 2]\n[6, 2, 8, 2, 10, 18, 4]\n[4, 2]", "<< appends to the array. sort returns sorted copy. uniq removes duplicates. map transforms each element. select filters by condition.")
    ]
}
}

# Apply Flutter
for topic_id, structured in FLUTTER.items():
    if topic_id in d['flutter']['content']:
        d['flutter']['content'][topic_id]['structured'] = structured

# Apply Ruby
for topic_id, structured in RUBY_EXTRA.items():
    if topic_id in d['ruby']['content']:
        d['ruby']['content'][topic_id]['structured'] = structured

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print("Flutter (18) + Ruby (3): All topics now have structured content!")
