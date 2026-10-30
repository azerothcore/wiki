# GemProperties.dbc

[`Back-to:DBC`](dbc-index)

**The \`GemProperties.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [gemproperties_dbc](gemproperties_dbc) table of the world database.

**Structure**

| Column | Field        | Type   | gemproperties\_dbc column                       | Comment                                                                                                         |
| :----: | :----------- | :----- | :---------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| 0      | ID           | uint32 | [ID](gemproperties_dbc#id)                      |                                                                                                                 |
| 1      | EnchantID    | uint32 | [Enchant_Id](gemproperties_dbc#enchantid)       | ID in [SpellItemEnchantment.dbc](dbc-spellitemenchantment) (2 of the 615 values used here are not in that file) |
| 2      | MaxCountInv  | uint32 | [Maxcount_Inv](gemproperties_dbc#maxcountinv)   |                                                                                                                 |
| 3      | MaxCountItem | uint32 | [Maxcount_Item](gemproperties_dbc#maxcountitem) |                                                                                                                 |
| 4      | Type         | uint32 | [Type](gemproperties_dbc#type)                  |                                                                                                                 |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/GemProperties).
