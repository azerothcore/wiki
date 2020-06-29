# lag_reports

[<-Back-to:Characters](database-characters.md)


## The `lag_reports` table

This table stores the lag reports made by players ingame (when they click on "Help Request").


## Structure

| Field           | Type        | Attributes | Key | Null | Default | Extra          | Comment |
|-----------------|-------------|------------|-----|------|---------|----------------|---------|
| [reportId][1]   | int(10)     | unsigned   | PRI | NO   |         | Auto Increment |         |
| [guid][2]       | int(10)     | unsigned   |     | NO   | 0       |                |         |
| [lagType][3]    | inyint(3)   | unsigned   |     | NO   | 0       |                |         |
| [mapId][4]      | smallint(5) | unsigned   |     | NO   | 0       |                |         |
| [posX][5]       | float       | signed     |     | NO   | 0       |                |         |
| [posY][6]       | float       | signed     |     | NO   | 0       |                |         |
| [posZ][7]       | float       | signed     |     | NO   | 0       |                |         |
| [latency][8]    | int(10)     | unsigned   |     | NO   | 0       |                |         |
| [createTime][9] | int(10)     | unsigned   |     | NO   | 0       |                |         |

[1]: #reportId
[2]: #guid
[3]: #lagType
[4]: #mapId
[5]: #posX
[6]: #posY
[7]: #posZ
[8]: #latency
[9]: #createTime


## Description of the fields

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

Map where lag was reported. See Map.dbc

### posX

Position X

### posY

Position Y

### posZ

Position Z

### latency

Latency in ms at the moment of the report.

### createTime

Creation date in Unix Time (TODO: should be changed to mysql timestamp)
