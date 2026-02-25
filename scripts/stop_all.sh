#!/bin/bash
# 停止所有服务（智能体 + 游戏服务器）

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=========================================="
echo "⏹️  停止简便运算系统"
echo "=========================================="
echo ""

# 停止智能体服务
if [ -f /tmp/agent.pid ]; then
    AGENT_PID=$(cat /tmp/agent.pid)
    if ps -p $AGENT_PID > /dev/null 2>&1; then
        echo "🤖 停止智能体服务 (PID: $AGENT_PID)..."
        kill $AGENT_PID
        rm /tmp/agent.pid
        echo "✅ 智能体服务已停止"
    else
        echo "⚠️  智能体服务未运行"
        rm -f /tmp/agent.pid
    fi
else
    echo "⚠️  智能体服务 PID 文件不存在"
fi

echo ""

# 停止游戏服务器
if [ -f /tmp/game.pid ]; then
    GAME_PID=$(cat /tmp/game.pid)
    if ps -p $GAME_PID > /dev/null 2>&1; then
        echo "🎮 停止游戏服务器 (PID: $GAME_PID)..."
        kill $GAME_PID
        rm /tmp/game.pid
        echo "✅ 游戏服务器已停止"
    else
        echo "⚠️  游戏服务器未运行"
        rm -f /tmp/game.pid
    fi
else
    echo "⚠️  游戏服务器 PID 文件不存在"
fi

echo ""

# 额外清理：杀死所有 uvicorn 和 http.server 进程
echo "🧹 清理残留进程..."

# 杀死 uvicorn 进程
pkill -f "uvicorn src.main:app" 2>/dev/null && echo "✅ 已清理 uvicorn 进程" || echo "✅ 无 uvicorn 残留进程"

# 杀死 http.server 进程
pkill -f "python -m http.server 8080" 2>/dev/null && echo "✅ 已清理 http.server 进程" || echo "✅ 无 http.server 残留进程"

echo ""

# 检查端口
echo "📋 端口状态:"
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "   ⚠️  端口 8000 仍被占用（智能体）"
else
    echo "   ✅ 端口 8000 已释放"
fi

if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "   ⚠️  端口 8080 仍被占用（游戏）"
else
    echo "   ✅ 端口 8080 已释放"
fi

echo ""
echo "=========================================="
echo "🎉 所有服务已停止！"
echo "=========================================="
