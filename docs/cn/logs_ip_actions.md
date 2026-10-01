# logs\_ip\_actions

[<-返回至:Auth](database-auth)

**\`logs\_ip\_actions\` 表**

**表结构**

| Field               | Type        | Attributes | Key | Null | Default           | Extra | Comment                       |
| ------------------- | ----------- | ---------- | --- | ---- | ----------------- | ----- | ----------------------------- |
| [id][1]             | INT         | UNSIGNED   | PRI | NO   | AUTO_INCREMENT    |       | 唯一标识符                    |
| [account_id][2]     | INT         | UNSIGNED   |     | NO   |                   |       | 账号 ID                       |
| [character_guid][3] | INT         | UNSIGNED   |     | NO   |                   |       | 角色 GUID                     |
| [type][4]           | TINYINT     | UNSIGNED   |     | NO   |                   |       |                               |
| [ip][5]             | VARCHAR(15) | SIGNED     |     | NO   | 127.0.0.1         |       |                               |
| [systemnote][6]     | TEXT        | SIGNED     |     | YES  |                   |       | 系统插入的备注                |
| [unixtime][7]       | INT         | UNSIGNED   |     | NO   |                   |       | Unix 时间                     |
| [time][8]           | TIMESTAMP   | SIGNED     |     | NO   | CURRENT_TIMESTAMP |       | 时间戳                        |
| [comment][9]        | TEXT        | SIGNED     |     | YES  |                   |       | 允许用户添加评论              |

[1]: #id
[2]: #accountid
[3]: #characterguid
[4]: #type
[5]: #ip
[6]: #systemnote
[7]: #unixtime
[8]: #time
[9]: #comment

## 字段说明

### id

`field-no-description|1`

### account\_id

`field-no-description|2`

### character\_guid

`field-no-description|3`

### type

`field-no-description|4`

### ip

`field-no-description|5`

### systemnote

`field-no-description|6`

### unixtime

`field-no-description|7`

### time

`field-no-description|8`

### comment

`field-no-description|9`
