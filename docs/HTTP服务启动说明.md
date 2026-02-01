# 🚀 HTTP 服务启动成功！

## ✅ 服务状态

**HTTP 服务已成功启动并运行中！**

| 项目 | 值 |
|------|-----|
| **服务地址** | http://localhost:8000 |
| **监听地址** | 0.0.0.0:8000 |
| **服务状态** | ✅ 运行中 |
| **健康检查** | ✅ 正常 |

---

## 🌐 API 端点

### 1. 健康检查
```
GET /health
```

**测试**：
```bash
curl http://localhost:8000/health
```

**响应**：
```json
{
  "status": "ok",
  "message": "Service is running"
}
```

---

### 2. 同步运行（非流式）
```
POST /run
```

**请求示例**：
```bash
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "type": "query",
    "session_id": "test-123",
    "content": {
      "query": {
        "prompt": [{
          "type": "text",
          "content": {"text": "你好，帮我讲解简便运算"}
        }]
      }
    }
  }'
```

---

### 3. 流式运行（SSE）
```
POST /stream_run
```

**请求示例**：
```bash
curl -X POST http://localhost:8000/stream_run \
  -H "Content-Type: application/json" \
  -d '{
    "type": "query",
    "session_id": "test-123",
    "content": {
      "query": {
        "prompt": [{
          "type": "text",
          "content": {"text": "出几道简便运算练习题"}
        }]
      }
    }
  }'
```

---

### 4. 取消执行
```
POST /cancel/{run_id}
```

**请求示例**：
```bash
curl -X POST http://localhost:8000/cancel/{run_id}
```

---

### 5. OpenAI 兼容接口
```
POST /v1/chat/completions
```

**请求示例**：
```bash
curl -X POST http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "doubao-seed-1-6-251015",
    "messages": [
      {"role": "user", "content": "你好，帮我讲解简便运算"}
    ],
    "stream": true
  }'
```

---

### 6. 获取工作流参数
```
GET /graph_parameter
```

**请求示例**：
```bash
curl http://localhost:8000/graph_parameter
```

---

## 🎮 游戏页面访问

### 方式1：直接访问游戏文件
```
http://localhost:8000/assets/math_game.html
```

### 方式2：通过服务路由
需要配置静态文件路由才能访问。

---

## 🧪 测试服务

### 快速测试

```bash
# 1. 健康检查
curl http://localhost:8000/health

# 2. 简单对话
curl -X POST http://localhost:8000/run \
  -H "Content-Type: application/json" \
  -d '{
    "type": "query",
    "session_id": "test-001",
    "content": {
      "query": {
        "prompt": [{
          "type": "text",
          "content": {"text": "你好"}
        }]
      }
    }
  }'
```

---

## 📝 启动参数

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `-m` | 运行模式 (http, flow, node, agent) | http |
| `-p` | HTTP 端口 | 5000 |
| `-n` | 节点ID（node模式） | - |
| `-i` | 输入JSON字符串（flow/node模式） | - |

### 启动命令

```bash
# 基本启动
python main.py -m http -p 8000

# 开发模式（自动重载）
python main.py -m http -p 8000

# 指定不同端口
python main.py -m http -p 5000
```

---

## 🔍 查看日志

日志文件位置：
```
/app/work/logs/bypass/app.log
```

查看最新日志：
```bash
tail -n 20 /app/work/logs/bypass/app.log
```

---

## 📊 服务架构

```
客户端
  ↓
HTTP 请求 (FastAPI)
  ↓
GraphService
  ↓
Agent (LangChain)
  ↓
工具调用
  ↓
返回结果
```

---

## 🛠️ 服务特性

### 支持的功能
- ✅ 同步运行（非流式）
- ✅ 流式运行（SSE）
- ✅ OpenAI 兼容接口
- ✅ 任务取消
- ✅ 健康检查
- ✅ 自动重载（开发模式）
- ✅ 错误分类与处理

### 技术栈
- FastAPI - Web 框架
- Uvicorn - ASGI 服务器
- LangChain - Agent 框架
- LangGraph - 状态管理

---

## 💡 使用场景

### 1. 本地开发测试
```bash
# 启动服务
python main.py -m http -p 8000

# 测试API
curl -X POST http://localhost:8000/run ...
```

### 2. 集成到其他应用
```python
import requests

response = requests.post(
    "http://localhost:8000/run",
    json={
        "type": "query",
        "session_id": "app-001",
        "content": {
            "query": {
                "prompt": [{
                    "type": "text",
                    "content": {"text": "你的问题"}
                }]
            }
        }
    }
)

print(response.json())
```

### 3. 流式对话
```python
import requests

response = requests.post(
    "http://localhost:8000/stream_run",
    json={...},
    stream=True
)

for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))
```

---

## ⚠️ 注意事项

### 超时配置
- 默认超时时间：900 秒（15分钟）
- 可在代码中修改 `TIMEOUT_SECONDS` 常量

### 并发限制
- 默认工作进程数：1
- 开发模式支持自动重载

### 内存管理
- 使用滑动窗口保留最近 40 条消息
- 可配置 `MAX_MESSAGES` 调整

---

## 🔄 停止服务

### 方法1：Ctrl+C
在运行终端按 `Ctrl+C` 停止服务。

### 方法2：杀死进程
```bash
# 查找进程
ps aux | grep "python main.py"

# 杀死进程
kill <PID>
```

---

## 📚 相关文档

- **快速开始**：`docs/快速开始.md`
- **部署指南**：`docs/部署指南.md`
- **API 文档**：访问 http://localhost:8000/docs

---

## 🎉 服务已就绪！

现在你可以：
- ✅ 测试智能体功能
- ✅ 调用 API 接口
- ✅ 访问游戏页面
- ✅ 集成到你的应用

**开始使用吧！** 🚀
