# skill\_fishing\_base\_level

[<-Volver a:World](database-world)

**Tabla \`skill\_fishing\_base\_level\`**

Esta tabla controla el nivel de skill mínimo requerido en pesca para pescar en una zona determinada.

**Estructura**

| Field      | Type         | Attributes | Key | Null | Default | Extra | Comment                      |
|------------|--------------|------------|-----|------|---------|-------|------------------------------|
| [entry][1] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Area identifier              |
| [skill][2] | SMALLINT  | SIGNED     |     | NO   | 0       |       | Base skill level requirement |

[1]: #entry
[2]: #skill

**Descripción de los campos**

### entry

El ID de la zona, ver [AreaTable.dbc](areatable).

### skill

Los puntos de skill mínimos en pesca requeridos para pescar en la zona.
