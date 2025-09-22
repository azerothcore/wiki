# creature_template_locale

[<-Volver a:World](database-world)

**Tabla \`creature_template_locale\`**

Esta tabla se utiliza para proporcionar a los clientes localizados una cadena localizada para las criaturas.

**Estructura**

| Campo                       | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| --------------------------- | ------------ | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [entry](#entry)             | MEDIUMINT    | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [name_loc1](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [name_loc2](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [name_loc3](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [name_loc5](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [name_loc6](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [name_loc7](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [name_loc8](#nameloc)       | VARCHAR(100) | SIGNED    |       | NO   | NULL        |       |            |
| [subname_loc1](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc2](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc3](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc4](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc5](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc6](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc7](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |
| [subname_loc8](#subnameloc) | VARCHAR(100) | SIGNED    |       | Si   | NULL        |       |            |

**Descripción de los campos**

### entry

Esta entrada debe ser la misma que creature_template.entry y luego la fila se utilizará para proporcionar soporte de localización para este registro de criatura.

### name_loc

Contenido traducido para el campo [creature_template.name](creature_template#name) para el idioma X.

### subname_loc

Contenido traducido para el campo creature_template.subname para el idioma X.
