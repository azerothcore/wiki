# group\_member

[<-返回至:Characters](database-characters)

**\`group\_member\` 表**

此表保存了队伍成员的信息。

**表结构**

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

**字段说明**

#### guid

队伍的 GUID。参见 [groups.guid](groups#guid)。

#### memberGuid

队伍中角色成员的 GUID。参见 [characters.guid](characters#guid)。

| 名称                   | 值     | 唯一 |
| ---------------------- | ------ | ---- |
| MEMBER_FLAG_ASSISTANT  | 0x01   |      |
| MEMBER_FLAG_MAINTANK   | 0x02   | (U)  |
| MEMBER_FLAG_MAINASSIST | 0x04   | (U)  |

*(U) = 每个队伍唯一。*

### subgroup

取值范围 0-7（客户端中显示为 1-8），代表团队副本队伍的各个小队。
每个团队副本队伍的一个小队中最多只能有 5 名成员。

### roles

| 值   | 名称        | 注释                                                        |
| ---- | ----------- | ----------------------------------------------------------- |
| 0    | ROLE_NONE   |                                                             |
| 1    | ROLE_LEADER | 该角色已作为熟练者（experienced）报名随机地下城查找器       |
| 2    | ROLE_TANK   | 该角色已作为坦克报名随机地下城查找器                        |
| 4    | ROLE_HEALER | 该角色已作为治疗者报名随机地下城查找器                      |
| 8    | ROLE_DAMAGE | 该角色已作为伤害输出（dps）报名随机地下城查找器             |
