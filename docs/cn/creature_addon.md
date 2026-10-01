# creature\_addon

[<-返回至:World](database-world)

**`creature\_addon` 表**

creature\_addon 和 creature\_template\_addon 表定义了在生物加载时要应用的各种内容。这些"各种内容"可以例如是让生物骑乘、让它做出某种表情、让它显示光环效果等等。通过使用此表中的字段，可以改变生物外在视觉外观的许多方面。creature\_template\_addon 表会影响使用该生物模板 ID 的所有生物，而 creature\_addon 表则影响单个刷新的生物（因此使用相同模板的两个生物可以看起来不同）。

注意：如果 creature\_addon 记录与 creature\_template\_addon 记录在同一个生物上重叠，creature\_addon 记录将覆盖 creature\_template\_addon 记录。

提示：此表的数据很大程度上不完整，大多只是对客户端从服务器接收到的内容的复述。关于所有可能的值，本文仍在完善中（WIP）。

**表结构**

| 字段                          | 类型          | 属性     | 键   | 空   | 默认值 | 额外 | 注释 |
| ----------------------------- | ------------- | -------- | ---- | ---- | ------ | ---- | ---- |
| [guid/entry][1]              | INT/MEDIUMINT | UNSIGNED | PRI  | NO   |        |      |      |
| [path_id][2]                 | INT           | UNSIGNED |      | NO   |        |      |      |
| [mount][3]                   | MEDIUMINT     | UNSIGNED |      | NO   |        |      |      |
| [bytes1][4]                  | INT           | UNSIGNED |      | NO   |        |      |      |
| [bytes2][5]                  | INT           | UNSIGNED |      | NO   |        |      |      |
| [emote][6]                   | INT           | UNSIGNED |      | NO   |        |      |      |
| [visibilityDistanceType][10] | TINYINT       | UNSIGNED |      | NO   |        |      |      |
| [auras][11]                  | text          |           |      | YES  |        |      |      |

[1]: #guidentry
[2]: #pathid
[3]: #mount
[4]: #bytes1
[5]: #bytes2
[6]: #emote
[10]: #visibilityDistanceType
[11]: #auras

**字段说明**

### guid/entry

对于 creature\_addon，此字段表示一个唯一的生物 GUID。它只会影响 GUID 与此处指定值匹配的那个生物。
对于 creature\_template\_addon，此字段表示 [creature\_template.entry](creature_template#entry)。它会影响所有使用该模板 entry 刷新的生物。

### path\_id

如果生物使用路径点（waypoint）路径移动，此字段保存该生物要遵循的路径的 waypoint\_data.id。

### mount

用于让生物看起来处于骑乘状态的坐骑模型 ID。此处的值会覆盖生物的单位字段 UNIT\_FIELD\_MOUNTDISPLAYID 的值。

### bytes1

此处的值会覆盖生物的单位字段 UNIT\_FIELD\_BYTES\_1 的值。

已知值列表及其对生物产生的视觉影响：

- 1 = 坐立
- 2 = 坐在椅子上
- 3 = 睡眠
- 4 = 坐在矮椅子上
- 5 = 坐在中等椅子上
- 6 = 坐在高椅子上
- 7 = 将生命条显示为空的（与死亡状态表情组合使用，让生物看起来像死了）
- 8 = 让怪物跪下
- 9 = 将生物沉入地面以下
- 54432 = 悬浮模式
- 50331648 = 悬浮模式 2

### bytes2

此处的值会覆盖生物的单位字段 UNIT\_FIELD\_BYTES\_2 的值。

注意：//除非另有指定，生物总是准备好近战武器（如果有）

少数已知值列表及其对生物产生的视觉影响：

- 0 = STATE\_UNARMED（未准备武器，武器在身体两侧/背后）
- 1 = STATE\_MELEE（双手准备好近战武器）
- 2 = STATE\_RANGED（双手准备好远程武器，近战武器在身体两侧）

### emote

生物应持续执行的表情 ID。

常用表情 ID 列表及其作用可以在[此处](emotes)找到。

### visibilityDistanceType

此字段控制生物的可见距离：

- Normal = 0,  100.0f  // 默认可见距离，大陆上为 100 码
- Tiny = 1,  25.0f
- Small = 2,  50.0f
- Large = 3, 200.0f
- Gigantic = 4, 400.0f
- Infinite = 5, SIZE_OF_GRIDS // 可见对象的最大距离

### auras

此字段控制要应用于生物的任何光环（无论在效果上还是视觉上）。要应用多个光环，你可以添加更多光环条目，每个条目之间用空格分隔。请记住，一个法术可能会施加多个光环。

有用的光环条目列表（示例）：

- '16380' - 让生物隐身。
- '18950' - 让生物侦测到其他隐身的单位（玩家或生物）。
- '16380 18950' - 以上两个光环
