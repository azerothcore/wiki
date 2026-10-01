# 提交信息指南

# 📌 标题
**类型（作用域/子作用域）：** _提交的超简短说明_

| ✅ 示例（最多 50 个字符） |
|--------------------------------|
| fix(DB/SAI): Missing spell to NPC Hogger |
| fix(Scripts/Raid): Phase 2 of Ragnaros |
| feat(Core/Players): Implement missing player flags |

**注意不要留下格式错误的提交信息（例如随机的空格）**

---

# 📖 描述
解释**为什么**要做此更改，以及**修复了什么**。

| ✅ 示例（每行最多 72 个字符） |
|-------------------------------------|
| Hogger (id: 492) was not charging player when being engaged. |

---

# ✍️ 共同作者（Co-Author）
如果还有其他作者，可以这样提及他们：
```

Co-authored-by: Name [name@example.com](mailto:name@example.com)

```

**如果你在挑选（cherry-pick）提交，必须在你的提交中注明原作者。**

当你创建提交时（使用 GIT Bash 终端），请键入：

```
git commit --author="John Doe <john@example.com>" -m "Your commit message"
```

✔️ 这会将提交中的 Author 字段设置为 John Doe <john@example.com>
✔️ 你常规 Git 配置的 user.name 和 user.email 仍将用于 Committer 字段。

如果你使用 GitHub Desktop，可以在提交描述框下方填写共同作者字段。

---

# 📌 额外信息

# ✅ 类型
- **feat**：新功能
- **fix**：缺陷修复
- **refactor**：重构生产代码（预期不改变功能）
- **style**：格式、缺少分号等；无代码更改
- **docs**：文档更改
- **chore**：更新 bash 脚本、git 文件等；无生产代码更改

**请记住：**
- ✅ 标题行首字母大写
- ✅ 标题行使用**祈使语气**
- ✅ 标题行末尾不要加句号
- ✅ 用空行分隔标题和正文
- ✅ 使用正文解释**是什么**和**为什么**，而不是**怎么做**
- ✅ 正文中可以使用以 `-` 开头的多行项目符号

**更多信息：** [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.2/)

---

# 📦 作用域（Scope）和 🔧 子作用域（Subscope）
作用域定义了受影响的主要领域：

- Core（核心相关，框架文件）
- Scripts（核心相关，脚本文件）
- DB（数据库相关，SQL）

遵循文件名或内容类型：

- fix(Scripts/Ulduar): Mimiron rocket barrage targeting

- fix(DB/SAI): Add missing spells to Howling Prowler

👉 对于 SQL 提交：
如果内容混合，请选择最主要的表类型。
示例：如果大多数编辑都在 smart_scripts 中，请使用 SAI。
如果更改过于分散，请使用像 Misc 这样的一般性子作用域。

例如：
```
fix(Scripts/Ulduar): Mimiron rocket barrage targeting
```

或者

```
fix(DB/SAI): Add missing spells to Howling Prowler
```
