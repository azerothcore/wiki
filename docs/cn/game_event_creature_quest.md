# game\_event\_creature\_quest

[<-返回:World](database-world)

**\`game\_event\_creature\_quest\` 表**

该表保存有关仅应在事件正在进行时才能接取的任务信息。

**表结构**

| 字段             | 类型      | 属性     | 键 | 允许为空 | 默认值 | 额外 | 注释                 |
| ---------------- | --------- | -------- | --- | -------- | ------ | ---- | -------------------- |
| [eventEntry][1]  | TINYINT   | UNSIGNED |     | NO       |        |      | 游戏事件的条目。     |
| [id][2]          | MEDIUMINT | UNSIGNED | PRI | NO       | 0      |      |                      |
| [quest][3]       | MEDIUMINT | UNSIGNED | PRI | NO       | 0      |      |                      |

[1]: #evententry
[2]: #id
[3]: #quest

**字段说明**

### eventEntry

事件 ID。参见 game\_event.eventEntry

### id

NPC ID。参见 creature\_template.entry

### quest

任务 ID。参见 quest\_template.entry
