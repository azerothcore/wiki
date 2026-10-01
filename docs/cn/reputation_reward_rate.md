# reputation\_reward\_rate

[<-返回至:World](database-world)

**`reputation\_reward\_rate` 表**

保存特定阵营的声望倍率。

**表结构**

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
[2]: #questrate
[3]: #creaturerate
[4]: #spellrate
[5]: #questdailyrate
[6]: #questweeklyrate
[7]: #questmonthlyrate
[8]: #questrepeatablerate

**字段说明**

### faction

这些倍率所适用的阵营的 ID。

### quest\_rate

从任务（quest）中获得声望的倍率。

### quest\_daily\_rate

从日常任务（daily quest）中获得声望的倍率。

### quest\_weekly\_rate

从每周任务（weekly quest）中获得声望的倍率。

### quest\_monthly\_rate

从每月任务（monthly quest）中获得声望的倍率。

### quest\_repeatable\_rate

从可重复任务（repeatable quest）中获得声望的倍率。

### creature\_rate

从生物（creature）获得声望的倍率。

### spell\_rate

从法术（spell）获得声望的倍率。
