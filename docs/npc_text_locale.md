# npc_text_locale

[<-Back-to:World](database-world)

**The \`npc_text_locale\` table**

This table is used to provide localized clients with localized strings for npc_texts.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 |  |  |
| [Locale](#locale) | VARCHAR(4) |  | PRI | NO |  |  |  |
| [Text0_0](#text0_0) | TEXT |  |  | YES |  |  |  |
| [Text0_1](#text0_1) | TEXT |  |  | YES |  |  |  |
| [Text1_0](#text1_0) | TEXT |  |  | YES |  |  |  |
| [Text1_1](#text1_1) | TEXT |  |  | YES |  |  |  |
| [Text2_0](#text2_0) | TEXT |  |  | YES |  |  |  |
| [Text2_1](#text2_1) | TEXT |  |  | YES |  |  |  |
| [Text3_0](#text3_0) | TEXT |  |  | YES |  |  |  |
| [Text3_1](#text3_1) | TEXT |  |  | YES |  |  |  |
| [Text4_0](#text4_0) | TEXT |  |  | YES |  |  |  |
| [Text4_1](#text4_1) | TEXT |  |  | YES |  |  |  |
| [Text5_0](#text5_0) | TEXT |  |  | YES |  |  |  |
| [Text5_1](#text5_1) | TEXT |  |  | YES |  |  |  |
| [Text6_0](#text6_0) | TEXT |  |  | YES |  |  |  |
| [Text6_1](#text6_1) | TEXT |  |  | YES |  |  |  |
| [Text7_0](#text7_0) | TEXT |  |  | YES |  |  |  |
| [Text7_1](#text7_1) | TEXT |  |  | YES |  |  |  |

**Description of the fields**

### ID

This must match [npc_text.ID](npc_text#id).

### Locale

The locale (language code) for this row. There is one row per non-default locale, so a single record can have up to 8 translated variants here. Valid values: `koKR`, `frFR`, `deDE`, `zhCN`, `zhTW`, `esES`, `esMX`, `ruRU`. The default `enUS` text is stored in the base table, not here.

### Text0_0 to Text7_1

Translated variants of the corresponding [npc_text](npc_text) `textN_0` / `textN_1` columns for this locale.
