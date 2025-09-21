# command

[<-Volver a:World](database-world)

**Tabla `command`**

Contiene información de ayuda y seguridad para los comandos. Esta tabla no crea nuevos comandos; solo establece o anula la seguridad y proporciona ayuda.

**Estructura**

| Campo         | Tipo        | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ------------- | ----------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [name][1]     | VARCHAR(50) | SIGNED    | PRI   | NO   | NULL        |       |            |
| [security][2] | TINYINT     | UNSIGNED  |       | NO   | 0           |       |            |
| [help][3]     | longtext    | SIGNED    |       | YES  | NULL        |       |            |

[1]: #name
[2]: #security
[3]: #help

**Descripción de los campos**

### name

El nombre del comando. Véase: [comandos incluidos](gm-commands)

### security

El nivel de seguridad necesario para usar el comando. Corresponde con account_access.gmlevel en la base de datos del dominio.

### help

El texto de ayuda mostrado por el comando .help.
