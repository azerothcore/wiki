# banned\_addons

[<-Back-to:Characters](database-characters.md)

**The \`banned\_addons\` table**

**Structure**

| Field          | Type         | Attributes | Key | Null | Default           | Extra  | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ----------------- | ------ | ------- |
| [Id][1]        | INT          | UNSIGNED   | PRI | NO   |                   |        |         |
| [Name][2]      | VARCHAR(255) | SIGNED     |     | NO   |                   | UNIQUE |         |
| [Version][3]   | VARCHAR(255) | SIGNED     |     | NO   | ''                | UNIQUE |         |
| [Timestamp][4] | TIMESTAMP    | SIGNED     |     | NO   | CURRENT_TIMESTAMP |        |         |

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
