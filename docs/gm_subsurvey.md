# gm\_subsurvey

[<-Back-to:Characters](database-characters)

**The \`gm\_subsurvey\` table**

This table contains the answers to the survey questions. It's linked to `gm_survey`.

**Table Structure**

| Field              | Type | Attributes | Key | Null | Default        | Extra | Comment |
| ------------------ | ---- | ---------- | --- | ---- | -------------- | ----- | ------- |
| [surveyId][1]      | INT  | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |       |         |
| [questionId][2]    | INT  | UNSIGNED   | PRI | NO   | 0              |       |         |
| [answer][3]        | INT  | UNSIGNED   |     | NO   | 0              |       |         |
| [answerComment][4] | TEXT | SIGNED     |     | NO   |                |       |         |

[1]: #surveyid
[2]: #questionid
[3]: #answer
[4]: #answercomment

**Description of the fields**

### surveyId

`field-no-description|1`

### questionId

`field-no-description|2`

### answer

`field-no-description|3`

### answerComment

`field-no-description|4`
