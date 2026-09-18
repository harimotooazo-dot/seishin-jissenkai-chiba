from pathlib import Path

p = Path("index.html")
html = p.read_text(encoding="utf-8")

old_fee = '''<div class="fee"><strong>参加費</strong>　塾生：無料 ／ オブザーバー：5,000円　<small>※コンパ費用込み</small></div>'''

new_fee = '''<div class="fee fee-detail" style="margin:18px 0 24px;padding:20px;border-radius:18px"><div style="margin-bottom:14px;color:#2f2023;font-size:20px;font-weight:900">参加費</div><div class="fee-options" style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px"><div style="padding:14px 16px;border-radius:14px;background:#fff;text-align:center"><div style="font-weight:800;color:#66575b">塾生</div><div style="margin-top:4px;color:#7b1f2b;font-size:21px;font-weight:900">無料</div></div><div style="padding:14px 16px;border-radius:14px;background:#fff;text-align:center"><div style="font-weight:800;color:#66575b">オブザーバー</div><div style="margin-top:4px;color:#7b1f2b;font-size:21px;font-weight:900">5,000円</div></div></div><p style="margin:12px 0 0;color:#74656a;font-size:13px">※コンパ費用込み</p></div>'''

# Remove the old compact fee line from below the program section.
html = html.replace(old_fee, '', 1)

# Put the fee immediately after the date/venue/location cards and before the theme.
if 'class="fee fee-detail"' not in html:
    html = html.replace('<div class="theme">', new_fee + '<div class="theme">', 1)

css = '''
<style>
@media(max-width:600px){
  .fee-detail{padding:18px 16px !important;margin:16px 0 22px !important}
  .fee-detail .fee-options{grid-template-columns:1fr !important;gap:10px !important}
  .fee-detail .fee-options > div{padding:14px 16px !important}
}
</style>
'''
if '.fee-detail .fee-options' not in html:
    html = html.replace('</head>', css + '</head>', 1)

p.write_text(html, encoding="utf-8")
