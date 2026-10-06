# character\_equipmentsets

[<-Back-to:Characters](database-characters)

**The \`character\_equipmentsets\` table**

This table holds info about player's equipment manager settings.

**Table: character\_equipmentsets's Structure**

| Field                      | Type         |          | Null | Key | Default | Extra          | Comment |
| :------------------------- | :----------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [guid](#guid)              | INT          |          | NO   | MUL | 0       |                |         |
| [setguid](#setguid)        | BIGINT       |          | NO   | PRI |         | AUTO_INCREMENT |         |
| [setindex](#setindex)      | TINYINT      | UNSIGNED | NO   | MUL | 0       |                |         |
| [name](#name)              | VARCHAR(31)  |          | NO   |     |         |                |         |
| [iconname](#iconname)      | VARCHAR(100) |          | NO   |     |         |                |         |
| [ignore_mask](#ignoremask) | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item0](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item1](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item2](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item3](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item4](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item5](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item6](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item7](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item8](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item9](#item)             | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item10](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item11](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item12](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item13](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item14](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item15](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item16](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item17](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |
| [item18](#item)            | INT          | UNSIGNED | NO   |     | 0       |                |         |

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
