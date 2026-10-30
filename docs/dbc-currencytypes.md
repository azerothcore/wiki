# CurrencyTypes.dbc

[`Back-to:DBC`](dbc-index)

**The \`CurrencyTypes.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [currencytypes_dbc](currencytypes_dbc) table of the world database.

**Structure**

| Column | Field      | Type   | currencytypes\_dbc column                  | Comment                    |
| :----: | :--------- | :----- | :----------------------------------------- | :------------------------- |
| 0      | ID         | uint32 | [ID](currencytypes_dbc#id)                 |                            |
| 1      | ItemID     | uint32 | [ItemID](currencytypes_dbc#itemid)         | ID in [Item.dbc](dbc-item) |
| 2      | CategoryID | uint32 | [CategoryID](currencytypes_dbc#categoryid) |                            |
| 3      | BitIndex   | uint32 | [BitIndex](currencytypes_dbc#bitindex)     |                            |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CurrencyTypes).
