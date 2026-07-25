# creature_template_spell

[<-Volver a: World](database-world)

**Tabla \`creature_template_spell\`**

**Estructura**

| Field              | Type      | Attribute | Key  | Null | Default | Extra | Comment |
| ------------------ | --------- | --------- | ---- | ---- | ------- | ----- | ------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI  | NO   |         |       |         |
| [Index][2]         | TINYINT   | UNSIGNED  | PRI  | NO   | 0       |       |         |
| [Spell][3]         | MEDIUMINT | UNSIGNED  |      | YES  | Null    |       |         |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |      | YES  | 0       |       |         |

[1]: #creatureid
[2]: #index
[3]: #spell
[4]: #verifiedbuild

**Descripción de los campos**

### CreatureID

Entry de la criatura, de [creature_template.entry](creature_template#entry).

### Index

El valor debe estar dentro de este rango. Si es mayor o menor, el SQL fallará en `creature_template_spell_chk_1`.

Índice 0 - 7.

Posición del hechizo en la barra de acción para criaturas de tipo vehículo.

### Spell

ID del hechizo que puede usarse para el Control Mental de una criatura.

### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no ha sido analizado.

Si el valor es mayor que 0, entonces ha sido analizado con archivos WDB de esa build específica del cliente.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en los WDB.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa build específica del cliente y se editó manualmente más tarde por alguna necesidad especial.
