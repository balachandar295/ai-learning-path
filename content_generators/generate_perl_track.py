import json

file_path = r'core\static\tracks_data.js'
with open(file_path,'r',encoding='utf-8') as f: text=f.read()
json_start=text.find('{')
data=json.loads(text[json_start:text.rfind('}')+1])

def card(label,code):
    return f"<div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'><div style='background:linear-gradient(to right,#0ea5e9,#3b82f6);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>{label}</div><pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>{code}</pre></div>"

def section(title,desc,examples):
    h=f"<h4 style='color:#0ea5e9;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #0ea5e9;padding-left:12px;'>{title}</h4>"
    h+=f"<p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>{desc}</p>"
    for lbl,code in examples: h+=card(lbl,code)
    return h

def explanation(title,sections):
    h=f"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>"
    for s in sections: h+=section(*s)
    return h+"</div>"

def quiz(items): return [{"q":q,"options":o,"answer":a} for q,o,a in items]
def task(t,d,h,c): return {"title":t,"description":d,"hint":h,"code":c}
def problems(items): return [{"title":t,"description":d,"code":c} for t,d,c in items]

# ══════ PERL NODES ══════
pl_nodes_raw=[
    ("pl_basics",    "Perl Basics",          1),("pl_variables","Variables & Types",   1),
    ("pl_operators", "Operators",             1),("pl_control",  "Control Flow",         1),
    ("pl_loops",     "Loops",                 1),("pl_strings",  "Strings",               2),
    ("pl_arrays",    "Arrays",                2),("pl_hashes",   "Hashes",                2),
    ("pl_regex",     "Regular Expressions",   2),("pl_subs",     "Subroutines",           3),
    ("pl_fileio",    "File I/O",              3),("pl_refs",     "References",            3),
    ("pl_oop",       "OOP in Perl",           3),("pl_modules",  "Modules & Packages",    4),
    ("pl_advanced",  "Advanced Perl",         4),("pl_cpan",     "CPAN & Libraries",      4),
    ("pl_scripting", "Perl Scripting",        4),("pl_interview","Perl Interview Guide",  5),
]

pl_nodes=[]
for i,(nid,title,phase) in enumerate(pl_nodes_raw):
    node={"id":nid,"title":title,"x":1250 if i%2==0 else 1530,"y":150+i*160,
          "status":"available" if i==0 else "locked","phase":phase}
    if i>0: node["parent"]=pl_nodes_raw[i-1][0]
    pl_nodes.append(node)

pl={}

pl["pl_basics"]={
    "title":"Perl Basics",
    "explanation":explanation("Perl Basics",[
        ("What is Perl?","Perl (Practical Extraction and Reporting Language) was created by Larry Wall in 1987. It excels at text processing, system administration, bioinformatics, and web CGI scripting. Known for its powerful regex engine.",
         [("Hello World",'#!/usr/bin/perl\nuse strict;    # enforce good coding practices\nuse warnings;  # show helpful warnings\n\nprint "Hello, World!\\n";\nprint "Perl is powerful!\\n";\n\n# say automatically adds newline (like println)\nuse feature \'say\';\nsay "Same as print with newline!";'),
          ("Running Perl",'# Save as hello.pl, then run:\n# perl hello.pl\n\n# Check version:\n# perl -v\n\n# One-liner:\n# perl -e \'print "Hi!\\n"\'\n\n# With stdin:\n# perl -n -e \'print if /pattern/\' file.txt')]),
        ("Input & Output","Use print/say for output. Use <STDIN> or <> to read input. chomp removes trailing newline.",
         [("Print & say",'use feature \'say\';\n\nmy $name = "Alice";\nmy $age  = 25;\n\nprint "Name: $name\\n";     # print with explicit newline\nsay "Age: $age";            # say adds newline automatically\nprintf "GPA: %.2f\\n", 3.8; # formatted output'),
          ("Reading input",'#!/usr/bin/perl\nuse strict; use warnings;\n\nprint "Enter your name: ";\nmy $name = <STDIN>;    # read line\nchomp($name);          # remove trailing newline\n\nprint "Enter your age: ";\nmy $age = <STDIN>;\nchomp($age);\n\nprintf "Hello, %s! You are %d years old.\\n", $name, $age;')]),
    ]),
    "examples":[],
    "concept_quiz":quiz([
        ("Perl was created by?",["Larry Wall","Guido van Rossum","Brendan Eich","Dennis Ritchie"],"Larry Wall"),
        ("use strict does what?",["Slows program","Enforces variable declaration and good practices","Enables type safety","Imports modules"],"Enforces variable declaration and good practices"),
        ("chomp() does what?",["Removes first char","Removes trailing newline","Converts to lowercase","Splits string"],"Removes trailing newline"),
        ("Perl is best known for?",["Web frameworks","Text processing and regex","Database management","Mobile apps"],"Text processing and regex"),
        ("Perl file extension is?",["pp",".pl",".pe",".pr"],".pl"),
    ]),
    "hands_on":task("Hello Perl","Write a Perl program that reads name and age, greets the user with formatted output.","Use chomp after <STDIN>. Use printf for formatting.",'#!/usr/bin/perl\nuse strict; use warnings;\nuse feature \'say\';\n\nprint "Enter name: ";\nmy $name = <STDIN>; chomp($name);\nprint "Enter age: ";\nmy $age = <STDIN>; chomp($age);\n\nsay "Hello, $name!";\nprintf "You are %d years old. In 10 years: %d\\n", $age, $age+10;'),
    "problem_solving":problems([
        ("Sum Two Numbers","Read two numbers, print sum.",'my $a=10; my $b=20;\nprintf "Sum: %d\\n", $a+$b;'),
        ("Circle Area","Calculate area for radius 7.",'use POSIX qw(M_PI);\nmy $r=7;\nprintf "Area: %.2f\\n", M_PI*$r*$r;'),
        ("Celsius to Fahrenheit","Convert 100C to F.",'my $c=100;\nprintf "%.1f C = %.1f F\\n",$c,$c*9/5+32;'),
    ])
}

