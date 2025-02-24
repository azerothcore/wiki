# antidos_opcode_policies

[<-Back-to:World](database-world)

**Table Structure**

This table contains the policy definition for opcodes.

| Field                               | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Opcode](#opcode)                   | SMALLINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Policy](#policy)                   | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [MaxAllowedCount](#maxallowedcount) | SMALLINT | UNSIGNED   |     | NO   |         |       |         |

**Field Descriptions**

### Opcode

The opcode ID.

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

Max amount of packets allowed to be sent through the opcode.
