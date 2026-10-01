# mail_server_template_conditions

[<-Volver a:Characters](database-characters)

**Tabla \`mail_server_template_conditions\`**

Funciona junto con [mail_server_template](mail_server_template).

Nota: Las entradas de esta tabla se borrarán automáticamente cuando se elimine la entrada referenciada en [mail_server_template.id](mail_server_template#id). CONSTRAINT `fk_mail_template_conditions`

**Estructura**

| Field                            | Type | Attributes | Key | Null | Default | Extra          | Comment |
| -------------------------------- | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id](#id)                        | INT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [templatetID](#templateid)       | INT  | UNSIGNED   |     | NO   |         |                |         |
| [conditionType](#conditiontype)  | ENUM |            |     | NO   |         |                |         |
| [conditionValue](#conditiontype) | INT  | UNSIGNED   |     | NO   |         |                |         |
| [conditionState](#conditiontype) | INT  | UNSIGNED   |     | NO   | 0       |                |         |

**Descripción de los campos**

### id

ID único.

### templateID

[mail_server_template.id](mail_server_template#id).

### conditionType

| Name        | conditionValue                                                                                                              | conditionState                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Level       | nivel mínimo requerido                                                                                                      | siempre 0                                                                      |
| PlayTime    | tiempo de juego mínimo requerido en milisegundos                                                                            | siempre 0                                                                      |
| Quest       | id de quest                                                                                                                 | 0,1,3,5,6 (None, Complete, Incomplete, Failed, Rewarded)                       |
| Achievement | id de logro                                                                                                                 | siempre 0                                                                      |
| Reputation  | id de facción                                                                                                               | 0-7 (Hated, Hostile, Unfriendly, Neutral, Friendly, Honored, Revered, Exalted) |
| Faction     | 0/1 (Alliance/Horde)                                                                                                        | siempre 0                                                                      |
| Race        | Bitmask (Human 1, Orc 2, Dwarf 4, Night Elf 8, Undead 16, Tauren 32, Gnome 64, Troll 128, Blood Elf 512, Draenei 1024)      | siempre 0                                                                      |
| Class        | Bitmask (Warrior 1, Paladin 2, Hunter 4, Rogue 8, Priest 16, Death Knight 32, Shaman 64, Mage 128, Warlock 256, Druid 1024) | siempre 0                                                                      |
| AccountFlags | Bitmask de flags de cuenta (ver abajo)                                                                                      | siempre 0                                                                      |

#### Valores de AccountFlags

| Flag                            | Value      | Description                          |
| ------------------------------- | ---------- | ------------------------------------ |
| ACCOUNT_FLAG_GM                 | 0x1        | La cuenta es GM                      |
| ACCOUNT_FLAG_COLLECTOR          | 0x4        | Edición de coleccionista             |
| ACCOUNT_FLAG_TRIAL              | 0x8        | Cuenta de prueba                     |
| ACCOUNT_FLAG_IGR                | 0x20       | Internet Game Room                   |
| ACCOUNT_FLAG_REFERRAL           | 0x800      | Recruit-A-Friend                     |
| ACCOUNT_FLAG_EXPANSION_COLLECTOR | 0x10000   | Edición de coleccionista de TBC      |
| ACCOUNT_FLAG_DISABLE_VOICE      | 0x20000    | No puede unirse al chat de voz       |
| ACCOUNT_FLAG_DISABLE_VOICE_SPEAK | 0x40000   | No puede hablar en el chat de voz    |
| ACCOUNT_FLAG_REFERRAL_RESURRECT | 0x80000    | Scroll of Resurrection               |
| ACCOUNT_FLAG_EXPANSION2_COLLECTOR | 0x4000000 | Edición de coleccionista de WotLK   |
| ACCOUNT_FLAG_OVERMIND_LINKED    | 0x8000000  | Vinculada con Battle.net             |
| ACCOUNT_FLAG_DEATH_KNIGHT_OK    | 0x20000000 | Tiene un personaje de nivel 55+ en la cuenta |
