# game\_event\_npcflag

[<-Volver a:World](database-world)

**Tabla \`game\_event\_npcflag\`**

Esta tabla contiene npcflags que se van a añadir a un NPC cuando el evento indicado está activo para la creature con el guid dado.

**Estructura**

| Field           | Type      | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [eventEntry][1] | TINYINT   | UNSIGNED   | PRI | NO   |         |       | Entry del evento de juego |
| [guid][2]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                          |
| [npcflag][3]    | INT       | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #evententry
[2]: #guid
[3]: #npcflag

**Descripción de los campos**

### eventEntry

El eventEntry que está ligado a este cambio de npcflag.

### guid

El guid de la creature para la que quieres cambiar el npcflag.

### npcflag

Los npcflags que quieres establecer. El valor indicado aquí se añade bit a bit al npcflag ya establecido en el NPC.

Así que, si quieres que la creature sea también un dador de quests, simplemente pon 2 en esta columna.
