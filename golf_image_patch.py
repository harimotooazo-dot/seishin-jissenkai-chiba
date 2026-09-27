from pathlib import Path

IMG = '<img src="golf-2026.png" alt="盛心実践会 千葉・心を高める経営を伸ばす会 佐倉 合同ゴルフコンペ">'

# 活動予定
p=Path('schedule.html'); s=p.read_text(encoding='utf-8')
needle='<div class="date">2026年11月24日（火）</div><h2>盛心実践会 千葉・心を高める経営を伸ばす会 佐倉　合同ゴルフコンペ</h2></div><div class="body">'
if needle in s and 'golf-2026.png' not in s:
    s=s.replace(needle, needle.replace('</div><div class="body">','</div>'+IMG+'<div class="body">'),1)
p.write_text(s,encoding='utf-8')

# 塾生専用
p=Path('member.html'); s=p.read_text(encoding='utf-8')
needle='<h3>盛心実践会 千葉・心を高める経営を伸ばす会 佐倉　合同ゴルフコンペ</h3>'
if needle in s and 'golf-2026.png' not in s:
    s=s.replace(needle, needle+'<div style="margin:16px 0"><img src="golf-2026.png" alt="合同ゴルフコンペ" style="width:100%;height:auto;display:block;border-radius:16px"></div>',1)
p.write_text(s,encoding='utf-8')

# LINEメニューからの参加申込
p=Path('entry.html'); s=p.read_text(encoding='utf-8')
needle='<section class="event" id="golf">\n<div class="event-content">'
if needle in s and 'golf-2026.png' not in s:
    s=s.replace(needle,'<section class="event" id="golf">\n'+IMG+'\n<div class="event-content">',1)
p.write_text(s,encoding='utf-8')
