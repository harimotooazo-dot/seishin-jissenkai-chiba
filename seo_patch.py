from pathlib import Path
import re, json

p = Path('index.html')
html = p.read_text(encoding='utf-8')

html = re.sub(r'<title>.*?</title>', '<title>盛心実践会千葉｜稲盛和夫の経営哲学を学ぶ千葉の経営者勉強会</title>', html, count=1)
html = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="盛心実践会千葉は、千葉で稲盛和夫氏の経営哲学・経営12ヶ条・京セラフィロソフィを学び、実際の経営に生かす経営者勉強会です。経営者・後継者・会社幹部・個人事業主が学び合い、初めての方は月例勉強会へオブザーバー参加できます。">', html, count=1)
html = re.sub(r'<meta name="keywords" content="[^"]*">', '<meta name="keywords" content="盛心実践会千葉,稲盛和夫,稲盛経営哲学,経営哲学,経営者勉強会,千葉,千葉市,経営12ヶ条,京セラフィロソフィ,アメーバ経営,後継者,会社幹部">', html, count=1)
html = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="盛心実践会千葉｜稲盛和夫の経営哲学を学ぶ千葉の経営者勉強会">', html, count=1)
html = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="千葉で稲盛経営哲学を学び、経営に実践する。経営者・後継者・会社幹部向け。初めての方はオブザーバー参加から。">', html, count=1)

if 'twitter:card' not in html:
    html = html.replace(
        '<meta property="og:url" content="https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/">',
        '<meta property="og:url" content="https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/">\n  <meta property="og:site_name" content="盛心実践会千葉">\n  <meta property="og:locale" content="ja_JP">\n  <meta name="twitter:card" content="summary_large_image">\n  <meta property="og:image" content="https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/hero_group.webp">'
    )

html = html.replace(
    '<h1>心を高め、<br>経営を伸ばす。</h1>',
    '<h1>心を高め、<br>経営を伸ばす。<span class="seo-h1-sub">千葉で稲盛経営哲学を学ぶ経営者勉強会</span></h1>'
)

css = '.seo-h1-sub{display:block;margin-top:16px;font-size:clamp(16px,1.7vw,22px);line-height:1.5;font-weight:700;color:#6b1f2b}.local-seo{background:linear-gradient(135deg,#fff,#f6edef);border:1px solid #e8dadd;border-radius:28px;padding:34px}.local-seo h2{margin:6px 0 12px;font-size:clamp(28px,3.6vw,42px)}.local-seo p{color:#74656a;margin-bottom:14px}.text-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}.text-links a{display:inline-flex;padding:9px 14px;border-radius:999px;border:1px solid #e8dadd;background:#fff;color:#6b1f2b;font-weight:800;font-size:14px}.event-intro{background:#fff8f9;border:1px solid #ead6da;border-radius:20px;padding:22px;margin:22px 0}.event-intro h3{margin-top:0}.event-points{margin:14px 0 0;padding-left:1.4em}.event-points li{margin:6px 0}'
if '.local-seo{' not in html:
    html = html.replace('footer{', css + 'footer{', 1)
elif '.event-intro{' not in html:
    html = html.replace('footer{', '.event-intro{background:#fff8f9;border:1px solid #ead6da;border-radius:20px;padding:22px;margin:22px 0}.event-intro h3{margin-top:0}.event-points{margin:14px 0 0;padding-left:1.4em}.event-points li{margin:6px 0}footer{', 1)

local_section = '''<section id="chiba"><div class="wrap"><div class="local-seo"><div class="eyebrow">CHIBA / MANAGEMENT STUDY GROUP</div><h2>千葉で、稲盛経営哲学を経営に生かす。</h2><p>盛心実践会千葉は、千葉県を中心に、経営者・後継者・会社幹部・個人事業主が稲盛和夫氏の経営哲学を学び、実際の会社経営に落とし込むための勉強会です。経営12ヶ条、京セラフィロソフィ、稲盛会計学、アメーバ経営などを題材に、講話視聴・経営体験発表・グループディスカッションを通じて学びを深めます。</p><p>「千葉で経営哲学を学べる場を探している」「経営者同士で本音の議論をしたい」「学びを自社の業績や社員の幸せにつなげたい」という方は、まずは月例勉強会へのオブザーバー参加からご体験ください。</p><div class="text-links"><a href="#next-event">次回の千葉開催勉強会を見る</a><a href="#learn">学べる内容を見る</a><a href="#join">オブザーバー参加・入会案内</a></div></div></div></section>'''
if 'id="chiba"' not in html:
    m = re.search(r'(<section id="about".*?</section>)', html, flags=re.S)
    if m:
        html = html[:m.end()] + local_section + html[m.end():]

