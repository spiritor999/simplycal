#!/bin/bash
# 启动智能体 HTTP 服务（支持外网访问）

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK_DIR="${COZE_WORKSPACE_PATH:-$(dirname "$SCRIPT_DIR")}"
cd "$WORK_DIR"

# 默认配置
PORT=${PORT:-8000}
HOST=${HOST:-0.0.0.0}
WORKERS=${WORKERS:-1}

echo "=========================================="
echo "🤖 启动简便运算智能体服务"
echo "=========================================="
echo ""

# 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装"
    exit 1
fi

# 检查依赖
echo "📦 检查依赖..."
if ! python3 -c "import fastapi" 2>/dev/null; then
    echo "⚠️  正在安装依赖..."
    pip install -q fastapi uvicorn
fi

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

# 检查端口是否被占用
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "⚠️  端口 $PORT 已被占用"
    echo "💡 请使用 PORT=8001 启动"
    exit 1
fi

echo "✅ 依赖检查完成"
echo ""
echo "🚀 正在启动智能体服务..."
echo ""
echo "📋 服务信息:"
echo "   主机: $HOST"
echo "   端口: $PORT"
echo "   工作进程: $WORKERS"
echo ""
echo "🔗 访问地址:"
echo "   - 本地: http://localhost:$PORT"
echo "   - 内网: http://$HOST:$PORT"
echo "   - API文档: http://localhost:$PORT/docs"
echo ""
echo "⏳ 按 Ctrl+C 停止服务"
echo "=========================================="
echo ""

# 启动服务
if [ "$WORKERS" -eq 1 ]; then
    # 单进程模式（开发）
    uvicorn src.main:app --host "$HOST" --port "$PORT" --reload
else
    # 多进程模式（生产）
    uvicorn src.main:app --host "$HOST" --port "$PORT" --workers "$WORKERS"
fi
