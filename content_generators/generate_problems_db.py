import json
import random

problem_prefixes = ["Two", "Longest", "Median of", "Reverse", "Valid", "Sort", "Find", "Max", "Min", "Next", "Combination", "Remove", "Construct", "Search", "Insert", "Delete"]
problem_nouns = ["Sum", "Substring", "Palindromic Substring", "Arrays", "Integer", "Parentheses", "List", "Tree", "Graph", "Permutations", "Subarray", "Matrix", "Path", "Sequence"]

problems = []

# Hardcoded first few famous ones
preset = [
    {"title": "Two Sum", "difficulty": "Easy", "acceptance": "50.1%"},
    {"title": "Add Two Numbers", "difficulty": "Medium", "acceptance": "41.0%"},
    {"title": "Longest Substring Without Repeating Characters", "difficulty": "Medium", "acceptance": "34.2%"},
    {"title": "Median of Two Sorted Arrays", "difficulty": "Hard", "acceptance": "38.0%"},
    {"title": "Longest Palindromic Substring", "difficulty": "Medium", "acceptance": "33.0%"},
    {"title": "Zigzag Conversion", "difficulty": "Medium", "acceptance": "45.0%"},
    {"title": "Reverse Integer", "difficulty": "Medium", "acceptance": "28.0%"},
    {"title": "String to Integer (atoi)", "difficulty": "Medium", "acceptance": "17.0%"},
    {"title": "Palindrome Number", "difficulty": "Easy", "acceptance": "55.0%"},
    {"title": "Regular Expression Matching", "difficulty": "Hard", "acceptance": "28.5%"},
]

preset_titles = set([p["title"] for p in preset])

def generate_description(title, difficulty):
    desc = f"<p>You are tasked with solving a fundamental algorithmic challenge related to <strong>{title}</strong>. "
    
    # Adding backstory
    if "List" in title or "Node" in title:
        desc += "Imagine you are developing a low-level memory allocation system where memory blocks are represented as a linked list. You are given the head of a singly linked list. Your objective is to traverse or manipulate this list efficiently without allocating additional nodes arbitrarily."
        constraints = "<ul><li>The number of nodes in the list is in the range <code>[0, 10^4]</code>.</li><li><code>-10^5 <= Node.val <= 10^5</code></li><li>You must solve it in <code>O(1)</code> auxiliary space.</li></ul>"
    elif "Array" in title or "Matrix" in title or "Sum" in title:
        desc += "Consider a scenario involving high-frequency trading where data streams are batched into arrays. Given a zero-indexed array of integers, you must compute the requested combination or subarray that satisfies the target metric."
        constraints = "<ul><li><code>1 <= nums.length <= 10^5</code></li><li><code>-10^9 <= nums[i] <= 10^9</code></li><li><code>-10^9 <= target <= 10^9</code></li></ul>"
    elif "Tree" in title or "Graph" in title or "Path" in title:
        desc += "Assume you are constructing an efficient routing protocol for an internet-of-things (IoT) network representing a binary tree or directed acyclic graph. Given the root node, write an algorithm that explores the topology to return the requested sub-structure or optimal traversal path."
        constraints = "<ul><li>The number of nodes in the tree is in the range <code>[1, 10^4]</code>.</li><li><code>-1000 <= Node.val <= 1000</code></li><li>The maximum depth of the tree will not exceed <code>1000</code>.</li></ul>"
    elif "String" in title or "Substring" in title or "Palindrome" in title:
        desc += "You are building a text-processing engine for a gene-sequencing application. Given a string <code>s</code> consisting of English letters, digits, and symbols, write a routine that extracts or verifies the desired lexicographical property."
        constraints = "<ul><li><code>1 <= s.length <= 5 * 10^4</code></li><li><code>s</code> consists of printable ASCII characters.</li></ul>"
    else:
        desc += "This is a classical computational problem often encountered in systems design and competitive programming. Adhere strictly to the problem rules and boundary conditions to formulate an optimal algorithm yielding the expected output."
        constraints = "<ul><li><code>0 <= n <= 10^4</code></li><li>Results must fit within a 32-bit signed integer.</li></ul>"
        
    desc += "</p>"
    
    # Time complexity demands based on difficulty
    if difficulty == "Easy":
        desc += "<p><strong>Follow-up:</strong> While an <code>O(n^2)</code> approach is acceptable, can you come up with an algorithm that runs in less than <code>O(n^2)</code> time complexity?</p>"
    elif difficulty == "Medium":
        desc += "<p><strong>Requirement:</strong> You must write an algorithm that runs in <code>O(n log n)</code> or better time complexity and uses at most <code>O(n)</code> extra space.</p>"
    else:
        desc += "<p><strong>Requirement:</strong> You must design an algorithm that runs in strictly <code>O(log (m+n))</code> or <code>O(n)</code> time complexity and uses <code>O(1)</code> extra space to pass the strictest test limits.</p>"

    desc += f"<div style='margin-top: 15px;'><strong>Constraints:</strong><br>{constraints}</div>"
    
    # Mocking better examples
    examples = [
        {"input": "nums = [2,7,11,15], target = 9", "output": "[0,1]", "explanation": "Because nums[0] + nums[1] == 9, we return [0, 1]."},
        {"input": "nums = [3,2,4], target = 6", "output": "[1,2]", "explanation": "Looking at the array, nums[1] + nums[2] equals 6."},
        {"input": "nums = [3,3], target = 6", "output": "[0,1]", "explanation": "The constraints guarantee one unique valid answer exists."}
    ]
    return desc, examples

for i in range(300):
    if i < len(preset):
        prob = preset[i].copy()
    else:
        while True:
            title = f"{random.choice(problem_prefixes)} {random.choice(problem_nouns)}"
            if random.random() > 0.6:
                title += f" in {random.choice(problem_nouns)}"
            if title not in preset_titles:
                preset_titles.add(title)
                break
        
        diff_rand = random.random()
        if diff_rand < 0.25:
            diff = "Easy"
            acc = round(random.uniform(45.0, 75.0), 1)
        elif diff_rand < 0.75:
            diff = "Medium"
            acc = round(random.uniform(25.0, 55.0), 1)
        else:
            diff = "Hard"
            acc = round(random.uniform(10.0, 35.0), 1)
            
        prob = {
            "title": title,
            "difficulty": diff,
            "acceptance": f"{acc}%"
        }
    
    prob["id"] = i + 1
    prob["status"] = "solved" if random.random() < 0.2 else "todo"
    
    desc, examples = generate_description(prob["title"], prob["difficulty"])
    prob["description"] = desc
    prob["examples"] = examples
    
    problems.append(prob)

js_content = "const codingProblems = " + json.dumps(problems, indent=2) + ";\n"

with open(r"core\static\coding_problems_data.js", "w", encoding='utf-8') as f:
    f.write(js_content)

print(f"Generated {len(problems)} exactly to core/static/coding_problems_data.js with deep descriptions!")
