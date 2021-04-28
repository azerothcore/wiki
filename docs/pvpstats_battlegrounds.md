# pvpstats\_battlegrounds

[<-Back-to:Characters](database-characters.md)

**The \`[pvpstats\_battlegrounds](http://collab.kpsn.org/pages/createpage.action?spaceKey=tc&title=pvpstats_battlegrounds&linkCreation=true&fromPageId=331580)\` table**

This table holds datas about BattleGrounds scores. To enable storing this kind of informations, set **Battleground . StoreStatistics . Enable   =   1** in **worldserver.config** file.

**Structure**

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment |
|---------------------|----------|------------|-----|------|---------|-------|---------|
| [id][1]             | BIGINT   | unsigned   | PRI | NO   |         |       |         |
| [winner_faction][2] | TINYINT  |            |     | NO   |         |       |         |
| [bracket_id][3]     | TINYINT  | unsigned   |     | NO   |         |       |         |
| [type][4]           | TINYINT  | unsigned   |     | NO   |         |       |         |
| [date][5]           | datetime |            |     | NO   |         |       |         |

[1]: #id
[2]: #winner_faction
[3]: #bracket_id
[4]: #type
[5]: #date

**Description of the fields**

### id

An unique value which identifies a BattleGround.

### winner\_faction

The faction which won the BattleGround:

| Value | Description |
|-------|-------------|
| 0     | HORDE       |
| 1     | ALLIANCE    |
| 2     | NONE        |

### bracket\_id

Identifies the bracket level range:

| Value | Level range |
|-------|-------------|
| 1     | 10-19       |
| 2     | 20-29       |
| 3     | 30-39       |
| 4     | 40-49       |
| 5     | 50-59       |
| 6     | 60-69       |
| 7     | 70-79       |
| 8     | 80          |

### type

The BattleGround type:

| Value | Description            |
|-------|------------------------|
| 1     | Alterac Valley         |
| 2     | Warsong Gulch          |
| 3     | Arathi Basin           |
| 7     | Eye of the Storm       |
| 9     | Strand of the Ancients |
| 30    | Isle of Conquest       |

### date

Date and time of BattleGround ending.
