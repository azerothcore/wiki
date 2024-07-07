# spell\_group

[<-Back-to:World](database-world)

**The \`spell\_group\` table**

Table used to group spells for varius checks in the core. One spell may be added to many groups, but can occur in one group only once.

| Field             | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]           | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [spell_id][2]     | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [special_flag][3] | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #id
[2]: #spell_id
[3]: #special_flag

**Description of the fields**

### id

Group identifier
Rules of assigning id:

-   if group is going to be used in core code, use first avalible entry below 1000 and add enum value to SpellGroup enum in SpellMgr.h
-   if group is not going to be used in core code, use lowest avalible entry higher than 1000

### spell\_id

SpellId from Spell.dbc or spell\_group id prefixed with "-". If spell is added to spell\_ranks, spell\_id has to be first rank of that spell.

### special\_flag

Enum SpellGroupSpecialFlags in core:

| Flag | Hex    | Name                                                     | Comment                                                                                   |
| ---- | ------ | -------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 0    | 0x000  | SPELL\_GROUP\_SPECIAL\_FLAG\_NONE                        |                                                                                           |
| 1    | 0x001  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_BATTLE              |                                                                                           |
| 2    | 0x002  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_GUARDIAN            |                                                                                           |
| 3    | 0x003  | SPELL\_GROUP\_SPECIAL\_FLAG\_FLASK                       | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_BATTLE SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_GUARDIAN |
| 4    | 0x004  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_UNSTABLE            |                                                                                           |
| 8    | 0x008  | SPELL\_GROUP\_SPECIAL\_FLAG\_ELIXIR\_SHATTRATH           |                                                                                           |
| 15   | 0x00F  | SPELL\_GROUP\_SPECIAL\_FLAG\_STACK\_EXCLUSIVE\_MAX       |                                                                                           |
| 16   | 0x010  | SPELL\_GROUP\_SPECIAL\_FLAG\_FORCED\_STRONGEST           | Helpful flag if some spells have different auras, but only one should be present          |
| 32   | 0x020  | SPELL\_GROUP\_SPECIAL\_FLAG\_SKIP\_STRONGER\_CHECK       |                                                                                           |
| 64   | 0x040  | SPELL\_GROUP\_SPECIAL\_FLAG\_BASE\_AMOUNT\_CHECK         |                                                                                           |
| 256  | 0x100  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY1                   |                                                                                           |
| 512  | 0x200  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY2                   |                                                                                           |
| 1024 | 0x400  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY3                   |                                                                                           |
| 2048 | 0x800  | SPELL\_GROUP\_SPECIAL\_FLAG\_PRIORITY4                   |                                                                                           |
| 4096 | 0x1000 | SPELL\_GROUP\_SPECIAL\_FLAG\_SAME\_SPELL\_CHECK          |                                                                                           |
| 8192 | 0x2000 | SPELL\_GROUP\_SPECIAL\_FLAG\_SKIP\_STRONGER\_SAME\_SPELL |                                                                                           |
