from pathlib import Path
import re

p = Path("index.html")
html = p.read_text(encoding="utf-8")

# 会場はイベントごとに異なるため、トップページ下部の固定「会場アクセス」は表示しない。
html = re.sub(
    r'<section id="access">.*?</section>',
    '',
    html,
    count=1,
    flags=re.S,
)

# 次回勉強会カード内には participation_patch.py でイベント固有の会場・地図を表示するため、
# 固定アクセス欄へ飛ぶ旧ボタンは削除する。
html = html.replace(
    '<a class="btn btn-secondary" href="#access">会場アクセスを見る</a>',
    ''
)

p.write_text(html, encoding="utf-8")
