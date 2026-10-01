# lag\_reports

[<-返回至:Characters](database-characters)

**\`lag\_reports\` 表**

此表存储玩家在游戏中提交的延迟报告（当他们点击"帮助请求"时）。

**表结构**

| Field           | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [reportId][1]   | INT      | UNSIGNED   | PRI | NO   |         | Auto Increment |         |
| [guid][2]       | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [lagType][3]    | TINYINT  | UNSIGNED   |     | NO   | 0       |                |         |
| [mapId][4]      | SMALLINT | UNSIGNED   |     | NO   | 0       |                |         |
| [posX][5]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [posY][6]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [posZ][7]       | FLOAT    | SIGNED     |     | NO   | 0       |                |         |
| [latency][8]    | INT      | UNSIGNED   |     | NO   | 0       |                |         |
| [createTime][9] | INT      | UNSIGNED   |     | NO   | 0       |                |         |

[1]: #reportid
[2]: #guid
[3]: #lagtype
[4]: #mapid
[5]: #posx
[6]: #posy
[7]: #posz
[8]: #latency
[9]: #createtime

**字段说明**

### reportId

报告 ID

### guid

角色 guid。参见 [characters.guid](characters#guid)

### lagType

* 0 = 与掉落（Loot）相关
* 1 = 与拍卖行（Auction House）相关
* 2 = 与邮件（Mail）相关
* 3 = 与聊天（Chat）相关
* 4 = 与移动（Movement）相关
* 5 = 与法术和技能（Spells and Abilities）相关

### mapId

报告延迟的地图。参见 [Map.dbc](map)。

### posX

X 坐标。

### posY

Y 坐标。

### posZ

Z 坐标。

### latency

报告时的延迟，单位为毫秒。

### createTime

创建日期，以 Unix 时间表示。（待办：应更改为 mysql 时间戳）。
