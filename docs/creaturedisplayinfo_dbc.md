# creaturedisplayinfo\_dbc

[<-Back-to:World](database-world)

**The \`creaturedisplayinfo\_dbc\` table**

This table has the same columns as the client file `CreatureDisplayInfo.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: creaturedisplayinfo\_dbc's Structure**

| Field                                           | Type         |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                       | INT          |     | NO   | PRI | 0       |       |         |
| [ModelID](#modelid)                             | INT          |     | NO   |     | 0       |       |         |
| [SoundID](#soundid)                             | INT          |     | NO   |     | 0       |       |         |
| [ExtendedDisplayInfoID](#extendeddisplayinfoid) | INT          |     | NO   |     | 0       |       |         |
| [CreatureModelScale](#creaturemodelscale)       | FLOAT        |     | NO   |     | 0       |       |         |
| [CreatureModelAlpha](#creaturemodelalpha)       | INT          |     | NO   |     | 0       |       |         |
| [TextureVariation_1](#texturevariation)         | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [TextureVariation_2](#texturevariation)         | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [TextureVariation_3](#texturevariation)         | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [PortraitTextureName](#portraittexturename)     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [BloodLevel](#bloodlevel)                       | INT          |     | NO   |     | 0       |       |         |
| [BloodID](#bloodid)                             | INT          |     | NO   |     | 0       |       |         |
| [NPCSoundID](#npcsoundid)                       | INT          |     | NO   |     | 0       |       |         |
| [ParticleColorID](#particlecolorid)             | INT          |     | NO   |     | 0       |       |         |
| [CreatureGeosetData](#creaturegeosetdata)       | INT          |     | NO   |     | 0       |       |         |
| [ObjectEffectPackageID](#objecteffectpackageid) | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `CreatureDisplayInfoEntry::Displayid`.

### ModelID

The core reads this column into `CreatureDisplayInfoEntry::ModelId`.

### SoundID

Not used by the core.

### ExtendedDisplayInfoID

The core reads this column into `CreatureDisplayInfoEntry::ExtendedDisplayInfoID`.

### CreatureModelScale

The core reads this column into `CreatureDisplayInfoEntry::scale`.

### CreatureModelAlpha

Not used by the core.

### TextureVariation

Not used by the core.

### PortraitTextureName

Not used by the core.

### BloodLevel

Not used by the core.

### BloodID

Not used by the core.

### NPCSoundID

Not used by the core.

### ParticleColorID

Not used by the core.

### CreatureGeosetData

Not used by the core.

### ObjectEffectPackageID

Not used by the core.
