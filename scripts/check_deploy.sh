#!/bin/bash
# 部署前检查脚本

echo "=========================================="
echo "🔍 部署前检查"
echo "=========================================="
echo ""

# 检查1: 文件结构
echo "📋 检查文件结构..."
required_files=(
    "src/agents/agent.py"
    "src/main.py"
    "config/agent_llm_config.json"
    "assets/math_game.html"
    "requirements.txt"
)

all_files_exist=true
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file 不存在"
        all_files_exist=false
    fi
done

if [ "$all_files_exist" = true ]; then
    echo "   ✅ 所有必要文件都存在"
else
    echo "   ❌ 缺少必要文件，请检查"
    exit 1
fi

echo ""

# 检查2: Git仓库
echo "📋 检查Git仓库..."
if [ -d ".git" ]; then
    echo "   ✅ Git仓库已初始化"
    git remote -v | head -1 | sed 's/^/   /'
else
    echo "   ⚠️  Git仓库未初始化"
    echo "   💡 运行: git init"
fi

echo ""

# 检查3: 依赖文件
echo "📋 检查依赖文件..."
if [ -f "requirements.txt" ]; then
    echo "   ✅ requirements.txt 存在"
    echo "   📦 依赖列表:"
    head -10 requirements.txt | sed 's/^/      /'
else
    echo "   ❌ requirements.txt 不存在"
fi

echo ""

# 检查4: 配置文件
echo "📋 检查配置文件..."
if [ -f "config/agent_llm_config.json" ]; then
    echo "   ✅ 配置文件存在"
    if python -m json.tool config/agent_llm_config.json > /dev/null 2>&1; then
        echo "   ✅ 配置文件格式正确"
    else
        echo "   ❌ 配置文件格式错误"
    fi
else
    echo "   ❌ 配置文件不存在"
fi

echo ""

# 检查5: 代码语法
echo "📋 检查代码语法..."
python_files=(
    "src/agents/agent.py"
    "src/tools/math_problem_tool.py"
    "src/tools/game_interaction_tool.py"
)

syntax_ok=true
for file in "${python_files[@]}"; do
    if [ -f "$file" ]; then
        if python -m py_compile "$file" 2>/dev/null; then
            echo "   ✅ $file"
        else
            echo "   ❌ $file 语法错误"
            syntax_ok=false
        fi
    fi
done

if [ "$syntax_ok" = true ]; then
    echo "   ✅ 所有Python文件语法正确"
else
    echo "   ❌ 部分文件存在语法错误"
fi

echo ""

# 检查6: 游戏文件
echo "📋 检查游戏文件..."
if [ -f "assets/math_game.html" ]; then
    size=$(wc -c < assets/math_game.html)
    echo "   ✅ 游戏文件存在 ($size 字节)"
    if [ "$size" -gt 10000 ]; then
        echo "   ✅ 文件大小正常"
    else
        echo "   ⚠️  文件可能不完整"
    fi
else
    echo "   ❌ 游戏文件不存在"
fi

echo ""

# 检查7: 环境变量模板
echo "📋 环境变量..."
if [ -f ".env.example" ]; then
    echo "   ✅ 环境变量模板存在"
else
    echo "   💡 建议创建 .env.example 文件"
    echo "      包含需要配置的环境变量列表"
fi

echo ""

# 检查8: 文档
echo "📋 检查文档..."
docs=(
    "README.md"
    "docs/部署方案对比.md"
    "docs/Coze平台部署指南.md"
)

for doc in "${docs[@]}"; do
    if [ -f "$doc" ]; then
        echo "   ✅ $doc"
    else
        echo "   ℹ️  $doc (可选)"
    fi
done

echo ""

# 总结
echo "=========================================="
echo "✅ 检查完成"
echo "=========================================="
echo ""
echo "📋 检查结果:"
echo "   - 文件结构: $([ "$all_files_exist" = true ] && echo "✅ 通过" || echo "❌ 未通过")"
echo "   - 代码语法: $([ "$syntax_ok" = true ] && echo "✅ 通过" || echo "❌ 未通过")"
echo ""

if [ "$all_files_exist" = true ] && [ "$syntax_ok" = true ]; then
    echo "🎉 恭喜！所有检查都通过了！"
    echo ""
    echo "🚀 下一步："
    echo "   1. 提交代码: git add . && git commit -m 'ready to deploy'"
    echo "   2. 推送到远程: git push"
    echo "   3. 在Coze平台创建工作流"
    echo "   4. 部署游戏页面到Vercel"
    echo ""
    echo "📖 详细文档:"
    echo "   - docs/部署方案对比.md"
    echo "   - docs/Coze平台部署指南.md"
else
    echo "⚠️  还有问题需要解决，请检查上述错误"
fi

echo "=========================================="
