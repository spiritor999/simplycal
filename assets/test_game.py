"""
测试游戏页面的基本功能
"""
import os
import re

def test_game_file_exists():
    """测试游戏文件是否存在"""
    file_path = "assets/math_game.html"
    if os.path.exists(file_path):
        print(f"✅ 游戏文件存在: {file_path}")
        return True
    else:
        print(f"❌ 游戏文件不存在: {file_path}")
        return False

def test_html_structure():
    """测试HTML结构是否完整"""
    file_path = "assets/math_game.html"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查关键元素
    checks = {
        'DOCTYPE声明': '<!DOCTYPE html>',
        'HTML标签': '<html',
        '开始界面': 'startScreen',
        '游戏界面': 'gameScreen',
        '结果界面': 'resultScreen',
        'JavaScript代码': '<script>',
        'CSS样式': '<style>',
        '难度选择': 'selectDifficulty',
        '开始游戏': 'startGame',
        '提交答案': 'submitAnswer',
        '显示结果': 'showResult'
    }
    
    all_passed = True
    for name, pattern in checks.items():
        if pattern in content:
            print(f"✅ {name} - 检查通过")
        else:
            print(f"❌ {name} - 检查失败")
            all_passed = False
    
    return all_passed

def test_responsive_design():
    """测试响应式设计元素"""
    file_path = "assets/math_game.html"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        'viewport设置': 'viewport',
        '媒体查询': '@media',
        '移动端适配': 'max-width: 600px'
    }
    
    all_passed = True
    for name, pattern in checks.items():
        if pattern in content:
            print(f"✅ {name} - 检查通过")
        else:
            print(f"❌ {name} - 检查失败")
            all_passed = False
    
    return all_passed

def test_game_logic():
    """测试游戏逻辑函数"""
    file_path = "assets/math_game.html"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    checks = {
        '难度选择函数': 'function selectDifficulty',
        '开始游戏函数': 'function startGame',
        '加载题目函数': 'function loadQuestion',
        '提交答案函数': 'function submitAnswer',
        '显示结果函数': 'function showResult',
        '重新开始函数': 'function restartGame',
        '更新统计函数': 'function updateStats',
        '本地题目生成': 'function generateLocalQuestion'
    }
    
    all_passed = True
    for name, pattern in checks.items():
        if pattern in content:
            print(f"✅ {name} - 检查通过")
        else:
            print(f"❌ {name} - 检查失败")
            all_passed = False
    
    return all_passed

def main():
    """运行所有测试"""
    print("=" * 50)
    print("🎮 简便运算游戏页面测试")
    print("=" * 50)
    print()
    
    print("1. 检查文件存在性")
    print("-" * 50)
    test1 = test_game_file_exists()
    print()
    
    if not test1:
        print("❌ 文件不存在，无法继续测试")
        return
    
    print("2. 检查HTML结构")
    print("-" * 50)
    test2 = test_html_structure()
    print()
    
    print("3. 检查响应式设计")
    print("-" * 50)
    test3 = test_responsive_design()
    print()
    
    print("4. 检查游戏逻辑")
    print("-" * 50)
    test4 = test_game_logic()
    print()
    
    print("=" * 50)
    if test1 and test2 and test3 and test4:
        print("✅ 所有测试通过！游戏页面准备就绪！")
        print()
        print("📝 使用方法：")
        print("   方法1：直接双击 assets/math_game.html 文件用浏览器打开")
        print("   方法2：运行 'python -m http.server 8080' 后访问 http://localhost:8080/assets/math_game.html")
    else:
        print("❌ 部分测试失败，请检查游戏文件")
    print("=" * 50)

if __name__ == "__main__":
    main()
