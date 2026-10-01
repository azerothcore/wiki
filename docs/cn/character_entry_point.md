# character\_entry\_point

[<-返回:Characters](database-characters)

**\`character\_entry\_point\` 表**

**表结构**

| Field           | Type  | Attributes | Key | Null | Default | Extra | Comment                  |
| --------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]       | INT   | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [joinX][2]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinY][3]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinZ][4]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinO][5]      | FLOAT | SIGNED     |     | NO   | 0       |       |                          |
| [joinMapId][6]  | INT   | UNSIGNED   |     | YES  | 0       |       | Map Identifier           |
| [taxiPath0][7]  | INT   | UNSIGNED   |     | NO   | 0       |       |                          |
| [taxiPath1][9]  | INT   | UNSIGNED   |     | NO   | 0       |       |                          |
| [mountSpell][8] | INT   | UNSIGNED   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #joinx
[3]: #joiny
[4]: #joinz
[5]: #joino
[6]: #joinmapid
[7]: #taxipath0
[9]: #taxipath1
[8]: #mountspell

**字段说明**

### guid

全局唯一标识符。

### joinX

`field-no-description|2`

### joinY

`field-no-description|3`

### joinZ

`field-no-description|4`

### joinO

`field-no-description|5`

### joinMapId

地图标识符。

### taxiPath0

保存进入点（entry point）时角色所处飞行（taxi）路径的起始节点。

### taxiPath1

保存进入点（entry point）时角色所处飞行（taxi）路径的目的地节点。

### mountSpell

`field-no-description|8`
