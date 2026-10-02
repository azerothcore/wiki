# character\_equipmentsets

[<-Back-to:Characters](database-characters)

**The \`character\_equipmentsets\` table**

This table holds info about player's equipment manager settings.

**Table: character\_equipmentsets's Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra          | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [guid][1]        | INT          | SIGNED     | MUL | NO   | 0       |                |         |
| [setguid][2]     | BIGINT       | SIGNED     | PRI | NO   |         | AUTO_INCREMENT |         |
| [setindex][3]    | TINYINT      | UNSIGNED   | MUL | NO   | 0       |                |         |
| [name][4]        | VARCHAR(31)  |            |     | NO   |         |                |         |
| [iconname][5]    | VARCHAR(100) |            |     | NO   |         |                |         |
| [ignore_mask][6] | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item0][7]       | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item1][8]       | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item2][9]       | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item3][10]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item4][11]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item5][12]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item6][13]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item7][14]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item8][15]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item9][16]      | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item10][17]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item11][18]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item12][19]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item13][20]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item14][21]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item15][22]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item16][23]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item17][24]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |
| [item18][25]     | INT          | UNSIGNED   |     | NO   | 0       |                |         |

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

**Description of the table's fields**

### guid

Player's GUID. See [characters.guid](characters#guid).

### setguid

First free guid.

### setindex

Set index, values from 0 to 9 are used.

### name

Individual. Name is set by player.

### iconname

Name taken from ItemDisplayInfo.dbc, column 6.

### ignore\_mask

A bitmask of equipment slot indices that should be ignored (left unchanged) when this equipment set is applied. Each bit corresponds to an equipment slot index.

### item

Values taken from [item\_instance.guid](item_instance#guid).

| ID  | Name      |
| --- | --------- |
| 0   | Head      |
| 1   | Neck      |
| 2   | Shoulder  |
| 3   | Shirt     |
| 4   | Chest     |
| 5   | Waist     |
| 6   | Legs      |
| 7   | Feet      |
| 8   | Wrist     |
| 9   | Hands     |
| 10  | Ring 1    |
| 11  | Ring 2    |
| 12  | Trinket 1 |
| 13  | Trinket 2 |
| 14  | Back      |
| 15  | Main Hand |
| 16  | Off Hand  |
| 17  | Relic     |
| 18  | Tabard    |
