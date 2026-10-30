# acore\_string

[<-Back-to:World](database-world)

**The \`acore\_string\` table**

This table holds all of the strings used internally by the server. It is provided for the main purpose of translation.

To see which locale IDs correspond to what languages, visit the Localization\_lang page.

**Table: acore\_string's Structure**

| Field                              | Type |          | Null | Key | Default | Extra | Comment |
| :--------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)                    | INT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [content_default](#contentdefault) | TEXT |          | NO   |     |         |       |         |
| [locale_koKR](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_frFR](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_deDE](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_zhCN](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_zhTW](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_esES](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_esMX](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |
| [locale_ruRU](#localennnn)         | TEXT |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### entry

The ID that the core uses to identify a string. These IDs are contained and used internally and must correspond to what the core expects. The core will not operate if all IDs aren't in this table.

### content\_default

The English translation (locale ID 0).

### locale\_nnNN

The translation in another language depends on the locale name.
