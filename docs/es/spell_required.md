# spell\_required

[<-Volver a: World](database-world)

**Tabla \`spell\_required\`**

Tabla usada para añadir restricciones al aprendizaje de hechizos de un entrenador. El jugador no puede aprender el hechizo 'spell\_id' hasta que aprenda 'req\_spell'; cuando pierde 'req\_spell', 'spell\_id' también se perderá. La tabla se usa también para las especializaciones de profesión, ya que las especializaciones requieren una profesión de cierto rango para aprenderse.

**Estructura**

| Field          | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell_id][1]  | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |
| [req_spell][2] | MEDIUMINT | SIGNED     | PRI | NO   | 0       |       |         |

[1]: #spellid
[2]: #reqspell

**Descripción de los campos**

### spell\_id

ID del hechizo de [Spell.dbc](spell), que requiere conocer \`req\_spell\` para aprenderse de un entrenador.

### req\_spell

ID del hechizo de [Spell.dbc](spell), que se requiere conocer antes de poder aprender \`spell\_id\` de un entrenador.
