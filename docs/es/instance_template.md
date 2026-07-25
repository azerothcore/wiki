# instance\_template

[<-Volver a:World](database-world)

**Tabla \`instance\_template\`**

Esta tabla tiene todas las plantillas de cada instancia. Cuando un grupo entra en una instancia, se crea una nueva copia de esa instancia a partir de los valores de estos campos.

Si quieres cambiar el punto en el que apareces al entrar/salir de una instancia, ve a areatrigger\_teleport

**Estructura**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [map][1]        | INT          | UNSIGNED   |     | NO   | NULL    |       |         |
| [parent][2]     | BIGINT       | UNSIGNED   |     | NO   | 0       |       |         |
| [script][3]     | VARCHAR(128) | SIGNED     |     | NO   | NULL    |       |         |
| [allowMount][4] | tinyiny(1)   | SIGNED     |     | NO   | 0       |       |         |

[1]: #map
[2]: #parent
[3]: #script
[4]: #allowmount

**Descripción de los campos**

### map

El ID del mapa de la instancia. Ver Maps.dbc

### parent

Si la instancia es una subinstancia de otra instancia, este campo tiene el ID del mapa de la instancia padre.

### script

El nombre del script de instancia que la instancia usará y aplicará (si lo hay).

### allowMount

- 0 = no puedes montar dentro de esta instancia
- 1 = puedes montar dentro de esta instancia
