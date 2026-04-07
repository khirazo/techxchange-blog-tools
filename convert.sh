#!/bin/bash
# このファイルはAIによって生成されたコンテンツを含みます。

# TechXchange Blog Converter Wrapper Script
# 
# このスクリプトは以下の機能を提供します:
# - venvの存在チェックと自動アクティベーション
# - 実行環境に関わらず統一されたインターフェース
# - エラーハンドリングとユーザーフレンドリーなメッセージ

# スクリプトのディレクトリを取得
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${SCRIPT_DIR}/venv"
PYTHON_SCRIPT="${SCRIPT_DIR}/convert.py"

# 色付きメッセージ用の定義
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# エラーメッセージを表示して終了
error_exit() {
    echo -e "${RED}エラー: $1${NC}" >&2
    exit 1
}

# 情報メッセージを表示
info_message() {
    echo -e "${GREEN}$1${NC}"
}

# 警告メッセージを表示
warning_message() {
    echo -e "${YELLOW}$1${NC}"
}

# Python実行可能ファイルを検出
detect_python() {
    if command -v python3 &> /dev/null; then
        echo "python3"
    elif command -v python &> /dev/null; then
        echo "python"
    else
        return 1
    fi
}

# メイン処理
main() {
    # Python実行可能ファイルを検出
    PYTHON_CMD=$(detect_python)
    if [ $? -ne 0 ]; then
        error_exit "Pythonが見つかりません。Python 3.8以上をインストールしてください。"
    fi

    # convert.pyの存在確認
    if [ ! -f "${PYTHON_SCRIPT}" ]; then
        error_exit "convert.pyが見つかりません: ${PYTHON_SCRIPT}"
    fi

    # venvが存在するかチェック
    if [ -d "${VENV_DIR}" ]; then
        # venvのアクティベーションスクリプトを確認
        ACTIVATE_SCRIPT="${VENV_DIR}/bin/activate"
        if [ -f "${ACTIVATE_SCRIPT}" ]; then
            info_message "仮想環境を検出しました。アクティベーション中..."
            
            # 仮想環境をアクティベート
            source "${ACTIVATE_SCRIPT}"
            
            # アクティベーション成功を確認
            if [ $? -eq 0 ]; then
                info_message "仮想環境をアクティベートしました: ${VENV_DIR}"
            else
                warning_message "仮想環境のアクティベーションに失敗しました。システムPythonを使用します。"
            fi
        else
            warning_message "仮想環境が不完全です。システムPythonを使用します。"
        fi
    else
        info_message "仮想環境が見つかりません。システムPythonを使用します。"
    fi

    # 引数がない場合はヘルプを表示
    if [ $# -eq 0 ]; then
        "${PYTHON_CMD}" "${PYTHON_SCRIPT}" --help
        exit 0
    fi

    # convert.pyを実行
    info_message "変換を開始します..."
    "${PYTHON_CMD}" "${PYTHON_SCRIPT}" "$@"
    EXIT_CODE=$?

    # 結果を表示
    if [ ${EXIT_CODE} -eq 0 ]; then
        info_message "変換が完了しました。"
    else
        error_exit "変換に失敗しました (終了コード: ${EXIT_CODE})"
    fi

    return ${EXIT_CODE}
}

# スクリプト実行
main "$@"

# Made with Bob
