from pathlib import Path

TALLY = "https://tally.so/r/LZeJ4G"

# seo_patch.py の処理後に、申込導線を会員・オブザーバー共通フォームへ統一する。
p = Path("index.html")
html = p.read_text(encoding="utf-8")

# 旧Googleフォームを新Tallyフォームへ統一
html = html.replace("https://forms.gle/R7KaSbq9iwH9X8Yq6", TALLY)

# 次回例会欄：会員にも分かる共通の表現へ
html = html.replace(
    ">この勉強会にオブザーバー参加する</a>",
    ">例会に参加する・出欠を登録する</a><p style=\"margin:10px 0 0;color:#74656a;font-size:14px\">会員・オブザーバー共通の申込フォームです。フォーム内で参加区分を選択してください。</p>"
)

# 次回例会の案内画像を先頭に配置し、その直下に申込ボタンと開催情報を1行で表示
poster_block = '''<div style="max-width:760px;margin:0 auto 24px;text-align:center"><img src="2026-09-meeting.png" alt="盛心実践会千葉・心を高める経営を伸ばす会佐倉 2026年9月度合同自主例会のご案内" style="display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 12px 30px rgba(107,31,43,.12)"></div><div style="text-align:center;margin:0 0 22px"><a class="btn btn-primary" target="_blank" rel="noopener" href="https://tally.so/r/LZeJ4G">例会に参加する・出欠を登録する</a><p style="margin:10px 0 0;color:#74656a;font-size:14px">会員・オブザーバー共通の申込フォームです。フォーム内で参加区分を選択してください。</p></div><div style="margin:0 0 28px;padding:13px 16px;border-radius:14px;background:#f2e8ea;text-align:center;line-height:1.7"><strong>9月29日（火）18:00〜21:00</strong> <span style="color:#9b6a72;padding:0 8px">｜</span> <strong>グリーンセミナールーム</strong> <span style="color:#74656a">（千葉駅 徒歩約10分）</span></div>'''
marker = '<div class="event-body">'
if 'src="2026-09-meeting.png"' not in html and marker in html:
    html = html.replace(marker, marker + poster_block, 1)

# 画像と情報が重複するため、従来の大きな3列「開催日時・会場・住所」は非表示にする
html = html.replace('<div class="event-meta">', '<div class="event-meta" style="display:none">', 1)

# ページ下部にある同じ申込ボタンは重複するため削除（上部CTAに一本化）
old_bottom = '<div class="event-actions"><a class="btn btn-primary" target="_blank" rel="noopener" href="https://tally.so/r/LZeJ4G">例会に参加する・出欠を登録する</a><p style="margin:10px 0 0;color:#74656a;font-size:14px">会員・オブザーバー共通の申込フォームです。フォーム内で参加区分を選択してください。</p></div>'
html = html.replace(old_bottom, '', 1)

# 参加方法欄は一般向けの説明なので「オブザーバー参加」の表現を残し、リンクだけTallyへ
html = html.replace(
    'href="#observer">まずはオブザーバー参加</a>',
    f'href="{TALLY}" target="_blank" rel="noopener">まずはオブザーバー参加</a>'
)

p.write_text(html, encoding="utf-8")

# SEOランディングページにも同じ共通フォームを反映
lp = Path("chiba-keieisha-benkyokai.html")
if lp.exists():
    lhtml = lp.read_text(encoding="utf-8")
    lhtml = lhtml.replace("https://forms.gle/R7KaSbq9iwH9X8Yq6", TALLY)
    lhtml = lhtml.replace(
        ">この勉強会にオブザーバー参加する</a>",
        ">例会に参加する・出欠を登録する</a>"
    )
    lp.write_text(lhtml, encoding="utf-8")
