# 🧮 简便运算智能体 - 小学三年级数学学习助手

一个基于 LangChain 的智能体，为小学三年级学生提供简便运算讲解、练习和游戏化学习体验。

## ✨ 主要功能

### 🤖 智能讲解
- 详细讲解简便运算方法
- 支持凑十法、凑整法、交换律、结合律等方法
- 个性化学习建议

### 📝 智能练习
- 自动生成练习题
- 即时反馈和讲解
- 难度自适应

### 🎮 趣味游戏
- 三个难度递进（简单/中等/困难）
- 只包含加减法（专注核心）
- 闪电老师详细讲解错题
- 与智能体完全打通
- 支持逐步计算讲解

### 🔄 智能体与游戏联动
- 智能体提供游戏链接
- 游戏完成后返回智能体
- 智能体根据游戏结果给出评价和建议
- 形成完整的学习闭环

## 🚀 快速开始

### 前置要求
- Python 3.12+
- pip

### 一键启动

```bash
# 启动所有服务（智能体 + 游戏服务器）
bash scripts/start_all.sh
```

服务启动后，你可以访问：
- 智能体 API: http://localhost:8000
- API 文档: http://localhost:8000/docs
- 游戏页面: http://localhost:8080/math_game.html

### 外网访问（可选）

#### 使用 ngrok 快速实现外网访问

1. 安装 ngrok:
   - macOS: `brew install ngrok`
   - Linux: 参考 [部署指南](docs/智能体部署指南.md)

2. 启动 ngrok:
   ```bash
   bash scripts/start_ngrok.sh
   ```

3. 使用 ngrok 提供的公网地址访问

#### 游戏公网访问链接

```
https://coze-coding-project.tos.coze.site/coze_storage_7599855582224318498/math_game_b417786f.html?sign=1803563292-a7ff2330be-0-f3e5b9d6facbdd1a26b92a4dc62d0c680b91bc1f6be5042e090ff2098d8f3d5a
```

## 📚 使用指南

### 基础对话

```bash
# 使用 curl
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{"query": "你好"}'

# 或访问 API 文档测试
# http://localhost:8000/docs
```

### 智能体与游戏交互

#### 1. 启动游戏
```
对智能体说："开始游戏"

智能体返回游戏链接和难度选择
```

#### 2. 玩游戏
- 点击游戏链接
- 选择难度（简单/中等/困难）
- 玩10道题
- 查看得分和讲解

#### 3. 返回智能体
- 点击"返回智能体"按钮
- 告诉智能体游戏结果

#### 4. 获取评价
```
对智能体说："游戏已完成，得了85分，做对9题，难度中等"

智能体给出评价和建议
```

详细说明请参考：[智能体与游戏集成说明](docs/智能体与游戏集成说明.md)

## 🛠️ 技术栈

- **Python 3.12**: 核心语言
- **LangChain**: AI 智能体框架
- **LangGraph**: 状态管理和工作流
- **FastAPI**: Web 服务框架
- **Uvicorn**: ASGI 服务器
- **HTML/CSS/JavaScript**: 游戏前端
- **Docker**: 容器化部署

## 📁 项目结构

```
.
├── config/                     # 配置文件
│   └── agent_llm_config.json   # 模型配置
├── src/
│   ├── agents/                 # 智能体代码
│   │   └── agent.py            # 主智能体
│   ├── tools/                  # 工具定义
│   │   └── game_interaction_tool.py  # 游戏交互工具
│   └── main.py                 # FastAPI 主入口
├── assets/                     # 静态资源
│   └── math_game.html          # 游戏页面
├── scripts/                    # 启动脚本
│   ├── start_all.sh            # 一键启动所有服务
│   ├── stop_all.sh             # 停止所有服务
│   ├── start_agent_server.sh   # 启动智能体服务
│   ├── start_ngrok.sh          # 启动 ngrok 外网访问
│   └── start_game_server.sh    # 启动游戏服务器
├── docs/                       # 文档
│   ├── 快速启动指南.md         # 3分钟上手
│   ├── 智能体部署指南.md       # 详细部署方案
│   └── 智能体与游戏集成说明.md # 集成说明
├── Dockerfile                  # Docker 镜像
├── docker-compose.yml          # Docker Compose 配置
└── requirements.txt            # Python 依赖
```

## 🔧 常用命令

### 启动服务
```bash
# 启动所有服务
bash scripts/start_all.sh

# 只启动智能体
bash scripts/start_agent_server.sh

# 使用自定义端口
PORT=8001 bash scripts/start_agent_server.sh
```

### 停止服务
```bash
# 停止所有服务
bash scripts/stop_all.sh
```

### 查看日志
```bash
# 智能体日志
tail -f /tmp/agent.log

# 游戏日志
tail -f /tmp/game.log

# 应用日志
tail -f /app/work/logs/bypass/app.log
```

### 健康检查
```bash
curl http://localhost:8000/health
```

## 📖 文档

- [快速启动指南](docs/快速启动指南.md) - 3分钟上手
- [智能体部署指南](docs/智能体部署指南.md) - 详细部署方案（本地、ngrok、云服务器、Docker）
- [智能体与游戏集成说明](docs/智能体与游戏集成说明.md) - 完整的集成和使用说明

## 🌐 部署方案

### 本地启动
```bash
bash scripts/start_agent_server.sh
```

### ngrok 内网穿透（快速演示）
```bash
# 1. 启动智能体
bash scripts/start_all.sh

# 2. 启动 ngrok
bash scripts/start_ngrok.sh
```

### 云服务器部署
详见 [智能体部署指南](docs/智能体部署指南.md)

### Docker 部署
```bash
# 开发环境
docker-compose up

# 生产环境
docker-compose up -d
```

## 🔐 环境变量

智能体服务需要以下环境变量：

- `COZE_WORKSPACE_PATH`: 工作目录路径（默认: `/workspace/projects`）
- `COZE_INTEGRATION_MODEL_BASE_URL`: 模型 API 地址
- `COZE_WORKLOAD_IDENTITY_API_KEY`: 模型 API 密钥

## 🎮 游戏功能

### 难度设置
- **简单**: 两个数加减法（两位数）
- **中等**: 三个数加减法（两位数）
- **困难**: 三个数加减法（三位数）

### 游戏规则
- 每关10道题
- 答对+10分，答错-5分
- 选择方法、列式子、给结果
- 错题有详细讲解

### 支持的方法
**加法题目：**
- 凑十法
- 凑整法
- 加法交换律
- 加法结合律

**减法题目：**
- 破十法
- 凑整法
- 加法交换律
- 加法结合律

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License

## 🔗 相关链接

- **GitHub**: https://github.com/spiritor999/simplycal
- **Gitee**: https://gitee.com/spiritor/simplecal

## 📞 支持

如有问题，请提交 Issue 或查看文档。

---

**快速上手：**
```bash
# 1. 一键启动
bash scripts/start_all.sh

# 2. 访问 API 文档
# http://localhost:8000/docs

# 3. 访问游戏
# http://localhost:8080/math_game.html

# 4. 停止服务
bash scripts/stop_all.sh
```

祝你使用愉快！🎉
