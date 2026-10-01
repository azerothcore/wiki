# charsections\_dbc

[`Back-to:DBC`](dbc-index)

**The \`charsections\_dbc\` table**

This DBC contains the character customization sections (skin, face, facial hair, hair and underwear textures) available for each race/sex combination on the character creation and barbershop screens.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)

**Table Structure**

| Field                 | Type | Attributes | Key | Null | Default | Extra | Comment           |
| --------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ----------------- |
| [ID][1]                | INT  | SIGNED     | PRI | NO   | 0       |       | Unique ID         |
| [RaceID][2]            | INT  | SIGNED     |     | NO   | 0       |       |                   |
| [SexID][3]             | INT  | SIGNED     |     | NO   | 0       |       |                   |
| [BaseSection][4]       | INT  | SIGNED     |     | NO   | 0       |       | CharSectionType   |
| TextureName_1          | TEXT |            |     | YES  | NULL    |       | Not used server-side |
| TextureName_2          | TEXT |            |     | YES  | NULL    |       | Not used server-side |
| TextureName_3          | TEXT |            |     | YES  | NULL    |       | Not used server-side |
| [Flags][5]             | INT  | SIGNED     |     | NO   | 0       |       | CharSectionFlags  |
| [VariationIndex][6]    | INT  | SIGNED     |     | NO   | 0       |       |                   |
| [ColorIndex][7]        | INT  | SIGNED     |     | NO   | 0       |       |                   |

[1]: #id
[2]: #raceid
[3]: #sexid
[4]: #basesection
[5]: #flags
[6]: #variationindex
[7]: #colorindex

**Description of the fields**

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
