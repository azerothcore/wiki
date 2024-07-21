# lag\_reports

[<-Back-to:Characters](database-characters)

**The `\lag\_reports\` table**

This table stores the lag reports made by players ingame (when they click on "Help Request").

**Table Structure**

| Field           | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [reportId][1]   | INT      | UNSIGNED   | PRI | NO   |         | Auto Increment |         |
| [guid][2]       | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [lagType][3]    | TINYINT  | UNSIGNED   |     | NO   | 0       |                |         |
| [mapId][4]      | SMALLINT | UNSIGNED   |     | NO   | 0       |                |         |
| [posX][5]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [posY][6]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [posZ][7]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [latency][8]    | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [createTime][9] | INT      | UNSIGNED   |     | NO   | 0       |                |         |

[1]: #reportid
[2]: #guid
[3]: #lagtype
[4]: #mapid
[5]: #posx
[6]: #posy
[7]: #posz
[8]: #latency
[9]: #createtime

**Description of the fields**

### reportId

Report ID

### guid

Character guid. See [characters.guid](characters#guid)

### lagType

* 0 = Loot related
* 1 = Auction House related
* 2 = Mail related
* 3 = Chat related
* 4 = Movement related
* 5 = Spells and Abilities related

### mapId

Map where lag was reported. See [Map.dbc](map).

### posX

Position X.

### posY

Position Y.

### posZ

Position Z.

### latency

Latency in ms at the moment of the report.

### createTime

Creation date in Unix Time. (TODO: should be changed to mysql timestamp).
