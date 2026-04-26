import json
import os

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
# MYSQL TRACK — 18 Topics
# ══════════════════════════════════════════════
mysql_nodes_raw = [
    ("mysql_basics",      "MySQL Basics",       1),
    ("mysql_datatypes",   "Data Types",         1),
    ("mysql_crud",        "CRUD Operations",    1),
    ("mysql_filtering",   "Filtering (WHERE)",  1),
    ("mysql_sorting",     "Sorting & Paging",   1),
    ("mysql_functions",   "Built-in Functions", 2),
    ("mysql_grouping",    "Grouping Data",      2),
    ("mysql_joins",       "Joins",              2),
    ("mysql_subqueries",  "Subqueries",         2),
    ("mysql_set_ops",     "Set Operations",     3),
    ("mysql_constraints", "Constraints",        3),
    ("mysql_indexes",     "Indexes",            3),
    ("mysql_views",       "Views",              3),
    ("mysql_transactions","Transactions",       4),
    ("mysql_triggers",    "Triggers",           4),
    ("mysql_procedures",  "Stored Procedures",  4),
    ("mysql_optimization","Optimization",       4),
    ("mysql_interview",   "Interview Guide",    5),
]

mysql_nodes = []
for i, (nid, title, phase) in enumerate(mysql_nodes_raw):
    node = {"id": nid, "title": title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase}
    if i > 0: node["parent"] = mysql_nodes_raw[i-1][0]
    mysql_nodes.append(node)

# ══════ MYSQL CONTENT ══════
mysql_content = {}

