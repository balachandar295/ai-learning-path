import json, re

with open('core/static/tracks_data.js', 'r', encoding='utf-8') as f:
    raw = f.read()

match = re.search(r'window\.tracksData\s*=\s*', raw)
json_str = raw[match.end():].rstrip().rstrip(';')
data = json.loads(json_str)

# Show first track's topic keys
first_track = 'python'
topics = list(data[first_track]['content'].keys())
print(f"Python topics: {topics}")

# Show sample quiz
first_topic = topics[0]
sample = data[first_track]['content'][first_topic]
print(f"\nSample topic: {first_topic}")
print(f"Keys: {list(sample.keys())}")
cq = sample.get('concept_quiz', [])
print(f"\nconcept_quiz ({len(cq)} items):")
print(json.dumps(cq, indent=2)[:2000])
ho = sample.get('hands_on', {})
print(f"\nhands_on:")
print(json.dumps(ho, indent=2)[:500])
