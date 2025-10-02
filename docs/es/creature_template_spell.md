# creature_template_spell

[<-Volver a:World](database-world)

**Tabla \`creature_template_spell\`**

**Estructura**

| Campo              | Tipo      | Atributo  | Llave  | Nulo | Por defecto | Extra | Comentario |
| ------------------ | --------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [CreatureID][1]    | MEDIUMINT | UNSIGNED  | PRI   | NO   |             |       |            |
| [Index][2]         | TINYINT   | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [Spell][3]         | MEDIUMINT | UNSIGNED  |       | Si   | Null        |       |            |
| [VerifiedBuild][4] | SMALLINT  | SIGNED    |       | Si   | 0           |       |            |

[1]: #creatureid
[2]: #index
[3]: #spell
[4]: #verifiedbuild

**Descripción de los campos**

### CreatureID

Entrada de criatura de [creature_template.entry](creature_template#entry).

### Index

El valor debe estar dentro de este rango. Si es superior o inferior, SQL generará un error en `creature_template_spell_chk_1`.

Índice 0 - 7.

Posición del hechizo en la barra de acción para criaturas vehículo.

### Spell

Identificación de hechizo que se puede usar para el control mental de una criatura.

### VerifiedBuild

Este campo se utilizó para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no se ha analizado.

Si el valor es superior a 0, se ha analizado con archivos WDB de esa compilación de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en las WDB.

Si el valor es -Client Build, entonces se analizó con archivos WDB de esa compilación de cliente específica y luego se editó manualmente para satisfacer alguna necesidad especial.
