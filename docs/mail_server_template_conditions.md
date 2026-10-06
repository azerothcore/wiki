# mail\_server\_template\_conditions

[<-Back-to:Characters](database-characters)

**The \`mail\_server\_template\_conditions\` table**

Works together with [mail_server_template](mail_server_template).

Note: Entries in this table will be deleted automatically when the referenced entry in [mail_server_template.id](mail_server_template#id) is deleted. CONSTRAINT `fk_mail_template_conditions`

**Table: mail\_server\_template\_conditions's Structure**

| Field                            | Type |                                                                             | Null | Key | Default | Extra          | Comment |
| :------------------------------- | :--- | :-------------------------------------------------------------------------- | :--: | :-: | :-----: | :------------: | :------ |
| [id](#id)                        | INT  | UNSIGNED                                                                    | NO   | PRI |         | AUTO_INCREMENT |         |
| [templateID](#templateid)        | INT  | UNSIGNED                                                                    | NO   | MUL |         |                |         |
| [conditionType](#conditiontype)  | ENUM | Level,PlayTime,Quest,Achievement,Reputation,Faction,Race,Class,AccountFlags | NO   |     |         |                |         |
| [conditionValue](#conditiontype) | INT  | UNSIGNED                                                                    | NO   |     |         |                |         |
| [conditionState](#conditiontype) | INT  | UNSIGNED                                                                    | NO   |     | 0       |                |         |

**Description of the table's fields**

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
| Class        | Bitmask (Warrior 1, Paladin 2, Hunter 4, Rogue 8, Priest 16, Death Knight 32, Shaman 64, Mage 128, Warlock 256, Druid 1024) | always 0                                                                       |
| AccountFlags | Bitmask of account flags (see below)                                                                                        | always 0                                                                       |

### conditionValue

The value the condition checks, see the table in [conditionType](#conditiontype).

### conditionState

The state the condition checks, see the table in [conditionType](#conditiontype).

#### AccountFlags values

| Value     | Hex          | Flag                              | Comment                              |
| :-------- | :----------: | :-------------------------------- | :----------------------------------- |
| 1         | `0x00000001` | ACCOUNT_FLAG_GM                   | Account is GM                        |
| 4         | `0x00000004` | ACCOUNT_FLAG_COLLECTOR            | Collector's Edition                  |
| 8         | `0x00000008` | ACCOUNT_FLAG_TRIAL                | Trial account                        |
| 32        | `0x00000020` | ACCOUNT_FLAG_IGR                  | Internet Game Room                   |
| 2048      | `0x00000800` | ACCOUNT_FLAG_REFERRAL             | Recruit-A-Friend                     |
| 65536     | `0x00010000` | ACCOUNT_FLAG_EXPANSION_COLLECTOR  | TBC Collector's Edition              |
| 131072    | `0x00020000` | ACCOUNT_FLAG_DISABLE_VOICE        | Cannot join voice chat               |
| 262144    | `0x00040000` | ACCOUNT_FLAG_DISABLE_VOICE_SPEAK  | Cannot speak in voice chat           |
| 524288    | `0x00080000` | ACCOUNT_FLAG_REFERRAL_RESURRECT   | Scroll of Resurrection               |
| 67108864  | `0x04000000` | ACCOUNT_FLAG_EXPANSION2_COLLECTOR | WotLK Collector's Edition            |
| 134217728 | `0x08000000` | ACCOUNT_FLAG_OVERMIND_LINKED      | Linked with Battle.net               |
| 536870912 | `0x20000000` | ACCOUNT_FLAG_DEATH_KNIGHT_OK      | Has a level 55+ character on account |
