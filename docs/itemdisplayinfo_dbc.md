# itemdisplayinfo\_dbc

[<-Back-to:World](database-world)

**The \`itemdisplayinfo\_dbc\` table**

This table has the same columns as the client file `ItemDisplayInfo.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: itemdisplayinfo\_dbc's Structure**

| Field                                 | Type         |     | Null | Key | Default | Extra | Comment |
| :------------------------------------ | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                             | INT          |     | NO   | PRI | 0       |       |         |
| [ModelName_1](#modelname)             | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [ModelName_2](#modelname)             | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [ModelTexture_1](#modeltexture)       | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [ModelTexture_2](#modeltexture)       | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [InventoryIcon_1](#inventoryicon)     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [InventoryIcon_2](#inventoryicon)     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [GeosetGroup_1](#geosetgroup)         | INT          |     | NO   |     | 0       |       |         |
| [GeosetGroup_2](#geosetgroup)         | INT          |     | NO   |     | 0       |       |         |
| [GeosetGroup_3](#geosetgroup)         | INT          |     | NO   |     | 0       |       |         |
| [Flags](#flags)                       | INT          |     | NO   |     | 0       |       |         |
| [SpellVisualID](#spellvisualid)       | INT          |     | NO   |     | 0       |       |         |
| [GroupSoundIndex](#groupsoundindex)   | INT          |     | NO   |     | 0       |       |         |
| [HelmetGeosetVis_1](#helmetgeosetvis) | INT          |     | NO   |     | 0       |       |         |
| [HelmetGeosetVis_2](#helmetgeosetvis) | INT          |     | NO   |     | 0       |       |         |
| [Texture_1](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_2](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_3](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_4](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_5](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_6](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_7](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_8](#texture)                 | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [ItemVisual](#itemvisual)             | INT          |     | NO   |     | 0       |       |         |
| [ParticleColorID](#particlecolorid)   | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### ModelName

Not used by the core.

### ModelTexture

Not used by the core.

### InventoryIcon

The core reads `InventoryIcon_1`. `InventoryIcon_2` is not used by the core.

### GeosetGroup

Not used by the core.

### Flags

Not used by the core.

### SpellVisualID

Not used by the core.

### GroupSoundIndex

Not used by the core.

### HelmetGeosetVis

Not used by the core.

### Texture

Not used by the core.

### ItemVisual

Not used by the core.

### ParticleColorID

Not used by the core.
