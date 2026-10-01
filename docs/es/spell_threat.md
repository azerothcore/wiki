# spell\_threat

[<-Volver a: World](database-world)

**Tabla \`spell\_threat\`**

Esta tabla contiene los valores de amenaza (threat) de todos los hechizos que deban dar o quitar amenaza.

**Estructura**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]  | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [Threat][2] | SMALLINT  | SIGNED     |     | NO   | NULL    |       |         |

[1]: #entry
[2]: #threat

**Descripción de los campos**

### entry

El ID del hechizo. Ver [Spell.dbc](spell).

### Threat

El valor de amenaza que este hechizo debe añadir al lanzador (o quitar si es negativo).
