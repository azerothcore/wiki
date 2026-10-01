---
redirect_from: "/cn/TrinityCore-to-AzerothCore-characters-migration"
---

# TrinityCore 到 AzerothCore 角色与认证数据迁移工具

### 1) 安装 AzerothCore

按照安装说明安装一套全新的 AzerothCore（转换后我们会用到它）。

设置 AzerothCore 的说明可以[在这里](http://www.azerothcore.org/wiki/Installation)找到。

在继续之前，请确保你已完成全新安装并且没有额外模块即可正常工作。

### 2) 备份你的 TrinityCore 数据库

在继续之前备份你的 TrinityCore 数据库（做任何更改前始终要备份）
- auth
- characters
- world

### 3) 角色与认证数据迁移

下载 [TC-to-AC 角色迁移工具](https://github.com/azerothcore/tool-tc-migration)。

以下文件必须按 1 到 5 的顺序在你的 TrinityCore characters 数据库上运行：

- 1_CREATE_CLEANUP_TABLES
- 2_CREATE_MISSING_TABLES
- 3_ALTER_TABLES
- 4_CLEANUP_AND_CONVERT_SPELLS
- 5_FINAL_CLEANUP

在你的 TrinityCore auth 数据库上运行第 6 个文件

- 6_AUTH_CONVERTER

将你的 AzerothCore 服务器的 `worldserver.conf` 改为指向你转换后的（原 TrinityCore）characters 数据库，然后启动 `./worldserver`
