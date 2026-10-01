# spawn\_group\_template

[<-返回至:World](database-world)

**`spawn\_group\_template` 表**

此表定义刷新组模板及其名称和行为标志。刷新组允许将生物和游戏对象的刷新进行逻辑分组，并按组控制重生行为。

**表结构**

| Field                     | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [groupId](#groupid)       | INT          | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [groupName](#groupname)   | VARCHAR(100) |            |     | NO   | NULL    |       |         |
| [groupFlags](#groupflags) | INT          | UNSIGNED   |     | NO   | 0       |       |         |

**字段说明**

### groupId

这是该组的组 ID。它必须是唯一的数字。组 0 和组 1 是保留的系统组：

- 组 0："Default Group"（默认组）——默认使用动态重生的系统组。
- 组 1："Legacy Group"（旧版组）——使用兼容模式（旧版重生行为）的系统组。

### groupName

这是对该组的描述性名称。

### groupFlags

这些是应用于该组的标志。

| Flag                                   | Number | Description                                                                                                                                          |
| -------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| SPAWNGROUP\_FLAG\_NONE                 | 0x00   | 不应用任何标志                                                                                                                                        |
| SPAWNGROUP\_FLAG\_SYSTEM               | 0x01   | 此组是系统组。系统组无法通过 GM 命令手动刷新或取消刷新。                                                                                               |
| SPAWNGROUP\_FLAG\_COMPATIBILITY\_MODE  | 0x02   | 此组使用旧版重生行为：生物的尸体一直保留在地图上，直到重生计时器到期，然后生物原地重生。当未设置此标志时，生物死亡后会被完全移除，并由重生调度器重新创建。 |
| SPAWNGROUP\_FLAG\_MANUAL\_SPAWN        | 0x04   | 默认情况下，核心不会刷新此组。脚本可以通过 SmartAI 动作或 GM 命令按需手动刷新/取消刷新这些组。                                                        |
| SPAWNGROUP\_FLAG\_DYNAMIC\_SPAWN\_RATE | 0x08   | 此组将应用动态刷新速率（默认情况下，任务相关的生物/游戏对象和采集点使用此功能）。                                                                      |
| SPAWNGROUP\_FLAG\_ESCORTQUESTNPC       | 0x10   | 此组包含护送任务 NPC。这进一步增强了动态刷新功能，使重生计时从任务接取、护送开始时起算。                                                               |

> worldserver 配置选项 `Respawn.ForceCompatibilityMode` 可以强制所有刷新使用旧版（兼容模式）行为，而不管组标志如何。
