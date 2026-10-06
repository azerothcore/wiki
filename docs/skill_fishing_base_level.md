# skill\_fishing\_base\_level

[<-Back-to:World](database-world)

**The \`skill\_fishing\_base\_level\` table**

This table controls the minimum skill level required in fishing to fish in a certain area.

**Table: skill\_fishing\_base\_level's Structure**

| Field           | Type     |          | Null | Key | Default | Extra | Comment                      |
| :-------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :--------------------------- |
| [entry](#entry) | INT      | UNSIGNED | NO   | PRI | 0       |       | Area identifier              |
| [skill](#skill) | SMALLINT |          | NO   |     | 0       |       | Base skill level requirement |

**Description of the table's fields**

### entry

The area ID see [AreaTable.dbc](areatable).

### skill

The minimum skill points in fishing required to fish in the area.
