# command

[<-Volver a: World](database-world)

**Tabla `command`**

Contiene información de ayuda y de seguridad para los comandos. Esta tabla NO crea comandos nuevos, solo establece / sobrescribe la seguridad y proporciona la ayuda.

**Estructura**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [name][1]     | VARCHAR(50) | SIGNED     | PRI | NO   | NULL    |       |         |
| [security][2] | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [help][3]     | longtext    | SIGNED     |     | YES  | NULL    |       |         |

[1]: #name
[2]: #security
[3]: #help

**Descripción de los campos**

### name

El nombre del comando. Ver: [comandos incluidos](gm-commands)

### security

El nivel de seguridad requerido para usar el comando. Se corresponde con account_access.gmlevel en la base de datos del realm.

### help

El texto de ayuda que muestra el comando .help.