mysql_content["mysql_basics"] = {
    "title": "MySQL Basics",
    "explanation": explanation("MySQL Basics", [
        ("What is MySQL?",
         "MySQL is a popular open-source relational database management system (RDBMS) based on Structured Query Language (SQL). It organizes data into tables consisting of rows and columns.",
         [("Connect & Create Database", '-- Create a new database\nCREATE DATABASE learning_db;\n\n-- Use the database\nUSE learning_db;'),
          ("Create a Table", '-- Create a simple table\nCREATE TABLE users (\n    id INT AUTO_INCREMENT PRIMARY KEY,\n    username VARCHAR(50) NOT NULL,\n    email VARCHAR(100),\n    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);')]),
        ("Basic SQL Syntax",
         "SQL statements usually end with a semicolon (;). They are not case-sensitive, but uppercase is conventional for keywords.",
         [("Show Information", '-- List all databases\nSHOW DATABASES;\n\n-- List tables in current database\nSHOW TABLES;\n\n-- Show table structure\nDESCRIBE users;')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does RDBMS stand for?", ["Relational Database Management System", "Record Database Management System", "Relational Data Manipulation System", "Real Data Management System"], "Relational Database Management System"),
        ("Which keyword is used to select a database to use?", ["SELECT DATABASE", "USE", "CHOOSE", "CONNECT"], "USE"),
        ("What does the DESCRIBE command do?", ["Shows all databases", "Describes the table contents", "Shows the schema/structure of a table", "Deletes a table"], "Shows the schema/structure of a table"),
        ("Are SQL keywords case-sensitive?", ["Yes", "No", "Only on Linux", "Only SELECT is"], "No"),
        ("Which command lists all tables in the current database?", ["SHOW DATABASES;", "LIST TABLES;", "DISPLAY TABLES;", "SHOW TABLES;"], "SHOW TABLES;"),
    ]),
    "hands_on": task("Create a Database", "Write a query to create a database named 'School' and switch to it.", "Use CREATE DATABASE and USE.", 'CREATE DATABASE School;\nUSE School;'),
    "problem_solving": problems([
        ("Create Students Table", "Create a 'students' table with id (INT, Primary Key) and name (VARCHAR(100)).", 'CREATE TABLE students (\n    id INT PRIMARY KEY,\n    name VARCHAR(100)\n);'),
        ("Show Databases", "List all databases.", 'SHOW DATABASES;'),
        ("Describe Table", "Show the structure of the 'students' table.", 'DESCRIBE students;'),
    ])
}

mysql_content["mysql_datatypes"] = {
    "title": "Data Types",
    "explanation": explanation("Data Types", [
        ("Numeric Types",
         "Used to store numbers. Common types include INT (whole numbers), DECIMAL (exact decimals like money), and FLOAT/DOUBLE (floating-point numbers).",
         [("Numeric Examples", 'CREATE TABLE products (\n    id INT,\n    price DECIMAL(10, 2), -- 10 digits total, 2 after decimal\n    weight FLOAT\n);')]),
        ("String Types",
         "Used to store text. CHAR is fixed-length, VARCHAR is variable-length. TEXT is used for very long strings.",
         [("String Examples", 'CREATE TABLE articles (\n    code CHAR(5),        -- Always exactly 5 chars\n    title VARCHAR(200),  -- Up to 200 chars\n    content TEXT         -- Long text\n);')]),
        ("Date & Time Types",
         "Used to store dates and times. DATE (YYYY-MM-DD), DATETIME (YYYY-MM-DD HH:MM:SS), TIMESTAMP (auto-updates).",
         [("Date Examples", 'CREATE TABLE events (\n    event_date DATE,\n    start_time DATETIME,\n    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n);')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("Which data type is best for storing currency?", ["FLOAT", "INT", "DECIMAL", "VARCHAR"], "DECIMAL"),
        ("What is the difference between CHAR and VARCHAR?", ["CHAR holds numbers, VARCHAR holds strings", "CHAR is fixed-length, VARCHAR is variable-length", "VARCHAR is older", "They are identical"], "CHAR is fixed-length, VARCHAR is variable-length"),
        ("Which format does DATE use?", ["DD-MM-YYYY", "MM/DD/YYYY", "YYYY-MM-DD", "YYYY-DD-MM"], "YYYY-MM-DD"),
        ("Which data type is best for a blog post body?", ["CHAR(100)", "VARCHAR(50)", "INT", "TEXT"], "TEXT"),
        ("Which type automatically updates when a row is modified?", ["DATE", "DATETIME", "TIMESTAMP", "TIME"], "TIMESTAMP"),
    ]),
    "hands_on": task("Create Employee Table", "Create an 'employees' table with id (INT), name (VARCHAR(50)), salary (DECIMAL(8,2)), and hire_date (DATE).", "Match exactly these column names and types.", 'CREATE TABLE employees (\n    id INT,\n    name VARCHAR(50),\n    salary DECIMAL(8,2),\n    hire_date DATE\n);'),
    "problem_solving": problems([
        ("Book Table", "Table 'books' with isbn (CHAR(13)) and title (VARCHAR(150)).", 'CREATE TABLE books (\n    isbn CHAR(13),\n    title VARCHAR(150)\n);'),
        ("Time Tracking", "Table 'logs' with action (VARCHAR(20)) and created_at (TIMESTAMP).", 'CREATE TABLE logs (\n    action VARCHAR(20),\n    created_at TIMESTAMP\n);'),
        ("Account Balance", "Table 'accounts' with acc_no (INT) and balance (DECIMAL(12,2)).", 'CREATE TABLE accounts (\n    acc_no INT,\n    balance DECIMAL(12, 2)\n);'),
    ])
}

mysql_content["mysql_crud"] = {
    "title": "CRUD Operations",
    "explanation": explanation("CRUD Operations", [
        ("C - Create (Insert)",
         "Insert new records into a table using the INSERT INTO statement.",
         [("Insert Data", 'INSERT INTO users (username, email) \nVALUES (\'alice\', \'alice@example.com\');\n\n-- Multiple rows\nINSERT INTO users (username, email) \nVALUES \n    (\'bob\', \'bob@ex.com\'),\n    (\'charlie\', \'charlie@ex.com\');')]),
        ("R - Read (Select)",
         "Retrieve data from tables using the SELECT statement.",
         [("Select Data", '-- Select all columns\nSELECT * FROM users;\n\n-- Select specific columns\nSELECT username, email FROM users;')]),
        ("U - Update",
         "Modify existing records using the UPDATE statement. ALWAYS use a WHERE clause! otherwise all rows are updated.",
         [("Update Data", 'UPDATE users \nSET email = \'alice.new@example.com\' \nWHERE username = \'alice\';')]),
        ("D - Delete",
         "Remove records using the DELETE statement. ALWAYS use a WHERE clause!",
         [("Delete Data", 'DELETE FROM users \nWHERE username = \'bob\';\n\n-- Delete all rows (Danger!)\n-- DELETE FROM users;')]),
    ]),
    "examples": [],
    "concept_quiz": quiz([
        ("What does CRUD stand for?", ["Create, Read, Update, Delete", "Copy, Read, Upload, Delete", "Create, Run, Update, Drop", "Connect, Read, Use, Delete"], "Create, Read, Update, Delete"),
        ("Which keyword adds new rows to a table?", ["ADD", "CREATE ROW", "INSERT INTO", "PUT"], "INSERT INTO"),
        ("What happens if you run an UPDATE without a WHERE clause?", ["It throws an error", "It updates the first row", "It updates ALL rows", "It does nothing"], "It updates ALL rows"),
        ("Which command retrieves data from a database?", ["GET", "FETCH", "EXTRACT", "SELECT"], "SELECT"),
        ("How do you delete a specific record?", ["REMOVE FROM table WHERE...", "DELETE * FROM table WHERE...", "DELETE FROM table WHERE...", "DROP ROW table WHERE..."], "DELETE FROM table WHERE..."),
    ]),
    "hands_on": task("Basic CRUD", "Insert a record into 'users': username 'john', email 'john@doe.com'.", "Remember to match string syntax.", "INSERT INTO users (username, email) VALUES ('john', 'john@doe.com');"),
    "problem_solving": problems([
        ("Insert Row", "Insert into 'products': name='Laptop', price=999.99.", "INSERT INTO products (name, price) VALUES ('Laptop', 999.99);"),
        ("Update Price", "Update 'products', set price=1099.99 where name='Laptop'.", "UPDATE products SET price = 1099.99 WHERE name = 'Laptop';"),
        ("Delete Record", "Delete from 'users' where username='john'.", "DELETE FROM users WHERE username = 'john';"),
    ])
}

# Fill remaining MySQL topics with dummy or good content
for nid, title, phase in mysql_nodes_raw[3:]:
    if nid == "mysql_interview":
        mysql_content[nid] = {
            "title": "MySQL Interview Guide",
            "explanation": "<div style='line-height:1.8;'><h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>Top MySQL Interview Questions</h3><p style='color:#475569;font-size:1.1rem;margin-bottom:30px;'>Most asked SQL/MySQL questions in interviews.</p>" +
                "".join([f"<div style='background:#f8fafc;border-left:4px solid #0ea5e9;padding:20px;border-radius:10px;margin-bottom:20px;'><h4 style='color:#0f172a;'><span style='color:#0ea5e9;'>Q{i+1}:</span> {q}</h4><p style='color:#334155;line-height:1.7;'>{a}</p></div>"
                for i,(q,a) in enumerate([
                    ("Difference between DELETE and TRUNCATE?","DELETE removes rows based on WHERE, fires triggers, and can be rolled back. TRUNCATE resets the table, auto-increment, doesn't fire triggers, and is much faster (DDL vs DML)."),
                    ("Difference between INNER JOIN and LEFT JOIN?","INNER JOIN returns only rows that meet the join condition in both tables. LEFT JOIN returns all rows from the left table, and matched rows from the right (returns NULL if no match)."),
                    ("What is a Primary Key vs Unique Key?","Primary Key uniquely identifies a record, cannot be NULL, and a table can have only one. Unique Key ensures uniqueness, can accept one NULL value, and a table can have multiple."),
                    ("What are ACID properties?","Atomicity (all or nothing), Consistency (valid states), Isolation (concurrent safe), Durability (permanent)."),
                    ("What is an Index?","An index improves read (SELECT) performance at the cost of write (INSERT/UPDATE/DELETE) performance and storage space. It works like a book index."),
                    ("Difference between WHERE and HAVING?","WHERE filters rows before grouping (cannot use aggregates). HAVING filters groups after GROUP BY is applied (can use aggregates like COUNT)."),
                    ("What does normalization mean?","Process of organizing data to reduce redundancy and improve data integrity (1NF, 2NF, 3NF)."),
                    ("What is a foreign key?","A column that links to the primary key of another table, ensuring referential integrity."),
                ])]) + "</div>",
            "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
        }
    elif nid not in mysql_content:
        ex_map = {
            "mysql_filtering": ('SELECT * FROM employees\nWHERE age >= 25 AND department = \'Sales\'\n   OR salary > 50000;', "Filtering: WHERE, AND, OR"),
            "mysql_sorting": ('SELECT name, age FROM users\nORDER BY age DESC, name ASC\nLIMIT 10 OFFSET 20;', "Sorting & Paging: ORDER BY, LIMIT, OFFSET"),
            "mysql_functions": ('SELECT COUNT(*), MAX(salary), MIN(age),\n       UPPER(name), DATE_FORMAT(created_at, \'%Y-%m\')\nFROM users;', "Functions: String, Math, Date, Aggregation"),
            "mysql_grouping": ('SELECT department, COUNT(*), SUM(salary)\nFROM employees\nGROUP BY department\nHAVING COUNT(*) > 5;', "Grouping: GROUP BY, HAVING"),
            "mysql_joins": ('SELECT users.name, orders.amount\nFROM users\nINNER JOIN orders ON users.id = orders.user_id;', "Joins: INNER, LEFT, RIGHT"),
            "mysql_subqueries": ('SELECT name FROM employees\nWHERE salary > (SELECT AVG(salary) FROM employees);', "Subqueries: SELECT inside SELECT"),
            "mysql_set_ops": ('SELECT email FROM users_usa\nUNION\nSELECT email FROM users_europe;', "Set Operations: UNION, UNION ALL"),
            "mysql_constraints": ('CREATE TABLE dept (\n    id INT PRIMARY KEY,\n    name VARCHAR(50) UNIQUE NOT NULL\n);', "Constraints: PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT NULL"),
            "mysql_indexes": ('CREATE INDEX idx_user_email ON users(email);', "Indexes: CREATE INDEX to speed up queries"),
            "mysql_views": ('CREATE VIEW active_users AS\nSELECT * FROM users WHERE status = \'active\';', "Views: Virtual tables"),
            "mysql_transactions": ('START TRANSACTION;\nUPDATE accounts SET bal = bal - 100 WHERE id = 1;\nUPDATE accounts SET bal = bal + 100 WHERE id = 2;\nCOMMIT;', "Transactions: START TRANSACTION, COMMIT, ROLLBACK"),
        }
        code, lbl = ex_map.get(nid, (f'-- Example for {title}\nSELECT * FROM {title.replace(" ", "_").lower()};', f"{title} Example"))
        
        mysql_content[nid] = {
            "title": title,
            "explanation": explanation(title, [
                (f"Understanding {title}", f"{title} is an essential MySQL feature for database management.", [(lbl, code)])
            ]),
            "examples": [],
            "concept_quiz": quiz([
                (f"What is the primary use of {title}?", ["Data organization", "Writing queries faster", "Visualizing output", "None of these"], "Data organization"),
                (f"Is {title} specific to MySQL only?", ["Yes", "No, it's standard SQL", "Only in NoSQL", "Only in Oracle"], "No, it's standard SQL"),
            ]),
            "hands_on": task(f"Practice {title}", f"Write a query demonstrating {title}.", "Follow standard SQL syntax.", code),
            "problem_solving": problems([(f"{title} Problem", f"Solve a practical database scenario using {title}.", code)])
        }

# Inject MySQL track
data['mysql'] = {
    "title": "MySQL - Complete Guide",
    "description": "Master SQL and relational databases with MySQL, covering queries, design, and optimization.",
    "nodes": mysql_nodes,
    "content": mysql_content
}

print(f"MySQL track injected with {len(mysql_nodes)} nodes!")
new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("Saved!")
