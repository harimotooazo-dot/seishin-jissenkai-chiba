from pathlib import Path
import re

# 1) Activity schedule: remove September from upcoming events and add a past-activity archive.
p=Path('schedule.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'<article class="event">(?:(?!<article class="event">).)*?9月度 合同自主例会(?:(?!<article class="event">).)*?</article>','',s,count=1,flags=re.S)
archive='''<div style="margin:46px 0 18px"><div class="eyebrow">PAST ACTIVITIES</div><h2 style="margin:6px 0 8px">過去の活動</h2><p style="color:var(--muted);margin:0 0 18px">終了した勉強会・例会の学びと当日の様子を残しています。</p></div><article class="event"><div class="event-head"><div class="date">2026年9月29日（火）開催</div><h2>9月度 合同自主例会</h2></div><img src="2026-09-meeting-wide.png" alt="9月度 合同自主例会"><div class="body"><div class="theme">経営12ヵ条 第4条「誰にも負けない努力をする」</div><p>講話・グループディスカッション、フィロソフィ「ベクトルを揃える」、京セラ式コンパを通じて学びを深めました。</p><a class="btn" href="archive-2026-09.html">開催レポート・写真を見る →</a></div></article>'''
if 'PAST ACTIVITIES' not in s:
    s=s.replace('<div class="info">',archive+'<div class="info">',1)
p.write_text(s,encoding='utf-8')

# 2) LINE entry page: completed event is no longer shown under current applications.
p=Path('entry.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'\s*<section class="event" id="september">.*?</section>\s*','\n',s,count=1,flags=re.S)
p.write_text(s,encoding='utf-8')

# 3) Homepage: replace the completed September meeting with the next major event.
p=Path('index.html')
s=p.read_text(encoding='utf-8')
world='''<section id="next" class="next"><div class="wrap"><div class="section-title"><div class="eyebrow">UPCOMING EVENT</div><h2>次の主な活動</h2></div><div class="event"><div class="event-head"><div>2026年11月18日（水）10:30〜</div><h2>第六回 心を高める 経営を伸ばす 世界大会</h2></div><div class="event-body"><img src="2026-11-world-convention.png" alt="第六回 心を高める 経営を伸ばす 世界大会" style="width:100%;display:block;border-radius:18px;margin-bottom:22px"><div class="theme"><div class="eyebrow">WORLD CONVENTION</div><h3>国立京都国際会館</h3><strong>世界中のソウルメイトが一堂に会する、一年に一度の学びの場</strong></div><div class="fee"><strong>参加資格</strong>　正会員・会員企業の社員・ご家族</div><div class="actions"><a class="btn btn-primary" href="entry.html#world">世界大会の詳細・申込を見る</a><a class="btn btn-secondary" href="schedule.html">今後の活動予定を見る →</a></div></div></div></div></section>'''
s=re.sub(r'<section id="next" class="next">.*?</section>\s*(?=<section id="about">)',world+'\n',s,count=1,flags=re.S)
# Remove stale September Event structured data while keeping Organization schema.
s=re.sub(r'<script type="application/ld\+json">\[\{"@context":"https://schema.org","@type":"Organization","name":"盛心実践会千葉","areaServed":"千葉県"\},\{"@context":"https://schema.org","@type":"Event".*?\}\]</script>','<script type="application/ld+json">{"@context":"https://schema.org","@type":"Organization","name":"盛心実践会千葉","areaServed":"千葉県"}</script>',s,count=1,flags=re.S)
p.write_text(s,encoding='utf-8')

# 4) Member portal: remove completed meeting from 'next meeting' and add archive access.
p=Path('member.html')
s=p.read_text(encoding='utf-8')
s=re.sub(r'<section><div class="wrap"><div class="section-title"><h2>次回の勉強会</h2>.*?</section>','',s,count=1,flags=re.S)
member_archive='''<section><div class="wrap"><div class="section-title"><h2>勉強会アーカイブ</h2><p>これまでの学びを振り返る</p></div><article class="card" style="min-height:0"><div class="icon">🗂️</div><h3>2026年9月度 合同自主例会</h3><p>経営12ヵ条 第4条「誰にも負けない努力をする」／フィロソフィ「ベクトルを揃える」。当日の内容と写真をまとめています。</p><a class="btn" href="archive-2026-09.html">開催レポート・写真を見る →</a></article></div></section>'''
if '勉強会アーカイブ' not in s:
    s=s.replace('</main>',member_archive+'</main>',1)
p.write_text(s,encoding='utf-8')
