[Database Structure](Database-Structure) > [Character-Database](Character-Database) > [corpse](corpse)

| Field       | Type        | Attributes | Key | Null | Default | Extra  | Comment                            |
|-------------|-------------|------------|-----|------|---------|--------|------------------------------------|
| corpseGuid  | INT(10)     | UNSIGNED   | PRI | NO   | 0       | Unique | Global Unique Identifier           |
| guid        | INT(10)     | UNSIGNED   |     | NO   | 0       |        | Character Global Unique Identifier |
| posX        | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| posY        | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| posZ        | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| orientation | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| mapId       | SMALLINT(5) | UNSIGNED   |     | NO   | 0       |        | Map Identifier                     |
| phaseMask   | SMALLINT(5) | UNSIGNED   |     | NO   | 0       |        |                                    |
| displayId   | INT(10)     | UNSIGNED   |     | NO   | 0       |        |                                    |
| itemCache   | text        | SIGNED     |     | NO   |         |        |                                    |
| bytes1      | INT(10)     | UNSIGNED   |     | NO   | 0       |        |                                    |
| bytes2      | INT(10)     | UNSIGNED   |     | NO   | 0       |        |                                    |
| guildId     | INT(10)     | UNSIGNED   |     | NO   | 0       |        |                                    |
| flags       | TINYINT(3)  | UNSIGNED   |     | NO   | 0       |        |                                    |
| dynFlags    | TINYINT(3)  | UNSIGNED   |     | NO   | 0       |        |                                    |
| time        | INT(10)     | UNSIGNED   |     | NO   | 0       |        |                                    |
| corpseType  | TINYINT(3)  | UNSIGNED   |     | NO   | 0       |        |                                    |
| instanceId  | INT(10)     | UNSIGNED   |     | NO   | 0       |        |                                    |
