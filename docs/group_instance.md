# group\_instance

[<-Back-to:Characters](database-characters.md)

**The \`group\_instance\` table**

`table-no-description`

**Structure**

| Field          | Type       | Attributes | Key | Null | Default | Extra | Comment |
|----------------|------------|------------|-----|------|---------|-------|---------|
| [guid][1]      | int(10)    | unsigned   | PRI | NO   | 0       |       |         |
| [instance][2]  | int(10)    | unsigned   | PRI | NO   | 0       |       |         |
| [permanent][3] | TINYINT(3) | unsigned   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #instance
[3]: #permanent

**Description of the fields**

### guid

Guid of the group.

### instance

ID of the Instance session the group has enterd.

### permanent

Boolean flag if the group is bound to the Instance or not.
