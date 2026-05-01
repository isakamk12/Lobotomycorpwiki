import re

with open('ego_list.html', 'r', encoding='utf-8') as f:
    html = f.read()

risk_levels = ['zayin', 'teth', 'he', 'waw', 'aleph']

for risk in risk_levels:
    section_pattern = re.compile(f'(<section id="{risk}">)(.*?)(</section>)', re.DOTALL)
    match = section_pattern.search(html)
    if not match: continue
    
    section_head, section_body, section_tail = match.groups()
    
    # Process rows in this section
    def process_row(row_match):
        row = row_match.group(0)
        tds = re.findall(r'<td[^>]*>(.*?)</td>', row, re.DOTALL)
        if len(tds) < 2: return row
        
        abno_name = re.sub(r'<[^>]+>', '', tds[0]).strip()
        weapon_text = re.sub(r'<[^>]+>', '', tds[2]) if len(tds) > 2 else ""
        armor_text = re.sub(r'<[^>]+>', '', tds[3]) if len(tds) > 3 else ""
        
        upgraded_class = None
        for r in ['ZAYIN', 'TETH', 'HE', 'WAW', 'ALEPH']:
            if f'※{r}格上げ' in weapon_text or f'※{r}格上げ' in armor_text or f'{r}防具' in armor_text:
                upgraded_class = r
                
        if abno_name in ['黒の兵隊', '審判鳥', '貪欲の王']: upgraded_class = 'ALEPH'
        if abno_name in ['死んだ蝶の葬儀', '魔弾の射手']: upgraded_class = 'WAW'
        if abno_name in ['壊れゆく甲冑', '壁に向かう女']: upgraded_class = 'HE'
        
        final_class = upgraded_class if upgraded_class else risk.upper()
        
        # Strip existing tags to prevent duplicates
        row = re.sub(r'<span class="attr-tag[^>]*>.*?</span>', '', row)
        
        # Re-extract tds because row might have changed
        td_pattern = re.compile(r'(<td[^>]*>)(.*?)(</td>)', re.DOTALL)
        td_matches = list(td_pattern.finditer(row))
        if len(td_matches) >= 2:
            is_half = 'bg-half' in row
            if is_half:
                # Add tags to weapon and armor
                w_tag = f'<span class="attr-tag tag-{upgraded_class.lower()}" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">{upgraded_class}</span>'
                a_tag = f'<span class="attr-tag tag-{risk}" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">{risk.upper()}</span>'
                
                new_row = row
                # td 2 (weapon)
                td2_inner = td_matches[2].group(2) + w_tag
                new_row = new_row.replace(td_matches[2].group(0), td_matches[2].group(1) + td2_inner + td_matches[2].group(3))
                
                # td 3 (armor)
                if len(td_matches) > 3:
                    td3_inner = td_matches[3].group(2) + a_tag
                    new_row = new_row.replace(td_matches[3].group(0), td_matches[3].group(1) + td3_inner + td_matches[3].group(3))
                return new_row
            else:
                # Add tag to EGO name
                tag_html = f'<span class="attr-tag tag-{final_class.lower()}" style="margin-left:8px;padding:2px 6px;font-size:0.75rem;">{final_class}</span>'
                td1_inner = td_matches[1].group(2) + tag_html
                new_row = row.replace(td_matches[1].group(0), td_matches[1].group(1) + td1_inner + td_matches[1].group(3))
                return new_row
        return row
        
    new_section_body = re.sub(r'<tr[^>]*>.*?</tr>', process_row, section_body, flags=re.DOTALL)
    html = html.replace(match.group(0), section_head + new_section_body + section_tail)

with open('ego_list.html', 'w', encoding='utf-8') as f:
    f.write(html)
