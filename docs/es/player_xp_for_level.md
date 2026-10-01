# player\_xp\_for\_level

[<-Volver a:World](database-world)

**Tabla \`player\_xp\_for\_level\`**

Incluye información sobre cuánta experiencia se necesita para el siguiente nivel. Proviene de sniffs.

**Estructura**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Level][1]      | TINYINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [Experience][2] | INT     | UNSIGNED   |     | NO   | NULL    |       |         |

[1]: #level
[2]: #experience

**Descripción de los campos**

Esta tabla establece los puntos de experiencia necesarios para subir el nivel del jugador.

### Level

El nivel del jugador.

### Experience

La experiencia necesaria para subir del valor del campo "lvl" a "lvl" +1.

### Example

| Level | Experience |
| ----- | ---------- |
| 1     | 400        |
| 2     | 900        |
| 3     | 1400       |
| 4     | 2100       |
| 5     | 2800       |
