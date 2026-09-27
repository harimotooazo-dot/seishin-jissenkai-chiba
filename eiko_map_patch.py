from pathlib import Path

MAP='https://www.google.co.jp/maps?q=%E5%8D%83%E8%91%89%E7%9C%8C%E5%8D%83%E8%91%89%E5%B8%82%E4%B8%AD%E5%A4%AE%E5%8C%BA%E4%B8%AD%E5%A4%AE3%E4%B8%81%E7%9B%AE15-3+%E6%B0%B8%E8%88%88'
for name in ['schedule.html','member.html','entry.html']:
    p=Path(name)
    s=p.read_text(encoding='utf-8')
    # Add a map link immediately after the Asahi Plaza Chiba Chuo address wherever the golf details contain it.
    target='千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央'
    replacement=target+f'<br><a href="{MAP}" target="_blank" rel="noopener" style="font-weight:800;text-decoration:underline">Googleマップで見る</a>'
    if target in s and '永興' in s:
        s=s.replace(target,replacement)
    p.write_text(s,encoding='utf-8')
