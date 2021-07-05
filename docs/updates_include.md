# updates_include

[<-Back-to:Auth](database-auth.md)
[<-Back-to:Characters](database-characters.md)
[<-Back-to:World](database-world.md)

**The \`updates_include\` table**

**Structure**

| Field      | Type         | Attributes               | Key | Null | Default  | Extra | Comment                                                         |
| ---------- | ------------ | ------------------------ | --- | ---- | -------- | ----- | --------------------------------------------------------------- |
| [path][1]  | VARCHAR(200) |                          | PRI | NO   |          |       | Directory to include. $ means relative to the source directory. |
| [state][2] | ENUM         | RELEASED,CUSTOM,ARCHIVED |     | NO   | RELEASED |       | Defines if the directory contains released or archived updates. |

[1]: #path
[2]: #state

## Description of the fields

### path

The directory to include in updates.

$ means relative to the source directory.

### state

Defines if the directory has released, custom or archived updates.
