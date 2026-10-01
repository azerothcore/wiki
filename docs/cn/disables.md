# disables

[<-返回:世界](database-world)

**\`disables\` 表**

此表用于禁用副本/战场/法术等。

**表结构**

| 字段           | 类型         | 属性 | 键 | 空 | 默认值 | 额外 | 注释 |
| --------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [sourceType][1] | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [entry][2]      | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [flags][3]      | TINYINT      | UNSIGNED   |     | NO   | 0       |       |         |
| [params_0][4]   | VARCHAR(255) |            |     | NO   |         |       |         |
| [params_1][5]   | VARCHAR(255) |            |     | NO   |         |       |         |
| [comment][6]    | VARCHAR(255) |            |     | NO   |         |       |         |

[1]: #sourcetype
[2]: #entry
[3]: #flags
[4]: #params0
[5]: #params1
[6]: #comment

**字段说明**

### sourceType

| 值 | 类型                              |
| ----- | --------------------------------- |
| 0     | DISABLE_TYPE_SPELL                |
| 1     | DISABLE_TYPE_QUEST                |
| 2     | DISABLE_TYPE_MAP                  |
| 3     | DISABLE_TYPE_BATTLEGROUND         |
| 4     | DISABLE_TYPE_ACHIEVEMENT_CRITERIA |
| 5     | DISABLE_TYPE_OUTDOORPVP           |
| 6     | DISABLE_TYPE_VMAP                 |
| 7     | DISABLE_TYPE_MMAP                 |
| 8     | DISABLE_TYPE_LFG_MAP              |
| 9     | DISABLE_TYPE_GAME_EVENT           |
| 10    | DISABLE_TYPE_LOOT                 |

### entry

法术/任务/地图/战场/成就/地图/游戏事件/物品的条目。

***如果 sourceType = DISABLE_TYPE_SPELL:***

法术的条目

***如果 sourceType = DISABLE_TYPE_QUEST:***

[quest_template.id](quest_template#id)

***如果 sourceType = DISABLE_TYPE_MAP:***

***如果 sourceType = DISABLE_TYPE_VMAP:***

***如果 sourceType = DISABLE_TYPE_MMAP:***

***如果 sourceType = DISABLE_TYPE_OUTDOORPVP:***

***如果 sourceType = DISABLE_TYPE_LFG_MAP:***

地图的条目

***如果 sourceType = DISABLE_TYPE_ACHIEVEMENT_CRITERIA:***

成就的条目

***如果 sourceType = DISABLE_TYPE_GAME_EVENT:***

[game_event.eventEntry](game_event#evententry)

***如果 sourceType = DISABLE_TYPE_LOOT:***

[item_template.entry](item_template#entry)

### flags

如果 sourceType = DISABLE_TYPE_SPELL：指定该法术对谁禁用。

| 值 | 类型                                                                                          |
| ----- | --------------------------------------------------------------------------------------------- |
| 0     | 法术启用                                                                                 |
| 1     | 法术对玩家禁用                                                                    |
| 2     | 法术对生物禁用                                                                  |
| 4     | 法术对宠物禁用                                                                       |
| 8     | 法术完全禁用（用于 DBC 中已不存在的法术）                        |
| 16    | 法术对 MapId 禁用                                                                      |
| 32    | 法术对 AreaId 禁用                                                                     |
| 64    | 此法术的视线 (LOS) 被禁用（取代 "vmap.ignoreSpellIds" 配置选项） |

示例：INSERT INTO \`disables\` VALUES (0, 8921, (1+16+32), "571,1", "1519", "Moonfire Example");

这将在地图 571、1 和区域 1519 中禁用对玩家生效的月火术 (Moonfire) (8921)。

***如果 sourceType = DISABLE_TYPE_MAP:***

指定禁用哪种类型的地图（5人/10人/英雄等）。

| 值 | 类型                                                        |
| ----- | ----------------------------------------------------------- |
| 1     | DUNGEON_STATUS_FLAG_NORMAL 或 RAID_STATUS_FLAG_10MAN_NORMAL |
| 2     | DUNGEON_STATUS_FLAG_HEROIC 或 RAID_STATUS_FLAG_25MAN_NORMAL |
| 4     | RAID_STATUS_FLAG_10MAN_HEROIC                               |
| 8     | RAID_STATUS_FLAG_25MAN_HEROIC                               |

该值是特定地图有效模式的位掩码，因此 15 在某些地图上并非有效的掩码，只有对相应地图实际可能的模式才是有效的。

***如果 sourceType = DISABLE_TYPE_VMAP:***

指定应在哪张地图上禁用 vMap

| 值 | 类型                  |
| ----- | --------------------- |
| 1     | VMAP_DISABLE_AREAFLAG |
| 2     | VMAP_DISABLE_HEIGHT   |
| 4     | VMAP_DISABLE_LOS      |
| 8     | VMAP_LIQUIDSTATUS     |

示例：INSERT INTO \`disables\` VALUES (6, 1, (2 + 4), 0, 0, "Disable Kalimdor vMaps");

这将在整个卡利姆多禁用 vMaps。

***如果 sourceType = DISABLE_TYPE_QUEST:***

***如果 sourceType = DISABLE_TYPE_ACHIEVEMENT_CRITERIA:***

***如果 sourceType = DISABLE_TYPE_OUTDOORPVP:***

***如果 sourceType = DISABLE_TYPE_MMAP:***

***如果 sourceType = DISABLE_TYPE_LFG_MAP:***

***如果 sourceType = DISABLE_TYPE_GAME_EVENT:***

***如果 sourceType = DISABLE_TYPE_LOOT:***

不需要 flags，只需以 \`flags\`=0 将条目添加到表中即可。

### params_0

如果使用 DISABLE_TYPE_SPELL 则为 MapId，对于所有地图为 0。

### params_1

如果使用 DISABLE_TYPE_SPELL 则为 AreaId，对于所有区域为 0。

### comment

关于某个东西为何被禁用的注释，或任何你想要的其他文本。
