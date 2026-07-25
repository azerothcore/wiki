# spell\_linked\_spell

[<-Volver a: World](database-world)

**Tabla \`spell\_linked\_spell\`**

Esta tabla proporciona datos para el sistema de enlazado de hechizos (spell linking), indicándole qué hechizos activan qué, y bajo qué condiciones.

**Estructura**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell_trigger][1] | MEDIUMINT | SIGNED     |     | NO   |         |       |         |
| [spell_effect][2]  | MEDIUMINT | SIGNED     |     | NO   |         |       |         |
| [type][3]          | SMALLINT  | UNSIGNED   |     | NO   |         |       |         |
| [comment][4]       | text      |            |     | NO   |         |       |         |

[1]: #spelltrigger
[2]: #spelleffect
[3]: #type
[4]: #comment

**Descripción de los campos**

### spell\_trigger

El hechizo que, al lanzarse, activará el hechizo listado en [spell\_effect](#spell_effect)

### spell\_ effect

El hechizo que quieres que se active. Cómo actúa este hechizo lo determina el campo [type](#type).

### type

Son posibles tres valores (0,1,2). Ver abajo.

### comment

Comentario opcional para explicar el enlace.

# **Descripción de los efectos de enlace**

### type 0 (CAST)

**Modo de activación**

- \***spell\_trigger > 0:** "Cuando se lanza *spell\_trigger*..."
- \***spell\_trigger < 0:** "Cuando se elimina el aura debida a *spell\_trigger*..."

**Efecto**

- \***spell\_effect > 0:** *spell\_effect* también se lanza (con el flag triggered) sobre los mismos objetivos, sobre el lanzador si *spell\_trigger* no tiene objetivo.
- \***spell\_effect < 0:** Se eliminan las auras debidas a *spell\_effect*.

### type 1 (HIT)

**Modo de activación**

- \***spell\_trigger > 0:** "El efecto se ejecuta cuando *spell\_trigger* impacta a un objetivo. Supongo que si *spell\_trigger* impacta a más de un objetivo, el efecto se ejecuta por cada objetivo impactado.

**Efecto**

- \***spell\_effect > 0:** *spell\_effect* se lanza (con el flag triggered) sobre el mismo objetivo.
- \***spell\_effect < 0:** Se eliminan las auras debidas a *spell\_effect*.

### type 2 (AURA)

**Modo de activación**

- \***spell\_trigger > 0:** "El efecto se ejecuta cuando el aura *spell\_trigger* se aplica **Y** cuando se elimina de un objetivo.

**Efecto**

\***spell\_effect > 0 (AÑADIR/ELIMINAR AURA)**

-   AL APLICAR: Añade el aura *spell\_effect* sobre el mismo objetivo.
-   AL ELIMINAR: Elimina el aura *spell\_effect*sobre el mismo objetivo.

\***spell\_effect < 0 (INMUNIDAD)**

-   AL APLICAR: Hace al objetivo inmune a *spell\_effect*.
-   AL ELIMINAR: Limpia la inmunidad del objetivo a *spell\_effect*.
