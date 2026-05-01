import re
import glob

nav_html = """<nav class="main-nav">
        <div class="nav-container">
            <ul class="nav-list">
                <li class="nav-item"><a href="index.html">HOME</a></li>
                <li class="nav-item has-dropdown">
                    <a href="abnormality_zayin.html">アブノーマリティ</a>
                    <ul class="dropdown">
                        <li><a href="abnormality_zayin.html">ZAYIN</a></li>
                        <li><a href="abnormality_teth.html">TETH</a></li>
                        <li><a href="abnormality_he.html">HE</a></li>
                        <li><a href="abnormality_waw.html">WAW</a></li>
                        <li><a href="abnormality_aleph.html">ALEPH</a></li>
                        <li><a href="tool_list.html">ツール型 (Tool)</a></li>
                    </ul>
                </li>
                <li class="nav-item has-dropdown">
                    <a href="ego_list.html">E.G.O</a>
                    <ul class="dropdown">
                        <li><a href="gift_list.html">ギフト (Gift)</a></li>
                        <li><a href="ego_list.html">装備 (Equipment)</a></li>
                    </ul>
                </li>
                <li class="nav-item"><a href="story.html">ストーリー・関連作</a></li>
                <li class="nav-item"><a href="ordeals.html">試練</a></li>
                <li class="nav-item"><a href="suppression.html">研究・コア抑制</a></li>
                <li class="nav-item"><a href="mods.html">MOD</a></li>
            </ul>
        </div>
    </nav>"""

files = glob.glob('*.html')
for file in files:
    if file == 'abnormality_list.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace everything between <nav class="main-nav"> and </nav>
    content = re.sub(r'<nav class="main-nav">.*?</nav>', nav_html, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Nav fixed.")
