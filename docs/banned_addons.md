# banned\_addons

[<-Back-to:Characters](database-characters)

**The \`banned\_addons\` table**

**Table Structure**

| Field          | Type         | Attributes | Key    | Null | Default           | Extra | Comment |
| -------------- | ------------ | ---------- | ------ | ---- | ----------------- | ----- | ------- |
| [Id][1]        | INT          | UNSIGNED   | PRI    | NO   | AUTO_INCREMENT    |       |         |
| [Name][2]      | VARCHAR(255) |            | UNIQUE | NO   |                   |       |         |
| [Version][3]   | VARCHAR(255) |            | UNIQUE | NO   | ''                |       |         |
| [Timestamp][4] | TIMESTAMP    |            |        | NO   | CURRENT_TIMESTAMP |       |         |

[1]: #id
[2]: #name
[3]: #version
[4]: #timestamp

**Description of the fields**

### Id

`field-no-description|1`

### Name

`field-no-description|2`

### Version

`field-no-description|3`

### Timestamp

`field-no-description|4`
