# spell_jump_distance

[<-Volver a: World](database-world)


**Tabla `spell_jump_distance`**

Esta tabla almacena las sobrescrituras de distancia de salto en cadena por hechizo. Cuando está presente, el servidor carga `JumpDistance` y lo asigna a `SpellInfo::JumpDistance`; luego `Spell::SearchChainTargets()` usa este valor para limitar el radio de salto de objetivos en cadena.

**Estructura**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 | | Spell id (links to Spell.dbc) |
| [JumpDistance](#jumpdistance) | FLOAT | SIGNED | | NO | 0 | | Max hop distance in yards |

**Descripción de los campos**

### ID

Identificador del hechizo al que se aplica esta fila. Ver [Spell.dbc](spell).

### JumpDistance

Distancia máxima de salto en cadena (en yardas) para el hechizo. Cuando es > 0, el servidor usará este valor en lugar del radio de salto por defecto al buscar objetivos en cadena.
