"""
手动测试脚本 - 自动打开浏览器并加载游戏页面
适用于快速测试游戏功能
"""

import webbrowser
import os
import time

def open_game_in_browser():
    """在默认浏览器中打开游戏页面"""
    # 获取游戏文件的绝对路径
    game_file = os.path.abspath("assets/math_game.html")

    # 检查文件是否存在
    if not os.path.exists(game_file):
        print(f"❌ 游戏文件不存在: {game_file}")
        return False

    print(f"🎮 正在打开游戏页面...")
    print(f"📁 文件路径: {game_file}")
    print()
    print("✅ 测试步骤：")
    print("   1. 选择难度（简单/中等/困难）")
    print("   2. 点击'开始游戏'")
    print("   3. 输入答案并提交")
    print("   4. 完成所有关卡查看结果")
    print()

    # 使用系统默认浏览器打开
    webbrowser.open('file://' + game_file)

    return True

if __name__ == "__main__":
    print("=" * 60)
    print("🎮 简便运算游戏 - 手动测试")
    print("=" * 60)
    print()

    success = open_game_in_browser()

    if success:
        print("✅ 浏览器已打开，请开始测试游戏功能！")
    else:
        print("❌ 打开失败，请检查文件路径")

    print("=" * 60)
