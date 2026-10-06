# AuctionHouse.dbc

[`Back-to:DBC`](dbc-index)

**The \`AuctionHouse.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [auctionhouse_dbc](auctionhouse_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | auctionhouse\_dbc column                            | Comment                                         |
| :----: | :-------------- | :----- | :-------------------------------------------------- | :---------------------------------------------- |
| 0      | ID              | uint32 | [ID](auctionhouse_dbc#id)                           |                                                 |
| 1      | FactionID       | uint32 | [FactionID](auctionhouse_dbc#factionid)             | ID in [Faction.dbc](faction)                    |
| 2      | DepositRate     | uint32 | [DepositRate](auctionhouse_dbc#depositrate)         |                                                 |
| 3      | ConsignmentRate | uint32 | [ConsignmentRate](auctionhouse_dbc#consignmentrate) |                                                 |
| 4      | Name_0          | string | [Name_Lang_enUS](auctionhouse_dbc#namelang)         | Assumed enUS                                    |
| 5      | Name_1          | string | [Name_Lang_enGB](auctionhouse_dbc#namelang)         | Assumed enGB, not used in 3.3.5a                |
| 6      | Name_2          | string | [Name_Lang_koKR](auctionhouse_dbc#namelang)         | Assumed koKR                                    |
| 7      | Name_3          | string | [Name_Lang_frFR](auctionhouse_dbc#namelang)         | Assumed frFR                                    |
| 8      | Name_4          | string | [Name_Lang_deDE](auctionhouse_dbc#namelang)         | Assumed deDE                                    |
| 9      | Name_5          | string | [Name_Lang_enCN](auctionhouse_dbc#namelang)         | Assumed enCN, not used in 3.3.5a                |
| 10     | Name_6          | string | [Name_Lang_zhCN](auctionhouse_dbc#namelang)         | Assumed zhCN                                    |
| 11     | Name_7          | string | [Name_Lang_enTW](auctionhouse_dbc#namelang)         | Assumed enTW, not used in 3.3.5a                |
| 12     | Name_8          | string | [Name_Lang_zhTW](auctionhouse_dbc#namelang)         | Assumed zhTW                                    |
| 13     | Name_9          | string | [Name_Lang_esES](auctionhouse_dbc#namelang)         | Assumed esES                                    |
| 14     | Name_10         | string | [Name_Lang_esMX](auctionhouse_dbc#namelang)         | Assumed esMX                                    |
| 15     | Name_11         | string | [Name_Lang_ruRU](auctionhouse_dbc#namelang)         | Assumed ruRU                                    |
| 16     | Name_12         | string | [Name_Lang_ptPT](auctionhouse_dbc#namelang)         | Assumed ptPT, not used in 3.3.5a                |
| 17     | Name_13         | string | [Name_Lang_ptBR](auctionhouse_dbc#namelang)         | Assumed ptBR, not used in 3.3.5a                |
| 18     | Name_14         | string | [Name_Lang_itIT](auctionhouse_dbc#namelang)         | Assumed itIT, not used in 3.3.5a                |
| 19     | Name_15         | string | [Name_Lang_Unk](auctionhouse_dbc#namelang)          | Unknown language, unsure of the usage in 3.3.5a |
| 20     | Name_lang_mask  | uint32 | [Name_Lang_Mask](auctionhouse_dbc#namelang)         | Assumed flags of the localized text             |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/AuctionHouse).
