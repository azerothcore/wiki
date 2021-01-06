# skill\_fishing\_base\_level

[<-Back-to:World](database-world.md)

**The \`skill\_fishing\_base\_level\` table**

This table controls the minimum skill level required in fishing to fish in a certain area.

**Structure**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comment                      |
|------------|--------------|------------|-----|------|---------|-------|------------------------------|
| [entry][1] | mediumint(8) | unsigned   | PRI | NO   | 0       |       | Area identifier              |
| [skill][2] | smallint(6)  | signed     |     | NO   | 0       |       | Base skill level requirement |

**Description of the fields**

### entry

The area ID see [AreaTable.dbc](AreaTable).

### skill

The minimum skill points in fishing required to fish in the area.
