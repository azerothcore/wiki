# dungeon\_access\_template

[<-Back-to:World](database-world)

**The \`dungeon\_access\_template\` table**

Holds the dungeons and difficulties that have entry limits, with their level and item level limits. The detailed requirements are in [dungeon_access_requirements](dungeon_access_requirements).

**Table: dungeon\_access\_template's Structure**

| Field                                  | Type         |          | Null | Key | Default | Extra          | Comment                                                                                                                       |
| :------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :------------: | :---------------------------------------------------------------------------------------------------------------------------- |
| [id](#id)                              | TINYINT      | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT | The dungeon template ID                                                                                                       |
| [map_id](#mapid)                       | INT          | UNSIGNED | YES  | MUL | NULL    |                | Map ID from instance_template                                                                                                 |
| [difficulty](#difficulty)              | TINYINT      | UNSIGNED | NO   |     | 0       |                | 5 man: 0 = normal, 1 = heroic, 2 = epic (not implemented) \| 10 man: 0 = normal, 2 = heroic \| 25 man: 1 = normal, 3 = heroic |
| [min_level](#minlevel)                 | TINYINT      | UNSIGNED | YES  |     | NULL    |                |                                                                                                                               |
| [max_level](#maxlevel)                 | TINYINT      | UNSIGNED | YES  |     | NULL    |                |                                                                                                                               |
| [min_avg_item_level](#minavgitemlevel) | SMALLINT     | UNSIGNED | YES  |     | NULL    |                | Min average ilvl required to enter                                                                                            |
| [comment](#comment)                    | VARCHAR(255) |          | YES  |     | NULL    |                | Dungeon Name 5/10/25/40 man - Normal/Heroic                                                                                   |

**Description of the table's fields**

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

A description of the row. Not used by the core.
