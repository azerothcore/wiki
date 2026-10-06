# charsections\_dbc

[<-Back-to:World](database-world)

**The \`charsections\_dbc\` table**

This DBC contains the character customization sections (skin, face, facial hair, hair and underwear textures) available for each race/sex combination on the character creation and barbershop screens.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)

**Table: charsections\_dbc's Structure**

| Field                                                    | Type         |     | Null | Key | Default | Extra | Comment              |
| :------------------------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------------------- |
| [ID](#id)                                                | INT          |     | NO   | PRI | 0       |       | Unique ID            |
| [RaceID](#raceid)                                        | INT          |     | NO   |     | 0       |       |                      |
| [SexID](#sexid)                                          | INT          |     | NO   |     | 0       |       |                      |
| [BaseSection](#basesection)                              | INT          |     | NO   |     | 0       |       | CharSectionType      |
| [TextureName_1](#texturename1-texturename2-texturename3) | VARCHAR(100) |     | YES  |     | NULL    |       | Not used server-side |
| [TextureName_2](#texturename1-texturename2-texturename3) | VARCHAR(100) |     | YES  |     | NULL    |       | Not used server-side |
| [TextureName_3](#texturename1-texturename2-texturename3) | VARCHAR(100) |     | YES  |     | NULL    |       | Not used server-side |
| [Flags](#flags)                                          | INT          |     | NO   |     | 0       |       | CharSectionFlags     |
| [VariationIndex](#variationindex)                        | INT          |     | NO   |     | 0       |       |                      |
| [ColorIndex](#colorindex)                                | INT          |     | NO   |     | 0       |       |                      |

**Description of the table's fields**

### ID

This is the ID from CharSections.dbc.

### RaceID

ID from [ChrRaces.dbc](chrraces).

### SexID

| ID  | Name   |
| --- | ------ |
| 0   | Male   |
| 1   | Female |

### BaseSection

CharSectionType, the customization category this row belongs to.

| ID  | Name         |
| --- | ------------ |
| 0   | Skin         |
| 1   | Face         |
| 2   | Facial Hair  |
| 3   | Hair         |
| 4   | Underwear    |

### TextureName\_1, TextureName\_2, TextureName\_3

Client texture file paths for this section. Not used by the core.

### Flags

CharSectionFlags, a bitmask.

| Flag | Bit Value | Comment           |
| ---- | --------- | ----------------- |
| 1    | 0x01      | Player            |
| 4    | 0x04      | Death Knight      |

### VariationIndex

Index of the variation (style) within the base section, e.g. the hairstyle number.

### ColorIndex

Index of the color variation, e.g. the hair color number.
