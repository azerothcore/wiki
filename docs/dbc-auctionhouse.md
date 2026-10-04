# AuctionHouse.dbc

[`Back-to:DBC`](dbc-index)

**The \`AuctionHouse.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [auctionhouse_dbc](auctionhouse_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | auctionhouse\_dbc column                            | Comment |
| :----: | :-------------- | :----- | :-------------------------------------------------- | :------ |
| 0      | ID              | uint32 | [ID](auctionhouse_dbc#id)                           |         |
| 1      | FactionID       | uint32 | [FactionID](auctionhouse_dbc#factionid)             |         |
| 2      | DepositRate     | uint32 | [DepositRate](auctionhouse_dbc#depositrate)         |         |
| 3      | ConsignmentRate | uint32 | [ConsignmentRate](auctionhouse_dbc#consignmentrate) |         |
| 4      | Name_0          | string | [Name_Lang_enUS](auctionhouse_dbc#namelang)         |         |
| 5      | Name_1          | string | [Name_Lang_enGB](auctionhouse_dbc#namelang)         |         |
| 6      | Name_2          | string | [Name_Lang_koKR](auctionhouse_dbc#namelang)         |         |
| 7      | Name_3          | string | [Name_Lang_frFR](auctionhouse_dbc#namelang)         |         |
| 8      | Name_4          | string | [Name_Lang_deDE](auctionhouse_dbc#namelang)         |         |
| 9      | Name_5          | string | [Name_Lang_enCN](auctionhouse_dbc#namelang)         |         |
| 10     | Name_6          | string | [Name_Lang_zhCN](auctionhouse_dbc#namelang)         |         |
| 11     | Name_7          | string | [Name_Lang_enTW](auctionhouse_dbc#namelang)         |         |
| 12     | Name_8          | string | [Name_Lang_zhTW](auctionhouse_dbc#namelang)         |         |
| 13     | Name_9          | string | [Name_Lang_esES](auctionhouse_dbc#namelang)         |         |
| 14     | Name_10         | string | [Name_Lang_esMX](auctionhouse_dbc#namelang)         |         |
| 15     | Name_11         | string | [Name_Lang_ruRU](auctionhouse_dbc#namelang)         |         |
| 16     | Name_12         | string | [Name_Lang_ptPT](auctionhouse_dbc#namelang)         |         |
| 17     | Name_13         | string | [Name_Lang_ptBR](auctionhouse_dbc#namelang)         |         |
| 18     | Name_14         | string | [Name_Lang_itIT](auctionhouse_dbc#namelang)         |         |
| 19     | Name_15         | string | [Name_Lang_Unk](auctionhouse_dbc#namelang)          |         |
| 20     | Name_lang_mask  | uint32 | [Name_Lang_Mask](auctionhouse_dbc#namelang)         |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/AuctionHouse).
