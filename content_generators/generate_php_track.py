import json

file_path = r'core\static\tracks_data.js'
with open(file_path,'r',encoding='utf-8') as f: text=f.read()
json_start=text.find('{')
data=json.loads(text[json_start:text.rfind('}')+1])

def card(l,c): return f"<div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'><div style='background:linear-gradient(to right,#0ea5e9,#3b82f6);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>{l}</div><pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>{c}</pre></div>"
def sec(t,d,ex): h=f"<h4 style='color:#0ea5e9;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #0ea5e9;padding-left:12px;'>{t}</h4>"; h+=f"<p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>{d}</p>"; [h.__class__.__add__(h,card(l,c)) for l,c in ex]; return h+"".join(card(l,c) for l,c in ex)
def expl(title,secs): h=f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"; h+="".join(sec(*s) for s in secs); return h+"</div>"
def quiz(items): return [{"q":q,"options":o,"answer":a} for q,o,a in items]
def task(t,d,h,c): return {"title":t,"description":d,"hint":h,"code":c}
def probs(items): return [{"title":t,"description":d,"code":c} for t,d,c in items]

# ══════════════════════════ PHP TRACK ══════════════════════════
php_nodes_raw=[
    ("php_basics",    "PHP Basics",           1),("php_variables","Variables & Types",   1),
    ("php_operators", "Operators",             1),("php_control",  "Control Flow",        1),
    ("php_loops",     "Loops",                 1),("php_functions","Functions",            2),
    ("php_arrays",    "Arrays",                2),("php_strings",  "Strings",              2),
    ("php_forms",     "Forms & Input",         2),("php_oop",      "OOP Basics",           3),
    ("php_inheritance","Inheritance",          3),("php_traits",   "Traits & Interfaces",  3),
    ("php_pdo",       "PDO & Database",        3),("php_sessions", "Sessions & Cookies",   4),
    ("php_files",     "File Handling",         4),("php_json",     "JSON & APIs",          4),
    ("php_advanced",  "Advanced PHP",          4),("php_interview","PHP Interview Guide",  5),
]
php_nodes=[]
for i,(nid,title,phase) in enumerate(php_nodes_raw):
    node={"id":nid,"title":title,"x":1250 if i%2==0 else 1530,"y":150+i*160,"status":"available" if i==0 else "locked","phase":phase}
    if i>0: node["parent"]=php_nodes_raw[i-1][0]
    php_nodes.append(node)

ph={}

