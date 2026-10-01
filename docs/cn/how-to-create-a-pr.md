---
redirect_from: "/cn/How-to-create-a-PR"
---

# 如何创建 PR

本指南将介绍如何提交 PR 来提交各种修复（C++、SQL 等）。

下面的每一步都会**展示两次**：一次是使用 [GitHub Desktop](https://desktop.github.com/)（一个图形化应用，无需使用终端），另一次是使用**命令行**（`git`）。两种方式产生的结果完全相同，所以只需选择你习惯的一种，忽略另一种即可。你也可以混合使用它们：GitHub Desktop 是一个普通的 git 客户端，因此用它克隆的仓库也可以在终端中正常使用，反之亦然。

如果你只提交**数据库**修复，可以尝试我们[提交包含 SQL 代码的 PR 的简化方式](how-to-create-a-db-pr)：这种方式完全在 GitHub 网站上完成，不需要任何工具。

## 选择你的方式

创建 fork 和提交 PR 本身是在 GitHub 网站上完成的，对每个人来说都一样。以下步骤是两种方式不同的地方，因此你可以直接跳到对应工具的说明：

| 步骤                                        | GitHub Desktop                                                    | 命令行                                                                   |
| :------------------------------------------ | :---------------------------------------------------------------- | :---------------------------------------------------------------------- |
| 克隆你的 fork *（仅第一次）*                | [用应用克隆](#clone-with-github-desktop)                           | [用 git 克隆](#clone-with-the-command-line)                             |
| 更新你的本地克隆                            | [用应用更新](#update-your-clone-with-github-desktop)               | [用 git 更新](#update-your-clone-with-the-command-line)                  |
| 创建新分支                                  | [用应用创建分支](#create-the-branch-with-github-desktop)           | [用 git 创建分支](#create-the-branch-with-the-command-line)              |
| 选择要提交的文件                            | [用应用选择](#selecting-files-with-github-desktop)                 | [用 git 选择](#selecting-files-with-the-command-line)                    |
| 创建 SQL 文件 *（仅数据库修复）*            | [用应用创建](#create-the-sql-file-with-github-desktop)             | [用 git 创建](#create-the-sql-file-with-the-command-line)                |
| 提交并推送                                  | [用应用提交](#commit-and-push-with-github-desktop)                 | [用 git 提交](#commit-and-push-with-the-command-line)                    |

## 只需做一次：创建并克隆你的 AzerothCore fork

### 1. 创建 AzerothCore 的 fork

此步骤在 GitHub 网站上完成，无论之后使用什么工具都一样。

你需要登录 [github.com](https://github.com/)。如果你还没有账号，请先创建一个。

打开 [AzerothCore 仓库](https://github.com/azerothcore/azerothcore-wotlk)，然后点击右上角的 “Fork” 按钮来创建它的 fork：

![创建 AzerothCore 的 fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/1.png)

*fork* 是你自己的 AzerothCore 副本，位于你的 GitHub 账号下。你可以在其中做任何想做的事情：只有当你提交 PR 并被合并后，这些更改才会到达 AzerothCore。

### 2. 将你的 fork 克隆到本地机器

fork 创建完成后，你会看到一个显示 **YourUsername/azerothcore-wotlk** 的界面。

*克隆*意味着将该 fork 下载到你的电脑上，这样你就可以用常用的编辑器修改文件。

#### 使用 GitHub Desktop 克隆 {#clone-with-github-desktop}

1. 下载并安装 [GitHub Desktop](https://desktop.github.com/)，然后使用你的 GitHub 账号登录
   （**File** → **Options** → **Accounts**）。
2. 进入 **File** → **Clone repository...** 并打开 **GitHub.com** 选项卡：你的 fork
   `YourUsername/azerothcore-wotlk` 会列在那里。
3. 选择你想要下载源码的 **Local path**，然后点击 **Clone**。

通过 GitHub Desktop 登录也会一并处理身份验证，因此稍后推送时不会再要求你输入凭据。

#### 使用命令行克隆 {#clone-with-the-command-line}

点击 “Clone or download” 按钮（在右侧），复制你的 fork 的 https 地址：

![复制你的 AzerothCore fork 地址](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/2.png)

现在打开**终端**（如果你使用 Windows，请使用 [git bash 终端](https://git-scm.com/downloads)），输入 `git clone `，后面跟上你刚刚复制的 fork 的 git 地址：

![克隆你的 AzerothCore fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/3.png)

```
git clone https://github.com/YourUsername/azerothcore-wotlk.git
```

等待下载完成，然后进入 `azerothcore-wotlk` 目录：

```
cd azerothcore-wotlk
```

![进入 AzerothCore 目录](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/4.png)

## 创建新的 PR

### 1. 在 GitHub 上更新你的 fork

打开浏览器，导航到你在 GitHub 上的 fork（将 `YourUsername` 替换为你的实际 GitHub 用户名）：

**https://github.com/YourUsername/azerothcore-wotlk**

如果你的 `master` 分支不是最新的 AzerothCore，你会看到类似这样的提示：

`This branch is XX commits behind azerothcore:master`

![更新 AzerothCore fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-1.png)

要更新它，请点击 **Sync fork**（在旧版本的 GitHub 界面中称为 **Fetch upstream**），然后通过 **Update branch** / **Fetch and merge** 确认。

之后，你的 fork 的 `master` 分支应该显示：

`This branch is up to date with azerothcore:master`

![更新 AzerothCore fork](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/update-fork-2.png)

### 2. 更新你的本地克隆

在上一步中你只更新了*远程* fork，但你也需要同步你的本地克隆。

#### 使用 GitHub Desktop 更新你的克隆 {#update-your-clone-with-github-desktop}

在 **Current branch** 下拉菜单中选择 `master` 分支，然后点击 **Fetch origin**，当它变为 **Pull origin** 后，再次点击它。

#### 使用命令行更新你的克隆 {#update-your-clone-with-the-command-line}

在 `azerothcore-wotlk` 目录中打开终端并运行：

```
git checkout master
git pull
```

### 3. 创建一个新分支

{% include important.html content="永远不要向你的 <b>master</b> 分支提交更改，这会让你的 fork 变得混乱。" %}

*分支*是一条独立的工作线：一个分支 = 一个 PR。创建新分支时，git 会复制你的**当前**分支，因此在创建新分支**之前**，请始终确保你位于最新的 `master` 上。

给新分支起一个与任何现有分支都不同的名字。你可以起任何你喜欢的名字（将 “xxxx” 替换为你正在修复的内容），例如 `fix-issue-xxxx`。

#### 使用 GitHub Desktop 创建分支 {#create-the-branch-with-github-desktop}

打开 **Current branch** 下拉菜单，确保 `master` 是选中的分支，然后点击 **New branch**，输入名称并用 **Create branch** 确认。

**Current branch** 按钮现在会显示你的新分支：从此以后你提交的所有内容都会进入该分支。

#### 使用命令行创建分支 {#create-the-branch-with-the-command-line}

```
git checkout master
git checkout -b fix-issue-xxxx
```

![进入 AzerothCore 目录](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/5.png)

### 4. 添加你的 C++ 更改（如有）

请确保所有更改都符合 [C++ 代码规范](cpp-code-standards)！

如果你没有任何 C++ 更改，可以跳过这一步。否则，打开你的编辑器现在就动手吧！我会等你...

在本指南中，我们假设你修改了文件 `instance_deadmines.cpp`

#### 使用 GitHub Desktop 选择文件 {#selecting-files-with-github-desktop}

无需任何操作：一旦你保存文件，它就会出现在左侧的 **Changes** 选项卡中，复选框已默认勾选。只有勾选的文件才会包含在你的 commit 中，所以请取消勾选任何你不想提交的文件，并在提交前点击每个文件查看你自己的差异。

#### 使用命令行选择文件 {#selecting-files-with-the-command-line}

现在添加要提交的文件：

```
git add src/server/scripts/EasternKingdoms/Deadmines/instance_deadmines.cpp
```

![AzerothCore - 使用 git add 添加文件](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/6.png)

如果你修改了更多文件，只需使用 `git add path/to/file` 添加它们。

你可以使用 `git status` 命令检查哪些文件已被选中待提交：

![AzerothCore - git status](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/7.png)

### 5. 添加你的 SQL 更改（如有）

如果你没有任何 SQL 更改，可以跳过这一步。

否则，你的 SQL 代码必须放入 `data/sql/updates/pending_db_world` 文件夹中的**新**文件里，命名为 `rev_XXXXXXXXXXXX.sql`，其中 `XXXXXXXXXXXX` 是一个还没有其他人使用过的数字（通常使用时间戳）。永远不要编辑已有的 `rev_*.sql` 文件。

#### 使用 GitHub Desktop 创建 SQL 文件 {#create-the-sql-file-with-github-desktop}

用你的编辑器（或文件管理器）在你的克隆目录下的 `data/sql/updates/pending_db_world` 文件夹中自己创建文件，使用类似 `rev_1700000000000.sql` 的名称，并把你的 SQL 代码放进去。

保存后，这个新文件就会像其他更改一样出现在 **Changes** 选项卡中。

#### 使用命令行创建 SQL 文件 {#create-the-sql-file-with-the-command-line}

一个辅助脚本会为你生成具有唯一名称的文件：

```
./data/sql/updates/pending_db_world/create_sql.sh
```

这会在 `data/sql/updates/pending_db_world` 目录下生成一个新文件，其唯一名称类似 `rev_XXXXXXXXXXXX.sql`

![AzerothCore - 创建待处理的 sql 文件](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/8.png)

将你的 SQL 代码写入该文件，然后使用 `git add path/to/file` 命令将其添加为待提交文件：

```
git add data/sql/updates/pending_db_world/rev_XXXXXXXXXXXX.sql
```

（当然，请将 `rev_XXXXXXXXXXXX.sql` 替换为文件的实际名称）

![AzerothCore - git add 待处理的 sql 文件](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/9.png)

### 6. 提交并推送你的更改

*commit* 是您的更改快照，附带一条描述这些更改的消息；*推送*会将你的 commit 上传到你在 GitHub 上的 fork。

我们使用 [Conventional Commits 格式](https://www.conventionalcommits.org/) 作为 commit message，例如：

```
fix(DB/Creature): Deadmines - Mr. Smite no longer resets
```

你可以参考[这个 commit](https://github.com/azerothcore/azerothcore-wotlk/commit/afc33e7b285efd717dcd4ce75b590d99f2bcbdf6)作为示例。

有关可接受的类型、scope 及更多示例，请参阅 [commit message 规范](commit-message-guidelines)。

#### 使用 GitHub Desktop 提交并推送 {#commit-and-push-with-github-desktop}

在左下角，用 commit message 填写 **Summary** 字段，并可选地在 **Description** 字段中填写更多详细信息。然后点击 **Commit to fix-issue-xxxx**。

{% include note.html content="GitHub Desktop 不使用 AzerothCore 的 commit 模板，因此你需要自己编写 <code>type(Scope): description</code> 这行内容。" %}

最后，点击窗口顶部的 **Publish branch**（后续提交时会变为 **Push origin**）。

#### 使用命令行提交并推送 {#commit-and-push-with-the-command-line}

##### 只需做一次：git config

首先，确保使用 AC 的 commit 模板（通常只需做一次）：

```
git config --local commit.template ".git_commit_template.txt"
```

当你编写 commit message 时，默认的文本编辑器 `Vim` 非常难以操作。你可以保留它，也可以改用更简单的 `Nano` 编辑器。操作方法是，输入：

```
git config --global core.editor "nano"
```

##### Git commit

然后通过输入以下命令提交你的更改：

```
git commit
```

接着系统会提示你输入合适的 commit message。请遵循模板中显示的格式规范（即以 # 开头的每一行都会在 commit message 中被忽略）。如果使用 `Nano`，按 [ctrl]+[x] 并确认保存退出（其他命令写在 `Nano` 底部，也可以很容易地在网上找到，或在终端中输入 `man nano` 查看）。

输入 `git show` 确认你满意当前结果。按 [q] 退出。如果不满意，你可以通过输入 `git commit --amend` 重新提交**最后一个本地** commit。

现在该把它们推送到远程了。如果你第一次在该分支上使用 `git push` 命令，git 会要求你指定要推送到的远程分支。

所以你应该输入：

```
git push --set-upstream origin fix-issue-xxxx
```

（当然，请将 `fix-issue-xxxx` 替换为你分支的实际名称）

![AzerothCore - git push](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/10.png)

### 7. 提交 PR

这最后一步发生在 GitHub 网站上，对每个人来说都一样。

回到[主 AzerothCore 仓库](https://github.com/azerothcore/azerothcore-wotlk)，你会注意到 GitHub 足够智能，能意识到你即将提交一个 PR，并显示这个漂亮的浅黄色提示框：

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/11.png)

点击绿色的 “Compare & pull request” 按钮（位于右侧）。

{% include note.html content="GitHub Desktop 也会显示同样的快捷方式：发布分支后，应用中会出现一个 <b>Create Pull Request</b> 按钮，点击后会在你的浏览器中打开同一个页面。" %}

现在按照屏幕上出现的说明填写 PR 模板，不要忘记添加**测试说明**，这样人们才能测试你的 PR，它也才能被合并：

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/12.png)

另外，养成检查 “File changes” 选项卡的好习惯，确认一切如你所料：

![AzerothCore - Compare & pull request](http://www.azerothcore.org/wiki/assets/images/pr-tutorial/13.png)

{% include important.html content="我们非常不喜欢白嫖者！如果你的修复来自其他组织或个人，你应该始终为原作者和原 commit 署名！" %}

就是这样！

## 常见问题

### 文件更改中有错误或缺失，我想推送更多更改

只需编辑/添加你想要的文件，在**同一分支**上再次提交并推送。如果你刷新 PR 页面，就会看到这些更改：无需提交新的 PR。

- **GitHub Desktop：** 编辑过的文件会重新出现在 **Changes** 选项卡中，提交它们并点击 **Push origin**。
- **命令行：** `git add` 这些文件，然后执行 `git commit` 和 `git push`。

### 我已经创建了一个 PR，想再创建一个该怎么办？

只需从 *创建新的 PR* 的第 1 步开始重复操作即可：每个 PR 都需要自己的分支。

创建新分支时要小心：你**必须**从最新的 `master` 开始（使用命令行时，先输入 `git checkout master`；使用 GitHub Desktop 时，在点击 **New branch** 之前，先在 **Current branch** 下拉菜单中选择 `master`）。

### 如何更新我 fork 的 master 分支？

最简单的方法是使用 fork 在 GitHub 页面上的 **Sync fork** 按钮，如步骤 1 所述，然后拉取你的本地克隆（步骤 2）。

从命令行也可以不借助浏览器完成。如果你以前从未更新过 fork，请输入：

```
git remote add upstream https://github.com/azerothcore/azerothcore-wotlk.git
```

然后按照以下步骤操作：

1) `git checkout master`
2) `git fetch upstream`
3) `git merge upstream/master`
4) `git push origin master`

你的 fork 现在就更新好了。

### 如何用最新的 master 更新我的分支？

你首先需要更新你 fork 的 master 分支（见上文）。

- **命令行：** `git checkout your-branch`，然后执行 `git merge master`。
- **GitHub Desktop：** 在 **Current branch** 下拉菜单中选择你的分支，然后执行
  **Branch** → **Update from master**，最后 **Push origin**。

### 我的 PR 需要多久才能被审查、测试和合并？

这是一个开源项目，人们利用空闲时间工作，所以我们无法估计时间。

我们可以建议的是：编写**清晰的**测试 PR 说明，这样任何人都能轻松测试它。

如果你的测试说明不清楚或完全没有，
那么只有高级用户才能测试你的 PR，这将花费更多时间。

### 本教程中使用的是什么终端？

https://github.com/robbyrussell/oh-my-zsh

但任何 linux/mac 终端都可以。
如果你使用 Windows，请使用 [git bash](https://git-scm.com/downloads)（或者，如果你希望完全避开终端，也可以使用 GitHub Desktop）。

### 每次使用 git push 都需要重新认证吗？

使用 GitHub Desktop 时这已经处理好了：你在安装时就登录过一次。

使用命令行时，你可以使用 SSH 而不是 HTTPS 克隆自己的 fork，然后按照[这份指南](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)设置 SSH 密钥。这样你就可以使用 `git push` 而无需反复输入密码。

### 我把分支/fork 弄乱了，如何重新开始？

只要你的工作仍然在你的机器或 fork 上，就没有什么会丢失。

最简单的修复方法是：从一个最新的 `master` 创建一个**新的**分支并在那里重做更改（之后可以删除旧分支）。如果你 fork 的 `master` 本身变得很乱，你可以在 GitHub 上删除整个 fork，然后重新 fork AzerothCore，再克隆一次。
