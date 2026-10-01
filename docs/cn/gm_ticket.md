# gm\_ticket

[<-返回:Characters](database-characters)

**\`gm\_tickets\` 表**

此表存储所有工单（ticket）。

注意：不要直接向这些列中的大多数插入数据，否则客户端在表重新加载并注销之前不会更新工单状态。

**表结构**

| 字段                  | 类型        | 属性     | 键 | 空 | 默认值        | 额外 | 注释                                    |
| ---------------------- | ----------- | ---------- | --- | ---- | -------------- | ----- | ------------------------------------------ |
| [Id][1]                | INT         | UNSIGNED   | PRI | NO   | AUTO_INCREMENT |       |                                            |
| [type][2]              | TINYINT     | UNSIGNED   |     | NO   | 0              |       | 0 开启，1 关闭，2 角色已删除      |
| [playerGuid][3]        | INT         | UNSIGNED   |     | NO   | 0              |       | 工单创建者的全局唯一标识符 |
| [name][4]              | VARCHAR(12) | SIGNED     |     | NO   |                |       | 工单创建者的名称                     |
| [description][5]       | text        | SIGNED     |     | NO   |                |       |                                            |
| [createTime][6]        | INT         | UNSIGNED   |     | NO   | 0              |       |                                            |
| [mapId][7]             | SMALLINT    | UNSIGNED   |     | NO   | 0              |       |                                            |
| [posX][8]              | FLOAT       | SIGNED     |     | NO   | 0              |       |                                            |
| [posY][9]              | FLOAT       | SIGNED     |     | NO   | 0              |       |                                            |
| [posZ][10]             | FLOAT       | SIGNED     |     | NO   | 0              |       |                                            |
| [lastModifiedTime][11] | INT         | UNSIGNED   |     | NO   | 0              |       |                                            |
| [closedBy][12]         | INT         | SIGNED     |     | NO   | 0              |       | -1 由控制台关闭，>0 GM 的 GUID        |
| [assignedTo][13]       | INT         | UNSIGNED   |     | NO   | 0              |       | 工单所分配到的管理员 GUID   |
| [comment][14]          | text        | SIGNED     |     | NO   |                |       |                                            |
| [response][15]         | text        | SIGNED     |     | NO   |                |       |                                            |
| [completed][16]        | TINYINT     | UNSIGNED   |     | NO   | 0              |       |                                            |
| [escalated][17]        | TINYINT     | UNSIGNED   |     | NO   | 0              |       |                                            |
| [viewed][18]           | TINYINT     | UNSIGNED   |     | NO   | 0              |       |                                            |
| [needMoreHelp][19]     | TINYINT     | UNSIGNED   |     | NO   | 0              |       |                                            |
| [resolvedBy][20]       | INT         | SIGNED     |     | NO   | 0              |       | -1 由控制台解决，>0 GM 的 GUID      |

[1]: #id
[2]: #type
[3]: #playerguid
[4]: #name
[5]: #description
[6]: #createtime
[7]: #mapid
[8]: #posx
[9]: #posy
[10]: #posz
[11]: #lastmodifiedtime
[12]: #closedby
[13]: #assignedto
[14]: #comment
[15]: #response
[16]: #completed
[17]: #escalated
[18]: #viewed
[19]: #needmorehelp
[20]: #resolvedby

**字段说明**

### Id

工单的全局唯一标识符。此编号必须是唯一的，是区分各个工单的最佳方式。

### type

工单的类型。变量：
- 0 = 开启（open）
- 1 = 关闭（closed）
- 2 = 角色已删除（character deleted）

### playerGuid

玩家的 GUID。参见 [characters.guid](characters#guid)。

### name

创建该工单的角色名称。

### description

工单的内容。

### createTime

工单的创建时间，以 linux 时间戳表示。

### mapId

创建工单时所在的地图。参见 [Map.dbc](map)。

### posX

创建工单时的 X 坐标。

### posY

创建工单时的 Y 坐标。

### posZ

创建工单时的 Z 坐标。

### lastModifiedTime

工单被发起者关闭或删除的时间，以 linux 时间戳表示。

### closedBy

- 0 = 开启（Open）
- ~-1 = 由控制台关闭（Closed by Console）~（在 azerothcore 上尚未实现）
- > 0 = 放弃工单的玩家或关闭工单的 GM

### assignedTo

指定被分配到此工单的 GM（GameMaster）的账号编号。

### comment

通过 `.ticket comment` 添加的工单评论，只有游戏管理员可见。如果该命令使用两次，会覆盖之前的评论。

### response

GM 在完成工单之前使用 `.ticket response` 命令插入的回复字符串。如果该命令使用两次，会在之前的回复末尾追加新的回复。

### completed

- 0 = 未完成
- 1 = 已完成（会通知用户并显示 `response` 中的内容）

### escalated

- 0 = 工单当前未分配给任何 GM
- 1 = 工单已分配给一个普通 GM
- 2 = 工单在完成后已被升级（需要 GM 联系玩家）


### viewed

- 0 = 还没有人查看过该工单。
- > 0 = 该工单被 GM 查看的次数

### needMoreHelp

对 GM 已经回复过的工单请求进一步的 GM 交互。基本上表示"有一个新工单"。

### resolvedBy

- 0 = 开启（Open）
- ~-1 = 由控制台解决（Resolved by Console）~（由于数据库中的数据类型问题，在 azerothcore 上尚不支持）
- > 0 = 解决该工单的 GM 的角色 GUID（通过关闭工单或完成工单）
