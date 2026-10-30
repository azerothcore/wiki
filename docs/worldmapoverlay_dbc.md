# worldmapoverlay\_dbc

[<-Back-to:World](database-world)

**The \`worldmapoverlay\_dbc\` table**

This table has the same columns as the client file `WorldMapOverlay.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: worldmapoverlay\_dbc's Structure**

| Field                           | Type         |     | Null | Key | Default | Extra | Comment |
| :------------------------------ | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT          |     | NO   | PRI | 0       |       |         |
| [MapAreaID](#mapareaid)         | INT          |     | NO   |     | 0       |       |         |
| [AreaID_1](#areaid)             | INT          |     | NO   |     | 0       |       |         |
| [AreaID_2](#areaid)             | INT          |     | NO   |     | 0       |       |         |
| [AreaID_3](#areaid)             | INT          |     | NO   |     | 0       |       |         |
| [AreaID_4](#areaid)             | INT          |     | NO   |     | 0       |       |         |
| [MapPointX](#mappointx)         | INT          |     | NO   |     | 0       |       |         |
| [MapPointY](#mappointy)         | INT          |     | NO   |     | 0       |       |         |
| [TextureName](#texturename)     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [TextureWidth](#texturewidth)   | INT          |     | NO   |     | 0       |       |         |
| [TextureHeight](#textureheight) | INT          |     | NO   |     | 0       |       |         |
| [OffsetX](#offsetx)             | INT          |     | NO   |     | 0       |       |         |
| [OffsetY](#offsety)             | INT          |     | NO   |     | 0       |       |         |
| [HitRectTop](#hitrecttop)       | INT          |     | NO   |     | 0       |       |         |
| [HitRectLeft](#hitrectleft)     | INT          |     | NO   |     | 0       |       |         |
| [HitRectBottom](#hitrectbottom) | INT          |     | NO   |     | 0       |       |         |
| [HitRectRight](#hitrectright)   | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `WorldMapOverlayEntry::ID`.

### MapAreaID

Not used by the core.

Comment in the core source: "idx in WorldMapArea.dbc"

### AreaID

The core reads these columns into `WorldMapOverlayEntry::areatableID`.

### MapPointX

Not used by the core.

### MapPointY

Not used by the core.

### TextureName

Not used by the core.

### TextureWidth

Not used by the core.

### TextureHeight

Not used by the core.

### OffsetX

Not used by the core.

### OffsetY

Not used by the core.

### HitRectTop

Not used by the core.

### HitRectLeft

Not used by the core.

### HitRectBottom

Not used by the core.

### HitRectRight

Not used by the core.
