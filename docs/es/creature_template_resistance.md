# creature_template_resistance

[<-Volver a: World](database-world)

**Tabla \`creature_template_resistance\`**

**Estructura**

| Field              | Type      | Attribute | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI | NO   |         |       |         |
| [School][2]        | TINYINT   | UNSIGNED  | PRI | NO   |         |       |         |
| [Resistance][3]    | SMALLINT  | SIGNED    |     | YES  | NULL    |       |         |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |     | YES  | 0       |       |         |

[1]: #creatureid
[2]: #school
[3]: #resistance
[4]: #verifiedbuild

**Descripción de los campos**

### CreatureID

Entry de la criatura, de [creature_template.entry](creature_template#entry).

### School

El valor debe estar dentro de este rango. Si es mayor o menor, el SQL fallará en `creature_template_resistance_chk_1`.

| Value | Name                |
| :---- | :------------------ |
| 1     | SPELL_SCHOOL_HOLY   |
| 2     | SPELL_SCHOOL_FIRE   |
| 3     | SPELL_SCHOOL_NATURE |
| 4     | SPELL_SCHOOL_FROST  |
| 5     | SPELL_SCHOOL_SHADOW |
| 6     | SPELL_SCHOOL_ARCANE |

### Resistance

Valor de resistencia.

### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no ha sido analizado.

Si el valor es mayor que 0, entonces ha sido analizado con archivos WDB de esa build específica del cliente.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en los WDB.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa build específica del cliente y se editó manualmente más tarde por alguna necesidad especial.
