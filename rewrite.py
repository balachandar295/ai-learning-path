with open('core/templates/skill_tests_hub.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace("{% extends 'basic.html' %}", '')
text = text.replace('{% extends "basic.html" %}', '')
text = text.replace("{% block content %}", '')
text = text.replace("{% endblock %}", '')

with open('header_snippet.html', 'r', encoding='utf-8') as f:
    header = f.read()

head_meta = """
<style>
body { background-color: #f4f7fb; }
</style>
"""

foot = "\\n</body>\\n</html>"

final_text = header + head_meta + text + foot
with open('core/templates/skill_tests_hub.html', 'w', encoding='utf-8') as f:
    f.write(final_text)

with open('core/templates/comprehensive_test.html', 'r', encoding='utf-8') as f:
    ctext = f.read()
ctext = ctext.replace("{% extends 'basic.html' %}", '')
ctext = ctext.replace("{% block content %}", '')
ctext = ctext.replace("{% endblock %}", '')

final_ctext = header + head_meta + ctext + foot
with open('core/templates/comprehensive_test.html', 'w', encoding='utf-8') as f:
    f.write(final_ctext)

print("Success rewriting templates.")
