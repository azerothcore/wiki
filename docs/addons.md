# addons

[<-Back-to:Characters](database-characters)

**The \`addons\` table**

**Table: addons's Structure**

| Field     | Type         | Attributes | Key | Null | Default | Extra | Comment |
| --------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [name][1] | VARCHAR(120) | SIGNED     | PRI | NO   | ''      | PRI   |         |
| [crc][2]  | INT          | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #name
[2]: #crc

**Description of the table's fields**

### name

The name of the addon.

### crc

The CRC the client sent for the addon.
