# -*- coding: utf-8 -*-
"""
PostToolUse hook: このプロジェクトの index.html を編集したときだけ、
ヘッダーの「更新日：」の日付を今日に書き換える。

- 編集対象がこのプロジェクトの index.html でなければ、何もせず終了する
  （他プロジェクトの index.ts などで誤発火しないようにするため）
- 書き換えるのは日付部分のみ。件数表記やHTML全体には触らない
"""
import sys
import json
import re
from pathlib import Path
from datetime import date

TARGET = (Path(__file__).resolve().parent / "index.html")

try:
    sys.stdin.reconfigure(encoding='utf-8')
except Exception:
    pass


def main():
    data = json.load(sys.stdin)
    file_path = data.get('tool_input', {}).get('file_path', '')
    if not file_path:
        return

    try:
        edited = Path(file_path).resolve()
    except Exception:
        return

    # このプロジェクトの index.html 以外は対象外
    if edited != TARGET:
        return
    if not TARGET.exists():
        return

    html = TARGET.read_text(encoding='utf-8')
    d = date.today()
    new_html, n = re.subn(
        r'(更新日：)\d{4}/\d{1,2}/\d{1,2}',
        r'\g<1>%d/%d/%d' % (d.year, d.month, d.day),
        html,
        count=1,
    )
    if n and new_html != html:
        TARGET.write_text(new_html, encoding='utf-8')


try:
    main()
except Exception:
    pass  # エラーが起きても Claude の作業を止めない
