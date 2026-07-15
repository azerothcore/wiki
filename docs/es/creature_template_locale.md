# creature_template_locale

[<-Volver a: World](database-world)

**Tabla \`creature_template_locale\`**

Esta tabla se usa para proporcionar a los clientes localizados las cadenas localizadas de las criaturas.

**Estructura**

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

**Descripción de los campos**

### entry

Este entry debe ser el mismo que creature_template.entry, y entonces la fila se usará para proporcionar soporte de localización para este registro de criatura.

### name_loc

Contenido traducido del campo [creature_template.name](creature_template#name) para el idioma X.

### subname_loc

Contenido traducido del campo creature_template.subname para el idioma X.
