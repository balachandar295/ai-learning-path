import os

base_dir = r"c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\templates"
# Include these standalone pages
targets = ['arithmetic_topics.html', 'aptitude_categories.html', 'topic_detail.html', 'progress.html']

for target in targets:
    path = os.path.join(base_dir, target)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Don't add twice
        if 'ai_bot.html' not in content:
            new_content = content.replace('</body>', "{% include 'ai_bot.html' %}\n</body>")
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added ai_bot to {target}")

print("Done injecting bot!")