if '<a href="#learn">学べること</a>' not in html:
    html = html.replace('<a href="#greeting">代表あいさつ</a>', '<a href="#greeting">代表あいさつ</a><a href="#learn">学べること</a>')

html = html.replace('alt="盛心実践会千葉の集合写真"', 'alt="千葉で稲盛経営哲学を学ぶ盛心実践会千葉の勉強会参加者"')

# 9月度合同自主例会を、初参加・オブザーバーにも内容が伝わるよう詳しく案内
new_event_section = '''<section id="next-event" class="next-event"><div class="wrap"><div class="event-card"><div class="event-head"><div class="event-date"><div>2026</div><div class="day">29</div><div>9月・火曜日</div></div><div><div class="eyebrow" style="color:#f0cbd2">NEXT MEETING</div><h2>盛心実践会千葉・心高会 佐倉<br>9月度 合同自主例会</h2><p>稲盛経営12ヵ条 第4条「誰にも負けない努力をする」を中心に、講話視聴と対話を通して、自分自身と自社の経営を見つめ直します。</p></div></div><div class="event-body"><div class="event-meta"><div class="meta"><strong>開催日時</strong><br>2026年9月29日（火）<br>18:00〜21:00</div><div class="meta"><strong>会場</strong><br>グリーンセミナールーム<br>千葉駅 徒歩約10分</div><div class="meta"><strong>住所</strong><br>〒260-0015<br>千葉県千葉市中央区富士見2丁目8-14 エキニア千葉4F</div></div><div class="event-intro"><h3>今回のテーマ</h3><p><strong>稲盛経営12ヵ条　第4条「誰にも負けない努力をする」</strong><br>～地味な仕事を一歩一歩堅実に、弛まぬ努力を続ける～</p><p>今回の経営12ヵ条は、第4条「誰にも負けない努力をする」を勉強します。稲盛塾長が言われているのは、「自分なりの努力」ではなく「誰にも負けない努力」です。どんなに偉大な仕事も、毎日の小さな努力の積み重ねからできています。</p><p>第4条は、とてもシンプルで分かりやすい言葉です。しかし、分かったつもりになりやすく、実際に続けることは簡単ではありません。そこで今回は、一本の講話だけではなく、第4条について稲盛塾長がさまざまな角度から話されている複数の講話を取り上げます。</p><ul class="event-points"><li>なぜ「誰にも負けない努力」が必要なのか</li><li>努力を続けるためには、どのような考え方が必要なのか</li><li>自分の努力は、本当に誰にも負けないと言えるのか</li></ul><p>複数の講話を通して第4条を多次元的に学び、自分自身と自社の経営に照らし合わせて考えます。</p></div><div class="program"><div class="program-item"><h3>第1部｜経営論「経営12ヵ条」</h3><p><strong>第4条　誰にも負けない努力をする</strong></p><p>複数の講話を視聴し、第4条の意味をさまざまな角度から学びます。その後、グループディスカッションを行い、自社での実践にどうつなげるかを考えます。</p></div><div class="program-item"><h3>第2部｜フィロソフィの紐解き</h3><p><strong>① ベクトルを合わせる</strong></p><p>「京セラフィロソフィをひもとくシリーズ」から、社員全員のベクトルを合わせ、力を一つにするためにはどうしたらよいのか。稲盛塾長の実体験をもとに、フィロソフィの根幹にある考え方を紐解いていきます。</p></div><div class="program-item"><h3>第3部｜京セラ式コンパ</h3><p>本音で語り合い、互いの心を高め合う「京セラ式コンパ」を実践します。勉強会の感想や自身の経営課題について、参加者同士で率直に語り合います。</p></div></div><div class="event-intro"><h3>初めての方・オブザーバーの方へ</h3><p>塾生の皆さまはもちろん、オブザーバーの方、稲盛経営哲学を初めて学ぶ方もご参加いただけます。講話を視聴して終わるのではなく、参加した皆さんと意見を交わしながら、自分自身と自社の経営を見つめ直す例会です。</p></div><div class="fee-box"><strong>参加費</strong><br>塾生：無料 ／ 塾生の従業員：3,000円 ／ オブザーバー：5,000円<br>※当日会場にて集金・コンパ費用込み</div><div class="event-actions"><a class="btn btn-primary" target="_blank" rel="noopener" href="https://forms.gle/R7KaSbq9iwH9X8Yq6">この勉強会にオブザーバー参加する</a></div></div></div></div></section>'''
html = re.sub(r'<section id="next-event" class="next-event">.*?</section>', new_event_section, html, count=1, flags=re.S)

