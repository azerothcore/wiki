# SpellDifficulty.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellDifficulty.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spelldifficulty_dbc](spelldifficulty_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | spelldifficulty\_dbc column                                   | Comment |
| :----: | :------------------ | :----- | :------------------------------------------------------------ | :------ |
| 0      | ID                  | uint32 | [ID](spelldifficulty_dbc#id)                                  |         |
| 1      | DifficultySpellID_0 | int32  | [DifficultySpellID_1](spelldifficulty_dbc#difficultyspellid1) |         |
| 2      | DifficultySpellID_1 | int32  | [DifficultySpellID_2](spelldifficulty_dbc#difficultyspellid2) |         |
| 3      | DifficultySpellID_2 | int32  | [DifficultySpellID_3](spelldifficulty_dbc#difficultyspellid3) |         |
| 4      | DifficultySpellID_3 | int32  | [DifficultySpellID_4](spelldifficulty_dbc#difficultyspellid4) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellDifficulty).
