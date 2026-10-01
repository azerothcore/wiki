# 最佳实践

一系列使用 AzerothCore 的最佳实践。


## 自定义修改

- **永远不要**在 AzerothCore 源码中添加自定义修改。请改为[创建模块](http://www.azerothcore.org/wiki/Create-a-Module)。

如果你需要新的 hook 来在模块中实现你的自定义修改，欢迎提交一个实现它们的 PR。

原因：

1. 保持你的基础源码整洁，将更容易更新它
2. 将你的自定义内容保存在模块中，将允许你轻松地启用/禁用它们，以排查任何潜在的问题
3. 模块化的软件更容易维护


## Pull Requests (PR)

- 将你的 fork 更新到最新的 Master 分支。

原因：

1. 有助于避免合并冲突
2. 你将以应用于最新 master 版本的方式实现（并测试）你的修改

- **永远不要**向 `master` 分支推送更改。始终让你的 `master` 分支保持干净。

当你创建新的 PR 时，先执行 `git checkout master`，然后使用 `git checkout -b new-branch` 创建一个新分支。

原因：

1. 这将允许你创建多个相互独立的 PR
2. 这将允许你轻松地将分支更新到最新的 master：先同步你的 fork，然后将 `master` 合并到你的 PR 分支中。
