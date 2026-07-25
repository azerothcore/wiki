# skill\_discovery\_template

[<-Volver a:World](database-world)

**Tabla \`skill\_discovery\_template\`**

Esta tabla controla el llamado sistema de "descubrimiento" (discovery) para aprender spells. Este sistema lo usa únicamente ![(question)](images/icons/emoticons/help_16.png){.emoticon .emoticon-question} la profesión de alquimia y controla la probabilidad de que un jugador "descubra" otra receta mientras crea items con otras recetas.

**Estructura**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment                           |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | --------------------------------- |
| [spellId][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | SpellId of the discoverable spell |
| [reqSpell][2]      | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | spell requirement                 |
| [reqSkillValue][3] | SMALLINT  | UNSIGNED   |     | NO   | 0       |       | skill points requirement          |
| [chance][4]        | FLOAT     | SIGNED     |     | NO   | 0       |       | chance to discover                |

[1]: #spellid
[2]: #reqspell
[3]: #reqskillvalue
[4]: #chance

**Descripción de los campos**

### spellId

El ID del spell de la receta que tiene una probabilidad de descubrirse automáticamente. Ver Spell.dbc

### reqSpell

Si es distinto de cero, este campo controla qué spell debe usarse específicamente para desencadenar el descubrimiento (p. ej., el spell 41458 solo se descubrirá al usar el spell 28575). Si es cero, entonces el uso de cualquier receta puede desencadenar el descubrimiento. Ver Spell.dbc

### reqSkillValue

El nivel de skill mínimo requerido en la profesión correspondiente para poder descubrir esta receta.

### chance

La probabilidad, en porcentaje, de que una receta se "descubra" automáticamente, ya sea por el uso de cualquier receta o por el uso de la receta específica definida en [reqSpell](#skill_discovery_template-reqSpell)
