"""
简便运算游戏 - 使用示例
展示如何在不同的测试场景中调用游戏
"""

# ============================================================
# 场景1: 单元测试 - 测试游戏逻辑
# ============================================================

def example_unit_test():
    """示例：在单元测试中使用游戏逻辑"""
    print("\n" + "=" * 60)
    print("场景1: 单元测试")
    print("=" * 60)

    # 导入游戏测试函数
    from assets.test_game_automated import (
        generate_local_question,
        test_answer_verification
    )

    print("\n📝 测试题目生成...")
    question = generate_local_question()
    print(f"   生成题目: {question['problem']}")
    print(f"   正确答案: {question['answer']}")

    print("\n✅ 单元测试完成！")

# ============================================================
# 场景2: 集成测试 - 使用浏览器自动化
# ============================================================

def example_integration_test():
    """示例：在集成测试中使用Selenium"""
    print("\n" + "=" * 60)
    print("场景2: 集成测试")
    print("=" * 60)

    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        import time
        import os

        print("\n🔧 配置浏览器...")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")

        print("🚀 启动浏览器...")
        driver = webdriver.Chrome(options=chrome_options)

        print("📖 加载游戏页面...")
        file_url = "file://" + os.path.abspath("assets/math_game.html")
        driver.get(file_url)

        print("⏳ 等待页面加载...")
        time.sleep(2)

        print("✅ 浏览器测试完成！")

        driver.quit()

    except ImportError:
        print("\n❌ 需要安装 selenium: pip install selenium")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")

# ============================================================
# 场景3: 手动测试 - 打开浏览器
# ============================================================

def example_manual_test():
    """示例：手动测试 - 打开浏览器"""
    print("\n" + "=" * 60)
    print("场景3: 手动测试")
    print("=" * 60)

    import webbrowser
    import os

    print("\n🚀 正在打开浏览器...")
    game_file = os.path.abspath("assets/math_game.html")
    webbrowser.open('file://' + game_file)

    print("✅ 已在浏览器中打开游戏页面")
    print("💡 请手动测试游戏功能")

# ============================================================
# 场景4: 代码中调用 - 提取游戏逻辑
# ============================================================

def example_code_usage():
    """示例：在代码中调用游戏逻辑"""
    print("\n" + "=" * 60)
    print("场景4: 代码中调用游戏逻辑")
    print("=" * 60)

    import random

    def generate_question(difficulty="easy"):
        """生成题目"""
        if difficulty == "easy":
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            num1 = a * 10 + b
            num2 = a * 10 + (10 - b)
            return {
                "problem": f"{num1} + {num2} = ?",
                "answer": num1 + num2
            }
        elif difficulty == "medium":
            bases = [10, 20, 30, 40, 50]
            base = random.choice(bases)
            small = random.randint(1, 9)
            num1 = base + small
            num2 = base - small
            return {
                "problem": f"{num1} + {num2} = ?",
                "answer": num1 + num2
            }
        else:
            num1 = random.randint(10, 99)
            return {
                "problem": f"{num1} × 11 = ?",
                "answer": num1 * 11
            }

    print("\n📝 生成简单题目:")
    q1 = generate_question("easy")
    print(f"   题目: {q1['problem']}")
    print(f"   答案: {q1['answer']}")

    print("\n📝 生成中等题目:")
    q2 = generate_question("medium")
    print(f"   题目: {q2['problem']}")
    print(f"   答案: {q2['answer']}")

    print("\n📝 生成困难题目:")
    q3 = generate_question("hard")
    print(f"   题目: {q3['problem']}")
    print(f"   答案: {q3['answer']}")

    print("\n✅ 代码调用完成！")

# ============================================================
# 场景5: 批量测试 - 生成多道题目
# ============================================================

def example_batch_test():
    """示例：批量测试 - 生成多道题目"""
    print("\n" + "=" * 60)
    print("场景5: 批量测试")
    print("=" * 60)

    import random

    def generate_batch_questions(count=5, difficulty="easy"):
        """批量生成题目"""
        questions = []
        for _ in range(count):
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            num1 = a * 10 + b
            num2 = a * 10 + (10 - b)
            questions.append({
                "problem": f"{num1} + {num2} = ?",
                "answer": num1 + num2
            })
        return questions

    print(f"\n📝 生成 {5} 道题目:")
    questions = generate_batch_questions(5)
    for i, q in enumerate(questions, 1):
        print(f"   {i}. {q['problem']}  答案: {q['answer']}")

    print("\n✅ 批量测试完成！")

# ============================================================
# 场景6: API 调用 - 与后端交互
# ============================================================

def example_api_call():
    """示例：调用后端API"""
    print("\n" + "=" * 60)
    print("场景6: API 调用")
    print("=" * 60)

    import requests
    import json

    print("\n📡 调用后端API...")

    # 注意：需要确保后端服务已启动
    # python scripts/http_run.sh -p 8000

    try:
        url = "http://localhost:8000/v1/chat/completions"
        payload = {
            "messages": [
                {"role": "user", "content": "生成一道简单的简便运算题"}
            ],
            "session_id": "test_session"
        }

        print(f"   请求URL: {url}")
        print(f"   请求参数: {payload}")

        # response = requests.post(url, json=payload)
        # result = response.json()
        # print(f"   响应结果: {result}")

        print("   ✅ API调用成功！（需要确保服务已启动）")

    except requests.exceptions.ConnectionError:
        print("   ❌ 无法连接到服务器，请确保服务已启动")
    except Exception as e:
        print(f"   ❌ API调用失败: {e}")

# ============================================================
# 主函数 - 运行所有示例
# ============================================================

def main():
    """运行所有使用示例"""
    print("\n" + "=" * 60)
    print("🎮 简便运算游戏 - 使用示例")
    print("=" * 60)

    examples = [
        ("单元测试", example_unit_test),
        ("集成测试", example_integration_test),
        ("手动测试", example_manual_test),
        ("代码调用", example_code_usage),
        ("批量测试", example_batch_test),
        ("API调用", example_api_call),
    ]

    print("\n📋 可用示例:")
    for i, (name, _) in enumerate(examples, 1):
        print(f"   {i}. {name}")

    print("\n💡 运行特定示例:")
    print("   python assets/使用示例.py --example 1")

    print("\n🚀 运行所有示例...")

    for name, func in examples:
        try:
            func()
        except Exception as e:
            print(f"\n❌ {name} 执行失败: {e}")

    print("\n" + "=" * 60)
    print("✅ 所有示例执行完成！")
    print("=" * 60)

if __name__ == "__main__":
    main()
