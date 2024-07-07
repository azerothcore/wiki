# item\_template\_locale

[<-Back-to:World](database-world)

**The \`item\_template\_locale\` table**

This table is used to provide to localized clients with localized string for items.

**Table Structure**

| Field                               | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)                     | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [name_loc1](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc2](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc3](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc4](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc5](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc6](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc7](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc8](#nameloc)               | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [description_loc1](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc2](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc3](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc4](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc5](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc6](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc7](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |
| [description_loc8](#descriptionloc) | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

**Description of the fields**

### entry

This entry must be the same as  [item\_template.entry](item_template#entry) and then the row will be used to provide localization support for this creature record.

### name_loc

Translated content for [item\_template.name](item_template#name) field for language X.
See localization languages list to know which value to use for X.

### description_loc

Translated content for  [item\_template.description](item_template#description) field for language X.
See localization languages list to know which value to use for X.