ph["php_basics"]={
    "title":"PHP Basics",
    "explanation":expl("PHP Basics",[
        ("What is PHP?","PHP (PHP: Hypertext Preprocessor) is a server-side scripting language designed for web development. It powers 77% of websites including Facebook, WordPress, Wikipedia. PHP code runs on the server and outputs HTML.",
         [("Hello World",'<?php\n    echo "Hello, World!\\n";\n    echo "PHP is awesome!\\n";\n    print("Same as echo\\n");\n\n    // PHP in HTML\n?>\n<!DOCTYPE html>\n<html>\n<body>\n    <h1><?php echo "Hello from PHP!"; ?></h1>\n    <p><?= "Short echo tag" ?></p>\n</body>\n</html>'),
          ("PHP Structure",'<?php\n// PHP code always inside <?php ... ?>\n// Single-line comment\n\n/* Multi-line\n   comment */\n\n// Echo and print\necho "Echo can output multiple values\\n";\nprint "Print returns 1 (can use in expressions)\\n";\n\n// PHPInfo — see all config\n// phpinfo();\n\n// Check PHP version\necho PHP_VERSION . "\\n";  // e.g., 8.2.0')]),
        ("Variables & echo","Variables start with $. PHP is loosely typed — no type declaration needed. Strings concatenate with . (dot).",
         [("Basic variables",'<?php\n$name   = "Alice";\n$age    = 25;\n$gpa    = 3.8;\n$active = true;\n\necho "Name: $name\\n";           // variable inside string\necho "Age: " . $age . "\\n";     // concatenation\necho "GPA: {$gpa}\\n";           // curly braces\nprintf("GPA: %.1f\\n", $gpa);    // formatted\n\n// var_dump shows type+value\nvar_dump($active);   // bool(true)\nvar_dump($age);      // int(25)'),
          ("User input (from URL/form)",'<?php\n// GET request: URL?name=Alice&age=25\n$name = $_GET["name"]  ?? "Guest";   // ?? null coalescing\n$age  = $_GET["age"]   ?? 0;\n\n// POST request (form submission)\n$email    = $_POST["email"]    ?? "";\n$password = $_POST["password"] ?? "";\n\n// Always sanitize input!\n$clean_name = htmlspecialchars($name, ENT_QUOTES, "UTF-8");\necho "Hello, $clean_name!\\n";')]),
    ]),
    "examples":[],
    "concept_quiz":quiz([
        ("PHP stands for?",["Personal Home Page","PHP: Hypertext Preprocessor","Preprocessed HTML Pages","Private Hosting Protocol"],"PHP: Hypertext Preprocessor"),
        ("PHP variables start with?",["#","&","$","@"],"$"),
        ("String concatenation in PHP uses?",["+"," .",",","&"]," ."),
        ("PHP runs on?",["Client (browser)","Server","Both","Mobile only"],"Server"),
        ("<?= ?> is shorthand for?",["<?php print ?>","<?php echo ?>","<?php ?>","<?php return ?>"],"<?php echo ?>"),
    ]),
    "hands_on":task("PHP Info Page","Write a PHP script that shows your name, PHP version, and server time in HTML.","Use PHP_VERSION, date(), and echo inside HTML.",'<?php\n$name = "Alice";\n$version = PHP_VERSION;\n$time = date("Y-m-d H:i:s");\n?>\n<!DOCTYPE html>\n<html>\n<body>\n    <h1>Welcome, <?= htmlspecialchars($name) ?></h1>\n    <p>PHP Version: <?= $version ?></p>\n    <p>Server Time: <?= $time ?></p>\n</body>\n</html>'),
    "problem_solving":probs([
        ("Fahrenheit Converter","Convert 100°C to Fahrenheit.",'<?php\n$c=100;\n$f=$c*9/5+32;\necho "$c°C = {$f}°F\\n";'),
        ("Sum of digits","Sum digits of 12345.",'<?php\n$n=12345; $sum=0;\nwhile($n>0){$sum+=$n%10;$n=(int)($n/10);}\necho "Sum: $sum\\n";'),
        ("String reverse","Reverse the string \'Hello World\'.",'<?php\necho strrev("Hello World")."\\n";'),
    ])
}

