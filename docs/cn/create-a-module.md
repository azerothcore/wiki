---
redirect_from: "/cn/Create-a-Module"
---

# 创建模块

## **如何创建一个模块**

在开始之前，我们建议你先阅读[关于模块化结构的文档](the-modular-structure)，以了解 AzerothCore 的工作方式。

### 资源

- 模块模板（强烈推荐）：[https://github.com/azerothcore/skeleton-module](https://github.com/azerothcore/skeleton-module)
- 脚本模板：https://github.com/azerothcore/azerothcore-boilerplates
- 核心中的所有钩子都列在 [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h) 中。如果你需要自定义钩子，可以通过[提交 PR](how-to-create-a-pr) 将其添加到核心中。
- 目录中列出的现有模块：[https://www.azerothcore.org/catalogue.html](https://www.azerothcore.org/catalogue.html)
- 如果你需要为你的模块创建新的钩子，请遵循本指南：[如何创建新的钩子](hooks-script)

### **基础**

1. 在 `modules/` 目录下创建一个文件夹

2. 现在你可以开发并向主项目添加任何内容，例如一些脚本，甚至整个库

注意：我们建议使用 AzerothCore 的[目录结构](directory-structure)标准来更好地组织你的模块，并熟悉主项目。

### **添加第一个脚本**

1. 在继续之前，我们建议你先遵循我们关于如何为 AzerothCore 创建脚本的指南

2. 创建好脚本后，你需要创建一个 .cpp 文件来处理脚本的加载。

  例如（假设你创建了一个 src 文件夹）：

  `my_custom_loader.cpp`

 ```cpp
// 来自 SC
void AddMyCustomScripts();

// 添加所有
// 参见命名约定 https://github.com/azerothcore/azerothcore-wotlk/blob/master/doc/changelog/master#how-to-upgrade-4
// 另外，将模块文件夹名称中的所有 '-' 替换为 '_'
void Addmod_my_customScripts()
{
    AddMyCustomScripts();
}
```

  注意：AddMyCustomScripts 由以下几部分组成：

  Add（前缀）

  MyCustom（脚本的唯一名称标识符，用于避免函数冲突）

  Scripts（后缀）

### **创建自定义配置文件**

如果你需要为你的模块添加一个会随服务器一起安装的自定义配置文件，步骤非常简单。

1. 在文件夹 `./conf` 中添加一个扩展名为 `.conf.dist` 的文件
2. 完成。是的，真的，仅此而已。

### **将你的数据库文件添加到 db_assembler**

你可以创建 base、updates 和自定义 SQL，它们会被自动加载到我们的 db_assembler 中。

**正在完善中……**

### **完成创建你的模块了吗？**

将你的模块发布到我们的目录：https://www.azerothcore.org/catalogue.html#/how-to
