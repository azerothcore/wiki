# pvpstats\_battlegrounds

[<-Back-to:Characters](database-characters)

**The \`pvpstats\_battlegrounds\` table**

This table holds datas about BattleGrounds scores. To enable storing this kind of informations, set **Battleground.StoreStatistics.Enable = 1** in **worldserver.config.dist** file.

**Table: pvpstats\_battlegrounds's Structure**

| Field                            | Type     |          | Null | Key | Default | Extra          | Comment |
| :------------------------------- | :------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [id](#id)                        | BIGINT   | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [winner_faction](#winnerfaction) | TINYINT  |          | NO   |     |         |                |         |
| [bracket_id](#bracketid)         | TINYINT  | UNSIGNED | NO   |     |         |                |         |
| [type](#type)                    | TINYINT  | UNSIGNED | NO   |     |         |                |         |
| [date](#date)                    | DATETIME |          | NO   |     |         |                |         |

**Description of the table's fields**

### id

An unique value which identifies a BattleGround.

### winner\_faction

The faction which won the BattleGround:

| Value | Description |
| ----- | ----------- |
| 0     | HORDE       |
| 1     | ALLIANCE    |
| 2     | NONE        |

### bracket\_id

Identifies the bracket level range:

| Value | Level range |
| ----- | ----------- |
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
| ----- | ---------------------- |
| 1     | Alterac Valley         |
| 2     | Warsong Gulch          |
| 3     | Arathi Basin           |
| 7     | Eye of the Storm       |
| 9     | Strand of the Ancients |
| 30    | Isle of Conquest       |

### date

Date and time of BattleGround ending.
