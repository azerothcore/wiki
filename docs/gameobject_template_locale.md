# gameobject_template_locale

[<-Back-to:World](database-world)

**The \`gameobject_template_locale\` table**

This table is used to provide to localized clients with localized string for gameobjects.

**Table Structure**

| Field                                     | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)                           | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [name_loc1](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc2](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc3](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc4](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc5](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc6](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc7](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [name_loc8](#nameloc)                     | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc1](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc2](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc3](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc4](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc5](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc6](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc7](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |
| [castbarcaption_loc8](#castbarcaptionloc) | VARCHAR(100) | SIGNED     |     | NO   | NULL    |       |         |

**Description of the fields**

### entry

This entry must be the same as  [gameobject_template.entry](gameobject_template#entry) and then the row will be used to provide localization support for this gameobject record.

### name_loc

Translated content for [gameobject_template.name](gameobject_template#name) field for language X.

### castbarcaption_loc

Translated content for  [gameobject_template.castBarCaption](gameobject_template#castbarcaption) field for language X.
