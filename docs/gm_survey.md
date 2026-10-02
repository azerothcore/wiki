# gm\_survey

[<-Back-to:Characters](database-characters)

**The \`gm\_survey\` table**

**Table: gm\_survey's Structure**

| Field           | Type     | Attributes | Key | Null | Default        | Extra | Comment |
| --------------- | -------- | ---------- | --- | ---- | -------------- | ----- | ------- |
| [surveyId][1]   | INT      | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |       |         |
| [guid][2]       | INT      | UNSIGNED   |     | NO   | 0              |       |         |
| [mainSurvey][3] | INT      | UNSIGNED   |     | NO   | 0              |       |         |
| [comment][4]    | LONGTEXT | SIGNED     |     | NO   |                |       |         |
| [createTime][5] | INT      | UNSIGNED   |     | NO   | 0              |       |         |
| [maxMMR][6]     | SMALLINT | SIGNED     |     | NO   |                |       |         |

[1]: #surveyid
[2]: #guid
[3]: #mainsurvey
[4]: #comment
[5]: #createtime
[6]: #maxmmr

**Description of the table's fields**

### surveyId

The unique ID of the survey.

### guid

GUID of the character that filled in the survey. See [characters.guid](characters#guid).

### mainSurvey

ID of the survey from GMSurveySurveys.dbc.

### comment

The comment the player wrote.

### createTime

The time the survey was sent, in Unix time.

### maxMMR

Not set by the core.
