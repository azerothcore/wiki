# spell\_script\_names

[<-返回:世界数据库](database-world)

**\`spell\_script\_names\` 表**

保存法术 ID 与 ScriptName 的对应关系，供法术脚本（spell script）使用。

**表结构**

| Field           | Type     | Attributes | Key    | Null | Default | Extra | Comment |
| --------------- | -------- | ---------- | ------ | ---- | ------- | ----- | ------- |
| [spell_id][1]   | INT      | SIGNED     | UNIQUE | NO   | NONE    |       |         |
| [ScriptName][2] | char(64) | UNSIGNED   | UNIQUE | NO   | NONE    |       |         |

[1]: #spellid
[2]: #scriptname

**字段说明**

### spell\_id

要绑定的法术 ID。如果为负数，且是某个法术的第一级（rank），则包含 spell\_ranks 表中该法术的所有等级。

一个法术可以分配多个脚本。

### ScriptName

指定法术所使用的脚本名称。
