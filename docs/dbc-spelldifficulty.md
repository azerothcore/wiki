# SpellDifficulty.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellDifficulty.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spelldifficulty_dbc](spelldifficulty_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | spelldifficulty\_dbc column                                   | Comment                                                                       |
| :----: | :------------------ | :----- | :------------------------------------------------------------ | :---------------------------------------------------------------------------- |
| 0      | ID                  | uint32 | [ID](spelldifficulty_dbc#id)                                  |                                                                               |
| 1      | DifficultySpellID_0 | int32  | [DifficultySpellID_1](spelldifficulty_dbc#difficultyspellid1) | ID in [Spell.dbc](spell) (3 of the 580 values used here are not in that file) |
| 2      | DifficultySpellID_1 | int32  | [DifficultySpellID_2](spelldifficulty_dbc#difficultyspellid2) | ID in [Spell.dbc](spell) (3 of the 579 values used here are not in that file) |
| 3      | DifficultySpellID_2 | int32  | [DifficultySpellID_3](spelldifficulty_dbc#difficultyspellid3) | ID in [Spell.dbc](spell) (1 of the 296 values used here are not in that file) |
| 4      | DifficultySpellID_3 | int32  | [DifficultySpellID_4](spelldifficulty_dbc#difficultyspellid4) | ID in [Spell.dbc](spell) (1 of the 294 values used here are not in that file) |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellDifficulty).
