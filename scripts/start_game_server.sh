#!/bin/bash
# 启动游戏专用HTTP服务器

echo "=========================================="
echo "🎮 启动简便运算游戏服务器"
echo "=========================================="
echo ""

# 检查端口
PORT=8080
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo "⚠️  端口 $PORT 已被占用"
    echo "💡 请尝试使用其他端口"
    exit 1
fi

# 获取游戏文件路径
GAME_FILE="assets/math_game.html"

if [ ! -f "$GAME_FILE" ]; then
    echo "❌ 游戏文件不存在: $GAME_FILE"
    exit 1
fi

echo "✅ 游戏文件已找到: $GAME_FILE"
echo ""
echo "🚀 正在启动HTTP服务器..."
echo ""
echo "📋 服务器信息:"
echo "   端口: $PORT"
echo "   访问地址: http://localhost:$PORT/$GAME_FILE"
echo "   或者: http://127.0.0.1:$PORT/$GAME_FILE"
echo ""
echo "⏳ 按 Ctrl+C 停止服务器"
echo "=========================================="
echo ""

# 启动HTTP服务器
python3 -m http.server $PORT
