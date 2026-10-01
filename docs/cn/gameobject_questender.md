# gameobject\_questender

[<-返回:World](database-world)

**\`gameobject\_questender\` 表**

保存游戏对象与任务完结者（quest taker）之间的关系。此表中的游戏对象都应属于 QUESTGIVER（2）类型。

**表结构**

| 字段      | 类型      | 属性     | 键 | 空 | 默认值 | 额外 | 注释          |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                  |
| [quest][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 任务标识符 |

[1]: #id
[2]: #quest

**字段说明**

### id

游戏对象的模板 ID。参见 [gameobject\_template.entry](http://www.azerothcore.org/wiki/gameobject_template#entry)

### quest

此游戏对象所完成的任务的 ID。参见 [quest\_template.id](http://www.azerothcore.org/wiki/quest_template#id)
