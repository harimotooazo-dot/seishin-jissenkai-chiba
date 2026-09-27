from pathlib import Path

MAP = '''<div style="margin:12px 0 8px"><iframe title="中国料理 永興 地図" src="https://www.google.com/maps?q=%E5%8D%83%E8%91%89%E7%9C%8C%E5%8D%83%E8%91%89%E5%B8%82%E4%B8%AD%E5%A4%AE%E5%8C%BA%E4%B8%AD%E5%A4%AE3-15-3%20%E6%9C%9D%E6%97%A5%E3%83%97%E3%83%A9%E3%82%B6%E5%8D%83%E8%91%89%E4%B8%AD%E5%A4%AE&output=embed" width="100%" height="260" style="border:0;border-radius:14px" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div><p><a href="https://www.google.com/maps/search/?api=1&query=%E4%B8%AD%E5%9B%BD%E6%96%99%E7%90%86%20%E6%B0%B8%E8%88%88%20%E5%8D%83%E8%91%89%E5%B8%82%E4%B8%AD%E5%A4%AE%E5%8C%BA%E4%B8%AD%E5%A4%AE3-15-3" target="_blank" rel="noopener" style="font-weight:800">Googleマップで大きく見る</a></p>'''

for fn in ('schedule.html','member.html','entry.html'):
    p=Path(fn)
    if not p.exists(): continue
    s=p.read_text(encoding='utf-8')
    if '中国料理 永興 地図' in s: continue
    needles=[
      '千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央</p>',
      '千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央2階</p>',
      '千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央<br>',
    ]
    for n in needles:
        if n in s:
            s=s.replace(n,n+MAP,1)
            break
    p.write_text(s,encoding='utf-8')
