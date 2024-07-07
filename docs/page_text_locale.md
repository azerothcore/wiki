# page\_text\_locale

[<-Back-to:World](database-world)

**The \`page\_text\_locale\` table**

This table is used to provide localized clients with localized string for page\_texts.

**Table Structure**

| Field                          | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)              | longtext  | SIGNED     |     | YES  | NULL    |       |         |
| [Name](#name) | longtext  | SIGNED     |     | YES  | NULL    |       |         |

**Description of the fields**

### ID

This entry must be the same as  [page\_text.entry](#page_text#entry) and then the row will be used to provide localization support for this page\_text record.

### locale

`field-no-description|2`

### Name

Translated content for [page\_text.text](#page_text#text) field for language X.
