from pathlib import Path

TALLY = "https://tally.so/r/LZeJ4G"
MAP_URL = "https://www.google.com/maps/search/?api=1&query=%E5%8D%83%E8%91%89%E7%9C%8C%E5%8D%83%E8%91%89%E5%B8%82%E4%B8%AD%E5%A4%AE%E5%8C%BA%E5%AF%8C%E5%A3%AB%E8%A6%8B2%E4%B8%81%E7%9B%AE8-14%20%E3%82%A8%E3%82%AD%E3%83%8B%E3%82%A2%E5%8D%83%E8%91%89"
MAP_EMBED = "https://www.google.com/maps?q=%E5%8D%83%E8%91%89%E7%9C%8C%E5%8D%83%E8%91%89%E5%B8%82%E4%B8%AD%E5%A4%AE%E5%8C%BA%E5%AF%8C%E5%A3%AB%E8%A6%8B2%E4%B8%81%E7%9B%AE8-14%20%E3%82%A8%E3%82%AD%E3%83%8B%E3%82%A2%E5%8D%83%E8%91%89&output=embed"

p = Path("index.html")
html = p.read_text(encoding="utf-8")

# 正式名称に統一
html = html.replace("心高会 佐倉", "心を高める経営を伸ばす会 佐倉")
html = html.replace("心高会　佐倉", "心を高める経営を伸ばす会 佐倉")

html = html.replace("https://forms.gle/R7KaSbq9iwH9X8Yq6", TALLY)
html = html.replace(
    ">この勉強会にオブザーバー参加する</a>",
    ">例会に参加する・出欠を登録する</a><p style=\"margin:10px 0 0;color:#74656a;font-size:14px\">会員・オブザーバー共通の申込フォームです。フォーム内で参加区分を選択してください。</p>"
)

poster_block = '''<div style="max-width:760px;margin:0 auto 24px;text-align:center"><img src="2026-09-meeting.png" alt="盛心実践会千葉・心を高める経営を伸ばす会佐倉 2026年9月度合同自主例会のご案内" style="display:block;width:100%;height:auto;border-radius:18px;box-shadow:0 12px 30px rgba(107,31,43,.12)"></div><div style="text-align:center;margin:0 0 22px"><a class="btn btn-primary" target="_blank" rel="noopener" href="https://tally.so/r/LZeJ4G">例会に参加する・出欠を登録する</a><p style="margin:10px 0 0;color:#74656a;font-size:14px">会員・オブザーバー共通の申込フォームです。フォーム内で参加区分を選択してください。</p></div><div style="margin:0 0 28px;padding:13px 16px;border-radius:14px;background:#f2e8ea;text-align:center;line-height:1.7"><strong>9月29日（火）18:00〜21:00</strong> <span style="color:#9b6a72;padding:0 8px">｜</span> <strong>グリーンセミナールーム</strong> <span style="color:#74656a">（千葉駅 徒歩約10分）</span></div>'''
marker = '<div class="event-body">'
if 'src="2026-09-meeting.png"' not in html and marker in html:
    html = html.replace(marker, marker + poster_block, 1)

html = html.replace('<div class="event-meta">', '<div class="event-meta" style="display:none">', 1)

old_theme = '''<div class="event-intro"><h3>今回のテーマ</h3><p><strong>稲盛経営12ヵ条　第4条「誰にも負けない努力をする」</strong><br>～地味な仕事を一歩一歩堅実に、弛まぬ努力を続ける～</p>'''
new_theme = '''<div class="event-intro"><div style="display:inline-block;margin-bottom:14px;padding:6px 14px;border-radius:999px;background:#6b1f2b;color:#fff;font-size:14px;font-weight:800;letter-spacing:.08em">今回のテーマ</div><div style="margin:0 0 8px;color:#2f2023;font-size:clamp(22px,2.7vw,34px);font-weight:900;line-height:1.45">稲盛経営12ヵ条 第4条<br><span style="color:#7b1f2b">「誰にも負けない努力をする」</span></div><p style="margin:0 0 22px;color:#5f5054;font-size:clamp(15px,1.5vw,18px);font-weight:700;line-height:1.7">～地味な仕事を一歩一歩堅実に、弛まぬ努力を続ける～</p>'''
html = html.replace(old_theme, new_theme, 1)

