# ミライズ会計事務所｜LINE「補助金で買えるもの図鑑」プロジェクト

税理士事務所（ミライズ会計事務所）の補助金有料サービスの一機能として、LINEで「補助金で買えるもの」を業種別に視覚的に紹介する画面。
ターゲット：税理士事務所職員 + 一般事業主（補助金に詳しくない人）。

**完成版リファレンス**: `kensetsu_kaerumono.html`（建設業・解体業版）。
他業種を追加する場合は、このファイルの構造・トーン・補助金マスタをそのまま流用し、データ部分（CATEGORIES配列）を入れ替える。

---

## 必須デザインパターン

### ファイル構成
- 単一HTML（CSS/JS/データ全てインライン）。LINE内ブラウザで即表示できる自己完結型。
- 最大幅 `max-width: 480px` で中央寄せ（LINE想定）。

### レイアウト要素（上から順）
1. **HEADER**（LINE緑グラデーション `#06C755→#00A546`）
   - アイコン絵文字（業種別） + 業種名｜補助金で買えるもの図鑑
   - サブ：業種固有の課題サマリ + 更新日
2. **業種スイッチャー**（ind-bar、横スクロール）
   - 現在の業種=active、他業種は`coming`クラスで「準備中」表示
3. **SUMMARY パネル**（白カード）
   - リード文：業種の課題（強調赤字） + 自己負担割合
   - 「💡 申請から発注可能まで約6か月かかります。早めの準備を。」（赤字必須）
   - **予算イメージ** / **補助率** の2タイル
   - 「使える主な補助金（タップでフィルタ）」チップ群
4. **FILTER BAR**（sticky、補助金別フィルタ）
5. **件数カウンタ**
6. **カテゴリ × カード**（後述）
7. **フッタ note**（※注意書き + 監修：ミライズ会計事務所）
8. **FAB**（⬆ トップへ戻る）
9. **モーダル**（カード詳細）

### カテゴリ設計（5前後）
建設業のパターン例：
- 🚜 基幹機械
- 🦾 自動化・省力化
- 📡 計測・現場把握
- 💻 ICT管理・DX
- 🏚️ 業種特化（解体業など）

他業種でも「基幹機械／自動化／計測／ICT管理／業種特化」の5枠で組むと収まりが良い。

### カード（item）
- グリッド 2列（mobile）
- 上から：絵文字（写真代替・大）/ 設備名 / 1行使い道 / 補助金タグ（色分け） / 価格目安
- 🔥人気バッジ（厳選した目玉設備に付与）
- **【必須】各カテゴリの設備数は偶数（4 / 6 / 8 / 10 / 12...）にする**。2列グリッドのため奇数だと右下に空白が出る。新規追加・削除の際もこのルールを必ず守る。

### モーダル（item詳細）
- 大きい絵文字 / 設備名 / カテゴリ / 「📝 こんな現場・課題に」（営業トーク用UC文）/ 「💰 価格イメージ」/ 「🎯 使える補助金」
- **モーダル内に外部リンクは入れない**（ユーザー指示）

---

## 補助金マスタ（SUBS）

```js
const SUBS = {
  shoryokuka:  { name: "省力化投資補助金", icon: "🤖", amt: "500万〜1億円・補助率1/2〜2/3" },
  monozukuri:  { name: "ものづくり補助金 / 新事業進出統合", icon: "⚙️", amt: "750万〜3,500万・補助率1/2〜2/3" },
  jizokuka:    { name: "小規模事業者持続化補助金", icon: "📣", amt: "50万〜250万・補助率2/3〜3/4" },
  it:          { name: "AI導入補助金", icon: "🤖", amt: "5万〜450万・補助率1/2〜4/5" },
  gyomukaizen: { name: "業務改善助成金（賃上げ＋設備）", icon: "💼", amt: "30万〜600万" },
};
```

- **フィルタに「新事業進出（shineigi）」は出さない**（ユーザー指示で削除済）
- 「IT導入」ではなく **「AI導入」** と表記する（ユーザー指示）
- 各設備の `subs` 配列で適合補助金を複数指定可

