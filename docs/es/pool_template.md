# pool\_template

[<-Volver a:World](database-world)

**Tabla \`pool\_template\`**

Cada pool único se define en esta tabla.

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                               |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------------- |
| [entry][1]       | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       | Entry del pool                        |
| [max_limit][2]   | INT          | UNSIGNED   |     | NO   | 0       |       | Número máximo de objetos (0) sin límite |
| [description][3] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |                                       |

[1]: #entry
[2]: #max_limit
[3]: #description

**Descripción de los campos**

### entry

El ID del pool. Es un número arbitrario que solo se usa para enlazar los gameobjects, creatures o quests de este pool.

### max\_limit

Este es el número máximo de objetos que deberían aparecer en este pool.
0 significa sin límite.

### description

Campo que describe la información básica sobre a qué se refiere el pool. Ejemplo: Snarlflare (14272)
