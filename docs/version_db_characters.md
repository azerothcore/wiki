# version\_db\_characters

[<-Back-to:Characters](database-characters.md)

**The \`version\_db\_characters\` table**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [sql_rev][1]       | VARCHAR(100) | SIGNED     | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) | SIGNED     |     | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  | SIGNED     |     | YES  |         |       |         |
| [2021_07_08_00][4] | BIT(1)       | SIGNED     |     | YES  |         |       |         |

[1]: #sqlrev
[2]: #requiredrev
[3]: #date
[4]: #2021070800

**Description of the fields**

### sql\_rev

SQL review.

### required\_rev

`field-no-description|2`

### date 

Sql revisions date.

### 2021\_07\_08\_00

The date of the last update to the characters database.

**Note** this column changes automatically according to the last update of the characters database.