pl["pl_variables"]={
    "title":"Variables & Data Types",
    "explanation":explanation("Variables & Data Types",[
        ("Perl Variables: $, @, %","Perl has 3 variable types: Scalar ($), Array (@), Hash (%). my declares lexically scoped variable (use with use strict).",
         [("Scalar variables",'#!/usr/bin/perl\nuse strict; use warnings;\n\n# Scalars — single values\nmy $name   = "Alice";      # string\nmy $age    = 25;           # integer\nmy $gpa    = 3.8;          # float\nmy $active = 1;            # boolean (1=true, 0=false)\nmy $undef  = undef;        # undefined\n\nprint "Name: $name, Age: $age, GPA: $gpa\\n";\n\n# Perl auto-converts between str and num\nmy $s = "42";\nmy $n = $s + 8;   # "42" treated as number -> 50\nprint "Result: $n\\n";  # 50'),
          ("Context: string vs numeric",'my $x = "5 apples";\nmy $y = $x + 3;     # numeric context: 5+3=8\nprint "Numeric: $y\\n"; # 8\n\nmy $str = "Hello" x 3;  # string repetition\nprint "$str\\n";  # HelloHelloHello\n\nmy $num = 2 ** 10;\nprint "2^10 = $num\\n";  # 1024')]),
        ("Arrays & Hashes overview","@ prefix = array (ordered list). % prefix = hash (key-value pairs).",
         [("Quick arrays & hashes",'# Array\nmy @fruits = ("apple","banana","cherry");\nprint "First: $fruits[0]\\n";    # apple\nprint "Count: ", scalar @fruits, "\\n"; # 3\n\n# Hash\nmy %person = (name=>"Bob", age=>30, city=>"Delhi");\nprint "Name: $person{name}\\n";  # Bob\nprint "Age:  $person{age}\\n";   # 30'),
          ("undef and defined",'my $x = undef;\nif (defined $x) { print "Defined\\n"; }\nelse            { print "Undefined\\n"; }  # prints this\n\n$x = 0;\nif (defined $x) { print "Defined (even if 0)\\n"; }  # True! 0 is defined')]),
    ]),
    "examples":[],
    "concept_quiz":quiz([
        ("Scalar variable prefix?",["@","#","$","%"],"$"),
        ("Array prefix?",["$","@","%","^"],"@"),
        ("Hash prefix?",["$","@","*","%"],"%"),
        ("undef vs 0 in Perl?",["Same","undef is undefined, 0 is defined false","0 is undef","Cannot compare"],"undef is undefined, 0 is defined false"),
        ("x operator in Perl?",["Multiply","String repetition","XOR","Cross product"],"String repetition"),
    ]),
    "hands_on":task("Variable Explorer","Declare scalar, array, hash. Print each type with its data.",'Use $, @, %.',' #!/usr/bin/perl\nuse strict; use warnings;\n\nmy $lang   = "Perl";\nmy @skills = ("regex","scripting","text processing");\nmy %info   = (version=>5, year=>1987, creator=>"Larry Wall");\n\nprint "Language: $lang\\n";\nprint "Skills: @skills\\n";\nprint "Version: $info{version}\\n";\nprint "Creator: $info{creator}\\n";'),
    "problem_solving":problems([
        ("String repetition","Print 'ha' repeated 5 times.",'print "ha"x5,"\\n";'),
        ("Array info","Show size and last element of array.",'my @a=(10,20,30,40);\nprintf "Size: %d, Last: %d\\n",scalar @a,$a[-1];'),
        ("Hash access","Create hash of 3 capitals, print India\'s.",'my %cap=(India=>"Delhi",Japan=>"Tokyo",France=>"Paris");\nprint "India: $cap{India}\\n";'),
    ])
}

