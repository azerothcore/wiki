---
redirect_from: "/cn/Upgrade-from-pre-2.0.0-to-latest-master"
---

# 从 2.0.0 之前版本升级到最新 master

本教程介绍如何将任何现有服务器从 [2.0.0 发布](https://github.com/azerothcore/azerothcore-wotlk/releases/tag/v2.0.0) 之前的版本升级到最新的 `master` 版本。

**注意**：建议在每次更新前都备份你的数据库。

### 步骤 1：升级到最后一个 2.0.0 提交

你首先需要将服务器更新到[这个提交](https://github.com/azerothcore/azerothcore-wotlk/commit/1fc22a74088e235e78fa02decbaf0864899477d7)，运行：

`git checkout 1fc22a74088e235e78fa02decbaf0864899477d7`

现在，像[你平时做的那样](database-keeping-the-server-up-to-date)更新你的**数据库**。

### 步骤 2：升级到最新 master

更新到最新 master：

`git checkout master; git pull;`

**注意**：如果你在使用自己的 AC 分支（fork），照常需要[同步它](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)

现在，（再次）像[你平时做的那样](keeping-the-server-up-to-date)更新你的**核心和数据库**。
