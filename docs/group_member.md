# group\_member

[<-Back-to:Characters](database-characters)

**The \`group\_member\` table**

This table holds info about group members.

**Table Structure**

| Field            | Type    | Attributes | Key | Null | Default | Extra  | Comment |
| ---------------- | ------- | ---------- | --- | ---- | ------- | ------ | ------- |
| [guid][1]        | INT     | UNSIGNED   |     | NO   |         |        |         |
| [memberGuid][2]  | INT     | UNSIGNED   | PRI | NO   |         | Unique |         |
| [memberFlags][3] | TINYINT | UNSIGNED   |     | NO   | 0       |        |         |
| [subgroup][4]    | TINYINT | UNSIGNED   |     | NO   | 0       |        |         |
| [roles][5]       | TINYINT | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #guid
[2]: #memberguid
[3]: #memberflags
[4]: #subgroup
[5]: #roles

**Description of the fields**

#### guid

GUID of the group. See [groups.guid](groups#guid).

#### memberGuid

GUID of the character member of the group. See [characters.guid](characters#guid).

| Name                   | Value | Unique |
| ---------------------- | ----- | ------ |
| MEMBER_FLAG_ASSISTANT  | 0x01  |        |
| MEMBER_FLAG_MAINTANK   | 0x02  | (U)    |
| MEMBER_FLAG_MAINASSIST | 0x04  | (U)    |

*(U) = Unique per group.*

### subgroup

Ranging 0-7 (1-8 in client), representing the subgroups of a raid group.
There can only be 5 membes in one subgroup per raid group.

### roles

| Value | Name        | Comments                                                         |
| ----- | ----------- | ---------------------------------------------------------------- |
| 0     | ROLE_NONE   |                                                                  |
| 1     | ROLE_LEADER | The character has signed to Random Dungeon Finder as experienced |
| 2     | ROLE_TANK   | The character has signed to Random Dungeon Finder as tank        |
| 4     | ROLE_HEALER | The character has signed to Random Dungeon Finder as healer      |
| 8     | ROLE_DAMAGE | The character has signed to Random Dungeon Finder as dps         |
