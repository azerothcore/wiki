# spell\_area

[<-返回至:World](database-world)

**`spell\_area` 表**

此表用于在游戏中的某个区域内对玩家施加特定的法术光环。当任何玩家进入该区域，或以某种方式与任务交互时，该光环都会得到相应的处理。

**表结构**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell][1]              | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [area][2]               | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [quest_start][3]        | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [quest_end][4]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [aura_spell][5]         | MEDIUMINT | SIGNED     | PRI | NO   |         |       |         |
| [racemask][6]           | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [gender][7]             | TINYINT   | UNSIGNED   | PRI | NO   |         |       |         |
| [autocast][8]           | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [quest_start_status][9] | INT       | UNSIGNED   |     | NO   |         |       |         |
| [quest_end_status][10]  | INT       | UNSIGNED   |     | NO   |         |       |         |

[1]: #spell
[2]: #area
[3]: #queststart
[4]: #questend
[5]: #auraspell
[6]: #racemask
[7]: #gender
[8]: #autocast
[9]: #quest_start_status
[10]: #quest_end_status

**字段说明**

### spell

要对玩家施放的法术 ID。参见 [Spell.dbc](spell)。

### area

区域 ID。在游戏内输入 ".gps" 并查找 "Area:" 数值来用于此单元格。另参见 AreaTable.dbc。

### quest\_start

玩家必须以 **quest\_start\_status** 所定义的状态拥有的任务条目。参见 [quest\_template.id](quest_template#id)。

### quest\_end

玩家不得以 **quest\_end\_status** 所定义的状态拥有的任务条目。参见 [quest\_template.id](quest_template#id)。将 **quest\_start** 和 **quest\_end** 都设置为相同的值是无效的。

### aura\_spell

如果设置，此值（加上或减去来自 Spell.dbc 的光环法术 ID）会施加额外条件。

该值具有以下效果：

- **< 0**（负值）如果玩家拥有光环 **-aura\_spell**，则 [spell](#spell) 不会被激活。
- **0** 此列被忽略。
- **> 0**（正值）如果玩家没有光环 **aura\_spell**，则 [spell](#spell) 不会被激活。

### racemask

此 ID 会自动从 [ChrRaces.dbc](chrraces) 调用。此处填写位掩码。

- 0、1791 = 所有种族
- 690（2 + 16 + 32 + 128 + 512）= 仅部落
- 1101（1 + 4 + 8 + 64 + 1024）= 仅联盟

### gender

此条目适用的性别类型。0 = 男，1 = 女，2 = 任意。

### autocast

| Flag | Value | Name                          | Comment                                                                                                                   |
| ---- | ----- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1    | 0x01  | SPELL\_AREA\_FLAG\_AUTOCAST   | 当角色进入区域时是否自动施加该法术。同时防止用户将其移除。                                                                |
| 2    | 0x02  | SPELL\_AREA\_FLAG\_AUTOREMOVE | 当角色**处于**该区域内时是否自动移除该法术（仅与任务更新配合使用）                                                         |

注意：离开区域时法术总是会被移除，SPELL\_AREA\_FLAG\_AUTOREMOVE 对此没有影响。

示例：

- flags = 0：进入时不施加法术（必须手动施加），任务更新时不会自动移除，但离开时会移除。
- flags = 1：进入时自动施加法术，任务更新时不会自动移除，但离开时会移除。
- flags = 2：进入时不施加法术（必须手动施加），任务更新时自动移除，离开时也会移除。
- flags = 3：（默认）进入时自动施加法术，任务更新时自动移除，离开时也会移除。

### quest\_start\_status、quest\_end\_status

在 **quest\_start\_status** 中，你可以定义 **quest\_start** 所需的任务状态掩码。

在 **quest\_end\_status** 中，你可以定义 **quest\_end** 所需的任务状态掩码。

示例：

区域 257 是泰达希尔的一个洞穴。我们想要的效果很简单：当玩家接取 28725 任务时，他在洞穴中拥有该光环。当他完成 28727 任务时，光环消失。

进入洞穴时应拥有法术 92237，条件为：

- 开始任务 28725 处于未完成、已完成或已奖励状态（2 | 8 | 64 = 74）
- 结束任务 28727 未被接取（无）、处于未完成或已完成状态但未被奖励（1 | 2 | 8 = 11）

以下是该示例的 SQL：

```sql
INSERT INTO `spell_area` (`spell`, `area`, `quest_start`, `quest_end`, `autocast`, `quest_start_status`, `quest_end_status`) VALUES 
(92237, 257, 28725, 28727, 1, 74, 11);
```

| Quest Status                       | Flag          | Explanation                                                                         |
| ---------------------------------- | ------------- | ----------------------------------------------------------------------------------- |
| QUEST\_STATUS\_NONE = 0            | 1             | 玩家从未拥有过该任务。他本可以接受，但（还）没有接受。                              |
| QUEST\_STATUS\_COMPLETE = 1        | 2             | 玩家已达成目标，但尚未交任务。                                                      |
| ~~QUEST\_STATUS\_UNAVAILABLE = 2~~ | 4 (NOT USED)  | （未使用）                                                                          |
| QUEST\_STATUS\_INCOMPLETE = 3      | 8             | 玩家尚未达成目标                                                                    |
| ~~QUEST\_STATUS\_AVAILABLE = 4~~   | 16 (NOT USED) | （未使用）                                                                          |
| QUEST\_STATUS\_FAILED = 5          | 32            | 玩家因任何原因未能达成目标，例如超时                                                  |
| QUEST\_STATUS\_REWARDED = 6        | 64            | 玩家已交任务，这属于某种任务完成后的交互                                              |

SQL 示例

对于一个应包含 QUEST\_STATUS\_NONE (1)、QUEST\_STATUS\_COMPLETE (2) 和 QUEST\_STATUS\_INCOMPLETE (8) 的 \`quest\_end\_status\`：

``` sql
-- 等价于 `quest_end_status` = 11
UPDATE `spell_area` SET `quest_end_status`= (1|2|8) WHERE `spell`=XXXXX AND `area`=YYYY;
```

一些示例：

- 某个区域可以让所有玩家平静下来（法术 39331）
- 另一个区域可以每 1 秒完全治疗一次（法术 48591）
- 将玩家传送出某个区域（法术 53141）
- 阵营专属增益，例如在冰冠堡垒中：
- 部落的"加尔鲁什的战歌"（法术 73822）
- 联盟的"乌瑞恩之力"（法术 73828）
- 甚至基于区域的增益，例如区域 440 —— 塔纳利斯。