ph["php_variables"]={
    "title":"Variables & Data Types",
    "explanation":expl("Variables & Data Types",[
        ("PHP Data Types","PHP has 8 types: int, float, string, bool, array, object, null, resource. PHP is dynamically typed — type depends on value.",
         [("All types",'<?php\n$int    = 42;\n$float  = 3.14;\n$string = "Hello";\n$bool   = true;\n$null   = null;\n$arr    = [1, 2, 3];\n$obj    = new stdClass();\n\necho gettype($int);    // integer\necho gettype($float);  // double\necho gettype($string); // string\necho gettype($bool);   // boolean\necho gettype($null);   // NULL'),
          ("Type juggling & casting",'<?php\n// PHP auto-converts (type juggling)\n$x = "5" + 3;        // 8  (string to int)\n$y = "5 apples" + 2; // 7  (leading number)\n$z = "apple" + 0;    // 0  (no number)\n\n// Explicit casting\n$a = (int)"42.9";     // 42\n$b = (float)"3";      // 3.0\n$c = (string)42;      // "42"\n$d = (bool)0;         // false\n$e = (bool)"hello";   // true (non-empty)\n\nvar_dump($a, $b, $c, $d);')]),
        ("Constants & Heredoc","define() creates constants. const also works in class scope. Heredoc syntax for multi-line strings.",
         [("Constants",'<?php\ndefine("PI", 3.14159);\ndefine("APP_NAME", "LearnPHP");\ndefine("MAX_SIZE", 100);\n\necho PI . "\\n";       // 3.14159\necho APP_NAME . "\\n"; // LearnPHP\n\n// Constants don\'t use $\n// class constant:\nclass Config {\n    const VERSION = "1.0.0";\n    const DEBUG   = false;\n}\necho Config::VERSION . "\\n"; // 1.0.0'),
          ("Heredoc & Nowdoc",'<?php\n$name = "Alice";\n$age  = 25;\n\n// Heredoc: variables ARE parsed\n$text = <<<EOT\nHello, $name!\nYou are $age years old.\nEOT;\necho $text;\n\n// Nowdoc: variables NOT parsed (like single quotes)\n$raw = <<<\'EOT\'\nHello, $name! (not parsed)\nEOT;\necho $raw;')]),
    ]),
    "examples":[],
    "concept_quiz":quiz([
        ("gettype() returns?",["Variable name","Variable value","Variable type as string","Memory address"],"Variable type as string"),
        ("Which is true? (bool)\"0\" = ?",["true","false","null","Error"],"false"),
        ("PHP constant is defined with?",["let","const or define()","$CONST","final"],"const or define()"),
        ("$x='5'+3 equals?",["'53'","8","Error","53"],"8"),
        ("null coalescing ?? returns?",["Left if truthy","Left if not null, else right","Right always","Left always"],"Left if not null, else right"),
    ]),
    "hands_on":task("Type Inspector","Create variables of each PHP type. Use var_dump to display type and value for each.","var_dump shows both type and value.",'<?php\n$values = [\n    42, 3.14, "Hello", true, false, null, [1,2,3]\n];\nforeach ($values as $v) {\n    echo gettype($v) . ": ";\n    var_export($v);\n    echo "\\n";\n}'),
    "problem_solving":probs([
        ("Check type","Check if variable is int, float, or string.",'<?php\nfunction checkType($v){\n    if(is_int($v)) echo "Integer\\n";\n    elseif(is_float($v)) echo "Float\\n";\n    elseif(is_string($v)) echo "String\\n";\n    else echo "Other\\n";\n}\ncheckType(42); checkType(3.14); checkType("hi");'),
        ("Safe to Int","Convert \'abc\', \'42\', \'3.7\' to int safely.",'<?php\nforeach(["abc","42","3.7"] as $s){\n    $n=is_numeric($s)?(int)$s:0;\n    echo "$s -> $n\\n";\n}'),
        ("Constant usage","Define MAX=100, MIN=1. Check if 50 is in range.",'<?php\ndefine("MAX",100); define("MIN",1);\n$n=50;\necho($n>=MIN&&$n<=MAX?"In range\\n":"Out of range\\n");'),
    ])
}

