# access\_requirement

[<-Back-to:World](database-world.md)

**The \`access\_requirement\` table**

This table contains the access requirements to enter an instance.
**Note:** If you reload this table with `.reload access_r`, you will have to close and reopen the ingame Dungeon Finder/Raid Browser to update its status.

**Structure**

| Field                       | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-----------------------------|--------------|------------|-----|------|---------|-------|---------|
| [mapId][1]                  | MEDIUMINT(8) | unsigned   | PRI | NO   |         |       |         |
| [difficulty][2]             | tinyint(3)   | unsigned   | PRI | NO   | 0       |       |         |
| [level_min][3]              | tinyint(3)   | unsigned   |     | NO   | 0       |       |         |
| [level_max][4]              | tinyint(3)   | unsigned   |     | NO   | 0       |       |         |
| [item_level][5]             | smallint(5)  | unsigned   |     | NO   | 0       |       |         |
| [item][6]                   | MEDIUMINT(8) | unsigned   |     | NO   | 0       |       |         |
| [item2][7]                  | MEDIUMINT(8) | unsigned   |     | NO   | 0       |       |         |
| [quest_done_A][8]           | MEDIUMINT(8) | unsigned   |     | NO   | 0       |       |         |
| [quest_done_H][9]           | MEDIUMINT(8) | unsigned   |     | NO   | 0       |       |         |
| [completed_achievement][10] | MEDIUMINT(8) | unsigned   |     | NO   | 0       |       |         |
| [quest_failed_text][11]     | text         |            |     | YES  |         |       |         |
| [comment][12]               | text         |            |     | YES  |         |       |         |

[1]: #mapid
[2]: #difficulty
[3]: #level_min
[4]: #level_max
[5]: #item_level
[6]: #item
[7]: #item2
[8]: #quest_done_a
[9]: #quest_done_h
[10]: #completed_achievement
[11]: #quest_failed_text
[12]: #comment

**Description of the fields**

### mapId

This is the [access\_id](instance_template) field from the [instance\_template](instance_template) table. It is an arbitrary number that merely links the requirements to an [instance\_template](instance_template), or [areatrigger\_teleport](areatrigger_teleport)

### difficulty

- 5 man dungeons - 0 for normal, 1 for heroic, 2 for epic (not used yet)
- 10 man dungeons - 0 for normal, 2 for heroic
- 25 man dungeons - 1 for normal, 3 for heroic

### level\_min

The minimum level that you must be in order to enter the instance.

### level\_max

The maximum level that you can be in order to enter the instance.

### item\_level

The at least required item level for an instance.

-   All WotLK Heroics require at least an average item level of 180.
-   Trial of the Champion, Pit of Saron, and the Forge of Souls require an average item level of 200.
-   Halls of Reflection requires an average item level of 219.

**Note:** this requirement only applies to the Dungeon Finder and the Raid Browser, not to a dungeon/raid portal (and it's blizzlike). This also means a guild could try to clear a raid while being undergeared :)

### item

A horde only [item](item_template) that you must have in your inventory to enter the instance. This item can not be in the bank.

### item2

An alliance only [item](item_template) that you must have in your inventory. This item can not be in the bank.

### quest\_done\_A

A [quest](quest_template) that you must have completed. This field is only for alliance.

### quest\_done\_H

A [quest](quest_template) that you must have completed. This field is only for horde.

### completed\_achievement

An [achievement](Achievement) that must be completed by the player to enter an instance.

### quest\_failed\_text

The text that is shown if you try and enter the instance without having completed the quest.

### comment

This field is for any comment you want to make about the requirements or the instance. It is arbitrary text.

### Example

| mapId | difficulty | level_min | level_max | comment                      |
|-------|------------|-----------|-----------|------------------------------|
| 33    | 0          | 14        | 0         | Shadowfang Keep Entrance     |
| 34    | 0          | 15        | 0         | Stormwind Stockades Entrance |

**Note:** The table, has more attributes, but as an example, it was not necessary to show them all, because most did not have values and thus, avoid the table is very extensive. The executed SQL query is the following:

```sql
SELECT `mapId`, `difficulty`, `level_min`, `level_max`, `comment` FROM `access_requirement` LIMIT 2;
```
