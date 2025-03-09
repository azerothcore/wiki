# mail_server_template_conditions

[<-Back-to:Characters](database-characters)

**The \`mail_server_template_conditions\` table**

Works together with [mail_server_template](mail_server_template).

Note: Entries in this table will be deleted automatically when the referenced entry in [mail_server_template.id](mail_server_template#id) is deleted. CONSTRAINT `fk_mail_template_conditions`

**Table Structure**

| Field                            | Type | Attributes | Key | Null | Default | Extra          | Comment |
| -------------------------------- | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id](#id)                        | INT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [templatetID](#templateid)       | INT  | UNSIGNED   |     | NO   |         |                |         |
| [conditionType](#conditiontype)  | ENUM |            |     | NO   |         |                |         |
| [conditionValue](#conditiontype) | INT  | UNSIGNED   |     | NO   |         |                |         |
| [conditionState](#conditiontype) | INT  | UNSIGNED   |     | NO   | 0       |                |         |

**Description of the fields**

### id

Unique ID.

### templateID

[mail_server_template.id](mail_server_template#id).

### conditionType

| Name        | conditionValue                                                                                                              | conditionState                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Level       | minimum required level                                                                                                      | always 0                                                                       |
| PlayTime    | miniumum required play time in milliseconds                                                                                 | always 0                                                                       |
| Quest       | quest id                                                                                                                    | 0,1,3,5,6 (None, Complete, Incomplete, Failed, Rewarded)                       |
| Achievement | achievement id                                                                                                              | always 0                                                                       |
| Reputation  | faction id                                                                                                                  | 0-7 (Hated, Hostile, Unfriendly, Neutral, Friendly, Honored, Revered, Exalted) |
| Faction     | 0/1 (Alliance/Horde)                                                                                                        | always 0                                                                       |
| Race        | Bitmask (Human 1, Orc 2, Dwarf 4, Night Elf 8, Undead 16, Tauren 32, Gnome 64, Troll 128, Blood Elf 512, Draenei 1024)      | always 0                                                                       |
| Class       | Bitmask (Warrior 1, Paladin 2, Hunter 4, Rogue 8, Priest 16, Death Knight 32, Shaman 64, Mage 128, Warlock 256, Druid 1024) | always 0                                                                       |
