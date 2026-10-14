from pathlib import Path
import re

# Final golf signup update: runs after the existing event and map patches.
FORM = "https://chouseisan.com/s?h=932c92e4598a42ca8295b22751225003"
GOLF_MAP = "https://maps.app.goo.gl/5SmTDKeMMwVMqskP9"
DINNER_MAP = "https://maps.app.goo.gl/6PeCMToFKNsHWJ2M7"

def replace_one(text, pattern, replacement, label):
    result, n = re.subn(pattern, lambda _: replacement, text, count=1, flags=re.S)
    if n != 1:
        raise RuntimeError("Could not update " + label)
    return result

def link(label, css_class, extra=""):
    return f'<a class="{css_class}" href="{FORM}" target="_blank" rel="noopener noreferrer" {extra}>ゴルフコンペに申し込む（調整さん） →</a>'

def notes():
    return ('<p><strong>申込締切：11月16日（月）</strong><br>'
            '先着順受付（5組20名様）です。<br>'
            'お申し込みの際は、調整さんの<strong>コメント欄に平均スコア</strong>をご記入ください。</p>')

# Public activities page
p = Path("schedule.html")
s = p.read_text(encoding="utf-8")
s = replace_one(
    s, r'<h3>お申し込み</h3><div class="golf-contact">.*?</div>',
    '<h3>お申し込み（調整さん）</h3><div class="golf-contact">'
    + notes() + link("申込", "btn") + '</div>',
    "schedule golf signup")
s = s.replace('朝の受付時に集金します。', '当日、現金にて集金します。')
s = s.replace('各自フロントにてご精算ください。', '各自フロントにてご精算ください。')
s = s.replace(
    '<h3>懇親会場</h3>',
    '<h3>懇親会場</h3>', 1)
s = s.replace(
    '〒299-3241 千葉県大網白里市季美の森南2-49<br>TEL：0475-73-0109',
    f'〒299-3241 千葉県大網白里市季美の森南2-49<br>TEL：0475-73-0109<br><a href="{GOLF_MAP}" target="_blank" rel="noopener noreferrer">ゴルフ場の地図を見る →</a>', 1)
s = s.replace(
    '千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央</p>',
    f'千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央<br><a href="{DINNER_MAP}" target="_blank" rel="noopener noreferrer">懇親会場の地図を見る →</a></p>', 1)
s = s.replace(
    '</div></details></div></article><article class="event">',
    '</div></details></div></article><article class="event">', 1)
# Place an obvious signup button above the fold, before expanded details.
s = replace_one(
    s, r'(<div class="golf-quick">.*?</div></div></div>)(<details class="golf-details">)',
    lambda_placeholder := '<div class="golf-quick"><div><span>募集定員</span><strong>5組・20名（先着順）</strong></div><div><span>プレー費＋参加費</span><strong>14,800円＋5,000円</strong></div><div><span>申込締切</span><strong>11月16日（月）</strong></div></div>'
    + link("申込", "btn")
    + '<p style="font-size:13px">調整さんのコメント欄に平均スコアをご記入ください。</p><details class="golf-details">',
    "schedule golf primary button")
p.write_text(s, encoding="utf-8")

# Member portal
p = Path("member.html")
s = p.read_text(encoding="utf-8")
s = replace_one(
    s, r'<h4>お申し込み</h4><div class="member-golf-contact">.*?</div>',
    '<h4>お申し込み（調整さん）</h4><div class="member-golf-contact">'
    + notes() + link("申込", "btn") + '</div>',
    "member golf signup")
s = s.replace('（景品代／朝の受付時に集金）', '（景品代／当日現金にて集金）')
s = s.replace('（朝の受付時に集金）', '（当日現金にて集金）')
s = s.replace(
    '〒299-3241 千葉県大網白里市季美の森南2-49<br>TEL：0475-73-0109',
    f'〒299-3241 千葉県大網白里市季美の森南2-49<br>TEL：0475-73-0109<br><a href="{GOLF_MAP}" target="_blank" rel="noopener noreferrer">ゴルフ場の地図を見る →</a>', 1)
s = s.replace(
    '千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央</p>',
    f'千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央<br><a href="{DINNER_MAP}" target="_blank" rel="noopener noreferrer">懇親会場の地図を見る →</a></p>', 1)
s = replace_one(
    s, r'(<div class="member-event-quick">.*?</div></div></div>)(<details class="member-golf-details">)',
    '<div class="member-event-quick"><div><span>募集定員</span><strong>5組・20名</strong></div><div><span>プレー費＋参加費</span><strong>14,800円＋5,000円</strong></div><div><span>申込締切</span><strong>11月16日（月）</strong></div></div>'
    + link("申込", "btn")
    + '<p style="font-size:13px">調整さんのコメント欄に平均スコアをご記入ください。</p><details class="member-golf-details">',
    "member golf primary button")
p.write_text(s, encoding="utf-8")

# LINE menu participation page
p = Path("entry.html")
s = p.read_text(encoding="utf-8")
s = replace_one(
    s,
    r'<h3>申込方法</h3>.*?<div class="contact-actions">.*?</div>',
    '<h3>お申し込み（調整さん）</h3>' + notes()
    + link("申込", "button"),
    "LINE golf signup")
s = s.replace(
    '<h3>懇親会</h3><p>参加費：7,000円（朝の受付時に集金）',
    '<h3>懇親会</h3><p><strong>懇親会のみの参加も大歓迎です！</strong></p><p>参加費：7,000円（当日、現金にて集金）',
    1)
s = s.replace(
    '参加費：5,000円</strong>（景品代）',
    '参加費：5,000円</strong>（当日現金にて集金）', 1)
s = s.replace(
    'プレー費：14,800円</strong>（各自精算）',
    'プレー費：14,800円</strong>（各自フロントにて精算）', 1)
s = s.replace(
    '〒299-3241 千葉県大網白里市季美の森南2-49<br>TEL：0475-73-0109',
    f'〒299-3241 千葉県大網白里市季美の森南2-49<br>TEL：0475-73-0109<br><a href="{GOLF_MAP}" target="_blank" rel="noopener noreferrer">ゴルフ場の地図を見る →</a>', 1)
s = s.replace(
    '千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央</p>',
    f'千葉県千葉市中央区中央3丁目15-3 朝日プラザ千葉中央<br><a href="{DINNER_MAP}" target="_blank" rel="noopener noreferrer">懇親会場の地図を見る →</a></p>', 1)
s = s.replace(
    '<details class="details"><summary>ゴルフコンペの詳細・申込方法を見る',
    link("申込", "button") + '<p class="notice">11月16日（月）締切・先着5組20名。コメント欄に平均スコアをご記入ください。</p><details class="details"><summary>ゴルフコンペの詳細・申込方法を見る',
    1)
p.write_text(s, encoding="utf-8")
