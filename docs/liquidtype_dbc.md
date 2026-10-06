# liquidtype\_dbc

[<-Back-to:World](database-world)

**The \`liquidtype\_dbc\` table**

This table has the same columns as the client file `LiquidType.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: liquidtype\_dbc's Structure**

| Field                                     | Type         |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                 | INT          |     | NO   | PRI | 0       |       |         |
| [Name](#name)                             | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Flags](#flags)                           | INT          |     | NO   |     | 0       |       |         |
| [Type](#type)                             | INT          |     | NO   |     | 0       |       |         |
| [SoundID](#soundid)                       | INT          |     | NO   |     | 0       |       |         |
| [SpellID](#spellid)                       | INT          |     | NO   |     | 0       |       |         |
| [MaxDarkenDepth](#maxdarkendepth)         | FLOAT        |     | NO   |     | 0       |       |         |
| [FogDarkenintensity](#fogdarkenintensity) | FLOAT        |     | NO   |     | 0       |       |         |
| [AmbDarkenintensity](#ambdarkenintensity) | FLOAT        |     | NO   |     | 0       |       |         |
| [DirDarkenintensity](#dirdarkenintensity) | FLOAT        |     | NO   |     | 0       |       |         |
| [LightID](#lightid)                       | INT          |     | NO   |     | 0       |       |         |
| [ParticleScale](#particlescale)           | FLOAT        |     | NO   |     | 0       |       |         |
| [ParticleMovement](#particlemovement)     | INT          |     | NO   |     | 0       |       |         |
| [ParticleTexSlots](#particletexslots)     | INT          |     | NO   |     | 0       |       |         |
| [MaterialID](#materialid)                 | INT          |     | NO   |     | 0       |       |         |
| [Texture_1](#texture)                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_2](#texture)                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_3](#texture)                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_4](#texture)                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_5](#texture)                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Texture_6](#texture)                     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [Color_1](#color)                         | INT          |     | NO   |     | 0       |       |         |
| [Color_2](#color)                         | INT          |     | NO   |     | 0       |       |         |
| [Float_1](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_2](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_3](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_4](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_5](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_6](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_7](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_8](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_9](#float)                         | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_10](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_11](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_12](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_13](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_14](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_15](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_16](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_17](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Float_18](#float)                        | FLOAT        |     | NO   |     | 0       |       |         |
| [Int_1](#int)                             | INT          |     | NO   |     | 0       |       |         |
| [Int_2](#int)                             | INT          |     | NO   |     | 0       |       |         |
| [Int_3](#int)                             | INT          |     | NO   |     | 0       |       |         |
| [Int_4](#int)                             | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Name

Not used by the core.

### Flags

Not used by the core.

### Type

The core reads this column.

### SoundID

Not used by the core.

### SpellID

The core reads this column.

### MaxDarkenDepth

Not used by the core.

### FogDarkenintensity

Not used by the core.

### AmbDarkenintensity

Not used by the core.

### DirDarkenintensity

Not used by the core.

### LightID

Not used by the core.

### ParticleScale

Not used by the core.

### ParticleMovement

Not used by the core.

### ParticleTexSlots

Not used by the core.

### MaterialID

Not used by the core.

### Texture

Not used by the core.

### Color

Not used by the core.

### Float

Not used by the core.

### Int

Not used by the core.
