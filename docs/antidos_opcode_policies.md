# antidos\_opcode\_policies

[<-Back-to:World](database-world)

**Table: antidos\_opcode\_policies's Structure**

This table contains the policy definition for opcodes.

| Field                               | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [Opcode](#opcode)                   | SMALLINT | UNSIGNED | NO   | PRI |         |       |         |
| [Policy](#policy)                   | TINYINT  | UNSIGNED | NO   |     |         |       |         |
| [MaxAllowedCount](#maxallowedcount) | SMALLINT | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

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
