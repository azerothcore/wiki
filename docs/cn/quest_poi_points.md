# quest\_poi\_points

[<-返回至:World](database-world)

**`quest\_poi\_points` 表**

来源于嗅探（sniffs）。从视觉上说，该表用于确定地图（不是小地图，而是主地图）上任务问号应出现的 X 和 Y 坐标。使用 ".gps" 命令获取你所站位置的坐标。要看到更改效果，请执行 ".reload quest\_poi"，关闭 Wow.exe，然后删除你的缓存文件夹。

**表结构**

| Field              | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [questid][1]       | INT      | UNSIGNED  | PRI | NO   | 0       |       |         |
| [Idx1][6]          | INT      | UNSIGNED  | PRI | NO   | 0       |       |         |
| [idx2][2]          | INT      | UNSIGNED  | PRI | NO   | 0       |       |         |
| [x][3]             | INT      | UNSIGNED  |     | NO   | 0       |       |         |
| [y][4]             | INT      | UNSIGNED  |     | NO   | 0       |       |         |
| [VerifiedBuild][5] | SMALLINT | UNSIGNED  |     | YES  | NULL    |       |         |

[1]: #questid
[2]: #idx2
[3]: #x
[4]: #y
[5]: #verifiedbuild
[6]: #idx1

**字段说明**

### questid

来自 [quest\_poi.questid](quest_poi#questid) 的任务 ID。

### idx1

用于对 quest\_poi.id 中的多条记录进行分组。对于 quest\_poi\_point 中具有相同 questId 的每一新行，你必须手动将此值加 1（0、1、2、3……）。

### idx2

用于对任务 POI 点中的多条记录进行分组，以绘制该兴趣点的多边形。实际点即为每个多边形的角点。

示例任务：Secreat Communication（秘密通讯）。

| QuestID | idx1 | idx2 | x     | y    | VerifiedBuild |
| ------- | ---- | ---- | ----- | ---- | ------------- |
| 8318    | 3    | 0    | -6231 | -51  | 0             |
| 8318    | 3    | 1    | -6236 | -19  | 0             |
| 8318    | 3    | 2    | -6241 | -52  | 0             |
| 8318    | 3    | 3    | -6316 | -282 | 0             |
| 8318    | 3    | 4    | -6413 | -282 | 0             |
| 8318    | 3    | 5    | -6483 | -250 | 0             |
| 8318    | 3    | 6    | -6483 | -217 | 0             |
| 8318    | 3    | 7    | -6326 | -7   | 0             |

**这些点都是蓝色方框上的小角点。idx1 表示由 idx2 的各点定义的区域，用于绘制形状。**

![image](https://user-images.githubusercontent.com/1884642/119476187-bca11b00-bd45-11eb-95e5-876960f24457.png)

### x

地图上问号的 X 位置。

### y

地图上问号的 Y 位置。

### VerifiedBuild

VerifiedBuild
