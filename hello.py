#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
シンプルな挨拶アプリ
Gitの練習用サンプルコード
初期コミット
"""

from typing import Final

APP_TITLE: Final[str] = "=== 挨拶アプリ ==="


def greet(name: str) -> str:
    """
    名前を受け取って挨拶を返す関数
    
    Args:
        name (str): 挨拶する相手の名前
    
    Returns:
        str: 挨拶メッセージ
    """
    return f"こんにちは、{name}さん!"


def main() -> None:
    """メイン関数"""
    print(APP_TITLE)
    name = input("あなたの名前を入力してください: ").strip()
    
    if name != "":
        message = greet(name)
        print(message)
    else:
        print("名前が入力されませんでした。")


if __name__ == "__main__":
    main()
