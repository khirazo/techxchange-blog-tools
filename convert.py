#!/usr/bin/env python3
# このファイルはAIによって生成されたコンテンツを含みます。

"""
TechXchange Blog Markdown to HTML Converter

Markdownファイルを TechXchange ブログ用のHTMLに変換します。

主な機能:
- h1/h2レベルの目次を自動生成
- 各h1/h2セクションに「トップに戻る」リンクを追加
- 画像をプレースホルダーに変換
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Tuple

import markdown
from markdown.extensions.toc import TocExtension
from bs4 import BeautifulSoup


def process_images(content: str) -> str:
    """
    画像をプレースホルダーに変換
    
    Args:
        content: Markdownコンテンツ
        
    Returns:
        画像がプレースホルダーに変換されたコンテンツ
    """
    # バックスラッシュをスラッシュに正規化
    content = content.replace('\\', '/')
    
    # 画像をプレースホルダーに変換
    # ![alt text](image/path.png) -> <div>プレースホルダー</div>
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def replacement(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        return (
            f'<div class="image-placeholder">'
            f'<strong>[画像をここに挿入: {image_path}]</strong>'
            f'<br><em>説明: {alt_text}</em>'
            f'</div>'
        )
    
    return re.sub(pattern, replacement, content)


def normalize_list_indentation(content: str) -> str:
    """
    入れ子リストのインデントを正規化（3スペース→4スペース）
    
    Markdownパーサーは入れ子リストに4スペースのインデントを要求するが、
    一部のエディターは3スペースを使用する。この関数は自動的に変換する。
    
    Args:
        content: Markdownコンテンツ
        
    Returns:
        インデントが正規化されたコンテンツ
    """
    import re
    
    lines = content.split('\n')
    normalized_lines = []
    
    for line in lines:
        # 行頭の空白を検出
        match = re.match(r'^(\s*)(.*)$', line)
        if match:
            indent = match.group(1)
            rest = match.group(2)
            
            # リスト項目（-, *, +, 数字.）で始まる行かチェック
            if rest and re.match(r'^[-*+]|\d+\.', rest):
                # インデントが3の倍数の場合、4の倍数に変換
                indent_len = len(indent)
                if indent_len > 0 and indent_len % 3 == 0 and indent_len % 4 != 0:
                    # 3スペース単位を4スペース単位に変換
                    new_indent_len = (indent_len // 3) * 4
                    normalized_lines.append(' ' * new_indent_len + rest)
                    continue
        
        normalized_lines.append(line)
    
    return '\n'.join(normalized_lines)


def convert_to_html(content: str) -> Tuple[str, str]:
    """
    Markdown→HTML変換（目次付き）
    
    Args:
        content: Markdownコンテンツ
        
    Returns:
        (目次HTML, 本文HTML)
    """
    md = markdown.Markdown(
        extensions=[
            TocExtension(
                toc_depth='1-2',  # h1とh2を目次に含める
                title='目次',
                permalink=False,
                anchorlink=False  # 見出しにリンクを追加しない
            ),
            'extra',
            'nl2br'  # 改行を<br>に変換
        ]
    )
    
    html_body = md.convert(content)
    toc_html = md.toc if hasattr(md, 'toc') else ''
    
    return toc_html, html_body


def convert_id_to_name_anchors(html: str) -> str:
    """
    id属性をname属性に変換（TechXchange互換性のため）
    
    Args:
        html: HTML文字列
        
    Returns:
        name属性に変換されたHTML
    """
    soup = BeautifulSoup(html, 'lxml')
    body = soup.find('body')
    if not body:
        return html
    
    # すべてのh1とh2タグを処理
    for heading in body.find_all(['h1', 'h2']):
        if heading.get('id'):
            # idをnameに変換するためのアンカータグを作成
            anchor = soup.new_tag('a', attrs={'name': heading['id']})
            # 見出しの内容をアンカーで囲む
            heading.insert(0, anchor)
            # 元のテキストをアンカー内に移動
            for child in list(heading.children)[1:]:  # アンカー以外の子要素
                anchor.append(child.extract())
            # id属性を削除
            del heading['id']
    
    return str(body).replace('<body>', '').replace('</body>', '')


def add_top_anchor_and_back_links(html: str) -> str:
    """
    各h1/h2セクションに「トップに戻る」リンクを追加
    
    Args:
        html: HTML文字列
        
    Returns:
        リンクが追加されたHTML
    """
    soup = BeautifulSoup(html, 'lxml')
    
    # lxmlは自動的に<html><body>タグを追加するので、bodyの中身だけを取得
    body = soup.find('body')
    if not body:
        return html
    
    # h1とh2タグを取得
    heading_tags = body.find_all(['h1', 'h2'])
    
    if not heading_tags:
        return str(body).replace('<body>', '').replace('</body>', '')
    
    # 各見出しセクションの末尾に「トップに戻る」リンクを追加
    for i, heading in enumerate(heading_tags):
        # 次の見出しを探す
        next_heading = heading_tags[i + 1] if i + 1 < len(heading_tags) else None
        
        # 「トップに戻る」リンクを作成
        back_link = soup.new_tag('p')
        a_tag = soup.new_tag('a', href='#toc')
        a_tag.string = 'トップに戻る'
        back_link.append(a_tag)
        
        # 挿入位置を決定
        if next_heading:
            # 次の見出しの直前に挿入
            next_heading.insert_before(back_link)
        else:
            # 最後の見出しの場合は、bodyの末尾に追加
            body.append(back_link)
    
    # <body>タグを除去して中身だけを返す
    return str(body).replace('<body>', '').replace('</body>', '')


def convert_markdown_to_html(input_file: Path, output_file: Path) -> None:
    """
    MarkdownファイルをTechXchange用HTMLに変換
    
    Args:
        input_file: 入力Markdownファイルのパス
        output_file: 出力HTMLファイルのパス
    """
    # Markdownファイルを読み込み
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"エラー: ファイルが見つかりません: {input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"エラー: ファイルの読み込みに失敗しました: {e}", file=sys.stderr)
        sys.exit(1)
    
    # 画像をプレースホルダーに変換
    markdown_content = process_images(markdown_content)
    
    # 入れ子リストのインデントを正規化（3スペース→4スペース）
    markdown_content = normalize_list_indentation(markdown_content)
    
    # Markdown→HTML変換（目次付き）
    toc_html, body_html = convert_to_html(markdown_content)
    
    # id属性をname属性に変換（TechXchange互換性）
    body_html = convert_id_to_name_anchors(body_html)
    
    # 「トップに戻る」リンクを追加
    body_html = add_top_anchor_and_back_links(body_html)
    
    # 最終的なHTMLを組み立て
    final_html_parts = []
    
    # 目次にアンカーを追加
    if toc_html:
        final_html_parts.append('<a name="toc"></a>')
        final_html_parts.append(toc_html)
    
    final_html_parts.append(body_html)
    
    final_html = '\n\n'.join(final_html_parts)
    
    # HTMLファイルに出力
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"変換完了: {output_file}")
    except Exception as e:
        print(f"エラー: ファイルの書き込みに失敗しました: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """メイン関数"""
    parser = argparse.ArgumentParser(
        description='TechXchange Blog Markdown to HTML Converter',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  python convert.py "記事.md"
  python convert.py "記事.md" "output.html"
  python convert.py --help

機能:
  - h1とh2レベルの目次を自動生成
  - 各h1/h2セクションに「トップに戻る」リンクを追加
  - 画像はプレースホルダーに変換
        """
    )
    
    parser.add_argument(
        'input_file',
        type=str,
        help='入力Markdownファイル'
    )
    
    parser.add_argument(
        'output_file',
        type=str,
        nargs='?',
        help='出力HTMLファイル（省略時は入力ファイル名.htmlを使用）'
    )
    
    args = parser.parse_args()
    
    # 入力ファイルのパス
    input_path = Path(args.input_file)
    
    # 出力ファイルのパス
    if args.output_file:
        output_path = Path(args.output_file)
    else:
        output_path = input_path.with_suffix('.html')
    
    # 変換実行
    convert_markdown_to_html(input_path, output_path)


if __name__ == '__main__':
    main()

# Made with Bob
