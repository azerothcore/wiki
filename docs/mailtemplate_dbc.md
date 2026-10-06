# mailtemplate\_dbc

[<-Back-to:World](database-world)

**The \`mailtemplate\_dbc\` table**

This table has the same columns as the client file `MailTemplate.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: mailtemplate\_dbc's Structure**

| Field                             | Type         |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                         | INT          |          | NO   | PRI | 0       |       |         |
| [Subject_Lang_enUS](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_enGB](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_koKR](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_frFR](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_deDE](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_enCN](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_zhCN](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_enTW](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_zhTW](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_esES](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_esMX](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_ruRU](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_ptPT](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_ptBR](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_itIT](#subjectlang) | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_Unk](#subjectlang)  | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Subject_Lang_Mask](#subjectlang) | INT          | UNSIGNED | NO   |     | 0       |       |         |
| [Body_Lang_enUS](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_enGB](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_koKR](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_frFR](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_deDE](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_enCN](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_zhCN](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_enTW](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_zhTW](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_esES](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_esMX](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_ruRU](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_ptPT](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_ptBR](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_itIT](#bodylang)       | VARCHAR(500) |          | YES  |     | NULL    |       |         |
| [Body_Lang_Unk](#bodylang)        | VARCHAR(100) |          | YES  |     | NULL    |       |         |
| [Body_Lang_Mask](#bodylang)       | INT          | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `MailTemplateEntry::ID`.

### Subject\_Lang

Not used by the core.

The text columns are the 16 locale slots of the file. They are ordered by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Subject_Lang_enUS` = enUS, `Subject_Lang_enGB` = koKR, `Subject_Lang_koKR` = frFR, `Subject_Lang_frFR` = deDE, `Subject_Lang_deDE` = zhCN, `Subject_Lang_enCN` = zhTW, `Subject_Lang_zhCN` = esES, `Subject_Lang_enTW` = esMX, `Subject_Lang_zhTW` = ruRU. The remaining text columns, `Subject_Lang_esES` to `Subject_Lang_Unk`, are not supported in 3.3.5a and are not used.

### Body\_Lang

The core reads `Body_Lang_enUS` to `Body_Lang_Unk` into `MailTemplateEntry::content`. `Body_Lang_Mask` is not used by the core.

The text columns are the 16 locale slots of the file. The core reads them by position, not by name. 3.3.5a supports only the nine locales in the core's `LocaleConstant` list, and they are the first nine columns: `Body_Lang_enUS` = enUS, `Body_Lang_enGB` = koKR, `Body_Lang_koKR` = frFR, `Body_Lang_frFR` = deDE, `Body_Lang_deDE` = zhCN, `Body_Lang_enCN` = zhTW, `Body_Lang_zhCN` = esES, `Body_Lang_enTW` = esMX, `Body_Lang_zhTW` = ruRU. The remaining text columns, `Body_Lang_esES` to `Body_Lang_Unk`, are not supported in 3.3.5a and are not used.
