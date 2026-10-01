# spell\_group\_stack\_rules

[<-Volver a: World](database-world)

**Tabla \`spell\_group\_stack\_rules\`**

Tabla que define si las auras de un mismo spell\_group no pueden apilarse entre sí.

Notas: La tabla no afecta al apilamiento de auras de área persistentes ni al apilamiento de auras pasivas (siempre pueden apilarse) ni a los hechizos que pertenecen al mismo spell\_rank (siempre están sujetos a la regla SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE)

**Estructura**

| Field                       | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [group\_id](#groupid)       | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [stack\_rule](#stackrule)   | TINYINT      | SIGNED     |     | NO   | 0       |       |         |
| [description](#description) | VARCHAR(150) |            |     | NO   |         |       |         |

**Descripción de los campos**

### group\_id

Id del grupo en la tabla [spell\_group](spell_group#id). El spell\_group puede contener otros spell\_groups dentro; si es así, la regla de apilamiento debe definirse para esos grupos por separado.

### stack\_rule

Enum SpellGroupStackFlags en el core:

| Id  |       | Stack Rule Name                              | Description                                  |
| --- | ----- | -------------------------------------------- | -------------------------------------------- |
| 0   | 0x00  | SPELL\_GROUP\_STACK\_RULE\_DEFAULT           | No stacking rule defined - placeholder       |
| 1   | 0x01  | SPELL\_GROUP\_STACK\_RULE\_EXCLUSIVE         | Auras from group can't stack with each other |
| 2   | 0x02  | SPELL\_GROUP\_STACK\_FLAG\_NOT\_SAME\_CASTER |                                              |
| 4   | 0x04  | SPELL\_GROUP\_STACK\_FLAG\_FLAGGED           |                                              |
| 8   | 0x08  | SPELL\_GROUP\_STACK\_FLAG\_NEVER\_STACK      |                                              |
| 10  | 0x10  | SPELL\_GROUP\_STACK\_FLAG\_EFFECT\_EXCLUSIVE |                                              |
| 20  | 0x20  | SPELL\_GROUP\_STACK\_FLAG\_MAX               |                                              |
|     |       | // Internal use                              |                                              |
| 100 | 0x100 | SPELL\_GROUP\_STACK\_FLAG\_FORCED\_STRONGEST |                                              |
| 200 | 0x200 | SPELL\_GROUP\_STACK\_FLAG\_FORCED\_WEAKEST   |                                              |

### description

Una breve descripción de qué tipo de hechizos hay en el grupo y qué regla se aplica.
