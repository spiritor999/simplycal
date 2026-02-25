#!/bin/bash
# 使用 ngrok 实现智能体外网访问（快速测试方案）

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK_DIR="${COZE_WORKSPACE_PATH:-$(dirname "$SCRIPT_DIR")}"
cd "$WORK_DIR"

# 默认配置
PORT=${PORT:-8000}
NGROK_PORT=${NGROK_PORT:-4040}

echo "=========================================="
echo "🌐 使用 ngrok 实现智能体外网访问"
echo "=========================================="
echo ""

# 检查 ngrok
if ! command -v ngrok &> /dev/null; then
    echo "❌ ngrok 未安装"
    echo ""
    echo "💡 安装方法:"
    echo "   macOS:   brew install ngrok"
    echo "   Linux:   curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null"
    echo "            echo 'deb https://ngrok-agent.s3.amazonaws.com buster main' | sudo tee /etc/apt/sources.list.d/ngrok.list"
    echo "            sudo apt update && sudo apt install ngrok"
    echo ""
    echo "   或者访问: https://ngrok.com/download"
    echo ""
    exit 1
fi

# 检查端口是否被占用
if ! lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  智能体服务未在端口 $PORT 运行"
    echo ""
    echo "💡 请先启动智能体服务:"
    echo "   bash scripts/start_agent_server.sh"
    echo ""
    exit 1
fi

echo "✅ 智能体服务正在运行（端口 $PORT）"
echo ""
echo "🚀 正在启动 ngrok 隧道..."
echo ""

# 启动 ngrok
ngrok http $PORT --log=stdout

# 退出时显示信息
trap 'echo ""; echo "💡 提示: ngrok 隧道已关闭";' EXIT
