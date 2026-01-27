"""
数学题目生成工具
用于生成适合小学三年级的简便运算题目
"""

import random
from langchain.tools import tool

@tool
def generate_math_problem(difficulty: str = "easy") -> str:
    """
    生成一个简便运算题目

    Args:
        difficulty: 题目难度，可选值为 "easy"（简单）、"medium"（中等）、"hard"（困难）

    Returns:
        返回一个数学题目和正确答案的 JSON 格式字符串，包含 problem（题目）、answer（答案）、difficulty（难度）和 hint（提示）
    """
    # 根据难度生成不同类型的题目
    if difficulty == "easy":
        # 生成简单题目：利用凑十法、凑整法
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        # 生成可以简便计算的题目
        num1 = a * 10 + b
        num2 = a * 10 + (10 - b)
        problem = f"{num1} + {num2} = ?"
        answer = num1 + num2

    elif difficulty == "medium":
        # 生成中等题目：拆分法、凑整法
        base = random.choice([10, 20, 30, 40, 50])
        small = random.randint(1, 9)

        if random.choice([True, False]):
            num1 = base + small
            num2 = base - small
            problem = f"{num1} + {num2} = ?"
            answer = num1 + num2
        else:
            num1 = 100 - small
            num2 = small
            problem = f"{num1} - {num2} = ?"
            answer = num1 - num2

    else:  # hard
        # 生成困难题目：混合运算，需要灵活运用简便方法
        base = 100
        a = random.randint(1, 9)
        b = random.randint(1, 9)

        if random.choice([True, False]):
            num1 = base - a
            num2 = base - b
            problem = f"{num1} + {num2} = ?"
            answer = num1 + num2
        else:
            # 生成 34×11, 56×11 这样的题目
            num1 = random.randint(10, 99)
            num2 = 11
            problem = f"{num1} × {num2} = ?"
            answer = num1 * num2

    # 返回 JSON 格式
    result = {
        "problem": problem,
        "answer": answer,
        "difficulty": difficulty,
        "hint": "提示：试试用凑整法、拆分法或者观察数字规律哦！"
    }

    import json
    return json.dumps(result, ensure_ascii=False)


@tool
def verify_answer(problem: str, user_answer: int) -> str:
    """
    验证学生的答案是否正确

    Args:
        problem: 数学题目字符串（如 "25 + 35 = ?"）
        user_answer: 学生给出的答案

    Returns:
        返回验证结果的 JSON 格式字符串，包含 is_correct（是否正确）、user_answer（学生答案）、correct_answer（正确答案）和 message（消息）
    """
    try:
        # 从题目中提取算式
        # 支持 +, -, ×, * 等运算符
        equation = problem.replace("=", "").replace("?", "").strip()

        # 标准化乘号
        equation = equation.replace("×", "*")

        # 计算正确答案
        correct_answer = eval(equation)

        # 判断是否正确
        is_correct = (user_answer == correct_answer)

        result = {
            "is_correct": is_correct,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "message": "太棒了！答案正确！🎉" if is_correct else f"加油！正确答案是 {correct_answer}，再试试看！💪"
        }

        import json
        return json.dumps(result, ensure_ascii=False)

    except Exception as e:
        import json
        return json.dumps({
            "is_correct": False,
            "error": f"题目解析错误：{str(e)}"
        }, ensure_ascii=False)
