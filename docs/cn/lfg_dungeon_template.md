# lfg_dungeon_template

[<-返回:World](database-world)

**\`lfg_dungeon_template\` 表**

用于为被精神控制（Mind Control）的 NPC 设置法术冷却时间。

**表结构**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment                        |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------ |
| [dungeonId](#dungeonid)         | INT          | UNSIGNED   | PRI | NO   | 0       |       | Unique id from LFGDungeons.dbc |
| [name](#name)                   | VARCHAR(255) |            |     | YES  | NULL    |       |                                |
| [position_x](#positionx)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [position_y](#positiony)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [position_z](#positionz)        | FLOAT        |            |     | NO   | 0       |       |                                |
| [orientation](#orientation)     | FLOAT        |            |     | NO   | 0       |       |                                |
| [VerifiedBuild](#verifiedbuild) | INT          |            |     | YES  | NULL    |       |                                |

**字段说明**

### DungionId

来自 LFGDungeons.dbc 的唯一 id

### name

地下城名称

### poisition_x

`field-no-description|3`

### poisition_y

`field-no-description|4`

### poisition_z

`field-no-description|5`

### orientation

`field-no-description|6`

### VerifiedBuild

该字段用于确定数据是否来自已验证的嗅探（sniff）数据。

如果值为 0，则表示它尚未被解析，或者继承自旧版数据库或其他核心。

如果值大于 0，则表示它已使用特定客户端构建的嗅探数据解析过。

如果值为 -客户端构建号，则表示它使用特定客户端构建的 WDB 文件解析，并在之后因某些特殊需要而手动编辑。
