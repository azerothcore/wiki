---
redirect_from: "/cn/Languages"
---

# Languages

[`Back-to:DBC`](dbc-index)

[如何将 DBC 数据导入我的数据库](how-to-import-dbc-data-in-db)  

**DBC 结构 - 适用于版本 3.3.5a**

此 DBC 包含可用于文本中的语言。玩家必须精通该语言才能理解所写的内容。

| Column | Type  | Notes                                   |
| ------ | ----- | --------------------------------------- |
| 1      | long  | 语言的 ID。必须唯一。                   |
| 2      | str   | 语言名称写在这里。                      |
| 18     | flags | 此列的用途未知。                        |

任何未列出的列都不在 DBC 文件中使用。

**DBC 内容 - 适用于版本 3.3.5a**

*Languages.dbc* 文件中的所有种族及其 ID 如下。

| ID  | Name           |
| --- | -------------- |
| 1   | Orcish         |
| 2   | Darnassian     |
| 3   | Taurahe        |
| 6   | Dwarvish       |
| 7   | Common         |
| 8   | Demonic        |
| 9   | Titan          |
| 10  | Thalassian     |
| 11  | Draconic       |
| 12  | Kalimag        |
| 13  | Gnomish        |
| 14  | Troll          |
| 33  | Gutterspeak    |
| 35  | Draenei        |
| 36  | Zombie         |
| 37  | Gnomish Binary |
| 38  | Goblin Binary  |
