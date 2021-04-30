# character\_equipmentsets

[<-Back-to:Characters](database-characters.md)

**The \`character\_equipmentsets\` table**

This table holds info about player's equipment manager settings.

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra          | Comment |
|------------------|--------------|------------|-----|------|---------|----------------|---------|
| [guid][1]        | INT      | SIGNED     |     | NO   |         |                |         |
| [setguid][2]     | BIGINT   | SIGNED     | PRI | NO   |         | Auto Increment |         |
| [setindex][3]    | TINYINT   | SIGNED     |     | NO   |         |                |         |
| [name][4]        | VARCHAR(31)  |            |     | NO   |         |                |         |
| [iconname][5]    | VARCHAR(100) |            |     | NO   |         |                |         |
| [ignore_mask][6] | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item0][7]       | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item1][8]       | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item2][9]       | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item3][10]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item4][11]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item5][12]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item6][13]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item7][14]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item8][15]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item9][16]      | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item10][17]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item11][18]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item12][19]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item13][20]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item14][21]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item15][22]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item16][23]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item17][24]     | INT      | UNSIGNED   |     | NO   |         |                |         |
| [item18][25]     | INT      | UNSIGNED   |     | NO   |         |                |         |

[1]: #guid
[2]: #setguid
[3]: #setindex
[4]: #name
[5]: #iconname
[6]: #ignore_mask
[7]: #item0
[8]: #item1
[9]: #item2
[10]: #item3
[11]: #item4
[12]: #item5
[13]: #item6
[14]: #item7
[15]: #item8
[16]: #item9
[17]: #item10
[18]: #item11
[19]: #item12
[20]: #item13
[21]: #item14
[22]: #item15
[23]: #item16
[24]: #item17
[25]: #item18

**Description of the fields**

### guid

Player's GUID. See characters.guid

### setguid

First free guid.

### setindex

Set index, values from 0 to 9 are used.

### name

Individual. Name is set by player.

### iconname

Name taken from ItemDisplayInfo.dbc, column 6

### ignore\_mask

`field-no-description|6`

### item0-18

Values taken from item\_instance.guid

| ID | Name      |
|----|-----------|
| 0  | Head      |
| 1  | Neck      |
| 2  | Shoulder  |
| 3  | Shirt     |
| 4  | Chest     |
| 5  | Waist     |
| 6  | Legs      |
| 7  | Feet      |
| 8  | Wrist     |
| 9  | Hands     |
| 10 | Ring 1    |
| 11 | Ring 2    |
| 12 | Trinket 1 |
| 13 | Trinket 2 |
| 14 | Back      |
| 15 | Main Hand |
| 16 | Off Hand  |
| 17 | Relic     |
| 18 | Tabard    |
