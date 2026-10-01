---
redirect_from: "/cn/How-to-test-a-PR"
---

# 如何测试 PR

## 简介

在 AzerothCore，我们非常重视游戏质量和稳定性。因此，**我们不会直接将更改推送到 master 分支**。相反，每当引入新的更改时，我们都会创建一个新的 [Pull Request](https://help.github.com/articles/about-pull-requests/)（通常简称为 PR）。

这让我们能够在任何更改进入生产环境之前对其进行充分的**审查和测试**。任何能够安装 AzerothCore 的人都可以通过测试 PR 来做出贡献。本指南将介绍如何做到这一点。

帮助我们测试 PR 的用户越多，我们的开发活动在速度和质量上就会越好。

## 哪些 PR 需要测试？

我们为所有已经由作者完成且代码已通过审查的 PR 打上 [**Waiting to be tested**](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22Waiting+to+be+tested%22) 标签。

点击上面的标签，你就能看到所有为了合并到 `master` 分支而需要测试的 PR 列表。

## 测试 PR 之前我需要准备什么？

你需要：

- 在系统中安装好 AzerothCore（参见[安装](installation)）。
- 有一个 GitHub 账号，你可以[在这里免费注册](https://github.com/join)。

### 如果 PR 只有数据库（DB）更改怎么办？

有些 PR 只有数据库更改（没有 C++ 更改）。如果是这种情况，有一个[测试此类更改的简化流程](how-to-test-db-only-changes)。

如果你不确定，就继续读下去，进行传统的 PR 测试即可，它适用于所有类型的 PR。

### 克隆了 AzerothCore fork 而非主仓库的用户请注意：

如果你是开发者，通常会创建并克隆你自己的 AzerothCore fork。
如果这是你的情况，那么你需要：

- 添加主 AzerothCore 远程仓库，使用：
```
git remote add upstream https://github.com/azerothcore/azerothcore-wotlk.git
```
- 将下面所有命令中的 `origin` 替换为 `upstream`

## 获取要测试的 PR 代码

- 打开终端并进入你的 AzerothCore 源码目录，例如使用 `cd azerothcore-wotlk`。

![image](https://user-images.githubusercontent.com/75517/52176403-b6708480-27b2-11e9-93b0-9f3d3232e817.png)

- 这里我们假设你从一个干净、最新的 `master` 分支开始。你可以输入 `git checkout` 来验证你当前所在的分支。如果你还不在 master 上，请使用 `git checkout master` 回到 master。既然到了这里，你也可以执行 `git pull` 以确保你拥有最新的 master。请记住，**永远不要向 master 分支添加自定义更改**（如果必须添加，请始终创建一个新的、独立的分支）。

- 查看你想要测试的 PR 的 ID，它会出现在 PR 的 URL 和标题中。例如，这个 PR 的 ID 是 **1383**：[https://github.com/azerothcore/azerothcore-wotlk/pull/1383](https://github.com/azerothcore/azerothcore-wotlk/pull/1383)

![image](https://user-images.githubusercontent.com/75517/52176395-9ccf3d00-27b2-11e9-9600-64206e7b33bc.png)

- 现在你需要运行以下命令，并将 “XXXX” 替换为你要测试的 PR 的 ID：

```git checkout -b pr-XXXX```

```git pull origin pull/XXXX/head```

上述命令会创建一个名为 `pr-XXXX` 的新本地分支，其中包含所有需要测试的更改。

终端会弹出一个编辑器（通常是 `nano` 或 `vim`），要求你保存合并 commit message。只需保存更改并退出编辑器即可。

- 如果编辑器是 `nano`，你可以简单地使用 `CTRL+O` 和 `ENTER` 保存，然后用 `CTRL+X` 退出。
- 如果编辑器是 `vim`，你可以按住 `SHIFT` 键并按两次 `Z` 来保存并退出。

你可以[在这里](http://web.mit.edu/6.005/www/fa14/tutorial/git/config.html)阅读更多关于 `git` 配置及其默认编辑器的信息。

{% include note.html content="检查控制台中的消息。如果显示 'Automatic merge failed; fix conflicts and then commit the result'，你应该向 PR 反馈，请开发者修复合并冲突，并移除 'waiting to be tested' 标签，同时贴上 'merge conflict' 标签。" %}


## 更新你的本地服务器以应用更改

现在你只需用新的更改更新你的本地服务器。流程与普通的服务器更新类似。

基本上你需要**重新编译你的源码**并**更新数据库（DB）**。

### 使用传统安装方式

如果你使用传统安装方式，你需要按照主安装指南中的[核心安装](core-installation)步骤重新编译。

你还需要更新你的数据库。你可以使用 DB assembler 来完成，但通常更快的方法是手动导入 PR 中包含的待处理 sql 文件。这些文件位于 `data/sql/updates/pending_db_*` 目录下。

**提示**：通常一个 PR 包含一个位于 `data/sql/updates/pending_db_world` 下的新的 world 更新文件。你可以通过查看 PR 页面的 “Files changed” 选项卡，检查添加了哪些文件，以发现任何新增的 sql 文件：

![File Changes](https://user-images.githubusercontent.com/75517/52176720-ea4da900-27b6-11e9-8459-d58adf7fd50c.png)

然后像往常一样启动服务器。

### 使用 Docker 安装方式

如果你使用 Docker 安装方式，可以通过运行以下命令来触发重新编译：

Linux：```./bin/acore-docker-build```
Windows：```./acore.sh docker build```

然后要启动服务器，你需要销毁并重新创建容器，使用 `docker-compose down` 和 `docker-compose up`。

{% include note.html content="这也会自动更新你的数据库。" %}

-----

## 验证你的实际版本

为确保你正确地使用该 PR 运行服务器，请检查 `server info` 命令输出中的日期和分支名称。它们应与该 PR 匹配。

现在登录游戏并进行测试吧！

官方 PR 还会在 CI 中运行[在线端到端（e2e）测试](live-e2e)（完整的 authserver + worldserver、协议机器人）。这是额外的覆盖。它不能替代本页面上的游戏内检查。

## 需要测试什么？ {#what-needs-to-be-tested}

PR 范围内需要测试的内容说明应由 PR 的作者在 PR 描述中提供。如果没有提供，请随时在 PR 描述中留言，请求测试说明。

对于高级用户：你还可以查看 PR 中实际更改了什么，自己决定要测试什么。有时换个角度思考是件好事！只需确保你在报告中描述了你测试了什么。

## 报告你的测试结果

通过在**PR 页面**留言来报告你的测试结果非常重要。

你应该写明：

- 你测试了什么
- 你测试的内容是否按预期工作？
- 有时你可能还想说明在 PR **之前**和**之后**的表现如何
- 请尽可能多地提供细节
- 你还可以插入截图或视频

## 优秀测试报告示例

![image](https://user-images.githubusercontent.com/75517/52176856-1702c000-27b9-11e9-9030-48fe01669247.png)

![image](https://user-images.githubusercontent.com/75517/52176862-3bf73300-27b9-11e9-8852-51624d882ccd.png)

![image](https://user-images.githubusercontent.com/75517/52176828-980d8780-27b8-11e9-9fcc-071d64176022.png)

![image](https://user-images.githubusercontent.com/75517/52176837-becbbe00-27b8-11e9-9b42-94a9521b6647.png)

![image](https://user-images.githubusercontent.com/75517/52176842-cee39d80-27b8-11e9-97e6-25f272a346bd.png)

![image](https://user-images.githubusercontent.com/75517/52176846-ea4ea880-27b8-11e9-9497-919cec1e22ff.png)

![image](https://user-images.githubusercontent.com/75517/52176849-02262c80-27b9-11e9-927f-687dcc43cb26.png)

![image](https://user-images.githubusercontent.com/75517/52176867-44e80480-27b9-11e9-9f43-070e4edcb77d.png)

## 完成测试

一旦你留下了测试报告，你可能希望将你的 AC 安装恢复到基础状态，以便进行进一步的测试。要做到这一点，使用 `git reset --hard` 移除所有未暂存的更改，然后使用 `git checkout master` 回到 master 分支。为了整理干净，你还可以使用 `git clean -fd` 清除任何未跟踪的文件。最后，你可以输入 `git status` 确保一切恢复正常。
