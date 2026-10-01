# creature_template

[<-返回：世界](database-world)

**\`creature_template\` 表**

该表包含生物的描述。每个被刷新的生物都是此表中某个模板的实例，这意味着每个生物都必须在此表中定义。

**表结构**

| Field                                              | Type               | Null | Key | Default | Extra | Comment                              |
| -------------------------------------------------- | ------------------ | ---- | --- | ------- | ----- | ------------------------------------ |
| [entry](#entry)                                    | MEDIUMINT UNSIGNED | NO   | PRI | 0       |       |                                      |
| [difficulty_entry_1](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [difficulty_entry_2](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [difficulty_entry_3](#difficultyentryx)            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [KillCredit1](#killcredit1)                        | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [KillCredit2](#killcredit2)                        | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [name](#name)                                      | char(100)          | NO   | MUL | 0       |       |                                      |
| [subname](#subname)                                | char(100)          | YES  |     | (NULL)  |       |                                      |
| [IconName](#iconname)                              | char(100)          | YES  |     | (NULL)  |       |                                      |
| [gossip_menu_id](#gossipmenuid)                    | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [minlevel](#minlevel)                              | TINYINT UNSIGNED   | NO   |     | 1       |       |                                      |
| [maxlevel](#maxlevel)                              | TINYINT UNSIGNED   | NO   |     | 1       |       |                                      |
| [exp](#exp)                                        | SMALLINT           | NO   |     | 0       |       |                                      |
| [faction](#faction)                                | SMALLINT UNSIGNED  | NO   |     | 0       |       |                                      |
| [npcflag](#npcflag)                                | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [speed_walk](#speedwalk)                           | FLOAT              | NO   |     | 1       |       | 2.5/2.5 的结果，最常见的值 |
| [speed_run](#speedrun)                             | FLOAT              | NO   |     | 1.14286 |       | 8.0/7.0 的结果，最常见的值 |
| [speed_swim](#speedswim)                           | FLOAT              | NO   |     | 1       |       |                                      |
| [speed_flight](#speedflight)                       | FLOAT              | NO   |     | 1       |       |                                      |
| [detection_range](#detectionrange)                 | FLOAT              | NO   |     | 20      |       |                                      |
| [rank](#rank)                                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [dmgschool](#dmgschool)                            | TINYINT            | NO   |     | 0       |       |                                      |
| [BaseAttackTime](#baseattacktime)                  | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [RangeAttackTime](#rangeattacktime)                | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [BaseVariance](#basevariance)                      | FLOAT              | NO   |     | 1       |       |                                      |
| [RangeVariance](#rangevariance)                    | FLOAT              | NO   |     | 1       |       |                                      |
| [unit_class](#unitclass)                           | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [unit_flags](#unitflags)                           | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [unit_flags2](#unitflags2)                         | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [dynamicflags](#dynamicflags)                      | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [family](#family)                                  | TINYINT            | NO   |     | 0       |       |                                      |
| [type](#type)                                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [type_flags](#typeflags)                           | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [lootid](#lootid)                                  | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [pickpocketloot](#pickpocketloot)                  | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [skinloot](#skinloot)                              | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [PetSpellDataId](#petspelldataid)                  | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [VehicleId](#vehicleid)                            | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [mingold](#mingold)                                | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [maxgold](#maxgold)                                | MEDIUMINT UNSIGNED | NO   |     | 0       |       |                                      |
| [AIName](#ainame)                                  | char(64)           | NO   |     |         |       |                                      |
| [MovementType](#movementtype)                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [HoverHeight](#hoverheight)                        | FLOAT              | NO   |     | 1       |       |                                      |
| [HealthModifier](#healthmodifier)                  | FLOAT              | NO   |     | 1       |       |                                      |
| [ManaModifier](#manamodifier)                      | FLOAT              | NO   |     | 1       |       |                                      |
| [ArmorModifier](#armormodifier)                    | FLOAT              | NO   |     | 1       |       |                                      |
| [DamageModifier](#damagemodifier)                  | FLOAT              | NO   |     | 1       |       |                                      |
| [ExperienceModifier](#experiencemodifier)          | FLOAT              | NO   |     | 1       |       |                                      |
| [RacialLeader](#racialleader)                      | TINYINT UNSIGNED   | NO   |     | 0       |       |                                      |
| [movementId](#movementid)                          | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [RegenHealth](#regenhealth)                        | TINYINT UNSIGNED   | NO   |     | 1       |       |                                      |
| [CreatureImmunitiesId](#creatureimmunitiesid)      | INT UNSIGNED       | NO   |     | 0       |       | 引用 creature_immunities 表 |
| [flags_extra](#flagsextra)                         | INT UNSIGNED       | NO   |     | 0       |       |                                      |
| [ScriptName](#scriptname)                          | char(64)           | NO   |     |         |       |                                      |
| [VerifiedBuild](#verifiedbuild)                    | SMALLINT           | YES  |     | 0       |       |                                      |

---

**字段说明**

#### entry

生物的唯一 ID。

#### difficulty_entry_x

| name                                                      | entry | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| --------------------------------------------------------- | ----- | ------------------ | ------------------ | ------------------ |
| [Anomalus](http://www.wowhead.com/npc=26763/anomalus)     | 26763 | 30529              | 0                  | 0                  |
| [Sindragosa](http://www.wowhead.com/npc=36853/sindragosa) | 36853 | 38265              | 38266              | 38267              |

Anomalus 是位于魔枢（The Nexus）的 5 人本 Boss。你可以在两种难度（普通地下城和英雄地下城）下与他对战。根据难度类型的不同，Boss 拥有不同的属性，如生命值和伤害。以 Anomalus 为例，当你在普通难度下与他战斗时使用条目 26763 的信息，而在英雄难度下战斗时使用条目 30529。

Sindragosa 是位于冰冠堡垒（Icecrown Citadel）的团队副本 Boss 战，由于 3.2 补丁引入了英雄团队副本模式（10 人普通/英雄、25 人普通/英雄），她可以在 4 种不同的难度下被挑战。根据难度类型的不同，她必须拥有不同的属性。所以如果你在 10 人普通团队副本中看到她，她将使用条目 36853 的信息；在 25 人普通团队副本中使用条目 38265，以此类推。这与帕奇维克（Patchwerk）和 XT-002 拆解者（XT-002 Deconstructor）等团队副本 Boss 形成鲜明对比，这两个 Boss 分别位于纳克萨玛斯（Naxxramas）和奥杜尔（Ulduar），它们只有两种团队副本模式（10 人"普通"/25 人"普通"）。奥杜尔团队副本中的困难模式（Hardmode）没有自己的模板，因为游戏机制会在战斗过程中本身触发更高难度。

以下是奥特兰克山谷（Alterac Valley）战场的特殊情况。有 4 个等级段，NPC 会根据你的等级段而被削弱或加强（在 WoW 3.2.2 补丁中新增，当时 80 级角色在该战场拥有自己的等级段，而所有 80 级以下的等级段也都拥有各自的难度等级）。同样的概念也适用于征服之岛（Isle of Conquest）战场，只不过只有两个等级段。

如果你查看数据库，会注意到一个非常典型的模式，总结在下表中：

| name             | entry             | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| ---------------- | ----------------- | ------------------ | ------------------ | ------------------ |
| 普通生物         | 不同于 0          | 0                  | 0                  | 0                  |
| 地下城生物       | 普通地下城        | 英雄地下城         | 0                  | 0                  |
| 团队副本生物     | 10 人普通团队副本 | 25 人普通团队副本  | 10 人英雄团队副本  | 25 人英雄团队副本  |
| 战场             | 51- 59            | 60-69              | 70-79              | 80                 |

#### KillCredit1

如果这是一个击杀计数（kill credit）模板——即当一个任务中可以有多个生物被计为击杀时使用的虚拟模板，那么这就是第一个可被击杀以给予任务击杀计数的生物 [entry](#entry) 的链接。

#### KillCredit2

如果这是一个击杀计数（kill credit）模板——即当一个任务中可以有多个生物被计为击杀时使用的虚拟模板，那么这就是第二个可被击杀以给予任务击杀计数的生物 [entry](#entry) 的链接。如果可以击杀两个以上的生物并计入同一目标，则将需要智能脚本（smart script）或 C++ 脚本。

#### name

生物的基础名称。

#### subname

生物的子名称（subname），显示在生物名称下方的 &lt;&gt; 中。

#### IconName

用于告诉玩家这个生物是什么类型的 NPC。

| IconName           | 描述                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Directions**     | 用于卫兵和传送 NPC。                                              |
| **Gunner**         | 炮塔 NPC/玩家控制的指示符。                                       |
| **vehichleCursor** | 表示这是一个 PCV（玩家控制载具）                           |
| **Driver**         | 鼠标悬停时显示方向盘图标。                                       |
| **Attack**         | 显示一把剑的图标，表示你可以攻击该目标。                          |
| **Buy**            | 通常当 NPC 只出售物品时，显示一个棕色袋子图标。                       |
| **Speak**          | 如果该 NPC 有任务/对话选项，显示一个聊天气泡图标。                     |
| **Pickup**         | 如果该 NPC 可以被拾取以获得任务/物品，显示一个抓取的手图标。           |
| **Interact**       | 显示齿轮图标，通常用于任务/传送。                                  |
| **Trainer**        | 显示一本书的图标，表明该 NPC 是训练师。                              |
| **Taxi**           | 显示一个带翅膀的靴子图标，表明该 NPC 是出租车（飞行管理员）。                       |
| **Repair**         | 显示一个铁砧图标，表明该 NPC 可以修理。                           |
| **LootAll**        | 显示多个棕色袋子图标（与拾取生物前按住 shift 相同）。 |
| **Quest**          | 未使用或未知（参见条目 32870 "The Real Ronakada"）。                           |
| **PVP**            | 未使用或未知（参见条目 29387 "Arena Master: Dalaran Arena"）。                 |

**注意！** 除非你使用脚本或对话选项，否则这不是使 NPC 正常运行所必需的。名称区分大小写，如有疑问请使用上面的示例。

#### gossip_menu_id

该生物的对话（gossip）ID。此字段从嗅探（更新字段）中获得。如果你无法嗅探此值，并且需要自行编造一个，则它必须 &gt; 50000。此字段是 [gossip_menu.MenuID](gossip_menu#menuid) 的链接。

#### minlevel

如果生物具有等级范围，则这是生物的最低等级。

#### maxlevel

如果生物具有等级范围，则这是生物的最高等级。当添加到世界时，会在指定的等级范围内选择一个等级。

#### exp

生物的生命值取自的版本扩展表。值范围为 0 到 2。参见 creature_classlevelstats。

| exp | 名称                   |
| --- | ---------------------- |
| 0   | 经典旧世                |
| 1   | 燃烧的远征    |
| 2   | 巫妖王之怒 |

#### faction

生物的阵营。参见 [FactionTemplate](factiontemplate)。仅仅因为多个阵营具有相同的名称，阵营间的关系也可能不同。

注意：此字段还控制生物的家族援助机制。只有具有相同阵营的生物才会相互援助。

#### npcflag

一个位掩码，表示生物具有哪些 NPC 标志。每个位控制一个不同的标志，要组合标志，可以将你想要每个标志相加，从而激活相应的位。

| Flag     |            | Name               | Comment                                                                          |
| -------- | ---------- | ------------------ | -------------------------------------------------------------------------------- |
| 1        | 0x00000001 | Gossip             | 如果生物有更多对话选项，添加此标志以弹出菜单。           |
| 2        | 0x00000002 | Quest Giver        | 任何给予或收取任务的生物都需要此标志。                    |
| 16       | 0x00000010 | Trainer            | 允许生物拥有训练师列表以教授法术                       |
| 32       | 0x00000020 | Class Trainer      | 是职业训练师                                                                 |
| 64       | 0x00000040 | Profession Trainer | 是专业技能训练师                                                            |
| 128      | 0x00000080 | Vendor             | 是商人（通用）任何出售物品的生物都需要此标志。          |
| 256      | 0x00000100 | Vendor Ammo        | 是商人（弹药）                                                                 |
| 512      | 0x00000200 | Vendor Food        | 是商人（食物）                                                                 |
| 1024     | 0x00000400 | Vendor Poison      | 是商人（毒药）                                                               |
| 2048     | 0x00000800 | Vendor Reagent     | 是商人（施法材料）                                                              |
| 4096     | 0x00001000 | Repairer           | 具有此标志的生物可以修理物品。                                       |
| 8192     | 0x00002000 | Flight Master      | 任何充当飞行管理员的生物都具有此标志。                                  |
| 16384    | 0x00004000 | Spirit Healer      | 使生物对活着的角色不可见，并具有复活功能。 |
| 32768    | 0x00008000 | Spirit Guide       | 是灵魂向导                                                                  |
| 65536    | 0x00010000 | Innkeeper          | 具有此标志的生物可以设置炉石位置。                          |
| 131072   | 0x00020000 | Banker             | 具有此标志的生物可以显示银行                                       |
| 262144   | 0x00040000 | Petitioner         | 处理公会/竞技场申请                                                    |
| 524288   | 0x00080000 | Tabard Designer    | 允许设计公会战袍。                                           |
| 1048576  | 0x00100000 | Battlemaster       | 具有此标志的生物将玩家传送到战场。                          |
| 2097152  | 0x00200000 | Auctioneer         | 允许生物显示拍卖列表。                                         |
| 4194304  | 0x00400000 | Stable Master      | 有为猎人寄存宠物的选项。                                       |
| 8388608  | 0x00800000 | Guild Banker       | 是公会银行职员                                                                  |
| 16777216 | 0x01000000 | Spellclick         | 需要在 npc_spellclick_spells 表中有数据                                        |
| 67108864 | 0x04000000 | Mailbox            | NPC 将表现得像一个邮箱（右键点击可打开邮箱）                     |

因此，如果你想要一个既是任务给予者(2)、商人(128)又可以修理(4096)的 NPC，只需将特定标志相加：2+128+4096=4226

#### speed_walk

控制生物可以行走的速度。对于载具：提高飞行速度。

#### speed_run

控制生物可以奔跑的速度。对于载具：提高地面移动速度。

#### speed_swim

控制生物可以游泳的速度。

#### speed_flight

控制生物可以飞行的速度。

#### detection_range

控制生物侦测和看到玩家的范围。

#### rank

生物的等级（rank）：

| Rank | 名称       | 默认刷新时间 Creature.spawntimesecs | 尸体消失时间 Worldserver.conf (Corpse.Decay) | 总默认刷新时间 spawntimesecs + Corpse.Decay |
| ---- | ---------- | ------------------------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| 0    | 普通     | 5 分钟                                       | 60 秒                                            | 6 分钟                                              |
| 1    | 精英      | 5 分钟                                       | 5 分钟                                             | 10 分钟                                             |
| 2    | 稀有精英 | 5 分钟                                       | 5 分钟                                             | 10 分钟                                             |
| 3    | Boss       | 5 分钟                                       | 1 小时                                            | 1 小时 5 分钟                                      |
| 4    | 稀有       | 5 分钟                                       | 5 分钟                                             | 10 分钟                                             |

**注意 1：** NPC 的等级（rank）大多是视觉上的（这也需要清除你的缓存才能看到变化）。更改此值不会改变其生命值、伤害或战利品。但是，它会改变生物的刷新时间。

**注意 2：** 刷新时间还可以在两个其他地方修改：[Creature.spawntimesecs](creature#spawntimesecs)（仅针对该生物的单个 GUID）以及 worldserver.conf 文件中 "Corpse.Decay" 设置（针对所有相同等级的生物）。所有已刷新生物默认的 \`spawntimesecs\` 为 300 秒（5 分钟）。例如，使用 ".npc add" 命令刷新一个"普通"NPC 会赋予其默认 6 分钟的刷新时间（spawntimesecs + Corpse.Decay 时间）。此外，生物必须先消失（decay）才能刷新。因此，生物的尸体消失时间也是其最短刷新时间，因为将生物的 Creature.spawntimesecs 设置为 0 会移除默认刷新时间。在上面的示例中，将普通 NPC 的 spawntimesecs 设置为 0 意味着生物的刷新时间从 6 分钟减少到 60 秒。

**注意 3：** 如果你希望生物在头像中显示骷髅或"??"（通常用于 Boss），请将 [type_flags](#typeflags) 设置为 4。

#### dmgschool

生物的近战伤害学派。

| ID  | 名称                |
| --- | ------------------- |
| 0   | SPELL_SCHOOL_NORMAL |
| 1   | SPELL_SCHOOL_HOLY   |
| 2   | SPELL_SCHOOL_FIRE   |
| 3   | SPELL_SCHOOL_NATURE |
| 4   | SPELL_SCHOOL_FROST  |
| 5   | SPELL_SCHOOL_SHADOW |
| 6   | SPELL_SCHOOL_ARCANE |

#### BaseAttackTime

这是决定生物在两次近战攻击之间必须等待多长时间的基础时间。此时间以毫秒为单位。

#### RangeAttackTime

这是决定生物在两次远程攻击之间必须等待多长时间的基础时间。此时间以毫秒为单位。

#### BaseVariance

用于自定义生物伤害输出的值。参见 [DamageModifier](#damagemodifier)。

非自定义生物应始终将其保持为 1。

#### RangeVariance

用于自定义生物伤害输出的值。参见 [DamageModifier](#damagemodifier)。

非自定义生物应始终将其保持为 1。

#### unit_class

这是生物的职业，它决定了生命值和法力值的等级。另请注意，生命值和法力值将根据 [exp](#exp)、[HealthModifier](#healthmodifier) 和 [ManaModifier](#manamodifier) 而变化。不设置此值将在 "DB_Errors.log" 中报告一条轻微警告。

| Value | Name          | 显示的能量                                            |
| ----- | ------------- | ------------------------------------------------------ |
| 1     | CLASS_WARRIOR | 仅生命值（与潜行者相同）                           |
| 2     | CLASS_PALADIN | 生命值和法力值（比法师有更多生命值但更少法力值）    |
| 4     | CLASS_ROGUE   | 仅生命值（与战士相同）                         |
| 8     | CLASS_MAGE    | 生命值和法力值（比圣骑士更少生命值但更多法力值） |

#### unit_flags

允许手动向生物应用单位标志。同样这是一个位掩码字段，要应用多个标志，只需将不同的数字相加。一些可能的标志有：

| Flag       |            | Name                                    | Comments                                                                                                                                                                                                                                     |
| ---------- | ---------- | --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | 0x00000001 | UNIT_FLAG_SERVER_CONTROLLED             | 仅当单位移动由服务器控制时设置 - 通过 SPLINE/MONSTER_MOVE 数据包，与 UNIT_FLAG_STUNNED 一起；仅对客户端控制的单位设置；当为所有者设置时，客户端函数 CGUnit_C::IsClientControlled 返回 false |
| 2          | 0x00000002 | UNIT_FLAG_NON_ATTACKABLE                | 不可攻击                                                                                                                                                                                                                               |
| 4          | 0x00000004 | UNIT_FLAG_DISABLE_MOVE                  |                                                                                                                                                                                                                                              |
| 8          | 0x00000008 | UNIT_FLAG_PLAYER_CONTROLLED             | 由玩家控制，使用 _IMMUNE_TO_PC 而不是 _IMMUNE_TO_NPC                                                                                                                                                                            |
| 16         | 0x00000010 | UNIT_FLAG_RENAME                        |                                                                                                                                                                                                                                              |
| 32         | 0x00000020 | UNIT_FLAG_PREPARATION                   | 对于具有 SPELL_ATTR_EX5_NO_REAGENT_WHILE_PREP 的法术不消耗施法材料                                                                                                                                                                     |
| 64         | 0x00000040 | UNIT_FLAG_UNK_6                         | 不确定它是做什么的，但它是在 smart_scripts 中施放非触发法术所必需的                                                                                                                                                         |
| 128        | 0x00000080 | UNIT_FLAG_NOT_ATTACKABLE_1              | ??（UNIT_FLAG_PLAYER_CONTROLLED                                                                                                                                                                                                              |
| 256        | 0x00000100 | UNIT_FLAG_IMMUNE_TO_PC                  | 禁用与玩家角色（PC）的战斗/协助                                                                                                                                                                                        |
| 512        | 0x00000200 | UNIT_FLAG_IMMUNE_TO_NPC                 | 禁用与非玩家角色（NPC）的战斗/协助                                                                                                                                                                                    |
| 1024       | 0x00000400 | UNIT_FLAG_LOOTING                       | 拾取动画                                                                                                                                                                                                                               |
| 2048       | 0x00000800 | UNIT_FLAG_PET_IN_COMBAT                 | 在战斗中？2.0.8                                                                                                                                                                                                                             |
| 4096       | 0x00001000 | UNIT_FLAG_PVP                           | 在 3.0.3 中更改                                                                                                                                                                                                                             |
| 8192       | 0x00002000 | UNIT_FLAG_SILENCED                      | 无法施放法术                                                                                                                                                                                                                            |
| 16384      | 0x00004000 | UNIT_FLAG_CANNOT_SWIM                   | 2.0.8                                                                                                                                                                                                                                        |
| 32768      | 0x00008000 | UNIT_FLAG_SWIMMING                      | 在水中显示游泳动画                                                                                                                                                                                                                |
| 65536      | 0x00010000 | UNIT_FLAG_NON_ATTACKABLE_2              | 移除可攻击图标，如果作用于自身，则无法协助自己，但可以施放 TARGET_SELF 法术 - 由 SPELL_AURA_MOD_UNATTACKABLE 添加                                                                                                           |
| 131072     | 0x00020000 | UNIT_FLAG_PACIFIED                      | 生物将不会攻击                                                                                                                                                                                                                     |
| 262144     | 0x00040000 | UNIT_FLAG_STUNNED                       | 3.0.3 ok                                                                                                                                                                                                                                     |
| 524288     | 0x00080000 | UNIT_FLAG_IN_COMBAT                     | （来自 WPP 中 UnitFlags.cs 的 'AffectingCombat'）                                                                                                                                                                                                 |
| 1048576    | 0x00100000 | UNIT_FLAG_TAXI_FLIGHT                   | 在客户端禁用施放出租车飞行不允许的法术（骑乘？），可能与 0x4 标志一起使用                                                                                                                                      |
| 2097152    | 0x00200000 | UNIT_FLAG_DISARMED                      | 3.0.3，禁用近战法术施放...，"需要近战武器"被添加到近战法术的工具提示中。                                                                                                                                               |
| 4194304    | 0x00400000 | UNIT_FLAG_CONFUSED                      | 混乱。                                                                                                                                                                                                                                    |
| 8388608    | 0x00800000 | UNIT_FLAG_FLEEING                       | （来自 WPP 中 UnitFlags.cs 的 'Feared'）                                                                                                                                                                                                          |
| 16777216   | 0x01000000 | UNIT_FLAG_POSSESSED                     | 由玩家直接客户端控制（占据或载具）                                                                                                                                                                                 |
| 33554432   | 0x02000000 | UNIT_FLAG_NOT_SELECTABLE                | 无法通过鼠标或 /target {name} 命令选择。                                                                                                                                                                                   |
| 67108864   | 0x04000000 | UNIT_FLAG_SKINNABLE                     | 可剥皮                                                                                                                                                                                                                                    |
| 134217728  | 0x08000000 | UNIT_FLAG_MOUNT                         | 客户端似乎能完美处理它。也用于制作自定义坐骑。                                                                                                                                                                |
| 268435456  | 0x10000000 | UNIT_FLAG_UNK_28                        | （来自 WPP 中 UnitFlags.cs 的 PreventKneelingWhenLooting）                                                                                                                                                                                        |
| 536870912  | 0x20000000 | UNIT_FLAG_PREVENT_EMOTES_FROM_CHAT_TEXT | 防止自动播放由解析聊天文本产生的表情，例如 /say 中的 "lol"、以 ? 或 ! 结尾的消息，或使用 /yell                                                                                                           |
| 1073741824 | 0x40000000 | UNIT_FLAG_SHEATHE                       |                                                                                                                                                                                                                                              |
| 2147483648 | 0x80000000 | UNIT_FLAG_IMMUNE                        | 对伤害免疫                                                                                                                                                                                                                             |

#### unit_flags2

允许额外向生物应用单位标志。同样，这是一个位掩码字段，要应用多个标志，只需将不同的数字相加。一些可能的标志有：


| Flag   |            | Name                                  | Comments                                                                    |
| ------ | ---------- | ------------------------------------- | --------------------------------------------------------------------------- |
| 1      | 0x00000001 | UNIT_FLAG2_FEIGN_DEATH                |                                                                             |
| 2      | 0x00000002 | UNIT_FLAG2_HIDE_BODY                  | 隐藏单位模型（仅显示玩家装备）                                    |
| 4      | 0x00000004 | UNIT_FLAG2_IGNORE_REPUTATION          |                                                                             |
| 8      | 0x00000008 | UNIT_FLAG2_COMPREHEND_LANG            |                                                                             |
| 16     | 0x00000010 | UNIT_FLAG2_MIRROR_IMAGE               |                                                                             |
| 32     | 0x00000020 | UNIT_FLAG2_DO_NOT_FADE_IN             | 单位模型在被召唤时立即出现（不淡入）               |
| 64     | 0x00000040 | UNIT_FLAG2_FORCE_MOVEMENT             |                                                                             |
| 128    | 0x00000080 | UNIT_FLAG2_DISARM_OFFHAND             |                                                                             |
| 256    | 0x00000100 | UNIT_FLAG2_DISABLE_PRED_STATS         | 玩家已禁用预测属性（由团队框架使用）                   |
| 1024   | 0x00000400 | UNIT_FLAG2_DISARM_RANGED              | 这不会禁用远程武器的显示（可能需要额外的标志？） |
| 2048   | 0x00000800 | UNIT_FLAG2_REGENERATE_POWER           |                                                                             |
| 4096   | 0x00001000 | UNIT_FLAG2_RESTRICT_PARTY_INTERACTION | 将交互限制为队伍或团队                                       |
| 8192   | 0x00002000 | UNIT_FLAG2_PREVENT_SPELL_CLICK        | 阻止法术点击                                                          |
| 16384  | 0x00004000 | UNIT_FLAG2_ALLOW_ENEMY_INTERACT       |                                                                             |
| 32768  | 0x00008000 | UNIT_FLAG2_CANNOT_TURN                |                                                                             |
| 65536  | 0x00010000 | UNIT_FLAG2_UNK2                       |                                                                             |
| 131072 | 0x00020000 | UNIT_FLAG2_PLAY_DEATH_ANIM            | 死亡时播放特殊死亡动画                                    |
| 262144 | 0x00040000 | UNIT_FLAG2_ALLOW_CHEAT_SPELLS         | 允许施放具有 AttributesEx7 和 SPELL_ATTR7_IS_CHEAT_SPELL 的法术       |

#### dynamicflags

控制生物视觉外观的标志。

一些已知的标志及其用途如下：


| Flag |      | Name                                   | Comments                                                                                            |
| ---- | ---- | -------------------------------------- | --------------------------------------------------------------------------------------------------- |
| 0    | 0x00 | UNIT_DYNFLAG_NONE                      |                                                                                                     |
| 1    | 0x01 | UNIT_DYNFLAG_LOOTABLE                  |                                                                                                     |
| 2    | 0x02 | UNIT_DYNFLAG_TRACK_UNIT                | 生物的位置将作为一个小点显示在小地图上                                      |
| 4    | 0x04 | UNIT_DYNFLAG_TAPPED                    | 使生物的名称显示为灰色（Lua_UnitIsTapped）                                                 |
| 8    | 0x08 | UNIT_DYNFLAG_TAPPED_BY_PLAYER          | Lua_UnitIsTappedByPlayer 通常由 PCV（玩家控制载具）使用                          |
| 16   | 0x10 | UNIT_DYNFLAG_SPECIALINFO               |                                                                                                     |
| 32   | 0x20 | UNIT_DYNFLAG_DEAD                      | 使生物看起来已死亡（这不会使生物名称变灰或使其不攻击玩家）。 |
| 64   | 0x40 | UNIT_DYNFLAG_REFER_A_FRIEND            |                                                                                                     |
| 128  | 0x80 | UNIT_DYNFLAG_TAPPED_BY_ALL_THREAT_LIST | Lua_UnitIsTappedByAllThreatList                                                                     |

#### family

该生物所属的家族。

| ID  | 家族       | ID  | 家族         |
| --- | ------------ | --- | -------------- |
| 1.  | 狼         | 26. | 猫头鹰            |
| 2.  | 猫          | 27. | 风蛇   |
| 3.  | 蜘蛛       | 28. | 遥控   |
| 4.  | 熊         | 29. | 恶魔卫士       |
| 5.  | 野猪         | 30. | 龙鹰     |
| 6.  | 鳄鱼    | 31. | 掠夺者        |
| 7.  | 食腐鸟 | 32. | 迁跃跟踪者   |
| 8.  | 螃蟹         | 33. | 孢子蝠       |
| 9.  | 大猩猩      | 34. | 虚空鳐     |
| 11. | 迅猛龙       | 35. | 蛇        |
| 12. | 陆行鸟  | 37. | 蛾           |
| 15. | 地狱猎犬    | 38. | 奇美拉       |
| 16. | 虚空行者   | 39. | 魔暴龙      |
| 17. | 魅魔     | 40. | 食尸鬼          |
| 19. | 末日守卫    | 41. | 其拉虫       |
| 20. | 蝎子      | 42. | 蠕虫           |
| 21. | 乌龟       | 43. | 犀牛          |
| 23. | 小鬼          | 44. | 黄蜂           |
| 24. | 蝙蝠          | 45. | 熔核犬     |
| 25. | 鬣狗        | 46. | 灵魂兽   |

#### type

生物的类型。

| ID  | 类型           |
| --- | -------------- |
| 0   | 无           |
| 1   | 野兽          |
| 2   | 龙类      |
| 3   | 恶魔          |
| 4   | 元素      |
| 5   | 巨人          |
| 6   | 亡灵         |
| 7   | 人型生物       |
| 8   | 小动物        |
| 9   | 机械     |
| 10  | 未指定  |
| 11  | 图腾          |
| 12  | 非战斗宠物 |
| 13  | 毒气云      |

#### type_flags

该字段可以控制怪物是否可被采矿、采药或可被工程师拾取。如果它属于这三种情况之一，那么当它被剥皮/采矿时给予的战利品将存储在 [skinning_loot_template](loot_template) 表中。它还控制这个怪物是否可以被猎人驯服。其他字段在服务器端没有特殊含义。整个字段将通过 SMSG_CREATURE_QUERY_RESPONSE 发送到客户端

| Flag       |            | Name                                                 | Comments                                                                                   |
| ---------- | ---------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1          | 0x00000001 | CREATURE_TYPE_FLAG_TAMEABLE                          | 使怪物可被驯服（也必须是野兽并设置家族）                          |
| 2          | 0x00000002 | CREATURE_TYPE_FLAG_VISIBLE_TO_GHOSTS                 | 生物对未死亡的玩家也可见。如果 npcflag 允许，是否允许对话互动？ |
| 4          | 0x00000004 | CREATURE_TYPE_FLAG_BOSS_MOB                          | 将生物的可见等级更改为生物头像中的"??" - 免疫击退。 |
| 8          | 0x00000008 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_WOUND_PARRY_ANIMATION | 招架时不播放受伤动画。                                                    |
| 16         | 0x00000010 | CREATURE_TYPE_FLAG_NO_FACTION_TOOLTIP                | 隐藏提示信息中的阵营。                                                                     |
| 32         | 0x00000020 | CREATURE_TYPE_FLAG_MORE_AUDIBLE                      |                                                                                            |
| 64         | 0x00000040 | CREATURE_TYPE_FLAG_SPELL_ATTACKABLE                  | 可被法术攻击。                                                                          |
| 128        | 0x00000080 | CREATURE_TYPE_FLAG_INTERACT_WHILE_DEAD               | 玩家可以在生物死亡时与之互动（不是玩家死亡）                        |
| 256        | 0x00000100 | CREATURE_TYPE_FLAG_SKIN_WITH_HERBALISM               | 使怪物可采药                                                                         |
| 512        | 0x00000200 | CREATURE_TYPE_FLAG_SKIN_WITH_MINING                  | 使怪物可采矿                                                                          |
| 1024       | 0x00000400 | CREATURE_TYPE_FLAG_NO_DEATH_MESSAGE                  | 不记录战斗日志死亡。                                                                  |
| 2048       | 0x00000800 | CREATURE_TYPE_FLAG_ALLOW_MOUNTED_COMBAT              | 生物可以在进入战斗时保持骑乘状态                                           |
| 4096       | 0x00001000 | CREATURE_TYPE_FLAG_CAN_ASSIST                        | 在范围内时可以协助任何处于战斗中的玩家？                                  |
| 8192       | 0x00002000 | CREATURE_TYPE_FLAG_NO_PET_BAR                        | 是否使用宠物动作条。                                                                          |
| 16384      | 0x00004000 | CREATURE_TYPE_FLAG_MASK_UID                          |                                                                                            |
| 32768      | 0x00008000 | CREATURE_TYPE_FLAG_SKIN_WITH_ENGINEERING             | 使怪物可被工程师拾取                                                             |
| 65536      | 0x00010000 | CREATURE_TYPE_FLAG_TAMEABLE_EXOTIC                   | 可作为异种宠物驯服。还必须设置普通可驯服标志。                            |
| 131072     | 0x00020000 | CREATURE_TYPE_FLAG_USE_MODEL_COLLISION_SIZE          | 与碰撞相关。（总是使用默认碰撞盒？）                                   |
| 262144     | 0x00040000 | CREATURE_TYPE_FLAG_ALLOW_INTERACTION_WHILE_IN_COMBAT | 是攻城武器。                                                                           |
| 524288     | 0x00080000 | CREATURE_TYPE_FLAG_COLLIDE_WITH_MISSILES             | 抛射物可以与这个生物碰撞 - 与 TARGET_DEST_TRAJ 交互               |
| 1048576    | 0x00100000 | CREATURE_TYPE_FLAG_NO_NAME_PLATE                     | 隐藏姓名板。                                                                           |
| 2097152    | 0x00200000 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_MOUNTED_ANIMATIONS    | 不播放骑乘动画。                                                          |
| 4194304    | 0x00400000 | CREATURE_TYPE_FLAG_IS_LINK_ALL                       |                                                                                            |
| 8388608    | 0x00800000 | CREATURE_TYPE_FLAG_INTERACT_ONLY_WITH_CREATOR        | 只能与其创造者互动。                                                        |
| 16777216   | 0x01000000 | CREATURE_TYPE_FLAG_DO_NOT_PLAY_UNIT_EVENT_SOUNDS     |                                                                                            |
| 33554432   | 0x02000000 | CREATURE_TYPE_FLAG_HAS_NO_SHADOW_BLOB                |                                                                                            |
| 67108864   | 0x04000000 | CREATURE_TYPE_FLAG_TREAT_AS_RAID_UNIT                | 生物可以被要求目标位于施法者队伍/团队中的法术瞄准        |
| 134217728  | 0x08000000 | CREATURE_TYPE_FLAG_FORCE_GOSSIP                      | 允许生物显示单个对话选项。                                     |
| 268435456  | 0x10000000 | CREATURE_TYPE_FLAG_DO_NOT_SHEATHE                    |                                                                                            |
| 536870912  | 0x20000000 | CREATURE_TYPE_FLAG_DO_NOT_TARGET_ON_INTERACTION      |                                                                                            |
| 1073741824 | 0x40000000 | CREATURE_TYPE_FLAG_DO_NOT_RENDER_OBJECT_NAME         |                                                                                            |
| 2147483648 | 0x80000000 | CREATURE_TYPE_FLAG_UNIT_IS_QUEST_BOSS                |                                                                                            |

#### lootid

该生物用于生成战利品时应使用的战利品模板 ID。参见 [creature_loot_template.entry](loot_template#entry)

#### pickpocketloot

该生物用于生成扒窃战利品时应使用的扒窃战利品模板 ID。参见 [pickpocketing_loot_template.entry](loot_template#entry)

#### skinloot

该生物用于生成剥皮战利品时应使用的剥皮战利品模板 ID。参见 [skinning_loot_template.entry](loot_template#entry)

#### PetSpellDataId

在 CreatureSpellData.dbc 中找到的 ID，用于显示宠物在客户端具有哪些法术。

#### VehicleId

如果生物是载具或拥有载具条目，则为载具条目。此字段决定玩家在载具上的外观、载具如何移动，以及是否显示载具动作条。例如，vehicleID 为 292 会使玩家隐身，阻止载具左右平移（但允许前进/后退），并会显示载具动作条法术（在 [spell1-8](http://trinitycore.atlassian.net#spell) 中定义）。要使此功能生效，必须为该生物条目创建一条 npc_spellclick_spells 记录。

#### mingold

生物被击杀时掉落的最低金钱，以铜币为单位。

#### maxgold

生物被击杀时掉落的最高金钱，以铜币为单位。

#### AIName

如果 ScriptName 字段与 AIName 同时设置，则 ScriptName 字段将覆盖此字段。

| Name           | 描述                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------- |
| NullCreatureAI | 空的 AI，生物什么都不做；不能被魅惑。                                                 |
| TriggerAI      | 与 "NullCreatureAI" 相同，不同之处在于生物在被召唤时会施放 spell1 字段中的法术。 |
| AggressorAI    | 生物在进入仇恨半径时攻击；只使用近战攻击。                               |
| ReactorAI      | 生物只在被仇恨时攻击；只使用近战攻击。                                          |
| PassiveAI      | 生物表现被动，无法攻击。                                                            |
| CritterAI      | 受到攻击会逃跑的小动物。                                                                    |
| GuardAI        | 生物是区域卫兵。                                                                           |
| PetAI          | 生物是宠物。                                                                                  |
| TotemAI        | 生物施放 spell1 字段中的法术；不移动。                                              |
| CombatAI       | 一旦有东西进入仇恨范围，生物立即攻击；也使用法术。                          |
| ArcherAI       | 生物施放 spell1 字段中的法术；追击目标。                                          |
| TurretAI       | 生物使用 spell1 字段中的法术攻击；不移动。                                      |
| VehicleAI      | 生物充当玩家载具。                                                                    |
| SmartAI        | 生物使用 "[smart_scripts](smart_scripts)" 表来指定其行为。                 |

#### MovementType

生物的默认移动类型。

| ID  | 类型                                              |
| --- | ------------------------------------------------- |
| 0   | 待机；停留在一个地方                           |
| 1   | 在 wander_distance 半径内随机移动 |
| 2   | 路径点移动                                 |

#### HoverHeight

如果生物启用了 MOVEMENTFLAG_DISABLE_GRAVITY，则其为在地面上方悬停的距离。值取自嗅探。

#### HealthModifier

用于修改生物的基础等级/职业生命值。此字段来自 WDB。

#### ManaModifier

用于修改生物的基础等级/职业法力值。此字段来自 WDB。

#### ArmorModifier

用于修改生物的基础等级/职业护甲。

#### DamageModifier

用于修改生物的最小/最大伤害。

计算伤害输出的公式如下：

MINDAMAGE = ((([damage_base](creature_classlevelstats#damagebase) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))  
MAXDAMAGE = (((([damage_base](creature_classlevelstats#damagebase) * 1.5) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](creature_template#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))

damage_base 来自 creature_classlevelstats 表，其值根据生物的 [exp](#exp) 值取自 [damage_base](creature_classlevelstats#damagebase)、[damage_exp1](creature_classlevelstats#damageexp1) 或 [damage_exp2](creature_classlevelstats#damageexp2)（0 = base_damage，1 = damage_exp1，2 = damage_exp2）。

BaseAttackTime 根据攻击类型为 [BaseAttackTime](#baseattacktime) 或 [RangeAttackTime](#rangeattacktime)。

attackpower 根据攻击类型为 [attackpower](creature_classlevelstats#attackpower) 或 [rangedattackpower](creature_classlevelstats#rangedattackpower)。

BaseVariance 根据攻击类型为 [BaseVariance](#basevariance) 或 [RangeVariance](#rangevariance)。


#### ExperienceModifier

待办（TODO）！

#### RacialLeader

一个具有两个可能值 '1' 或 '0' 的标志，表示该生物是否为种族领袖。击杀种族领袖可获得 100 点荣誉。

| entry | name                     |
| ----- | ------------------------ |
| 2784  | 麦格尼·铜须   |
| 3057  | 凯恩·血蹄         |
| 4949  | 萨尔                   |
| 7999  | 泰兰德·语风      |
| 10181 | 希尔瓦娜斯·风行者 |
| 16802 | 洛瑟玛·塞隆        |
| 17468 | 维伦            |
| 29611 | 瓦里安·乌瑞恩        |
| 36648 | 贝恩·血蹄（领袖） |
| 37764 | 洛瑟玛·塞隆        |

#### movementId

我们不知道这个字段是做什么的。它被直接传递给客户端。

#### RegenHealth

布尔值 '1' 或 '0'，控制生物是否应该恢复其生命值。

#### CreatureImmunitiesId

引用 `creature_immunities` 表，该表集中了基于法术和机制的免疫。

有关机制和法术学派位的详细列表，参见 [creature_immunities](creature_immunities)。

#### flags_extra

这些标志控制某些生物特有的属性。标志可以相加以应用多个。

**示例：** 32+64=96

| Flag       | Type                                                |            |                                                                                                                                        |
| ---------- | --------------------------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | CREATURE_FLAG_EXTRA_INSTANCE_BIND                   | 0x00000001 | 生物击杀将实例绑定到击杀者和击杀者的队伍                                                                              |
| 2          | CREATURE_FLAG_EXTRA_CIVILIAN                        | 0x00000002 | 生物不产生仇恨（忽略阵营/声望敌对）                                                                          |
| 4          | CREATURE_FLAG_EXTRA_NO_PARRY                        | 0x00000004 | 生物不招架                                                                                                                |
| 8          | CREATURE_FLAG_EXTRA_NO_PARRY_HASTEN                 | 0x00000008 | 生物不在招架时反击                                                                                              |
| 16         | CREATURE_FLAG_EXTRA_NO_BLOCK                        | 0x00000010 | 生物不格挡                                                                                                                |
| 32         | CREATURE_FLAG_EXTRA_NO_CRUSHING_BLOWS               | 0x00000020 | 生物不造成碾压攻击                                                                                                     |
| 64         | CREATURE_FLAG_EXTRA_NO_XP                           | 0x00000040 | 生物击杀不给予经验值                                                                                                         |
| 128        | CREATURE_FLAG_EXTRA_TRIGGER                         | 0x00000080 | 生物是触发器 NPC（仅对玩家不可见）                                                                                    |
| 256        | CREATURE_FLAG_EXTRA_NO_TAUNT                        | 0x00000100 | 生物对嘲讽光环和"攻击我"效果免疫                                                                        |
| 512        | CREATURE_FLAG_EXTRA_NO_MOVE_FLAGS_UPDATE            | 0x00000200 | （CREATURE_FLAG_EXTRA_UNUSED_10 未实现）生物不更新移动标志                                                   |
| 1024       | CREATURE_FLAG_EXTRA_GHOST_VISIBILITY                | 0x00000400 | 生物只对死亡的玩家可见                                                                                         |
| 2048       | CREATURE_FLAG_EXTRA_USE_OFFHAND_ATTACK              | 0x00000800 | 生物将使用副手攻击                                                                                                      |
| 4096       | CREATURE_FLAG_EXTRA_NO_SELL_VENDOR                  | 0x00001000 | 玩家不能向这个商人出售物品                                                                                                |
| 8192       | CREATURE_FLAG_EXTRA_CANNOT_ENTER_COMBAT             | 0x00002000 | 生物不能进入战斗（不会攻击也不会被攻击）                                                                          |
| 16384      | CREATURE_FLAG_EXTRA_WORLDEVENT                      | 0x00004000 | 用于世界事件的自定义标志（为合并留出空间）                                                                                   |
| 32768      | CREATURE_FLAG_EXTRA_GUARD                           | 0x00008000 | 生物是卫兵（将忽略假死和消失）                                                                               |
| 65536      | CREATURE_FLAG_EXTRA_IGNORE_FEIGN_DEATH              | 0x00010000 | 生物忽略假死                                                                                                           |
| 131072     | CREATURE_FLAG_EXTRA_NO_CRIT                         | 0x00020000 | 生物不造成暴击                                                                                                  |
| 262144     | CREATURE_FLAG_EXTRA_NO_SKILL_GAINS                  | 0x00040000 | 生物不会提升武器技能                                                                                                  |
| 524288     | CREATURE_FLAG_EXTRA_OBEYS_TAUNT_DIMINISHING_RETURNS | 0x00080000 | 生物的嘲讽受递减收益影响                                                                                       |
| 1048576    | CREATURE_FLAG_EXTRA_ALL_DIMINISH                    | 0x00100000 | 生物受所有递减收益影响                                                                                         |
| 2097152    | CREATURE_FLAG_EXTRA_NO_PLAYER_DAMAGE_REQ            | 0x00200000 | 生物不需要承受玩家伤害即可获得击杀计数                                                                           |
| 4194304    | CREATURE_FLAG_EXTRA_AVOID_AOE                       | 0x00400000 | 被 AOE 攻击忽略（用于 ICC 鲜血王子议会 NPC - 黑暗内核）                                                               |
| 8388608    | CREATURE_FLAG_EXTRA_NO_DODGE                        | 0x00800000 | 目标无法闪避                                                                                                                    |
| 16777216   | CREATURE_FLAG_EXTRA_MODULE                          | 0x01000000 | 由模块生物使用以避免暴雪风格检查。                                                                                    |
| 33554432   | CREATURE_FLAG_EXTRA_DONT_CALL_ASSISTANCE            | 0x02000000 | 阻止生物在初始仇恨时呼叫援助                                                                        |
| 67108864   | CREATURE_FLAG_EXTRA_IGNORE_ALL_ASSISTANCE_CALLS     | 0x04000000 | 阻止生物响应援助呼叫                                                                                  |
| 134217728  | CREATURE_FLAG_EXTRA_DONT_OVERRIDE_SAI_ENTRY         | 0x08000000 | 允许生物同时使用特定 GUID 和特定 ENTRY 的 SAI，而不会相互覆盖                                             |
| 268435456  | CREATURE_FLAG_EXTRA_DUNGEON_BOSS                    | 0x10000000 | 生物是地下城 Boss。此标志由核心在运行时自动设置。在数据库中设置此标志将导致启动错误。 |
| 536870912  | CREATURE_FLAG_EXTRA_IGNORE_PATHFINDING              | 0x20000000 | 生物将忽略寻路。这就像只针对一个生物禁用 Mmaps。                                                 |
| 1073741824 | CREATURE_FLAG_EXTRA_IMMUNITY_KNOCKBACK              | 0x40000000 | 生物将对所有击退效果免疫                                                                                             |
| 2147483648 | CREATURE_FLAG_EXTRA_HARD_RESET                      | 0x80000000 | 生物在脱离战斗（evade）时消失                                                                                                         |

#### ScriptName

该生物使用的脚本名称（如果有）。这将脚本引擎中的脚本与此生物绑定。

#### VerifiedBuild

该字段用于确定模板是否已根据 WDB 文件进行验证。

如果值为 0，则表示尚未解析。

如果值大于 0，则表示已使用来自该特定客户端构建的 WDB 文件进行解析。

如果值为 -1，则仅为占位符，直到在 WDB 中找到正确的数据。

如果值为 -客户端构建（Client Build），则表示已使用来自该特定 [客户端构建](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") 的 WDB 文件进行解析，并在之后为某些特殊需要而手动编辑。
