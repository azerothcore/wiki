# creature_template_locale

[<-Back-to:World](database-world)

**The \`creature_template_locale\` table**

This table is used to provide to localized clients with localized string for creatures.

**Table Structure**

| Field                       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)             | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [name_loc1](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc2](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc3](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc5](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc6](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc7](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc8](#nameloc)       | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [subname_loc1](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc2](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc3](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc4](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc5](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc6](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc7](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |
| [subname_loc8](#subnameloc) | VARCHAR(100) | SIGNED     |     | YES  | NULL    |       |         |

**Description of the fields**

### entry

This entry must be the same as creature_template.entry and then the row will be used to provide localization support for this creature record.

### name_loc

Translated content for [creature_template.name](creature_template#name) field for language X.

### subname_loc

Translated content for creature_template.subname field for language X.
