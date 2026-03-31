# クイックスタートガイド

TechXchange用ブログ変換ツールの簡単な使い方ガイドです。

## 🚀 5分で始める

### 1. リポジトリをクローン

```bash
# GitHubからクローン
git clone https://github.com/khirazo/techxchange-blog-tools.git

# ディレクトリに移動
cd techxchange-blog-tools
```

### 2. Pandocをインストール

```bash
# Ubuntu/WSL
sudo apt-get update && sudo apt-get install pandoc

# macOS
brew install pandoc
```

**注意**: `sed`と`awk`はmacOS/Linux/WSLに標準搭載されています。

### 3. ブログを変換

```bash
# ブログディレクトリに移動
cd "あなたのブログディレクトリ"

# 変換実行（WSL）
wsl bash path/to/techxchange-blog-tools/convert-simple.sh "記事.md"

# 変換実行（Mac/Linux）
bash path/to/techxchange-blog-tools/convert-simple.sh "記事.md"
```

### 4. 結果を確認

生成された`.html`ファイルをブラウザで開いて確認します。

### 5. TechXchangeに投稿

1. HTMLファイルをテキストエディタで開く
2. 全内容をコピー
3. TechXchangeのHTMLエディタに貼り付け
4. `[画像をここに挿入: ...]`を見つけて画像をアップロード

## 📝 完全なワークフロー

```
1. GitHubからクローン
   ↓
2. Pandocインストール
   ↓
3. Markdown作成 (Bob/VSCode)
   ↓
4. HTML変換 (スクリプト)
   ↓
5. ブラウザ確認
   ↓
6. TechXchange投稿 (画像アップロード)
```

## 💡 よくある質問

### Q: Qiitaにも投稿できますか？

A: 元のMarkdownファイルをそのままQiitaに投稿できます。(このツールは不要です)

### Q: 画像はどうなりますか？

A: `[画像をここに挿入: ...]`というプレースホルダーに変換されます。TechXchangeで手動アップロードが必要です。

### Q: 目次は自動生成されますか？

A: はい！Markdownの見出し（`#`, `##`）から自動生成されます。

### Q: 「トップに戻る」リンクは？

A: 各h1セクションの末尾に自動的に追加されます。

### Q: スタイルはカスタマイズできますか？

A: このツールはスタイル指定を一切含まないため、TechXchangeのデフォルトスタイルが適用されます。

## 🔧 トラブルシューティング

### Pandocが見つからない

```bash
# インストール確認
pandoc --version

# 再インストール（Ubuntu/WSL）
sudo apt-get install --reinstall pandoc
```

### sed/awkが見つからない

通常はmacOS/Linux/WSLに標準搭載されていますが、もし見つからない場合：

```bash
# Ubuntu/WSL
sudo apt-get install sed gawk

# 確認
which sed
which awk
```

### パスエラーが発生する

ブログディレクトリ内で実行してください：

```bash
cd "ブログディレクトリ"
wsl bash path/to/techxchange-blog-tools/convert-simple.sh "記事.md"
```

## 📚 詳細情報

詳しい使い方は[README.md](README.md)を参照してください。

## 🎯 生成されるHTML例

```html
<header id="title-block-header">
<h1 class="title">タイトル</h1>
</header>
<nav id="TOC" role="doc-toc">
<ul>
<li><a href="#セクション1">セクション1</a></li>
</ul>
</nav>
<h1 id="セクション1">セクション1</h1>
<p>本文...</p>
<div class="image-placeholder">
<strong>[画像をここに挿入: media/image1.png]</strong>
<em>説明: 画像の説明</em>
</div>
<p><a href="#">トップに戻る</a></p>
```

## ✨ 主な特徴

- **スタイル指定なし**: TechXchangeのデフォルトスタイルを使用
- **目次自動生成**: Markdownの見出しから自動作成
- **トップに戻るリンク**: 各セクション末尾に自動追加
- **クロスプラットフォーム**: Mac/Linux/WSL対応