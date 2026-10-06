# areatrigger\_tavern

[<-Back-to:World](database-world)

**The \`areatrigger\_tavern\` table**

Enable a trigger when player enters a city or tavern. This causes the player to enter a resting state.

**Table: areatrigger\_tavern's Structure**

| Field               | Type |          | Null | Key | Default | Extra | Comment    |
| :------------------ | :--- | :------- | :--: | :-: | :-----: | :---: | :--------- |
| [id](#id)           | INT  | UNSIGNED | NO   | PRI | 0       |       | Identifier |
| [name](#name)       | TEXT |          | YES  |     | NULL    |       |            |
| [faction](#faction) | INT  | UNSIGNED | NO   |     | 0       |       |            |

**Description of the table's fields**

### id

This is the trigger identifier, see [AreaTrigger.dbc](dbc-areatrigger)

### name

Name of the city or tavern. This is purely for descriptive purposes.

### faction

Faction required for the resting trigger to apply. `0` means no faction restriction.

### Example

| id  | name                                         |
| --- | -------------------------------------------- |
| 71  | Westfall - Sentinel Hill Inn                 |
| 98  | Nesingwary's Expedition                      |
| 178 | Strahnbrad                                   |
| 562 | Elwynn Forest - Goldshire - Lion's Pride Inn |
| 682 | Redridge Mountains - Lakeshire Inn           |
