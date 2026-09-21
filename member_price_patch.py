from pathlib import Path

p = Path('member.html')
html = p.read_text(encoding='utf-8')

html = html.replace(
    '.subsidy-item span{display:block;color:var(--muted);font-size:13px;font-weight:800}.subsidy-item strong{display:block;margin-top:3px;color:var(--deep);font-size:21px}',
    '.subsidy-item span{display:block;color:var(--muted);font-size:13px;font-weight:800}.regular-price{display:block;margin-top:6px;color:#8a7a7f;font-size:13px}.regular-price s{font-weight:700}.price-arrow{display:block;color:#9b6a72;font-size:12px;line-height:1.2}.subsidy-item strong{display:block;margin-top:1px;color:var(--deep);font-size:21px}.subsidy-item strong small{font-size:11px;margin-right:4px;color:#9b6a72}'
)

html = html.replace(
    '<div class="subsidy-grid"><div class="subsidy-item"><span>リアル参加＋懇親会</span><strong>10,000円</strong></div><div class="subsidy-item"><span>リアル参加のみ</span><strong>5,000円</strong></div><div class="subsidy-item"><span>アーカイブ参加</span><strong>3,000円</strong></div></div>',
    '<div class="subsidy-grid"><div class="subsidy-item"><span>リアル参加＋懇親会</span><div class="regular-price">通常 <s>25,000円</s></div><div class="price-arrow">↓</div><strong><small>実質</small>10,000円</strong></div><div class="subsidy-item"><span>リアル参加のみ</span><div class="regular-price">通常 <s>17,000円</s></div><div class="price-arrow">↓</div><strong><small>実質</small>5,000円</strong></div><div class="subsidy-item"><span>アーカイブ参加</span><div class="regular-price">通常 <s>14,000円</s></div><div class="price-arrow">↓</div><strong><small>実質</small>3,000円</strong></div></div>'
)

p.write_text(html, encoding='utf-8')
