# addons

[<-Back-to:Characters](database-characters)

**The \`addons\` table**

Holds the CRC of each standard Blizzard client addon the server knows about. The core checks the addons a client reports at login against it.

**Table: addons's Structure**

| Field         | Type         |          | Null | Key | Default | Extra | Comment |
| :------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [name](#name) | VARCHAR(120) |          | NO   | PRI | ''      |       |         |
| [crc](#crc)   | INT          | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### name

The name of the addon.

### crc

The CRC the client sent for the addon.
