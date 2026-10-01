# playercreateinfo_cast_spell

[<-返回至:World](database-world)

**`playercreateinfo_cast_spell` 表**

定义在角色创建时立即施放的法术，按种族和职业位掩码过滤。此表是对 [playercreateinfo_spell_custom](playercreateinfo_spell_custom) 的补充，后者是将法术授予为*已知*状态，而不是施放它们。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [raceMask](#racemask) | INT | UNSIGNED |  | NO | 0 |  |  |
| [classMask](#classmask) | INT | UNSIGNED |  | NO | 0 |  |  |
| [spell](#spell) | INT | UNSIGNED |  | NO | 0 |  |  |
| [note](#note) | VARCHAR(255) |  |  | YES | (NULL) |  |  |

**字段说明**

### raceMask

此施放效果适用的种族位掩码（`0` = 所有种族）。

### classMask

此施放效果适用的职业位掩码（`0` = 所有职业）。

### spell

要在新建角色身上施放的法术 ID。

### note

该条目的可选自由文本描述。
