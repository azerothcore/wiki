# creature\_questender

[<-Volver a: World](database-world)

**Tabla \`creature\_questender\`**

Contiene las relaciones de NPCs que finalizan misiones: qué NPCs finalizan qué misiones.

**Estructura**

| Field      | Type      | Attributes | Key | Null | Default | Extra | Comment          |
| ---------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------- |
| [id][1]    | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Identifier       |
| [quest][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Quest Identifier |

[1]: #id
[2]: #quest

**Descripción de los campos**

### id

El ID de la criatura. Véase [creature\_template.entry](creature_template#entry)

### quest

El ID de la misión que la criatura finaliza. Véase [quest\_template.id](quest_template#id)
