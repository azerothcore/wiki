# creature_template_model

[<-Volver a: World](database-world)

**Tabla `creature_template_model`**

Esta tabla describe qué modelo se asigna a una criatura específica.

**Estructura**

| Field                  | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [CreatureID][1]        | INT      | UNSIGNED   | PRI | NO   |         |       |         |
| [Idx][2]               | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [CreatureDisplayID][3] | INT      | UNSIGNED   |     | NO   |         |       |         |
| [DisplayScale][4]      | FLOAT    |            |     | NO   | 1       |       |         |
| [Probability][5]       | FLOAT    |            |     | NO   | 0       |       |         |
| [VerifiedBuild][6]     | SMALLINT |            |     | YES  |         |       |         |

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

DisplayID de CreatureDisplayInfo.dbc.

### DisplayScale

Modifica la escala del modelo.

### Probability

0-1

Si supera o queda por debajo de 1, el core lo corregirá durante el arranque para que sea igual a 1.

### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0, entonces aún no ha sido analizado.

Si el valor es mayor que 0, entonces ha sido analizado con archivos WDB de esa build específica del cliente.

Si el valor es -1, entonces es solo un marcador de posición hasta que se encuentren los datos adecuados en los WDB.

Si el valor es [client build](realmlist#gamebuild), entonces se analizó con archivos WDB de esa build específica del cliente y se editó manualmente más tarde por alguna necesidad especial.
