# transports

[<-返回:World](database-world)

**\`transports\` 表**

此表包含所有类型 15 的交通工具（船只和飞艇）。所有其他类型的交通工具，其帧时间均从 TransportAnimation.dbc 读取。

**表结构**

| Field           | Type      | Attributes | Key    | Null | Default        | Extra | Comment |
| --------------- | --------- | ---------- | ------ | ---- | -------------- | ----- | ------- |
| [Guid][1]       | INT       | UNSIGNED   | PRI    | NO   | AUTO_INCREMENT |       |         |
| [Entry][2]      | MEDIUMINT | UNSIGNED   | UNIQUE | NO   | 0              |       |         |
| [Name][3]       | TEXT      |            |        | YES  | NULL           |       |         |
| [ScriptName][4] | CHAR(64)  |            |        | NO   | ' '            |       |         |

[1]: #guid
[2]: #entry
[3]: #name
[4]: #scriptname

**字段描述**

### guid

交通工具的唯一标识符。每次添加新的 guid 时，只需在最大 guid 基础上加一（1）。

### entry

用于该交通工具的 [gameobject_template.entry](gameobject_template#entry)。它必须是类型 15 的游戏对象。

### name

用于描述交通工具条目的任意名称。

### ScriptName

该交通工具的脚本名称。引用 ScriptDev 或 SmartAI 中的脚本。

**注意：** 交通工具拥有独立的地图：https://wow.tools/dbc/?dbc=map&build=3.3.5.12340#page=1&colFilter[1]=Transport
