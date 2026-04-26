import json

filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

prefix = 'window.tracksData = '
d = json.loads(content.split(prefix)[1].strip(';\n'))

last_fixes = {
    "python/strings": {
        0: "<p>You can create a string using either single quotes (<code>'hello'</code>) or double quotes (<code>\"hello\"</code>). Both are identical - choose one style and be consistent. Triple quotes (<code>'''</code> or <code>\"\"\"</code>) create multi-line strings, perfect for long text blocks and docstrings.</p><p>Strings are <strong>immutable</strong> in Python - once created, individual characters cannot be changed. Operations like <code>.upper()</code> return a new string. Strings support indexing (<code>s[0]</code>), slicing (<code>s[1:4]</code>), and negative indexing (<code>s[-1]</code> for the last character).</p>",
        1: "<p>Strings come with dozens of built-in methods. <code>.upper()</code> and <code>.lower()</code> change case. <code>.strip()</code> removes whitespace from both ends. <code>.split()</code> breaks a string into a list. <code>.join()</code> combines a list into a string. <code>.replace(old, new)</code> substitutes text.</p><p>Searching: <code>.find('x')</code> returns the index of 'x' (or -1 if not found). <code>.count('a')</code> counts occurrences. <code>.startswith()</code> and <code>.endswith()</code> check prefixes/suffixes. All methods return new strings without modifying the original.</p>",
        2: "<p>F-strings (formatted string literals) are the modern way to embed expressions in strings. Add <code>f</code> before the quotes: <code>f\"Hello {name}, you are {age} years old\"</code>. You can put any Python expression inside the curly braces: <code>f\"{price * 1.1:.2f}\"</code> formats to 2 decimal places.</p><p>F-strings replace older methods like <code>%</code> formatting and <code>.format()</code>. They're faster, more readable, and more powerful. Use format specifiers for alignment (<code>{name:>20}</code>), padding (<code>{num:05d}</code>), and number formatting (<code>{val:,.2f}</code> for comma-separated decimals).</p>"
    },
    "flask/flask_practices": {
        1: "<p>Never trust user input. Validate all request data with schema libraries like <strong>Marshmallow</strong> or <strong>Cerberus</strong>. Raw form/JSON data can contain SQL injection, XSS attacks, or simply malformed data that crashes your application.</p><p>Sanitize inputs by escaping HTML (<code>markupsafe.escape()</code>), validating types (ensure integers are actually integers), checking ranges (age between 0-150), and enforcing string lengths. Use CSRF tokens for form submissions and rate-limiting to prevent abuse.</p>"
    },
    "css/css_basics": {
        1: "<p>CSS syntax follows a simple pattern: <code>selector { property: value; }</code>. The selector targets HTML elements, the property is what you want to change (color, font-size, margin), and the value sets the new style.</p><p>Selectors range from simple (<code>h1</code>, <code>.class</code>, <code>#id</code>) to complex (<code>div > p</code>, <code>a:hover</code>, <code>[type='text']</code>). Properties can be shorthand: <code>margin: 10px 20px;</code> sets top/bottom and left/right. The cascade determines which rule wins when conflicts occur: specificity > source order.</p>"
    },
    "dsa/dsa_bst": {
        1: "<p>BST deletion has three cases: <strong>Leaf node</strong> (no children) - simply remove it. <strong>One child</strong> - replace the node with its only child. <strong>Two children</strong> - find the inorder successor (smallest node in right subtree), copy its value to the node being deleted, then delete the successor.</p><p>The two-children case maintains BST ordering because the inorder successor is the smallest value larger than the deleted node. Alternatively, use the inorder predecessor (largest in left subtree). Deletion maintains O(log n) for balanced BSTs but degrades to O(n) for skewed trees.</p>"
    },
    "ai/ai_search": {
        1: "<p>UCS extends BFS to handle non-uniform step costs - it always expands the <strong>lowest-cost</strong> node first using a priority queue. While BFS finds the shallowest goal, UCS finds the <strong>cheapest path</strong>, making it optimal for weighted graphs.</p><p>UCS is equivalent to Dijkstra's algorithm when applied to graph search. Time complexity is O(b^(1+C*/e)) where C* is the optimal cost and e is the minimum step cost. UCS is complete and optimal when all step costs are positive. It's the foundation for understanding A* search, which adds a heuristic to guide exploration.</p>"
    }
}

applied = 0
for key, subs in last_fixes.items():
    lang, topic_id = key.split('/')
    content = d[lang]['content'][topic_id]
    for idx, new_content in subs.items():
        if idx < len(content['structured']['subtopics']):
            content['structured']['subtopics'][idx]['content'] = new_content
            applied += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(prefix + json.dumps(d, ensure_ascii=False) + ';\n')

print(f"Expanded final {applied} subtopics!")
