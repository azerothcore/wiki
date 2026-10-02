# banned\_addons

[<-Back-to:Characters](database-characters)

**The \`banned\_addons\` table**

**Table: banned\_addons's Structure**

| Field          | Type         | Attributes | Key | Null | Default           | Extra                       | Comment |
| -------------- | ------------ | ---------- | --- | ---- | ----------------- | --------------------------- | ------- |
| [Id][1]        | INT          | UNSIGNED   | PRI | NO   |                   | AUTO_INCREMENT              |         |
| [Name][2]      | VARCHAR(255) |            | MUL | NO   |                   |                             |         |
| [Version][3]   | VARCHAR(255) |            |     | NO   | ''                |                             |         |
| [Timestamp][4] | TIMESTAMP    |            |     | NO   | CURRENT_TIMESTAMP | ON UPDATE CURRENT_TIMESTAMP |         |

[1]: #id
[2]: #name
[3]: #version
[4]: #timestamp

**Description of the table's fields**

### Id

The unique ID of the entry.

### Name

The name of the addon. The server sends this list to the client, which then disables the addon.

### Version

The version of the addon to ban. Empty bans all versions.

### Timestamp

The time the entry was added or last changed.