# Remaining Perl topics
pl_codes={
    "pl_operators":('my $a=17;my $b=5;\nprint $a+$b,"\\n";  # 22\nprint $a/$b,"\\n";  # 3.4 (Perl does float div!)\nprint $a%$b,"\\n";  # 2\nprint $a**2,"\\n";  # 289 (power)\n\n# String operators\nmy $s="Hello"." World"; # concatenation\nprint "$s\\n";\nprint "ha"x3,"\\n";     # hahaha\n\n# Comparison\nprint 5==5?"Equal":"NotEqual","\\n";\nprint "abc" eq "abc"?"Same":"Diff","\\n"; # string compare','Arithmetic, string, comparison operators'),
    "pl_control":('my $score=82;\nif   ($score>=90){ print "A\\n" }\nelsif($score>=75){ print "B\\n" }\nelsif($score>=60){ print "C\\n" }\nelse             { print "F\\n" }\n\n# unless = if not\nmy $raining=0;\nunless($raining){ print "Go outside!\\n" }\n\n# Postfix if\nprint "Adult\\n" if $score>=18;\nprint "Low\\n"  unless $score>90;\n\n# Ternary\nmy $g=$score>=60?"Pass":"Fail";\nprint "Result: $g\\n";','if/elsif/else, unless, postfix, ternary'),
    "pl_loops":('# for/foreach\nfor my $i (1..5){ print "$i " } print "\\n";\nforeach my $fruit ("apple","banana","cherry"){\n    print "Fruit: $fruit\\n";\n}\n\n# while\nmy $n=1;\nwhile($n<=5){ print "$n "; $n++ }\nprint "\\n";\n\n# do-while\nmy $x=0;\ndo { print "x=$x\\n"; $x++ } while($x<3);\n\n# map and grep (functional)\nmy @nums=(1..10);\nmy @evens=grep{$_%2==0}@nums;\nmy @doubled=map{$_*2}@nums;\nprint "@evens\\n";    # 2 4 6 8 10\nprint "@doubled\\n";  # 2 4 6 8 10 12 14 16 18 20','for, foreach, while, map, grep'),
    "pl_strings":('my $s="  Hello, Perl World!  ";\n$s=~s/^\\s+|\\s+$//g; # trim (regex)\nprint "Length: ",length($s),"\\n";\nprint "Upper: ",uc($s),"\\n";\nprint "Lower: ",lc($s),"\\n";\nprint "Has Perl: ",($s=~/Perl/?"Yes":"No"),"\\n";\n\n(my $replaced=$s)=~s/Perl/Python/;\nprint "Replaced: $replaced\\n";\n\nmy @words=split(/\\s+/,$s);\nprint "Words: ",scalar @words,"\\n";\n\nmy $joined=join("-",@words);\nprint "Joined: $joined\\n";\n\n# substr\nprint "Sub: ",substr($s,7,4),"\\n";  # Perl','String functions: uc, lc, length, split, join, substr'),
    "pl_arrays":('my @arr=(5,3,8,1,9,2);\n\n# Push/pop (end), shift/unshift (start)\npush @arr,10;    # add to end\nmy $last=pop @arr; # remove from end\nunshift @arr,0;  # add to start\nmy $first=shift @arr; # remove from start\n\n# Sort\nmy @sorted=sort{$a<=>$b}@arr;  # numeric sort\nprint "@sorted\\n";\n\n# Slice\nmy @slice=@arr[1..3];\n\n# Grep and map\nmy @big=grep{$_>5}@arr;\nmy @sq=map{$_**2}@arr;\n\n# Reverse, join\nprint join(",",reverse @sorted),"\\n";\nprintf "Sum: %d\\n", eval join("+",@arr);','push, pop, sort, grep, map, slice, join'),
    "pl_hashes":('my %capitals=(\n    India  =>"Delhi",\n    Japan  =>"Tokyo",\n    France =>"Paris",\n    Germany=>"Berlin"\n);\n\n# Access\nprint $capitals{India},"\\n";\n\n# Add / modify / delete\n$capitals{Italy}="Rome";\ndelete $capitals{France};\n\n# Check existence\nif(exists $capitals{Japan})  { print "Japan exists\\n" }\nif(!defined $capitals{USA})  { print "USA undefined\\n" }\n\n# Keys and values\nforeach my $k(sort keys %capitals){\n    printf "%-10s -> %s\\n",$k,$capitals{$k};\n}\n\n# Hash slice\nmy @some=@capitals{qw(India Japan)};\nprint "@some\\n";  # Delhi Tokyo','Hash: access, add, delete, keys, values, slices'),
    "pl_regex":('my $text="The quick brown fox jumps over the lazy dog";\n\n# Match\nif($text=~/fox/)  { print "Found fox!\\n" }\n\n# Capture groups\n$text=~/(\\w+)\\s+(\\w+)/;\nprint "First two words: $1 $2\\n";\n\n# Global match — find all words\nmy @words=($text=~/\\b\\w{4}\\b/g);\nprint "4-letter words: @words\\n";\n\n# Substitution\n(my $new=$text)=~s/fox/cat/g;\nprint "Replaced: $new\\n";\n\n# Case-insensitive\nif($text=~/THE/i) { print "Case insensitive match!\\n" }\n\n# Split with regex\nmy @parts=split(/\\s+/,$text);\nprintf "Word count: %d\\n",scalar @parts;',"=~, /pattern/, capture groups, s///, flags"),
    "pl_subs":('# Subroutine (function in Perl)\nsub greet {\n    my ($name,$greeting)=@_;   # @_ = argument array\n    $greeting//="Hello";       # default value\n    return "$greeting, $name!";\n}\n\nprint greet("Alice"),"\\n";\nprint greet("Bob","Hi"),"\\n";\n\n# Return multiple values\nsub min_max {\n    my @nums=@_;\n    return (sort{$a<=>$b}@nums)[0,-1];\n}\nmy($min,$max)=min_max(3,1,8,2,9);\nprint "Min=$min Max=$max\\n";\n\n# Recursive\nsub factorial {\n    my $n=shift;\n    return 1 if $n<=1;\n    return $n*factorial($n-1);\n}\nprint "5! = ",factorial(5),"\\n";','Subroutines: @_, defaults, return, recursion'),
    "pl_fileio":('use strict;use warnings;\n\n# Write to file\nopen(my $fh,">","output.txt") or die "Cannot open: $!";\nprint $fh "Line 1\\n";\nprint $fh "Line 2\\n";\nclose($fh);\n\n# Read file line by line\nopen(my $in,"<","output.txt") or die "Cannot open: $!";\nwhile(my $line=<$in>){\n    chomp $line;\n    print "Read: $line\\n";\n}\nclose($in);\n\n# Read all at once\nopen($in,"<","output.txt") or die $!;\nmy @lines=<$in>;\nclose($in);\nchomp @lines;\nprint "Total lines: ",scalar @lines,"\\n";','File: open, read, write, close, chomp'),
    "pl_refs":('# Reference = pointer to variable\nmy @arr=(1,2,3,4,5);\nmy $ref=\\@arr;     # reference to array\n\nprint $$ref[0],"\\n";      # dereference: 1\nprint $ref->[1],"\\n";     # arrow notation: 2\npush @$ref,6;              # modify via ref\nprint "@arr\\n";  # 1 2 3 4 5 6\n\n# Reference to hash\nmy %h=(a=>1,b=>2);\nmy $href=\\%h;\nprint $href->{a},"\\n";  # 1\n\n# Anonymous refs\nmy $aref=[10,20,30];      # anonymous array ref\nmy $hrf={x=>1,y=>2};     # anonymous hash ref\nprint $aref->[1],"\\n";  # 20\nprint $hrf->{x},"\\n";   # 1','References: \\, dereference, arrow notation, anonymous'),
}

