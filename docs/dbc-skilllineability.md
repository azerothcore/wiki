# SkillLineAbility.dbc

[`Back-to:DBC`](dbc-index)

**The \`SkillLineAbility.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [skilllineability_dbc](skilllineability_dbc) table of the world database.

**Structure**

| Column | Field                    | Type   | skilllineability\_dbc column                                              | Comment                                                                         |
| :----: | :----------------------- | :----- | :------------------------------------------------------------------------ | :------------------------------------------------------------------------------ |
| 0      | ID                       | uint32 | [ID](skilllineability_dbc#id)                                             |                                                                                 |
| 1      | SkillLine                | uint32 | [SkillLine](skilllineability_dbc#skillline)                               | ID in [SkillLine.dbc](skillline)                                                |
| 2      | Spell                    | uint32 | [Spell](skilllineability_dbc#spell)                                       | ID in [Spell.dbc](spell) (33 of the 9751 values used here are not in that file) |
| 3      | RaceMask                 | uint32 | [RaceMask](skilllineability_dbc#racemask)                                 | Race mask. See [ChrRaces.dbc](chrraces#content)                                 |
| 4      | ClassMask                | uint32 | [ClassMask](skilllineability_dbc#classmask)                               | Class mask. See [ChrClasses.dbc](chrclasses#content)                            |
| 5      | ExcludeRace              | uint32 | [ExcludeRace](skilllineability_dbc#excluderace)                           |                                                                                 |
| 6      | ExcludeClass             | uint32 | [ExcludeClass](skilllineability_dbc#excludeclass)                         |                                                                                 |
| 7      | MinSkillLineRank         | uint32 | [MinSkillLineRank](skilllineability_dbc#minskilllinerank)                 |                                                                                 |
| 8      | SupercededBySpell        | uint32 | [SupercededBySpell](skilllineability_dbc#supercededbyspell)               | ID in [Spell.dbc](spell) (18 of the 765 values used here are not in that file)  |
| 9      | AcquireMethod            | uint32 | [AcquireMethod](skilllineability_dbc#acquiremethod)                       |                                                                                 |
| 10     | TrivialSkillLineRankHigh | uint32 | [TrivialSkillLineRankHigh](skilllineability_dbc#trivialskilllinerankhigh) |                                                                                 |
| 11     | TrivialSkillLineRankLow  | uint32 | [TrivialSkillLineRankLow](skilllineability_dbc#trivialskilllineranklow)   |                                                                                 |
| 12     | CharacterPoints_0        | uint32 | [CharacterPoints_1](skilllineability_dbc#characterpoints)                 |                                                                                 |
| 13     | CharacterPoints_1        | uint32 | [CharacterPoints_2](skilllineability_dbc#characterpoints)                 |                                                                                 |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SkillLineAbility).
