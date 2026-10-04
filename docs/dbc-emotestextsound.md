# EmotesTextSound.dbc

[`Back-to:DBC`](dbc-index)

**The \`EmotesTextSound.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [emotestextsound_dbc](emotestextsound_dbc) table of the world database.

**Structure**

| Column | Field        | Type   | emotestextsound\_dbc column                      | Comment |
| :----: | :----------- | :----- | :----------------------------------------------- | :------ |
| 0      | ID           | uint32 | [ID](emotestextsound_dbc#id)                     |         |
| 1      | EmotesTextID | uint32 | [EmotesTextID](emotestextsound_dbc#emotestextid) |         |
| 2      | RaceID       | uint32 | [RaceID](emotestextsound_dbc#raceid)             |         |
| 3      | SexID        | uint32 | [SexID](emotestextsound_dbc#sexid)               |         |
| 4      | SoundID      | uint32 | [SoundID](emotestextsound_dbc#soundid)           |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/EmotesTextSound).