schema = [
  {"@context":"https://schema.org","@type":"WebSite","name":"盛心実践会千葉","url":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/","inLanguage":"ja","description":"千葉で稲盛和夫氏の経営哲学を学び、経営に実践する経営者勉強会"},
  {"@context":"https://schema.org","@type":"Organization","name":"盛心実践会千葉","url":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/","image":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/hero_group.webp","description":"千葉で稲盛和夫氏の経営哲学、経営12ヶ条、京セラフィロソフィ等を学び、経営への実践を目指す経営者・後継者・会社幹部のための勉強会","areaServed":{"@type":"AdministrativeArea","name":"千葉県"},"email":"harimoto_te@oazo7.jp"},
  {"@context":"https://schema.org","@type":"Event","name":"2026年 盛心実践会千葉・心高会 佐倉 9月度合同自主例会","startDate":"2026-09-29T18:00:00+09:00","endDate":"2026-09-29T21:00:00+09:00","eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled","location":{"@type":"Place","name":"グリーンセミナールーム","address":{"@type":"PostalAddress","postalCode":"260-0015","addressRegion":"千葉県","addressLocality":"千葉市中央区","streetAddress":"富士見2丁目8-14 エキニア千葉4F","addressCountry":"JP"}},"organizer":{"@type":"Organization","name":"盛心実践会千葉","url":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/"},"description":"千葉市で開催する経営者勉強会。稲盛経営12ヵ条 第4条『誰にも負けない努力をする』を複数の講話から学び、フィロソフィ『ベクトルを合わせる』、グループディスカッション、京セラ式コンパを行う合同自主例会。初めての方・オブザーバー参加可。"},
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"初めてでも参加できますか？","acceptedAnswer":{"@type":"Answer","text":"はい。正式入会の前に、各月の勉強会へオブザーバーとしてご参加いただけます。"}},{"@type":"Question","name":"どのような方が参加していますか？","acceptedAnswer":{"@type":"Answer","text":"経営者、後継者、会社幹部、個人事業主など、規模や年齢を問わずさまざまな方が参加しています。"}},{"@type":"Question","name":"オンライン参加はできますか？","acceptedAnswer":{"@type":"Answer","text":"オンライン開催を行う回もあります。各勉強会の案内でご確認ください。"}}]}
]
html = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>', html, count=1, flags=re.S)

p.write_text(html, encoding='utf-8')

# SEOランディングページ側の次回例会案内も詳しくする
lp = Path('chiba-keieisha-benkyokai.html')
if lp.exists():
    lhtml = lp.read_text(encoding='utf-8')
    detailed_event = '''<section><div class="wrap"><div class="event"><div class="eyebrow" style="color:#f0cbd2">NEXT MEETING</div><h2>2026年9月29日（火）18:00〜21:00<br>盛心実践会千葉・心高会 佐倉 9月度合同自主例会</h2><p><strong>稲盛経営12ヵ条　第4条「誰にも負けない努力をする」</strong><br>～地味な仕事を一歩一歩堅実に、弛まぬ努力を続ける～</p><p>「自分なりの努力」ではなく「誰にも負けない努力」とは何か。今回は一本の講話だけでなく、複数の講話を通して、第4条をさまざまな角度から学びます。</p><div class="event-grid"><div class="event-box"><strong>第1部｜経営12ヵ条</strong><br>第4条「誰にも負けない努力をする」<br><small>なぜ努力が必要なのか、どうすれば続けられるのか、自分の努力は本当に誰にも負けないと言えるのかを考えます。</small></div><div class="event-box"><strong>第2部｜フィロソフィの紐解き</strong><br>① ベクトルを合わせる<br><small>社員全員のベクトルを合わせ、力を一つにするための考え方を稲盛塾長の実体験から学びます。</small></div></div><p><strong>第3部｜京セラ式コンパ</strong><br>勉強会の感想や自身の経営課題について、参加者同士で本音で語り合います。</p><p><strong>会場：</strong>グリーンセミナールーム<br>千葉県千葉市中央区富士見2丁目8-14 エキニア千葉4F（千葉駅から徒歩約10分）</p><p>塾生の方はもちろん、オブザーバーの方、稲盛経営哲学を初めて学ぶ方も参加できます。講話を聞くだけではなく、参加者と意見を交わしながら、自分自身と自社の経営を見つめ直す例会です。</p><p><strong>参加費：</strong>塾生 無料 ／ 塾生の従業員 3,000円 ／ オブザーバー 5,000円（コンパ費用込み）</p><div class="actions"><a class="btn" style="background:#fff;color:#6b1f2b" href="https://forms.gle/R7KaSbq9iwH9X8Yq6" target="_blank" rel="noopener">この勉強会にオブザーバー参加する</a></div></div></div></section>'''
    lhtml = re.sub(r'<section><div class="wrap"><div class="event">.*?</section>', detailed_event, lhtml, count=1, flags=re.S)
    lp.write_text(lhtml, encoding='utf-8')
