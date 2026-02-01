# 🔐 Git 推送认证配置指南

## 当前问题

代码已准备好，但推送需要身份认证：

```
fatal: could not read Username for 'https://gitee.com': No such device or address
```

---

## 🎯 解决方案（任选一种）

### 方案1：使用 HTTPS + 个人访问令牌（推荐新手）

#### 步骤1：获取 Gitee 个人访问令牌

1. 访问 Gitee：https://gitee.com
2. 登录你的账号
3. 点击右上角头像 → **设置**
4. 左侧菜单 → **私人令牌** → **生成新令牌**
5. 填写令牌信息：
   - **令牌描述**：Coze 沙箱推送
   - **权限**：至少勾选 **projects**（仓库读写权限）
6. 点击 **提交**
7. **重要**：复制生成的令牌（只显示一次！）

#### 步骤2：在云端沙箱配置认证

告诉我你的：
- Gitee 用户名（不是邮箱，是用户名）
- 刚刚生成的个人访问令牌

我会帮你配置并推送。

---

### 方案2：使用 SSH（推荐熟练用户）

#### 步骤1：生成 SSH 密钥

在云端沙箱执行：
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# 连续按3次回车（使用默认配置）
```

#### 步骤2：查看公钥

```bash
cat ~/.ssh/id_ed25519.pub
```

#### 步骤3：添加到 Gitee

1. 复制输出的公钥内容
2. 访问 Gitee：https://gitee.com
3. 点击右上角头像 → **设置**
4. 左侧菜单 → **SSH 公钥**
5. 粘贴公钥
6. 点击 **确定**

#### 步骤4：切换到 SSH 地址

```bash
git remote set-url origin git@gitee.com:spiritor/simplecal.git
```

#### 步骤5：测试连接

```bash
ssh -T git@gitee.com
# 应该显示：Hi spiritor! You've successfully authenticated...
```

#### 步骤6：推送

```bash
git push -u origin main
```

---

## 📊 方案对比

| 方案 | 优点 | 缺点 | 适用人群 |
|------|------|------|---------|
| **HTTPS + Token** | 简单快速 | 需要提供凭据 | 新手、快速推送 |
| **SSH** | 安全持久 | 配置稍复杂 | 常用 Git、多仓库 |

---

## 🎯 我的建议

### 如果你：
- **不熟悉 Git/SSH** → 选择 **方案1（HTTPS + Token）**
- **想要快速搞定** → 选择 **方案1（HTTPS + Token）**
- **长期使用 Git** → 选择 **方案2（SSH）**

---

## 🤖 我可以帮你做什么

### 方案1（HTTPS + Token）
你提供：
- Gitee 用户名
- 个人访问令牌

我会：
- 配置 Git 凭据
- 推送代码到 Gitee

### 方案2（SSH）
你提供：
- 你的邮箱地址（用于生成密钥）

我会：
- 生成 SSH 密钥
- 给你公钥内容
- 指导你添加到 Gitee
- 完成推送

---

## ❓ 接下来怎么做？

### 请选择方案：

**选择方案1（推荐）**
```
请告诉我：
1. Gitee 用户名
2. 个人访问令牌

然后我会立即推送！
```

**选择方案2**
```
请告诉我你的邮箱地址，我会生成 SSH 密钥并指导你配置。
```

---

**选择一个方案，告诉我，我马上帮你推送代码！** 🚀
