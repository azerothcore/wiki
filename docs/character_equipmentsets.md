# character\_equipmentsets

[<-Back-to:Characters](database-characters)

**The \`character\_equipmentsets\` table**

This table holds info about player's equipment manager settings.

**Table Structure**

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

**Description of the fields**

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

`field-no-description|6`

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
