# linked\_respawn

[<-Volver a:World](database-world)

**Tabla \`linked\_respawn\`**

Esta tabla enlaza los mobs de relleno (trash) con los jefes para que, si matas al jefe, el trash no reaparezca antes de que se reinicie la instancia.
¡Los gameobjects también se pueden enlazar!

**Estructura**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment            |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [guid][1]       | INT     | UNSIGNED   | PRI | NO   |         |       | Dependent Creature |
| [linkedGuid][2] | INT     | UNSIGNED   |     | NO   |         |       | Master Creature    |
| [linkType][3]   | TINYINT | UNSIGNED   |     | NO   | 0       |       |                    |

[1]: #guid
[2]: #linkedguid
[3]: #linktype

**Descripción de los campos**

### guid

Este es el guid de la [creature](creature#guid) o [gameobject](gameobject#guid) que quieres enlazar.

### linkedGuid

Este es el guid de la [creature](creature#guid) o [gameobject](gameobject#guid) (lo más probable es que sea el jefe) al que quieres enlazar.

### linkedType

| Value | Dependent  | Master     |
| ----- | ---------- | ---------- |
| 0     | creature   | creature   |
| 1     | creature   | gameobject |
| 2     | gameobject | gameobject |
| 3     | gameobject | creature   |
