# npc\_text\_locale

[<-Back-to:World](database-world)

**The \`npc\_text\_locale\` table**

This table is used to provide localized clients with localized strings for npc_texts.

**Table: npc\_text\_locale's Structure**

| Field                        | Type       |          | Null | Key | Default | Extra | Comment |
| :--------------------------- | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                    | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [Locale](#locale)            | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Text0_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text0_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text1_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text1_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text2_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text2_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text3_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text3_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text4_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text4_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text5_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text5_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text6_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text6_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text7_0](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |
| [Text7_1](#text00-to-text71) | LONGTEXT   |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

This must match [npc_text.ID](npc_text#id).

### Locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Text0_0 to Text7_1

Translated variants of the corresponding [npc_text](npc_text) `textN_0` / `textN_1` columns for this locale.
