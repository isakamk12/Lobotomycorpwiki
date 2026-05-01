import json
import re

gift_data = json.load(open('scratch/gift_data.json', encoding='utf-8'))
zayin=[]; teth=[]; he=[]; waw=[]; aleph=[]; abno_risks={}
c = open('abnormality_zayin.html', encoding='utf-8').read()

zayin_list = ['たった一つの罪と何百もの善', '妖精の祭典', '蓋の空いたウェルチアース', 'お前、ハゲだよ…', '黒の兵隊']
teth_list = ['赤い靴', '血の風呂', '捨てられた殺人者', '罰鳥', '宇宙の欠片', '壊れゆく甲冑', '肉の灯籠', '今日は恥ずかしがり屋', '空虚な夢', '墓穴の桜', 'キュートちゃん', '美女と野獣', '母なるクモ', '1.76MHz', '壁に向かう女', 'オールドレディ', 'マッチガール']
he_list = ['暖かい心の木こり', '幸せなテディ', '無名の胎児', '歌う機械', '雪の女王', 'オールアラウンドヘルパー', 'そりのルドル・タ', '銀河の子', 'レティシア', '死んだ蝶の葬儀', '魔弾の射手', 'シャーデンフロイデ', '知恵を欲する案山子', 'ポーキュバス']
waw_list = ['黒鳥の夢', '不調和', '絶望の騎士', '赤ずきんの傭兵', '大きくて悪いオオカミ', '地中の天国', '次元屈折変異体', '大鳥', '白雪姫のりんご', 'ラ・ルナ', '風雲僧', '夢見る流れ', '火の鳥', '寄生樹', 'アルリウネ', '憎しみの女王', '裸の巣', '女王蜂', '審判鳥', '貪欲の王']
aleph_list = ['規制済み', '静かなオーケストラ', '溶ける愛', '白夜', '何もない', '笑う死体の山', '蒼星', '終末鳥']

for abno in zayin_list: abno_risks[abno] = 'ZAYIN'
for abno in teth_list: abno_risks[abno] = 'TETH'
for abno in he_list: abno_risks[abno] = 'HE'
for abno in waw_list: abno_risks[abno] = 'WAW'
for abno in aleph_list: abno_risks[abno] = 'ALEPH'

for g in gift_data.values():
    risk = abno_risks.get(g['abno_name'])
    if risk == 'ZAYIN': zayin.append(g)
    elif risk == 'TETH': teth.append(g)
    elif risk == 'HE': he.append(g)
    elif risk == 'WAW': waw.append(g)
    elif risk == 'ALEPH': aleph.append(g)

def gen_table(gifts, title):
    html = f'<section id="gift-{title.lower()}"><h2 class="risk-header {title.lower()} reveal">{title} GIFTS</h2>'
    html += '<div class="data-table-container reveal"><table class="data-table gift-table"><thead><tr>'
    html += '<th>アブノーマリティ</th><th>ギフト名</th><th>部位</th><th>効果・ステータス</th></tr></thead><tbody>'
    for g in gifts:
        html += f'<tr><td>{g["abno_name"]}</td><td>{g["gift_name"]}</td><td>{g["part"]}</td><td>{g["stats"]}</td></tr>'
    html += '</tbody></table></div></section>'
    return html

head = c.split('<main')[0]
tail = c.split('</main>')[1]

content = head + '<main class="container" style="padding-top: 4rem;"><h1 class="reveal" style="font-size: 3rem; margin-bottom: 2rem;">E.G.O GIFT DATABASE</h1>'
content += gen_table(zayin, 'ZAYIN')
content += gen_table(teth, 'TETH')
content += gen_table(he, 'HE')
content += gen_table(waw, 'WAW')
content += gen_table(aleph, 'ALEPH')
content += '</main>' + tail

open('gift_list.html', 'w', encoding='utf-8').write(content)
