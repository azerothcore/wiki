# EmotesText.dbc

[`Back-to:DBC`](dbc-index)

**The \`EmotesText.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [emotestext_dbc](emotestext_dbc) table of the world database.

**Structure**

| Column | Field        | Type   | emotestext\_dbc column                   | Comment                                        |
| :----: | :----------- | :----- | :--------------------------------------- | :--------------------------------------------- |
| 0      | ID           | uint32 | [ID](emotestext_dbc#id)                  |                                                |
| 1      | Name         | string | [Name](emotestext_dbc#name)              |                                                |
| 2      | EmoteID      | uint32 | [EmoteID](emotestext_dbc#emoteid)        | ID in [Emotes.dbc](emotes)                     |
| 3      | EmoteText_0  | uint32 | [EmoteText_1](emotestext_dbc#emotetext)  | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 4      | EmoteText_1  | uint32 | [EmoteText_2](emotestext_dbc#emotetext)  | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 5      | EmoteText_2  | uint32 | [EmoteText_3](emotestext_dbc#emotetext)  | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 6      | EmoteText_3  | uint32 | [EmoteText_4](emotestext_dbc#emotetext)  |                                                |
| 7      | EmoteText_4  | uint32 | [EmoteText_5](emotestext_dbc#emotetext)  | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 8      | EmoteText_5  | uint32 | [EmoteText_6](emotestext_dbc#emotetext)  |                                                |
| 9      | EmoteText_6  | uint32 | [EmoteText_7](emotestext_dbc#emotetext)  | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 10     | EmoteText_7  | uint32 | [EmoteText_8](emotestext_dbc#emotetext)  |                                                |
| 11     | EmoteText_8  | uint32 | [EmoteText_9](emotestext_dbc#emotetext)  | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 12     | EmoteText_9  | uint32 | [EmoteText_10](emotestext_dbc#emotetext) | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 13     | EmoteText_10 | uint32 | [EmoteText_11](emotestext_dbc#emotetext) |                                                |
| 14     | EmoteText_11 | uint32 | [EmoteText_12](emotestext_dbc#emotetext) |                                                |
| 15     | EmoteText_12 | uint32 | [EmoteText_13](emotestext_dbc#emotetext) | ID in [EmotesTextData.dbc](dbc-emotestextdata) |
| 16     | EmoteText_13 | uint32 | [EmoteText_14](emotestext_dbc#emotetext) |                                                |
| 17     | EmoteText_14 | uint32 | [EmoteText_15](emotestext_dbc#emotetext) |                                                |
| 18     | EmoteText_15 | uint32 | [EmoteText_16](emotestext_dbc#emotetext) |                                                |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/EmotesText).
