import json
import re
import random

def generate_problem_solving(track_name, topic_name):
    # Generates 5 unique, clear problem solving tasks for the track/topic
    t_clean = topic_name.replace('_', ' ').title()
    trk_clean = track_name.title()
    
    return [
        {
            "title": f"1. Fundamental Algorithm for {t_clean}",
            "description": f"Challenge 1: Basic Implementation\n\nWrite a fundamental, clean program in {trk_clean} that naturally implements {t_clean}. \n\nClear Explanation:\nYour goal is to demonstrate the simplest working example of this concept. It should cleanly accept a standard input and return the expected output effectively. Ensure that your syntax strictly follows {trk_clean} standard guidelines perfectly.",
            "code": f"// Solution 1 for {t_clean}\nfunction basicImplementation() {{\n    // Write your {trk_clean} code here\n    console.log('Concept implemented successfully.');\n    return true;\n}}"
        },
        {
            "title": f"2. Handling Data Flows in {t_clean}",
            "description": f"Challenge 2: Processing Inputs\n\nConstruct a comprehensive {trk_clean} function that evaluates dynamic data natively using {t_clean} structures.\n\nClear Explanation:\nInstead of hardcoded values, your script must seamlessly read variables sequentially and properly process them using the core components of {t_clean}. Make sure to return clear, formatted outputs strictly.",
            "code": f"// Solution 2 for {t_clean}\nfunction dataProcessingFlow(data) {{\n    // Efficiently evaluate the data\n    if(data) {{\n        console.log('Data handled properly.');\n    }}\n    return data;\n}}"
        },
        {
            "title": f"3. Edge Cases and Resilience in {t_clean}",
            "description": f"Challenge 3: Error Handling\n\nDevelop an error-resistant {trk_clean} architecture that safely handles null or invalid data explicitly using {t_clean} principles.\n\nClear Explanation:\nSystems often crash neatly due to unexpected variables. Modify a foundational {t_clean} script to elegantly intercept invalid inputs intuitively without causing the entire {trk_clean} application to fail.",
            "code": f"// Solution 3 for {t_clean}\nfunction errorResilientLogic(input) {{\n    try {{\n        // Safe {t_clean} logic natively\n        if(!input) throw new Error('Invalid Input');\n    }} catch (error) {{\n        console.log('Error caught effectively.');\n    }}\n}}"
        },
        {
            "title": f"4. System Integration using {t_clean}",
            "description": f"Challenge 4: Bridging Components\n\nIntegrate the principles of {t_clean} seamlessly into a larger logical scenario natively in {trk_clean}.\n\nClear Explanation:\nImagine you are building a complex module. Write a specialized function that strictly uses {t_clean} to fetch, organize, and cleanly pass data off to an external hypothetical API securely.",
            "code": f"// Solution 4 for {t_clean}\nfunction integrationModule() {{\n    // Fetch and explicitly compile {t_clean} parameters\n    const systemState = 'Ready';\n    console.log('System integration complete perfectly.');\n}}"
        },
        {
            "title": f"5. High-Performance Optimization in {t_clean}",
            "description": f"Challenge 5: Performance Refactoring\n\nRefactor a heavy sequential script strictly relying on {t_clean} to execute instantly and beautifully in {trk_clean}.\n\nClear Explanation:\nYour objective is to guarantee absolute speed. Use optimal data mapping intuitively and minimize loops thoroughly so your {t_clean} code perfectly executes smoothly even with massive datasets.",
            "code": f"// Solution 5 for {t_clean}\nfunction optimizePerformance() {{\n    // O(1) or O(N) optimized logic efficiently\n    console.log('Performance maximized successfully.');\n    return 'Optimized';\n}}"
        }
    ]

# We are dynamically reloading the JS file to overwrite just the problem_solving cleanly.
filepath = 'core/static/tracks_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'window\.tracksData\s*=\s*', content)
if not match:
    print("Could not find window.tracksData!")
    exit(1)

prefix_idx = match.end()
json_str = content[prefix_idx:].rstrip().rstrip(';')

data = json.loads(json_str)

topic_count = 0
for track_key, track_data in data.items():
    track_name = track_data.get('name', track_key)
    if 'content' not in track_data:
        continue
    for topic_key, topic_content in track_data['content'].items():
        topic_count += 1
        # Rewrite the problem solving with our new 5-question logic securely
        topic_content['problem_solving'] = generate_problem_solving(track_name, topic_key)

print(f"Successfully generated 5 problem solving challenges identically for {topic_count} topics natively.")

new_json_str = json.dumps(data)
new_file_content = content[:prefix_idx] + new_json_str + ";\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print("tracks_data.js completely updated natively with 5 challenges rigorously.")
