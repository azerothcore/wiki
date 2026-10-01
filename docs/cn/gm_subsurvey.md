# gm\_subsurvey

[<-返回:Characters](database-characters)

**\`gm\_subsurvey\` 表**

此表包含调查问题的答案。它与 `gm_survey` 相关联。

**表结构**

| 字段              | 类型 | 属性     | 键 | 空 | 默认值        | 额外 | 注释 |
| ------------------ | ---- | ---------- | --- | ---- | -------------- | ----- | ------- |
| [surveyId][1]      | INT  | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |       |         |
| [questionId][2]    | INT  | UNSIGNED   | PRI | NO   | 0              |       |         |
| [answer][3]        | INT  | UNSIGNED   |     | NO   | 0              |       |         |
| [answerComment][4] | TEXT | SIGNED     |     | NO   |                |       |         |

[1]: #surveyid
[2]: #questionid
[3]: #answer
[4]: #answercomment

**字段说明**

### surveyId

`field-no-description|1`

### questionId

`field-no-description|2`

### answer

`field-no-description|3`

### answerComment

`field-no-description|4`
