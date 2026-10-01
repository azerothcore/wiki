# spell\_group\_stack\_rules

[<-返回至:World](database-world)

**\`spell\_group\_stack\_rules\` 表**

此表定义同一 spell\_group 中的光环是否不能相互叠加。

注意：此表不影响持续性区域光环的叠加或被动光环的叠加（它们始终可以叠加），也不影响属于同一 spell\_rank 的法术（它们始终受 SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE 规则约束）。

**表结构**

| Field                       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [group\_id](#groupid)       | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [stack\_rule](#stackrule)   | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [description](#description) | VARCHAR(150) |            |     | NO   |         |       |         |

**字段说明**

### group\_id

[spell\_group](spell_group#id) 表中的组 id。spell\_group 内部可能包含其他 spell\_group，如果是这样，则需要为这些组分别定义叠加规则。

### stack\_rule

核心中的枚举 SpellGroupStackFlags：

| Id  |       | Stack Rule Name                              | Description                                  |
| --- | ----- | -------------------------------------------- | -------------------------------------------- |
| 0   | 0x00  | SPELL\_GROUP\_STACK\_RULE\_DEFAULT           | 未定义叠加规则 - 占位符                      |
| 1   | 0x01  | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE         | 来自该组的光环不能相互叠加                   |
| 2   | 0x02  | SPELL\_GROUP\_STACK\_FLAG\_NOT\_SAME\_CASTER |                                              |
| 4   | 0x04  | SPELL\_GROUP\_STACK\_FLAG\_FLAGGED           |                                              |
| 8   | 0x08  | SPELL\_GROUP\_STACK\_FLAG\_NEVER\_STACK      |                                              |
| 10  | 0x10  | SPELL\_GROUP\_STACK\_FLAG\_EFFECT\_EXCLUSIVE |                                              |
| 20  | 0x20  | SPELL\_GROUP\_STACK\_FLAG\_MAX               |                                              |
|     |       | // Internal use                              |                                              |
| 100 | 0x100 | SPELL\_GROUP\_STACK\_FLAG\_FORCED\_STRONGEST |                                              |
| 200 | 0x200 | SPELL\_GROUP\_STACK\_FLAG\_FORCED\_WEAKEST   |                                              |

### description

对该组中包含何种类型的法术以及应用了何种规则所做的简短描述。
