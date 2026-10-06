# banned\_addons

[<-Back-to:Characters](database-characters)

**The \`banned\_addons\` table**

Holds the client interface addons that are banned on the server.

**Table: banned\_addons's Structure**

| Field                   | Type         |          | Null | Key | Default           | Extra                       | Comment |
| :---------------------- | :----------- | :------- | :--: | :-: | :---------------: | :-------------------------: | :------ |
| [Id](#id)               | INT          | UNSIGNED | NO   | PRI |                   | AUTO_INCREMENT              |         |
| [Name](#name)           | VARCHAR(255) |          | NO   | MUL |                   |                             |         |
| [Version](#version)     | VARCHAR(255) |          | NO   |     | ''                |                             |         |
| [Timestamp](#timestamp) | TIMESTAMP    |          | NO   |     | CURRENT_TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP |         |

**Description of the table's fields**

### Id

The unique ID of the entry.

### Name

The name of the addon. The server sends this list to the client, which then disables the addon.

### Version

The version of the addon to ban. Empty bans all versions.

### Timestamp

The time the entry was added or last changed.
