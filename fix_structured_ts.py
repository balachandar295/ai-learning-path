import json

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

def ex(title, code, output, explanation):
    return {"title": title, "code": code, "output": output, "explanation": explanation}

TS = {
"typescript_types": {
    "introduction": "<p><strong>TypeScript Types</strong> are the foundation of TypeScript. Types explicitly define the shape and kind of data a variable can hold. This catches bugs at compile time instead of runtime, provides IntelliSense in your IDE, and serves as living documentation.</p><p>TypeScript has <strong>primitive types</strong> (string, number, boolean, null, undefined, symbol, bigint), <strong>object types</strong>, <strong>array types</strong>, <strong>tuple types</strong>, and special types like <code>any</code>, <code>unknown</code>, <code>never</code>, and <code>void</code>.</p>",
    "subtopics": [
        {"title": "1. Primitive Types", "content": "<p>Annotate variables with a colon: <code>let name: string = 'Alice';</code>. TypeScript will error if you try to assign the wrong type. The most common primitives are <code>string</code>, <code>number</code> (all numbers, including floats), and <code>boolean</code>.</p>"},
        {"title": "2. Arrays & Tuples", "content": "<p>Type arrays with <code>number[]</code> or <code>Array&lt;number&gt;</code>. Tuples are fixed-length arrays with specific types at each position: <code>let pair: [string, number] = ['Alice', 25];</code>. Tuples are great for function return values.</p>"},
        {"title": "3. Union & Literal Types", "content": "<p>Union types allow multiple types: <code>let id: string | number;</code>. Literal types restrict to specific values: <code>let direction: 'up' | 'down' | 'left' | 'right';</code>. This is more precise than plain string.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Type Annotation:</strong> Explicitly declare types with colon syntax</li><li><strong>Type Inference:</strong> TypeScript can auto-detect types from assigned values</li><li><strong>Union Types (|):</strong> Variable can be one of several types</li><li><strong>any vs unknown:</strong> 'any' disables checking; 'unknown' is safer (requires narrowing)</li></ul>",
    "examples": [
        ex("Basic Types", "let name: string = 'Alice';\nlet age: number = 25;\nlet active: boolean = true;\nlet scores: number[] = [90, 85, 92];\nlet pair: [string, number] = ['Bob', 30];\n\nconsole.log(name, age, scores.length);", "Alice 25 3", "Each variable has an explicit type. The compiler will reject any assignment that doesn't match the declared type."),
        ex("Union Types", "function formatId(id: string | number): string {\n  if (typeof id === 'string') {\n    return id.toUpperCase();\n  }\n  return '#' + id;\n}\n\nconsole.log(formatId('abc'));\nconsole.log(formatId(123));", "ABC\n#123", "Union types accept multiple types. Use typeof guards to narrow the type within conditional blocks.")
    ]
},

"typescript_interfaces": {
    "introduction": "<p><strong>Interfaces</strong> define the structure of an object - what properties it must have and their types. They act as contracts: any object claiming to be that type must satisfy all required properties.</p><p>Interfaces are heavily used for typing API responses, component props (in React), and function parameters. They make your code self-documenting and catch shape mismatches at compile time.</p>",
    "subtopics": [
        {"title": "1. Defining Interfaces", "content": "<p>An interface declares property names and types: <code>interface User { name: string; age: number; }</code>. Optional properties use <code>?</code>: <code>email?: string</code>. Readonly properties use <code>readonly</code>: <code>readonly id: number</code>.</p>"},
        {"title": "2. Extending Interfaces", "content": "<p>Interfaces can extend other interfaces: <code>interface Admin extends User { role: string; }</code>. This creates a new type with all parent properties plus new ones. You can extend multiple interfaces.</p>"},
        {"title": "3. Interface vs Type Alias", "content": "<p>Both define object shapes, but interfaces can be extended and merged (declaration merging). Type aliases can use unions and intersections. General rule: use interfaces for objects, type aliases for unions and primitives.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Structural Typing:</strong> TypeScript uses 'duck typing' - shape matters, not name</li><li><strong>Optional (?):</strong> Properties that may or may not exist</li><li><strong>readonly:</strong> Properties that can only be set during initialization</li><li><strong>extends:</strong> Interface inheritance for building upon existing contracts</li></ul>",
    "examples": [
        ex("Interface Definition", "interface User {\n  readonly id: number;\n  name: string;\n  email?: string;\n}\n\nconst user: User = { id: 1, name: 'Alice' };\nconsole.log(user.name);", "Alice", "The User interface requires id and name, but email is optional (?). readonly prevents id from being changed after creation."),
        ex("Extending Interfaces", "interface Animal {\n  name: string;\n  speak(): void;\n}\n\ninterface Dog extends Animal {\n  breed: string;\n}\n\nconst dog: Dog = {\n  name: 'Rex', breed: 'Labrador',\n  speak() { console.log('Woof!'); }\n};\ndog.speak();", "Woof!", "Dog extends Animal, inheriting name and speak() while adding breed. All properties must be implemented.")
    ]
},

"typescript_classes": {
    "introduction": "<p><strong>TypeScript Classes</strong> enhance JavaScript classes with access modifiers (<code>public</code>, <code>private</code>, <code>protected</code>), readonly properties, abstract classes, and parameter properties. This brings Java/C#-style OOP to JavaScript.</p><p>Classes can implement interfaces, ensuring they satisfy a specific contract. This combination of classes and interfaces is the backbone of enterprise TypeScript applications.</p>",
    "subtopics": [
        {"title": "1. Access Modifiers", "content": "<p><code>public</code> (default) - accessible everywhere. <code>private</code> - only inside the class. <code>protected</code> - inside the class and subclasses. These enforce encapsulation at compile time.</p>"},
        {"title": "2. Parameter Properties", "content": "<p>TypeScript shorthand: declaring access modifiers in constructor parameters automatically creates and assigns properties. <code>constructor(public name: string)</code> replaces three lines of boilerplate code.</p>"},
        {"title": "3. Abstract Classes", "content": "<p>Abstract classes cannot be instantiated directly. They define abstract methods that subclasses must implement. Unlike interfaces, abstract classes can contain implementation (concrete methods) alongside abstract ones.</p>"}
    ],
    "key_concepts": "<ul><li><strong>public/private/protected:</strong> Control member visibility</li><li><strong>Parameter Properties:</strong> Shorthand for declaring class fields in constructor</li><li><strong>implements:</strong> Class must satisfy an interface contract</li><li><strong>abstract:</strong> Template class with required overrides</li></ul>",
    "examples": [
        ex("Class with Modifiers", "class BankAccount {\n  constructor(\n    public owner: string,\n    private balance: number = 0\n  ) {}\n\n  deposit(amount: number): void {\n    this.balance += amount;\n  }\n\n  getBalance(): number {\n    return this.balance;\n  }\n}\n\nconst acc = new BankAccount('Alice');\nacc.deposit(1000);\nconsole.log(acc.getBalance());", "1000", "Parameter properties (public owner, private balance) auto-create class fields. balance is private - only accessible within the class.")
    ]
},

"typescript_generics": {
    "introduction": "<p><strong>Generics</strong> let you write reusable components that work with multiple types while preserving type safety. Instead of using <code>any</code> (which loses all type information), generics use type parameters like <code>&lt;T&gt;</code> that are filled in when the function/class is used.</p><p>Generics are everywhere in TypeScript: <code>Array&lt;T&gt;</code>, <code>Promise&lt;T&gt;</code>, <code>Map&lt;K, V&gt;</code>. Understanding them is essential for reading library type definitions.</p>",
    "subtopics": [
        {"title": "1. Generic Functions", "content": "<p>A generic function uses a type parameter: <code>function identity&lt;T&gt;(arg: T): T { return arg; }</code>. The type is inferred from the argument: <code>identity('hello')</code> returns type <code>string</code>.</p>"},
        {"title": "2. Generic Constraints", "content": "<p>Use <code>extends</code> to constrain what types are allowed: <code>&lt;T extends { length: number }&gt;</code> means T must have a length property. This lets you access specific properties safely.</p>"},
        {"title": "3. Generic Classes & Interfaces", "content": "<p>Classes and interfaces can be generic too: <code>class Stack&lt;T&gt; { items: T[] = []; push(item: T) { ... } }</code>. Type is specified at instantiation: <code>new Stack&lt;number&gt;()</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Type Parameter &lt;T&gt;:</strong> Placeholder for a type specified later</li><li><strong>Constraints (extends):</strong> Limit which types are accepted</li><li><strong>Type Inference:</strong> TypeScript often infers generic types from arguments</li><li><strong>Multiple Type Params:</strong> &lt;K, V&gt; for key-value structures</li></ul>",
    "examples": [
        ex("Generic Function", "function firstElement<T>(arr: T[]): T | undefined {\n  return arr[0];\n}\n\nconst num = firstElement([1, 2, 3]);      // number\nconst str = firstElement(['a', 'b', 'c']); // string\n\nconsole.log(num, str);", "1 a", "The function works with any array type. TypeScript infers T from the argument, preserving the return type.")
    ]
},

"typescript_enums": {
    "introduction": "<p><strong>Enums</strong> define a set of named constants, making your code more readable and less error-prone. Instead of scattered magic numbers or strings, enums group related values under a meaningful name.</p><p>TypeScript has numeric enums (auto-incrementing from 0), string enums (explicit values), and const enums (inlined at compile time for performance).</p>",
    "subtopics": [
        {"title": "1. Numeric Enums", "content": "<p>By default, enum values auto-increment from 0: <code>enum Direction { Up, Down, Left, Right }</code>. Direction.Up is 0, Direction.Down is 1, etc. You can set a custom start value.</p>"},
        {"title": "2. String Enums", "content": "<p>String enums require explicit values: <code>enum Color { Red = 'RED', Blue = 'BLUE' }</code>. They are more readable in logs and debugging since you see the string value instead of a number.</p>"},
        {"title": "3. const Enums", "content": "<p><code>const enum</code> is completely removed during compilation - the values are inlined directly. This produces smaller, faster JavaScript at the cost of losing reverse mapping.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Numeric Enums:</strong> Auto-increment from 0 (or custom start)</li><li><strong>String Enums:</strong> Explicit values for readability</li><li><strong>const Enums:</strong> Inlined at compile time for zero runtime cost</li><li><strong>Reverse Mapping:</strong> Numeric enums support value-to-name lookup</li></ul>",
    "examples": [
        ex("Enum Usage", "enum Status {\n  Active = 'ACTIVE',\n  Inactive = 'INACTIVE',\n  Pending = 'PENDING'\n}\n\nfunction getLabel(s: Status): string {\n  switch (s) {\n    case Status.Active: return 'User is active';\n    case Status.Inactive: return 'User is inactive';\n    default: return 'Pending review';\n  }\n}\n\nconsole.log(getLabel(Status.Active));", "User is active", "String enums provide type-safe constants. The switch statement handles each case. Passing an invalid value causes a compile error.")
    ]
},

"typescript_assertions": {
    "introduction": "<p><strong>Type Assertions</strong> tell the TypeScript compiler 'I know more about this type than you do'. They override type inference when you have more context than the compiler - for example, when working with DOM elements or API responses.</p><p>Assertions use <code>as</code> syntax: <code>const input = element as HTMLInputElement;</code>. They don't change the runtime value - they only affect compile-time type checking.</p>",
    "subtopics": [
        {"title": "1. as Syntax", "content": "<p>The <code>as</code> keyword asserts a more specific type: <code>const el = document.getElementById('input') as HTMLInputElement;</code>. Now TypeScript knows el has <code>.value</code>, <code>.checked</code> properties.</p>"},
        {"title": "2. Non-null Assertion (!)", "content": "<p>The <code>!</code> postfix tells TypeScript a value is definitely not null/undefined: <code>const el = document.getElementById('app')!;</code>. Use sparingly - if the element doesn't exist, you'll get a runtime error.</p>"},
        {"title": "3. Type Narrowing vs Assertion", "content": "<p>Prefer type narrowing (if/typeof/instanceof checks) over assertions whenever possible. Narrowing is runtime-safe; assertions are compile-time only. Use assertions only when narrowing isn't practical.</p>"}
    ],
    "key_concepts": "<ul><li><strong>as keyword:</strong> Assert a specific type (compile-time only)</li><li><strong>! operator:</strong> Assert non-null (use carefully)</li><li><strong>No runtime effect:</strong> Assertions are removed during compilation</li><li><strong>Prefer narrowing:</strong> Runtime checks are safer than assertions</li></ul>",
    "examples": [
        ex("Type Assertion", "const input = document.getElementById('search') as HTMLInputElement;\ninput.value = 'TypeScript';\nconsole.log(input.value);", "TypeScript", "Without the assertion, TypeScript only knows it's HTMLElement | null. The 'as' assertion tells it to treat it as HTMLInputElement, enabling .value access.")
    ]
},

"typescript_advanced": {
    "introduction": "<p><strong>Advanced TypeScript Types</strong> include Union, Intersection, Conditional, Mapped, and Template Literal types. These powerful features let you model complex real-world data shapes and create type-safe utilities.</p><p>Intersection types (<code>&</code>) combine multiple types. Conditional types (<code>T extends U ? X : Y</code>) create types based on conditions. These are the building blocks of TypeScript's utility types like Partial, Pick, and Omit.</p>",
    "subtopics": [
        {"title": "1. Intersection Types (&)", "content": "<p>Intersection types merge multiple types into one: <code>type AdminUser = User & Admin;</code>. The resulting type has ALL properties from both types. Useful for mixing in capabilities.</p>"},
        {"title": "2. Conditional Types", "content": "<p>Conditional types select a type based on a condition: <code>type IsString&lt;T&gt; = T extends string ? 'yes' : 'no';</code>. They power advanced type transformations and are used heavily in library definitions.</p>"},
        {"title": "3. Mapped Types", "content": "<p>Mapped types transform properties of existing types: <code>type ReadonlyUser = { readonly [K in keyof User]: User[K] }</code>. This is how Partial, Required, and Readonly utility types are built.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Intersection (&):</strong> Combines multiple types into one</li><li><strong>Conditional Types:</strong> T extends U ? X : Y pattern</li><li><strong>Mapped Types:</strong> Transform existing types programmatically</li><li><strong>keyof:</strong> Gets the union of all property names as a type</li></ul>",
    "examples": [
        ex("Intersection Types", "interface Printable {\n  print(): void;\n}\ninterface Loggable {\n  log(): void;\n}\n\ntype PrintLogger = Printable & Loggable;\n\nconst obj: PrintLogger = {\n  print() { console.log('Printing...'); },\n  log() { console.log('Logging...'); }\n};\nobj.print();\nobj.log();", "Printing...\nLogging...", "Intersection types require ALL properties from ALL combined types. The object must implement both print() and log().")
    ]
},

"typescript_modules": {
    "introduction": "<p><strong>TypeScript Modules</strong> follow the ES6 module system with <code>import</code>/<code>export</code>. Each file is its own module with its own scope. TypeScript adds type-only imports and module augmentation on top of JavaScript's module system.</p><p>Modules are essential for organizing large codebases. They prevent naming conflicts, enable tree-shaking (removing unused code), and make dependencies explicit.</p>",
    "subtopics": [
        {"title": "1. Named & Default Exports", "content": "<p>Named exports: <code>export const PI = 3.14;</code>, imported as <code>import { PI } from './math';</code>. Default exports: <code>export default class App {}</code>, imported as <code>import App from './App';</code>. A module can have both.</p>"},
        {"title": "2. Type-Only Imports", "content": "<p><code>import type { User } from './types';</code> imports ONLY the type, not the runtime value. This is stripped during compilation, reducing bundle size. TypeScript 3.8+ feature.</p>"},
        {"title": "3. Module Resolution", "content": "<p>TypeScript resolves modules using strategies defined in tsconfig.json: <code>node</code> (Node.js style, looks in node_modules) or <code>classic</code>. Path aliases (<code>@/components</code>) can be configured with <code>paths</code> in tsconfig.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Named Export:</strong> Multiple per file, imported by exact name</li><li><strong>Default Export:</strong> One per file, imported with any name</li><li><strong>import type:</strong> Type-only imports removed at compile time</li><li><strong>Path Aliases:</strong> Configure shortcut paths in tsconfig.json</li></ul>",
    "examples": [
        ex("Module Exports", "// types.ts\nexport interface User {\n  name: string;\n  age: number;\n}\nexport const DEFAULT_AGE = 18;\n\n// app.ts\nimport type { User } from './types';\nimport { DEFAULT_AGE } from './types';\n\nconst user: User = { name: 'Alice', age: DEFAULT_AGE };\nconsole.log(user);", "{ name: 'Alice', age: 18 }", "import type only imports the type (removed at compile time). DEFAULT_AGE is a runtime value import.")
    ]
},

"typescript_decorators": {
    "introduction": "<p><strong>Decorators</strong> are special functions that modify classes, methods, properties, or parameters. They use the <code>@expression</code> syntax and execute at class definition time (not instance creation). Decorators are widely used in Angular and NestJS.</p><p>Decorators are currently a Stage 3 TC39 proposal and require <code>experimentalDecorators: true</code> in tsconfig.json for TypeScript's legacy implementation.</p>",
    "subtopics": [
        {"title": "1. Class Decorators", "content": "<p>A class decorator receives the constructor function as its argument. It can modify the class or return a new constructor. Example: <code>@sealed class Greeter {}</code> where sealed freezes the class prototype.</p>"},
        {"title": "2. Method Decorators", "content": "<p>Method decorators receive the target, method name, and property descriptor. They can wrap methods to add logging, validation, or caching behavior.</p>"},
        {"title": "3. Property Decorators", "content": "<p>Property decorators can observe that a property has been declared. Combined with metadata reflection, they power dependency injection frameworks like Angular's <code>@Inject()</code>.</p>"}
    ],
    "key_concepts": "<ul><li><strong>@expression:</strong> Decorator syntax applied above declarations</li><li><strong>Class Decorator:</strong> Receives the constructor function</li><li><strong>Method Decorator:</strong> Can wrap or replace method behavior</li><li><strong>Experimental:</strong> Requires experimentalDecorators flag in tsconfig</li></ul>",
    "examples": [
        ex("Method Decorator", "function log(\n  target: any, name: string, descriptor: PropertyDescriptor\n) {\n  const original = descriptor.value;\n  descriptor.value = function(...args: any[]) {\n    console.log(`Calling ${name} with`, args);\n    return original.apply(this, args);\n  };\n}\n\nclass Calculator {\n  @log\n  add(a: number, b: number) { return a + b; }\n}\n\nnew Calculator().add(2, 3);", "Calling add with [2, 3]", "The @log decorator wraps the add method, logging its name and arguments before executing the original function.")
    ]
},

"typescript_utility": {
    "introduction": "<p><strong>Utility Types</strong> are built-in type transformations provided by TypeScript. They let you create new types from existing ones without redefining properties. The most commonly used are <code>Partial</code>, <code>Required</code>, <code>Readonly</code>, <code>Pick</code>, <code>Omit</code>, and <code>Record</code>.</p><p>These utilities are essential for real-world TypeScript development, especially when working with forms, API responses, and state management.</p>",
    "subtopics": [
        {"title": "1. Partial & Required", "content": "<p><code>Partial&lt;T&gt;</code> makes all properties optional. <code>Required&lt;T&gt;</code> makes all properties required. Partial is perfect for update functions where you only change some fields.</p>"},
        {"title": "2. Pick & Omit", "content": "<p><code>Pick&lt;T, K&gt;</code> creates a type with only the specified properties. <code>Omit&lt;T, K&gt;</code> excludes specified properties. Great for creating subset types from large interfaces.</p>"},
        {"title": "3. Record & ReturnType", "content": "<p><code>Record&lt;K, V&gt;</code> creates an object type with keys K and values V: <code>Record&lt;string, number&gt;</code> is a string-to-number map. <code>ReturnType&lt;T&gt;</code> extracts a function's return type.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Partial&lt;T&gt;:</strong> All properties become optional</li><li><strong>Pick&lt;T, K&gt;:</strong> Select specific properties from a type</li><li><strong>Omit&lt;T, K&gt;:</strong> Remove specific properties from a type</li><li><strong>Record&lt;K, V&gt;:</strong> Create a mapped object type</li></ul>",
    "examples": [
        ex("Utility Types", "interface User {\n  id: number;\n  name: string;\n  email: string;\n  age: number;\n}\n\ntype UserPreview = Pick<User, 'id' | 'name'>;\ntype UpdateUser = Partial<Omit<User, 'id'>>;\n\nconst preview: UserPreview = { id: 1, name: 'Alice' };\nconst update: UpdateUser = { name: 'Bob' };\n\nconsole.log(preview, update);", "{ id: 1, name: 'Alice' } { name: 'Bob' }", "Pick selects only id and name. Partial+Omit creates an update type where all fields except id are optional.")
    ]
},

"typescript_tsconfig": {
    "introduction": "<p><strong>tsconfig.json</strong> is the configuration file that controls how TypeScript compiles your code. It specifies compiler options, file inclusion/exclusion patterns, and project references. Every TypeScript project needs one.</p><p>Key options include <code>strict</code> (enables all strict checks), <code>target</code> (JS version output), <code>module</code> (module system), and <code>outDir</code> (output directory).</p>",
    "subtopics": [
        {"title": "1. Essential Options", "content": "<p><code>target</code>: Output JavaScript version (es5, es6, es2020). <code>module</code>: Module system (commonjs for Node, esnext for modern). <code>outDir</code>: Where compiled JS files go. <code>rootDir</code>: Source files location.</p>"},
        {"title": "2. Strict Mode Options", "content": "<p>The <code>strict: true</code> flag enables: <code>strictNullChecks</code>, <code>noImplicitAny</code>, <code>strictFunctionTypes</code>, <code>strictBindCallApply</code>, and more. Always enable strict mode for new projects - it catches many common bugs.</p>"},
        {"title": "3. Path Mapping", "content": "<p>Configure path aliases with <code>paths</code>: <code>\"@/*\": [\"src/*\"]</code> lets you write <code>import { api } from '@/services'</code> instead of <code>'../../../services'</code>. Requires <code>baseUrl</code> to be set.</p>"}
    ],
    "key_concepts": "<ul><li><strong>strict:</strong> Master switch for all strict type-checking options</li><li><strong>target:</strong> Controls JavaScript output version</li><li><strong>paths:</strong> Create import aliases for cleaner imports</li><li><strong>include/exclude:</strong> Control which files TypeScript processes</li></ul>",
    "examples": [
        ex("tsconfig.json", '{\n  "compilerOptions": {\n    "target": "es2020",\n    "module": "esnext",\n    "strict": true,\n    "outDir": "./dist",\n    "rootDir": "./src",\n    "baseUrl": ".",\n    "paths": {\n      "@/*": ["src/*"]\n    }\n  },\n  "include": ["src/**/*"],\n  "exclude": ["node_modules"]\n}', "(Configuration file - no runtime output)", "This config enables strict mode, targets ES2020, uses ESNext modules, and sets up path aliases for clean imports.")
    ]
},

"typescript_dom": {
    "introduction": "<p><strong>DOM Manipulation with TypeScript</strong> brings type safety to browser interactions. TypeScript provides comprehensive types for all HTML elements, events, and Web APIs. This catches common DOM errors at compile time.</p><p>TypeScript knows that <code>getElementById</code> returns <code>HTMLElement | null</code>, forcing you to handle the null case. Element-specific types like <code>HTMLInputElement</code> provide access to element-specific properties.</p>",
    "subtopics": [
        {"title": "1. Typed Element Selection", "content": "<p>Use type assertions or generic querySelector: <code>document.querySelector&lt;HTMLInputElement&gt;('#email')</code>. This tells TypeScript the exact element type, enabling autocomplete for properties like <code>.value</code>, <code>.checked</code>.</p>"},
        {"title": "2. Event Handling", "content": "<p>TypeScript types events: <code>MouseEvent</code>, <code>KeyboardEvent</code>, <code>InputEvent</code>, <code>SubmitEvent</code>. In event handlers, access type-safe properties like <code>event.key</code> (KeyboardEvent) or <code>event.target</code>.</p>"},
        {"title": "3. Null Safety", "content": "<p>DOM methods can return null if the element doesn't exist. TypeScript forces you to check: <code>const el = document.getElementById('app'); if (el) { el.textContent = 'Hi'; }</code>. This prevents null reference errors.</p>"}
    ],
    "key_concepts": "<ul><li><strong>HTMLElement types:</strong> HTMLInputElement, HTMLButtonElement, HTMLDivElement, etc.</li><li><strong>Event types:</strong> MouseEvent, KeyboardEvent, InputEvent for type-safe handlers</li><li><strong>Null checks:</strong> DOM methods return T | null, must handle null case</li><li><strong>Generic querySelector:</strong> Specify the return element type</li></ul>",
    "examples": [
        ex("Typed DOM", "const btn = document.querySelector<HTMLButtonElement>('#submit');\nconst input = document.querySelector<HTMLInputElement>('#name');\n\nif (btn && input) {\n  btn.addEventListener('click', (e: MouseEvent) => {\n    console.log('Name:', input.value);\n    btn.disabled = true;\n  });\n}", "(Logs input value and disables button on click)", "Generic querySelector specifies the element type. The if-check satisfies null safety. e: MouseEvent types the event object.")
    ]
},

"typescript_react": {
    "introduction": "<p><strong>TypeScript with React</strong> provides type safety for components, props, state, and hooks. It catches prop mismatches, ensures correct hook usage, and provides excellent IntelliSense for the component API.</p><p>React + TypeScript is now the industry standard for production applications. Most React libraries ship with TypeScript definitions, and Create React App supports TypeScript out of the box.</p>",
    "subtopics": [
        {"title": "1. Typing Props", "content": "<p>Define prop types with an interface: <code>interface Props { title: string; count?: number; }</code>. Use it with the component: <code>const Header: React.FC&lt;Props&gt; = ({ title }) => ...</code>. TypeScript will error if required props are missing.</p>"},
        {"title": "2. Typing State & Hooks", "content": "<p>useState with generics: <code>const [users, setUsers] = useState&lt;User[]&gt;([]);</code>. useRef for DOM elements: <code>const ref = useRef&lt;HTMLInputElement&gt;(null);</code>. TypeScript infers types for useReducer actions.</p>"},
        {"title": "3. Event Handlers", "content": "<p>Type event handlers explicitly: <code>const handleChange = (e: React.ChangeEvent&lt;HTMLInputElement&gt;) => { ... }</code>. React provides its own event types that wrap native DOM events.</p>"}
    ],
    "key_concepts": "<ul><li><strong>React.FC&lt;Props&gt;:</strong> Typed functional component</li><li><strong>useState&lt;T&gt;:</strong> Generic state hook with type parameter</li><li><strong>React.ChangeEvent:</strong> Typed event for form inputs</li><li><strong>children: React.ReactNode:</strong> Type for child elements</li></ul>",
    "examples": [
        ex("Typed Component", "interface CardProps {\n  title: string;\n  description: string;\n  onClick?: () => void;\n}\n\nconst Card: React.FC<CardProps> = ({ title, description, onClick }) => (\n  <div onClick={onClick}>\n    <h2>{title}</h2>\n    <p>{description}</p>\n  </div>\n);\n\n// Usage: <Card title='Hello' description='World' />", "(Renders a card with typed props)", "Props interface defines required and optional properties. TypeScript errors if you forget to pass 'title' or 'description'.")
    ]
},

"typescript_typeguards": {
    "introduction": "<p><strong>Type Guards</strong> are runtime checks that narrow a variable's type within a conditional block. They are the safe alternative to type assertions. TypeScript understands guards and automatically narrows the type for you.</p><p>Built-in guards include <code>typeof</code> (primitives), <code>instanceof</code> (classes), and <code>in</code> (property existence). Custom type guards use the <code>is</code> keyword in return types.</p>",
    "subtopics": [
        {"title": "1. typeof & instanceof", "content": "<p><code>typeof x === 'string'</code> narrows to string. <code>x instanceof Date</code> narrows to Date. These are the simplest and most common guards.</p>"},
        {"title": "2. Custom Type Guards", "content": "<p>Define custom guards with <code>is</code>: <code>function isFish(pet: Fish | Bird): pet is Fish { return (pet as Fish).swim !== undefined; }</code>. After calling isFish(), TypeScript knows the exact type.</p>"},
        {"title": "3. Discriminated Unions", "content": "<p>Add a shared literal property to union members: <code>{ type: 'circle', radius: number } | { type: 'square', side: number }</code>. Switch on the <code>type</code> field for exhaustive narrowing.</p>"}
    ],
    "key_concepts": "<ul><li><strong>typeof:</strong> Guards for primitive types (string, number, boolean)</li><li><strong>instanceof:</strong> Guards for class instances</li><li><strong>Custom Guard (is):</strong> User-defined type predicates</li><li><strong>Discriminated Union:</strong> Shared literal field for exhaustive switching</li></ul>",
    "examples": [
        ex("Type Guard", "interface Circle { kind: 'circle'; radius: number; }\ninterface Square { kind: 'square'; side: number; }\ntype Shape = Circle | Square;\n\nfunction area(shape: Shape): number {\n  switch (shape.kind) {\n    case 'circle': return Math.PI * shape.radius ** 2;\n    case 'square': return shape.side ** 2;\n  }\n}\n\nconsole.log(area({ kind: 'circle', radius: 5 }));", "78.54", "The discriminated union (kind field) lets TypeScript narrow the type in each case branch, providing access to the correct properties.")
    ]
},

"typescript_strict": {
    "introduction": "<p><strong>Strict Mode</strong> in TypeScript enables a set of compiler flags that enforce the highest level of type safety. Enabling <code>strict: true</code> in tsconfig.json turns on all strict checks at once, catching many common bugs at compile time.</p><p>Every serious TypeScript project should use strict mode. It may require more annotations initially, but it prevents entire categories of runtime errors.</p>",
    "subtopics": [
        {"title": "1. strictNullChecks", "content": "<p>Without this, <code>null</code> and <code>undefined</code> are assignable to all types. With it, you must explicitly handle null: <code>const name: string | null = getName();</code>. This alone prevents thousands of 'cannot read property of null' errors.</p>"},
        {"title": "2. noImplicitAny", "content": "<p>When TypeScript can't infer a type, it defaults to <code>any</code> (no checking). With <code>noImplicitAny</code>, you must explicitly annotate these cases. This ensures all code is properly typed.</p>"},
        {"title": "3. strictFunctionTypes", "content": "<p>Enables stricter checking of function types. Without it, function parameters are checked bivariantly (unsafely). With it, only contravariant parameter types are allowed, preventing subtle bugs.</p>"}
    ],
    "key_concepts": "<ul><li><strong>strict: true:</strong> Master switch enabling all strict flags</li><li><strong>strictNullChecks:</strong> Null/undefined must be explicitly handled</li><li><strong>noImplicitAny:</strong> No silent 'any' inference</li><li><strong>noImplicitReturns:</strong> All code paths must return a value</li></ul>",
    "examples": [
        ex("Strict Null Checks", "function getUser(id: number): string | undefined {\n  const users: Record<number, string> = { 1: 'Alice', 2: 'Bob' };\n  return users[id];\n}\n\nconst name = getUser(3);\n\n// Must check for undefined!\nif (name) {\n  console.log(name.toUpperCase());\n} else {\n  console.log('User not found');\n}", "User not found", "With strictNullChecks, TypeScript forces you to handle the undefined case. Without the if-check, calling .toUpperCase() would be a compile error.")
    ]
},

"typescript_practices": {
    "introduction": "<p><strong>TypeScript Best Practices</strong> are patterns and conventions that lead to maintainable, type-safe code. Following these practices helps you get the most out of TypeScript's type system while keeping code readable.</p><p>The golden rules: avoid <code>any</code>, prefer interfaces for objects, use strict mode, leverage type inference, and let TypeScript work for you instead of fighting it.</p>",
    "subtopics": [
        {"title": "1. Avoid 'any'", "content": "<p>Using <code>any</code> defeats the purpose of TypeScript. Use <code>unknown</code> when the type is truly unknown (requires narrowing before use). Use generics for reusable code. Only use <code>any</code> as a last resort for migration.</p>"},
        {"title": "2. Leverage Type Inference", "content": "<p>Don't over-annotate: <code>const name = 'Alice';</code> is already typed as string. Only annotate when TypeScript can't infer correctly, for function parameters, or for documentation.</p>"},
        {"title": "3. Use Readonly & Immutability", "content": "<p>Mark properties as <code>readonly</code> when they shouldn't change. Use <code>ReadonlyArray&lt;T&gt;</code> or <code>Readonly&lt;T&gt;</code> to prevent mutations. Immutability reduces bugs and makes code easier to reason about.</p>"}
    ],
    "key_concepts": "<ul><li><strong>Avoid any:</strong> Use unknown, generics, or proper types instead</li><li><strong>Inference:</strong> Let TypeScript infer types when it can</li><li><strong>Readonly:</strong> Prevent accidental mutations</li><li><strong>Strict mode:</strong> Always enable for new projects</li></ul>",
    "examples": [
        ex("Good Practices", "// BAD: Using any\n// function parse(data: any) { ... }\n\n// GOOD: Using unknown with narrowing\nfunction parse(data: unknown): string {\n  if (typeof data === 'string') return data;\n  if (typeof data === 'number') return String(data);\n  throw new Error('Unsupported type');\n}\n\nconsole.log(parse('hello'));\nconsole.log(parse(42));", "hello\n42", "Using unknown instead of any forces you to narrow the type before using it, ensuring type safety at every step.")
    ]
},

"typescript_interview": {
    "introduction": "<p><strong>TypeScript Interview Preparation</strong> covers the most frequently asked concepts in technical interviews: type vs interface, generics, utility types, type guards, declaration merging, and understanding how TypeScript compiles to JavaScript.</p><p>Interviewers test both theoretical understanding and practical application. Be prepared to explain the type system, write generic utilities, and solve typing challenges.</p>",
    "subtopics": [
        {"title": "1. Common Questions", "content": "<p>Top interview topics: Difference between <code>type</code> and <code>interface</code>. When to use generics vs union types. How <code>any</code> differs from <code>unknown</code>. What is type narrowing and type guards. How TypeScript handles null safety.</p>"},
        {"title": "2. Type Challenges", "content": "<p>Be ready to write: Generic utility types like DeepPartial&lt;T&gt;, conditional types, mapped types, template literal types. Understanding how Partial, Pick, Omit work internally shows deep knowledge.</p>"},
        {"title": "3. Real-World Patterns", "content": "<p>Demonstrate knowledge of discriminated unions for state machines, generic hooks in React, proper error handling with Result types, and API response typing with unknown validation.</p>"}
    ],
    "key_concepts": "<ul><li><strong>type vs interface:</strong> Interfaces are extendable; types support unions/intersections</li><li><strong>any vs unknown:</strong> any disables checking; unknown requires narrowing</li><li><strong>Generics:</strong> Creates reusable, type-safe components</li><li><strong>Type Guards:</strong> Runtime checks that narrow types</li></ul>",
    "examples": [
        ex("Interview Question: DeepReadonly", "type DeepReadonly<T> = {\n  readonly [K in keyof T]: T[K] extends object\n    ? DeepReadonly<T[K]>\n    : T[K];\n};\n\ninterface User {\n  name: string;\n  address: { city: string; zip: number; };\n}\n\nconst user: DeepReadonly<User> = {\n  name: 'Alice',\n  address: { city: 'NYC', zip: 10001 }\n};\n// user.address.city = 'LA'; // Error!", "(Compile-time only - prevents deep mutations)", "DeepReadonly recursively makes all properties readonly, including nested objects. This uses mapped types and conditional types together.")
    ]
}
}

for topic_id, structured in TS.items():
    if topic_id in d['typescript']['content']:
        d['typescript']['content'][topic_id]['structured'] = structured

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print("TypeScript: All 17 topics now have structured content!")
