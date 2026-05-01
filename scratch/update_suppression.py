import os
import re

html_content = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>研究・コア抑制 | Lobotomy Corporation Wiki</title>
    <link rel="stylesheet" href="index.css">
    <style>
        .research-box {
            margin-top: 1rem;
            padding: 1rem;
            background: rgba(0, 0, 0, 0.4);
            border-radius: 4px;
            border-left: 2px solid var(--text-secondary);
        }
        .research-box h4 {
            font-size: 1.1rem;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }
        .research-box ul {
            list-style-type: disc;
            margin-left: 1.5rem;
            font-size: 0.9rem;
            color: var(--text-secondary);
        }
        .research-box li {
            margin-bottom: 0.3rem;
        }
        .bug-note {
            margin-top: 0.5rem;
            padding: 0.5rem;
            background: rgba(255, 50, 50, 0.1);
            border-left: 3px solid #ff3333;
            font-size: 0.85rem;
            color: #ffcccc;
        }
    </style>
</head>
<body>
    <div class="scanline"></div>
    <div class="noise"></div>
    <nav class="main-nav">
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
    </nav>
    <main class="container" style="padding-top: 4rem;">
        <h1 class="reveal" style="font-size: 3rem; margin-bottom: 1rem;">RESEARCH & SUPPRESSION (研究とコア抑制)</h1>
        <p class="reveal" style="color: var(--text-secondary); margin-bottom: 3rem;">各部門のミッションを進めることで解放される「研究」、そしてセフィラたちの精神を安定させるための特殊戦「コア抑制」。これらをクリアすることで施設全体に強力な恩恵をもたらします。</p>

        <!-- 1. 上層セフィラ -->
        <section id="upper">
            <h2 class="section-title reveal">01. 上層セフィラ</h2>
            <div class="grid-2">
                <div class="card reveal" style="border-left: 4px solid #ffba00;">
                    <span class="attr-tag" style="background: #ffba00; color: #000;">コントロール：マルクト</span>
                    <h3>コア抑制: 作業名隠蔽</h3>
                    <p>指示がランダムに入れ替わり、名称が「？」で隠されます。暴走レベル4以降は指示のキャンセルも不可能に。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 移動速度強化、LOBポイント獲得量が1.2倍</p>
                    <div class="bug-note">
                        <strong>【バグ情報】 移動速度強化のバグ</strong><br>
                        「全職員の移動速度が強化される」という報酬テキストが表示されますが、抑制前後で比較してもほとんど差が生じず、実質的に機能していないバグ（設定ミス）が確認されています。
                    </div>
                    
                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li><strong>TT2プロトコル:</strong> ゲーム速度の変更（倍速）が可能になります。</li>
                            <li><strong>合同指揮:</strong> 職員を他部門へ移動・作業指示できるようになります。</li>
                            <li><strong>集合命令:</strong> 全職員をメインルームに待機させるコマンドを追加します。</li>
                        </ul>
                    </div>
                </div>
                <div class="card reveal" style="border-left: 4px solid #cc00ff;">
                    <span class="attr-tag" style="background: #cc00ff; color: #fff;">情報：イェソド</span>
                    <h3>コア抑制: ピクセル化</h3>
                    <p>UIが強烈なモザイクで覆われ、HPバーやステータスが判別不能に。事前に職員の配置と能力を覚えておくことが鍵。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 固有PEボックス獲得量25%増加</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">アブノーマリティから得られる固有PEボックスが増え、装備の抽出が早くなります。</p>
                    
                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li><strong>可視化・ダメージ規格化:</strong> 職員のHP/SPや名前、アブノーマリティのHPや危険度、さらに受けるダメージの属性と値・耐性などを画面に表示させる、最も基礎的な必須研究です。</li>
                            <li><strong>アブノーマリティ対応マニュアル:</strong> オフィサーが受ける恐怖ダメージを軽減し、パニックになりにくくします。</li>
                        </ul>
                    </div>
                </div>
                <div class="card reveal" style="border-left: 4px solid #00ccff;">
                    <span class="attr-tag" style="background: #00ccff; color: #000;">教育：ホド</span>
                    <h3>コア抑制: 能力値低下</h3>
                    <p>全職員のステータスに最大-35のデバフ。「あなたは幸せでなければならない」等で補正するか、短期決戦を狙いましょう。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 新規雇用職員が「ランク3」でスタート</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">たった1ポイントでランク4の職員が雇えるようになるなど、育成効率が飛躍的に向上する最高クラスの報酬です。</p>
                    
                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li><strong>教育マニュアル配給:</strong> 全職員の成長速度を+50%する非常に強力なバフ研究です。</li>
                            <li><strong>職務教育の強化:</strong> オフィサーの能力値が向上し（命中率が40%から60%へ上昇）、黎明やTETH程度なら少しは戦えるようになります。</li>
                            <li><strong>雇用手続き強化:</strong> 新規雇用時のステータスがわずかに上昇します（実感できない程度の気休めです）。</li>
                        </ul>
                    </div>
                </div>
                <div class="card reveal" style="border-left: 4px solid #00ff66;">
                    <span class="attr-tag" style="background: #00ff66; color: #000;">安全：ネツァク</span>
                    <h3>コア抑制: 回復不能</h3>
                    <p>施設内の回復効果が全て無効化。暴走レベルが上がる瞬間の全回復タイミングを戦略的に利用する必要があります。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 廊下・エレベーターでも自動回復が適用</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">メインルーム限定だった自動回復効果が施設全域に適用されるようになります。</p>
                    
                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li><strong>再生リアクターMk2 / 精神汚染中和ガス:</strong> メインルームでのHPおよびSPの自動回復量を増加させます（5〜6から10へ増加）。</li>
                            <li><strong>再生リアクター認識基準修正:</strong> 通常、メインルームに敵が侵入すると回復が止まりますが、この研究により50%の確率で回復が継続するようになります。</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>

        <!-- 2. 中層セフィラ -->
        <section id="middle">
            <h2 class="section-title reveal">02. 中層セフィラ</h2>
            <div class="grid-2">
                <div class="card reveal" style="border-left: 4px solid #ffeb3b;">
                    <span class="attr-tag" style="background: #ffeb3b; color: #000;">中央本部：ティファレト</span>
                    <h3>コア抑制: 長期持久戦</h3>
                    <p>暴走レベル10到達が目標。必ず「夕暮れ」「深夜」の試練を越える必要があり、安全な場所への避難が不可欠。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 弾丸の最大数が30%増加、「PALEシールド弾」解放</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">弾丸の最大数が増加し、さらに貴重なPALE属性のシールド弾が追加されます。</p>
                </div>
                <div class="card reveal" style="border-left: 4px solid #f44336;">
                    <span class="attr-tag" style="background: #f44336; color: #fff;">懲戒：ゲブラー</span>
                    <h3>コア抑制: 赤い霧 (Red Mist)</h3>
                    <p>最強の戦士との直接対決。正攻法のほか、「シェルター」を利用してアブノーマリティに戦わせる攻略法も存在。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: E.G.O最大製造数が+1</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">本来1着しか作れない強力なALEPH装備を2着ずつ作れるようになる破格の報酬です。</p>
                    
                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li><strong>クリフォト干渉シールド:</strong> 敵対個体の移動速度を一定時間半減させる弾丸です。</li>
                            <li><strong>処刑弾:</strong> 職員やオフィサーを即座に消去（即死）させます。死体に反応して脱走するアブノーマリティ（笑う死体の山など）を防ぐための必須の技術です。</li>
                            <li><strong>ウサギチーム:</strong> エネルギーを25%消費してR社の傭兵部隊を呼び出し、指定した部門を完全封鎖して鎮圧を任せることができます。</li>
                        </ul>
                    </div>
                </div>
                <div class="card reveal" style="border-left: 4px solid #2196f3;">
                    <span class="attr-tag" style="background: #2196f3; color: #fff;">福祉：ケセド</span>
                    <h3>コア抑制: ダメージ倍増</h3>
                    <p>指定属性の被ダメージが5倍に。暴走レベルに応じて属性が増え、一瞬のミスが即死に繋がります。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 死亡・パニック時に25%の確率で耐え凌ぐ</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">職員のHP・SPが0になって死亡・パニックになる際、確率で少しだけ回復して生き残るようになります。</p>
                    
                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li><strong>HP弾 / SP弾:</strong> 職員の体力や精神力を即座に回復させる弾丸です。</li>
                            <li><strong>物理保護 / トラウマ / 侵食 シールド弾:</strong> それぞれRED、WHITE、BLACK属性のダメージを一定量無効化するバリアを付与します。</li>
                        </ul>
                        <div class="bug-note" style="margin-top: 0.5rem;">
                            <strong>【罠情報】 回復弾の回復量増加のバグ</strong><br>
                            HP弾・SP弾の回復量を上げる研究ですが、バグのため取得しても回復量は25のままで一切変化しません。この研究を取得するメリットは全く存在せず、後回しにすべき罠となっています。
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 3. 下層セフィラ -->
        <section id="lower">
            <h2 class="section-title reveal">03. 下層セフィラ</h2>
            <div class="grid-2">
                <div class="card reveal" style="border-left: 4px solid #9e9e9e;">
                    <span class="attr-tag" style="background: #9e9e9e; color: #fff;">記録：ホクマー</span>
                    <h3>コア抑制: 一時停止禁止</h3>
                    <p>PAUSEでペナルティ（即死・パニック）。暴走レベルと共にゲーム速度が加速。Escキーでの擬似停止が救済措置に。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 職員ステータス上限が130まで解放</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">LOBポイントでそこまで強化できるようになります。</p>

                    <div class="research-box">
                        <h4>主な研究</h4>
                        <ul>
                            <li>職員のステータス（勇気、慎重、自制）の上限を100から120まで引き上げてくれます。</li>
                        </ul>
                    </div>
                </div>
                <div class="card reveal" style="border-left: 4px solid #4a148c;">
                    <span class="attr-tag" style="background: #4a148c; color: #fff;">抽出：ビナー</span>
                    <h3>コア抑制: 調律者 (Arbiter)</h3>
                    <p>特殊暴走をばら撒くボス戦。暴走を対処して弱体化した隙に総攻撃を仕掛けましょう。「逆行時計」も有効。</p>
                    <p style="margin-top: 1rem; color: var(--accent-color); font-weight: bold;">REWARD: 職員死亡時に装備（E.G.O）を100%回収</p>
                    <p style="font-size: 0.9rem; color: var(--text-secondary);">職員が死亡しても、装備していたE.G.Oが失われず100%手元に残るようになります。</p>
                </div>
            </div>
        </section>
    </main>
    <script src="main.js"></script>
</body>
</html>
"""

with open('suppression.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
