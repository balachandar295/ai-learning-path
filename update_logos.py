import os

templates_dir = 'core/templates'

OLD = 'height:40px; vertical-align:middle;'
NEW = 'height:48px; vertical-align:middle;'

updated = []
for fname in os.listdir(templates_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(templates_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content
    content = content.replace(OLD, NEW)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append(fname)

print(f"Updated logo size in {len(updated)} files")
