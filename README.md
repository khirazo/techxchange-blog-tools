# TechXchange ブログ変換ツール

このリポジトリには、MarkdownファイルをTechXchange Community用のHTMLに変換するPythonツールが含まれています。

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
- ✅ 各h1/h2セクション末尾に「トップに戻る」リンクを自動追加
- ✅ Windows/Mac/Linux対応

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

- **Python**: 3.8以上
- **pip**: Pythonパッケージマネージャー

### 確認方法

```bash
# Pythonのバージョン確認
python --version
# または
python3 --version

# pipの確認
pip --version
# または
pip3 --version
```

## インストール

### 1. 依存関係のインストール

```bash
# リポジトリディレクトリで実行
pip install -r requirements.txt

# または、ユーザー環境にインストール（推奨）
pip install --user -r requirements.txt
```

**WSL Ubuntu 24.04以降の場合:**

システムPythonへの直接インストールが制限されているため、仮想環境を使用します：

```bash
# 仮想環境の作成（初回のみ）
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate

# 依存関係のインストール
pip install -r requirements.txt
```

### 2. インストール確認

```bash
# WSLの場合（仮想環境を有効化してから）
python convert.py --help

# Windows/Mac/Linuxの場合
python convert.py --help
```

ヘルプメッセージが表示されればOKです。

## 使い方

### 推奨: ラッパースクリプトを使用（最も簡単）

venvの有無を自動判定し、必要に応じてアクティベートしてから実行します。

```bash
# WSL/Linux/Mac環境
cd techxchange-blog-tools
./convert.sh "記事.md"

# 出力ファイル名を指定
./convert.sh "記事.md" "output.html"

# 別のディレクトリのファイルを変換
./convert.sh "../ブログディレクトリ/記事.md"

# ヘルプを表示
./convert.sh --help
```

**特徴:**
- ✅ venvの存在を自動チェック
- ✅ venvがあれば自動でアクティベート
- ✅ venvがなければシステムPythonを使用
- ✅ 毎回手動でvenvをアクティベートする必要なし
- ✅ エラーハンドリングとわかりやすいメッセージ

### 従来の方法: Pythonスクリプトを直接実行

```bash
# 方法1: pythonコマンドで実行
python convert.py "記事.md"

# 方法2: 直接実行（Unix/Linux/WSL/Mac）
./convert.py "記事.md"

# 出力ファイル名を指定
python convert.py "記事.md" "output.html"

# 別のディレクトリのファイルを変換
python convert.py "../ブログディレクトリ/記事.md" "../ブログディレクトリ/output.html"
```

### WSL環境で手動でvenvを管理する場合

```bash
# 仮想環境を有効化
cd techxchange-blog-tools
source venv/bin/activate

# 変換実行
python convert.py "../ブログディレクトリ/記事.md"

# 作業が終わったら仮想環境を無効化
deactivate
```

## ワークフロー

### 1. Markdownでブログを作成

Bob/VSCode/TyporaなどでMarkdownファイルを作成します。

#### 📝 Markdownファイルの記述ルール

**シンプルなルール:**

1. **通常通りMarkdownを記述**
   - h1（`#`）とh2（`##`）を使って構造化
   - 画像は通常通り`![説明](path/to/image.png)`で記述

2. **コンテンツに関する注記など（任意）**
   - ファイルの先頭に任意の注記を記載できます
   - 例: `このブログはAIによって生成されたコンテンツを含みます。`

#### 推奨されるMarkdown構造

```markdown
このブログはAIによって生成されたコンテンツを含みます。(スクショ、コマンド出力、ログ、トレースなどには含みません)

# IBM Guardium Cryptography Manager 2.0.1 リリース紹介

## はじめに

本文...

![スクリーンショット](media/image1.png)

## 主要な機能

本文...

### サブセクション

詳細...
```

#### 変換後のHTML構造

```html
<div class="toc">
<span class="toctitle">目次</span>
<ul>
  <li><a href="#ibm-guardium-cryptography-manager-201">IBM Guardium Cryptography Manager 2.0.1 リリース紹介</a>
    <ul>
      <li><a href="#はじめに">はじめに</a></li>
    </ul>
  </li>
  <li><a href="#主要な機能">主要な機能</a></li>
</ul>
</div>

<a id="page-top" style="display: none;"></a>
<p>このブログはAIによって生成されたコンテンツを含みます。...</p>

<h1 id="ibm-guardium-cryptography-manager-201">IBM Guardium Cryptography Manager 2.0.1 リリース紹介</h1>
<p style="text-align: right;"><a href="#page-top">トップに戻る</a></p>

<h2 id="はじめに">はじめに</h2>
<p>本文...</p>
<div class="image-placeholder">
<strong>[画像をここに挿入: media/image1.png]</strong>
<br><em>説明: スクリーンショット</em>
</div>
<p style="text-align: right;"><a href="#page-top">トップに戻る</a></p>

<h2 id="主要な機能">主要な機能</h2>
<p>本文...</p>
<p style="text-align: right;"><a href="#page-top">トップに戻る</a></p>
```

**特徴:**
- h1とh2の両方が目次に含まれます（階層構造付き）
- 各h1/h2セクションの末尾に「トップに戻る」リンクが自動追加されます
- 画像はプレースホルダーに変換されます
- ページトップに隠しアンカー（`#toc`）が追加されます

### 2. HTMLに変換

