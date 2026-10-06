# BankBagSlotPrices.dbc

[`Back-to:DBC`](dbc-index)

**The \`BankBagSlotPrices.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [bankbagslotprices_dbc](bankbagslotprices_dbc) table of the world database.

**Structure**

| Column | Field | Type   | bankbagslotprices\_dbc column      | Comment |
| :----: | :---- | :----- | :--------------------------------- | :------ |
| 0      | ID    | uint32 | [ID](bankbagslotprices_dbc#id)     |         |
| 1      | Cost  | uint32 | [Cost](bankbagslotprices_dbc#cost) |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/BankBagSlotPrices).
