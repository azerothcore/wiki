# pool\_pool

[<-Volver a:World](database-world)

**Tabla \`pool\_pool\`**

Esta es la tabla de pools de pools. Puedes crear un pool con una probabilidad de que se active un rango de pools dentro de ese pool.

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [pool_id][1]     | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [mother_pool][2] | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [chance][3]      | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [description][4] | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #pool_id
[2]: #mother_pool
[3]: #chance
[4]: #description

**Descripción de los campos**

### pool\_id

El ID del [pool\_template](pool_template)) que quieres incluir en este "pool de pools" como pool hijo.

### mother\_pool

El ID del [pool\_template](pool_template)) que define este "pool de pools".

### chance

La probabilidad porcentual explícita de que este pool hijo aparezca.

Si el pool madre hace aparecer solo un pool hijo (max\_limit = 1 en el [pool\_template](pool_template) del respectivo pool madre), el core selecciona el pool hijo a aparecer en un proceso de dos pasos: primero, solo se tiran los pools hijo con probabilidad explícita (chance > 0) del pool madre. Si esa tirada no produce ningún pool hijo, todos los pools hijo sin probabilidad explícita (chance = 0) se tiran con la misma probabilidad.

Si el pool madre hace aparecer más de un pool hijo, la probabilidad se ignora y todos los pools hijo del pool madre se tiran en un solo paso con la misma probabilidad.

En caso de que el pool madre haga aparecer solo un pool hijo y todos los pools hijo tengan una probabilidad distinta de cero, la suma de las probabilidades de todos los pools hijo debe ser igual a 100, de lo contrario el pool madre no funcionará correctamente.

### description

Un campo de texto para describir para qué sirve este pool de pools.
