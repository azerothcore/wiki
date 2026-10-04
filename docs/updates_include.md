# updates\_include

[<-Back-to:Auth](database-auth)
[<-Back-to:Characters](database-characters)
[<-Back-to:World](database-world)

**The \`updates\_include\` table**

The directories the database updater looks in for SQL update files. The table is in the auth, characters and world databases.

**Table: updates\_include's Structure**

| Field           | Type         |                                  | Null | Key | Default  | Extra | Comment                                                         |
| :-------------- | :----------- | :------------------------------- | :--: | :-: | :------: | :---: | :-------------------------------------------------------------- |
| [path](#path)   | VARCHAR(200) |                                  | NO   | PRI |          |       | directory to include. $ means relative to the source directory. |
| [state](#state) | ENUM         | RELEASED,ARCHIVED,CUSTOM,PENDING | NO   |     | RELEASED |       | defines if the directory contains released or archived updates. |

**Description of the table's fields**

### path

The directory to include in updates.

$ means relative to the source directory.

### state

Defines if the directory has released, custom or archived updates.
