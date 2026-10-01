# areatrigger\_scripts

[<-返回:World](database-world)

**\`areatrigger\_scripts\` 表**

允许使用 Trinity Script 为区域触发器编写脚本。

**表结构**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]      | MEDIUMINT |            | PRI | NO   |         |       |         |
| [ScriptName][2] | char(64)  |            |     | NO   |         |       |         |

[1]: #entry
[2]: #scriptname

**字段描述**

### entry

这是来自 [AreaTrigger.dbc](dbc-areatrigger) 的触发器标识符

### ScriptName

在核心中为其编写脚本时使用的 ScriptName。
它也可能是 'SmartTrigger'。那样的话，它将使用 [SmartAI](smart_scripts)。

### 示例

| entry | ScriptName        |
| ----- | ----------------- |
| 302   | at_sentry_point   |
| 962   | SmartTrigger      |
| 1447  | SmartTrigger      |
| 1526  | at_ring_of_law    |
| 1726  | at_scent_larkorwi |
