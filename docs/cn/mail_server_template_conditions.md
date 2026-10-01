# mail_server_template_conditions

[<-返回至:Characters](database-characters)

**\`mail_server_template_conditions\` 表**

与 [mail_server_template](mail_server_template) 协同工作。

注意：当 [mail_server_template.id](mail_server_template#id) 中被引用的条目被删除时，此表中的条目将自动删除。约束 CONSTRAINT `fk_mail_template_conditions`

**表结构**

| Field                            | Type | Attributes | Key | Null | Default | Extra          | Comment |
| -------------------------------- | ---- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [id](#id)                        | INT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [templateID](#templateid)        | INT  | UNSIGNED   |     | NO   |         |                |         |
| [conditionType](#conditiontype)  | ENUM |            |     | NO   |         |                |         |
| [conditionValue](#conditiontype) | INT  | UNSIGNED   |     | NO   |         |                |         |
| [conditionState](#conditiontype) | INT  | UNSIGNED   |     | NO   | 0       |                |         |

## 字段说明

### id

唯一 ID。

### templateID

[mail_server_template.id](mail_server_template#id)。

### conditionType

| 名称        | conditionValue                                                                                                              | conditionState                                                                 |
| ----------- | --------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Level       | 最低所需等级                                                                                                                | 始终为 0                                                                       |
| PlayTime    | 最低所需游戏时间（以毫秒为单位）                                                                                            | 始终为 0                                                                       |
| Quest       | 任务 id                                                                                                                     | 0,1,3,5,6 (无、已完成、未完成、失败、已奖励)                                   |
| Achievement | 成就 id                                                                                                                     | 始终为 0                                                                       |
| Reputation  | 声望阵营 id                                                                                                                 | 0-7 (仇恨、敌对、冷淡、中立、友好、尊敬、崇敬、崇拜)                           |
| Faction     | 0/1 (联盟/部落)                                                                                                             | 始终为 0                                                                       |
| Race        | 位掩码 (人类 1、兽人 2、矮人 4、暗夜精灵 8、亡灵 16、牛头人 32、侏儒 64、巨魔 128、血精灵 512、德莱尼 1024)                 | 始终为 0                                                                       |
| Class       | 位掩码 (战士 1、圣骑士 2、猎人 4、潜行者 8、牧师 16、死亡骑士 32、萨满祭司 64、法师 128、术士 256、德鲁伊 1024)              | 始终为 0                                                                       |
| AccountFlags | 账号标志的位掩码（见下文）                                                                                                  | 始终为 0                                                                       |

#### AccountFlags 值

| 标志                            | 值         | 描述                              |
| ------------------------------- | ---------- | ---------------------------------- |
| ACCOUNT_FLAG_GM                 | 0x1        | 账号是 GM                         |
| ACCOUNT_FLAG_COLLECTOR          | 0x4        | 典藏版                            |
| ACCOUNT_FLAG_TRIAL              | 0x8        | 试玩账号                          |
| ACCOUNT_FLAG_IGR                | 0x20       | Internet Game Room                |
| ACCOUNT_FLAG_REFERRAL           | 0x800      | 招募好友（Recruit-A-Friend）       |
| ACCOUNT_FLAG_EXPANSION_COLLECTOR | 0x10000   | TBC 典藏版                        |
| ACCOUNT_FLAG_DISABLE_VOICE      | 0x20000    | 无法加入语音聊天                  |
| ACCOUNT_FLAG_DISABLE_VOICE_SPEAK | 0x40000   | 无法在语音聊天中发言              |
| ACCOUNT_FLAG_REFERRAL_RESURRECT | 0x80000    | 复活卷轴                          |
| ACCOUNT_FLAG_EXPANSION2_COLLECTOR | 0x4000000 | WotLK 典藏版                      |
| ACCOUNT_FLAG_OVERMIND_LINKED    | 0x8000000  | 与 Battle.net 账号关联            |
| ACCOUNT_FLAG_DEATH_KNIGHT_OK    | 0x20000000 | 账号上有一个 55+ 级的角色         |
