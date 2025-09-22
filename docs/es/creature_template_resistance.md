# creature_template_resistance

[<-Volver a:World](database-world)

**Tabla \`creature_template_resistance\`**

**Estructura**

| Campo              | Tipo      | Atributo | Llave | Nulo | Por defecto | Extra | Comentario |
| ------------------ | --------- | -------- | ----- | ---- | ----------- | ----- | ---------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED | PRI   | NO   |             |       |            |
| [School][2]        | TINYINT   | UNSIGNED | PRI   | NO   |             |       |            |
| [Resistance][3]    | SMALLINT  | SIGNED   |       | YES  | NULL        |       |            |
| [VerifiedBuild][4] | SMALLINT  | SIGNED   |       | YES  | 0           |       |            |

[1]: #creatureid
[2]: #school
[3]: #resistance
[4]: #verifiedbuild

**Descripción de los campos**

### CreatureID

Entrada de criatura de [creature_template.entry](creature_template#entry).

### School

El valor debe estar dentro de este rango. Si es superior o inferior, SQL generará un error en `creature_template_resistance_chk_1`.

| Valor | Nombre              |
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

Este campo se utilizó para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no se ha analizado.

Si el valor es superior a 0, se ha analizado con archivos WDB de esa compilación de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en las WDB.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa compilación de cliente específica y luego se editó manualmente para satisfacer alguna necesidad especial.
