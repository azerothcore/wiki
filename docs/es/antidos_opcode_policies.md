# antidos_opcode_policies

[<-Voler a:World](database-world)

**Estructura**

This table contains the policy definition for opcodes.

| Campo                               | Tipo     | Atributos | Llave | Null | Por defecto | Extra | Comentario |
| ----------------------------------- | -------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [Opcode](#opcode)                   | SMALLINT | UNSIGNED  | PRI   | NO   |             |       |            |
| [Policy](#policy)                   | TINYINT  | UNSIGNED  |       | NO   |             |       |            |
| [MaxAllowedCount](#maxallowedcount) | SMALLINT | UNSIGNED  |       | NO   |             |       |            |

**Descripciones de campos**

### Opcode

El ID del código de operación.

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

Cantidad máxima de paquetes que se pueden enviar a través del código de operación.
