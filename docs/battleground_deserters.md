# battleground\_deserters

[<-Back-to:Characters](database-characters)

**The \`battleground\_deserters\` table**

This table holds datas about BattleGrounds deserters. To enable storing this kind of informations, set **Battleground.TrackDeserters.Enable = 1** in **worldserver.config** file.

**Table Structure**

| Field         | Type     | Attributes | Key | Null | Default | Extra | Comment                   |
| ------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------------------------- |
| [guid][1]     | INT      | UNSIGNED   |     | NO   |         |       | characters.guid           |
| [type][2]     | TINYINT  | UNSIGNED   |     | NO   |         |       | type of the desertion     |
| [datetime][3] | DATETIME | SIGNED     |     | NO   |         |       | datetime of the desertion |

[1]: #guid
[2]: #type
[3]: #datetime

**Description of the fields**

### guid

Link to [characters.guid](characters#guid).

### type

| Value | Description                                             |
| ----- | ------------------------------------------------------- |
| 0     | player leaves the BG                                    |
| 1     | player is kicked from BG because offline                |
| 2     | player is invited to join and refuses to do it          |
| 3     | player is invited to join and do nothing (time expires) |
| 4     | player is invited to join and logs out                  |

### datetime

Date and time of the event.
