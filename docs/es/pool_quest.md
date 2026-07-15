# pool\_quest

[<-Volver a:World](database-world)

**Tabla \`pool\_quest\`**

Esta tabla contiene una lista de quests que están ligadas a un pool concreto.

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]       | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [pool_entry][2]  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [description][3] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #entry
[2]: #pool_entry
[3]: #description

**Descripción de los campos**

### entry

[id](quest_template#id) de la quest.

### pool\_entry

El [pool](pool_template#entry) en el que está esta quest. Se refiere a [pool\_template entry](pool_template#entry).

### description

Una descripción o comentario legible para esta entrada de quest del pool.
