# worldmaparea\_dbc

[<-Back-to:World](database-world)

**The \`worldmaparea\_dbc\` table**

This table has the same columns as the client file `WorldMapArea.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: worldmaparea\_dbc's Structure**

| Field                                       | Type         |     | Null | Key | Default | Extra | Comment |
| :------------------------------------------ | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                   | INT          |     | NO   | PRI | 0       |       |         |
| [MapID](#mapid)                             | INT          |     | NO   |     | 0       |       |         |
| [AreaID](#areaid)                           | INT          |     | NO   |     | 0       |       |         |
| [AreaName](#areaname)                       | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [LocLeft](#locleft)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [LocRight](#locright)                       | FLOAT        |     | NO   |     | 0       |       |         |
| [LocTop](#loctop)                           | FLOAT        |     | NO   |     | 0       |       |         |
| [LocBottom](#locbottom)                     | FLOAT        |     | NO   |     | 0       |       |         |
| [DisplayMapID](#displaymapid)               | INT          |     | NO   |     | 0       |       |         |
| [DefaultDungeonFloor](#defaultdungeonfloor) | INT          |     | NO   |     | 0       |       |         |
| [ParentWorldMapID](#parentworldmapid)       | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

Not used by the core.

### MapID

The core reads this column into `WorldMapAreaEntry::map_id`.

### AreaID

The row ID. The core uses it as the index of the rows and stores it in `WorldMapAreaEntry::area_id`.

Comment in the core source: "index (continent 0 areas ignored)"

### AreaName

Not used by the core.

### LocLeft

The core reads this column into `WorldMapAreaEntry::y1`.

### LocRight

The core reads this column into `WorldMapAreaEntry::y2`.

### LocTop

The core reads this column into `WorldMapAreaEntry::x1`.

### LocBottom

The core reads this column into `WorldMapAreaEntry::x2`.

### DisplayMapID

The core reads this column.

### DefaultDungeonFloor

Not used by the core.

Comment in the core source: "pointer to DungeonMap.dbc (owerride x1, x2, y1, y2 coordinates)"

### ParentWorldMapID

Not used by the core.
