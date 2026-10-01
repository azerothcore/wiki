# antidos_opcode_policies

[<-Volver a: World](database-world)

**Estructura**

Esta tabla contiene la definición de la política para los opcodes.

| Field                               | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Opcode](#opcode)                   | SMALLINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Policy](#policy)                   | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [MaxAllowedCount](#maxallowedcount) | SMALLINT | UNSIGNED   |     | NO   |         |       |         |

**Descripción de los campos**

### Opcode

El ID del opcode.

### Policy

| Value | Policy           |
| ----- | ---------------- |
| 0     | Process          |
| 1     | Kick             |
| 2     | Ban              |
| 3     | Log              |
| 4     | BlockingThrottle |
| 5     | DropPacket       |

### MaxAllowedCount

Cantidad máxima de paquetes que se permite enviar a través del opcode.