### 色割当（チップ）
- shoryokuka: オレンジ系（#fff3e8 / #b85a00）
- monozukuri: 赤系（#fff0f0 / #c0392b）
- jizokuka: 緑系（#f0faf4 / #00884a）
- it（AI導入）: 青系（#eef3ff / #2253c7）
- gyomukaizen: 紫系（#f3e8ff / #6d28d9）

---

## 文体・トーン

### 設備名 → 1行 desc
動詞で締め、定量化を入れる。例：
- 「丁張作業3名→0、若手で熟練レベル」
- 「結束時間1/3・腰痛者の現場復帰」
- 「左官2名→1名、施工速度2倍」

### uc（モーダルの「こんな現場・課題に」）
営業トークそのまま使える口語。「決定打」「主役」「定番」「鉄板」OK。
1段落・100〜180字を目安。`◯名×◯時間` の定量化を必ず入れる。

### 強調表現の禁止/推奨
- 「採択率○○%」「いま通りやすい」などの煽り文は **入れない**（ユーザー指示で削除済）
- 「申請から発注まで約6か月」の早め準備喚起は **必ず入れる**
- 監修：ミライズ会計事務所 を必ず入れる

---

## ユーザーフィードバック履歴（重要）

1. **当初の建設業PDF（48点）から重複・低需要を除外** → 34点へ
2. **2点しか残らないカテゴリは統合**（安全管理・資材管理→ICT・施工管理に統合）
3. **省力化投資補助金にフォーカスして20点抽出** → 既存ファイルに重複なしで8点追加
4. **採択率煽り文は不要**
5. **新事業進出フィルタは不要**
6. **IT導入 → AI導入** に統一
7. **モーダルからリンクは削除**
8. **フッタの「国の補助金一覧を見る」CTAは削除**
9. **高付加価値化カテゴリは削除**（インフラ点検ドローンは自動化・省力化へ移動）
10. **ICT管理は精鋭6点に絞る**（クラウド施工管理/写真管理/工程表/原価管理/現場安全/RFID）

---

## 他業種への横展開時のチェックリスト

新業種HTMLを作る際の確認項目：

- [ ] 業種スイッチャーで対象業種をactiveに
- [ ] HEADER 業種名・絵文字・サブ文を業種固有に
- [ ] SUMMARY のリード文を業種の課題で書き換え
- [ ] 予算イメージ・補助率は実態に合わせて調整
- [ ] CATEGORIES 配列の5カテゴリを業種に合わせて再構成
- [ ] 各設備に：v(絵文字) / name / desc / price / subs / popular / uc を設定
- [ ] 「申請から発注まで約6か月」「監修：ミライズ会計事務所」は必ず維持
- [ ] モーダルに外部リンクを入れない
- [ ] フッタにCTAボタンは入れない
- [ ] 新事業進出補助金はフィルタに入れない
- [ ] IT導入ではなくAI導入と表記
- [ ] 採択率の数字は文中に入れない（煽り回避）

---

## ファイル一覧

- `kensetsu_kaerumono.html` ← マスター参考ファイル（建設業・解体業）
- `seizou_kaerumono.html` ← 製造業版（6カテゴリ・50点）
- `unsou_kaerumono.html` ← 運送業版（5カテゴリ・40点）
- `inshoku_kaerumono.html` ← 飲食業版（6カテゴリ・48点）
- `kouri_kaerumono.html` ← 小売業版（6カテゴリ・36点）
- `kaerumono_index.html` ← **トップページ**（8業種選択画面・GitHub Pages配信時のエントリ）
- `biyou_kaerumono.html` ← 美容業版（6カテゴリ・32点）
- `kaigo_kaerumono.html` ← 介護福祉業版（4カテゴリ・28点）
- `iryou_kaerumono.html` ← 医療業版（5カテゴリ・32点・**PDFなしClaude生成**）
- `shoryokuka_kaerumono.html` ← 補助金別ページ試作（現状不使用、将来用に保管）
- 元素材：デスクトップの `..._建設業.pdf` / `..._製造業.pdf` / `..._運送業.pdf` / `..._飲食業.pdf` / `..._小売業.pdf` / `..._美容業.pdf` / `..._介護福祉業.pdf`（業種別カタログPDF）
- ※ 医療業はPDF素材なし → Claudeが業界知識から生成

