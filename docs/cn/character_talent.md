# character\_talent

[<-返回:角色库](database-characters)

**\`character\_talent\` 表**

包含每个角色的全部个人天赋数据。该表仅用作存储表，当玩家切换专精时，数据会从这张表读取并写入 character_spell，反之亦然。

**表结构**

| 字段 | 类型 | 属性 | 键 | 空 | 默认值 | 额外 | 备注 |
| ------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]     | INT       | UNSIGNED   | PRI | NO   |         |       |         |
| [spell][2]    | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [specMask][3] | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #guid
[2]: #spell
[3]: #specmask

**字段说明**

### guid

角色全局唯一标识符（guid）。参见 [characters.guid](characters#guid)。

### spell

法术 ID。参见 [Spell.dbc](spell) 第 1 列。

### specMask

保存使用该天赋的专精的位掩码。
| 值 | 类型                              |
| ----- | --------------------------------- |
| 1     | 第一专精                        |
| 2     | 第二专精                       |
| 3     | 双专精                        |
