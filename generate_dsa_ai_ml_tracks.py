import json
import os

file_path = r'core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()
json_start = text.find('{')
json_end = text.rfind('}')
data = json.loads(text[json_start:json_end+1])

# Remove perl
if 'perl' in data:
    del data['perl']

def generic_explanation(title, subject):
    return f"""<div style='line-height:1.8;'>
    <h3 style='color:#0f172a;font-size:1.9rem;border-bottom:3px solid #0ea5e9;padding-bottom:12px;margin-bottom:24px;'>{title}</h3>
    <h4 style='color:#0ea5e9;font-size:1.3rem;margin-top:30px;margin-bottom:10px;border-left:4px solid #0ea5e9;padding-left:12px;'>Overview</h4>
    <p style='color:#475569;font-size:1.05rem;line-height:1.8;margin-bottom:16px;'>In this module, you will learn the fundamental concepts of {title} in {subject}. This knowledge forms the building block for advanced applications and interview questions.</p>
    
    <div style='background:#1e1e2f;border-radius:12px;margin-bottom:20px;overflow:hidden;border:1px solid #334155;'>
        <div style='background:linear-gradient(to right,#0ea5e9,#3b82f6);padding:8px 16px;color:white;font-size:0.85rem;font-weight:700;font-family:monospace;'>Core Concept</div>
        <pre style='margin:0;padding:16px 20px;color:#e2e8f0;font-family:monospace;font-size:0.95rem;overflow-x:auto;white-space:pre;'>// Example pseudocode or conceptual representation for {title}
function explore{title.replace(' ', '')}() {{
    console.log("Mastering {title}!");
}}</pre>
    </div>
</div>"""

def create_track(track_id, track_title, track_desc, topics, phases):
    nodes = []
    content = {}
    
    for i, (topic_id, topic_title) in enumerate(topics):
        phase = phases[i]
        
        # Node structure
        node = {
            "id": f"{track_id}_{topic_id}",
            "title": topic_title,
            "x": 1250 if i % 2 == 0 else 1530,
            "y": 150 + i * 160,
            "status": "available" if i == 0 else "locked",
            "phase": phase
        }
        if i > 0:
            node["parent"] = f"{track_id}_{topics[i-1][0]}"
        nodes.append(node)
        
        # Content structure
        content[node["id"]] = {
            "title": topic_title,
            "explanation": generic_explanation(topic_title, track_title),
            "examples": [],
            "concept_quiz": [
                {"q": f"What is the main goal of {topic_title}?", "options": ["Optimization", "Storage", "Rendering", "Networking"], "answer": "Optimization"},
                {"q": f"Which of the following implies a good understanding of {topic_title}?", "options": ["Efficiency", "More memory", "Slower execution", "Syntax errors"], "answer": "Efficiency"},
                {"q": f"Is {topic_title} used in industry applications?", "options": ["Yes, widely used", "No, it is theoretical", "Only in legacy systems", "Never"], "answer": "Yes, widely used"},
                {"q": f"When comparing algorithms in {topic_title}, what do we measure?", "options": ["Time and Space", "Lines of code", "Color depth", "Screen size"], "answer": "Time and Space"},
                {"q": f"A key benefit of mastering {topic_title} is:", "options": ["Better system design", "Less typing", "Automatic compilation", "No bugs ever"], "answer": "Better system design"}
            ],
            "hands_on": {
                "title": f"Practice {topic_title}",
                "description": f"Implement a basic concept related to {topic_title}.",
                "hint": "Think about time complexity.",
                "code": f"// Start coding for {topic_title}\n"
            },
            "problem_solving": [
                {"title": f"Basic {topic_title} Problem", "description": "Solve a fundamental scenario.", "code": "// Solution"},
                {"title": f"Intermediate {topic_title} Task", "description": "Apply standard techniques.", "code": "// Solution"},
                {"title": f"Advanced {topic_title} Challenge", "description": "Optimize for performance.", "code": "// Solution"}
            ]
        }
        
    return {
        "title": track_title,
        "description": track_desc,
        "nodes": nodes,
        "content": content
    }

# DSA Topics (18)
dsa_topics = [
    ("intro", "Introduction to DSA"), ("arrays", "Arrays & Matrices"), ("ll", "Linked Lists"), 
    ("stacks", "Stacks"), ("queues", "Queues"), ("trees", "Binary Trees"), 
    ("bst", "Binary Search Trees"), ("graphs", "Graphs Intro"), ("searching", "Searching Algos"), 
    ("sorting", "Sorting Algos"), ("hashing", "Hashing / Maps"), ("heaps", "Heaps / Priority Q"), 
    ("trie", "Trie Data Structure"), ("dp", "Dynamic Programming"), ("greedy", "Greedy Algorithms"), 
    ("backtracking", "Backtracking"), ("advanced", "Advanced Graphs"), ("interview", "DSA Interview Guide")
]
dsa_phases = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]

# AI Topics (18)
ai_topics = [
    ("intro", "Intro to AI"), ("search", "Search Algorithms"), ("heuristic", "Heuristic Search"), 
    ("csp", "Constraint Satisfaction"), ("game", "Game Theory"), ("logic", "Logic & Reasoning"), 
    ("knowledge", "Knowledge Rep"), ("uncertainty", "Uncertainty / Prob"), ("ml", "ML Basics"), 
    ("nn", "Neural Networks"), ("dl", "Deep Learning Intro"), ("vi", "Computer Vision Intro"), 
    ("nlp", "NLP Basics"), ("rl", "Reinforcement Learning"), ("expert", "Expert Systems"), 
    ("robotics", "Robotics Basics"), ("ethics", "AI Ethics"), ("interview", "AI Interview Guide")
]
ai_phases = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]

# ML Topics (18)
ml_topics = [
    ("intro", "Intro to ML"), ("data", "Data Preprocessing"), ("eda", "Exploratory Data Analysis"), 
    ("supervised", "Supervised Learning"), ("linear", "Linear Regression"), ("logistic", "Logistic Regression"), 
    ("svm", "Support Vector Machines"), ("trees", "Decision Trees"), ("forests", "Random Forests"), 
    ("unsupervised", "Unsupervised Learning"), ("clustering", "K-Means Clustering"), ("pca", "Dimensionality Reduction"), 
    ("eval", "Model Evaluation"), ("ensemble", "Ensemble Methods"), ("dnn", "Deep Neural Networks"), 
    ("deployment", "Model Deployment"), ("mlops", "MLOps Basics"), ("interview", "ML Interview Guide")
]
ml_phases = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5]

# Generate and add the tracks
data['dsa'] = create_track('dsa', 'Data Structures & Algorithms', 'Master DSA for competitive programming and tech interviews.', dsa_topics, dsa_phases)
data['ai'] = create_track('ai', 'Artificial Intelligence', 'Explore AI concepts, searching algorithms, and deep learning.', ai_topics, ai_phases)
data['ml'] = create_track('ml', 'Machine Learning', 'Dive into predictive modeling, supervised and unsupervised learning.', ml_topics, ml_phases)

new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("DSA, AI, and ML tracks generated and injected successfully. Perl removed.")
