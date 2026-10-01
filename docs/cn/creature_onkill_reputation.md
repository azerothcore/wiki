# creature\_onkill\_reputation

[<-返回：世界](database-world)

**\`creature\_onkill\_reputation\` 表**

该表控制生物被其他玩家击杀时给予的声望。

**表结构**

| Field                     | Type      | Attributes | Key | Null | Default | Extra | Comment             |
| ------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------- |
| [creature_id][1]          | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | 生物标识符          |
| [RewOnKillRepFaction1][2] | SMALLINT  | SIGNED     |     | NO   | 0       |       |                     |
| [RewOnKillRepFaction2][3] | SMALLINT  | SIGNED     |     | NO   | 0       |       |                     |
| [MaxStanding1][4]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [IsTeamAward1][5]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [RewOnKillRepValue1][6]   | MEDIUMINT | SIGNED     |     | NO   | 0       |       |                     |
| [MaxStanding2][7]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [IsTeamAward2][8]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [RewOnKillRepValue2][9]   | MEDIUMINT | SIGNED     |     | NO   | 0       |       |                     |
| [TeamDependent][10]       | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                     |

[1]: #creatureid
[2]: #rewonkillrepfaction1
[3]: #rewonkillrepfaction2
[4]: #maxstanding1
[5]: #isteamaward1
[6]: #rewonkillrepvalue1
[7]: #maxstanding2
[8]: #isteamaward2
[9]: #rewonkillrepvalue2
[10]: #teamdependent

**字段说明**

### creature\_id

生物模板 ID。参见 [creature\_template.entry](creature_template#entry)

### RewOnKillRepFaction

玩家将在其中获得或失去声望的阵营 ID。参见 Faction.dbc

### MaxStanding

生物将持续授予声望直到该最高声望等级。如果玩家达到该声望等级或任何更高等级，生物将不再授予任何声望。

| ID  | 等级       |
| --- | ---------- |
| 0   | 仇恨      |
| 1   | 敌对    |
| 2   | 不和 |
| 3   | 中立    |
| 4   | 友好   |
| 5   | 尊敬    |
| 6   | 崇敬    |
| 7   | 崇拜    |

### IsTeamAward

布尔值 0 或 1，控制玩家是否不仅获得该阵营的声望，还获得该阵营所属阵营团队的声望。

-   0：玩家仅获得该阵营的声望
-   1：玩家同时获得该阵营及其所属阵营团队的声望

注意：玩家为团队获得的声望值（如果该字段为 1）是 [RewOnKillRepValue](#rewonkillrepvalue) 中指定值的一半

### RewOnKillRepValue

玩家通过击杀该生物获得的声望值（若为负数则为失去的声望值）。

### TeamDependent

布尔值 0 或 1。

-   0：如果两个字段（RewOnKillRepFaction1 和 RewOnKillRepFaction2）都非零，生物将向任何玩家授予两个字段的声望。
-   1：生物将向联盟玩家授予 RewOnKillRepFaction1 的声望，向部落玩家授予 RewOnKillRepFaction2 的声望
