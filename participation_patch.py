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
