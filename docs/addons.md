# addons

[<-Back-to:Characters](database-characters)

**The \`addons\` table**

Holds the CRC of each standard Blizzard client addon the server knows about. The core checks the addons a client reports at login against it.

**Table: addons's Structure**

| Field     | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [name][1] | VARCHAR(120) |            | PRI | NO   | ''      |       |         |
| [crc][2]  | INT          | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #name
[2]: #crc

**Description of the table's fields**

### name

The name of the addon.

### crc

The CRC the client sent for the addon.
