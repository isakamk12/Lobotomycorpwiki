import re
from bs4 import BeautifulSoup

with open('ego_list.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# We know the tables are inside <section id="zayin">, etc.
risk_levels = ['zayin', 'teth', 'he', 'waw', 'aleph']

for risk in risk_levels:
    section = soup.find('section', id=risk)
    if not section:
        continue
    
    tbody = section.find('tbody')
    if not tbody:
        continue
        
    for tr in tbody.find_all('tr'):
        # Column 1: Abno Name, Column 2: EGO Name, Column 3: Weapon, Column 4: Armor
        tds = tr.find_all('td')
        if len(tds) >= 2:
            ego_name_td = tds[1]
            weapon_td = tds[2]
            armor_td = tds[3] if len(tds) >= 4 else None
            
            # Determine the actual class of the EGO. Default is the section's risk.
            ego_class = risk.upper()
            weapon_text = weapon_td.get_text()
            armor_text = armor_td.get_text() if armor_td else ""
            
            # Check for upgrades in weapon or armor text
            # E.g. （※HE格上げ）
            if 'ALEPH格上げ' in weapon_text or 'ALEPH格上げ' in armor_text or 'ALEPH防具' in armor_text or 'ALEPH' in weapon_text or 'ALEPH' in armor_text:
                ego_class = 'ALEPH'
            elif 'WAW格上げ' in weapon_text or 'WAW格上げ' in armor_text or 'WAW' in weapon_text or 'WAW' in armor_text:
                ego_class = 'WAW'
            elif 'HE格上げ' in weapon_text or 'HE格上げ' in armor_text or 'HE' in weapon_text or 'HE' in armor_text:
                ego_class = 'HE'
            elif 'TETH格上げ' in weapon_text or 'TETH格上げ' in armor_text or 'TETH' in weapon_text or 'TETH' in armor_text:
                ego_class = 'TETH'
                
            # Wait, if we just blindly look for "ALEPH" it might catch things like "ALEPH級"
            # The explicit notes are "※〇〇格上げ"
            # Let's be more precise
            upgraded_class = None
            for r in ['ZAYIN', 'TETH', 'HE', 'WAW', 'ALEPH']:
                if f'※{r}格上げ' in weapon_text or f'※{r}格上げ' in armor_text or f'{r}防具' in armor_text:
                    upgraded_class = r
            
            # Pink, Justitia: ALEPH
            abno_name = tds[0].get_text().strip()
            if abno_name in ['黒の兵隊', '審判鳥', '貪欲の王']:
                upgraded_class = 'ALEPH'
            if abno_name in ['死んだ蝶の葬儀', '魔弾の射手']:
                upgraded_class = 'WAW'
            if abno_name in ['壊れゆく甲冑', '壁に向かう女']:
                upgraded_class = 'HE'
            
            # We will append the tag to the EGO Name column.
            # But wait, earlier I appended it to the weapon column!
            # Let's remove any existing tags first to avoid duplicates.
            for span in weapon_td.find_all('span', class_='attr-tag'):
                span.decompose()
            for span in ego_name_td.find_all('span', class_='attr-tag'):
                span.decompose()
                
            final_class = upgraded_class if upgraded_class else risk.upper()
            
            # We want to add it to E.G.O名 (tds[1])
            # Or maybe to both EGO Name? The user said "EGOは抽出元と武器のクラス違う...タグ付けたのに"
            tag_html = soup.new_tag('span', attrs={'class': f'attr-tag tag-{final_class.lower()}', 'style': 'margin-left:8px; padding:2px 6px; font-size:0.75rem;'})
            tag_html.string = final_class
            
            ego_name_td.append(tag_html)
            
            # If weapon and armor have DIFFERENT classes (half-and-half), 
            # maybe we should tag weapon and armor separately!
            # E.g. Gold Rush (Weapon ALEPH, Armor WAW)
            if 'bg-half' in tr.get('class', []):
                weapon_class = upgraded_class
                armor_class = risk.upper()
                
                # Weapon tag
                w_tag = soup.new_tag('span', attrs={'class': f'attr-tag tag-{weapon_class.lower()}', 'style': 'margin-left:5px; padding:2px 4px; font-size:0.7rem;'})
                w_tag.string = weapon_class
                weapon_td.append(w_tag)
                
                # Armor tag
                if armor_td:
                    a_tag = soup.new_tag('span', attrs={'class': f'attr-tag tag-{armor_class.lower()}', 'style': 'margin-left:5px; padding:2px 4px; font-size:0.7rem;'})
                    a_tag.string = armor_class
                    armor_td.append(a_tag)
                    
                # The EGO name column can just have the overall (or no tag, or both)
                # Let's put BOTH tags in the EGO name if they differ?
                # Actually, putting it in the weapon and armor columns makes more sense if they differ.
                # If they are half-half, I'll remove the tag from EGO name and put them in weapon/armor.
                ego_name_td.find('span', class_='attr-tag').decompose()

with open('ego_list.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Tags applied to all EGOs.")
