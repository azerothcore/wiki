# gm\_survey

[<-Volver a:Characters](database-characters.md)

**Tabla \`gm\_survey\` **

Por el momento esta tabla no tiene una definicón específica, tanto en la versión española como inglesa de éste foro y de otros emuladores. Las descripciones aquí hechas NO son las oficiales.

**Estructura**

| Field           | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [surveyId][1]   | INT      | UNSIGNED   | PRI | NO   |         | Auto Increment |         |
| [guid][2]       | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [mainSurvey][3] | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [comment][4]    | LONGTEXT | SIGNED     |     | NO   |         |                |         |
| [createTime][5] | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [maxMMR][6]     | SMALLINT | SIGNED     |     | NO   |         |                |         |

[1]: #surveyid
[2]: #guid
[3]: #mainsurvey
[4]: #comment
[5]: #createtime
[6]: #maxmmr

**Descripción de los Campos**

### surveyId

`field-no-description|1` (¿Identificador único del 'survey'?)

### guid

`field-no-description|2` (¿GUID del personaje del 'survey'?)

### mainSurvey

`field-no-description|3` (¿ID del 'survey' principal?)

### comment

`field-no-description|4` (¿Un texto a manera de comentario?)

### createTime

`field-no-description|5` (¿Tiempo de haber sido creado? Posiblemente medido en tiempo UNIX)

### maxMMR

`field-no-description|6` (Matchmaking Rating o [Rango de Emparejamiento de Partidas](https://es.wikipedia.org/wiki/Emparejamiento_(videojuegos) máximo medido en valores enteros)
