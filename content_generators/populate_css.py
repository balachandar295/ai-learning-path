import json

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

css_topics = [
    ("css_basics", "CSS Basics", "Cascading Style Sheets dictate how HTML elements look across devices.", "body {\n  font-family: Arial, sans-serif;\n  background-color: #f4f4f9;\n}"),
    ("css_selectors", "Selectors", "Targeting HTML elements by tag, class, or ID.", "/* Tag selector */\np { color: blue; }\n/* Class selector */\n.btn { padding: 10px; }\n/* ID selector */\n#header { font-size: 24px; }"),
    ("css_colors", "Colors & Backgrounds", "Using hex, rgb, hsl colors, and applying backgrounds.", ".box {\n  background-color: #3b82f6;\n  color: white;\n  background-image: url('bg.png');\n}"),
    ("css_box", "Box Model", "Understanding padding, borders, margins, and content dimensions.", ".box {\n  width: 300px;\n  padding: 20px;\n  border: 1px solid gray;\n  margin: 10px auto;\n}"),
    ("css_text", "Typography", "Styling text sizes, fonts, weights, alignments, and spacings.", "h1 {\n  font-size: 2rem;\n  font-weight: 700;\n  text-align: center;\n  text-transform: uppercase;\n  letter-spacing: 2px;\n}"),
    ("css_float", "Position & Float", "Flowing text around elements using float, and positioning elements absolutely/relatively.", ".sidebar { float: left; width: 25%; }\n.modal { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); }"),
    ("css_flex", "Flexbox", "1-dimensional layouts made easy. Aligning items horizontally or vertically seamlessly.", ".container {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n}"),
    ("css_grid", "CSS Grid", "2-dimensional grid layouts with rows and columns for robust design.", ".grid {\n  display: grid;\n  grid-template-columns: repeat(3, 1fr);\n  gap: 20px;\n}"),
    ("css_responsive", "Media Queries", "Adapting designs to different screen widths.", "@media (max-width: 768px) {\n  .container {\n    flex-direction: column;\n  }\n}"),
    ("css_pseudo", "Pseudo-classes", "Styling specific states of an element, like hovering.", "a:hover { color: orange; }\ninput:focus { outline: 2px solid blue; }\nli:nth-child(even) { background: #eee; }"),
    ("css_shadows", "Shadows & Gradients", "Adding depth through text-shadows, box-shadows, and linear gradients.", ".card {\n  box-shadow: 0 4px 6px rgba(0,0,0,0.1);\n  background: linear-gradient(to right, #ff7e5f, #feb47b);\n}"),
    ("css_vars", "CSS Variables", "Reusable custom properties defined in the root.", ":root {\n  --primary: #3b82f6;\n}\n.btn {\n  background-color: var(--primary);\n}"),
    ("css_transitions", "Transitions", "Smoothly changing properties over a duration.", ".btn {\n  transition: all 0.3s ease-in-out;\n}\n.btn:hover {\n  transform: scale(1.05);\n}"),
    ("css_animations", "Animations", "Creating complex keyframe animations.", "@keyframes bounce {\n  0%, 100% { transform: translateY(0); }\n  50% { transform: translateY(-20px); }\n}\n.ball {\n  animation: bounce 1s infinite;\n}"),
    ("css_transforms", "Transforms", "Translating, rotating, scaling, and skewing elements.", ".rotate-box {\n  transform: rotate(45deg) scale(1.2);\n}"),
    ("css_zindex", "Z-Index", "Controlling the stacking order of overlapping elements.", ".overlay {\n  position: absolute;\n  z-index: 9999;\n}"),
    ("css_optimization", "Optimization", "Minifying CSS, grouping selectors, and avoiding overly complex nesting.", "/* Grouped selectors logic */\nh1, h2, h3 {\n  font-family: inherit;\n  margin-bottom: 0.5em;\n}"),
]

for nid, title, desc, code in css_topics:
    data['css']['content'][nid] = {
        "title": title,
        "explanation": explanation(title, [
            (f"Understanding {title}", desc, [(f"{title} Usage", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([(f"What property primarily enables {title.lower()}?", ["Specific CSS Property", "HTML Tag", "JS Script", "None of the above"], "Specific CSS Property")]),
        "hands_on": task(f"Implement {title}", f"Write the CSS rules correctly establishing {title}.", "Apply CSS correctly.", code),
        "problem_solving": problems([(f"{title} Problem", f"Adjust styles for an element applying {title}.", code)])
    }

data['css']['content']['css_interview'] = {
    "title": "CSS Interview Guide",
    "explanation": explanation("CSS Interview Questions", [
        ("Common Questions", "Frequently assessed CSS capabilities.", [
            ("What is the Box Model?", "CSS box model consists of margins, borders, padding, and the actual content."),
            ("Flexbox vs Grid?", "Flexbox is designed for 1D layouts (row or column). Grid is designed for 2D layouts (rows and columns)."),
            ("What is specificity?", "It's the algorithm used by browsers to determine the CSS declaration that is the most relevant and applied.")
        ])
    ]),
    "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
}

new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("CSS content updated fully!")
