# 🚀 推送代码到Gitee仓库

## 📋 准备工作

✅ Git远程仓库已配置：`https://gitee.com/spiritor/simplecal.git`
✅ 代码已提交到本地仓库
✅ 当前分支：`main`

---

## ⚠️ 需要身份验证

由于Gitee需要身份验证，你需要在本地终端手动完成推送。

---

## 🔄 推送步骤

### 方法1: 使用HTTPS推送（推荐）

```bash
# 1. 进入项目目录
cd /workspace/projects

# 2. 推送代码
git push -u origin main
```

系统会提示输入：
- **用户名**：你的Gitee用户名（spiritor）
- **密码**：你的Gitee密码或访问令牌

### 方法2: 使用SSH密钥（免密推送）

```bash
# 1. 生成SSH密钥（如果还没有）
ssh-keygen -t rsa -C "your_email@example.com"

# 2. 查看公钥
cat ~/.ssh/id_rsa.pub

# 3. 复制公钥，在Gitee设置中添加
# Gitee -> 设置 -> SSH公钥 -> 添加公钥

# 4. 测试连接
ssh -T git@gitee.com

# 5. 修改远程仓库为SSH地址
git remote set-url origin git@gitee.com:spiritor/simplecal.git

# 6. 推送代码
git push -u origin main
```

### 方法3: 使用Gitee访问令牌（推荐）

```bash
# 1. 在Gitee生成访问令牌
# Gitee -> 设置 -> 私人令牌 -> 生成新令牌
# 权限：至少勾选 projects 和 repositories

# 2. 使用令牌推送
git push -u origin main
# 用户名：spiritor
# 密码：粘贴令牌（不是你的密码）
```

---

## 📊 推送验证

推送成功后，你应该看到类似输出：

```
Enumerating objects: 123, done.
Counting objects: 100% (123/123), done.
Delta compression using up to 8 threads
Compressing objects: 100% (89/89), done.
Writing objects: 100% (123/123), 1.2 MiB | 2.3 MiB/s, done.
Total 123 (delta 34), reused 0 (delta 0)
remote: Powered by GITEE.COM
To https://gitee.com/spiritor/simplecal.git
 * [new branch]      main -> main
```

---

## ✅ 验证推送成功

### 在Gitee仓库查看

访问：https://gitee.com/spiritor/simplecal

你应该能看到：
- 所有代码文件
- 提交历史
- 文件树结构

### 命令行验证

```bash
# 查看远程分支
git branch -r

# 应该看到：
# origin/main

# 验证最新提交
git log origin/main --oneline -3
```

---

## 🔄 后续更新

推送成功后，后续更新代码只需：

```bash
# 添加修改的文件
git add .

# 提交
git commit -m "更新描述"

# 推送
git push
```

---

## ❓ 常见问题

### Q1: 提示"remote rejected"怎么办？
**A:** 可能远程仓库已有内容，使用：
```bash
git push -u origin main --force
```
⚠️ 谨慎使用，会覆盖远程内容！

### Q2: 忘记密码怎么办？
**A:** 在Gitee重置密码，或生成新的访问令牌。

### Q3: 推送太慢怎么办？
**A:**
1. 检查网络连接
2. 使用SSH方式推送
3. 减少推送的文件数量

### Q4: 如何查看推送进度？
**A:** 推送时会自动显示进度条，也可以按 `Ctrl+C` 取消。

---

## 🎯 推送完成后

推送成功后，你可以：

1. **在Coze平台导入仓库**
   - 使用仓库地址：`https://gitee.com/spiritor/simplecal.git`

2. **部署游戏页面到Vercel**
   - 使用GitHub仓库（如果需要）
   - 或从Gitee导出

3. **分享链接**
   - Gitee仓库链接：`https://gitee.com/spiritor/simplecal`

---

## 📞 需要帮助？

如果推送过程中遇到问题，告诉我：
1. **具体的错误信息**
2. **使用的推送方法**
3. **卡在哪一步**

我会帮你解决！

---

## 💡 推荐方式

**使用访问令牌推送**（最安全、最简单）

1. 在Gitee生成访问令牌
2. 用令牌作为密码推送
3. 令牌可以随时撤销
4. 不需要暴露真实密码

---

现在请在你的终端中执行推送命令！🚀
