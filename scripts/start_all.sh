#!/bin/bash
# 一键启动脚本 - 同时启动游戏服务器和智能体服务

echo "=========================================="
echo "🚀 一键启动简便运算系统"
echo "=========================================="
echo ""

# 检查端口
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        echo "⚠️  端口 $port 已被占用"
        return 1
    else
        echo "✅ 端口 $port 可用"
        return 0
    fi
}

# 检查文件
check_files() {
    local files=(
        "assets/math_game.html"
        "src/agents/agent.py"
        "config/agent_llm_config.json"
    )

    echo "📋 检查文件..."
    for file in "${files[@]}"; do
        if [ -f "$file" ]; then
            echo "   ✅ $file"
        else
            echo "   ❌ $file 不存在"
            return 1
        fi
    done
    echo ""
}

# 启动游戏服务器
start_game_server() {
    echo "🎮 启动游戏服务器（端口8080）..."
    nohup python -m http.server 8080 > logs/game_server.log 2>&1 &
    GAME_PID=$!
    echo "   ✅ 游戏服务器已启动 (PID: $GAME_PID)"
    echo "   访问地址: http://localhost:8080/assets/math_game.html"
    echo ""

    # 等待服务器启动
    sleep 2
    if curl -I http://localhost:8080/assets/math_game.html 2>/dev/null | grep -q "200"; then
        echo "   ✅ 游戏服务器运行正常"
    else
        echo "   ⚠️  游戏服务器启动失败，请检查日志"
        tail -20 logs/game_server.log
    fi
    echo ""
}

# 启动智能体服务
start_agent_server() {
    echo "🤖 启动智能体服务（端口8000）..."
    nohup bash scripts/http_run.sh -p 8000 > logs/agent_server.log 2>&1 &
    AGENT_PID=$!
    echo "   ✅ 智能体服务已启动 (PID: $AGENT_PID)"
    echo "   API地址: http://localhost:8000"
    echo ""

    # 等待服务启动
    sleep 3
    if curl -I http://localhost:8000 2>/dev/null | grep -q "200"; then
        echo "   ✅ 智能体服务运行正常"
    else
        echo "   ⚠️  智能体服务启动失败，请检查日志"
        tail -20 logs/agent_server.log
    fi
    echo ""
}

# 创建日志目录
mkdir -p logs

# 检查端口
echo "📡 检查端口..."
check_port 8080 && check_port 8000 || exit 1
echo ""

# 检查文件
check_files || exit 1

# 启动服务
start_game_server
start_agent_server

# 保存PID
echo "$GAME_PID" > logs/game_server.pid
echo "$AGENT_PID" > logs/agent_server.pid

# 显示启动信息
echo "=========================================="
echo "✅ 所有服务已启动！"
echo "=========================================="
echo ""
echo "📋 服务信息:"
echo "   游戏服务器: http://localhost:8080"
echo "   智能体服务: http://localhost:8000"
echo ""
echo "🎮 游戏地址:"
echo "   http://localhost:8080/assets/math_game.html"
echo ""
echo "📝 日志文件:"
echo "   游戏服务器: logs/game_server.log"
echo "   智能体服务: logs/agent_server.log"
echo ""
echo "⏹️  停止服务:"
echo "   bash scripts/stop_all.sh"
echo ""
echo "=========================================="
echo "🎉 系统已就绪，开始使用吧！"
echo "=========================================="
