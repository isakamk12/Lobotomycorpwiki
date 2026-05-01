import re
import glob

# 1. Fix 'ペイル' to '青(PALE)' in all HTML files
files = glob.glob('*.html')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('>ペイル<', '>青(PALE)<')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Add half-and-half and ALEPH backgrounds to ego_list.html
with open('ego_list.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'<tr>(<td>壊れゆく甲冑.*?</td>)</tr>', r'<tr class="bg-half-teth-he">\1</tr>', c)
c = re.sub(r'<tr>(<td>壁に向かう女.*?</td>)</tr>', r'<tr class="bg-half-teth-he">\1</tr>', c)
c = re.sub(r'<tr>(<td>死んだ蝶の葬儀.*?</td>)</tr>', r'<tr class="bg-half-he-waw">\1</tr>', c)
c = re.sub(r'<tr>(<td>魔弾の射手.*?</td>)</tr>', r'<tr class="bg-half-he-waw">\1</tr>', c)
c = re.sub(r'<tr>(<td>貪欲の王.*?</td>)</tr>', r'<tr class="bg-half-waw-aleph">\1</tr>', c)
c = re.sub(r'<tr>(<td>黒の兵隊.*?</td>)</tr>', r'<tr class="bg-aleph">\1</tr>', c)
c = re.sub(r'<tr>(<td>審判鳥.*?</td>)</tr>', r'<tr class="bg-aleph">\1</tr>', c)

# Add explicit EGO class tags to those upgraded items
c = re.sub(r'（※HE格上げ）', r'（※HE格上げ）<span class="attr-tag tag-he" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">HE</span>', c)
c = re.sub(r'（※WAW格上げ・FFあり）', r'（※WAW格上げ・FFあり）<span class="attr-tag tag-waw" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">WAW</span>', c)
c = re.sub(r'（※WAW格上げ）', r'（※WAW格上げ）<span class="attr-tag tag-waw" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">WAW</span>', c)
c = re.sub(r'（※ALEPH格上げ・超火力）', r'（※ALEPH格上げ・超火力）<span class="attr-tag tag-aleph" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">ALEPH</span>', c)
c = re.sub(r'（※ALEPH格上げ）', r'（※ALEPH格上げ）<span class="attr-tag tag-aleph" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">ALEPH</span>', c)
c = re.sub(r'（※ALEPH防具）', r'（※ALEPH防具）<span class="attr-tag tag-aleph" style="margin-left:5px;padding:2px 4px;font-size:0.7rem;">ALEPH</span>', c)

with open('ego_list.html', 'w', encoding='utf-8') as f:
    f.write(c)

# 3. Add bug notes to abnormality_aleph.html
with open('abnormality_aleph.html', 'r', encoding='utf-8') as f:
    c_aleph = f.read()

bug_note = """
                    </ul>
                    <div class="bug-note" style="margin-top: 1rem;">
                        <strong>【バグ情報】 機能不全バグ</strong><br>
                        たまに攻撃も追跡もせず、その場でひたすら滑り続ける「機能不全バグ」があります。停止していても突然発生し、DPSや回復効率が大幅に下がってしまいます。<br><br>
                        <strong>【バグ情報】 特殊攻撃持ち武器の攻撃判定消失バグ</strong><br>
                        ミミック、ダ・カーポ、黄金狂など特殊攻撃持ちの武器で、ダメージ発生直前に鎮圧を解除して再度指定すると、モーションがキャンセルされ攻撃判定が消失するバグがあります。
                    </div>"""

c_aleph = c_aleph.replace('<li><strong style="color: var(--text-primary);">防具「ミミック」:</strong> REDダメージを0.2まで抑える最強のRED特化防具。</li>\n                    </ul>', '<li><strong style="color: var(--text-primary);">防具「ミミック」:</strong> REDダメージを0.2まで抑える最強のRED特化防具。</li>' + bug_note)

with open('abnormality_aleph.html', 'w', encoding='utf-8') as f:
    f.write(c_aleph)

# 4. Add risk tags to all abnormality cards in abnormality_*.html
risk_levels = ['zayin', 'teth', 'he', 'waw', 'aleph']
for risk in risk_levels:
    file = f'abnormality_{risk}.html'
    try:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Insert tag right after <div class="card reveal" ...>
        # Wait, cards look like: <div class="card reveal">\n                    <h3>
        # Or <div class="card reveal" style="...">\n
        
        def replacer(match):
            card_open = match.group(0)
            tag = f'\n                    <span class="attr-tag tag-{risk}">{risk.upper()}</span>'
            # Only add if not already has a tag span (like the warnings)
            return card_open + tag

        # Using a regex that matches <div class="card ...> not followed by <span
        # Actually it's easier to just do:
        content = re.sub(r'(<div class="card reveal"[^>]*>)\s*(?!<span class="attr-tag)', replacer, content)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        print(f"Error processing {file}: {e}")

print("All fixes applied successfully.")
