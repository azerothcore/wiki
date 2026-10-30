# reputation\_reward\_rate

[<-Back-to:World](database-world)

**The \`reputation\_reward\_rate\` table**

Holds reputation multipliers for specific factions.

**Table: reputation\_reward\_rate's Structure**

| Field                                         | Type  |          | Null | Key | Default | Extra | Comment |
| :-------------------------------------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [faction](#faction)                           | INT   | UNSIGNED | NO   | PRI | 0       |       |         |
| [quest_rate](#questrate)                      | FLOAT |          | NO   |     | 1       |       |         |
| [quest_daily_rate](#questdailyrate)           | FLOAT |          | NO   |     | 1       |       |         |
| [quest_weekly_rate](#questweeklyrate)         | FLOAT |          | NO   |     | 1       |       |         |
| [quest_monthly_rate](#questmonthlyrate)       | FLOAT |          | NO   |     | 1       |       |         |
| [quest_repeatable_rate](#questrepeatablerate) | FLOAT |          | NO   |     | 1       |       |         |
| [creature_rate](#creaturerate)                | FLOAT |          | NO   |     | 1       |       |         |
| [spell_rate](#spellrate)                      | FLOAT |          | NO   |     | 1       |       |         |

**Description of the table's fields**

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
