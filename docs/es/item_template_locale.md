# item\_template\_locale

[<-Volver a: World](database-world)

**Tabla \`item\_template\_locale\`**

Esta tabla se usa para proporcionar a los clientes localizados cadenas localizadas para los objetos.

**Estructura**

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

**Descripción de los campos**

### entry

Este entry debe ser el mismo que [item\_template.entry](item_template#entry) y entonces la fila se usará para proporcionar soporte de localización para este registro de objeto.

### name_loc

Contenido traducido del campo [item\_template.name](item_template#name) para el idioma X.
Consulta la lista de idiomas de localización para saber qué valor usar para X.

### description_loc

Contenido traducido del campo [item\_template.description](item_template#description) para el idioma X.
Consulta la lista de idiomas de localización para saber qué valor usar para X.
