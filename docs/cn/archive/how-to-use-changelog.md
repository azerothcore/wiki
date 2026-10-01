# 如何使用更新日志

本项目所有破坏性/重要的变更都会记录在 `/docs/changelog/master` 文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)，并且本项目遵循 [语义化版本](https://semver.org/spec/v2.0.0.html)（Semantic Versioning）。

**这份更新日志应为开发人员提供一种简便的方式来升级他们与 AzerothCore 相关的代码**（例如模块、API、脚本等）。它并不是用来跟踪所有变更的（我们有 git 历史来做这件事）。因此，只需遵循两条黄金法则：

- 当你添加了其他人可以使用的破坏性变更、安全修复或重要的新功能时，**一定要写**更新日志。
- 当你添加的是小修复或小改进时，**不要写**更新日志。

## 如何创建更新日志

为 PR 创建更新日志与创建新的 SQL 文件类似。在 `doc/changelog/pendings` 文件夹下，你会找到一个 `create.sh` 脚本。

运行此脚本会在同一文件夹中创建一个新的更新日志文件，它会被自动命名为 `changes_<timestamp>.md`。

PR 合并后，我们的流水线会将你的文件合并到 `doc/changelog/master` 中，并自动在该文件内创建一个新章节。这个章节将以新的版本号命名，版本号基于根目录下 `acore.json` 文件中的上一个版本自动递增。

例如：如果当前版本是 `1.0.0-dev.1`，你的 PR 合并后，`acore.json` 中的版本会自动变为 `1.0.0-dev.2`，并且在 `master` 更新日志下会创建一个名为 `## 1.0.0-dev.2` 的新章节。

这种方法对于模块跟踪兼容性也非常有用

## 如何编写更新日志

必须使用 "[Keep a Changelog](https://keepachangelog.com/en/1.0.0/)" 格式，并正确使用以下类型的章节标题：

- Added 用于新功能。
- Changed 用于对现有功能的修改。
- Deprecated 用于即将被移除的功能。
- Removed 用于已被移除的功能。
- Security 用于漏洞相关。

你必须为每种不同类型的变更创建一个新的 H3 章节（markdown 中的 `###`）。

例如：

```
### Added

- new hooks X, Y
- new formula for Z

### Changed

- return value for hook X, now it's boolean instead of void
```

### 记录如何升级

在上述章节之后，你必须描述升级代码所需的步骤。这是**最重要的部分**，对模块作者尤其有用，他们可以基于你的更改修复自己的代码，而不必费力阅读大量提交并四处查找信息。

为此，你可以使用我们的 `create.sh` 生成的 `### How to upgrade` 章节。请尽可能详细。如果说明非常长，需要超过几行（例如一整页 wiki），那么你可以直接链接到该页面。

示例：

```
### How to upgrade

- The hook OnCheck of the Achievement script class now returns a boolean instead of a void. Add `return true` to your methods if you don't want to change the original behaviour. 
```

## 如何发布新的主版本

这是一个手动过程。每当我们发布一个新的主版本（4.0.0、5.0.0 等）时，都需要将 `master` 移入 `doc/changelog/previous-versions` 文件夹，并使用 `v[major].x` 这样的格式重命名。之后，我们需要创建一个新的空白 `master` 文件
