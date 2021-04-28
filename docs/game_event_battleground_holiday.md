# game\_event\_battleground\_holiday

[<-Back-to:World](database-world.md)

**The \`Game\_event\_battleground\_holiday\` table**

This table is used to add a holiday to a battleground, for things like extra reputation / honor.

**Structure**

| Field           | Type       | Attributes | Key | Null | Default | Extra  | Comment                 |
|-----------------|------------|------------|-----|------|---------|--------|-------------------------|
| [eventEntry][1] | TINYINT(3) | UNSIGNED   | PRI | NO   |         | Unique | Entry of the game event |
| [bgflag][2]     | INT(10)    | UNSIGNED   |     | NO   | 0       |        |                         |

[1]: #evententry
[2]: #bgflag

**Description of the fields**

### eventEntry

This is entry id of the game\_event that was setup to add the holiday.

### bgflag

This is a bitmask field that decides which battle grounds are affected for this given holiday.

| bit  | Battleground           |
|------|------------------------|
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
