# command

[<-Back-to:World](database-world.md)

**The `command` table**

Holds help and security information for commands. This table does NOT create new commands, it only sets / overrides security and provides help.

**Structure**

| Field         | Type        | Attributes | Key | Null | Default | Extra | Comment |
|---------------|-------------|------------|-----|------|---------|-------|---------|
| [name][1]     | VARCHAR(50) | SIGNED     | PRI | NO   | NULL    |       |         |
| [security][2] | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [help][3]     | longtext    | SIGNED     |     | YES  | NULL    |       |         |

[1]: #name
[2]: #security
[3]: #help

**Description of the fields**

### name

The name of the command. [included commands](gm-commands.md)

### security

The security level required to use the command. Corresponds with account_access.gmlevel in the realm database.

### help

The help text displayed by the .help command.
