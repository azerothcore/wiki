---
redirect_from: "/cn/Environment-Variable"
---

# 环境变量

### 简介
要在命令行中使用 MySQL 服务器，你必须拥有正确的系统路径。这通常是自动完成的。

如何检查 MySQL 服务器是否已加入环境变量：
* 按 `Windows + R` 并输入 cmd
* 在打开的 CMD 中输入 `mysql`

如果 MySQL 服务器不在环境变量中，你会收到类似这样的错误：`Not recognised command`

### 要求
必须已安装 MySQL 服务器，如果你还没有安装 MySQL 服务器，请参考[本教程](http://www.azerothcore.org/wiki/Requirements)

### 操作步骤

* 找到 `mysql.exe`。例如：`C:\Program Files\MySQL\MySQL Server 5.6\bin`
* 搜索 `编辑系统环境变量`
* 点击 `环境变量` 并找到 `User variables for $USERNAME`
* 选择 `Path` 变量并点击编辑
* 点击 `新建` 按钮，输入你之前找到的 `mysql.exe` 的路径
* * 示例：`C:\Program Files\MySQL\MySQL Server 5.6\bin`

现在一切就绪，你可以从命令行访问 `mysql` 了。

要检查设置是否正确完成，请按 `Windows + R` 并输入 cmd，当你在控制台中输入 `mysql` 时，你会看到所有选项。

[点击此处返回数据库安装](http://www.azerothcore.org/wiki/Database-Setup)
