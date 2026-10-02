# updates

[<-Back-to:Auth](database-auth)
[<-Back-to:Characters](database-characters)
[<-Back-to:World](database-world)

**The \`updates\` table**

Lists the SQL update files the database updater has applied to this database. The table is in the auth, characters and world databases.

**Table: updates's Structure**

| Field          | Type         | Attributes                              | Key | Null | Default           | Extra | Comment                                       |
| -------------- | ------------ | --------------------------------------- | --- | ---- | ----------------- | ----- | --------------------------------------------- |
| [name][1]      | VARCHAR(200) |                                         | PRI | NO   |                   |       | filename with extension of the update.        |
| [hash][2]      | CHAR(40)     |                                         |     | YES  | ''                |       | sha1 hash of the sql file.                    |
| [state][3]     | ENUM         | RELEASED,CUSTOM,MODULE,ARCHIVED,PENDING |     | NO   | RELEASED          |       | defines if an update is released or archived. |
| [timestamp][4] | TIMESTAMP    |                                         |     | NO   | CURRENT_TIMESTAMP |       | timestamp when the query was applied.         |
| [speed][5]     | INT          | UNSIGNED                                |     | NO   | 0                 |       | time the query takes to apply in ms.          |

[1]: #name
[2]: #hash
[3]: #state
[4]: #timestamp
[5]: #speed


**Description of the table's fields**

### name

The filename of the imported file.

### hash

The SHA1 hash from the imported file.

### state

Defines if the update is released, custom or archived.

### timestamp

The time that the file was imported.

### speed

How long in ms it took to import the file.
