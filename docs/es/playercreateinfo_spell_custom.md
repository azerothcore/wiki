# playercreateinfo\_spell\_custom

[<-Volver a:World](database-world)

**Tabla \`playercreateinfo_spell_custom\`**

Esta tabla contiene información sobre qué spells debería tener un personaje recién creado al empezar si la opción PlayerStart.AllSpells está activada en worldserver.conf. Un personaje en esta tabla se define por su combinación de raza y clase.

Ten en cuenta que tendrás que poner PlayerStart.CustomSpells a 1 en la configuración; si no, esta tabla no tendrá ningún efecto.

**Estructura**

| Field          | Type         | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [racemask][1]  | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [classmask][2] | INT          | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Spell][3]     | MEDIUMINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Note][4]      | VARCHAR(255) | SIGNED     |     | YES  | NULL    |       |         |

[1]: #racemask
[2]: #classmask
[3]: #spell
[4]: #note

**Descripción de los campos**

### racemask

Una o más razas del personaje. Ver [ChrRaces.dbc](chrraces).

### classmask

Una o más clases del personaje. Ver [ChrClasses.dbc](chrclasses)

### Spell

Id de spell. Ver [Spell.dbc](spell)

### Note

Básicamente un comentario de lo que hace tu consulta.
