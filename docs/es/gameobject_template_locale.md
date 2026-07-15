# gameobject_template_locale

[<-Volver a: World](database-world)

**Tabla \`gameobject_template_locale\`**

Esta tabla se usa para proporcionar a los clientes localizados cadenas localizadas para los gameobjects.

**Estructura**

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

**Descripción de los campos**

### entry

Este entry debe ser el mismo que [gameobject_template.entry](gameobject_template#entry) y entonces la fila se usará para proporcionar soporte de localización para este registro de gameobject.

### name_loc

Contenido traducido del campo [gameobject_template.name](gameobject_template#name) para el idioma X.

### castbarcaption_loc

Contenido traducido del campo [gameobject_template.castBarCaption](gameobject_template#castbarcaption) para el idioma X.
