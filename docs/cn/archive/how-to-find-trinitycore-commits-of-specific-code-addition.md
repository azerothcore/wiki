---
redirect_from: "/cn/How-to-find-TrinityCore-commits-of-specific-code-addition"
---

# 如何查找特定代码新增对应的 TrinityCore 提交

有时我们需要从 TrinityCore 导入某些内容，例如我们在代码中看到多了一行或一个文件，并且想更好地了解该新增内容的背景（即引入它的那个提交）。

如何做到这一点：

**1)** 克隆一份 [3.3.5 TrinityCore](https://github.com/TrinityCore/TrinityCore/tree/3.3.5)，并用 [Visual Studio Code](https://code.visualstudio.com/) 或任何其他带有**注释（annotate）**功能的 IDE 打开它。

- 如果使用 Visual Studio Code，你可以安装 [Annotator](https://github.com/ryu1kn/vscode-annotator) 插件。

- 如果使用 CLion（或其他基于 IntelliJ 的 IDE），注释功能默认就有。

- 如果使用其他 IDE，请在 Google 搜索你的 IDE 名称 + "annotate"。

**2)** 转到目标文件或代码行

**3)** 使用 Annotator

#### 在 CLion 或其他基于 IntelliJ 的 IDE 中

右键单击行号并选择 "Annotate"。

#### 在 Visual Studio Code 中

按 CTRL+SHIFT+P（如果是 macOS 则按 CMD+SHIFT+P）并输入 Annotator

![](https://user-images.githubusercontent.com/75517/50727622-af0b7c00-111d-11e9-8423-1c42bc89a297.png)

选择 "Annotate the current file..."，它会打开类似这样的界面：

![](https://user-images.githubusercontent.com/75517/50727632-c9ddf080-111d-11e9-9bd0-9e3673bcd93b.png)

将鼠标移到你想查找对应提交的那一行变更上

![](https://user-images.githubusercontent.com/75517/50727642-0873ab00-111e-11e9-9c5c-aaf166adb972.png)

**4)** 复制提交哈希并粘贴到：

https://github.com/TrinityCore/TrinityCore/commit/PASTE-THE-COMMIT-HASH-HERE

那将是你正在寻找的提交。

**重要提示**：同时检查 [最新版本](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) 中被修改的文件也很有用，因为这些文件可能在更新的提交中又被修改过。

**重要提示 2**：还要查看该提交或 PR 的评论，通常如果有问题，都会以 GitHub 评论的形式进行说明
