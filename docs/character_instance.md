# character\_instance

[<-Back-to:Characters](database-characters)

**The \`character\_instance\` table**

Contains the instance data for characters.

**Table: character\_instance's Structure**

| Field                   | Type    |          | Null | Key | Default | Extra | Comment |
| :---------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)           | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [instance](#instance)   | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [permanent](#permanent) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [extended](#extended)   | TINYINT | UNSIGNED | NO   |     |         |       |         |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### instance

The instance ID. See [instance.id](instance#id).

### permanent

Boolean 0 or 1 controlling if the player has been bound to the instance. A player is bound to the instance only when he (or his party/raid) kills a creature with the CREATURE\_FLAG\_EXTRA\_INSTANCE\_BIND flag set in the [flags\_extras](creature_template#flagsextra) field.

### extended

Boolean (0 or 1). If 1, the player has extended this instance's reset timer for an additional reset cycle.
