# version\_db\_characters

[<-Back-to:Auth](database-auth.md)

**The \`version\_db\_characters\` table**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [sql_rev][1]       | VARCHAR(100) | SIGNED     | PRI | NO   |         |       |         |
| [required_rev][2]  | VARCHAR(100) | SIGNED     |     | YES  |         |       |         |
| [date][3]          | VARCHAR(50)  | SIGNED     |     | YES  |         |       |         |
| [2021_07_08_00][4] | BIT(1)       | SIGNED     |     | YES  |         |       |         |

[1]: #sql_rev
[2]: #required_rev
[3]: #date
[4]: #2021_07_08_00

**Description of the fields**

### sql_rev

SQL review.

### required_rev

`field-no-description|2`

### date 

Sql revisions date.

### 2021_07_08_00

The date of the last update to the auth database.

**Note** this column changes automatically according to the last update of the auth database.