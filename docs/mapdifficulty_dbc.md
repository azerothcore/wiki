# mapdifficulty\_dbc

[<-Back-to:World](database-world)

**The \`mapdifficulty\_dbc\` table**

This table has the same columns as the client file `MapDifficulty.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: mapdifficulty\_dbc's Structure**

| Field                                 | Type         |          | Null | Key | Default | Extra | Comment |
| :------------------------------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                             | INT          |          | NO   | PRI | 0       |       |         |
| [MapID](#mapid)                       | INT          |          | NO   |     | 0       |       |         |
| [Difficulty](#difficulty)             | INT          |          | NO   |     | 0       |       |         |
| [Message_Lang_enUS](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_enGB](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_koKR](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_frFR](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_deDE](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_enCN](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_zhCN](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_enTW](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_zhTW](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_esES](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_esMX](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_ruRU](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_ptPT](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_ptBR](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_itIT](#messagelang)     | VARCHAR(200) |          | YES  |     | NULL    |       |         |
| [Message_Lang_Unk](#messagelang)      | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Message_Lang_Mask](#messagelang)     | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [RaidDuration](#raidduration)         | INT          |          | NO   |     | 0       |       |         |
| [MaxPlayers](#maxplayers)             | INT          |          | NO   |     | 0       |       |         |
| [Difficultystring](#difficultystring) | VARCHAR(100) |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### MapID

The core reads this column.

### Difficulty

The core reads this column.

### Message\_Lang

The core reads `Message_Lang_enUS`. `Message_Lang_enGB` to `Message_Lang_Mask` are not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Message_Lang_enUS` = enUS, `Message_Lang_enGB` = koKR, `Message_Lang_koKR` = frFR, `Message_Lang_frFR` = deDE, `Message_Lang_deDE` = zhCN, `Message_Lang_enCN` = zhTW, `Message_Lang_zhCN` = esES, `Message_Lang_enTW` = esMX, `Message_Lang_zhTW` = ruRU. The remaining text columns, `Message_Lang_esES` to `Message_Lang_Unk`, are not supported in 3.3.5a and are not used.

### RaidDuration

The core reads this column.

### MaxPlayers

The core reads this column.

### Difficultystring

Not used by the core.