for nid,title,phase in pl_nodes_raw[2:]:
    if nid=="pl_interview":
        pl[nid]={
            "title":"Perl Interview Guide",
            "explanation":"<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;'>Top Perl Interview Questions</h3><p style='color:#475569;margin-bottom:30px;'>Most asked Perl questions in sysadmin, bioinformatics, and scripting roles.</p>"+
                "".join([f"<div style='background:#f8fafc;border-left:4px solid #0ea5e9;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#0ea5e9;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
                for i,(q,a) in enumerate([
                    ("What are Perl's three variable types?","Scalar ($): single value. Array (@): ordered list. Hash (%): key-value pairs."),
                    ("What does use strict do?","Enforces variable declaration with my, prevents barewords and symbolic refs. Essential for clean code."),
                    ("What is chomp()?","Removes trailing newline from a string. Essential after reading <STDIN> or file lines."),
                    ("What are references in Perl?","Scalar values pointing to another variable. Created with \\. Used to pass arrays/hashes to subroutines and create complex data structures."),
                    ("Explain Perl regex syntax.","m// for matching, s/// for substitution. =~ binds regex to variable. Flags: /g (global), /i (case-insensitive), /m (multiline)."),
                    ("What is wantarray()?","Returns true if subroutine is called in list context, false in scalar context. Allows context-sensitive returns."),
                    ("What is the difference between my and local?","my creates lexically scoped variable. local temporarily overrides a global variable within the current scope (dynamic scoping)."),
                    ("What is Perl's die() function?","Throws an exception / terminates script with a message. Used with 'or die $!' after file operations."),
                    ("What are CPAN modules?","Comprehensive Perl Archive Network — library of 25,000+ reusable Perl modules. Install with: cpan Module::Name or cpanm."),
                    ("What is grep() in Perl?","Filters a list based on a condition. Returns elements where the block is true. Similar to filter() in other languages."),
                ])]) + "</div>",
            "examples":[],"concept_quiz":[],"hands_on":None,"problem_solving":[]
        }
    elif nid in pl_codes:
        code,lbl=pl_codes[nid]
        pl[nid]={
            "title":title,
            "explanation":explanation(title,[("Key Concepts",f"{title} is essential for Perl scripting.",[(lbl,code)])]),
            "examples":[],
            "concept_quiz":quiz([
                (f"What makes {title} special in Perl?",["Nothing","Perl has unique syntax and power","Only in Java","Only basic"],"Perl has unique syntax and power"),
                ("Perl is best for?",["Mobile apps","Text processing and scripting","Web frameworks","Desktop GUIs"],"Text processing and scripting"),
            ]),
            "hands_on":task(f"Practice {title}",f"Apply {title} concepts in a Perl script.","Use the examples above as reference.",code),
            "problem_solving":problems([
                (f"{title} Example",f"Working example of {title}.",code),
                ("Count vowels","Count vowels in 'Hello World'.",'my $s="Hello World";\nmy $count=()=$s=~/[aeiou]/gi;\nprint "Vowels: $count\\n";'),
            ])
        }
    elif nid not in pl:
        pl[nid]={
            "title":title,
            "explanation":explanation(title,[(f"Introduction to {title}",f"{title} is an important Perl concept.",[("Example",f'#!/usr/bin/perl\nuse strict; use warnings;\n# {title} example\nprint "Learning {title}!\\n";')])]),
            "examples":[],"concept_quiz":quiz([("Perl prefix for OOP packages?",["$","::","->","use"],"::"),("Perl module files end with?",[".pm",".pl",".pr",".mod"],".pm"),]),
            "hands_on":task(f"Practice {title}",f"Apply {title} in Perl.","Refer to Perl documentation.",f'print "Practicing {title}\\n";'),
            "problem_solving":problems([(f"{title} task",f"Implement {title}.",f'print "{title}\\n";')])
        }

data['perl']={"title":"Perl - Beginner to Advanced","description":"Master Perl for text processing, system scripting, regex, and automation.","nodes":pl_nodes,"content":pl}
print(f"Perl track: {len(pl_nodes)} nodes")
new_text="window.tracksData = "+json.dumps(data,indent=2,ensure_ascii=False)+";\n"
with open(file_path,'w',encoding='utf-8') as f: f.write(new_text)
print("Saved!")
