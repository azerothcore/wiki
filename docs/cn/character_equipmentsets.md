# character\_equipmentsets

[<-返回:Characters](database-characters)

**\`character\_equipmentsets\` 表**

该表保存了玩家的装备管理器（equipment manager）设置信息。

**表结构**

| Field            | Type         | Attributes | Key | Null | Default | Extra  | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ------ | ------- |
| [guid][1]        | INT          | SIGNED     |     | NO   |         | UNIQUE |         |
| [setguid][2]     | BIGINT       | SIGNED     | PRI | NO   |         | UNIQUE |         |
| [setindex][3]    | TINYINT      | UNSIGNED   |     | NO   |         | UNIQUE |         |
| [name][4]        | VARCHAR(31)  | SIGNED     |     | NO   |         |        |         |
| [iconname][5]    | VARCHAR(100) | SIGNED     |     | NO   |         |        |         |
| [ignore_mask][6] | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item0][7]       | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item1][8]       | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item2][9]       | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item3][10]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item4][11]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item5][12]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item6][13]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item7][14]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item8][15]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item9][16]      | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item10][17]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item11][18]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item12][19]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item13][20]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item14][21]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item15][22]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item16][23]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item17][24]     | INT          | UNSIGNED   |     | NO   |         |        |         |
| [item18][25]     | INT          | UNSIGNED   |     | NO   |         |        |         |

[1]: #guid
[2]: #setguid
[3]: #setindex
[4]: #name
[5]: #iconname
[6]: #ignoremask
[7]: #item
[8]: #item
[9]: #item
[10]: #item
[11]: #item
[12]: #item
[13]: #item
[14]: #item
[15]: #item
[16]: #item
[17]: #item
[18]: #item
[19]: #item
[20]: #item
[21]: #item
[22]: #item
[23]: #item
[24]: #item
[25]: #item

**字段说明**

### guid

玩家的 GUID。参见 [characters.guid](characters#guid)。

### setguid

第一个可用的 GUID。

### setindex

套装索引，使用 0 到 9 之间的值。

### name

自定义名称。名称由玩家设置。

### iconname

取自 ItemDisplayInfo.dbc 第 6 列的名称。

### ignore\_mask

一个位掩码，指定应用此装备套装时应被忽略（保持不变）的装备槽位索引。每个位对应一个装备槽位索引。

### item

取自 [item\_instance.guid](item_instance#guid) 的值。

| ID  | 名称      |
| --- | --------- |
| 0   | 头部      |
| 1   | 颈部      |
| 2   | 肩部      |
| 3   | 衬衣      |
| 4   | 胸甲      |
| 5   | 腰部      |
| 6   | 腿部      |
| 7   | 脚部      |
| 8   | 手腕      |
| 9   | 手部      |
| 10  | 戒指 1    |
| 11  | 戒指 2    |
| 12  | 饰品 1    |
| 13  | 饰品 2    |
| 14  | 背部      |
| 15  | 主手      |
| 16  | 副手      |
| 17  | 圣物      |
| 18  | 战袍      |
