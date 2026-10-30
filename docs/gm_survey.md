# gm\_survey

[<-Back-to:Characters](database-characters)

**The \`gm\_survey\` table**

Stores the GM surveys players fill in after a ticket is closed. Surveys are only offered when `GM.TicketSystem.ChanceOfGMSurvey` in worldserver.conf is above 0.

**Table: gm\_survey's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra          | Comment |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [surveyId](#surveyid)     | INT      | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [guid](#guid)             | INT      | UNSIGNED | NO   |     | 0       |                |         |
| [mainSurvey](#mainsurvey) | INT      | UNSIGNED | NO   |     | 0       |                |         |
| [comment](#comment)       | LONGTEXT |          | NO   |     |         |                |         |
| [createTime](#createtime) | INT      | UNSIGNED | NO   |     | 0       |                |         |
| [maxMMR](#maxmmr)         | SMALLINT |          | NO   |     |         |                |         |

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