program_replacements = [
    ('<div class="program-item"><h3>第1部｜経営論「経営12ヵ条」</h3><p><strong>第4条　誰にも負けない努力をする</strong></p>', '<div class="program-item" style="padding:26px 28px;border:1px solid #ead6da;border-radius:20px;background:#fffaf9;box-shadow:0 8px 24px rgba(107,31,43,.05)"><div style="display:inline-block;margin-bottom:12px;padding:5px 12px;border-radius:999px;background:#6b1f2b;color:#fff;font-size:13px;font-weight:900;letter-spacing:.08em">第1部</div><h3 style="margin:0 0 14px;color:#2f2023;font-size:clamp(21px,2.2vw,29px);font-weight:900;line-height:1.45">経営論「経営12ヵ条」</h3><p style="margin:0 0 14px;color:#7b1f2b;font-size:clamp(17px,1.7vw,21px);font-weight:800"><strong>第4条　誰にも負けない努力をする</strong></p>'),
    ('<div class="program-item"><h3>第2部｜フィロソフィの紐解き</h3><p><strong>① ベクトルを合わせる</strong></p>', '<div class="program-item" style="padding:26px 28px;border:1px solid #ead6da;border-radius:20px;background:#fffaf9;box-shadow:0 8px 24px rgba(107,31,43,.05)"><div style="display:inline-block;margin-bottom:12px;padding:5px 12px;border-radius:999px;background:#6b1f2b;color:#fff;font-size:13px;font-weight:900;letter-spacing:.08em">第2部</div><h3 style="margin:0 0 14px;color:#2f2023;font-size:clamp(21px,2.2vw,29px);font-weight:900;line-height:1.45">フィロソフィの紐解き</h3><p style="margin:0 0 14px;color:#7b1f2b;font-size:clamp(17px,1.7vw,21px);font-weight:800"><strong>① ベクトルを合わせる</strong></p>'),
    ('<div class="program-item"><h3>第3部｜京セラ式コンパ</h3>', '<div class="program-item" style="padding:26px 28px;border:1px solid #ead6da;border-radius:20px;background:#fffaf9;box-shadow:0 8px 24px rgba(107,31,43,.05)"><div style="display:inline-block;margin-bottom:12px;padding:5px 12px;border-radius:999px;background:#6b1f2b;color:#fff;font-size:13px;font-weight:900;letter-spacing:.08em">第3部</div><h3 style="margin:0 0 14px;color:#2f2023;font-size:clamp(21px,2.2vw,29px);font-weight:900;line-height:1.45">京セラ式コンパ</h3>')
]
for old, new in program_replacements:
    html = html.replace(old, new, 1)

old_observer = '''<div class="event-intro"><h3>初めての方・オブザーバーの方へ</h3><p>塾生の皆さまはもちろん、オブザーバーの方、稲盛経営哲学を初めて学ぶ方もご参加いただけます。講話を視聴して終わるのではなく、参加した皆さんと意見を交わしながら、自分自身と自社の経営を見つめ直す例会です。</p></div>'''
new_observer = '''<div class="event-intro" style="padding:26px 28px;background:#fffaf9"><div style="display:inline-block;margin-bottom:12px;padding:5px 12px;border-radius:999px;background:#6b1f2b;color:#fff;font-size:13px;font-weight:900;letter-spacing:.08em">初めての方へ</div><h3 style="margin:0 0 14px;color:#2f2023;font-size:clamp(21px,2.2vw,29px);font-weight:900;line-height:1.45">オブザーバー参加について</h3><p style="margin:0;color:#66575b;line-height:1.9">塾生の皆さまはもちろん、オブザーバーの方、稲盛経営哲学を初めて学ぶ方もご参加いただけます。講話を視聴して終わるのではなく、参加した皆さんと意見を交わしながら、自分自身と自社の経営を見つめ直す例会です。</p></div>'''
html = html.replace(old_observer, new_observer, 1)

