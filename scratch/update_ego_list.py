import re

with open('ego_list.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'<tr>(<td>壊れゆく甲冑.*?</td>)</tr>', r'<tr class="bg-half-teth-he">\1</tr>', c)
c = re.sub(r'<tr>(<td>壁に向かう女.*?</td>)</tr>', r'<tr class="bg-half-teth-he">\1</tr>', c)
c = re.sub(r'<tr>(<td>死んだ蝶の葬儀.*?</td>)</tr>', r'<tr class="bg-half-he-waw">\1</tr>', c)
c = re.sub(r'<tr>(<td>魔弾の射手.*?</td>)</tr>', r'<tr class="bg-half-he-waw">\1</tr>', c)
c = re.sub(r'<tr>(<td>貪欲の王.*?</td>)</tr>', r'<tr class="bg-half-waw-aleph">\1</tr>', c)

# For pink and justitia, they are upgraded entirely so we color their row as ALEPH
c = re.sub(r'<tr>(<td>黒の兵隊.*?</td>)</tr>', r'<tr class="bg-aleph">\1</tr>', c)
c = re.sub(r'<tr>(<td>審判鳥.*?</td>)</tr>', r'<tr class="bg-aleph">\1</tr>', c)

with open('ego_list.html', 'w', encoding='utf-8') as f:
    f.write(c)
