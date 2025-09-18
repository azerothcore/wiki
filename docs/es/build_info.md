# build\_info

[<-Volver a:Auth](database-auth)

**Tabla \`build\_info\`**

**Estructura**

| Campo                 | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra | Comentario    |
| --------------------- | ------------ | --------- | ----- | ---- | ----------- | ----- |-------------- |
| [build][1]            | INT          | SIGNED    | PRI   | NO   |             |       | Identificador |
| [majorVersion][2]     | INT          | SIGNED    |       | YES  |             |       |               |
| [minorVersion][3]     | INT          | SIGNED    |       | YES  |             |       |               |
| [bugfixVersion][4]    | INT          | SIGNED    |       | YES  |             |       |               |
| [hotfixVersion][5]    | CHAR(3)      | SIGNED    |       | YES  |             |       |               |
| [winAuthSeed][6]      | VARCHAR(32)  | SIGNED    |       | YES  |             |       |               |
| [win64AuthSeed][7]    | VARCHAR(32)  | SIGNED    |       | YES  |             |       |               |
| [mac64AuthSeed][8]    | VARCHAR(32)  | SIGNED    |       | YES  |             |       |               |
| [winChecksumSeed][9]  | VARCHAR(40)  | SIGNED    |       | YES  |             |       |               |
| [macChecksumSeed][10] | VARCHAR(40)  | SIGNED    |       | YES  |             |       |               |

[1]: #build
[2]: #majorversion
[3]: #minorversion
[4]: #bugfixversion
[5]: #hotfixversion
[6]: #winauthseed
[7]: #win64authseed
[8]: #mac64authseed
[9]: #winchecksumseed
[10]: #macchecksumseed

**Descripción de los campos**

### build

El build del cliente.

### majorVersion

`campo-sin-descripción|2`

### minorVersion

`campo-sin-descripción|3`

### bugfixVersion

`campo-sin-descripción|4`

### hotfixVersion

`campo-sin-descripción|5`

### winAuthSeed

`campo-sin-descripción|6`

### win64AuthSeed

`campo-sin-descripción|7`

### mac64AuthSeed

`campo-sin-descripción|8`

### winChecksumSeed

`campo-sin-descripción|9`

### macChecksumSeed

`campo-sin-descripción|10`
