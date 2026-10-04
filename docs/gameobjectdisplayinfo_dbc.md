# gameobjectdisplayinfo\_dbc

[<-Back-to:World](database-world)

**The \`gameobjectdisplayinfo\_dbc\` table**

This table has the same columns as the client file `GameObjectDisplayInfo.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: gameobjectdisplayinfo\_dbc's Structure**

| Field                                           | Type         |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                       | INT          |     | NO   | PRI | 0       |       |         |
| [ModelName](#modelname)                         | VARCHAR(200) |     | YES  |     | NULL    |       |         |
| [Sound_1](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_2](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_3](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_4](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_5](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_6](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_7](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_8](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_9](#sound)                               | INT          |     | NO   |     | 0       |       |         |
| [Sound_10](#sound)                              | INT          |     | NO   |     | 0       |       |         |
| [GeoBoxMinX](#geoboxminx)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [GeoBoxMinY](#geoboxminy)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [GeoBoxMinZ](#geoboxminz)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [GeoBoxMaxX](#geoboxmaxx)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [GeoBoxMaxY](#geoboxmaxy)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [GeoBoxMaxZ](#geoboxmaxz)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [ObjectEffectPackageID](#objecteffectpackageid) | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `GameObjectDisplayInfoEntry::Displayid`.

### ModelName

The core reads this column into `GameObjectDisplayInfoEntry::filename`.

### Sound

Not used by the core.

### GeoBoxMinX

The core reads this column.

### GeoBoxMinY

The core reads this column.

### GeoBoxMinZ

The core reads this column.

### GeoBoxMaxX

The core reads this column.

### GeoBoxMaxY

The core reads this column.

### GeoBoxMaxZ

The core reads this column.

### ObjectEffectPackageID

Not used by the core.