# Topics 3-17
php_topic_codes={
    "php_operators":('<?php\n$a=17; $b=5;\necho $a+$b,"\\n";  // 22\necho $a/$b,"\\n";  // 3.4 (float div!)\necho $a%$b,"\\n";  // 2\necho $a**2,"\\n";  // 289 (power)\necho ($a<=>$b),"\\n"; // 1 (spaceship: -1,0,1)\n\n// String\necho "Hello"." World\\n";\necho str_repeat("ab",3),"\\n"; // ababab\n\n// Comparison (== vs ===)\nvar_dump(0=="a");   // true (PHP 7: loose)\nvar_dump(0==="a");  // false (strict)\nvar_dump("1"==1);   // true\nvar_dump("1"===1);  // false\n\n// Null coalescing\n$x=null;\necho($x??"default"),"\\n"; // default',"PHP operators: arithmetic, spaceship, ==vs==="),
    "php_control":('<?php\n$score=82;\nif($score>=90)      echo "A\\n";\nelseif($score>=75)  echo "B\\n";\nelseif($score>=60)  echo "C\\n";\nelse                echo "F\\n";\n\n// match expression (PHP 8+)\n$status=1;\n$label=match($status){\n    0=>"Inactive",\n    1=>"Active",\n    2=>"Suspended",\n    default=>"Unknown"\n};\necho "$label\\n";\n\n// switch\nswitch($score){\n    case $score>=90: echo "Excellent"; break;\n    default: echo "Keep going";\n}',"if/elseif/else, match, switch"),
    "php_loops":('<?php\n// for\nfor($i=1;$i<=5;$i++) echo "$i ";\necho "\\n";\n\n// foreach (best for arrays)\n$fruits=["apple","banana","cherry"];\nforeach($fruits as $i=>$fruit){\n    echo "$i: $fruit\\n";\n}\n\n// while\n$n=10;\nwhile($n>0){ echo "$n "; $n-=3; }\necho "\\n";\n\n// do-while\n$x=0;\ndo { echo "x=$x\\n"; $x++; } while($x<3);\n\n// array_map, array_filter (functional)\n$nums=range(1,10);\n$evens=array_filter($nums,fn($n)=>$n%2==0);\n$doubled=array_map(fn($n)=>$n*2,$nums);\necho implode(",",array_values($evens)),"\\n";',"for, foreach, while, array_map/filter"),
    "php_functions":('<?php\n// Basic function\nfunction greet(string $name, string $msg="Hello"): string {\n    return "$msg, $name!";\n}\necho greet("Alice"),"\\n";\necho greet("Bob","Hi"),"\\n";\n\n// Type hints (PHP 7+)\nfunction add(int $a, int $b): int { return $a+$b; }\necho add(5,3),"\\n";\n\n// Arrow function (PHP 7.4+)\n$square = fn($n) => $n ** 2;\necho $square(7),"\\n"; // 49\n\n// Variadic\nfunction sumAll(int ...$nums): int { return array_sum($nums); }\necho sumAll(1,2,3,4,5),"\\n"; // 15\n\n// Anonymous function (closure)\n$multiply = function($a,$b) { return $a*$b; };\necho $multiply(4,5),"\\n"; // 20',"Functions: type hints, arrow, variadic, closures"),
    "php_arrays":('<?php\n// Indexed array\n$arr=[5,3,8,1,9];\nsort($arr);\necho implode(",",$arr),"\\n"; // 1,3,5,8,9\n\n// Associative array\n$student=["name"=>"Alice","gpa"=>3.8,"year"=>2];\necho $student["name"],"\\n";\n\n// Array functions\n$nums=[3,1,4,1,5,9,2,6];\necho max($nums),"\\n";          // 9\necho min($nums),"\\n";          // 1\necho array_sum($nums),"\\n";   // 31\necho count($nums),"\\n";       // 8\n$unique=array_unique($nums);\n$filtered=array_filter($nums,fn($n)=>$n>3);\n$mapped=array_map(fn($n)=>$n*2,$nums);\necho implode(",",array_values($unique)),"\\n";\n\n// array_push / pop\narray_push($arr,10);\n$last=array_pop($arr);\necho "Last: $last\\n";',"Arrays: sort, filter, map, unique, push/pop"),
    "php_strings":('<?php\n$s="  Hello, PHP World!  ";\necho strlen($s),"\\n";\necho strtoupper(trim($s)),"\\n";\necho strtolower($s),"\\n";\necho str_contains($s,"PHP")?"Has PHP\\n":"No PHP\\n"; // PHP 8+\necho str_replace("PHP","Python",$s),"\\n";\nprint_r(explode(" ",trim($s))); // split to array\necho implode("-",["2026","04","01"]),"\\n"; // join\necho substr(trim($s),7,3),"\\n";  // PHP\necho strpos($s,"PHP"),"\\n";      // position\necho sprintf("Name: %s, GPA: %.2f","Alice",3.8),"\\n";\necho str_pad("5",4,"0",STR_PAD_LEFT),"\\n"; // 0005\necho str_repeat("*",10),"\\n";',"String functions: trim, upper, replace, sprintf"),
    "php_forms":('<?php\n// form_handler.php\nif($_SERVER["REQUEST_METHOD"]==="POST"){\n    // Sanitize inputs\n    $name  =htmlspecialchars($_POST["name"]??"");\n    $email =filter_input(INPUT_POST,"email",FILTER_SANITIZE_EMAIL);\n    $age   =filter_input(INPUT_POST,"age",FILTER_VALIDATE_INT);\n\n    if(!$name||!$email||$age===false){\n        echo "Invalid input!";\n    } else {\n        echo "Welcome, $name! Age: $age";\n    }\n}\n?>\n<form method="POST">\n    <input type="text"  name="name"  placeholder="Name"><br>\n    <input type="email" name="email" placeholder="Email"><br>\n    <input type="number"name="age"   placeholder="Age"><br>\n    <button type="submit">Submit</button>\n</form>',"Form handling: POST, sanitize, validate"),
    "php_oop":('<?php\nclass BankAccount {\n    private float $balance;\n    public string $owner;\n\n    public function __construct(string $owner, float $balance=0){\n        $this->owner   = $owner;\n        $this->balance = $balance;\n    }\n\n    public function deposit(float $amount): bool {\n        if($amount<=0) return false;\n        $this->balance+=$amount;\n        return true;\n    }\n\n    public function getBalance(): float { return $this->balance; }\n\n    public function __toString(): string {\n        return "{$this->owner}: \\${$this->balance}";\n    }\n}\n\n$acc=new BankAccount("Alice",1000);\n$acc->deposit(500);\necho $acc,"\\n"; // Alice: $1500',"Classes: constructor, properties, methods"),
    "php_inheritance":('<?php\nabstract class Shape {\n    public string $color;\n    public function __construct(string $color="black"){\n        $this->color=$color;\n    }\n    abstract public function area(): float;\n    public function describe(): string {\n        return "{$this->color} ".get_class($this)." area={$this->area()}";\n    }\n}\n\nclass Circle extends Shape {\n    public function __construct(private float $r, string $color="red"){\n        parent::__construct($color);\n    }\n    public function area(): float { return M_PI*$this->r**2; }\n}\n\nclass Rect extends Shape {\n    public function __construct(private float $w,private float $h){\n        parent::__construct("blue");\n    }\n    public function area(): float { return $this->w*$this->h; }\n}\n\nforeach([new Circle(5),new Rect(4,6)] as $s)\n    echo $s->describe(),"\\n";',"Abstract, extends, parent::__construct"),
    "php_traits":('<?php\ntrait Loggable {\n    public function log(string $msg): void {\n        echo "[LOG] ".date("H:i:s")." $msg\\n";\n    }\n}\n\ntrait Timestampable {\n    private ?string $createdAt=null;\n    public function setCreated(): void { $this->createdAt=date("Y-m-d"); }\n    public function getCreated(): ?string { return $this->createdAt; }\n}\n\ninterface Serializable { public function serialize(): string; }\n\nclass User implements Serializable {\n    use Loggable, Timestampable;\n    public function __construct(private string $name){}\n    public function serialize(): string { return json_encode(["name"=>$this->name]); }\n}\n\n$u=new User("Alice");\n$u->log("User created");\n$u->setCreated();\necho $u->serialize(),"\\n";',"Traits + Interfaces in PHP"),
    "php_pdo":('<?php\ntry {\n    // Connect to MySQL via PDO\n    $pdo=new PDO(\n        "mysql:host=localhost;dbname=mydb;charset=utf8mb4",\n        "root", "password",\n        [PDO::ATTR_ERRMODE=>PDO::ERRMODE_EXCEPTION]\n    );\n\n    // CREATE TABLE\n    $pdo->exec("CREATE TABLE IF NOT EXISTS users(\n        id INT AUTO_INCREMENT PRIMARY KEY,\n        name VARCHAR(100) NOT NULL,\n        email VARCHAR(255) UNIQUE NOT NULL\n    ) ENGINE=InnoDB");\n\n    // INSERT (prepared statement — prevents SQL injection!)\n    $stmt=$pdo->prepare("INSERT INTO users(name,email) VALUES(?,?)");\n    $stmt->execute(["Alice","alice@email.com"]);\n\n    // SELECT\n    $stmt=$pdo->prepare("SELECT * FROM users WHERE name=:name");\n    $stmt->execute([":name"=>"Alice"]);\n    $user=$stmt->fetch(PDO::FETCH_ASSOC);\n    echo $user["name"]." ".$user["email"]."\\n";\n\n} catch(PDOException $e) {\n    echo "DB Error: ".$e->getMessage();\n}',"PDO: connect, prepared statements, fetch"),
    "php_sessions":('<?php\nsession_start(); // must be first!\n\n// Set session\n$_SESSION["user"] = "Alice";\n$_SESSION["role"] = "admin";\n$_SESSION["login_time"] = time();\n\n// Read session\nif(isset($_SESSION["user"])){\n    echo "Logged in as: ".$_SESSION["user"]."\\n";\n    echo "Role: ".$_SESSION["role"]."\\n";\n}\n\n// Destroy session (logout)\n// session_destroy();\n\n// Cookies\nsetcookie("preferences","dark_mode",time()+86400,"/"); // 1 day\nif(isset($_COOKIE["preferences"])){\n    echo "Theme: ".$_COOKIE["preferences"]."\\n";\n}',"Sessions: start, set, read, destroy + Cookies"),
    "php_files":('<?php\n// Write file\nfile_put_contents("data.txt","Hello PHP File!\\nLine 2\\n");\n\n// Read file\n$content=file_get_contents("data.txt");\necho $content;\n\n// Read line by line\n$lines=file("data.txt",FILE_IGNORE_NEW_LINES);\nforeach($lines as $i=>$line)\n    echo "Line ".$i.": $line\\n";\n\n// File operations\necho file_exists("data.txt")?"Exists\\n":"Not found\\n";\necho filesize("data.txt")." bytes\\n";\n\n// fopen/fwrite/fclose\n$fh=fopen("log.txt","a"); // append mode\nfwrite($fh,date("Y-m-d H:i:s")." App started\\n");\nfclose($fh);\n\n// Directory listing\nforeach(glob("*.php") as $file)\n    echo "$file\\n";',"File: read, write, exists, fopen, glob"),
    "php_json":('<?php\n// PHP array to JSON\n$data=[\n    "name"=>"Alice",\n    "age"=>25,\n    "skills"=>["PHP","MySQL","JavaScript"],\n    "active"=>true\n];\n$json=json_encode($data,JSON_PRETTY_PRINT);\necho $json,"\\n";\n\n// JSON to PHP array\n$jsonStr=\'{"name":"Bob","score":92}\';\n$arr=json_decode($jsonStr,true); // true = array\necho $arr["name"]," scored ",$arr["score"],"\\n";\n\n// API call with cURL\nfunction fetchAPI(string $url): array {\n    $ch=curl_init($url);\n    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);\n    $response=curl_exec($ch);\n    curl_close($ch);\n    return json_decode($response,true)??[];\n}',"JSON encode/decode + cURL API calls"),
    "php_advanced":('<?php\n// Closures with use\n$multiplier=3;\n$triple=function($n) use ($multiplier) { return $n*$multiplier; };\necho $triple(7),"\\n"; // 21\n\n// Named arguments (PHP 8+)\nfunction createUser(string $name,int $age=18,string $role="user"):string{\n    return "$name($age)[$role]";\n}\necho createUser(role:"admin",name:"Alice"),"\\n";\n\n// Null safe operator (PHP 8+)\nclass User { public ?Address $address=null; }\nclass Address { public string $city="Delhi"; }\n$user=new User();\necho $user?->address?->city ?? "No city","\\n"; // No city\n\n// Fibers (PHP 8.1) — lightweight coroutines\n$fiber=new Fiber(function():void{\n    echo "Fiber start\\n";\n    Fiber::suspend("paused");\n    echo "Fiber end\\n";\n});\n$value=$fiber->start();\necho "Got: $value\\n";\n$fiber->resume();',"Closures, named args, null safe, Fibers"),
}

