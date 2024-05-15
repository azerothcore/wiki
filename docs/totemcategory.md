---
redirect_from: "/TotemCategory"
---

# TotemCategory

[`Back-to:DBC`](dbc-index.md)

**TotemCategory.dbc**

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## Structure

| Column | Field        | Type         | Notes                                                                    |
|--------|--------------|--------------|--------------------------------------------------------------------------|
| 1      | ID           | Integer      |                                                                          |
| 2-18   | sRefName     | String + Loc | Includes all kinds of component things.. not just totems                 |
| 19     | Category     | Integer      | Which category the tool belongs to (1 = totems, 3 = enchanting rods etc) |
| 20     | CategoryBits | BitMask      | Which tools in the category the tool can be used as.                     |

### For instance for totems:

| Bit | Description |
|-----|-------------|
| 0   | earth       |
| 1   | air         |
| 2   | fire        |
| 3   | water       |

Master Totem has the bitmask 1111b, meaning it can be used instead of all four normal totems.

## **Content**

| ID  | Name                     |
|-----|--------------------------|
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
