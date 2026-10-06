# SkillRaceClassInfo.dbc

[`Back-to:DBC`](dbc-index)

**The \`SkillRaceClassInfo.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [skillraceclassinfo_dbc](skillraceclassinfo_dbc) table of the world database.

**Structure**

| Column | Field          | Type   | skillraceclassinfo\_dbc column                          | Comment                                                                                                                 |
| :----: | :------------- | :----- | :------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------- |
| 0      | ID             | uint32 | [ID](skillraceclassinfo_dbc#id)                         |                                                                                                                         |
| 1      | SkillID        | uint32 | [SkillID](skillraceclassinfo_dbc#skillid)               |                                                                                                                         |
| 2      | RaceMask       | uint32 | [RaceMask](skillraceclassinfo_dbc#racemask)             | Race mask (1 of 59 values used here also set bits that are not in that file). See [ChrRaces.dbc](chrraces#content)      |
| 3      | ClassMask      | uint32 | [ClassMask](skillraceclassinfo_dbc#classmask)           | Class mask (2 of 39 values used here also set bits that are not in that file). See [ChrClasses.dbc](chrclasses#content) |
| 4      | Flags          | uint32 | [Flags](skillraceclassinfo_dbc#flags)                   |                                                                                                                         |
| 5      | MinLevel       | uint32 | [MinLevel](skillraceclassinfo_dbc#minlevel)             |                                                                                                                         |
| 6      | SkillTierID    | uint32 | [SkillTierID](skillraceclassinfo_dbc#skilltierid)       | ID in [SkillTiers.dbc](dbc-skilltiers)                                                                                  |
| 7      | SkillCostIndex | uint32 | [SkillCostIndex](skillraceclassinfo_dbc#skillcostindex) | ID in [SkillCostsData.dbc](dbc-skillcostsdata)                                                                          |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SkillRaceClassInfo).
