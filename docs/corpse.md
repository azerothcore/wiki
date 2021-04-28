[Database Structure](Database-Structure) > [Character-Database](Character-Database) > [corpse](corpse)

| Field       | Type        | Attributes | Key | Null | Default | Extra  | Comment                            |
|-------------|-------------|------------|-----|------|---------|--------|------------------------------------|
| corpseGuid  | INT(10)     | unsigned   | PRI | NO   | 0       | Unique | Global Unique Identifier           |
| guid        | INT(10)     | unsigned   |     | NO   | 0       |        | Character Global Unique Identifier |
| posX        | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| posY        | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| posZ        | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| orientation | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| mapId       | SMALLINT(5) | unsigned   |     | NO   | 0       |        | Map Identifier                     |
| phaseMask   | SMALLINT(5) | unsigned   |     | NO   | 0       |        |                                    |
| displayId   | INT(10)     | unsigned   |     | NO   | 0       |        |                                    |
| itemCache   | text        | signed     |     | NO   |         |        |                                    |
| bytes1      | INT(10)     | unsigned   |     | NO   | 0       |        |                                    |
| bytes2      | INT(10)     | unsigned   |     | NO   | 0       |        |                                    |
| guildId     | INT(10)     | unsigned   |     | NO   | 0       |        |                                    |
| flags       | TINYINT(3)  | unsigned   |     | NO   | 0       |        |                                    |
| dynFlags    | TINYINT(3)  | unsigned   |     | NO   | 0       |        |                                    |
| time        | INT(10)     | unsigned   |     | NO   | 0       |        |                                    |
| corpseType  | TINYINT(3)  | unsigned   |     | NO   | 0       |        |                                    |
| instanceId  | INT(10)     | unsigned   |     | NO   | 0       |        |                                    |
