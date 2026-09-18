from pathlib import Path

p = Path("index.html")
html = p.read_text(encoding="utf-8")

old = '''<div style="margin:0 0 28px;padding:13px 16px;border-radius:14px;background:#f2e8ea;text-align:center;line-height:1.7"><strong>9月29日（火）18:00〜21:00</strong> <span style="color:#9b6a72;padding:0 8px">｜</span> <strong>グリーンセミナールーム</strong> <span style="color:#74656a">（千葉駅 徒歩約10分）</span></div>'''

new = '''<div class="meeting-summary"><div class="meeting-summary-date">9月29日（火）18:00〜21:00</div><div class="meeting-summary-venue"><strong>グリーンセミナールーム</strong><span>（千葉駅 徒歩約10分）</span></div></div>'''

html = html.replace(old, new, 1)

# 参加費はスマホで「塾生／無料」「オブザーバー／5,000円」を明確に分離する
fee_grid = 'style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px"'
html = html.replace(fee_grid, 'class="fee-options" style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px"', 1)

css = '''
<style>
.meeting-summary{margin:0 0 28px;padding:13px 16px;border-radius:14px;background:#f2e8ea;text-align:center;line-height:1.7;display:flex;align-items:center;justify-content:center;gap:14px;flex-wrap:wrap}
.meeting-summary-date{font-weight:800;white-space:nowrap}
.meeting-summary-venue{display:flex;align-items:baseline;justify-content:center;gap:4px;flex-wrap:wrap}
.meeting-summary-venue strong{white-space:nowrap}
.meeting-summary-venue span{color:#74656a;white-space:nowrap}
@media(max-width:600px){
  .meeting-summary{display:block;padding:16px 14px;line-height:1.55}
  .meeting-summary-date{font-size:16px}
  .meeting-summary-venue{margin-top:7px;display:block}
  .meeting-summary-venue strong{display:block;font-size:17px}
  .meeting-summary-venue span{display:block;margin-top:2px;font-size:14px}
  .fee-options{grid-template-columns:1fr !important;gap:10px !important}
  .fee-options > div{padding:15px 16px !important}
}
</style>
'''

if '.meeting-summary{' not in html:
    html = html.replace('</head>', css + '</head>', 1)

p.write_text(html, encoding="utf-8")
