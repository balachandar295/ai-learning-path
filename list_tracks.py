import json, re

try:
    with open(r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\tracks_data.js', 'r', encoding='utf-8') as f:
        text = f.read()

    # The file starts with 'window.tracksData = {'
    # Let's find top-level keys by matching the pattern:
    print("TRACKS DATA:")
    keys = re.findall(r'^  \"([a-zA-Z0-9_]+)\": \{', text, re.MULTILINE)
    print(keys)
    
except Exception as e:
    print("Error tracks_data:", e)

try:
    with open(r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\data.js', 'r', encoding='utf-8') as f:
        text2 = f.read()

    keys2 = re.findall(r'^    \"([a-zA-Z0-9_]+)\": \{', text2, re.MULTILINE)
    print("DATA JS KEYS:", keys2)
except Exception as e:
    print("Error data.js:", e)
