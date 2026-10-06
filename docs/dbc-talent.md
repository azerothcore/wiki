# Talent.dbc

[`Back-to:DBC`](dbc-index)

**The \`Talent.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [talent_dbc](talent_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | talent\_dbc column                            | Comment                                                                             |
| :----: | :-------------- | :----- | :-------------------------------------------- | :---------------------------------------------------------------------------------- |
| 0      | ID              | uint32 | [ID](talent_dbc#id)                           |                                                                                     |
| 1      | TabID           | uint32 | [TabID](talent_dbc#tabid)                     | ID in [TalentTab.dbc](dbc-talenttab)                                                |
| 2      | TierID          | uint32 | [TierID](talent_dbc#tierid)                   |                                                                                     |
| 3      | ColumnIndex     | uint32 | [ColumnIndex](talent_dbc#columnindex)         |                                                                                     |
| 4      | SpellRank_0     | uint32 | [SpellRank_1](talent_dbc#spellrank)           | ID in [Spell.dbc](spell)                                                            |
| 5      | SpellRank_1     | uint32 | [SpellRank_2](talent_dbc#spellrank)           | ID in [Spell.dbc](spell)                                                            |
| 6      | SpellRank_2     | uint32 | [SpellRank_3](talent_dbc#spellrank)           | ID in [Spell.dbc](spell)                                                            |
| 7      | SpellRank_3     | uint32 | [SpellRank_4](talent_dbc#spellrank)           | ID in [Spell.dbc](spell)                                                            |
| 8      | SpellRank_4     | uint32 | [SpellRank_5](talent_dbc#spellrank)           | ID in [Spell.dbc](spell)                                                            |
| 9      | SpellRank_5     | uint32 | [SpellRank_6](talent_dbc#spellrank)           |                                                                                     |
| 10     | SpellRank_6     | uint32 | [SpellRank_7](talent_dbc#spellrank)           |                                                                                     |
| 11     | SpellRank_7     | uint32 | [SpellRank_8](talent_dbc#spellrank)           |                                                                                     |
| 12     | SpellRank_8     | uint32 | [SpellRank_9](talent_dbc#spellrank)           |                                                                                     |
| 13     | PrereqTalent_0  | uint32 | [PrereqTalent_1](talent_dbc#prereqtalent)     | ID in [Talent.dbc](dbc-talent) (2 of the 125 values used here are not in that file) |
| 14     | PrereqTalent_1  | uint32 | [PrereqTalent_2](talent_dbc#prereqtalent)     |                                                                                     |
| 15     | PrereqTalent_2  | uint32 | [PrereqTalent_3](talent_dbc#prereqtalent)     |                                                                                     |
| 16     | PrereqRank_0    | uint32 | [PrereqRank_1](talent_dbc#prereqrank)         |                                                                                     |
| 17     | PrereqRank_1    | uint32 | [PrereqRank_2](talent_dbc#prereqrank)         |                                                                                     |
| 18     | PrereqRank_2    | uint32 | [PrereqRank_3](talent_dbc#prereqrank)         |                                                                                     |
| 19     | Flags           | uint32 | [Flags](talent_dbc#flags)                     |                                                                                     |
| 20     | RequiredSpellID | uint32 | [RequiredSpellID](talent_dbc#requiredspellid) |                                                                                     |
| 21     | CategoryMask_0  | uint32 | [CategoryMask_1](talent_dbc#categorymask)     |                                                                                     |
| 22     | CategoryMask_1  | uint32 | [CategoryMask_2](talent_dbc#categorymask)     |                                                                                     |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Talent).
