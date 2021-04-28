# battleground\_deserters

[<-Back-to:Characters](database-characters.md)

**The \`battleground\_deserters\` table**

This table holds datas about BattleGrounds deserters. To enable storing this kind of informations, set **Battleground . TrackDeserters . Enable   =   1** in **worldserver.config** file.

**Structure**

| Field         | Type     | Attributes | Key | Null | Default | Extra | Comment |
|---------------|----------|------------|-----|------|---------|-------|---------|
| [guid][1]     | INT      | UNSIGNED   |     |      |         |       |         |
| [type][2]     | TINYINT  | UNSIGNED   |     |      |         |       |         |
| [datetime][3] | datetime |            |     |      |         |       |         |

[1]: #guid
[2]: #type
[3]: #datetime

**Description of the fields**

### guid

Link to characters.guid

### type

| Value | Description                                             |
|-------|---------------------------------------------------------|
| 0     | player leaves the BG                                    |
| 1     | player is kicked from BG because offline                |
| 2     | player is invited to join and refuses to do it          |
| 3     | player is invited to join and do nothing (time expires) |
| 4     | player is invited to join and logs out                  |

### datetime

date and time of the event
