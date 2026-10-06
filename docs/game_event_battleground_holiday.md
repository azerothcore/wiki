# game\_event\_battleground\_holiday

[<-Back-to:World](database-world)

**The \`game\_event\_battleground\_holiday\` table**

This table is used to add a holiday to a battleground, for things like extra reputation / honor.

**Table: game\_event\_battleground\_holiday's Structure**

| Field                     | Type    |          | Null | Key | Default | Extra | Comment                 |
| :------------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------- |
| [eventEntry](#evententry) | TINYINT | UNSIGNED | NO   | PRI |         |       | Entry of the game event |
| [bgflag](#bgflag)         | INT     | UNSIGNED | NO   |     | 0       |       |                         |

**Description of the table's fields**

### eventEntry

[game_event.eventEntry](game_event#evententry)

### bgflag

This is a bitmask field that decides which battle grounds are affected for this given holiday.

| Value | Hex      | Flag                   | Comment |
| :---- | :------: | :--------------------- | :------ |
| 1     | `0x0001` | Alterac Valley         |         |
| 4     | `0x0004` | Warsong Gulch          |         |
| 8     | `0x0008` | Arathi Basin           |         |
| 16    | `0x0010` | Nagrand Arena          |         |
| 32    | `0x0020` | Blade's Edge Arena     |         |
| 64    | `0x0040` | All Arena              |         |
| 128   | `0x0080` | Eye of the Storm       |         |
| 256   | `0x0100` | Ruins of Lordaeron     |         |
| 512   | `0x0200` | Strand of the Ancients |         |
| 1024  | `0x0400` | Dalaran Sewers         |         |
| 2048  | `0x0800` | The Ring of Valor      |         |

| Value      | Hex          | Flag                                  | eventEntry |
| :--------- | :----------: | :------------------------------------ | :--------- |
| 2          | `0x00000002` | Call to Arms: Alterac Valley!         | 18         |
| 4          | `0x00000004` | Call to Arms: Warsong Gulch!          | 19         |
| 8          | `0x00000008` | Call to Arms: Arathi Basin!           | 20         |
| 128        | `0x00000080` | Call to Arms: Eye of the Storm!       | 21         |
| 512        | `0x00000200` | Call to Arms: Strand of the Ancients! | 53         |
| 1073741824 | `0x40000000` | Call to Arms: Isle of Conquest!       | 54         |
