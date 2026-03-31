#!/bin/bash
# This file includes AI-generated code - Review and modify as needed
# シンプルなMarkdown→HTML変換スクリプト（スタイルなし版）

set -e

if [ $# -lt 1 ]; then
    echo "使用方法: $0 input.md [output.html]"
    exit 1
fi

INPUT_FILE="$1"
OUTPUT_FILE="${2:-${INPUT_FILE%.md}.html}"

if [ ! -f "$INPUT_FILE" ]; then
    echo "エラー: 入力ファイルが見つかりません: $INPUT_FILE"
    exit 1
fi

if ! command -v pandoc &> /dev/null; then
    echo "エラー: Pandocがインストールされていません"
    exit 1
fi

echo "変換中: $INPUT_FILE -> $OUTPUT_FILE"

# 一時ファイルを作成
TEMP_FILE=$(mktemp)
TEMP_FILE2=$(mktemp)
TEMP_HTML=$(mktemp)
trap "rm -f '$TEMP_FILE' '$TEMP_FILE2' '$TEMP_HTML'" EXIT

# ステップ1: 画像をプレースホルダーに変換し、既存の「トップに戻る」リンクを統一
sed -E \
    -e 's|!\[([^]]*)\]\(([^)]+)\)|<div class="image-placeholder"><strong>[画像をここに挿入: \2]</strong><em>説明: \1</em></div>|g' \
    -e 's|\[トップに戻る\]\(#[^)]*\)|[トップに戻る](#)|g' \
    "$INPUT_FILE" > "$TEMP_FILE"

# ステップ2: 各h1セクションの最後に「トップに戻る」リンクを追加
awk '
BEGIN { 
    in_section = 0
    section_lines = ""
    first_section = 1
}
{
    # h1見出しを検出（# で始まり、## ではない行）
    if ($0 ~ /^# [^#]/) {
        # 前のセクションがあれば出力
        if (in_section) {
            print section_lines
            # 既存の「トップに戻る」リンクがなければ追加
            if (section_lines !~ /トップに戻る/) {
                print ""
                print "[トップに戻る](#)"
                print ""
            }
        }
        # 新しいセクション開始
        section_lines = $0
        in_section = 1
        first_section = 0
    } else {
        # セクション内容を蓄積
        if (section_lines == "") {
            section_lines = $0
        } else {
            section_lines = section_lines "\n" $0
        }
    }
}
END {
    # 最後のセクションを出力
    print section_lines
    if (in_section && section_lines !~ /トップに戻る/) {
        print ""
        print "[トップに戻る](#)"
    }
}
' "$TEMP_FILE" > "$TEMP_FILE2"

# Pandocで変換（standaloneで目次生成、後でbody部分のみ抽出）
pandoc "$TEMP_FILE2" \
    --output="$TEMP_HTML" \
    --toc \
    --toc-depth=3 \
    --standalone \
    --metadata title="$(basename "$INPUT_FILE" .md)" \
    --from markdown+hard_line_breaks \
    --to html5

# <body>タグの内容のみを抽出（<body>と</body>タグ自体は除外）
sed -n '/<body>/,/<\/body>/p' "$TEMP_HTML" | sed '1d;$d' > "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
    echo "✓ 変換完了: $OUTPUT_FILE"
    echo "  - 目次が自動生成されました"
    echo "  - 各セクションに「トップに戻る」リンクが追加されました"
    echo "  - Pandocのデフォルトスタイルのみ（最小限）"
else
    echo "エラー: 変換に失敗しました"
    exit 1
fi

# Made with Bob
