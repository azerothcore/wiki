# gm\_subsurvey

[<-Volver a:Characters](database-characters)

Leer en: [English :gb:](../gm_subsurvey) [Spanish :es:](gm_subsurvey)

**Tabla \`gm\_subsurvey\`**

Esta tabla contiene las respuestas a las preguntas de la encuesta. Está vinculado a `gm_survey`.

**Estructura**

| Field              | Type | Attributes | Key | Null | Default | Extra          | Comment |
| ------------------ | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [surveyId][1]      | INT  | UNSIGNED   | PRI | NO   |         | Auto increment |         |
| [questionId][2]    | INT  | UNSIGNED   | PRI | NO   | 0       |                |         |
| [answer][3]        | INT  | UNSIGNED   |     | NO   | 0       |                |         |
| [answerComment][4] | TEXT | SIGNED     |     | NO   |         |                |         |

[1]: #surveyid
[2]: #questionid
[3]: #answer
[4]: #answercomment

**Descripción de los campos**

### surveyId

`campo-sin-descripción|1`

### questionId

`campo-sin-descripción|2`

### answer

`campo-sin-descripción|3`

### answerComment

`campo-sin-descripción|4`