```bash
# 推奨: ラッパースクリプトを使用（venv自動判定）
cd techxchange-blog-tools
./convert.sh "../ブログディレクトリ/記事.md"

# 従来の方法: WSL環境（仮想環境を手動管理）
cd techxchange-blog-tools
source venv/bin/activate
python convert.py "../ブログディレクトリ/記事.md"

# 従来の方法: Windows/Mac/Linux環境
cd techxchange-blog-tools
python convert.py "../ブログディレクトリ/記事.md"
```

### 3. 生成されたHTMLを確認

ブラウザで開いて以下を確認：
- ✅ 目次が正しく生成されている（h1とh2の階層構造）
- ✅ 見出しのリンクが動作する
- ✅ 画像プレースホルダーが表示されている
- ✅ 各h1/h2セクションに「トップに戻る」リンクがある

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
├── convert.sh                 # ラッパースクリプト（推奨）
├── convert.py                 # 変換スクリプト（Python）
├── requirements.txt           # Python依存関係
├── .gitignore                 # Git除外設定
├── .gitattributes             # Git属性設定（LF改行）
└── venv/                      # Python仮想環境（WSL用、自動生成）

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

**注意:** バックスラッシュ（`\`）を使った画像パスも自動的にスラッシュ（`/`）に正規化されます。

### HTML変換後

画像は以下のようなプレースホルダーに変換されます：

```html
<div class="image-placeholder">
<strong>[画像をここに挿入: media/image1.png]</strong>
<br><em>説明: 説明文</em>
</div>
```

TechXchangeでこのプレースホルダーを見つけて、対応する画像をアップロードしてください。

## 生成されるHTMLの特徴

### 目次

- 自動生成される目次（TOC）
- h1とh2レベルの見出しを含む（階層構造付き）
- クリック可能なリンク

### スタイル

- **カスタムスタイルなし**: 独自のCSS/フォント指定は一切なし
- **最小限の属性のみ**: `class`属性と`id`属性のみ
- **TechXchange完全互換**: サイトのデフォルトスタイルに完全依存

### トップに戻るリンク

- 各h1/h2セクションの末尾に自動追加
- `href="#page-top"`で隠しアンカーにリンク
- ページトップに確実に戻る

### 画像プレースホルダー

- `<div class="image-placeholder">`で明確に表示
- 画像パスと説明文を含む
- TechXchangeで手動アップロード時に識別しやすい

## トラブルシューティング

### Pythonが見つからない

**エラー:** `command not found: python`

**解決策:**
1. Pythonをインストール
   - Windows: [python.org](https://www.python.org/)からインストーラーをダウンロード
   - macOS: `brew install python3`
   - Ubuntu/WSL: `sudo apt-get install python3 python3-pip`
2. ターミナルを再起動
3. `python --version`または`python3 --version`で確認

### 依存関係のインストールエラー

**エラー:** `error: externally-managed-environment`（Ubuntu 24.04以降）

**解決策:**
仮想環境を使用してください：

```bash
# 仮想環境の作成
python3 -m venv venv

# 仮想環境の有効化
source venv/bin/activate

# 依存関係のインストール
pip install -r requirements.txt
```

### 変換エラーが発生する

**原因:** Markdownファイルの構文エラーまたはエンコーディングの問題

**解決策:**
- Markdownの構文を確認
- ファイルがUTF-8エンコーディングであることを確認
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
- 見出しレベルは`#`（h1）と`##`（h2）を使用

## 使用例

### 例1: ラッパースクリプトで基本的な変換（推奨）

```bash
cd techxchange-blog-tools
./convert.sh "../GCM2使用方法1 CSVインポート/GCM2使用方法1 CSVインポート.md"
```

### 例2: ラッパースクリプトで出力ファイル名を指定

```bash
cd techxchange-blog-tools
./convert.sh "../QSR OSS版紹介ブログ/QSR OSS版紹介ブログ.md" "../QSR OSS版紹介ブログ/techxchange-qsr.html"
```

### 例3: 従来の方法（Pythonスクリプト直接実行）

```bash
cd techxchange-blog-tools
python convert.py "../GCM2使用方法1 CSVインポート/GCM2使用方法1 CSVインポート.md"
```

### 例4: WSL環境で手動venv管理

```bash
# 仮想環境を有効化
cd techxchange-blog-tools
source venv/bin/activate

# 変換実行
python convert.py "../ブログディレクトリ/記事.md"

# 作業が終わったら無効化
deactivate
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

### 使用しているライブラリ

- **markdown**: Markdown→HTML変換（目次生成機能付き）
- **beautifulsoup4**: HTML解析と操作
- **lxml**: BeautifulSoupの高速パーサー

### 処理フロー

1. Markdownファイルを読み込み
2. 画像をプレースホルダーに変換（バックスラッシュ→スラッシュ正規化）
3. Markdown→HTML変換（目次付き、h1とh2レベル）
4. ページトップに隠しアンカーを追加
5. 各h1/h2セクション末尾に「トップに戻る」リンクを追加
6. HTMLファイルに出力

## サポート

問題が発生した場合は、以下を確認してください：

1. Pythonのバージョン: `python --version`
2. 依存関係のインストール状況: `pip list | grep -E "markdown|beautifulsoup4|lxml"`
3. 入力ファイルのエンコーディング: UTF-8であることを確認
4. エラーメッセージの全文をコピー

## ライセンス

このツールはIBM Data Security Communityブログ作成用に作成されました。