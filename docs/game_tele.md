# game\_tele

[<-Back-to:World](database-world)

**Table Structure**

This table contains a list of teleport locations that can be used with the *.tele* command in-game. Entries in this table can be added/deleted manually or with the *.tele add* and *.tele delete* commands.

| Field            | Type         | Attributes | Key | Null | Default | Extra          |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | -------------- |
| [id][1]          | MEDIUMINT    | UNSIGNED   | PRI | NO   | NULL    | Auto increment |
| [position_x][2]  | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [position_y][3]  | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [position_z][4]  | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [orientation][5] | FLOAT        | SIGNED     |     | NO   | 0       |                |
| [map][6]         | SMALLINT     | UNSIGNED   |     | NO   | 0       |                |
| [name][7]        | VARCHAR(100) | SIGNED     |     | NO   | NULL    |                |

[1]: #id
[2]: #position_x
[3]: #position_y
[4]: #position_z
[5]: #orientation
[6]: #map
[7]: #name

**Field Descriptions**

### id

The ID of the teleport location. This number is unique to every location added.

### position\_x

The x-axis coordinate of the teleport location. This can be attained by using the *.gps* command.

### position\_y

The y-axis coordinate of the teleport location. This can be attained by using the *.gps* command.

### position\_z

The z-axis coordinate of the teleport location. This can be attained by using the *.gps* command.

### orientation

The direction that the player will face after arriving at the teleport location. This can be attained by using the *.gps* command.

(North = 0, South = 3.14159)

### map

The map ID of the location. See the [Map DBC file](Map) for the IDs of all of the zones.

### name

A descriptive name for the teleport location. The name *cannot* have any spaces in it. It is also not recommended to use special characters such as periods, commas, slashes, etc...

### Examples

| id  | position_x | position_y | position_z | orientation | map | name         |
| --- | ---------- | ---------- | ---------- | ----------- | --- | ------------ |
| 10  | 2799.46    | 847.549    | 111.842    | 0.509892    | 0   | AgamandMills |
| 11  | -7040.08   | -3342.15   | 241.667    | 0.82338     | 0   | AgmondsEnd   |
| 12  | 451.572    | -3342.23   | 119.689    | 0.772541    | 0   | AgolWatha    |
| 13  | -2681.4    | -4787.21   | 16.0751    | 4.69276     | 1   | AlcazIsland  |
| 14  | -1746.58   | 5780.03    | 146.44     | 1.30629     | 530 | AldorRise    |
