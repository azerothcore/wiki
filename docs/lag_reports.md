# lag\_reports

[<-Back-to:Characters](database-characters)

**The \`lag\_reports\` table**

This table stores the lag reports made by players ingame (when they click on "Help Request").

**Table: lag\_reports's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra          | Comment |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [reportId](#reportid)     | INT      | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [guid](#guid)             | INT      | UNSIGNED | NO   |     | 0       |                |         |
| [lagType](#lagtype)       | TINYINT  | UNSIGNED | NO   |     | 0       |                |         |
| [mapId](#mapid)           | SMALLINT | UNSIGNED | NO   |     | 0       |                |         |
| [posX](#posx)             | FLOAT    |          | NO   |     | 0       |                |         |
| [posY](#posy)             | FLOAT    |          | NO   |     | 0       |                |         |
| [posZ](#posz)             | FLOAT    |          | NO   |     | 0       |                |         |
| [latency](#latency)       | INT      | UNSIGNED | NO   |     | 0       |                |         |
| [createTime](#createtime) | INT      | UNSIGNED | NO   |     | 0       |                |         |

**Description of the table's fields**

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

Time the report was created, as a Unix timestamp.
