#!/bin/bash
# 停止所有服务脚本

echo "=========================================="
echo "⏹️  停止简便运算系统"
echo "=========================================="
echo ""

# 读取PID并停止
stop_service() {
    local pid_file=$1
    local service_name=$2

    if [ -f "$pid_file" ]; then
        pid=$(cat "$pid_file")
        if ps -p $pid > /dev/null 2>&1; then
            echo "⏹️  停止 $service_name (PID: $pid)..."
            kill $pid
            rm "$pid_file"
            echo "   ✅ $service_name 已停止"
        else
            echo "   ℹ️  $service_name 未运行"
            rm "$pid_file"
        fi
    else
        echo "   ℹ️  $service_name 未运行"
    fi
}

# 停止游戏服务器
stop_service "logs/game_server.pid" "游戏服务器"
echo ""

# 停止智能体服务
stop_service "logs/agent_server.pid" "智能体服务"
echo ""

# 检查端口
echo "📋 检查端口状态..."
if lsof -Pi :8080 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "   ⚠️  端口8080仍被占用"
else
    echo "   ✅ 端口8080已释放"
fi

if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "   ⚠️  端口8000仍被占用"
else
    echo "   ✅ 端口8000已释放"
fi

echo ""
echo "=========================================="
echo "✅ 所有服务已停止"
echo "=========================================="
