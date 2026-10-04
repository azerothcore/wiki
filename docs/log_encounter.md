# log\_encounter

[<-Back-to:Characters](database-characters)

**The \`log\_encounter\` table**

Logs completed encounters: time, map, difficulty, the credit given and the players involved.

**Table: log\_encounter's Structure**

| Field                       | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [time](#time)               | DATETIME |          | NO   |     |         |       |         |
| [map](#map)                 | SMALLINT | UNSIGNED | NO   |     |         |       |         |
| [difficulty](#difficulty)   | TINYINT  | UNSIGNED | NO   |     |         |       |         |
| [creditType](#credittype)   | TINYINT  | UNSIGNED | NO   |     |         |       |         |
| [creditEntry](#creditentry) | INT      | UNSIGNED | NO   |     |         |       |         |
| [playersInfo](#playersinfo) | TEXT     |          | NO   |     |         |       |         |

**Description of the table's fields**

### time

The date and time the boss was killed.

### map

The map of the encounter. See [Map.dbc](map).

### difficulty

The difficulty of the map.

### creditType

0 if the encounter was credited by killing a creature, 1 if it was credited by a spell.

### creditEntry

The creature entry or spell ID that credited the encounter.

### playersInfo

One line per player in the map, with the name, GUID, account, IP, guild, position and the auras on the player as `spell(effectMask)`.
