# creature\_summon\_groups

[<-Back-to:World](database-world)

# Table: creature\_summon\_groups

This table holds data about temporary summoned creatures. It is possible to group summons and create boss waves of adds etc.

**Table: creature\_summon\_groups's Structure**

| Field                         | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [summonerId](#summonerid)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [summonerType](#summonertype) | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [groupId](#groupid)           | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [entry](#entry)               | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [position_x](#positionx)      | FLOAT        |          | NO   |     | 0       |       |         |
| [position_y](#positiony)      | FLOAT        |          | NO   |     | 0       |       |         |
| [position_z](#positionz)      | FLOAT        |          | NO   |     | 0       |       |         |
| [orientation](#orientation)   | FLOAT        |          | NO   |     | 0       |       |         |
| [summonType](#summontype)     | TINYINT      | UNSIGNED | NO   |     | 0       |       |         |
| [summonTime](#summontime)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Comment](#comment)           | VARCHAR(255) |          | NO   |     | ''      |       |         |

**Description of the table's fields**

### summonerId

Summoner's id depending on [summonerType](#summonertype)

### summonerType

Summoner's type:

| Value | Type                     |
| ----- | ------------------------ |
| 0     | SUMMONER_TYPE_CREATURE   |
| 1     | SUMMONER_TYPE_GAMEOBJECT |
| 2     | SUMMONER_TYPE_MAP        |

### groupId

Group identificator, all creatures with the same [groupId](#groupid) will be summoned at once

### entry

Entry of summoned creature from [creature\_template.entry](creature_template#entry)

### position\_x

X coordinate of position, where the creature will be spawned

### position\_y

Y coordinate of position, where the creature will be spawned

### position\_z

Z coordinate of position, where the creature will be spawned

### orientation

Orientation the summoned creature will get when spawned

### summonType

| Value | Name                                   | Comments                                                            |
| ----- | -------------------------------------- | ------------------------------------------------------------------- |
| 1     | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | Despawns after a specified time OR when the creature disappears     |
| 2     | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | Despawns after a specified time OR when the creature dies           |
| 3     | TEMPSUMMON_TIMED_DESPAWN               | Despawns after a specified time                                     |
| 4     | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | Despawns after a specified time after the creature is out of combat |
| 5     | TEMPSUMMON_CORPSE_DESPAWN              | Despawns instantly after death                                      |
| 6     | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | Despawns after a specified time after death                         |
| 7     | TEMPSUMMON_DEAD_DESPAWN                | Despawns when the creature disappears                               |
| 8     | TEMPSUMMON_MANUAL_DESPAWN              | Despawns when UnSummon() is called                                  |

### summonTime

Timer linked to summontype

### Comment

Comment
