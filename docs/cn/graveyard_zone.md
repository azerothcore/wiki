# graveyard\_zone

[<-返回至:World](database-world)

**\`graveyard\_zone\` 表**

包含与世界地图墓地相关联的区域信息。

此表用于设置指定墓地会接受哪些阵营，同时也用于指定某个区域最近的墓地。

如需查看所有现有墓地区域及其对应 ID 的列表，请查阅 WorldSafeLocs.dbc

**表结构**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)               | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [GhostZone](#ghostzone) | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Faction](#faction)     | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [Comment](#comment)     | TEXT      |            |     |      |         |       |         |

**字段说明**

### ID

墓地的 ID。参见 WorldSafeLocs.dbc

### GhostZone

传送至墓地前幽灵位置所在的区域 ID。参见 AreaTable.dbc

### Faction

墓地所属的队伍（阵营）。

0 - 接受任何阵营

469 - 仅限联盟

67 - 仅限部落

### Comment

用于描述此墓地区域条目的可读注释。
