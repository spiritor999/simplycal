#!/bin/bash
# 简便运算智能体 - 部署脚本
# 独立部署，不影响现有生产项目

set -e

echo "=========================================="
echo "🚀 简便运算智能体 - 部署脚本"
echo "=========================================="
echo ""

# 检查 Docker 是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装，请先安装 Docker"
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose 未安装，请先安装 Docker Compose"
    exit 1
fi

echo "✅ Docker 环境检查通过"
echo ""

# 检查端口是否被占用
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo "⚠️  端口 $1 已被占用"
        return 1
    else
        echo "✅ 端口 $1 可用"
        return 0
    fi
}

echo "📋 检查端口占用..."
check_port 8000 || echo "   💡 端口 8000 被占用，请修改 docker-compose-simplecal.yml 中的端口映射"
echo ""

# 检查环境变量文件
if [ ! -f ".env.simplecal" ]; then
    echo "⚠️  环境变量文件不存在: .env.simplecal"
    echo ""
    echo "💡 请先创建环境变量文件："
    echo "   cp .env.simplecal.example .env.simplecal"
    echo "   vim .env.simplecal  # 编辑配置"
    echo ""
    read -p "是否现在创建环境变量文件？(y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        cp .env.simplecal.example .env.simplecal
        echo "✅ 已创建 .env.simplecal"
        echo "📝 请编辑此文件，配置 COZE_WORKLOAD_IDENTITY_API_KEY"
        echo "   vim .env.simplecal"
        echo ""
        read -p "配置完成后按 Enter 继续..."
    else
        echo "❌ 需要配置环境变量才能继续"
        exit 1
    fi
fi

# 加载环境变量
if [ -f ".env.simplecal" ]; then
    export $(cat .env.simplecal | grep -v '^#' | xargs)
    echo "✅ 环境变量已加载"
    echo ""
fi

# 检查必需的环境变量
if [ -z "$COZE_WORKLOAD_IDENTITY_API_KEY" ]; then
    echo "❌ 缺少必需的环境变量: COZE_WORKLOAD_IDENTITY_API_KEY"
    echo "💡 请在 .env.simplecal 文件中配置"
    exit 1
fi

# 检查配置文件
if [ ! -f "config/agent_llm_config.json" ]; then
    echo "❌ 配置文件不存在: config/agent_llm_config.json"
    exit 1
fi

echo "✅ 配置文件检查通过"
echo ""

# 检查智能体代码
if [ ! -f "src/agents/agent.py" ]; then
    echo "❌ 智能体代码不存在: src/agents/agent.py"
    exit 1
fi

echo "✅ 智能体代码检查通过"
echo ""

# 开始部署
echo "🚀 开始部署..."
echo ""

# 停止现有服务（如果有）
echo "📋 停止现有服务..."
docker-compose -f docker-compose-simplecal.yml down 2>/dev/null || true

# 构建镜像
echo "📦 构建镜像..."
docker-compose -f docker-compose-simplecal.yml build

# 启动服务
echo "🎬 启动服务..."
docker-compose -f docker-compose-simplecal.yml up -d

# 等待服务启动
echo "⏳ 等待服务启动..."
sleep 5

# 检查服务状态
echo ""
echo "📊 服务状态:"
docker-compose -f docker-compose-simplecal.yml ps

# 检查健康状态
echo ""
echo "🏥 健康检查:"
if curl -f http://localhost:8000/health >/dev/null 2>&1; then
    echo "✅ 智能体服务运行正常"
else
    echo "⚠️  智能体服务可能未正常启动"
    echo "💡 查看日志: docker-compose -f docker-compose-simplecal.yml logs agent"
fi

echo ""
echo "=========================================="
echo "🎉 部署完成！"
echo "=========================================="
echo ""
echo "📋 服务信息:"
echo "   智能体服务: http://localhost:8000"
echo "   API 文档: http://localhost:8000/docs"
echo "   健康检查: http://localhost:8000/health"
echo ""
echo "📝 常用命令:"
echo "   查看日志: docker-compose -f docker-compose-simplecal.yml logs -f agent"
echo "   停止服务: docker-compose -f docker-compose-simplecal.yml down"
echo "   重启服务: docker-compose -f docker-compose-simplecal.yml restart"
echo "   查看状态: docker-compose -f docker-compose-simplecal.yml ps"
echo ""
echo "🌐 外网访问:"
echo "   智能体页面: https://coze-coding-project.tos.coze.site/coze_storage_7599855582224318498/agent_2378e586.html?sign=..."
echo "   游戏页面: https://coze-coding-project.tos.coze.site/coze_storage_7599855582224318498/math_game_7156ba9f.html?sign=..."
echo ""
echo "💡 在智能体页面配置 API 地址:"
echo "   如果在服务器上: http://服务器IP:8000"
echo "   如果有域名: https://your-domain.com"
echo ""
