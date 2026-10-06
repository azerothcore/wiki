# Item.dbc

[`Back-to:DBC`](dbc-index)

**The \`Item.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [item_dbc](item_dbc) table of the world database.

**Structure**

| Column | Field                   | Type   | item\_dbc column                                              | Comment                                          |
| :----: | :---------------------- | :----- | :------------------------------------------------------------ | :----------------------------------------------- |
| 0      | ID                      | uint32 | [ID](item_dbc#id)                                             |                                                  |
| 1      | ClassID                 | uint32 | [ClassID](item_dbc#classid)                                   | ID in [ItemClass.dbc](dbc-itemclass)             |
| 2      | SubclassID              | uint32 | [SubclassID](item_dbc#subclassid)                             |                                                  |
| 3      | SoundOverrideSubclassID | int32  | [Sound_Override_Subclassid](item_dbc#soundoverridesubclassid) |                                                  |
| 4      | Material                | int32  | [Material](item_dbc#material)                                 | ID in [Material.dbc](dbc-material)               |
| 5      | DisplayInfoID           | uint32 | [DisplayInfoID](item_dbc#displayinfoid)                       | ID in [ItemDisplayInfo.dbc](dbc-itemdisplayinfo) |
| 6      | InventoryType           | uint32 | [InventoryType](item_dbc#inventorytype)                       |                                                  |
| 7      | SheatheType             | uint32 | [SheatheType](item_dbc#sheathetype)                           |                                                  |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Item).
