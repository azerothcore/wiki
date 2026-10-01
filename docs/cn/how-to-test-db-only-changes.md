---
redirect_from: "/cn/How-to-test-DB-only-changes"
---

# 如何测试仅包含数据库（DB）更改的内容

## 简介

主要的[如何测试 PR](how-to-test-a-pr)指南适用于所有类型的 PR。

然而，常见的 PR 只对数据库（通常是 `world` 数据库）进行更改。

对于此类 PR，有一种更简单的测试方法，本页面将对其进行说明。

**提示**：需要测试的完整 PR 列表可以在[这里](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22Waiting+to+be+tested%22)查看。

## 前提条件

本教程假设你：

- 在系统中安装了**较新**版本的 AzerothCore（无论是使用[传统安装方式](installation)还是[Docker 安装方式](install-with-docker)）。我们建议使用最新的 `master`。
- 有一个 GitHub 账号，你可以[在这里免费注册](https://github.com/join)。
- 有一个数据库客户端，如 [HeidiSQL](https://www.heidisql.com/)、Navicat 或类似的工具。

## 检查 PR 是否只有数据库（DB）更改

打开 PR 页面并点击 “File Changes” 选项卡：

![File Changes](https://user-images.githubusercontent.com/75517/52176720-ea4da900-27b6-11e9-8459-d58adf7fd50c.png)

- 如果你看到 `*.cpp`、`*.h` 文件的更改，请改而遵循[这份指南](how-to-test-a-pr)。

- 如果你只看到 `*.sql` 更改，请继续阅读。

## 将更改导入你的数据库

PR 会在 `pending_db_xxxxx` 文件夹中包含一些 sql 文件（通常只有一个），其中 `xxxxx` 是数据库的名称（通常是 `world`）。

基本上你只需要将这些更改导入到对应的数据库（通常是 `acore_world`）。

要做到这一点，点击 PR 页面 “File changes” 选项卡下的 “View file” 按钮。你可以下载整个文件，也可以直接手动复制所有 SQL 代码。

然后打开你的数据库客户端（例如 HeidiSQL），选择正确的数据库（例如 `acore_world`）并执行 SQL 代码。

例如，在 HeidiSQL 中**首先**从左侧列中选择数据库，然后打开 “Query” 选项卡，将 SQL 代码粘贴到那里并按 F9 执行：

![HeidiSQL import example](https://user-images.githubusercontent.com/75517/52532889-e4624580-2d2b-11e9-8325-aa587c2d080d.png)

## 在游戏中反映更改

让你的服务器加载新更改的一个快捷方式就是重启 `worldserver` 进程。

**提示**：如果你使用 Docker 运行 AC，只需使用 `docker-compose restart ac-worldserver` 重启你的数据库容器即可。

**进阶提示**：有时更改只影响可以直接在游戏中用命令 `.reload tablename` 重新加载的表。

现在你可以测试这些更改，并将你的结果作为评论发布在 PR 的 GitHub 页面上！

## 恢复到干净状态

测试完更改后，你需要恢复到干净状态（就像你在将这些更改应用到数据库之前一样）。

- 在**传统安装方式**下，你可以删除你的 `acore_world` 数据库，并使用 DB assembler 生成一个新的。

- 在 **docker 安装方式**下，你可以通过 HeidiSQL 删除 `acore_world` 数据库，然后在 azerothcore-wotlk 目录内运行 `docker compose up`，系统会提示你重新创建 `acore_world` 数据库（按回车键）。

## 报告

关于需要测试什么、如何报告你的测试结果以及其他报告示例的说明，请阅读主 PR 指南中的[这一部分](how-to-test-a-pr#what-needs-to-be-tested)。
