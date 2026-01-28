"""
游戏交互工具
让智能体能够与简便运算游戏交互
"""

import json
import os
from langchain.tools import tool

@tool
def start_game_session(difficulty: str = "easy") -> str:
    """
    开始一个游戏会话，生成游戏链接和会话ID

    Args:
        difficulty: 游戏难度，可选值为 "easy"（简单）、"medium"（中等）、"hard"（困难）

    Returns:
        返回游戏会话信息，包含游戏链接和会话ID的JSON字符串
    """
    import time

    # 生成会话ID
    session_id = f"game_{int(time.time())}"

    # 获取游戏文件路径
    game_file = os.path.abspath("assets/math_game.html")

    # 检查文件是否存在
    if not os.path.exists(game_file):
        return json.dumps({
            "success": False,
            "error": "游戏文件不存在"
        }, ensure_ascii=False)

    # 构建游戏链接（本地文件路径）
    game_link = f"file://{game_file}"

    # HTTP链接（使用8080端口）
    http_link = "http://localhost:8080/assets/math_game.html"

    # 添加服务器检查提示
    server_info = """
    💡 如果打不开链接，请先启动游戏服务器：
       方法1: bash scripts/start_game_server.sh
       方法2: python -m http.server 8080
    """

    result = {
        "success": True,
        "session_id": session_id,
        "game_link": game_link,
        "http_link": http_link,
        "difficulty": difficulty,
        "server_info": server_info,
        "message": "游戏已开始！请打开链接玩游戏，完成后告诉我你的得分！"
    }

    return json.dumps(result, ensure_ascii=False)


@tool
def submit_game_result(score: int, stars: int, session_id: str) -> str:
    """
    提交游戏结果，获取智能体的评价和反馈

    Args:
        score: 游戏得分（0-30）
        stars: 获得的星星数量（0-3）
        session_id: 游戏会话ID

    Returns:
        返回评价和反馈的JSON字符串
    """
    # 计算评价
    if score == 30:
        evaluation = "完美通关"
        emoji = "🏆"
        comment = "哇！你简直是简便运算小天才！三关全部满分通过！"
        encouragement = "继续保持，你一定能成为数学高手！"
    elif score >= 21:
        evaluation = "优秀"
        emoji = "🥇"
        comment = "太棒了！你表现非常出色！"
        encouragement = "再多练习几次，你肯定能拿到满分！"
    elif score >= 15:
        evaluation = "良好"
        emoji = "🥈"
        comment = "做得不错！你掌握了基本的简便运算方法。"
        encouragement = "继续加油，你越来越棒了！"
    elif score >= 10:
        evaluation = "及格"
        emoji = "🥉"
        comment = "还需要多多练习哦。"
        encouragement = "别灰心，多练习几次，你一定能掌握的！"
    else:
        evaluation = "继续努力"
        emoji = "💪"
        comment = "这次没发挥好，没关系！"
        encouragement = "复习一下简便运算的方法，再试一次吧！"

    # 根据星星数量给出额外建议
    star_feedback = ""
    if stars == 3:
        star_feedback = "🌟🌟🌟 满星！太厉害了！"
    elif stars == 2:
        star_feedback = "🌟🌟 收获两颗星，很棒！"
    elif stars == 1:
        star_feedback = "🌟 收获一颗星，继续努力！"
    else:
        star_feedback = "💫 这次没有星星，下次一定有！"

    # 给出学习建议
    tips = []
    if score < 15:
        tips.append("提示：记住凑十法的秘诀：看大数，拆小数，凑成十，加剩数")
        tips.append("提示：25×4=100，125×8=1000，这两个组合要记住哦")
    elif score < 25:
        tips.append("提示：试试多观察数字规律，找到最快的方法")
    else:
        tips.append("提示：你已经是简便运算高手了，可以挑战更难的题目！")

    result = {
        "success": True,
        "session_id": session_id,
        "score": score,
        "stars": stars,
        "evaluation": evaluation,
        "emoji": emoji,
        "comment": comment,
        "encouragement": encouragement,
        "star_feedback": star_feedback,
        "tips": tips
    }

    return json.dumps(result, ensure_ascii=False)


@tool
def get_game_tips(topic: str = "all") -> str:
    """
    获取简便运算技巧和学习建议

    Args:
        topic: 主题，可选值为 "all"（全部）、"basic"（基础）、"advanced"（进阶）

    Returns:
        返回技巧和建议的JSON字符串
    """
    tips = {
        "basic": [
            {
                "title": "凑十法",
                "content": "把一个数拆分，使其中一部分和另一个数凑成10。例如：8+7，把7拆成2+5，先算8+2=10，再算10+5=15。",
                "example": "7 + 8 = 7 + 3 + 5 = 10 + 5 = 15"
            },
            {
                "title": "凑整法",
                "content": "把数凑成整十、整百。例如：47+33，把47看成40+7，33看成30+3，先算40+30=70，再算7+3=10，最后70+10=80。",
                "example": "47 + 33 = (40+7) + (30+3) = 70 + 10 = 80"
            }
        ],
        "advanced": [
            {
                "title": "拆分法",
                "content": "把复杂的数拆分成简单的部分。例如：99+27，把99看成100-1，先算100+27=127，再减去1，得到126。",
                "example": "99 + 27 = (100-1) + 27 = 100 + 27 - 1 = 126"
            },
            {
                "title": "乘法巧算",
                "content": "记住一些特殊的乘法组合：25×4=100，125×8=1000，11×任何两位数可以快速计算（两边一拉，中间相加）。",
                "example": "25 × 4 = 100，125 × 8 = 1000，34 × 11 = 374"
            }
        ]
    }

    if topic == "all":
        result = {
            "success": True,
            "topic": "all",
            "basic_tips": tips["basic"],
            "advanced_tips": tips["advanced"]
        }
    elif topic == "basic":
        result = {
            "success": True,
            "topic": "basic",
            "tips": tips["basic"]
        }
    else:
        result = {
            "success": True,
            "topic": "advanced",
            "tips": tips["advanced"]
        }

    return json.dumps(result, ensure_ascii=False)
