# character\_reputation

[<-Back-to:Characters](database-characters)

**The \`character\_reputation\` table**

This table holds the reputation information for each character.

**Table: character\_reputation's Structure**

| Field                 | Type     |          | Null | Key | Default | Extra | Comment                  |
| :-------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)         | INT      | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [faction](#faction)   | SMALLINT | UNSIGNED | NO   | PRI | 0       |       |                          |
| [standing](#standing) | INT      |          | NO   |     | 0       |       |                          |
| [flags](#flags)       | SMALLINT | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### faction

The faction ID that the character has the given reputation in. See [Faction.dbc](faction).

### standing

The current reputation value that the character has.

### flags

This field is a bitmask containing flags that apply to the faction and how it's displayed to the character. Just like any flag field, you can combine flags by adding them together. If this field is 0, then it is not shown in the reputation list in-game.

| Value | Hex    | Flag                          | Comment                                                                  |
| :---- | :----: | :---------------------------- | :----------------------------------------------------------------------- |
| 1     | `0x01` | FACTION_FLAG_VISIBLE          | Displayed in the reputation tab                                          |
| 2     | `0x02` | FACTION_FLAG_AT_WAR           | Active when the player sets the at war checkbox                          |
| 4     | `0x04` | FACTION_FLAG_HIDDEN           | Hidden faction from reputation pane in client                            |
| 8     | `0x08` | FACTION_FLAG_INVISIBLE_FORCED | Always overwrites FACTION_FLAG_VISIBLE and hide faction in rep.list      |
| 16    | `0x10` | FACTION_FLAG_PEACE_FORCED     | Always overwrites FACTION_FLAG_AT_WAR                                    |
| 32    | `0x20` | FACTION_FLAG_INACTIVE         | The player moved the faction to the inactive list                        |
| 64    | `0x40` | FACTION_FLAG_RIVAL            | Flag for the two competing outland factions                              |
| 128   | `0x80` | FACTION_FLAG_SPECIAL          | Horde and alliance home cities and their northrend allies have this flag |
