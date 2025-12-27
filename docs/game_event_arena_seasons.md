# game_event_arena_seasons

[<-Back-to:World](database-world)

**The \`game_event_arena_seasons\` table**

This information comes from sniffs and is NOT supposed to be changed.

**Table Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra  | Comment                  |
| --------------- | ------- | ---------- | --- | ---- | ------- | ------ | ------------------------ |
| [eventEntry][1] | TINYINT | UNSIGNED   |     | NO   |         | Unique | Entry of the game event. |
| [season][2]     | TINYINT | UNSIGNED   |     | NO   |         | Unique | Arena season number      |

[1]: #evententry
[2]: #season

**Description of the fields**

### eventEntry

[game_event.eventEntry](game_event#eventEntry)

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
