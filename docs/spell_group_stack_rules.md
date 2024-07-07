# spell\_group\_stack\_rules

[<-Back-to:World](database-world)

**The \`spell\_group\_stack\_rules\` table**

Table defines if auras in one spell\_group can't stack with each other.

Notes: The table doesn't affect persistent area auras stacking or passive auras stacking (they can stack always) or spells belonging to same spell\_rank (they are always subject of SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE rule)

**Table Structure**

| Field                       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [group\_id](#groupid)       | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [stack\_rule](#stackrule)   | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [description](#description) | VARCHAR(150) |            |     | NO   |         |       |         |

**Description of the fields**

### group\_id

Id of group in [spell\_group](spell_group#id) table. The spell\_group may contain another spell\_groups inside, if so stacking rule needs to be defined for these groups separately.

### stack\_rule

Enum SpellGroupStackFlags in core:

| Id  |       | Stack Rule Name                              | Description                                  |
| --- | ----- | -------------------------------------------- | -------------------------------------------- |
| 0   | 0x00  | SPELL\_GROUP\_STACK\_RULE\_DEFAULT           | No stacking rule defined - placeholder       |
| 1   | 0x01  | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE         | Auras from group can't stack with each other |
| 2   | 0x02  | SPELL\_GROUP\_STACK\_FLAG\_NOT\_SAME\_CASTER |                                              |
| 4   | 0x04  | SPELL\_GROUP\_STACK\_FLAG\_FLAGGED           |                                              |
| 8   | 0x08  | SPELL\_GROUP\_STACK\_FLAG\_NEVER\_STACK      |                                              |
| 10  | 0x10  | SPELL\_GROUP\_STACK\_FLAG\_EFFECT\_EXCLUSIVE |                                              |
| 20  | 0x20  | SPELL\_GROUP\_STACK\_FLAG\_MAX               |                                              |
|     |       | // Internal use                              |                                              |
| 100 | 0x100 | SPELL\_GROUP\_STACK\_FLAG\_FORCED\_STRONGEST |                                              |
| 200 | 0x200 | SPELL\_GROUP\_STACK\_FLAG\_FORCED\_WEAKEST   |                                              |

### description

A short description of what type of spells are in the group and what rule is applied.