old_fee = '''<div class="fee-box"><strong>参加費</strong><br>塾生：無料 ／ 塾生の従業員：3,000円 ／ オブザーバー：5,000円<br>※当日会場にて集金・コンパ費用込み</div>'''
new_fee = '''<div class="fee-box" style="padding:26px 28px;border-radius:20px"><div style="margin-bottom:18px;color:#2f2023;font-size:clamp(21px,2.2vw,28px);font-weight:900">参加費</div><div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px"><div style="padding:16px;border-radius:14px;background:#fff;text-align:center"><div style="font-weight:800;color:#66575b">塾生</div><div style="margin-top:5px;color:#7b1f2b;font-size:22px;font-weight:900">無料</div></div><div style="padding:16px;border-radius:14px;background:#fff;text-align:center"><div style="font-weight:800;color:#66575b">オブザーバー</div><div style="margin-top:5px;color:#7b1f2b;font-size:22px;font-weight:900">5,000円</div></div></div><p style="margin:14px 0 0;color:#74656a;font-size:14px">※当日会場にて集金・コンパ費用込み</p></div>'''
html = html.replace(old_fee, new_fee, 1)

# 会場アクセス：地図は遅延読み込みし、スマホからGoogle Mapsへ直接開ける導線も用意
if 'class="venue-access"' not in html:
    access = f'''<div class="venue-access" style="margin:28px 0;padding:26px 28px;border:1px solid #ead6da;border-radius:20px;background:#fffaf9"><div style="display:inline-block;margin-bottom:12px;padding:5px 12px;border-radius:999px;background:#6b1f2b;color:#fff;font-size:13px;font-weight:900;letter-spacing:.08em">会場アクセス</div><h3 style="margin:0 0 8px;color:#2f2023;font-size:clamp(21px,2.2vw,29px);font-weight:900">グリーンセミナールーム</h3><p style="margin:0 0 16px;color:#66575b;line-height:1.8">千葉県千葉市中央区富士見2丁目8-14 エキニア千葉4F</p><div style="overflow:hidden;border-radius:16px;border:1px solid #ead6da;background:#eee"><iframe title="グリーンセミナールーム 会場地図" src="{MAP_EMBED}" width="100%" height="300" style="display:block;border:0" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div><div style="text-align:center;margin-top:16px"><a class="btn btn-primary" href="{MAP_URL}" target="_blank" rel="noopener">Googleマップで開く</a></div></div>'''
    fee_marker = '<div class="fee-box" style="padding:26px 28px;border-radius:20px">'
    pos = html.find(fee_marker)
    if pos != -1:
        # Insert access card immediately before the participation fee card.
        html = html[:pos] + access + html[pos:]

old_bottom = '<div class="event-actions"><a class="btn btn-primary" target="_blank" rel="noopener" href="https://tally.so/r/LZeJ4G">例会に参加する・出欠を登録する</a><p style="margin:10px 0 0;color:#74656a;font-size:14px">会員・オブザーバー共通の申込フォームです。フォーム内で参加区分を選択してください。</p></div>'
html = html.replace(old_bottom, '', 1)
html = html.replace('href="#observer">まずはオブザーバー参加</a>', f'href="{TALLY}" target="_blank" rel="noopener">まずはオブザーバー参加</a>')

p.write_text(html, encoding="utf-8")

lp = Path("chiba-keieisha-benkyokai.html")
if lp.exists():
    lhtml = lp.read_text(encoding="utf-8")
    lhtml = lhtml.replace("https://forms.gle/R7KaSbq9iwH9X8Yq6", TALLY)
    lhtml = lhtml.replace("心高会 佐倉", "心を高める経営を伸ばす会 佐倉")
    lhtml = lhtml.replace("心高会　佐倉", "心を高める経営を伸ばす会 佐倉")
    lhtml = lhtml.replace(">この勉強会にオブザーバー参加する</a>", ">例会に参加する・出欠を登録する</a>")
    lp.write_text(lhtml, encoding="utf-8")
