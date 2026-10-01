---
redirect_from: "/cn/How-to-create-a-DB-PR"
---

# 如何通过 GitHub 创建数据库 PR

这是一份简化指南，帮助你无需处理终端即可轻松创建包含数据库修复（SQL 代码）的 PR，
是[传统创建 PR 方式](how-to-create-a-pr)的更简单替代方案。
如果你想提交 C++ 或其他非 SQL 类型的修复，请遵循另一份指南。

## 只需做一次：创建你的 AzerothCore fork

你需要登录 [github.com](https://github.com/)。如果还没有账号，请先创建一个。

打开 [AzerothCore 仓库](https://github.com/azerothcore/azerothcore-wotlk)
并通过点击右上角的 "Fork" 按钮来创建它的 fork：

![创建 AzerothCore 的 fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/1.png)

## 创建新的 PR

### 1. 在 GitHub 上更新你的 fork

打开浏览器，导航到你在 GitHub 上的 fork（将 `YourUsername` 替换为你实际的 GitHub 用户名）：

**https://github.com/YourUsername/azerothcore-wotlk**

如果你的 `master` 分支与最新的 AzerothCore 不同步，你会看到类似这样的提示：

`This branch is XX commits behind azerothcore:master`

![更新 AzerothCore fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-1.png)

要更新它，点击 **Fetch upstream**，然后点击 **Fetch and merge**。

完成后，你 fork 的 `master` 分支应该显示：

`This branch is even with azerothcore:master`

![AzerothCore fork 已更新](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-2.png)

### 2. 创建新分支

确保当前选择的是 `master` 分支，点击分支下拉菜单并创建一个新分支。

![AzerothCore fork 已更新](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-branch.png)

你可以随意命名新分支（通常取与你的修复相关的名字），
只需确保之前没有用过该名称，并且你是通过复制 master 分支来创建新分支的。

你应该会看到类似 **Create branch my-new-branch-123 from master** 的消息。

创建新分支后，确保**保持选中该分支**。

### 3. 导航到 pending_db_world 文件夹

你现在需要进入你 fork 中的 `data/sql/updates/pending_db_world` 文件夹。

你可以手动点击 `data` 文件夹，然后依次进入 `sql`、`updates`、`pending_db_world`；

...或者你可以直接打开这个 URL（将 `YourUsername` 替换为你实际的 GitHub 用户名）：

**https://github.com/YourUsername/azerothcore-wotlk/tree/my-new-branch-123/data/sql/updates/pending_db_world**

### 4. 创建并提交新文件

回到 GitHub，在 `pending_db_world` 文件夹中，点击 **Add file**，然后点击 **Create new file**：

![AzerothCore 创建新的 SQL 文件](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-1.png)

现在你需要：

- 为文件取一个任意名称，文件扩展名为 `.sql`。
- 添加一个新行，然后在下面添加你自己的 SQL 代码，最后在文件末尾再添加一个空行。

![AzerothCore 新 SQL 文件示例](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-new-file-2.png)

现在向下滚动页面，你需要：

1. 填写提交信息，我们使用 [Conventional Commits 格式](https://www.conventionalcommits.org/)，
  例如 `fix(DB/Creature): some commit description here`。
2. 包含一些额外的描述（可选）。
3. 确保选中了 "Commit directly to the `your-new-branch-name`"。
4. 点击 **Commit new file**。

![AzerothCore 创建新提交](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/web-create-commit.png)

### 5. 打开 PR

回到[主 AzerothCore 仓库](https://github.com/azerothcore/azerothcore-wotlk)，
你会注意到 GitHub 很聪明地意识到你即将打开一个 PR，
并显示这个漂亮的浅黄色提示框：

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/11.png)

点击 "Compare & pull request" 绿色按钮（位于右侧）。

现在按照屏幕上出现的说明填写 PR 模板，
不要忘记添加**测试说明**，这样人们才能测试你的 PR，并且它才能被合并：

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/12.png)

同时建议检查一下 "File changes" 标签页，确保一切符合你的预期：

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/13.png)

{% include important.html content="我们非常不欢迎白嫖者（leechers）！如果你的修复来自其他组织或个人，你应该始终注明原作者和原始提交！" %}

就这样！
