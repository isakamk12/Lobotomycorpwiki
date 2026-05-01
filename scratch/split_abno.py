import os
import re

with open('abnormality_list.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Instead of relying on exact character indices which might be wrong due to CRLF, 
# I will use split based on sections.
head = c.split('<section id="zayin">')[0]
tail_parts = c.split('</section>\n    </main>')
if len(tail_parts) > 1:
    tail = '</section>\n    </main>' + tail_parts[1]
else:
    tail = '</main>' + c.split('</main>')[1]

zayin_match = re.search(r'(<section id="zayin">.*?</section>)', c, re.DOTALL)
teth_match = re.search(r'(<section id="teth">.*?</section>)', c, re.DOTALL)
he_match = re.search(r'(<section id="he">.*?</section>)', c, re.DOTALL)
waw_match = re.search(r'(<section id="waw">.*?</section>)', c, re.DOTALL)
aleph_match = re.search(r'(<section id="aleph">.*?</section>)', c, re.DOTALL)

sections = {
    'abnormality_zayin.html': (zayin_match, 'ZAYIN'),
    'abnormality_teth.html': (teth_match, 'TETH'),
    'abnormality_he.html': (he_match, 'HE'),
    'abnormality_waw.html': (waw_match, 'WAW'),
    'abnormality_aleph.html': (aleph_match, 'ALEPH')
}

nav_html = """<li class="nav-item has-dropdown">
                    <a href="abnormality_zayin.html">アブノーマリティ</a>
                    <ul class="dropdown">
                        <li><a href="abnormality_zayin.html">ZAYIN</a></li>
                        <li><a href="abnormality_teth.html">TETH</a></li>
                        <li><a href="abnormality_he.html">HE</a></li>
                        <li><a href="abnormality_waw.html">WAW</a></li>
                        <li><a href="abnormality_aleph.html">ALEPH</a></li>
                        <li><a href="tool_list.html">ツール型 (Tool)</a></li>
                    </ul>
                </li>"""

ego_nav_html = """<li class="nav-item has-dropdown">
                    <a href="ego_list.html">E.G.O</a>
                    <ul class="dropdown">
                        <li><a href="gift_list.html">ギフト (Gift)</a></li>
                        <li><a href="ego_list.html">装備 (Equipment)</a></li>
                    </ul>
                </li>"""

# Process all sections
for fname, (match, label) in sections.items():
    if match:
        content = match.group(1)
        # Reconstruct full HTML
        full_html = head + '<main class="container" style="padding-top: 4rem;">\n        ' + content + '\n    </main>\n' + tail
        
        # Update Nav
        full_html = re.sub(r'<li class="nav-item has-dropdown">\s*<a href="abnormality_list.html">.*?</ul>\s*</li>', nav_html, full_html, count=1, flags=re.DOTALL)
        full_html = re.sub(r'<li class="nav-item has-dropdown">\s*<a href="ego_list.html">.*?</ul>\s*</li>', ego_nav_html, full_html, count=1, flags=re.DOTALL)
        
        # Update H1
        full_html = re.sub(r'ABNORMALITY ENCYCLOPEDIA', f'ABNORMALITY ENCYCLOPEDIA - {label}', full_html)
        
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(full_html)
    else:
        print(f"Failed to find match for {label}")

# Update other pages
other_pages = ['index.html', 'ego_list.html', 'tool_list.html', 'ordeals.html', 'suppression.html', 'story.html', 'mods.html']
for page in other_pages:
    with open(page, 'r', encoding='utf-8') as f:
        page_content = f.read()
    
    page_content = re.sub(r'<li class="nav-item has-dropdown">\s*<a href="abnormality_list.html">.*?</ul>\s*</li>', nav_html, page_content, count=1, flags=re.DOTALL)
    page_content = re.sub(r'<li class="nav-item has-dropdown">\s*<a href="ego_list.html">.*?</ul>\s*</li>', ego_nav_html, page_content, count=1, flags=re.DOTALL)
    
    # Fix abnormality_list.html#anchors if any
    page_content = re.sub(r'abnormality_list\.html#zayin', 'abnormality_zayin.html', page_content)
    page_content = re.sub(r'abnormality_list\.html#teth', 'abnormality_teth.html', page_content)
    page_content = re.sub(r'abnormality_list\.html#he', 'abnormality_he.html', page_content)
    page_content = re.sub(r'abnormality_list\.html#waw', 'abnormality_waw.html', page_content)
    page_content = re.sub(r'abnormality_list\.html#aleph', 'abnormality_aleph.html', page_content)
    page_content = re.sub(r'abnormality_list\.html', 'abnormality_zayin.html', page_content)

    with open(page, 'w', encoding='utf-8') as f:
        f.write(page_content)
