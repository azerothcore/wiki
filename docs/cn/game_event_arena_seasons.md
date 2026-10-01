# game_event_arena_seasons

[<-返回:World](database-world)

**\`game_event_arena_seasons\` 表**

此信息来自嗅探（sniffs），**不应**被修改。

**表结构**

| 字段             | 类型    | 属性     | 键 | 允许为空 | 默认值 | 额外   | 注释                 |
| ---------------- | ------- | -------- | --- | -------- | ------ | ------ | -------------------- |
| [eventEntry][1]  | TINYINT | UNSIGNED |     | NO       |        | Unique | 游戏事件的条目。     |
| [season][2]      | TINYINT | UNSIGNED |     | NO       |        | Unique | 竞技场赛季编号       |

[1]: #evententry
[2]: #season

**字段说明**

### eventEntry

[game_event.eventEntry](game_event#eventEntry)

### season

竞技场赛季编号：1 - 9

| eventEntry | season | 注释（不属于数据库的一部分）                       |
| ---------- | ------ | :----------------------------------------------- |
| 75         | 1      | TBC - 第 1 赛季："角斗士"（Gladiator）           |
| 76         | 2      | TBC - 第 2 赛季："无情角斗士"（Merciless Gladiator） |
| 55         | 3      | TBC - 第 3 赛季："复仇角斗士"（Vengeful Gladiator） |
| 56         | 4      | TBC - 第 4 赛季："残酷角斗士"（Brutal Gladiator） |
| 57         | 5      | WotLK - 第 5 赛季："致命角斗士"（Deadly Gladiator） |
| 58         | 6      | WotLK - 第 6 赛季："狂怒角斗士"（Furious Gladiator） |
| 59         | 7      | WotLK - 第 7 赛季："无情角斗士"（Relentless Gladiator） |
| 60         | 8      | WotLK - 第 8 赛季："愤怒角斗士"（Wrathful Gladiator） |
| 31         | 9      | 竞技场锦标赛：（请勿使用）                       |
