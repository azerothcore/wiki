# reputation\_reward\_rate

[<-Back-to:World](database-world)

**The \`reputation\_reward\_rate\` table**

Holds reputation multipliers for specific factions.

**Table Structure**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [faction][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [quest_rate][2]    | FLOAT     | SIGNED     |     | NO   | 1       |       |         |
| [quest_daily_rate][5] | FLOAT  | SIGNED     |     | NO   | 1       |       |         |
| [quest_weekly_rate][6] | FLOAT | SIGNED     |     | NO   | 1       |       |         |
| [quest_monthly_rate][7] | FLOAT | SIGNED    |     | NO   | 1       |       |         |
| [quest_repeatable_rate][8] | FLOAT | SIGNED |     | NO   | 1       |       |         |
| [creature_rate][3] | FLOAT     | SIGNED     |     | NO   | 1       |       |         |
| [spell_rate][4]    | FLOAT     | SIGNED     |     | NO   | 1       |       |         |

[1]: #faction
[2]: #quest_rate
[3]: #creature_rate
[4]: #spell_rate
[5]: #quest_daily_rate
[6]: #quest_weekly_rate
[7]: #quest_monthly_rate
[8]: #quest_repeatable_rate

**Description of the fields**

### faction

The ID of the faction these rates apply to.

### quest\_rate

The rate for reputation gain from quests.

### quest\_daily\_rate

The rate for reputation gain from daily quests.

### quest\_weekly\_rate

The rate for reputation gain from weekly quests.

### quest\_monthly\_rate

The rate for reputation gain from monthly quests.

### quest\_repeatable\_rate

The rate for reputation gain from repeatable quests.

### creature\_rate

The rate for reputation gain from creatures.

### spell\_rate

The rate for reputation gain from spells.