---

## GitHub 公開設定

### リポジトリ
- URL: `https://github.com/mato6627-cpu/-`
- GitHub Pages URL: `https://mato6627-cpu.github.io/-/`
- Cloudflare Pages URL: `https://hojokin-finder.pages.dev/`
- LINEボタン用URL: `https://hojokin-finder.pages.dev/kaerumono_index.html`

### ローカルgit設定（初回セットアップ済）
```bash
# 作業ディレクトリ
C:\Users\Iseyama-67\OneDrive - 伊勢山会計\デスクトップ\Claude-work\ミライズ_LINE買えるものリスト\

# git初期設定（済）
git config --global user.name "mato6627-cpu"
git config --global user.email "mato6627@gmail.com"
git config --global credential.helper store
```

### 「Gitup」コマンド手順
ユーザーが「Gitup」と指示したら以下を実行：
```powershell
Set-Location "C:\Users\Iseyama-67\OneDrive - 伊勢山会計\デスクトップ\Claude-work\ミライズ_LINE買えるものリスト"
git add <変更ファイル>
git commit -m "<変更内容の日本語メッセージ>"
git push origin main
```
- 変更ファイルは `git status` で自動検出
- コミットメッセージは変更内容に合わせて自動生成
- push 後、Cloudflare Pages が自動でデプロイ（数分で反映）

## 新PC・PC紛失時の復元手順

HTMLファイル本体はすべてOneDriveに保存されているため消えない。
新PCで作業を再開する際は以下の手順を実行する。

### Step 1｜Gitのインストール確認
```powershell
git --version
# バージョンが表示されればOK。なければ https://git-scm.com からインストール
```

### Step 2｜グローバルgit設定（新PCで必須）
```powershell
git config --global user.name "mato6627-cpu"
git config --global user.email "mato6627@gmail.com"
git config --global credential.helper store
```

### Step 3｜GitHub PAT（アクセストークン）の発行
- 旧PCのPATは安全のため失効させ、新しいPATを発行する
- 発行場所: https://github.com/settings/tokens → "Fine-grained tokens" → "Generate new token"
- 設定内容：
  - Repository access: `mato6627-cpu/-` のみ
  - Permissions: Contents → Read and write
  - Expiration: 任意（長めに設定推奨）

### Step 4｜認証情報の保存
```powershell
# 以下のファイルを新PCの C:\Users\<ユーザー名>\.git-credentials に作成
# 内容（<PAT>は発行したトークンに置換）:
# https://mato6627-cpu:<PAT>@github.com
```
※ Claudeに「git credentials を設定して」と依頼すれば自動で作成してもらえる

### Step 5｜動作確認
```powershell
Set-Location "C:\Users\Iseyama-67\OneDrive - 伊勢山会計\デスクトップ\Claude-work\ミライズ_LINE買えるものリスト"
git status
git push origin main
# 認証エラーなくpushできればOK
```

### まとめ
| データ | 保存場所 | PC紛失時 |
|--------|----------|----------|
| HTMLファイル全て | OneDrive ✅ | 自動で復元 |
| .git フォルダ（履歴） | OneDrive ✅ | 自動で復元 |
| GitHub上のファイル | GitHub ✅ | 自動で復元 |
| git global config | 新PCのローカル ⚠️ | Step 2で再設定 |
| GitHub PAT（認証） | 新PCのローカル ⚠️ | Step 3〜4で再発行 |

---

## 新業種ページ追加時の作業手順

1. 業種PDFを `python -c "import pypdfium2..."` で画像化（scale=3.0、上下半分split推奨）
2. カテゴリ・設備名・説明文を抽出
3. `kensetsu_kaerumono.html` 全体をコピーして新ファイル作成
4. HEADER（業種名・絵文字・サブ文）と SUMMARY（リード文・予算）を業種固有に書き換え
5. `CATEGORIES` 配列を業種データに差替（カテゴリ5〜6、各6〜14点を目安）
6. **既存全ページのind-bar**で、新業種を `coming` から `<a href="新ファイル">` リンクに更新
7. CLAUDE.md のファイル一覧に追加
