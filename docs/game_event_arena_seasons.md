# game\_event\_arena\_seasons

[<-Back-to:World](database-world)

**The \`game\_event\_arena\_seasons\` table**

This information comes from sniffs and is NOT supposed to be changed.

**Table: game\_event\_arena\_seasons's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment                 |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------- |
| [eventEntry](#evententry) | TINYINT | UNSIGNED | NO   |     |         |       | Entry of the game event |
| [season](#season)         | TINYINT | UNSIGNED | NO   | MUL |         |       | Arena season number     |

**Description of the table's fields**

### eventEntry

[game_event.eventEntry](game_event#evententry)

### season

Arena season number: 1 - 9

| eventEntry | season | Comment (not part of the DB)             |
| ---------- | ------ | :--------------------------------------- |
| 75         | 1      | TBC - Season 1: "Gladiator"              |
| 76         | 2      | TBC - Season 2: "Merciless Gladiator"    |
| 55         | 3      | TBC - Season 3: "Vengeful Gladiator"     |
| 56         | 4      | TBC - Season 4: "Brutal Gladiator"       |
| 57         | 5      | WotLK - Season 5: "Deadly Gladiator"     |
| 58         | 6      | WotLK - Season 6: "Furious Gladiator"    |
| 59         | 7      | WotLK - Season 7: "Relentless Gladiator" |
| 60         | 8      | WotLK - Season 8: "Wrathful Gladiator"   |
| 31         | 9      | Arena Tournament: (Do not use)           |
