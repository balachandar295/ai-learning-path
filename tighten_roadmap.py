import json

file_path = r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\tracks_data.js'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# We need to parse tracksData as JS object, but it's assigned to a variable.
json_start = text.find('{')
json_end = text.rfind('}') + 1

if json_start != -1 and json_end != -1:
    try:
        data = json.loads(text[json_start:json_end])
        
        # Apply tightening to all tracks
        for track_key, track_data in data.items():
            if 'nodes' in track_data:
                y_coord = 150
                for i, node in enumerate(track_data['nodes']):
                    # Left side vs Right side zigzag
                    node['x'] = 1250 if i % 2 == 0 else 1530
                    node['y'] = y_coord
                    y_coord += 160 # Tighter vertical spacing
                    
        # Write back
        new_text = "const tracksData = " + json.dumps(data, indent=4) + ";\n"
        base_path = r'c:\Users\ELCOT\Desktop\final_yr_project - Copy\core\static\tracks_data.js'
        with open(base_path, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Successfully tightened all roadmaps!")
        
    except Exception as e:
        print("JSON Error:", e)
else:
    print("Could not find JSON payload")
