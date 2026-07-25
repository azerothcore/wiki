# spell\_learn\_spell

[<-Volver a: World](database-world)

**Tabla \`spell\_learn\_spell\`**

Esta tabla contiene información sobre hechizos que deben aprenderse al mismo tiempo que un jugador aprende otro hechizo. Por ejemplo, los pocos hechizos que se aprenden automáticamente cuando un jugador aprende por primera vez una nueva profesión. Todos los campos de esta tabla usan IDs de hechizo de Spell.dbc.

NOTA: Los hechizos con el efecto de hechizo SPELL\_EFFECT\_LEARN\_SPELL NO deben incluirse en esta tabla.

**Estructura**

| Field        | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]   | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SpellID][2] | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Active][3]  | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #spellid
[3]: #active

**Descripción de los campos**

### entry

El entry del hechizo que el jugador aprende, ya sea de un entrenador o de cualquier otro sitio (.learn por ejemplo).

### SpellID

El entry del hechizo que el jugador aprenderá automáticamente cuando aprenda el hechizo especificado en [entry](#spell_learn_spell-entry).

### Active

Define si el hechizo se muestra en el libro de hechizos o no.
