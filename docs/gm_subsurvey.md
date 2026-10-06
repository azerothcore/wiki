# gm\_subsurvey

[<-Back-to:Characters](database-characters)

**The \`gm\_subsurvey\` table**

This table contains the answers to the survey questions. It's linked to `gm_survey`.

**Table: gm\_subsurvey's Structure**

| Field                           | Type |          | Null | Key | Default | Extra          | Comment |
| :------------------------------ | :--- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [surveyId](#surveyid)           | INT  | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [questionId](#questionid)       | INT  | UNSIGNED | NO   | PRI | 0       |                |         |
| [answer](#answer)               | INT  | UNSIGNED | NO   |     | 0       |                |         |
| [answerComment](#answercomment) | TEXT |          | NO   |     |         |                |         |

**Description of the table's fields**

### surveyId

The survey the answer belongs to. See [gm\_survey.surveyId](gm_survey#surveyid).

### questionId

ID of the question from GMSurveyQuestions.dbc.

### answer

The rating the player chose for the question.

### answerComment

The comment the player wrote for the question.
