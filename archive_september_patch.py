from pathlib import Path
import re

# 1) Activity schedule: remove September from upcoming events, add October meeting, and keep September archive.
p=Path('schedule.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'<article class="event">(?:(?!<article class="event">).)*?9月度 合同自主例会(?:(?!<article class="event">).)*?</article>','',s,count=1,flags=re.S)
october='''<article class="event"><div class="event-head"><div class="date">2026年10月27日（火）18:00〜21:00</div><h2>10月度 合同勉強会</h2></div><div class="body"><div class="theme">経営問答シリーズ</div><p><strong>会場：</strong>グリーンセミナールーム<br>千葉市中央区富士見2-8-14 エキニア千葉4F</p><p>今回は「経営問答シリーズ」を予定しています。テーマ・内容などの詳細は決まり次第ご案内します。</p></div></article>'''
if '2026年10月27日（火）' not in s:
    s=s.replace('<article class="event"><div class="event-head"><div class="date">2026年11月18日',october+'<article class="event"><div class="event-head"><div class="date">2026年11月18日',1)
archive='''<div style="margin:46px 0 18px"><div class="eyebrow">PAST ACTIVITIES</div><h2 style="margin:6px 0 8px">過去の活動</h2><p style="color:var(--muted);margin:0 0 18px">終了した勉強会・例会の学びと当日の様子を残しています。</p></div><article class="event"><div class="event-head"><div class="date">2026年9月29日（火）開催</div><h2>9月度 合同自主例会</h2></div><img src="2026-09-meeting-wide.png" alt="9月度 合同自主例会"><div class="body"><div class="theme">経営12ヵ条 第4条「誰にも負けない努力をする」</div><p>講話・グループディスカッション、フィロソフィ「ベクトルを揃える」、京セラ式コンパを通じて学びを深めました。</p><a class="btn" href="archive-2026-09.html#materials">資料を見る →</a></div></article>'''
if 'PAST ACTIVITIES' not in s:
    s=s.replace('<div class="info">',archive+'<div class="info">',1)
p.write_text(s,encoding='utf-8')

# 2) LINE entry page: completed September event is no longer shown under current applications.
p=Path('entry.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'\s*<section class="event" id="september">.*?</section>\s*','\n',s,count=1,flags=re.S)
p.write_text(s,encoding='utf-8')

# 3) Homepage: October 27 is the next meeting. Details are intentionally shown as undecided.
p=Path('index.html')
s=p.read_text(encoding='utf-8')
oct_home='''<section id="next" class="next"><div class="wrap"><div class="section-title"><div class="eyebrow">NEXT MEETING</div><h2>次回勉強会</h2></div><div class="event"><div class="event-head"><div>2026年10月27日（火）18:00〜21:00</div><h2>10月度 合同勉強会</h2></div><div class="event-body"><div class="meta-grid"><div class="meta"><strong>日時</strong><br>10月27日（火）18:00〜21:00</div><div class="meta"><strong>会場</strong><br>グリーンセミナールーム</div><div class="meta"><strong>場所</strong><br>千葉市中央区富士見2-8-14<br>エキニア千葉4F</div></div><div class="theme"><div class="eyebrow">MAIN THEME</div><h3>経営問答シリーズ</h3><strong>詳細は決まり次第ご案内します。</strong></div><div class="actions"><a class="btn btn-secondary" href="schedule.html">今後の活動予定を見る →</a></div></div></div></div></section>'''
s=re.sub(r'<section id="next" class="next">.*?</section>\s*(?=<section id="about">)',oct_home+'\n',s,count=1,flags=re.S)
s=re.sub(r'<script type="application/ld\+json">\[\{"@context":"https://schema.org","@type":"Organization","name":"盛心実践会千葉","areaServed":"千葉県"\},\{"@context":"https://schema.org","@type":"Event".*?\}\]</script>','<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"盛心実践会千葉","areaServed":"千葉県"}</script>',s,count=1,flags=re.S)
p.write_text(s,encoding='utf-8')

# 4) Member portal: remove completed September meeting, add next meeting and archive access.
p=Path('member.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'<section><div class="wrap"><div class="section-title"><h2>次回の勉強会</h2>.*?</section>','',s,count=1,flags=re.S)
next_meeting='''<section><div class="wrap"><div class="section-title"><h2>次回の勉強会</h2><p>2026年10月27日（火）</p></div><article class="card" style="min-height:0"><div class="icon">📘</div><h3>10月度 合同勉強会｜経営問答シリーズ</h3><p>18:00〜21:00／グリーンセミナールーム。テーマ・内容などの詳細は決まり次第ご案内します。</p><a class="btn" href="schedule.html">活動予定を見る →</a></article></div></section>'''
if '10月度 合同勉強会｜経営問答シリーズ' not in s:
    s=s.replace('</main>',next_meeting+'</main>',1)
member_archive='''<section><div class="wrap"><div class="section-title"><h2>勉強会アーカイブ</h2><p>これまでの学びを振り返る</p></div><article class="card" style="min-height:0"><div class="icon">🗂️</div><h3>2026年9月度 合同自主例会</h3><p>経営12ヵ条 第4条「誰にも負けない努力をする」／フィロソフィ「ベクトルを揃える」。当日の内容・写真・資料をまとめています。</p><a class="btn" href="archive-2026-09.html#materials">9月例会の資料を見る →</a></article></div></section>'''
if '勉強会アーカイブ' not in s:
    s=s.replace('</main>',member_archive+'</main>',1)
p.write_text(s,encoding='utf-8')
