[Database Structure](Database-Structure) > [Character-Database](Character-Database) > [corpse](corpse)

| Field       | Type        | Attributes | Key | Null | Default | Extra  | Comment                            |
|-------------|-------------|------------|-----|------|---------|--------|------------------------------------|
| corpseGuid  | int(10)     | unsigned   | PRI | NO   | 0       | Unique | Global Unique Identifier           |
| guid        | int(10)     | unsigned   |     | NO   | 0       |        | Character Global Unique Identifier |
| posX        | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| posY        | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| posZ        | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| orientation | FLOAT       | signed     |     | NO   | 0       |        |                                    |
| mapId       | SMALLINT(5) | unsigned   |     | NO   | 0       |        | Map Identifier                     |
| phaseMask   | SMALLINT(5) | unsigned   |     | NO   | 0       |        |                                    |
| displayId   | int(10)     | unsigned   |     | NO   | 0       |        |                                    |
| itemCache   | text        | signed     |     | NO   |         |        |                                    |
| bytes1      | int(10)     | unsigned   |     | NO   | 0       |        |                                    |
| bytes2      | int(10)     | unsigned   |     | NO   | 0       |        |                                    |
| guildId     | int(10)     | unsigned   |     | NO   | 0       |        |                                    |
| flags       | tinyint(3)  | unsigned   |     | NO   | 0       |        |                                    |
| dynFlags    | tinyint(3)  | unsigned   |     | NO   | 0       |        |                                    |
| time        | int(10)     | unsigned   |     | NO   | 0       |        |                                    |
| corpseType  | tinyint(3)  | unsigned   |     | NO   | 0       |        |                                    |
| instanceId  | int(10)     | unsigned   |     | NO   | 0       |        |                                    |
