import re
import glob

# 1. Update colors to English in ALL HTML files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace contents of color spans
    content = re.sub(r'(class="attr-text-red"[^>]*>)赤(</)', r'\1Red\2', content)
    content = re.sub(r'(class="attr-text-white"[^>]*>)白(</)', r'\1White\2', content)
    content = re.sub(r'(class="attr-text-black"[^>]*>)黒(</)', r'\1Black\2', content)
    content = re.sub(r'(class="attr-text-pale"[^>]*>)青\(PALE\)(</)', r'\1Pale\2', content)
    content = re.sub(r'(class="attr-text-pale"[^>]*>)青(</)', r'\1Pale\2', content)
    content = re.sub(r'(class="attr-text-pale"[^>]*>)ペイル(</)', r'\1Pale\2', content)
    
    # Also replace some standalone instances if they are strictly "赤" inside a td
    content = re.sub(r'>赤<', '>Red<', content)
    content = re.sub(r'>白<', '>White<', content)
    content = re.sub(r'>黒<', '>Black<', content)
    content = re.sub(r'>青\(PALE\)<', '>Pale<', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Modify ego_list.html table structure
# Add "危険度" column header
with open('ego_list.html', 'r', encoding='utf-8') as f:
    ego = f.read()

# Fix headers
ego = ego.replace('<th>E.G.O名</th>\n                            <th>武器の特徴</th>', '<th>E.G.O名</th>\n                            <th>危険度</th>\n                            <th>武器の特徴</th>')

# Process rows to move tags to a new column
def process_ego_row(match):
    row = match.group(0)
    td_pattern = re.compile(r'(<td[^>]*>)(.*?)(</td>)', re.DOTALL)
    td_matches = list(td_pattern.finditer(row))
    if len(td_matches) < 2:
        return row
    
    # Check if there is a tag in the EGO name, weapon, or armor
    # We will extract ALL tags, determine the overall class, or format them for the new column
    tags_in_row = re.findall(r'<span class="attr-tag[^>]*>.*?</span>', row)
    
    # Remove tags from the row
    clean_row = re.sub(r'<span class="attr-tag[^>]*>.*?</span>', '', row)
    clean_tds = list(td_pattern.finditer(clean_row))
    
    if len(clean_tds) >= 2:
        # Construct the new cell content
        new_cell_content = ' '.join(tags_in_row)
        
        # Insert the new cell after EGO name (td_matches[1])
        # Rebuild the row
        parts = []
        # Up to the end of td 1
        end_td1 = clean_tds[1].end()
        parts.append(clean_row[:end_td1])
        
        # New td
        parts.append(f'<td>{new_cell_content}</td>')
        
        # The rest of the row
        parts.append(clean_row[end_td1:])
        return "".join(parts)
    
    return row

# Apply row transformation
ego_new = re.sub(r'<tr[^>]*>.*?</tr>', process_ego_row, ego, flags=re.DOTALL)

with open('ego_list.html', 'w', encoding='utf-8') as f:
    f.write(ego_new)

print("Done")
