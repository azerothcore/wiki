# spell_cone

[<-Volver a: World](database-world)

**Tabla `spell_cone`**

Esta tabla almacena las sobrescrituras del radio de cono usadas por la selección de objetivos en cono.
Cuando existe una fila, se usa el valor de `spell_cone.cone_radius` para el cálculo del radio del cono.
Si no existe ninguna sobrescritura, el core recurre a `spell_dbc.ConeRadius`, y luego al manejo de hechizos hardcodeado heredado.

**Estructura**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id](#id) | INT | UNSIGNED | PRI | NO | 0 | | Spell identifier |
| [cone_radius](#cone_radius) | FLOAT | SIGNED | | NO | 1 | | Cone radius override (yards, schema default is 1) |

**Descripción de los campos**

### id

Identificador del hechizo al que se aplica esta fila.

### cone_radius

Radio del cono (en yardas) usado por el cálculo del ángulo del cono (base de 90° + ajuste por tamaño del objeto).
