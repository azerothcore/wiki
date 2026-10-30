# BannedAddOns.dbc

[`Back-to:DBC`](dbc-index)

**The \`BannedAddOns.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field        | Type   | Comment |
| :----: | :----------- | :----- | :------ |
| 0      | ID           | uint32 |         |
| 1      | NameMD5_0    | uint32 |         |
| 2      | NameMD5_1    | uint32 |         |
| 3      | NameMD5_2    | uint32 |         |
| 4      | NameMD5_3    | uint32 |         |
| 5      | VersionMD5_0 | uint32 |         |
| 6      | VersionMD5_1 | uint32 |         |
| 7      | VersionMD5_2 | uint32 |         |
| 8      | VersionMD5_3 | uint32 |         |
| 9      | LastModified | uint32 |         |
| 10     | Flags        | uint32 |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/BannedAddOns).
