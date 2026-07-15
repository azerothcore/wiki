# points\_of\_interest\_locale

[<-Volver a:World](database-world)

**Tabla \`locales\_points\_of\_interest\`**

`tabla-sin-descripción`

**Estructura**

| Field                           | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------- | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                       | INT        | UNSIGNED   | PRI | NO   | 0       |       |         |
| [locale](#locale)               | VARCHAR(4) |            |     |      |         |       |         |
| [Name](#name)                   | TEXT       |            |     | YES  | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild) | INT        |            |     | YES  | NULL    |       |         |

**Descripción de los campos**

### ID

`campo-sin-descripción|1`

### locale

`campo-sin-descripción|2`

### Name

`campo-sin-descripción|3`

### VerifiedBuild

### VerifiedBuild

Este campo se usa para determinar si los datos proceden de sniffs verificados.

Si el valor es 0 entonces aún no se ha parseado o se ha heredado de una BD más antigua o de otro Core.

Si el valor es mayor que 0 entonces se ha parseado con sniffs de esa build de cliente concreta.

Si el valor es -Client Build entonces se parseó con archivos WDB de esa build de cliente concreta y se editó manualmente después por alguna necesidad especial.
