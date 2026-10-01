# antidos_opcode_policies

[<-返回:World](database-world)

**表结构**

此表包含 opcode 的策略定义。

| Field                               | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [Opcode](#opcode)                   | SMALLINT | UNSIGNED   | PRI | NO   |         |       |         |
| [Policy](#policy)                   | TINYINT  | UNSIGNED   |     | NO   |         |       |         |
| [MaxAllowedCount](#maxallowedcount) | SMALLINT | UNSIGNED   |     | NO   |         |       |         |

**字段描述**

### Opcode

Opcode ID。

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

允许通过该 opcode 发送的最大数据包数量。
