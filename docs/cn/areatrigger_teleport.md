# areatrigger\_teleport

[<-返回:World](database-world)

**\`areatrigger\_teleport\` 表**

包含所有传送触发器的定义。此表用于补全 .dbc 文件的信息。

**表结构**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                 | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Name][2]               | text      |            | MUL | YES  |         |       |         |
| [target_map][3]         | SMALLINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [target_position_x][4]  | FLOAT     |            |     | NO   | 0       |       |         |
| [target_position_y][5]  | FLOAT     |            |     | NO   | 0       |       |         |
| [target_position_z][6]  | FLOAT     |            |     | NO   | 0       |       |         |
| [target_orientation][7] | FLOAT     |            |     | NO   | 0       |       |         |

[1]: #id
[2]: #name
[3]: #targetmap
[4]: #targetpositionx
[5]: #targetpositiony
[6]: #targetpositionz
[7]: #targetorientation

**字段描述**

### ID

这是触发器标识符，它必须与 [AreaTrigger.dbc](dbc-areatrigger) 中的一致

### name

触发器的名称。这可以是任意名称，仅用于描述目的。

### target\_map

触发器的目标地图（参见 Maps.dbc）。

### target\_position\_x

触发器目标目的地的 X 坐标

### target\_position\_y

触发器目标目的地的 Y 坐标

### target\_position\_z

触发器目标目的地的 Z 坐标

### target\_orientation

玩家出现在此位置时获得的方向

### 示例

| ID  | Name                                     | target_map | target_position_x | target_position_y | target_position_z | target_orientation |
| --- | ---------------------------------------- | ---------- | ----------------- | ----------------- | ----------------- | ------------------ |
| 45  | Scarlet Monastery - Graveyard (Entrance) | 189        | 1688.99           | 1053.48           | 18.6775           | 0.00117            |
| 78  | DeadMines Entrance                       | 36         | -16.4             | -383.07           | 61.78             | 1.86               |
| 101 | Stormwind Stockades Entrance             | 34         | 54.23             | 0.28              | -18.34            | 6.26               |
| 107 | Stormwind Vault Entrance                 | 35         | -0.91             | 40.57             | -24.23            | 0                  |
| 109 | Stormwind Vault Instance                 | 0          | -8653.45          | 606.19            | 91.16             | 0                  |
