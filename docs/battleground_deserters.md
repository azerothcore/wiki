# battleground\_deserters

[<-Back-to:Characters](database-characters)

**The \`battleground\_deserters\` table**

This table holds datas about BattleGrounds deserters. To enable storing this kind of informations, set **Battleground.TrackDeserters.Enable = 1** in **worldserver.config** file.

**Table: battleground\_deserters's Structure**

| Field                 | Type     |          | Null | Key | Default | Extra | Comment                   |
| :-------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------------------------ |
| [guid](#guid)         | INT      | UNSIGNED | NO   |     |         |       | characters.guid           |
| [type](#type)         | TINYINT  | UNSIGNED | NO   |     |         |       | type of the desertion     |
| [datetime](#datetime) | DATETIME |          | NO   |     |         |       | datetime of the desertion |

**Description of the table's fields**

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
