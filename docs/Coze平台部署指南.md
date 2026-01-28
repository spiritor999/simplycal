# 🚀 Coze平台部署指南

## 📋 部署前准备

### 1. 确认代码结构
```
/workspace/projects/
├── src/
│   ├── agents/
│   │   └── agent.py          # 智能体代码
│   ├── tools/
│   │   ├── math_problem_tool.py
│   │   └── game_interaction_tool.py
│   └── main.py               # 入口文件
├── config/
│   └── agent_llm_config.json # 配置文件
├── assets/
│   └── math_game.html        # 游戏页面
└── requirements.txt          # 依赖列表
```

### 2. 检查依赖
```bash
cat requirements.txt
```

应该包含：
```
langchain>=0.1.0
langchain-openai>=0.0.5
langgraph>=0.0.26
coze-coding-dev-sdk
uvicorn
fastapi
```

### 3. 本地测试
```bash
python -m pytest tests/
# 或
python src/main.py
```

---

## 🚀 部署步骤

### 步骤1: 推送代码到Git

```bash
# 初始化Git（如果还没有）
git init
git add .
git commit -m "feat: 添加简便运算智能体"

# 推送到远程仓库
# 方法1: GitHub
git remote add origin https://github.com/你的用户名/项目名.git
git push -u origin main

# 方法2: Gitee
git remote add origin https://gitee.com/你的用户名/项目名.git
git push -u origin master
```

### 步骤2: 在Coze平台创建工作流

1. **登录Coze平台**
   - 访问 Coze 平台
   - 登录你的账号

2. **创建新工作流**
   - 点击"创建工作流"
   - 选择"从Git导入"
   - 输入你的Git仓库地址
   - 选择分支（main或master）

3. **配置工作流**
   - 工作流名称：`简便运算智能体`
   - 描述：`小学三年级简便运算学习助手`
   - 触发方式：API触发

4. **配置环境变量**
   - COZE_WORKLOAD_IDENTITY_API_KEY：从Coze平台获取
   - COZE_INTEGRATION_MODEL_BASE_URL：模型服务地址
   - 其他需要的环境变量

5. **配置依赖**
   - 平台会自动读取 `requirements.txt`
   - 确认所有依赖都已列出

6. **配置入口**
   - 入口文件：`src/main.py`
   - 启动命令：`python src/main.py`
   - 端口：8000

### 步骤3: 部署游戏页面

#### 选项A: 部署到Vercel（推荐）

```bash
# 1. 安装Vercel CLI
npm install -g vercel

# 2. 登录Vercel
vercel login

# 3. 部署
cd assets
vercel

# 4. 记录返回的公网链接
# 例如: https://your-project.vercel.app/math_game.html
```

#### 选项B: 部署到GitHub Pages

```bash
# 1. 将游戏文件放到仓库的docs目录
cp assets/math_game.html docs/

# 2. 推送到GitHub
git add docs/
git commit -m "添加游戏页面"
git push

# 3. 在GitHub仓库设置中启用GitHub Pages
# Settings -> Pages -> Source: docs/
```

#### 选项C: 直接使用对象存储

```bash
# 如果有对象存储服务
# 上传 math_game.html
# 获取公网访问链接
```

### 步骤4: 更新智能体配置

编辑 `src/tools/game_interaction_tool.py`，更新游戏链接：

```python
# 将游戏链接更新为部署后的地址
http_link = "https://your-project.vercel.app/math_game.html"
```

或者使用环境变量：

```python
import os
http_link = os.getenv("GAME_URL", "http://localhost:8080/game.html")
```

### 步骤5: 重新部署智能体

```bash
# 更新代码
git add .
git commit -m "feat: 更新游戏链接为部署地址"
git push

# Coze平台会自动检测并重新部署
```

---

## ✅ 验证部署

### 1. 测试智能体
```bash
# 获取Coze平台提供的API地址
curl -X POST https://your-coze-url/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{"role": "user", "content": "你好"}],
    "session_id": "test"
  }'
```

### 2. 测试游戏页面
在浏览器中打开：
```
https://your-project.vercel.app/math_game.html
```

### 3. 测试完整流程
- 在智能体中说"开始游戏"
- 点击返回的链接
- 玩游戏
- 提交结果
- 确认收到反馈

---

## 🎯 获取公网链接

### Coze平台链接
部署成功后，Coze平台会提供一个：
- API访问链接
- Web界面链接
- 可以分享给其他人的链接

### 游戏页面链接
根据你选择的部署方式：
- Vercel: `https://your-project.vercel.app/math_game.html`
- GitHub Pages: `https://your-username.github.io/your-repo/math_game.html`

---

## 📝 环境变量配置

在Coze平台中配置以下环境变量：

```bash
# API密钥
COZE_WORKLOAD_IDENTITY_API_KEY=your_api_key

# 模型服务地址
COZE_INTEGRATION_MODEL_BASE_URL=https://api.coze.com

# 游戏页面地址
GAME_URL=https://your-project.vercel.app/math_game.html

# 其他配置
PORT=8000
LOG_LEVEL=INFO
```

---

## 🔧 常见问题

### Q1: 部署失败怎么办？
**A:** 检查以下几点：
1. requirements.txt 是否完整
2. 入口文件配置是否正确
3. 环境变量是否设置
4. 查看部署日志

### Q2: 如何更新代码？
**A:**
```bash
git add .
git commit -m "更新描述"
git push
# Coze平台会自动检测并重新部署
```

### Q3: 如何查看日志？
**A:** 在Coze平台的工作流详情页面，点击"日志"查看

### Q4: 游戏链接打不开？
**A:** 确认：
1. 游戏页面已成功部署
2. 链接地址正确
3. 防火墙允许访问

---

## 🎉 部署完成

部署成功后，你会获得：

### 智能体
- 公网访问链接
- 可以分享给同学
- 可以嵌入到其他应用

### 游戏页面
- 公网访问链接
- 任何浏览器都可以访问
- 支持移动端

### 分享方式
1. **直接分享链接**
   - 智能体链接
   - 游戏链接

2. **嵌入到网站**
   - 使用iframe嵌入
   - 或调用API

3. **生成二维码**
   - 生成链接的二维码
   - 扫码即可访问

---

## 📞 需要帮助？

如果部署过程中遇到问题，告诉我：
1. **当前在哪一步？**
2. **遇到什么错误？**
3. **错误信息是什么？**

我会帮你解决！
