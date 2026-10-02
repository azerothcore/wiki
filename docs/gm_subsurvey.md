# gm\_subsurvey

[<-Back-to:Characters](database-characters)

**The \`gm\_subsurvey\` table**

This table contains the answers to the survey questions. It's linked to `gm_survey`.

**Table: gm\_subsurvey's Structure**

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

**Description of the table's fields**

### surveyId

The survey the answer belongs to. See [gm\_survey.surveyId](gm_survey#surveyid).

### questionId

ID of the question from GMSurveyQuestions.dbc.

### answer

The rating the player chose for the question.

### answerComment

The comment the player wrote for the question.
