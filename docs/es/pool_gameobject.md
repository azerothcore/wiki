# pool\_gameobject

[<-Volver a:World](database-world)

**Tabla \`pool\_gameobject\`**

Esta tabla contiene gameobjects que están ligados a un pool concreto.
Esta tabla solo puede contener gameobjects que tengan un tipo GAMEOBJECT\_TYPE\_CHEST, GAMEOBJECT\_TYPE\_GOOBER, GAMEOBJECT\_TYPE\_FISHINGHOLE.

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

[gameobject.guid](gameobject#guid)

### pool\_entry

El pool en el que está este gameobject. Se refiere a [pool\_template.entry](pool_template#entry).

### chance

La probabilidad porcentual explícita de que este gameobject aparezca.

Si el pool hace aparecer solo un gameobject (max\_limit = 1 en su respectivo [pool\_template](pool_template)), el core selecciona el gameobject a aparecer en un proceso de dos pasos: primero, solo se tiran los gameobjects con probabilidad explícita (chance &gt; 0) del pool. Si esa tirada no produce ningún gameobject, todos los gameobjects sin probabilidad explícita (chance = 0) se tiran con la misma probabilidad.

Si el pool hace aparecer más de un gameobject, la probabilidad se ignora y todos los gameobjects del pool se tiran en un solo paso con la misma probabilidad.

En caso de que el pool haga aparecer solo un gameobject y todos los gameobjects tengan una probabilidad distinta de cero, la suma de las probabilidades de todos los gameobjects debe ser igual a 100, de lo contrario el pool no aparecerá.

El valor debe ser >=0. Si el valor no cumple la condición, el SQL fallará en `pool_gameobject_chk_1`.

### description

Este campo normalmente nombra el gameobject correspondiente al guid y menciona de qué punto de aparición se trata. Ejemplo: Spawn Point 4 - Tin Vein
