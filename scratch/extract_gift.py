import re
import json
import os

# Find the fandom file
fandom_file = None
for f in os.listdir('.'):
    if 'Fandom.html' in f:
        fandom_file = f
        break

if not fandom_file:
    print("Fandom file not found")
    exit(1)

with open(fandom_file, "r", encoding="utf-8") as f:
    content = f.read()

# Split by EGO sections
ego_sections = re.split(r'<h3><span[^>]*></span><span class="mw-headline"[^>]*>(.*?)</span>', content, flags=re.DOTALL)

gift_data = {}

for i in range(1, len(ego_sections), 2):
    header_raw = ego_sections[i]
    header_text = re.sub(r'<[^>]+>', '', header_raw).strip()
    body = ego_sections[i+1]
    
    gift_section_match = re.search(r'<u>ギフト：(.*?)</u>', body)
    if gift_section_match:
        gift_name = gift_section_match.group(1).strip()
        gift_body = body[body.find(gift_section_match.group(0)):]
        
        # Part (部位)
        part_match = re.search(r'装着部位は<b>(.*?)</b>', gift_body)
        part = part_match.group(1).strip() if part_match else "不明"
        
        # Stats (情報/効果)
        stats_match = re.search(r'<b>情報[：:]</b>(.*?)</p>', gift_body, re.DOTALL)
        stats = re.sub(r'<[^>]+>', '', stats_match.group(1)).strip() if stats_match else "なし"
        
        # Abnormality Name (from header)
        abno_name = header_text
        match = re.search(r'「([^」]+)」', header_text)
        if match:
            abno_name = match.group(1)
            
        gift_data[gift_name] = {
            "abno_name": abno_name,
            "gift_name": gift_name,
            "part": part,
            "stats": stats
        }

output_path = os.path.join("scratch", "gift_data.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(gift_data, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(gift_data)} Gifts to {output_path}")
