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

css = '.seo-h1-sub{display:block;margin-top:16px;font-size:clamp(16px,1.7vw,22px);line-height:1.5;font-weight:700;color:#6b1f2b}.local-seo{background:linear-gradient(135deg,#fff,#f6edef);border:1px solid #e8dadd;border-radius:28px;padding:34px}.local-seo h2{margin:6px 0 12px;font-size:clamp(28px,3.6vw,42px)}.local-seo p{color:#74656a;margin-bottom:14px}.text-links{display:flex;gap:10px;flex-wrap:wrap;margin-top:18px}.text-links a{display:inline-flex;padding:9px 14px;border-radius:999px;border:1px solid #e8dadd;background:#fff;color:#6b1f2b;font-weight:800;font-size:14px}'
if '.local-seo{' not in html:
    html = html.replace('footer{', css + 'footer{', 1)

local_section = '''<section id="chiba"><div class="wrap"><div class="local-seo"><div class="eyebrow">CHIBA / MANAGEMENT STUDY GROUP</div><h2>千葉で、稲盛経営哲学を経営に生かす。</h2><p>盛心実践会千葉は、千葉県を中心に、経営者・後継者・会社幹部・個人事業主が稲盛和夫氏の経営哲学を学び、実際の会社経営に落とし込むための勉強会です。経営12ヶ条、京セラフィロソフィ、稲盛会計学、アメーバ経営などを題材に、講話視聴・経営体験発表・グループディスカッションを通じて学びを深めます。</p><p>「千葉で経営哲学を学べる場を探している」「経営者同士で本音の議論をしたい」「学びを自社の業績や社員の幸せにつなげたい」という方は、まずは月例勉強会へのオブザーバー参加からご体験ください。</p><div class="text-links"><a href="#next-event">次回の千葉開催勉強会を見る</a><a href="#learn">学べる内容を見る</a><a href="#join">オブザーバー参加・入会案内</a></div></div></div></section>'''
if 'id="chiba"' not in html:
    m = re.search(r'(<section id="about".*?</section>)', html, flags=re.S)
    if m:
        html = html[:m.end()] + local_section + html[m.end():]

if '<a href="#learn">学べること</a>' not in html:
    html = html.replace('<a href="#greeting">代表あいさつ</a>', '<a href="#greeting">代表あいさつ</a><a href="#learn">学べること</a>')

html = html.replace('alt="盛心実践会千葉の集合写真"', 'alt="千葉で稲盛経営哲学を学ぶ盛心実践会千葉の勉強会参加者"')

schema = [
  {"@context":"https://schema.org","@type":"WebSite","name":"盛心実践会千葉","url":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/","inLanguage":"ja","description":"千葉で稲盛和夫氏の経営哲学を学び、経営に実践する経営者勉強会"},
  {"@context":"https://schema.org","@type":"Organization","name":"盛心実践会千葉","url":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/","image":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/hero_group.webp","description":"千葉で稲盛和夫氏の経営哲学、経営12ヶ条、京セラフィロソフィ等を学び、経営への実践を目指す経営者・後継者・会社幹部のための勉強会","areaServed":{"@type":"AdministrativeArea","name":"千葉県"},"email":"harimoto_te@oazo7.jp"},
  {"@context":"https://schema.org","@type":"Event","name":"2026年 盛心実践会千葉・心高会 佐倉 9月度合同自主例会","startDate":"2026-09-29T18:00:00+09:00","endDate":"2026-09-29T21:00:00+09:00","eventAttendanceMode":"https://schema.org/OfflineEventAttendanceMode","eventStatus":"https://schema.org/EventScheduled","location":{"@type":"Place","name":"グリーンセミナールーム","address":{"@type":"PostalAddress","postalCode":"260-0015","addressRegion":"千葉県","addressLocality":"千葉市中央区","streetAddress":"富士見2丁目8-14 エキニア千葉4F","addressCountry":"JP"}},"organizer":{"@type":"Organization","name":"盛心実践会千葉","url":"https://harimotooazo-dot.github.io/seishin-jissenkai-chiba/"},"description":"千葉市で開催する経営者勉強会。経営12ヶ条 第4条『誰にも負けない努力をする』、フィロソフィーに学ぶ、京セラ式コンパを行う合同自主例会。"},
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"初めてでも参加できますか？","acceptedAnswer":{"@type":"Answer","text":"はい。正式入会の前に、各月の勉強会へオブザーバーとしてご参加いただけます。"}},{"@type":"Question","name":"どのような方が参加していますか？","acceptedAnswer":{"@type":"Answer","text":"経営者、後継者、会社幹部、個人事業主など、規模や年齢を問わずさまざまな方が参加しています。"}},{"@type":"Question","name":"オンライン参加はできますか？","acceptedAnswer":{"@type":"Answer","text":"オンライン開催を行う回もあります。各勉強会の案内でご確認ください。"}}]}
]
html = re.sub(r'<script type="application/ld\+json">.*?</script>', '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>', html, count=1, flags=re.S)

p.write_text(html, encoding='utf-8')
