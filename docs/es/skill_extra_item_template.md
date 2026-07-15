# skill\_extra\_item\_template

[<-Volver a:World](database-world)

**Tabla \`skill\_extra\_item\_template\`**

Esta tabla contiene información sobre cómo, al usar ciertos spells de profesión, tienes la probabilidad de crear más de una copia del item.

**Estructura**

| Field                       | Type      | Attributes | Key | Null | Default | Extra | Comment                            |
| --------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [spellId][1]                | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | SpellId of the item creation spell |
| [requiredSpecialization][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | Specialization spell id            |
| [additionalCreateChance][3] | FLOAT     | SIGNED     |     | NO   | 0       |       | chance to create add               |
| [additionalMaxNum][4]       | TINYINT   | UNSIGNED   |     | NO   | 0       |       | max num of adds                    |

[1]: #spellid
[2]: #requiredspecialization
[3]: #additionalcreatechance
[4]: #additionalmaxnum

**Descripción de los campos**

### spellId

El ID del spell que crea el item. Ver [Spell.dbc](spell)

### requiredSpecialization

El ID del spell de especialización requerido. El personaje debe tener aprendido el ID del spell especificado aquí para tener una probabilidad de crear otro item al instante.

### additionalCreateChance

La probabilidad de que el jugador cree otro item al instante.

### additionalMaxNum

El número de copias extra que se pueden crear.
