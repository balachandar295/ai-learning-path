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

html_topics = [
    ("html_basics", "HTML Basics", "Introduction to HTML structure elements like <html>, <head>, and <body>.", "<!DOCTYPE html>\n<html>\n<head>\n    <title>My Page</title>\n</head>\n<body>\n    <h1>Welcome</h1>\n</body>\n</html>"),
    ("html_text", "Text Formatting", "Tags like <p>, <h1>-<h6>, <strong>, <em> to structure and format text.", "<h1>Heading</h1>\n<p>This is a <strong>bold</strong> and <em>italic</em> text.</p>"),
    ("html_links", "Links & Nav", "Using the completely basic <a> tag for creating hyperlinks to other pages or sections.", "<a href='https://example.com' target='_blank'>Visit Example</a>\n<a href='#section1'>Jump to Section 1</a>"),
    ("html_images", "Images", "Embedding images with the <img> tag and understanding attributes like src and alt.", "<img src='logo.png' alt='Company Logo' width='200' height='100'>"),
    ("html_lists", "Lists", "Creating ordered <ol>, unordered <ul>, and definition <dl> lists.", "<ul>\n    <li>Item 1</li>\n    <li>Item 2</li>\n</ul>\n<ol>\n    <li>First</li>\n    <li>Second</li>\n</ol>"),
    ("html_tables", "Tables", "Structuring data using <table>, <tr>, <th>, and <td>.", "<table border='1'>\n  <tr>\n    <th>Name</th><th>Age</th>\n  </tr>\n  <tr>\n    <td>Alice</td><td>25</td>\n  </tr>\n</table>"),
    ("html_forms", "Forms & Inputs", "Collecting user input using <form>, <input>, <button>, and <select>.", "<form action='/submit' method='POST'>\n  <input type='text' name='username' placeholder='Name'>\n  <button type='submit'>Submit</button>\n</form>"),
    ("html_semantic", "Semantic HTML", "Using meaning-driven tags like <header>, <article>, <section>, <aside>, and <footer>.", "<header>\n  <nav>\n    <a href='/'>Home</a>\n  </nav>\n</header>\n<main>\n  <article>Content...</article>\n</main>\n<footer>\n  &copy; 2026\n</footer>"),
    ("html_media", "Audio & Video", "Embedding multimedia using HTML5 <audio> and <video> elements.", "<video controls width='400'>\n  <source src='movie.mp4' type='video/mp4'>\n  Your browser does not support the video tag.\n</video>"),
    ("html_meta", "Attributes & Meta", "Using the <meta> tag for page description, keywords, author, and viewport setting.", "<head>\n  <meta charset='UTF-8'>\n  <meta name='description' content='Learning HTML'>\n  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n</head>"),
    ("html_iframe", "iFrames", "Displaying a web page within a web page using <iframe>.", "<iframe src='https://www.example.com' width='500' height='300' title='Example Website'></iframe>"),
    ("html_canvas", "Canvas & SVG", "Drawing graphics via scripting with <canvas> and inline scalable vector graphics <svg>.", "<svg width='100' height='100'>\n  <circle cx='50' cy='50' r='40' stroke='black' stroke-width='3' fill='red' />\n</svg>"),
    ("html_api", "HTML5 APIs", "Using advanced completely standard APIs like Drag and Drop, Web Storage, and Web Workers.", "<script>\n // Using Local Storage\n localStorage.setItem('user', 'Alice');\n document.write(localStorage.getItem('user'));\n</script>"),
    ("html_a11y", "Accessibility", "Making web content accessible using ARIA roles and labels.", "<button aria-label='Close Dialog'>X</button>\n<img src='chart.png' alt='Sales chart showing a 20% increase'>"),
    ("html_seo", "SEO Basics", "Structuring HTML properly for Search Engine Optimization, like heading hierarchy.", "<h1>Main Page Title</h1>\n<h2>Subheading</h2>\n<p>Optimized content here with descriptive alt text for images.</p>"),
    ("html_responsive", "Viewport", "Designing for mobile devices using responsive meta tags and proper widths.", "<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<style>\n  img { max-width: 100%; height: auto; }\n</style>"),
    ("html_practices", "Best Practices", "Using external CSS/JS files, lowercase labels, closing tags, and valid HTML structure.", "<!-- Best Practice: External link -->\n<link rel='stylesheet' href='styles.css'>\n<script src='script.js' defer></script>"),
]

for nid, title, desc, code in html_topics:
    data['html']['content'][nid] = {
        "title": title,
        "explanation": explanation(title, [
            (f"Understanding {title}", desc, [(f"{title} Usage", code)])
        ]),
        "examples": [],
        "concept_quiz": quiz([(f"Which tag is primarily used for {title.lower()} in HTML?", ["The core tags", "<div>", "<span>", "Python function"], "The core tags")]),
        "hands_on": task(f"Implement {title}", f"Write the HTML markup that correctly implements {title}.", "Follow standard HTML specifications.", code),
        "problem_solving": problems([(f"{title} Scenario", f"Fix or create an HTML element showcasing {title}.", code)])
    }

# Interview Node
data['html']['content']['html_interview'] = {
    "title": "HTML Interview Guide",
    "explanation": explanation("HTML Interview Questions", [
        ("Common Questions", "Frequently asked HTML concepts in front-end interviews.", [
            ("What are semantic elements?", "Elements like <header>, <footer>, <article> that clearly describe their meaning to both the browser and the developer."),
            ("What is DOCTYPE?", "It is an instruction to the web browser about what version of HTML the page is written in (e.g., <!DOCTYPE html> for HTML5)."),
            ("What are HTML attributes?", "Additional piece of information applied to an element (like id, class, src, href).")
        ])
    ]),
    "examples": [], "concept_quiz": [], "hands_on": None, "problem_solving": []
}

new_text = "window.tracksData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n"
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_text)

print("HTML content updated fully!")
