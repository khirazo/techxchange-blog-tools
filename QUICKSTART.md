# クイックスタートガイド

TechXchange ブログ変換ツールの最速セットアップガイドです。

## 🚀 5分でセットアップ

### 1. リポジトリをクローン

```bash
git clone https://github.com/khirazo/techxchange-blog-tools.git
cd techxchange-blog-tools
```

### 2. 依存関係をインストール

#### Windows/Mac/Linux（通常）

```bash
pip install -r requirements.txt
```

#### WSL Ubuntu 24.04以降

```bash
# 仮想環境を作成
python3 -m venv venv

# 仮想環境を有効化
source venv/bin/activate

# 依存関係をインストール
pip install -r requirements.txt
```

### 3. 変換を実行

#### 推奨: ラッパースクリプトを使用（最も簡単）

```bash
# 基本的な使い方（venvを自動判定・アクティベート）
./convert.sh "記事.md"

# 出力ファイル名を指定
./convert.sh "記事.md" "output.html"
```

#### 従来の方法: Pythonスクリプトを直接実行

```bash
# 基本的な使い方
python convert.py "記事.md"

# 出力ファイル名を指定
python convert.py "記事.md" "output.html"
```

## 📝 Markdownの書き方

### 最小限の例

```markdown
このブログはAIによって生成されたコンテンツを含みます。

# ブログタイトル

## はじめに

本文を書く...

![スクリーンショット](media/image1.png)

## まとめ

まとめを書く...
```

### ポイント

- ✅ h1（`#`）とh2（`##`）を使って構造化
- ✅ 画像は通常通り`![説明](path)`で記述
- ✅ AI生成注記は任意（ファイル先頭に記載）

## 🎯 変換後の確認

生成されたHTMLファイルをブラウザで開いて確認：

- ✅ 目次が生成されている
- ✅ 各セクションに「トップに戻る」リンクがある
- ✅ 画像がプレースホルダーになっている

## 📤 TechXchangeへの投稿

1. HTMLファイルをテキストエディタで開く
2. 全内容をコピー
3. TechXchangeのHTMLエディタに貼り付け
4. 画像プレースホルダーを見つけて画像をアップロード

## 💡 よくある質問

### Q: WSLで仮想環境を毎回有効化する必要がある？

A: **ラッパースクリプト（`convert.sh`）を使えば不要です！**

```bash
# venvの有無を自動判定して実行
cd techxchange-blog-tools
./convert.sh "記事.md"
```

従来の方法で手動管理する場合は、作業開始時に以下を実行：

```bash
cd techxchange-blog-tools
source venv/bin/activate
```

作業終了時に無効化：

```bash
deactivate
```

### Q: 画像のパスにバックスラッシュを使っても大丈夫？

A: はい。自動的にスラッシュに正規化されます。

### Q: h1とh2以外の見出しは？

A: h3以降も使えますが、目次にはh1とh2のみが含まれます。

### Q: 既存の「トップに戻る」リンクはどうなる？

A: 自動的に削除され、各h1/h2セクション末尾に統一されたリンクが追加されます。

## 🔧 トラブルシューティング

### Pythonが見つからない

```bash
# バージョン確認
python --version
# または
python3 --version
```

見つからない場合は[README.md](README.md)のインストール手順を参照。

### 依存関係のインストールエラー

Ubuntu 24.04以降で`externally-managed-environment`エラーが出る場合：

```bash
# 仮想環境を使用
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 変換エラー

- ファイルがUTF-8エンコーディングか確認
- Markdownの構文エラーがないか確認
- エラーメッセージの全文を確認

## 📚 詳細情報

詳しい使い方は[README.md](README.md)を参照してください。

## 🎓 使用例

### 例1: ラッパースクリプトで基本的な変換（推奨）

```bash
./convert.sh "../ブログディレクトリ/記事.md"
```

### 例2: ラッパースクリプトで出力先を指定

```bash
./convert.sh "記事.md" "techxchange.html"
```

### 例3: 従来の方法（Pythonスクリプト直接実行）

```bash
python convert.py "../ブログディレクトリ/記事.md"
```

### 例4: WSL環境で手動venv管理

```bash
# 仮想環境を有効化
source venv/bin/activate

# 変換実行
python convert.py "../ブログディレクトリ/記事.md"

# 無効化
deactivate
```

---

**これで準備完了です！** 🎉

詳細な情報が必要な場合は[README.md](README.md)を参照してください。