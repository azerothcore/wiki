# CreatureDisplayInfoExtra.dbc

[`Back-to:DBC`](dbc-index)

**The \`CreatureDisplayInfoExtra.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [creaturedisplayinfoextra_dbc](creaturedisplayinfoextra_dbc) table of the world database.

**Structure**

| Column | Field             | Type   | creaturedisplayinfoextra\_dbc column                            | Comment                                          |
| :----: | :---------------- | :----- | :-------------------------------------------------------------- | :----------------------------------------------- |
| 0      | ID                | uint32 | [ID](creaturedisplayinfoextra_dbc#id)                           |                                                  |
| 1      | DisplayRaceID     | uint32 | [DisplayRaceID](creaturedisplayinfoextra_dbc#displayraceid)     | ID in [ChrRaces.dbc](chrraces)                   |
| 2      | DisplaySexID      | uint32 | [DisplaySexID](creaturedisplayinfoextra_dbc#displaysexid)       |                                                  |
| 3      | SkinID            | uint32 | [SkinID](creaturedisplayinfoextra_dbc#skinid)                   |                                                  |
| 4      | FaceID            | uint32 | [FaceID](creaturedisplayinfoextra_dbc#faceid)                   |                                                  |
| 5      | HairStyleID       | uint32 | [HairStyleID](creaturedisplayinfoextra_dbc#hairstyleid)         |                                                  |
| 6      | HairColorID       | uint32 | [HairColorID](creaturedisplayinfoextra_dbc#haircolorid)         |                                                  |
| 7      | FacialHairID      | uint32 | [FacialHairID](creaturedisplayinfoextra_dbc#facialhairid)       |                                                  |
| 8      | NPCItemDisplay_0  | uint32 | [NPCItemDisplay1](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 9      | NPCItemDisplay_1  | uint32 | [NPCItemDisplay2](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 10     | NPCItemDisplay_2  | uint32 | [NPCItemDisplay3](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 11     | NPCItemDisplay_3  | uint32 | [NPCItemDisplay4](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 12     | NPCItemDisplay_4  | uint32 | [NPCItemDisplay5](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 13     | NPCItemDisplay_5  | uint32 | [NPCItemDisplay6](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 14     | NPCItemDisplay_6  | uint32 | [NPCItemDisplay7](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 15     | NPCItemDisplay_7  | uint32 | [NPCItemDisplay8](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 16     | NPCItemDisplay_8  | uint32 | [NPCItemDisplay9](creaturedisplayinfoextra_dbc#npcitemdisplay)  | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 17     | NPCItemDisplay_9  | uint32 | [NPCItemDisplay10](creaturedisplayinfoextra_dbc#npcitemdisplay) | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 18     | NPCItemDisplay_10 | uint32 | [NPCItemDisplay11](creaturedisplayinfoextra_dbc#npcitemdisplay) | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 19     | Flags             | uint32 | [Flags](creaturedisplayinfoextra_dbc#flags)                     |                                                  |
| 20     | BakeName          | string | [BakeName](creaturedisplayinfoextra_dbc#bakename)               |                                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CreatureDisplayInfoExtra).
