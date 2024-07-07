# achievement\_dbc

[<-Back-to:World](database-world)

**The \`achievement\_dbc\` table**

Stores achievement data that is missing in [Achievement.dbc](Achievement)

**Table Structure**

| Field                | Type | Attributes | Key | Null | Default | Extra | Comment                                                                          |
| -------------------- | ---- | ---------- | --- | ---- | ------- | ----- | -------------------------------------------------------------------------------- |
| [ID][1]              | INT  | UNSIGNED   | PRI | NO   |         |       |                                                                                  |
| [requiredFaction][2] | INT  | SIGNED     |     | NO   | -1      |       |                                                                                  |
| [mapID][3]           | INT  | SIGNED     |     | NO   | -1      |       |                                                                                  |
| [points][4]          | INT  | UNSIGNED   |     | NO   | 0       |       | Achievement points awarded for completing the achievement, has no use serverside |
| [flags][5]           | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |
| [count][6]           | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |
| [refAchievement][7]  | INT  | UNSIGNED   |     | NO   | 0       |       |                                                                                  |

[1]: #id
[2]: #requiredfaction
[3]: #mapid
[4]: #points
[5]: #flags
[6]: #count
[7]: #refachievement

**Description of the fields**

### ID

This is the ID of the achievement from [Achievement\_Criteria.dbc](Achievement+Criteria) (2nd column)

### requiredFaction

| Condition | Faction |
| --------- | ------- |
| Both      | -1      |
| Horde     | 0       |
| Alliance  | 1       |

### mapID

Condition: Player must be on that map to be allowed criteria updates (-1 if not set)

### points

Achievement points awarded for completing the achievement, has no use serverside

### flags

| Name                               | Value      | Comment                                                                                              |
| ---------------------------------- | ---------- | ---------------------------------------------------------------------------------------------------- |
| ACHIEVEMENT_FLAG_COUNTER           | 0x00000001 | Just count statistic (never stop and complete)                                                       |
| ACHIEVEMENT_FLAG_HIDDEN            | 0x00000002 | Not sent to client - internal use only                                                               |
| ACHIEVEMENT_FLAG_STORE_MAX_VALUE   | 0x00000004 | Store only max value? used only in "Reach level xx"                                                  |
| ACHIEVEMENT_FLAG_SUMM              | 0x00000008 | Use summ criteria value from all reqirements (and calculate max value)                               |
| ACHIEVEMENT_FLAG_MAX_USED          | 0x00000010 | Show max criteria (and calculate max value ??)                                                       |
| ACHIEVEMENT_FLAG_REQ_COUNT         | 0x00000020 | Use not zero req count (and calculate max value)                                                     |
| ACHIEVEMENT_FLAG_AVERAGE           | 0x00000040 | Show as average value (value / time_in_days) depend from other flag (by def use last criteria value) |
| ACHIEVEMENT_FLAG_BAR               | 0x00000080 | Show as progress bar (value / max vale) depend from other flag (by def use last criteria value)      |
| ACHIEVEMENT_FLAG_REALM_FIRST_REACH | 0x00000100 |                                                                                                      |
| ACHIEVEMENT_FLAG_REALM_FIRST_KILL  | 0x00000200 |                                                                                                      |

### count

Should always be 1.

### refAchievement

Should always be 0.
