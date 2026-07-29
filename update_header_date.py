# -*- coding: utf-8 -*-
"""
PostToolUse hook: index.html を編集したとき、ヘッダーの更新日を自動で今日の日付に更新する。
Claude Code の hooks.PostToolUse（matcher: Edit|Write）から stdin で JSON を受け取る。
"""
import sys
import json

try:
    sys.stdin.reconfigure(encoding='utf-8')
except Exception:
    pass

try:
    data = json.load(sys.stdin)
    file_path = data.get('tool_input', {}).get('file_path', '')

    if 'index' not in file_path:
        sys.exit(0)

    from bs4 import BeautifulSoup
    from datetime import date

    target = r'C:\Users\Iseyama-67\OneDrive - 伊勢山会計\デスクトップ\Claude-work\ミライズ_LINEモックアップ\index.html'

    with open(target, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    el = soup.select_one('.header-sub')
    if el:
        d = date.today()
        el.string = f'補助金11件・助成金6件 ｜ 更新日：{d.year}/{d.month}/{d.day}'
        with open(target, 'w', encoding='utf-8') as f:
            f.write(str(soup))

except Exception:
    pass  # エラーが起きても Claude の作業を止めない
