#!/bin/bash
# 一键启动脚本：智能体 + 游戏服务器

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK_DIR="${COZE_WORKSPACE_PATH:-$(dirname "$SCRIPT_DIR")}"
cd "$WORK_DIR"

echo "=========================================="
echo "🚀 一键启动简便运算系统"
echo "=========================================="
echo ""

# 检查依赖
echo "📦 检查依赖..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# 安装依赖
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "⏳ 正在安装依赖..."
    pip install -q fastapi uvicorn
fi

echo "✅ 依赖检查完成"
echo ""

# 检查配置文件
if [ ! -f "config/agent_llm_config.json" ]; then
    echo "❌ 配置文件不存在: config/agent_llm_config.json"
    exit 1
fi

# 检查智能体代码
if [ ! -f "src/agents/agent.py" ]; then
    echo "❌ 智能体代码不存在: src/agents/agent.py"
    exit 1
fi

# 检查游戏文件
if [ ! -f "assets/math_game.html" ]; then
    echo "❌ 游戏文件不存在: assets/math_game.html"
    exit 1
fi

# 启动智能体服务（后台运行）
echo "🤖 启动智能体服务..."
nohup python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 > /tmp/agent.log 2>&1 &
AGENT_PID=$!

# 等待智能体服务启动
sleep 3

# 检查智能体服务是否启动成功
if ! curl -f http://localhost:8000/health >/dev/null 2>&1; then
    echo "❌ 智能体服务启动失败"
    cat /tmp/agent.log
    exit 1
fi

echo "✅ 智能体服务已启动 (PID: $AGENT_PID)"
echo ""

# 启动游戏服务器（后台运行）
echo "🎮 启动游戏服务器..."
cd assets
nohup python -m http.server 8080 > /tmp/game.log 2>&1 &
GAME_PID=$!
cd "$WORK_DIR"

# 等待游戏服务器启动
sleep 2

# 检查游戏服务器是否启动成功
if ! curl -f http://localhost:8080/math_game.html >/dev/null 2>&1; then
    echo "⚠️  游戏服务器启动可能失败，请检查日志"
else
    echo "✅ 游戏服务器已启动 (PID: $GAME_PID)"
fi

echo ""
echo "=========================================="
echo "🎉 所有服务已启动成功！"
echo "=========================================="
echo ""
echo "📋 服务信息:"
echo "   智能体服务:"
echo "   - 本地访问: http://localhost:8000"
echo "   - API 文档: http://localhost:8000/docs"
echo "   - PID: $AGENT_PID"
echo ""
echo "   游戏服务器:"
echo "   - 本地访问: http://localhost:8080/math_game.html"
echo "   - PID: $GAME_PID"
echo ""
echo "   智能体与游戏已打通:"
echo "   - 对智能体说'开始游戏'即可获取游戏链接"
echo "   - 游戏完成后返回智能体获取评价"
echo ""
echo "📝 日志文件:"
echo "   - 智能体: tail -f /tmp/agent.log"
echo "   - 游戏: tail -f /tmp/game.log"
echo ""
echo "⏹️  停止服务:"
echo "   - 停止智能体: kill $AGENT_PID"
echo "   - 停止游戏: kill $GAME_PID"
echo "   - 或者运行: bash scripts/stop_all.sh"
echo ""
echo "🌐 外网访问（可选）:"
echo "   - 运行: bash scripts/start_ngrok.sh"
echo "   - 然后使用 ngrok 提供的公网地址访问"
echo ""
echo "=========================================="
echo ""

# 保存 PID 到文件，方便停止服务
echo "$AGENT_PID" > /tmp/agent.pid
echo "$GAME_PID" > /tmp/game.pid

# 提示按 Enter 退出
read -p "按 Enter 键退出（服务将继续在后台运行）..."

echo ""
echo "💡 提示: 服务仍在后台运行"
echo "   查看智能体日志: tail -f /tmp/agent.log"
echo "   查看游戏日志: tail -f /tmp/game.log"
echo ""
