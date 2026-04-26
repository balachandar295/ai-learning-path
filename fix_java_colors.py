"""Replace Java orange gradient with JS blue gradient in tracks_data.js"""

file_path = r'core\static\tracks_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the java section and replace only inside it
java_start = content.find('"java"')
python_start = content.find('"python"')
js_start = content.find('"javascript"')

# Java section is somewhere — replace orange gradient only inside java content
# Orange: linear-gradient(to right,#f89820,#e65c00)
# Blue:   linear-gradient(to right,#0ea5e9,#3b82f6)

# Also replace the section heading color for java
# Orange heading: color:#f89820
# Blue heading:   color:#0ea5e9

# Also replace the bottom border color
# border-bottom:3px solid #f89820  -> border-bottom:3px solid #0ea5e9
# border-left:4px solid #f89820   -> border-left:4px solid #0ea5e9

old_gradient = "linear-gradient(to right,#f89820,#e65c00)"
new_gradient = "linear-gradient(to right,#0ea5e9,#3b82f6)"

old_color_heading = "color:#f89820"
new_color_heading = "color:#0ea5e9"

old_border_bottom = "border-bottom:3px solid #f89820"
new_border_bottom = "border-bottom:3px solid #0ea5e9"

old_border_left = "border-left:4px solid #f89820"
new_border_left = "border-left:4px solid #0ea5e9"

count1 = content.count(old_gradient)
count2 = content.count(old_color_heading)
count3 = content.count(old_border_bottom)
count4 = content.count(old_border_left)

print(f"Found: gradient={count1}, heading={count2}, border-bottom={count3}, border-left={count4}")

content = content.replace(old_gradient, new_gradient)
content = content.replace(old_color_heading, new_color_heading)
content = content.replace(old_border_bottom, new_border_bottom)
content = content.replace(old_border_left, new_border_left)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Java now uses the same blue theme as JavaScript.")
