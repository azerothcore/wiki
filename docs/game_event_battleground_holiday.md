# game_event_battleground_holiday

[<-Back-to:World](database-world)

**The \`Game_event_battleground_holiday\` table**

This table is used to add a holiday to a battleground, for things like extra reputation / honor.

**Table Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra  | Comment                 |
| --------------- | ------- | ---------- | --- | ---- | ------- | ------ | ----------------------- |
| [eventEntry][1] | TINYINT | UNSIGNED   | PRI | NO   |         | Unique | Entry of the game event |
| [bgflag][2]     | INT     | UNSIGNED   |     | NO   | 0       |        |                         |

[1]: #evententry
[2]: #bgflag

**Description of the fields**

### eventEntry

[game_event.eventEntry](game_event#eventEntry)

### bgflag

This is a bitmask field that decides which battle grounds are affected for this given holiday.

| bit  | Battleground           |
| ---- | ---------------------- |
| 1    | Alterac Valley         |
| 4    | Warsong Gulch          |
| 8    | Arathi Basin           |
| 16   | Nagrand Arena          |
| 32   | Blade's Edge Arena     |
| 64   | All Arena              |
| 128  | Eye of the Storm       |
| 256  | Ruins of Lordaeron     |
| 512  | Strand of the Ancients |
| 1024 | Dalaran Sewers         |
| 2048 | The Ring of Valor      |

| eventEntry | bgflag        | Comment (not part of the DB)          |
| ---------- | ------------- | :------------------------------------ |
| 18         | 2             | Call to Arms: Alterac Valley!         |
| 19         | 4             | Call to Arms: Warsong Gulch!          |
| 20         | 8             | Call to Arms: Arathi Basin!           |
| 21         | 128           | Call to Arms: Eye of the Storm!       |
| 53         | 512           | Call to Arms: Strand of the Ancients! |
| 54         | 1 073 741 824 | Call to Arms: Isle of Conquest!       |
