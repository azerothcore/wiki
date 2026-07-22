# areatrigger\_tavern

[<-Back-to:World](database-world)

**The \`areatrigger\_tavern\` table**

Enable a trigger when player enters a city or tavern. This causes the player to enter a resting state.

**Table Structure**

| Field     | Type      | Attributes | Key | Null | Default | Extra | Comment    |
| --------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [id][1]   | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier |
| [name][2] | text      |            |     | YES  |         |       |            |
| [faction][3] | INT    | UNSIGNED   |     | NO   | 0       |       |            |

[1]: #id
[2]: #name
[3]: #faction

**Description of the fields**

### id

This is the trigger identifier, see [AreaTrigger.dbc](DBC-AreaTrigger)

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
