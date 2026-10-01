# warden\_checks

[<-Volver a: World](database-world)

**Tabla \`warden\_checks\`**

Esta tabla contiene datos relacionados con el uso de la herramienta anti-cheat Warden, que se puede activar en Worldserver.conf

**Estructura**

| Field                             | Type        | Attributes | Key | NULL | Default         | Comment                                   |
| --------------------------------- | ----------- | ---------- | --- | ---- | --------------- | ----------------------------------------- |
| [id](#id)                         | SMALLINT    | UNSIGNED   | PRI | NO   | auto\_increment | Unique ID, automatically incremented by 1 |
| [type](#type)                     | TINYINT     | UNSIGNED   |     | YES  | NULL            |                                           |
| [data](#data)                     | VARCHAR(48) |            |     | YES  | NULL            |                                           |
| [str](#str)                       | VARCHAR(20) |            |     | YES  | NULL            |                                           |
| [address](#address)               | INT         | UNSIGNED   |     | YES  | NULL            |                                           |
| [length](#length)                 | TINYINT     | UNSIGNED   |     | YES  | NULL            |                                           |
| [result](#result)                 | VARCHAR(24) |            |     | YES  | NULL            |                                           |
| [comment](#comment)               | VARCHAR(50) |            |     | YES  | NULL            |                                           |

**Descripción de los campos:**

### id

ID único, incrementado automáticamente en 1

### type

`campo-sin-descripción|2`

### data

`campo-sin-descripción|3`

### str

`campo-sin-descripción|4`

### address

`campo-sin-descripción|5`

### length

`campo-sin-descripción|6`

### result

`campo-sin-descripción|7`

### comment

`campo-sin-descripción|8` 
