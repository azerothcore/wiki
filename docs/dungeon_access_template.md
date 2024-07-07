# dungeon\_access\_template

[<-Back-to:World](database-world)

**The \`dungeon\_access\_template\` table**

**Table Structure**

| Field                   | Type         | Attributes | Key | Null | Default        | Extra                                         | Comment |
| ----------------------- | ------------ | ---------- | --- | ---- | -------------- | --------------------------------------------- | ------- |
| [id][1]                 | TINYINT      | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |                                               |         |
| [map_id][2]             | MEDIUMINT    | UNSIGNED   | KEY | NO   |                | FK_dungeon_access_template__instance_template |         |
| [difficulty][3]         | TINYINT      | UNSIGNED   |     | NO   | 0              |                                               |         |
| [min_level][4]          | TINYINT      | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [max_level][5]          | TINYINT      | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [min_avg_item_level][6] | SMALLINT     | UNSIGNED   |     | YES  | NULL           |                                               |         |
| [comment][7]            | VARCHAR(255) |            |     | YES  | NULL           |                                               |         |

[1]: #id
[2]: #map_id
[3]: #difficulty
[4]: #min_level
[5]: #max_level
[6]: #min_avg_item_level
[7]: #comment

**Description of the fields**

### id

The dungeon template ID

### map_id

Map ID from [instance_template.map](instance_template#map).

### difficulty

- 5 man: 0 = normal, 1 = heroic, 2 = epic (Mythic, not implemented in 3.3.5) 

- 10 man: 0 = normal, 2 = heroic 

- 25 man: 1 = normal, 3 = heroic

### min_level

The minimum level you must be to enter the instance.

### max_level

The maximum level you can be to enter the instance.

### min_avg_item_level

Min average ilvl required to enter the instance.

- All WotLK Heroics require at least an average item level of 180.

- Trial of the Champion, Pit of Saron, and the Forge of Souls require an average item level of 200.

- Halls of Reflection requires an average item level of 219.

**Note:** this requirement only applies to the Dungeon Finder and the Raid Browser, not to a dungeon/raid portal (and it's blizzlike). This also means a guild could try to clear a raid while being undergeared :)

### comment
