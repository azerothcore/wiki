# areatable\_dbc

[<-Back-to:World](database-world)

**The \`areatable\_dbc\` table**

This table has the same columns as the client file `AreaTable.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: areatable\_dbc's Structure**

| Field                                                       | Type         |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                                   | INT          |          | NO   | PRI | 0       |       |         |
| [ContinentID](#continentid)                                 | INT          |          | NO   |     | 0       |       |         |
| [ParentAreaID](#parentareaid)                               | INT          |          | NO   |     | 0       |       |         |
| [AreaBit](#areabit)                                         | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                                             | INT          |          | NO   |     | 0       |       |         |
| [SoundProviderPref](#soundproviderpref)                     | INT          |          | NO   |     | 0       |       |         |
| [SoundProviderPrefUnderwater](#soundproviderprefunderwater) | INT          |          | NO   |     | 0       |       |         |
| [AmbienceID](#ambienceid)                                   | INT          |          | NO   |     | 0       |       |         |
| [ZoneMusic](#zonemusic)                                     | INT          |          | NO   |     | 0       |       |         |
| [IntroSound](#introsound)                                   | INT          |          | NO   |     | 0       |       |         |
| [ExplorationLevel](#explorationlevel)                       | INT          |          | NO   |     | 0       |       |         |
| [AreaName_Lang_enUS](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_enGB](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_koKR](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_frFR](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_deDE](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_enCN](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_zhCN](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_enTW](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_zhTW](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_esES](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_esMX](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_ruRU](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_ptPT](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_ptBR](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_itIT](#areanamelang)                         | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_Unk](#areanamelang)                          | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [AreaName_Lang_Mask](#areanamelang)                         | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [FactionGroupMask](#factiongroupmask)                       | INT          |          | NO   |     | 0       |       |         |
| [LiquidTypeID_1](#liquidtypeid)                             | INT          |          | NO   |     | 0       |       |         |
| [LiquidTypeID_2](#liquidtypeid)                             | INT          |          | NO   |     | 0       |       |         |
| [LiquidTypeID_3](#liquidtypeid)                             | INT          |          | NO   |     | 0       |       |         |
| [LiquidTypeID_4](#liquidtypeid)                             | INT          |          | NO   |     | 0       |       |         |
| [MinElevation](#minelevation)                               | FLOAT        |          | NO   |     | 0       |       |         |
| [Ambient_Multiplier](#ambientmultiplier)                    | FLOAT        |          | NO   |     | 0       |       |         |
| [Lightid](#lightid)                                         | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `AreaTableEntry::ID`.

### ContinentID

The core reads this column into `AreaTableEntry::mapid`.

### ParentAreaID

The core reads this column into `AreaTableEntry::zone`.

Comment in the core source: "if 0 then it's zone, else it's zone id of this area"

### AreaBit

The core reads this column into `AreaTableEntry::exploreFlag`.

Comment in the core source: "main index"

### Flags

The core reads this column into `AreaTableEntry::flags`.

Comment in the core source: "unknown value but 312 for all cities"

### SoundProviderPref

Not used by the core.

### SoundProviderPrefUnderwater

Not used by the core.

### AmbienceID

Not used by the core.

### ZoneMusic

Not used by the core.

### IntroSound

Not used by the core.

### ExplorationLevel

The core reads this column into `AreaTableEntry::area_level`.

### AreaName\_Lang

The core reads `AreaName_Lang_enUS` to `AreaName_Lang_Unk` into `AreaTableEntry::area_name`. `AreaName_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `AreaName_Lang_enUS` = enUS, `AreaName_Lang_enGB` = koKR, `AreaName_Lang_koKR` = frFR, `AreaName_Lang_frFR` = deDE, `AreaName_Lang_deDE` = zhCN, `AreaName_Lang_enCN` = zhTW, `AreaName_Lang_zhCN` = esES, `AreaName_Lang_enTW` = esMX, `AreaName_Lang_zhTW` = ruRU. The remaining text columns, `AreaName_Lang_esES` to `AreaName_Lang_Unk`, are not supported in 3.3.5a and are not used.

### FactionGroupMask

The core reads this column into `AreaTableEntry::team`.

### LiquidTypeID

The core reads these columns into `AreaTableEntry::LiquidTypeOverride`.

Comment in the core source: "liquid override by type"

### MinElevation

Not used by the core.

### Ambient\_Multiplier

Not used by the core.

### Lightid

Not used by the core.
