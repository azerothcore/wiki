# map\_dbc

[<-Back-to:World](database-world)

**The \`map\_dbc\` table**

This table has the same columns as the client file `Map.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: map\_dbc's Structure**

| Field                                             | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                         | INT          |          | NO   | PRI | 0       |       |         |
| [Directory](#directory)                           | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [InstanceType](#instancetype)                     | INT          |          | NO   |     | 0       |       |         |
| [Flags](#flags)                                   | INT          |          | NO   |     | 0       |       |         |
| [PVP](#pvp)                                       | INT          |          | NO   |     | 0       |       |         |
| [MapName_Lang_enUS](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_enGB](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_koKR](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_frFR](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_deDE](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_enCN](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_zhCN](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_enTW](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_zhTW](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_esES](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_esMX](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_ruRU](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_ptPT](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_ptBR](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_itIT](#mapnamelang)                 | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_Unk](#mapnamelang)                  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapName_Lang_Mask](#mapnamelang)                 | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [AreaTableID](#areatableid)                       | INT          |          | NO   |     | 0       |       |         |
| [MapDescription0_Lang_enUS](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_enGB](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_koKR](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_frFR](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_deDE](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_enCN](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_zhCN](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_enTW](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_zhTW](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_esES](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_esMX](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_ruRU](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_ptPT](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_ptBR](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_itIT](#mapdescription0lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_Unk](#mapdescription0lang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapDescription0_Lang_Mask](#mapdescription0lang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [MapDescription1_Lang_enUS](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_enGB](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_koKR](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_frFR](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_deDE](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_enCN](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_zhCN](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_enTW](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_zhTW](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_esES](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_esMX](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_ruRU](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_ptPT](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_ptBR](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_itIT](#mapdescription1lang) | TEXT         |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_Unk](#mapdescription1lang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [MapDescription1_Lang_Mask](#mapdescription1lang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [LoadingScreenID](#loadingscreenid)               | INT          |          | NO   |     | 0       |       |         |
| [MinimapIconScale](#minimapiconscale)             | FLOAT        |          | NO   |     | 0       |       |         |
| [CorpseMapID](#corpsemapid)                       | INT          |          | NO   |     | 0       |       |         |
| [CorpseX](#corpsex)                               | FLOAT        |          | NO   |     | 0       |       |         |
| [CorpseY](#corpsey)                               | FLOAT        |          | NO   |     | 0       |       |         |
| [TimeOfDayOverride](#timeofdayoverride)           | INT          |          | NO   |     | 0       |       |         |
| [ExpansionID](#expansionid)                       | INT          |          | NO   |     | 0       |       |         |
| [RaidOffset](#raidoffset)                         | INT          |          | NO   |     | 0       |       |         |
| [MaxPlayers](#maxplayers)                         | INT          |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `MapEntry::MapID`.

### Directory

Not used by the core.

### InstanceType

The core reads this column into `MapEntry::map_type`.

### Flags

The core reads this column into `MapEntry::Flags`.

### PVP

Not used by the core.

### MapName\_Lang

The core reads `MapName_Lang_enUS` to `MapName_Lang_Unk` into `MapEntry::name`. `MapName_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `MapName_Lang_enUS` = enUS, `MapName_Lang_enGB` = koKR, `MapName_Lang_koKR` = frFR, `MapName_Lang_frFR` = deDE, `MapName_Lang_deDE` = zhCN, `MapName_Lang_enCN` = zhTW, `MapName_Lang_zhCN` = esES, `MapName_Lang_enTW` = esMX, `MapName_Lang_zhTW` = ruRU. The remaining text columns, `MapName_Lang_esES` to `MapName_Lang_Unk`, are not supported in 3.3.5a and are not used.

### AreaTableID

The core reads this column into `MapEntry::linked_zone`.

Comment in the core source: "common zone for instance and continent map"

### MapDescription0\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `MapDescription0_Lang_enUS` = enUS, `MapDescription0_Lang_enGB` = koKR, `MapDescription0_Lang_koKR` = frFR, `MapDescription0_Lang_frFR` = deDE, `MapDescription0_Lang_deDE` = zhCN, `MapDescription0_Lang_enCN` = zhTW, `MapDescription0_Lang_zhCN` = esES, `MapDescription0_Lang_enTW` = esMX, `MapDescription0_Lang_zhTW` = ruRU. The remaining text columns, `MapDescription0_Lang_esES` to `MapDescription0_Lang_Unk`, are not supported in 3.3.5a and are not used.

Comment in the core source: "text for PvP Zones"

### MapDescription1\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `MapDescription1_Lang_enUS` = enUS, `MapDescription1_Lang_enGB` = koKR, `MapDescription1_Lang_koKR` = frFR, `MapDescription1_Lang_frFR` = deDE, `MapDescription1_Lang_deDE` = zhCN, `MapDescription1_Lang_enCN` = zhTW, `MapDescription1_Lang_zhCN` = esES, `MapDescription1_Lang_enTW` = esMX, `MapDescription1_Lang_zhTW` = ruRU. The remaining text columns, `MapDescription1_Lang_esES` to `MapDescription1_Lang_Unk`, are not supported in 3.3.5a and are not used.

Comment in the core source: "text for PvP Zones"

### LoadingScreenID

The core reads this column into `MapEntry::multimap_id`.

### MinimapIconScale

Not used by the core.

### CorpseMapID

The core reads this column into `MapEntry::entrance_map`.

Comment in the core source: "map_id of entrance map"

### CorpseX

The core reads this column into `MapEntry::entrance_x`.

Comment in the core source: "entrance x coordinate (if exist single entry)"

### CorpseY

The core reads this column into `MapEntry::entrance_y`.

Comment in the core source: "entrance y coordinate (if exist single entry)"

### TimeOfDayOverride

Not used by the core.

### ExpansionID

The core reads this column into `MapEntry::expansionID`.

Comment in the core source: "(0: Vanilla, 1:TBC, 2:WotLK)"

### RaidOffset

Not used by the core.

Comment in the core source: "some kind of time?"

### MaxPlayers

The core reads this column into `MapEntry::maxPlayers`.

Comment in the core source: "max players, fallback if not present in MapDifficulty.dbc"
