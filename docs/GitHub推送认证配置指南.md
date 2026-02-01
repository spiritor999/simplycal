# 🚀 GitHub 推送认证配置

## ⚠️ 需要认证

推送到 GitHub 需要身份认证。

---

## 🎯 解决方案

### 方案1：使用个人访问令牌（推荐）⭐⭐⭐

#### 步骤1：生成 GitHub 个人访问令牌

1. 访问 GitHub：https://github.com
2. 登录你的账号（spiritor999）
3. 点击右上角头像 → **Settings**
4. 左侧菜单最下方 → **Developer settings**
5. 左侧菜单 → **Personal access tokens** → **Tokens (classic)**
6. 点击 **Generate new token** → **Generate new token (classic)**
7. 填写令牌信息：
   - **Note**：Coze 沙箱推送
   - **Expiration**：选择过期时间（推荐 90 days 或 No expiration）
   - **Scopes**：勾选 **repo**（完整仓库权限）
8. 点击 **Generate token**
9. **重要**：复制生成的令牌（只显示一次！）

#### 步骤2：推送代码到 GitHub

**方式 A：使用 Git 凭据助手**

在推送时输入：
```
Username: spiritor999
Password: <粘贴你的个人访问令牌>
```

**方式 B：将令牌嵌入 URL（我帮你执行）**

告诉我你的 GitHub 个人访问令牌，我会帮你推送。

---

### 方案2：使用 SSH 密钥（长期使用）⭐⭐

#### 步骤1：生成 SSH 密钥

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# 连续按 3 次回车
```

#### 步骤2：查看公钥

```bash
cat ~/.ssh/id_ed25519.pub
```

#### 步骤3：添加到 GitHub

1. 复制输出的公钥内容
2. 访问 GitHub → Settings → SSH and GPG keys
3. 点击 New SSH key
4. 粘贴公钥
5. 点击 Add SSH key

#### 步骤4：切换到 SSH 地址

```bash
git remote set-url github git@github.com:spiritor999/simplycal.git
```

#### 步骤5：测试连接

```bash
ssh -T git@github.com
# 应该显示：Hi spiritor999! You've successfully authenticated...
```

#### 步骤6：推送

```bash
git push -u github main
```

---

## 🎯 我的建议

### 如果你想要快速搞定（推荐）
**使用方案 1（个人访问令牌）**

告诉我你的 GitHub 个人访问令牌，我立即帮你推送！

### 如果你长期使用 Git
**使用方案 2（SSH 密钥）**

需要多个步骤，但配置一次后永久有效。

---

## 📊 对比表

| 方案 | 优点 | 缺点 | 适用人群 |
|------|------|------|---------|
| **个人访问令牌** | 简单快速 | 令牌会过期 | 新手、快速推送 |
| **SSH 密钥** | 安全持久 | 配置稍复杂 | 熟练用户、多仓库 |

---

## 🚀 下一步

### 选择方案 1（推荐）
```
请告诉我你的 GitHub 个人访问令牌
```

### 选择方案 2
```
我会生成 SSH 密钥并指导你配置
```

---

## 💡 如何获取个人访问令牌

**详细步骤：**

1. **访问 GitHub**
   - 打开：https://github.com

2. **进入设置**
   - 点击右上角头像 → Settings

3. **进入开发者设置**
   - 滚动到最底部 → Developer settings

4. **创建令牌**
   - 左侧菜单 → Personal access tokens → Tokens (classic)
   - 点击 Generate new token → Generate new token (classic)

5. **配置令牌**
   - Note：`Coze 沙箱推送`
   - Expiration：`90 days`（或选择 No expiration）
   - 勾选 `repo`（这将勾选所有 repo 相关权限）

6. **生成令牌**
   - 点击底部的 Generate token 按钮
   - **重要**：复制生成的令牌（格式：`ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

7. **给我令牌**
   - 告诉我这个令牌
   - 我会帮你推送代码

---

## ⚠️ 注意事项

1. **令牌只显示一次**
   - 生成后立即复制
   - 关闭页面后就看不到了

2. **令牌权限**
   - 勾选 `repo` 即可
   - 不需要其他权限

3. **令牌过期**
   - 可以设置过期时间
   - 也可以选择 No expiration（永不过期）

4. **安全性**
   - 令牌就像密码一样重要
   - 不要分享给其他人
   - 可以随时撤销

---

## 🎯 准备好了吗？

**请告诉我你的 GitHub 个人访问令牌！**

格式类似：`ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

告诉我后，我立即帮你推送代码到 GitHub！🚀
