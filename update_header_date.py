# -*- coding: utf-8 -*-
"""
PostToolUse hook: index.html を編集したとき、ヘッダーの更新日を自動で今日の日付に更新する。
Claude Code の hooks.PostToolUse（matcher: Edit|Write）から stdin で JSON を受け取る。

・書き込み先は「実際に編集されたファイル」から決める（絶対パスを埋め込まない）。
  複数PC運用のため、PCごとに違うclone先でもそのまま動く。
・更新するのは更新日の部分だけ。件数（補助金N件・助成金M件）は書き換えない。
"""
import sys
import json
import os
import re

try:
    sys.stdin.reconfigure(encoding='utf-8')
except Exception:
    pass

try:
    data = json.load(sys.stdin)
    target = data.get('tool_input', {}).get('file_path', '')

    # index.html を編集したときだけ動く
    if os.path.basename(target).lower() != 'index.html':
        sys.exit(0)
    if not os.path.isfile(target):
        sys.exit(0)

    from datetime import date

    with open(target, 'r', encoding='utf-8') as f:
        html = f.read()

    d = date.today()
    new_html, n = re.subn(
        r'(更新日：)\d{4}/\d{1,2}/\d{1,2}',
        lambda m: f'{m.group(1)}{d.year}/{d.month}/{d.day}',
        html,
    )

    if n and new_html != html:
        with open(target, 'w', encoding='utf-8') as f:
            f.write(new_html)

except Exception:
    pass  # エラーが起きても Claude の作業を止めない
