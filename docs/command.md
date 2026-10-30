# command

[<-Back-to:World](database-world)

**The \`command\` table**

Holds help and security information for commands. This table does NOT create new commands, it only sets / overrides security and provides help.

**Table: command's Structure**

| Field                 | Type        |          | Null | Key | Default | Extra | Comment |
| :-------------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [name](#name)         | VARCHAR(50) |          | NO   | PRI | ''      |       |         |
| [security](#security) | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [help](#help)         | LONGTEXT    |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### name

The name of the command. See: [included commands](gm-commands)

### security

The security level required to use the command. Corresponds with account_access.gmlevel in the realm database.

### help

The help text displayed by the .help command.
