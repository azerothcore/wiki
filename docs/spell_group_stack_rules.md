# spell\_group\_stack\_rules

[<-Back-to:World](database-world)

**The \`spell\_group\_stack\_rules\` table**

Table defines if auras in one spell\_group can't stack with each other.

Notes: The table doesn't affect persistent area auras stacking or passive auras stacking (they can stack always) or spells belonging to same spell\_rank (they are always subject of SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE rule)

**Table: spell\_group\_stack\_rules's Structure**

| Field                       | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [group\_id](#groupid)       | INT          | UNSIGNED | NO   | PRI | 0       |       |         |
| [stack\_rule](#stackrule)   | TINYINT      |          | NO   |     | 0       |       |         |
| [description](#description) | VARCHAR(150) |          | NO   |     | ''      |       |         |

**Description of the table's fields**

### group\_id

Id of group in [spell\_group](spell_group#id) table. The spell\_group may contain another spell\_groups inside, if so stacking rule needs to be defined for these groups separately.

### stack\_rule

Enum `SpellGroupStackRule` in the core:

| Value | Name                                                | Description                                                                                                        |
| ----- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 0     | SPELL\_GROUP\_STACK\_RULE\_DEFAULT                   | No stacking rule, the auras stack normally.                                                                         |
| 1     | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE                 | Auras from the group can not stack with each other. A new aura replaces the old one.                               |
| 2     | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE\_FROM\_SAME\_CASTER | Auras from the group can not stack with each other when they come from the same caster.                         |
| 3     | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE\_SAME\_EFFECT     | The auras stack, but for effects of the same type only the strongest one is used.                                   |
| 4     | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE\_HIGHEST         | Only the strongest aura from the group is kept. A weaker aura can not be applied while a stronger one is active.     |

### description

A short description of what type of spells are in the group and what rule is applied.
