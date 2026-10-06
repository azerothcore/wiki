# player\_xp\_for\_level

[<-Back-to:World](database-world)

**The \`player\_xp\_for\_level\` table**

Includes information on how much experience needed for next level. Comes from sniffs.

**Table: player\_xp\_for\_level's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [Level](#level)           | TINYINT | UNSIGNED | NO   | PRI |         |       |         |
| [Experience](#experience) | INT     | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

This table sets the exp point needed to upgrade the player's level.

### Level

The player's level.

### Experience

The experience needed to upgrade from the value in "lvl" field to "lvl" +1.

### Example

| Level | Experience |
| ----- | ---------- |
| 1     | 400        |
| 2     | 900        |
| 3     | 1400       |
| 4     | 2100       |
| 5     | 2800       |
