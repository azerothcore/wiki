# character\_reputation

[<-Back-to:Characters](database-characters)

**The \`character\_reputation\` table**

This table holds the reputation information for each character.

**Table Structure**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]     | INT         | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [faction][2]  | SMALLINT    | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [standing][3] | INT         | SIGNED     |     | NO   | 0       |       |                          |
| [flags][4]    | SMALLINT    | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #faction
[3]: #standing
[4]: #flags

**Description of the fields**

### guid

The character guid. See [characters.guid](characters#guid).

### faction

The faction ID that the character has the given reputation in. See [Faction.dbc](faction).

### standing

The current reputation value that the character has.

### flags

This field is a bitmask containing flags that apply to the faction and how it's displayed to the character. Just like any flag field, you can combine flags by adding them together. If this field is 0, then it is not shown in the reputation list in-game.

| Flag | Name                          | Comments                                                                 |
|----- | ----------------------------- | ------------------------------------------------------------------------ |
| 1    | FACTION_FLAG_VISIBLE          | Displayed in the reputation tab                                          |
| 2    | FACTION_FLAG_AT_WAR           | Active when the player sets the at war checkbox                          |
| 4    | FACTION_FLAG_HIDDEN           | Hidden faction from reputation pane in client                            |
| 8    | FACTION_FLAG_INVISIBLE_FORCED | Always overwrites FACTION_FLAG_VISIBLE and hide faction in rep.list      |
| 16   | FACTION_FLAG_PEACE_FORCED     | Always overwrites FACTION_FLAG_AT_WAR                                    |
| 32   | FACTION_FLAG_INACTIVE         |                                                                          |
| 64   | FACTION_FLAG_RIVAL            | Flag for the two competing outland factions                              |
| 128  | FACTION_FLAG_SPECIAL          | Horde and alliance home cities and their northrend allies have this flag |
