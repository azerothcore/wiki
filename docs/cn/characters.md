# characters

[<-返回:角色库](database-characters)

**\`characters\` 表**

这张表保存每个角色的重要静态信息。它用于在游戏中创建玩家对象。

**表结构**

| 字段                      | 类型        | 属性 | 键 | 空 | 默认值           | 额外  | 备注                  |
| -------------------------- | ----------- | ---------- | --- | ---- | ----------------- | ------ | ------------------------ |
| [guid][1]                  | INT         | UNSIGNED   | PRI | NO   | 0                 | Unique | 全局唯一标识符 |
| [account][2]               | INT         | UNSIGNED   |     | NO   | 0                 |        | 账号标识符       |
| [name][3]                  | VARCHAR(12) | SIGNED     |     | NO   |                   |        |                          |
| [race][4]                  | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [class][5]                 | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [gender][6]                | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [level][7]                 | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [xp][8]                    | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [money][9]                 | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [skin][10]                 | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [face][11]                 | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [hairStyle][12]            | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [hairColor][13]            | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [facialStyle][14]          | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [bankSlots][15]            | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [restState][16]            | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [playerflags][17]          | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [position_x][18]           | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [position_y][19]           | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [position_z][20]           | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [map][21]                  | SMALLINT    | UNSIGNED   |     | NO   | 0                 |        | 地图标识符           |
| [instance_id][22]          | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [instance_mode_mask][23]   | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [orientation][24]          | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [taximask][25]             | TEXT        | SIGNED     |     | NO   |                   |        |                          |
| [online][26]               | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [cinematic][27]            | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totaltime][28]            | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [leveltime][29]            | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [logout_time][30]          | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [is_logout_resting][31]    | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [rest_bonus][32]           | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [resettalents_cost][33]    | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [resettalents_time][34]    | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [trans_x][35]              | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_y][36]              | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_z][37]              | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_o][38]              | FLOAT       | SIGNED     |     | NO   | 0                 |        |                          |
| [transguid][39]            | MEDIUMINT   | SIGNED     |     | NO   | 0                 |        |                          |
| [extra_flags][40]          | SMALLINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [stable_slots][41]         | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [at_login][42]             | SMALLINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [zone][43]                 | SMALLINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [death_expire_time][44]    | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [taxi_path][45]            | TEXT        | SIGNED     |     | YES  |                   |        |                          |
| [arenaPoints][46]          | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totalHonorPoints][47]     | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [todayHonorPoints][48]     | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [yesterdayHonorPoints][49] | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totalKills][50]           | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [todayKills][51]           | SMALLINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [yesterdayKills][52]       | SMALLINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [chosenTitle][53]          | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [knownCurrencies][54]      | BIGINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [watchedFaction][55]       | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [drunk][56]                | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [health][57]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power1][58]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power2][59]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power3][60]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power4][61]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power5][62]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power6][63]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power7][64]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [latency][65]              | MEDIUMINT   | UNSIGNED   |     | NO   | 0                 |        |                          |
| [talentGroupsCount][66]    | TINYINT     | UNSIGNED   |     | NO   | 1                 |        |                          |
| [activeTalentGroup][67]    | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [exploredZones][68]        | LONGTEXT    | SIGNED     |     | YES  |                   |        |                          |
| [equipmentCache][69]       | LONGTEXT    | SIGNED     |     | YES  |                   |        |                          |
| [ammoId][70]               | INT         | UNSIGNED   |     | NO   | 0                 |        |                          |
| [knownTitles][71]          | LONGTEXT    | SIGNED     |     | YES  |                   |        |                          |
| [actionBars][72]           | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [grantableLevels][73]      | TINYINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [order][74]                | TINYINT     | SIGNED     |     | YES  |                   |        |                          |
| [creation_date][75]        | TIMESTAMP   | SIGNED     |     | NO   | CURRENT_TIMESTAMP |        |                          |
| [deleteInfos_Account][76]  | INT         | UNSIGNED   |     | YES  |                   |        |                          |
| [deleteInfos_Name][77]     | VARCHAR(12) | SIGNED     |     | YES  |                   |        |                          |
| [deleteDate][78]           | INT         | UNSIGNED   |     | YES  |                   |        |                          |
| [innTriggerId][79]         | INT         | UNSIGNED   |     | NO   |                   |        |                          |
| [extraBonusTalentCount][80] | INT        |            |     | NO   | 0                 |        |                          |

[1]: #guid
[2]: #account
[3]: #name
[4]: #race
[5]: #class
[6]: #gender
[7]: #level
[8]: #xp
[9]: #money
[10]: #skin
[11]: #face
[12]: #hairstyle
[13]: #haircolor
[14]: #facialstyle
[15]: #bankslots
[16]: #reststate
[17]: #playerflags
[18]: #positionx
[19]: #positiony
[20]: #positionz
[21]: #map
[22]: #instanceid
[23]: #instancemodemask
[24]: #orientation
[25]: #taximask
[26]: #online
[27]: #cinematic
[28]: #totaltime
[29]: #leveltime
[30]: #logouttime
[31]: #islogoutresting
[32]: #restbonus
[33]: #resettalentscost
[34]: #resettalentstime
[35]: #transx
[36]: #transy
[37]: #transz
[38]: #transo
[39]: #transguid
[40]: #extraflags
[41]: #stableslots
[42]: #atlogin
[43]: #zone
[44]: #deathexpiretime
[45]: #taxipath
[46]: #arenaPoints
[47]: #totalhonorpoints
[48]: #todayhonorpoints
[49]: #yesterdayhonorpoints
[50]: #totalkills
[51]: #todaykills
[52]: #yesterdayKills
[53]: #chosentitle
[54]: #knowncurrencies
[55]: #watchedfaction
[56]: #drunk
[57]: #health
[58]: #power
[59]: #power
[60]: #power
[61]: #power
[62]: #power
[63]: #power
[64]: #power
[65]: #latency
[66]: #talentgroupscount
[67]: #activetalentgroup
[68]: #exploredzones
[69]: #equipmentcache
[70]: #ammoid
[71]: #knownTitles
[72]: #actionbars
[73]: #grantablelevels
[74]: #order
[75]: #creationdate
[76]: #deleteinfosaccount
[77]: #deleteinfosname
[78]: #deletedate
[79]: #inntriggerid
[80]: #extrabonustalentcount

**字段说明**

### guid

角色的全局唯一标识符。此数字必须唯一，是区分不同角色的最佳方式。

### account

此角色所属的账号 ID。参见 auth 数据库中的 [account.id](account#id)。

### name

角色的名称。最大长度为 12 个字符。

### race

角色的种族。参见 [ChrRaces.dbc](chrraces)。

### class

角色的职业：[ChrClasses.dbc](chrclasses)。

### gender

角色的性别。

| Id  | 性别      |
| --- | ----------- |
| 0   | 男        |
| 1   | 女      |
| 2   | 未知（?） |

`2` 特别见于 [creature\_model\_info](creature_model_info) 表中。

### level

角色的等级。

### xp

该角色已获得的、距离升到下一级所需的经验值。

### money

该角色拥有的铜币数量。

### skin

包含角色肤色的数据。
skinColor = playerbytes  % 256

### face

包含角色脸型的数据。
faceStyle = (playerbytes &gt;&gt; 8) % 256

### hairStyle

包含角色发型的数据。
hairStyle = (playerbytes &gt;&gt; 16) % 256

### hairColor

包含角色发色的数据。
hairColor = (playerbytes &gt;&gt; 24) % 256

### facialStyle

包含角色面部毛发（胡须）的数据。
facialHair = playerBytes2 % 256

### bankSlots

`field-no-description|15`

### restState

`field-no-description|16`

### playerFlags

一个表示玩家拥有哪些 Player 标志的位掩码。每个位控制一个不同的标志，要组合标志，你可以把想要启用的标志值相加，从而激活相应的位。

| 标志     |            | 名称                          | 备注                                                                           |
| -------- | ---------- | ----------------------------- | --------------------------------------------------------------------------------- |
| 1        | 0x00000001 | PLAYER_FLAGS_GROUP_LEADER     |                                                                                   |
| 2        | 0x00000002 | PLAYER_FLAGS_AFK              |                                                                                   |
| 4        | 0x00000004 | PLAYER_FLAGS_DND              |                                                                                   |
| 8        | 0x00000008 | PLAYER_FLAGS_GM               |                                                                                   |
| 16       | 0x00000010 | PLAYER_FLAGS_GHOST            |                                                                                   |
| 32       | 0x00000020 | PLAYER_FLAGS_RESTING          |                                                                                   |
| 64       | 0x00000040 | PLAYER_FLAGS_UNK7             |                                                                                   |
| 128      | 0x00000080 | PLAYER_FLAGS_UNK8             | 3.0.3 之前是 PLAYER_FLAGS_FFA_PVP 标志，用于 FFA PVP 状态                             |
| 256      | 0x00000100 | PLAYER_FLAGS_CONTESTED_PVP    | 玩家参与过 PvP 战斗，将受到有争议守卫的攻击 |
| 512      | 0x00000200 | PLAYER_FLAGS_IN_PVP           |                                                                                   |
| 1024     | 0x00000400 | PLAYER_FLAGS_HIDE_HELM        |                                                                                   |
| 2048     | 0x00000800 | PLAYER_FLAGS_HIDE_CLOAK       |                                                                                   |
| 4096     | 0x00001000 | PLAYER_FLAGS_PLAYED_LONG_TIME | 已游玩较长时间                                                                  |
| 8192     | 0x00002000 | PLAYER_FLAGS_TOO_LONG         | 已游玩过长时间                                                              |
| 16384    | 0x00004000 | PLAYER_FLAGS_IS_OUT_OF_BOUNDS |                                                                                   |
| 32768    | 0x00008000 | PLAYER_FLAGS_DEVELOPER        | 某物的前缀？                                                             |
| 65536    | 0x00010000 | PLAYER_FLAGS_UNK17            | 3.0.3 之前是 PLAYER_FLAGS_SANCTUARY 标志，用于玩家进入庇护所                |
| 131072   | 0x00020000 | PLAYER_FLAGS_TAXI_BENCHMARK   | 出租车基准测试模式（开/关）（2.0.1）                                              |
| 262144   | 0x00040000 | PLAYER_FLAGS_PVP_TIMER        | 3.0.2，PVP 计时器激活（在你手动禁用 PVP 之后）                          |
| 524288   | 0x00080000 | PLAYER_FLAGS_UNK20            |                                                                                   |
| 1048576  | 0x00100000 | PLAYER_FLAGS_UNK21            |                                                                                   |
| 2097152  | 0x00200000 | PLAYER_FLAGS_UNK22            |                                                                                   |
| 4194304  | 0x00400000 | PLAYER_FLAGS_COMMENTATOR2     |                                                                                   |
| 8388608  | 0x00800000 | PLAYER_ALLOW_ONLY_ABILITY     | 被剑刃风暴和杀戮盛宴使用                                              |
| 16777216 | 0x01000000 | PLAYER_FLAGS_UNK25            | 在 tab 上禁用所有近战技能，包括自动攻击                                 |
| 33554432 | 0x02000000 | PLAYER_FLAGS_NO_XP_GAIN       |                                                                                   |

### position\_x

角色位置的 x 坐标。

### position\_y

角色位置的 y 坐标。

### position\_z

角色位置的 z 坐标。

### map

角色所在的地图 ID。

### instance\_id

角色当前所在并绑定的副本实例 ID。

### instance\_mode\_mask

玩家当前所处的副本难度。此字段是位掩码。各值可以组合，但四个值中一次只能使用两个。此描述可能并非 100% 正确。

| 标志 | 备注 |
| ---- | ------- |
| 0    | 普通  |
| 1    | 英雄  |
| 16   | 10 人  |
| 32   | 25 人  |

### orientation

角色面向的方向。（北 = 0.0，南 = 3.14159）

### taximask

已探索的飞行点节点，用空格分隔。

### online

记录角色是在线（1）还是离线（0）。

### cinematic

布尔值 1 或 0，控制开场动画是否已经播放过。

### totaltime

角色在世界中活跃的总时间，以秒为单位。

### leveltime

角色在当前等级于世界中所花费的总时间，以秒为单位。

### logout\_time

角色上次下线的时间，以 Unix 时间表示。

### is\_logout\_resting

布尔值 1 或 0，控制角色当前是否处于休息区域。

### rest_bonus

累积的休息经验加成，用于获得经验。

### resettalents\_cost

角色重置天赋所需的费用，以铜币计。

### resettalents\_time

`field-no-description|34`

### trans\_x

角色上次保存时所在载具的 x 坐标。

### trans\_y

角色上次保存时所在载具的 y 坐标。

### trans\_z

角色上次保存时所在载具的 z 坐标。

### trans\_o

角色上次保存时所在载具的朝向。

### transguid

角色上次保存时所在载具的全局唯一标识符。

### extra\_flags

这些标志控制某些玩家特定属性，主要是 GM 功能。

| 标志 |            | 名称                           | 描述                                         |
| ---- | ---------- | ------------------------------ | --------------------------------------------------- |
| 1    | 0x00000001 | PLAYER_EXTRA_GM_ON             | 定义 GM 状态                                    |
| 2    | 0x00000002 | PLAYER_EXTRA_GM_ACCEPT_TICKETS | 不再使用。定义是否接受工单      |
| 4    | 0x00000004 | PLAYER_EXTRA_ACCEPT_WHISPERS   | 定义是否接受密语                    |
| 8    | 0x00000008 | PLAYER_EXTRA_TAXICHEAT         | 设置飞行点作弊                                      |
| 16   | 0x00000010 | PLAYER_EXTRA_GM_INVISIBLE      | 定义 GM 可见性                               |
| 32   | 0x00000020 | PLAYER_EXTRA_GM_CHAT           | 在聊天消息中显示 GM 徽章                      |
| 64   | 0x00000040 | PLAYER_EXTRA_HAS_310_FLYER     | 标记玩家是否已拥有 310% 速度的飞行坐骑 |
| 256  | 0x00000100 | PLAYER_EXTRA_PVP_DEATH         | 在创建尸体前存储 PvP 死亡状态        |

### stable\_slots

在兽栏管理员处可用的（已购买的）兽栏栏位。

### at\_login

此字段是一个位掩码，控制玩家以该角色登录时执行的不同操作。

| 标志 |      | 名称                       | 描述                          |
| ---- | ---- | -------------------------- | ------------------------------------ |
| 1    | 0x01 | AT_LOGIN_RENAME            | 强制角色改名       |
| 2    | 0x02 | AT_LOGIN_RESET_SPELLS      | 重置法术（也包括专业技能）   |
| 4    | 0x04 | AT_LOGIN_RESET_TALENTS     | 重置天赋                        |
| 8    | 0x08 | AT_LOGIN_CUSTOMIZE         | 自定义角色                 |
| 16   | 0x10 | AT_LOGIN_RESET_PET_TALENTS | 重置宠物天赋                    |
| 32   | 0x20 | AT_LOGIN_FIRST             | 在首次登录时设置，之后移除 |
| 64   | 0x40 | AT_LOGIN_CHANGE_FACTION    | 更换阵营                       |
| 128  | 0x80 | AT_LOGIN_CHANGE_RACE       | 更换种族                          |

如需同时执行多个操作，请将各值相加。

### zone

角色所在的区域 ID。

### death\_expire\_time

角色处于灵魂形态时，若服务器崩溃或客户端退出，其可以被复活的时间，以 Unix 时间表示。

### taxi\_path

存储玩家当前飞行路径（[TaxiPath.dbc](https://wowdev.wiki/DB/TaxiPath)），如果玩家在下线时正处于飞行路径上。

### arenaPoints

该角色累积的竞技场点数数量，将在下次竞技场点数分配时获得。

### totalHonorPoints

该角色获得的荣誉点总数。

### todayHonorPoints

该角色今天获得的荣誉点数量。

### yesterdayHonorPoints

该角色昨天获得的荣誉点数量。

### totalKills

该角色击杀的玩家数量。

### todayKills

该角色今天击杀的玩家数量。

### yesterdayKills

该角色昨天击杀的玩家数量。

### chosenTitle

当前头衔，使用 bit_index 字段（[CharTitles.dbc](https://wowdev.wiki/DB/CharTitles) 中的 InGameOrder）。

### knownCurrencies

已知货币（即要列在货币标签页中的内容），BitIndexes 的位掩码，参见 [CurrencyTypes.dbc](https://wowdev.wiki/DB/CurrencyTypes)。

### watchedFaction

在经验条处追踪的阵营（使用声望 ID，参见 [Faction.dbc](faction)）。

### drunk

角色的醉酒状态，0-100

-   0 = 清醒
-   1-49 = 微醺
-   50-89 = 醉酒
-   90-100 = 烂醉

### health

角色当前的生命值。

### power

角色当前的能量（角色保存时的快照）。

| 字段  | 能量名称  |
| ------ | ----------- |
| power1 | 法力        |
| power2 | 怒气        |
| power3 | 集中值       |
| power4 | 能量      |
| power5 | 快乐值   |
| power6 | 符文       |
| power7 | 符文能量 |

### latency

该角色截至上次更新的延迟（或 ping），以毫秒为单位。

### talentGroupsCount

该角色可访问的专精数量。默认值为 1。当前支持的最大值为 2。绝不应为 0（这是双天赋系统出现之前创建的角色的标志）。

### activeTalentGroup

该角色当前激活的专精，spec = 0 表示第一专精，spec = 1 表示第二专精。

### exploredZones

已探索区域的位掩码（1 位表示已探索，0 位表示未探索）。

### equipmentCache

角色的装备和背包缓存。

### ammoId

弹药物品的[模板 ID](item_template#entry)。

### knownTitles

包含已知头衔的数据，存储在 6 个 16 位整数中。要计算某个 knownTitle 位于这 6 个整数中的哪一个，你可以这样做：我们从 [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles) 中选取一个头衔，以大法师（Archmage）头衔为例：

| TitleID | UnkRef? | MaleTitle   | FemaleTitle | InGameOrder |
| ------- | ------- | ----------- | ----------- | ----------- |
| 93      | 0       | Archmage %s | Archmage %s | 61          |

我们使用 InGameOrder 来计算头衔存储在 6 个（16 位）整数中的哪一个：

```
InGameOrder / 32 = X
61 / 32 = **1,90625** (1 - 请**不要**对该值取整！)
```

因此第 1 个整数存储该头衔。由于计数从 **0** 到 5，它将是 "0 **TITLE_BIT** 0 0 0 0"。

那么哪个位存储该头衔呢？我们使用取模来计算。

```
InGameOrder Modulo 32 = X
61 Mod 32 = **29**
```
因此第 29 位存储该头衔。即 2 ^ 29 = 536870912。这个位存储大法师头衔。这意味着如果你**只**拥有大法师头衔，characters.knownTitles 将是 "0 536870912 0 0 0 0"。

### actionBars

一个位掩码，包含玩家可见的动作条。

| 标志 |            | 备注          |
| ---- | ---------- | ---------------- |
| 1    | 0x00000001 | 左下动作条  |
| 2    | 0x00000002 | 右下动作条 |
| 4    | 0x00000004 | 右侧动作条        |
| 8    | 0x00000008 | 右侧动作条 2      |

### grantableLevels

招募战友（Recruit A Friend）相关内容。

### order

用于改变角色在选择角色界面中显示顺序的字段。order 字段优先使用，然后才是 [characters.guid](characters#guid)，这意味着如果账号所有角色的 order 列都为 NULL，则默认按 [characters.guid](characters#guid) 排序。

### creation\_date

角色的创建日期和时间。格式为 YYY-MM-DD HH:MM:SS，按服务器时间。

### deleteInfos\_Account

如果角色被删除且 worldserver.conf 中的 CharDelete.Method 设置为 1，则存储账号 ID。

### deleteInfos\_Name

如果角色被删除且 worldserver.conf 中的 CharDelete.Method 设置为 1，则存储角色名称。

### deleteDate

存储角色被删除的日期，前提是 worldserver.conf.dist 中的 CharDelete.Method 设置为 1。worldserver 会将其与 worldserver.conf.dist 中的 CharDelete.KeepDays 进行比较。如果该值低于 deleteDate + CharDelete.KeepDays，角色将被清除。

### innTriggerId

角色当前绑定休息地点的旅店区域触发器 ID（在旅店休息时设置）。如果未在旅店休息则为 `0`。

### extraBonusTalentCount

授予角色的、超出升级所得之外的天赋点数量。
