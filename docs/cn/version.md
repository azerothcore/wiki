# version

[<-返回:World](database-world)

**\`version\` 表**

包含当前核心和数据库版本的信息。

**表结构**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment                             |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ----------------------------------- |
| [core_version][1]   | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       | 启动时转储的核心修订版本            |
| [core_revision][2]  | VARCHAR(120) |            |     | YES  | NULL    |       | 核心修订版本哈希                    |
| [db_version][3]     | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | 世界数据库的版本                    |
| [cache_id][5]       | INT          | SIGNED     |     | YES  | 0       |       | 数据库次要版本                      |

[1]: #coreversion
[2]: #corerevision
[3]: #dbversion
[5]: #cacheid

**字段描述**

### core\_version

你的服务器当前运行的核心版本的完整文本描述。
示例：TrinityCore rev. 8e48ef7863c5 2015-03-22 01:28:02 +0100 (6.x branch) (Win64, Release)

### core\_revision

你的服务器当前运行的核心修订版本哈希，例如 **Unknown** 或 **8e48ef7863c5**。

### db\_version

你的服务器当前运行的数据库版本。示例：**TDB .58**

### cache\_id

`数据库次要版本。示例：58`
