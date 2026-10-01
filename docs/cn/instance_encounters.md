# instance\_encounters

[<-返回至:World](database-world)

**`instance\_encounters` 表**

副本战斗的定义。供随机副本（LFG）使用。

**表结构**

| Field                     | Type         | Attributes | Key | Null | Default | Extra | Comment                                                                 |
| ------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------- |
| [entry][1]                | INT          | UNSIGNED   | PRI | NO   | 0       |       | Unique entry from DungeonEncounter.dbc                                  |
| [creditType][2]           | TINYINT      | UNSIGNED   |     | NO   | 0       |       |                                                                         |
| [creditEntry][3]          | INT          | UNSIGNED   |     | NO   | 0       |       |                                                                         |
| [lastEncounterDungeon][4] | SMALLINT     | UNSIGNED   |     | NO   | 0       |       | If not 0, LfgDungeon.dbc entry for the instance it is last encounter in |
| [comment][5]              | varchat(255) | SIGNED     |     | NO   | "       |       |                                                                         |

[1]: #entry
[2]: #credittype
[3]: #creditentry
[4]: #lastencounterdungeon
[5]: #comment

**字段说明**

### entry

来自 [DungeonEncounter.dbc](https://wowdev.wiki/DB/DungeonEncounter) 的唯一条目

### creditType

参见枚举 EncounterCreditType。

ENCOUNTER\_CREDIT\_KILL\_CREATURE = 0

ENCOUNTER\_CREDIT\_CAST\_SPELL = 1

### creditEntry

如果 creditType = 0，则此字段的值为生物条目（creature entry）。参见 creature\_template.entry

如果 creditType = 1，则此字段的值为一个法术。参见 Spell.dbc。

### lastEncounterDungeon

对 [LfgDungeon.dbc](https://wowdev.wiki/DB/LFGDungeons) 条目的引用，表示此战斗在其所在副本中为最后一战。如果为 0，则此战斗不是最后一战。

### comment

用于便于识别的副本战斗注释。仅使用战斗名称。
