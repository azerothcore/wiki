---
redirect_from: "/cn/TotemCategory"
---

# TotemCategory

[`返回:DBC`](dbc-index)

**TotemCategory.dbc**

**版本：3.3.5a**

[如何将 DBC 数据导入我的数据库](how-to-import-dbc-data-in-db)  

## 结构

| Column | Field        | Type         | Notes                                                                    |
| ------ | ------------ | ------------ | ------------------------------------------------------------------------ |
| 1      | ID           | Integer      |                                                                          |
| 2-18   | sRefName     | String + Loc | 包含各种组件类的东西……不只是图腾                                  |
| 19     | Category     | Integer      | 工具属于哪个类别（1 = 图腾，3 = 附魔棒等）                         |
| 20     | CategoryBits | BitMask      | 该工具在所属类别中可以作为哪些工具使用。                                     |

### 例如对于图腾：

| Bit | Description |
| --- | ----------- |
| 0   | earth       |
| 1   | air         |
| 2   | fire        |
| 3   | water       |

大地图腾（Master Totem）的位掩码为 1111b，意味着它可以代替全部四种普通图腾使用。

## **内容**

| ID  | Name                     |
| --- | ------------------------ |
| 1   | Skinning Knife (OLD)     |
| 2   | Earth Totem              |
| 3   | Air Totem                |
| 4   | Fire Totem               |
| 5   | Water Totem              |
| 6   | Runed Copper Rod         |
| 7   | Runed Silver Rod         |
| 8   | Runed Golden Rod         |
| 9   | Runed Truesilver Rod     |
| 10  | Runed Arcanite Rod       |
| 11  | Mining Pick (OLD)        |
| 12  | Philosopher's Stone      |
| 13  | Blacksmith Hammer (OLD)  |
| 14  | Arclight Spanner         |
| 15  | Gyromatic Micro-Adjustor |
| 21  | Master Totem             |
| 41  | Runed Fel Iron Rod       |
| 62  | Runed Adamantite Rod     |
| 63  | Runed Eternium Rod       |
| 81  | Hollow Quill             |
| 101 | Runed Azurite Rod        |
| 121 | Virtuoso Inking Set      |
| 141 | Drums                    |
| 161 | Gnomish Army Knife       |
| 162 | Blacksmith Hammer        |
| 165 | Mining Pick              |
| 166 | Skinning Knife           |
| 167 | Hammer Pick              |
| 168 | Bladed Pickaxe           |
| 169 | Flint and Tinder         |
| 189 | Runed Cobalt Rod         |
| 190 | Runed Titanium Rod       |
