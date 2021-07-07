# account

[<-Volver a:Auth](database-auth.md)

**Tabla \`build_info\`**

**Estructura**

| Field                 | Type         | Attributes | Key | Null | Default           | Extra          | Comment    |
|-----------------------|--------------|------------|-----|------|-------------------|----------------|------------|
| [build][1]            | INT          |            | PRI | NO   |                   |                | Identifier |
| [majorVersion][2]     | INT          |            |     | YES  | NULL              |                |            |
| [minorVersion][3]     | INT          |            |     | YES  | NULL              |                |            |
| [bugfixVersion][4]    | INT          |            |     | YES  | NULL              |                |            |
| [hotfixVersion][5]    | CHAR(3)      |            |     | YES  | NULL              |                |            |
| [winAuthSeed][6]      | VARCHAR(32)  |            |     | YES  | NULL              |                |            |
| [win64AuthSeed][7]    | VARCHAR(32)  |            |     | YES  | NULL              |                |            |
| [mac64AuthSeed][8]    | VARCHAR(32)  |            |     | YES  | NULL              |                |            |
| [winChecksumSeed][9]  | VARCHAR(40)  |            |     | YES  | NULL              |                |            |
| [macChecksumSeed][10] | VARCHAR(40)  |            |     | YES  | NULL              |                |            |

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

## Descripción de los campos

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