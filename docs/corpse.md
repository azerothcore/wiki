[Database Structure](Database-Structure) > [Character-Database](Character-Database) > [corpse](corpse)

| Field       | Type        | Attributes | Key | Null | Default | Extra  | Comment                            |
|-------------|-------------|------------|-----|------|---------|--------|------------------------------------|
| corpseGuid  | INT     | UNSIGNED   | PRI | NO   | 0       | Unique | Global Unique Identifier           |
| guid        | INT     | UNSIGNED   |     | NO   | 0       |        | Character Global Unique Identifier |
| posX        | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| posY        | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| posZ        | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| orientation | FLOAT       | SIGNED     |     | NO   | 0       |        |                                    |
| mapId       | SMALLINT | UNSIGNED   |     | NO   | 0       |        | Map Identifier                     |
| phaseMask   | SMALLINT | UNSIGNED   |     | NO   | 0       |        |                                    |
| displayId   | INT     | UNSIGNED   |     | NO   | 0       |        |                                    |
| itemCache   | text        | SIGNED     |     | NO   |         |        |                                    |
| bytes1      | INT     | UNSIGNED   |     | NO   | 0       |        |                                    |
| bytes2      | INT     | UNSIGNED   |     | NO   | 0       |        |                                    |
| guildId     | INT     | UNSIGNED   |     | NO   | 0       |        |                                    |
| flags       | TINYINT  | UNSIGNED   |     | NO   | 0       |        |                                    |
| dynFlags    | TINYINT  | UNSIGNED   |     | NO   | 0       |        |                                    |
| time        | INT     | UNSIGNED   |     | NO   | 0       |        |                                    |
| corpseType  | TINYINT  | UNSIGNED   |     | NO   | 0       |        |                                    |
| instanceId  | INT     | UNSIGNED   |     | NO   | 0       |        |                                    |
