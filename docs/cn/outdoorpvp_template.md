# outdoorpvp_template

[<-返回:World](database-world)

**\`outdoorpvp_template\` 表**

**表结构**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [TypeId][1]     | TINYINT  | unasigned  | PRI | NO   |         |       |         |
| [ScriptName][2] | char(64) | SIGNED     |     | NO   | 0       |       |         |
| [comment][3]    | text     | SIGNED     |     | YES  | NULL    |       |         |

[1]: #typeid
[2]: #scriptname
[3]: #comment

**字段说明**

### TypeId
模拟器中为世界中每个 PvP 区域定义的 ID。

### ScriptName
此户外 PvP 所使用的脚本名称。这将脚本引擎中的脚本与此户外 PvP 关联起来。

### comment
给定 outdoorpvp_template 的脚本名称。

### 示例

| TypeId | ScriptName    | comment       |
| ------ | ------------- | ------------- |
| 1      | outdoorpvp_hp | 地狱火半岛     |
| 2      | outdoorpvp_na | 纳格兰        |
| 3      | outdoorpvp_tf | 泰罗卡森林     |
| 4      | outdoorpvp_zm | 赞加沼泽       |
| 5      | outdoorpvp_si | 希利苏斯       |
| 6      | outdoorpvp_ep | 东瘟疫之地     |
| 7      | outdoorpvp_gh | 灰熊丘陵       |
