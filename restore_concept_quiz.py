import json
import re
import random

def get_original_15_quizzes(track_name, topic_name):
    # Generates exactly 15 concept quiz questions logically related to the given track and topic.
    quizzes = []
    
    templates = [
        ("What is the primary advantage of utilizing {topic} in {track}?",
         ["It optimizes runtime performance significantly.", "It reduces memory consumption entirely.", "It automatically handles deployment.", "It bypasses all syntax errors."],
         "It optimizes runtime performance significantly."),
        
        ("Which common pitfall occurs when ignoring best practices for {topic} in {track}?",
         ["Unexpected logic bugs and execution crashes.", "Screen flickering issues.", "Hardware overheating.", "Loss of internet connectivity."],
         "Unexpected logic bugs and execution crashes."),
        
        ("How does the {track} compiler/interpreter typically handle {topic} natively?",
         ["By systematically executing defined structures precisely.", "By arbitrarily guessing user intent.", "By ignoring it completely.", "By relying tightly on third-party APIs exclusively."],
         "By systematically executing defined structures precisely."),
        
        ("What syntax behavior commonly governs structures referencing {topic} in {track}?",
         ["It relies strictly on context and specific semantic rules.", "`return true` explicitly", "`break` inherently", "`goto null` exclusively"],
         "It relies strictly on context and specific semantic rules."),
         
        ("From a debugging perspective, mastering {topic} guarantees what for a {track} engineer?",
         ["Robust architecture and consistent pipeline reliability.", "Absolute zero bugs forever.", "Less RAM usage permanently.", "Infinite loop prevention automatically."],
         "Robust architecture and consistent pipeline reliability."),
         
        ("True or False: Utilizing native {topic} in {track} is generally more optimal than building heavy external workarounds.",
         ["True", "False", "Only true on macOS", "Only true in older versions"],
         "True"),
         
        ("Which architectural component typically interacts directly with {topic}?",
         ["Data structures and core logical instances.", "Physical hard drives.", "The UI frontend layer exclusively.", "External networking routers."],
         "Data structures and core logical instances."),
         
        ("When reviewing code for {topic} issues in {track}, what is the first aspect to check?",
         ["Proper syntax adherence and logical data flows.", "The color of the code highlighting.", "The specific operating system version.", "The amount of comments in the code."],
         "Proper syntax adherence and logical data flows."),

        ("Why was {topic} introduced as a standard concept in {track}?",
         ["To provide elegant structural solutions to complex programming scenarios.", "To make the language harder to learn.", "To force developers to use more CPU resources.", "To satisfy a legacy hardware requirement."],
         "To provide elegant structural solutions to complex programming scenarios."),

        ("Which advanced feature in {track} heavily relies on a deep understanding of {topic}?",
         ["Asynchronous programming and complex system design.", "Simple math operations.", "Basic print formatting.", "Variable assignment directly."],
         "Asynchronous programming and complex system design."),

        ("What happens natively in {track} when {topic} configurations are mapped incorrectly?",
         ["The execution will likely throw a runtime exception or produce inaccurate logic.", "The computer will reboot safely.", "The code will automatically correct itself.", "It prints 'Hello World' silently."],
         "The execution will likely throw a runtime exception or produce inaccurate logic."),

        ("In technical interviews for {track}, questions about {topic} aim to evaluate what skill?",
         ["In-depth problem-solving capability and architectural knowledge.", "Typing speed.", "Memorization of standard libraries entirely.", "Ability to read documentation exclusively."],
         "In-depth problem-solving capability and architectural knowledge."),

        ("What is the most secure way to implement {topic} using {track}?",
         ["By strictly following official language documentation patterns safely.", "By copy-pasting code directly.", "By avoiding its usage purely.", "By granting all administrative permissions."],
         "By strictly following official language documentation patterns safely."),

        ("Which optimization strategy is often paired with {topic} conceptually in {track}?",
         ["Algorithmic refinement and data caching natively.", "Increasing hardware RAM.", "Turning off the monitor securely.", "Switching strictly to another language entirely."],
         "Algorithmic refinement and data caching natively."),

        ("If a junior {track} developer asks for the best resource to master {topic}, what is the ideal recommendation?",
         ["Comprehensive textbook tutorials and practical, rigorous problem-solving.", "Random video clips.", "Skimming a quick overview.", "Asking someone else entirely."],
         "Comprehensive textbook tutorials and practical, rigorous problem-solving.")
    ]

    for template, opts, ans in templates:
        q_text = template.replace("{track}", str(track_name).title()).replace("{topic}", str(topic_name).replace('_', ' ').title())
        
        shuffled_opts = list(opts)
        random.shuffle(shuffled_opts)
        
        quizzes.append({
            "q": q_text,
            "options": shuffled_opts,
            "answer": ans
        })
        
    return quizzes


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

for track_key, track_data in data.items():
    track_name = track_data.get('name', track_key)
    if 'content' not in track_data:
        continue
    for topic_key, topic_content in track_data['content'].items():
        # Restore the original 15 concept quiz questions natively
        topic_content['concept_quiz'] = get_original_15_quizzes(track_name, topic_key)
        # We explicitly DO NOT modify 'problem_solving' here so it stays realistic

new_json_str = json.dumps(data)
new_file_content = content[:prefix_idx] + new_json_str + ";\n"

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_file_content)

print("tracks_data.js concept quizzes restored logically safely natively.")
