# ミライズ LINE モックアップ プロジェクト

---

## 【プロジェクト①】補助金検索ページ（index.html）

税理士事務所向け補助金顧問サービス（月額3万円）のLINE機能内「国の補助金情報ページ」のモックアップ。
補助金に詳しくない一般事業主が直感的に探せるスマホ縦型ページ。

### メインファイル
- **`index.html`**（旧名：kokuho_finder.html）
- カード構成：補助金11件・助成金6件　計17件

### GitHub・公開
| 項目 | 内容 |
|---|---|
| GitHubアカウント | mato6627-cpu |
| GitHubリポジトリ | https://github.com/mato6627-cpu/- |
| 公開URL | https://hojokin-finder.pages.dev |
| デプロイ | GitHub push → Cloudflare Pages 自動反映（1〜2分） |

**共有するURLは必ず `https://hojokin-finder.pages.dev`（固定URL）を使うこと。**

### Git操作
```bash
# 初回セットアップ（新PCの場合）
git init
git remote add origin https://mato6627-cpu:[トークン]@github.com/mato6627-cpu/-
git config user.name "mato6627-cpu"
git config user.email "mato6627@gmail.com"
git branch -M main
git fetch origin
git merge origin/main --allow-unrelated-histories -X ours -m "Initial setup"

# 通常のアップロード
git add index.html
git commit -m "変更内容の説明"
git push origin main

# pushが弾かれた場合
git pull origin main --no-rebase
git push origin main
```

### 自動化（PostToolUseフック）
`index.html` を編集するたびにヘッダーの更新日を自動で今日の日付に書き換える。

#### settings.json に追加する内容
`C:\Users\[ユーザー名]\.claude\settings.json` に以下を追加：
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python \"C:\\Users\\[ユーザー名]\\OneDrive - 伊勢山会計\\デスクトップ\\Claude-work\\ミライズ_LINEモックアップ\\update_header_date.py\""
          }
        ]
      }
    ]
  }
}
```
※ スクリプト本体は `update_header_date.py` として同フォルダに保存済み。

### デザイン仕様
- LINEブランドカラー（#06C755）
- スマホ縦型（max-width: 480px）
- カテゴリーグリッド（2列）→ ステータスフィルター → カード一覧
- 相談受付中バッジ：オレンジ（#f97316）＋点滅アニメーション
- 🔥人気バッジ：省力化・持続化の2件（ゴールド）
- カード展開で「こんな会社に向いています」→対象経費→補助額→スケジュール→公式リンク

### カード構成（17件）
**補助金 11件**
- 🤖 省力化投資補助金
- 📣 小規模事業者持続化補助金
- 🏭 新事業進出・ものづくり補助金（2026年統合）
- ⚙️ ものづくり補助金（公募終了）
- 🚀 新事業進出補助金
- 💻 デジタル化・AI導入補助金
- 🤝 事業承継・M&A補助金
- 📈 中小企業成長加速化補助金
- 🏗️ 大規模成長投資補助金
- 🌿 省エネ・非化石転換補助金
- 👴 エイジフレンドリー補助金

**助成金 6件**
- キャリアアップ助成金
- 業務改善助成金
- 働き方改革推進支援助成金
- 両立支援等助成金
- 65歳超雇用推進助成金
- 人材開発支援助成金

### 週次LINE配信ルール
- 毎週1回、LINE公式アカウントから補助金情報を配信
- **売り込みNG・情報提供スタンス**
- **締切まで1か月以内の補助金は紹介しない**
- 1回1補助金にフォーカス

#### 配信テンプレート
```
📅【今週の補助金情報】

[補助金名]（[回次]）
締切：[日付]
⚠️ 事業計画書の作成に[期間]かかります
　 → 今から動き始める必要があります

━━━━━━━━━━━━
こういう方に関係する補助金です

・[対象者1]
・[対象者2]
・[対象者3]
━━━━━━━━━━━━
主な支援枠

🔹 [枠名]
　[対象経費の説明]
　補助額：[金額]

※補助率はいずれも[補助率]

詳しい条件・スケジュールはこちら👇
https://hojokin-finder.pages.dev
```

#### 配信履歴
| 配信日 | 補助金 | 締切 |
|---|---|---|
| 2026/5月下旬 | 事業承継・M&A補助金 | 7月24日 |
| 2026/5月下旬 | 省力化投資補助金 | 7月下旬 |

---

## 【プロジェクト②】補助金で買えるもの図鑑（kaerumono）

税理士事務所（ミライズ会計事務所）の補助金有料サービスの一機能として、LINEで「補助金で買えるもの」を業種別に視覚的に紹介する画面。
ターゲット：税理士事務所職員 + 一般事業主（補助金に詳しくない人）。

**完成版リファレンス**: `kensetsu_kaerumono.html`（建設業・解体業版）。

### ファイル一覧
- `kaerumono_index.html` ← トップページ（業種選択画面）
- `kensetsu_kaerumono.html` ← マスター参考ファイル（建設業・解体業）
- `seizou_kaerumono.html` ← 製造業版
- `unsou_kaerumono.html` ← 運送業版
- `inshoku_kaerumono.html` ← 飲食業版
- `kouri_kaerumono.html` ← 小売業版
- `biyou_kaerumono.html` ← 美容業版
- `kaigo_kaerumono.html` ← 介護福祉業版
- `iryou_kaerumono.html` ← 医療業版

### 公開URL
- `https://hojokin-finder.pages.dev/kaerumono_index.html`

### デザインルール
- 単一HTML（CSS/JS/データ全てインライン）。LINE内ブラウザで即表示。
- 最大幅 `max-width: 480px`
- **各カテゴリの設備数は偶数**（2列グリッドのため）
- モーダルに外部リンクは入れない
- 「採択率○○%」などの煽り文は入れない
- 「申請から発注まで約6か月」の早め準備喚起は必ず入れる
- 監修：ミライズ会計事務所 を必ず入れる
- IT導入ではなく「AI導入」と表記
- 新事業進出補助金はフィルタに入れない
