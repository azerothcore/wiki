# character\_instance

[<-Back-to:Characters](database-characters)

**The \`character\_instance\` table**

Contains the instance data for characters.

**Table Structure**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [instance][2]  | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [permanent][3] | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |
| [extended][4]  | TINYINT | UNSIGNED   |     | NO   |         |       |         |

[1]: #guid
[2]: #instance
[3]: #permanent
[4]: #extended

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### instance

The instance ID. See [instance.id](instance#id).

### permanent

Boolean 0 or 1 controlling if the player has been bound to the instance. A player is bound to the instance only when he (or his party/raid) kills a creature with the CREATURE\_FLAG\_EXTRA\_INSTANCE\_BIND flag set in the [flags\_extras](creature_template#creature_template-flags_extra) field.

### extended

`field-no-description|4`
