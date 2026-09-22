from pathlib import Path
p=Path('entry.html')
s=p.read_text(encoding='utf-8')

# Remove obsolete online-participation wording.
s=s.replace('          オンライン参加あり\n','')

# Add compact expandable-detail styles.
if '.event-summary{' not in s:
    s=s.replace('    .button {', '''    .event-summary {\n      margin: 0 0 20px;\n      padding: 16px 18px;\n      border-radius: 14px;\n      background: #f3f8fc;\n      color: #234f70;\n      line-height: 1.8;\n    }\n    .event-summary strong { color: #0b416d; }\n    .fee-line { margin-top: 10px; font-weight: 700; color: #0b416d; }\n    .details {\n      margin: 0 0 20px;\n      border: 1px solid #dbe5ed;\n      border-radius: 14px;\n      overflow: hidden;\n      background: #fff;\n    }\n    .details summary {\n      cursor: pointer;\n      padding: 15px 17px;\n      list-style: none;\n      font-weight: 800;\n      color: #0b416d;\n      background: #f8fbfd;\n    }\n    .details summary::-webkit-details-marker { display: none; }\n    .details summary::after { content: "＋"; float: right; }\n    .details[open] summary::after { content: "−"; }\n    .details-body { padding: 4px 17px 18px; border-top: 1px solid #e5edf3; color: #49677e; line-height: 1.8; }\n    .details-body h3 { margin: 16px 0 5px; font-size: 16px; color: #0b416d; }\n    .details-body p { margin: 7px 0; }\n    .details-body ul { margin: 6px 0 10px; padding-left: 20px; }\n    .details-body li { margin: 5px 0; }\n    .time-block { margin: 14px 0; padding: 12px 14px; border-left: 4px solid #1477b8; background: #f6faff; border-radius: 0 10px 10px 0; }\n    .time-block h3 { margin-top: 0; }\n\n    .button {''',1)

sep_info='''        <div class="info">\n\n          2026年9月29日（火）18:00〜21:00<br>\n\n          グリーンセミナールーム<br>\n\n\n        </div>'''
sep_new='''        <div class="info">\n          2026年9月29日（火）18:00〜21:00<br>\n          グリーンセミナールーム（千葉市中央区）\n        </div>\n        <div class="event-summary">\n          <strong>経営12ヵ条 第4条「誰にも負けない努力をする」</strong><br>\n          第1部：誰にも負けない努力をする<br>\n          第2部：フィロソフィ「ベクトルを揃える」<br>\n          第3部：京セラ式コンパ\n          <div class="fee-line">参加費　塾生：無料 ／ オブザーバー：5,000円</div>\n        </div>\n        <details class="details">\n          <summary>詳しい内容・当日の進行を見る</summary>\n          <div class="details-body">\n            <p>講義を聞くだけではなく、自分自身や自社に置き換えて考えるグループディスカッションも行います。</p>\n            <div class="time-block"><h3>18:00～18:10　開会</h3><ul><li>経営12ヵ条チェックシート</li><li>勉強会の目的確認</li></ul></div>\n            <div class="time-block"><h3>18:10～19:30　第1部</h3><p><strong>経営12ヵ条 第4条「誰にも負けない努力をする」</strong></p><p>～地味な仕事を一歩一歩堅実に、弛まぬ努力を続ける～</p><ul><li>塾長は、なぜ誰にも負けない努力を続けることができたのか</li><li>「自分なりの努力」と「誰にも負けない努力」の違い</li><li>努力を続けるために大切なこと</li><li>経営者の本気の努力が、周囲にもたらすもの</li><li>従業員が自ら努力する会社にするために、経営者は何をすべきか</li></ul><p><strong>グループディスカッション</strong></p></div>\n            <div class="time-block"><h3>19:30～20:10　第2部</h3><p><strong>フィロソフィ「ベクトルを揃える」</strong></p><ul><li>なぜ、組織のベクトルを揃える必要があるのか</li><li>全員が同じ目的、同じ方向に向かうために大切なこと</li><li>経営者の思いを、どのように従業員へ伝えるのか</li><li>一人ひとりの努力を、組織の大きな力に変えるには</li></ul></div>\n            <div class="time-block"><h3>20:10～21:00　第3部</h3><p><strong>京セラ式コンパ</strong></p><p>「ベクトルを揃える」をテーマに、それぞれの経営・仕事での実践について本音で語り合います。</p></div>\n            <div class="time-block"><h3>21:00　閉会</h3></div>\n          </div>\n        </details>'''
if sep_info in s:
    s=s.replace(sep_info,sep_new,1)

world_info='''        <div class="info">\n\n          2026年11月18日（水）10:30〜<br>\n\n          国立京都国際会館\n\n        </div>'''
world_new='''        <div class="info">\n          2026年11月18日（水）10:30〜<br>\n          国立京都国際会館\n        </div>\n        <div class="event-summary">\n          <strong>世界中で稲盛経営哲学を学び、実践するソウルメイトが一堂に会する、年に一度の学びの場です。</strong>\n          <div class="fee-line">参加資格：正会員・会員企業の社員・ご家族</div>\n        </div>\n        <details class="details">\n          <summary>世界大会について詳しく見る</summary>\n          <div class="details-body">\n            <p>仲間の実践や体験から学び、互いに刺激を受けながら、経営者として、人として、さらに心を高める貴重な機会です。</p>\n            <h3>通常参加費</h3>\n            <p>リアル参加＋懇親会：25,000円<br>リアル参加のみ：17,000円<br>アーカイブ参加：14,000円</p>\n            <p>※盛心実践会千葉の塾生向け補助については、塾生専用ページのお知らせをご確認ください。</p>\n          </div>\n        </details>'''
if world_info in s:
    s=s.replace(world_info,world_new,1)

p.write_text(s,encoding='utf-8')
