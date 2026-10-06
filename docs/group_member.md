# group\_member

[<-Back-to:Characters](database-characters)

**The \`group\_member\` table**

This table holds info about group members.

**Table: group\_member's Structure**

| Field                       | Type    |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)               | INT     | UNSIGNED | NO   |     |         |       |         |
| [memberGuid](#memberguid)   | INT     | UNSIGNED | NO   | PRI |         |       |         |
| [memberFlags](#memberflags) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [subgroup](#subgroup)       | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [roles](#roles)             | TINYINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

GUID of the group. See [groups.guid](groups#guid).

### memberGuid

GUID of the character member of the group. See [characters.guid](characters#guid).

### memberFlags

| Value | Hex    | Flag                   | Unique |
| :---- | :----: | :--------------------- | :----- |
| 1     | `0x01` | MEMBER_FLAG_ASSISTANT  |        |
| 2     | `0x02` | MEMBER_FLAG_MAINTANK   | (U)    |
| 4     | `0x04` | MEMBER_FLAG_MAINASSIST | (U)    |

*(U) = Unique per group.*

### subgroup

Ranging 0-7 (1-8 in client), representing the subgroups of a raid group.
There can only be 5 membes in one subgroup per raid group.

### roles

| Value | Hex    | Flag        | Comment                                                          |
| :---- | :----: | :---------- | :--------------------------------------------------------------- |
| 0     | `0x00` | ROLE_NONE   | No role                                                          |
| 1     | `0x01` | ROLE_LEADER | The character has signed to Random Dungeon Finder as experienced |
| 2     | `0x02` | ROLE_TANK   | The character has signed to Random Dungeon Finder as tank        |
| 4     | `0x04` | ROLE_HEALER | The character has signed to Random Dungeon Finder as healer      |
| 8     | `0x08` | ROLE_DAMAGE | The character has signed to Random Dungeon Finder as dps         |
