# reputation\_reward\_rate

[<-Volver a:World](database-world)

**Tabla \`reputation\_reward\_rate\`**

Contiene multiplicadores de reputación para facciones concretas.

**Estructura**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [faction][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [quest_rate][2]    | FLOAT     | SIGNED     |     | NO   | 1       |       |         |
| [creature_rate][3] | FLOAT     | SIGNED     |     | NO   | 1       |       |         |
| [spell_rate][4]    | FLOAT     | SIGNED     |     | NO   | 1       |       |         |

[1]: #faction
[2]: #quest_rate
[3]: #creature_rate
[4]: #spell_rate

**Descripción de los campos**

### faction

El ID de la facción a la que se aplican estas tasas.

### quest\_rate

La tasa para la ganancia de reputación por quests.

### creature\_rate

La tasa para la ganancia de reputación por creatures.

### spell\_rate

La tasa para la ganancia de reputación por spells.
