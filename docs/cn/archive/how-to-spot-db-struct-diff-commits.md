---
redirect_from: "/cn/How-to-spot-db-struct-diff-commits"
---

# 如何定位数据库结构差异提交

**1)** 克隆一份 [3.3.5 TrinityCore](https://github.com/TrinityCore/TrinityCore/tree/3.3.5)，并用 [Visual Studio Code](https://code.visualstudio.com/) 或任何其他带有**注释（annotate）**功能的 IDE 打开它（例如 IntellIJ 等）。

如果使用 Visual Studio Code，你可以安装 [Annotator](https://github.com/ryu1kn/vscode-annotator) 插件。

**2)** 从一个差异开始，可以是[这些](https://github.com/azerothcore/azerothcore-wotlk/milestone/3)/中的任何一个

例如：

![](https://user-images.githubusercontent.com/75517/50727531-78813180-111c-11e9-8a6b-37f098df8dff.png)

**3)** 选择一个已更改字段的名称并复制它，例如 `BaseAttackTime`，然后在 Visual Studio Code 中查找它

**4)** 滚动直到找到修改它的文件，例如：

![](https://user-images.githubusercontent.com/75517/50727603-66ec5980-111d-11e9-8aed-fb376874bba8.png)

**5)** 按 CTRL+SHIFT+P（如果是 macOS 则按 CMD+SHIFT+P）并输入 Annotator

![](https://user-images.githubusercontent.com/75517/50727622-af0b7c00-111d-11e9-8423-1c42bc89a297.png)

**6)** 选择 "Annotate the current file..."，它会打开类似这样的界面：

![](https://user-images.githubusercontent.com/75517/50727632-c9ddf080-111d-11e9-9bd0-9e3673bcd93b.png)

**7)** 将鼠标移到你想查找对应提交的那一行变更上

![](https://user-images.githubusercontent.com/75517/50727642-0873ab00-111e-11e9-9c5c-aaf166adb972.png)

**8)** 复制提交哈希并粘贴到：

https://github.com/TrinityCore/TrinityCore/commit/PASTE-THE-COMMIT-HASH-HERE

那将是你正在寻找的提交。

**重要提示**：同时检查 [最新版本](https://github.com/TrinityCore/TrinityCore/tree/3.3.5) 中被修改的文件也很有用，因为这些文件可能在更新的提交中又被修改过。