for nid,title,phase in php_nodes_raw[2:]:
    if nid=="php_interview":
        ph[nid]={"title":"PHP Interview Guide","explanation":"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;'>Top PHP Interview Questions</h3><p style='color:#475569;margin-bottom:30px;'>Most asked PHP interview questions — TCS, Wipro, web agencies, WordPress shops.</p>"+
            "".join([f"<div style='background:#f8fafc;border-left:4px solid #0ea5e9;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#0ea5e9;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
            for i,(q,a) in enumerate([
                ("What is the difference between echo and print?","Both output text. echo: no return value, can take multiple args, slightly faster. print: returns 1, can use in expressions, single arg only."),
                ("== vs === in PHP?","== compares values with type coercion ('1'==1 is true). === compares value AND type ('1'===1 is false)."),
                ("What are PHP sessions?","Sessions store user data across multiple pages server-side. Start with session_start(). Data stored in $_SESSION superglobal."),
                ("What is PDO?","PHP Data Objects — database abstraction layer. Prevents SQL injection via prepared statements. Works with MySQL, SQLite, PostgreSQL."),
                ("What is the difference between include and require?","require: fatal error if file not found (stops execution). include: warning only (continues execution). Use require for critical files."),
                ("What are PHP traits?","Traits allow code reuse in single inheritance languages. Use 'use TraitName' inside a class to include trait methods."),
                ("What is the null coalescing operator ??","Returns left side if it exists and is not null, otherwise right side. $x = $_GET['id'] ?? 'default';"),
                ("What is PHP 8's match expression?","Like switch but strict comparison (===), expression (returns value), no fall-through, exhaustive checking."),
                ("What is the difference between GET and POST?","GET: data in URL, visible, bookmarkable, max ~2KB, for reading. POST: data in body, hidden, no limit, for creating/changing data."),
                ("How to prevent SQL injection in PHP?","Use PDO or MySQLi with prepared statements and parameterized queries. Never concatenate user input directly into SQL."),
            ])])+"</div>","examples":[],"concept_quiz":[],"hands_on":None,"problem_solving":[]}
    elif nid in php_topic_codes:
        code,lbl=php_topic_codes[nid]
        ph[nid]={"title":title,"explanation":expl(title,[("Key Concepts",f"{title} is a core PHP skill for web development.",[(lbl,code)])]),"examples":[],"concept_quiz":quiz([("PHP is primarily used for?",["Desktop apps","Server-side web development","Mobile apps","Database management"],"Server-side web development"),("PHP arrays support?",["Only integers as keys","Only strings as keys","Both integers and strings as keys","Only one type"],"Both integers as keys and string keys")]),"hands_on":task(f"Practice {title}",f"Apply {title} in a PHP script.","Use the example above as reference.",code),"problem_solving":probs([(f"{title} Challenge","FizzBuzz 1-20.",'<?php\nfor($i=1;$i<=20;$i++)\n    echo($i%15==0?"FizzBuzz":($i%3==0?"Fizz":($i%5==0?"Buzz":$i)))."\\n";'),(f"{title} Example 2","Count words in a string.",'<?php\n$s="The quick brown fox";\necho str_word_count($s)."\\n"; // 4')])}

data['php']={"title":"PHP - Beginner to Advanced","description":"Master PHP for web development including OOP, PDO, sessions, forms, JSON and REST APIs.","nodes":php_nodes,"content":ph}
print(f"PHP: {len(php_nodes)} nodes injected!")
new_text="window.tracksData = "+json.dumps(data,indent=2,ensure_ascii=False)+";\n"
with open(file_path,'w',encoding='utf-8') as f: f.write(new_text)
print("Saved!")
