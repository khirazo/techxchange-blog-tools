# TechXchange ブログ変換ツール

このリポジトリには、MarkdownファイルをTechXchange Community用のHTMLに変換するツールが含まれています。

## 📋 目次

- [概要](#概要)
- [セットアップ](#セットアップ)
- [必要な環境](#必要な環境)
- [インストール](#インストール)
- [使い方](#使い方)
- [ワークフロー](#ワークフロー)
- [ファイル構成](#ファイル構成)
- [トラブルシューティング](#トラブルシューティング)

## 概要

このツールは以下の機能を提供します：

- ✅ Markdownから目次付きHTMLへの自動変換
- ✅ TechXchangeに適したクリーンなHTML出力（スタイル指定なし）
- ✅ 画像を明確なプレースホルダーに変換
- ✅ 各セクション末尾に「トップに戻る」リンクを自動追加
- ✅ Mac/Linux/WSL対応

## セットアップ

### リポジトリのクローン

```bash
# GitHubからクローン
git clone https://github.com/khirazo/techxchange-blog-tools.git

# ディレクトリに移動
cd techxchange-blog-tools
```

## 必要な環境

### 必須ツール

- **OS**: macOS, Linux, または Windows (WSL)
- **Pandoc**: 2.0以上
- **sed**: テキスト処理用（macOS/Linux/WSLに標準搭載）
- **awk**: テキスト処理用（macOS/Linux/WSLに標準搭載）

### 確認方法

```bash
# Pandocのバージョン確認
pandoc --version

# sed/awkの確認（通常は標準搭載）
which sed
which awk
```

**注意**: `sed`と`awk`はmacOS、Linux、WSLに標準でインストールされています。もし見つからない場合は、パッケージマネージャーでインストールしてください。

## インストール

### Pandocのインストール

#### macOS

```bash
brew install pandoc
```

#### Ubuntu/WSL

```bash
sudo apt-get update
sudo apt-get install pandoc
```

#### インストール確認

```bash
pandoc --version
```

バージョン情報が表示されればOKです。

## 使い方

### 基本的な使い方

```bash
# ブログディレクトリに移動
cd "GCM2使用方法1 CSVインポート"

# 変換実行（WSL環境の場合）
wsl bash path/to/techxchange-blog-tools/convert-simple.sh "GCM2使用方法1 CSVインポート.md"

# Mac/Linuxの場合
bash path/to/techxchange-blog-tools/convert-simple.sh "GCM2使用方法1 CSVインポート.md"
```

### 出力ファイル名を指定

```bash
wsl bash path/to/blog-tools/convert-simple.sh "記事.md" "techxchange.html"
```

## ワークフロー

### 1. Markdownでブログを作成

Bob/VSCode/TyporaなどでMarkdownファイルを作成します。

```markdown
# ブログタイトル

## セクション1

本文...

![スクリーンショット](media/image1.png)

## セクション2

本文...
```

### 2. HTMLに変換

```bash
# WSL環境
cd "ブログディレクトリ"
wsl bash path/to/techxchange-blog-tools/convert-simple.sh "記事.md"

# Mac/Linux環境
cd "ブログディレクトリ"
bash path/to/techxchange-blog-tools/convert-simple.sh "記事.md"
```

### 3. 生成されたHTMLを確認

ブラウザで開いて以下を確認：
- ✅ 目次が正しく生成されている
- ✅ 見出しのリンクが動作する
- ✅ 画像プレースホルダーが表示されている
- ✅ 各セクションに「トップに戻る」リンクがある

### 4. TechXchangeに投稿

1. 生成されたHTMLファイルをテキストエディタで開く
2. 全内容をコピー
3. TechXchangeのHTMLエディタに貼り付け
4. 画像プレースホルダー（`[画像をここに挿入: ...]`）を見つけて、対応する画像をアップロード

## ファイル構成

```
techxchange-blog-tools/
├── README.md                  # このファイル
├── QUICKSTART.md              # クイックガイド
├── convert-simple.sh          # 変換スクリプト
├── .gitignore                 # Git除外設定
└── .gitattributes             # Git属性設定（LF改行）

ブログディレクトリ/
├── 記事.md                    # 執筆用Markdown
├── 記事.html                  # 生成されたHTML（TechXchange用）
└── media/                     # 画像ファイル
    ├── image1.png
    └── image2.png
```

## 画像の扱い

### Markdown作成時

通常通り画像を参照：

```markdown
![説明文](media/image1.png)
```

VSCodeのプレビューなどで画像が表示されます。

### HTML変換後

画像は以下のようなプレースホルダーに変換されます：

```html
<div class="image-placeholder">
<strong>[画像をここに挿入: media/image1.png]</strong>
<em>説明: 説明文</em>
</div>
```

TechXchangeでこのプレースホルダーを見つけて、対応する画像をアップロードしてください。

## 生成されるHTMLの特徴

### 目次

- 自動生成される目次（TOC）
- h1とh2レベルの見出しを含む
- クリック可能なリンク

### スタイル

- **カスタムスタイルなし**: 独自のCSS/フォント指定は一切なし
- **Pandoc最小限の属性のみ**: `class`属性のみ（`title`, `TOC`など）
- **TechXchange完全互換**: サイトのデフォルトスタイルに完全依存

### トップに戻るリンク

- 各h1セクションの末尾に自動追加
- `href="#"`で汎用的に実装（特定のセクション名に依存しない）
- 既存の「トップに戻る」リンクも自動的に統一

### 画像プレースホルダー

- `<div class="image-placeholder">`で明確に表示
- 画像パスと説明文を含む
- TechXchangeで手動アップロード時に識別しやすい

## トラブルシューティング

### Pandocが見つからない

**エラー:** `Pandocがインストールされていません`

**解決策:**
1. Pandocをインストール（上記参照）
2. ターミナルを再起動
3. `pandoc --version`で確認

### sed/awkが見つからない

**エラー:** `command not found: sed` または `command not found: awk`

**解決策:**

macOS/Linux/WSLには通常標準搭載されていますが、もし見つからない場合：

```bash
# Ubuntu/WSL
sudo apt-get install sed gawk

# macOS（通常は不要）
brew install gnu-sed gawk
```

### 変換エラーが発生する

**原因:** Markdownファイルの構文エラー

**解決策:**
- Markdownの構文を確認
- 特殊文字が正しくエスケープされているか確認

### 画像が表示されない（ローカルプレビュー時）

**原因:** 画像パスが相対パスで指定されている

**解決策:**
- VSCodeのMarkdownプレビューを使用
- または、ブラウザでHTMLを開く際に、ファイルの場所を正しく指定

### 目次が生成されない

**原因:** Markdownに見出し（`#`, `##`など）がない

**解決策:**
- 適切な見出しを追加
- 見出しレベルは`#`（h1）から`##`（h2）まで使用

### WSLでパスエラーが発生する

**原因:** Windowsパスに特殊文字（スペース、`#`など）が含まれる

**解決策:**
- ブログディレクトリ内で実行
- 相対パスを使用

## 使用例

### 例1: 基本的な変換

```bash
cd "GCM2使用方法1 CSVインポート"
wsl bash path/to/techxchange-blog-tools/convert-simple.sh "GCM2使用方法1 CSVインポート.md"
```

### 例2: 出力ファイル名を指定

```bash
cd "QSR OSS版紹介ブログ"
wsl bash path/to/techxchange-blog-tools/convert-simple.sh "QSR OSS版紹介ブログ.md" "techxchange-qsr.html"
```

### 例3: 複数のブログを一括変換

```bash
for dir in */; do
  if [ -f "$dir"/*.md ]; then
    cd "$dir"
    wsl bash path/to/techxchange-blog-tools/convert-simple.sh *.md
    cd ..
  fi
done
```

## ヒントとベストプラクティス

### Markdown作成時

1. **見出しを適切に使用**: h1とh2を使って構造化
2. **画像の説明文を記載**: altテキストを必ず書く
3. **コードブロックを活用**: シンタックスハイライトが適用される
4. **リンクを確認**: 内部リンクと外部リンクが正しく動作するか確認

### HTML変換後

1. **ブラウザで確認**: 変換後は必ずブラウザで表示を確認
2. **目次のリンクをテスト**: すべてのリンクが正しく動作するか確認
3. **画像プレースホルダーを確認**: すべての画像が変換されているか確認
4. **TechXchangeでプレビュー**: 投稿前に必ずプレビューで確認

### TechXchange投稿時

1. **HTML全体をコピー**: 生成されたHTMLファイルの全内容をコピー
2. **画像を順番にアップロード**: プレースホルダーの順番通りにアップロード
3. **最終確認**: 投稿前に全体を確認

## 技術仕様

### 使用しているツール

- **Pandoc**: Markdown→HTML変換
- **sed**: 画像とリンクの正規表現置換
- **awk**: セクション単位の処理と「トップに戻る」リンク追加

### 処理フロー

1. `sed`で画像をプレースホルダーに変換
2. `sed`で既存の「トップに戻る」リンクを統一
3. `awk`で各h1セクション末尾に「トップに戻る」リンクを追加
4. Pandocで目次付きHTMLに変換
5. `<body>`タグ内のコンテンツのみを抽出

## サポート

問題が発生した場合は、以下を確認してください：

1. Pandocのバージョン: `pandoc --version`
2. sed/awkの存在確認: `which sed`, `which awk`
3. 入力ファイルのエンコーディング: UTF-8であることを確認
4. エラーメッセージの全文をコピー

## ライセンス

このツールはIBM Data Security Communityブログ作成用に作成されました。