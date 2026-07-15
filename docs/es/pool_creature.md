# pool\_creature

[<-Volver a:World](database-world)

**Tabla \`pool\_creature\`**

Esta tabla contiene una lista de creatures que están ligadas a un pool concreto.

**Estructura**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]        | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [pool_entry][2]  | MEDIUMINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [chance][3]      | FLOAT        | UNSIGNED   |     | NO   | 0       |       |         |
| [description][4] | VARCHAR(255) |            |     | YES  | NULL    |       |         |

[1]: #guid
[2]: #pool_entry
[3]: #chance
[4]: #description

**Descripción de los campos**

### guid

[creature.guid](creature#guid)

### pool\_entry

El pool en el que está esta creature. Se refiere a [pool\_template.entry](pool_template#entry).

### chance

La probabilidad porcentual explícita de que esta creature aparezca.

Si el pool hace aparecer solo una creature (max\_limit = 1 en su respectivo [pool\_template](pool_template)), el core selecciona la creature a aparecer en un proceso de dos pasos: primero, solo se tiran las creatures con probabilidad explícita (chance &gt; 0) del pool. Si esa tirada no produce ninguna creature, todas las creatures sin probabilidad explícita (chance = 0) se tiran con la misma probabilidad.

Si el pool hace aparecer más de una creature, la probabilidad se ignora y todas las creatures del pool se tiran en un solo paso con la misma probabilidad.

En caso de que el pool haga aparecer solo una creature y todas las creatures tengan una probabilidad distinta de cero, la suma de las probabilidades de todas las creatures debe ser igual a 100, de lo contrario el pool no aparecerá.

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `pool_creature_chk_1`.

### description

Este campo normalmente nombra la creature correspondiente al guid y menciona de qué punto de aparición se trata. Ejemplo: Snarlflare (14272) - Spawn 1
