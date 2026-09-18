from pathlib import Path

p = Path("index.html")
html = p.read_text(encoding="utf-8")

old_fee = '''<div class="fee"><strong>参加費</strong>　塾生：無料 ／ オブザーバー：5,000円　<small>※コンパ費用込み</small></div>'''

# 日時・会場・場所と同じテンションで、参加費だけが強く目立たない表示にする。
# 塾生とオブザーバーは改行して読み分けやすくする。
new_fee = '''<div class="fee fee-detail"><strong>参加費</strong><br><span>塾生：無料</span><br><span>オブザーバー：5,000円</span><br><small>※コンパ費用込み</small></div>'''

# Remove the old compact fee line from below the program section.
html = html.replace(old_fee, '', 1)

# Put the fee immediately after the date/venue/location cards and before the theme.
if 'class="fee fee-detail"' not in html:
    html = html.replace('<div class="theme">', new_fee + '<div class="theme">', 1)

css = '''
<style>
.fee-detail{
  margin:14px 0 24px;
  padding:15px;
  border-radius:16px;
  background:var(--soft);
  color:var(--ink);
  font-size:16px;
  line-height:1.8;
}
.fee-detail strong{color:var(--ink);font-size:16px}
.fee-detail span{font-weight:400}
.fee-detail small{color:var(--muted);font-size:13px}
@media(max-width:600px){
  .fee-detail{margin:14px 0 22px;padding:15px;font-size:16px}
}
</style>
'''
if '.fee-detail{' not in html:
    html = html.replace('</head>', css + '</head>', 1)

p.write_text(html, encoding="utf-8")
