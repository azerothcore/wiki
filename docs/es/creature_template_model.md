# creature_template_model

[<-Volver a:World](database-world)

**Tabla `creature_template_model`**

Esta tabla describe qué modelo está asignado a una criatura específica.

**Estructura**

| Campo                  | Tipo     | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------------- | -------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [CreatureID][1]        | INT      | UNSIGNED  | PRI   | NO   |             |       |            |
| [Idx][2]               | SMALLINT | UNSIGNED  | PRI   | NO   | 0           |       |            |
| [CreatureDisplayID][3] | INT      | UNSIGNED  |       | NO   |             |       |            |
| [DisplayScale][4]      | FLOAT    |           |       | NO   | 1           |       |            |
| [Probability][5]       | FLOAT    |           |       | NO   | 0           |       |            |
| [VerifiedBuild][6]     | SMALLINT |           |       | Si   |             |       |            |

[1]: #creatureid
[2]: #idx
[3]: #creaturedisplayid
[4]: #displayscale
[5]: #probability
[6]: #verifiedbuild

**Descripción de los campos**

### CreatureID

[creature_template.entry](creature_template#entry)

### Idx

Índice 0-3.

### CreatureDisplayID

ID de visualización de CreatureDisplayInfo.dbc.

### DisplayScale

Modifica la escala del modelo.

### Probability

0-1

Si excede o no llega a 1, el núcleo lo corregirá durante el arranque para que sea igual a 1.

### VerifiedBuild

Este campo se utilizó para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no se ha analizado.

Si el valor es superior a 0, se ha analizado con archivos WDB de esa compilación de cliente específica.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en las WDB.

Si el valor es [compilación del cliente](realmlist#gamebuild), entonces se analizó con archivos WDB de esa compilación del cliente específica y luego se editó manualmente para satisfacer alguna necesidad especial.
