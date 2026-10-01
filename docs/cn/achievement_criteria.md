---
redirect_from: "/cn/Achievement_Criteria"
---

# 成就条件（Achievement Criteria）

[`返回至:DBC`](dbc-index)

**Achievement\_Criteria.dbc**

此 DBC 自 WoW 3.0.1.8303 起引入，包含获得成就所需的各项条件。

**版本为：3.3.5a**

[如何将 DBC 数据导入我的数据库](how-to-import-dbc-data-in-db)

## 结构

| 列     | 字段             | 类型    | 注释                                                                    |
| ------ | ---------------- | ------- | ----------------------------------------------------------------------- |
| 1      | ID               | Integer | 条件 ID                                                                 |
| 2      | Achievement      | iRefID  | 引用该条件所属的成就。                                                   |
| 3      | Type             | Integer | 此条件属于哪种类型？这将决定下面各行的含义。参见下文。                   |
| 4      | asset_id         | Integer | 主要要求                                                               |
| 5      | Quantity         | Integer | 主要要求的数量                                                         |
| 6      | start_event      | Integer | 附加要求 1 的类型                                                      |
| 7      | start_asset      | Integer | 附加要求 1 的值                                                        |
| 8      | fail_event       | Integer | 附加要求 2 的类型                                                      |
| 9      | fail_asset       | Integer | 附加要求 2 的值                                                        |
| 10-25  | Description      | Loc     | 条件描述。                                                             |
| 26     | ?                |         | 大多为 16712190，但并不总是如此                                        |
| 27     | Flags            | Integer | 显示标志：1：显示进度条（其他标志我不清楚）                            |
| 28     | timer_start_event | Integer |                                                                       |
| 29     | timer_asset_id   | Integer |                                                                       |
| 30     | timer_time       | Integer | 在 %i 秒内完成任务。                                                   |
| 31     | ui_order         | Integer |                                                                       |

**字段说明**

这里按类型（第 2 行）描述了第 3 到 9 行。可能还有更多类型。未列出的字段为零。

此信息取自 DBCStructure.h。

#### KILL\_CREATURE = 0

*也用于玩家死亡..*

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | creatureID  | Integer |
| 5      | killCount   | Integer |

#### WIN\_BG = 1

*除了单纯获胜之外还有更多的条件*

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | [Map](map)  | iRefID  |
| 5      | winCount    | Integer |

#### REACH\_LEVEL = 5

| 列     | 字段   | 类型    |
| ------ | ------ | ------- |
| 4      | unused | Integer |
| 5      | level  | Integer |

#### REACH\_SKILL\_LEVEL = 7

| 列     | 字段        | 类型    | 注释                                  |
| ------ | ----------- | ------- | ------------------------------------- |
| 4      | skillID     | iRefID  | [SkillLine.dbc](skillline) 或其他？   |
| 5      | skillLevel  | Integer |                                       |

#### COMPLETE\_ACHIEVEMENT = 8

| 列     | 字段                        | 类型   |
| ------ | --------------------------- | ------ |
| 4      | [Achievement](achievement)  | iRefID |

#### COMPLETE\_QUEST\_COUNT = 9

| 列     | 字段             | 类型    |
| ------ | ---------------- | ------- |
| 4      | unused           | Integer |
| 5      | totalQuestCount  | Integer |

#### COMPLETE\_DAILY\_QUEST\_DAILY = 10

| 列     | 字段          | 类型    |
| ------ | ------------- | ------- |
| 4      | unused        | Integer |
| 5      | numberOfDays  | Integer |

#### COMPLETE\_QUESTS\_IN\_ZONE = 11

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | zoneID      | Integer |
| 5      | questCount  | Integer |

#### DAMAGE\_DONE = 13

#### COMPLETE\_DAILY\_QUEST = 14

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | unused      | Integer |
| 5      | questCount  | Integer |

#### COMPLETE\_BATTLEGROUND = 15

#### DEATH\_AT\_MAP = 16

| 列     | 字段        | 类型   |
| ------ | ----------- | ------ |
| 4      | [Map](map)  | iRefID |

#### DEATH\_IN\_DUNGEON = 18

| 列     | 字段      | 类型    |
| ------ | --------- | ------- |
| 4      | manLimit  | Integer |

#### COMPLETE\_RAID = 19

| 列     | 字段       | 类型    | 注释                |
| ------ | ---------- | ------- | ------------------- |
| 4      | groupSize  | Integer | 可以为 5、10 或 25  |

#### KILLED\_BY\_CREATURE = 20

| 列     | 字段           | 类型    |
| ------ | -------------- | ------- |
| 4      | creatureEntry  | Integer |

#### FALL\_WITHOUT\_DYING = 24

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | unused      | Integer |
| 5      | fallHeight  | Integer |

#### DEATHS\_FROM = 26

| 列     | 字段                 | 类型   |
| ------ | -------------------- | ------ |
| 4      | EnvironmentalDamage | iRefID |

#### COMPLETE\_QUEST = 27

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | questID     | Integer |
| 5      | questCount  | Integer |

#### BE\_SPELL\_TARGET = 28

#### BE\_SPELL\_TARGET2 = 69

| 列     | 字段            | 类型    |
| ------ | --------------- | ------- |
| 4      | [Spell](spell)  | iRefID  |
| 5      | spellCount      | Integer |

#### CAST\_SPELL = 29

#### CAST\_SPELL2 = 110

| 列     | 字段            | 类型    |
| ------ | --------------- | ------- |
| 4      | [Spell](spell)  | iRefID  |
| 5      | castCount       | Integer |

#### BG\_OBJECTIVE\_CAPTURE = 30

| 列     | 字段      | 类型    | 注释                        |
| ------ | --------- | ------- | --------------------------- |
| 4      | unknow    | Integer | 值 42 = 夺取旗帜            |
| 5      | count(?)  | Integer | 需要夺取多少次              |

#### HONORABLE\_KILL\_AT\_AREA = 31

| 列     | 字段               | 类型    |
| ------ | ------------------ | ------- |
| 4      | [Area](areatable)  | iRefID  |
| 5      | killCount          | Integer |

#### WIN\_ARENA = 32

#### PLAY\_ARENA = 33

| 列     | 字段        | 类型   |
| ------ | ----------- | ------ |
| 4      | [Map](map)  | iRefID |

#### LEARN\_SPELL = 34

| 列     | 字段            | 类型   |
| ------ | --------------- | ------ |
| 4      | [Spell](spell)  | iRefID |

#### OWN\_ITEM = 36

#### WIN\_RATED\_ARENA = 37

| 列     | 字段   | 类型    | 注释           |
| ------ | ------ | ------- | -------------- |
| 4      | unused | Integer |                |
| 5      | count  | Integer |                |
| 6      | flag   | Integer | 4=连续         |

#### HIGHEST\_TEAM\_RATING = 38

| 列     | 字段      | 类型    | 注释     |
| ------ | --------- | ------- | -------- |
| 4      | teamtype  | Integer | {2,3,5}  |

#### REACH\_TEAM\_RATING = 39

| 列     | 字段        | 类型    | 注释     |
| ------ | ----------- | ------- | -------- |
| 4      | teamtype    | Integer | {2,3,5}  |
| 5      | teamrating  | Integer |          |

#### LEARN\_SKILL\_LEVEL = 40

| 列     | 字段        | 类型    | 注释                                                                          |
| ------ | ----------- | ------- | ----------------------------------------------------------------------------- |
| 4      | skillID     | iRefID  | [SkillLine.dbc](skillline) 或其他？                                           |
| 5      | skillLevel  | Integer | 学徒=1，熟练工=2，专家=3，工匠=4，大师=5，宗师=6                             |

#### USE\_ITEM = 41

#### LOOT\_ITEM = 42

#### EXPLORE\_AREA = 43

- 此 areaReference **不是**来自 [AreaTable.dbc](areatable) 的索引。它来自 WorldMapOverlay.dbc。

| 列     | 字段           | 类型    |
| ------ | -------------- | ------- |
| 4      | areaReference  | Integer |

#### OWN\_RANK = 44

- 此等级**不是**来自 [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles) 的索引

| 列     | 字段   | 类型    |
| ------ | ------ | ------- |
| 4      | rank   | Integer |

#### BUY\_BANK\_SLOT = 45

| 列     | 字段           | 类型    |
| ------ | -------------- | ------- |
| 4      | unused         | Integer |
| 5      | numberOfSlots  | Integer |

#### GAIN\_REPUTATION = 46

| 列     | 字段                | 类型    | 注释                                          |
| ------ | ------------------- | ------- | --------------------------------------------- |
| 4      | [Faction](faction)  | iRefID  |                                               |
| 5      | reputationAmount    | Integer | 总声望值，所以 42000 = 崇拜                   |

#### GAIN\_EXALTED\_REPUTATION = 47

| 列     | 字段                     | 类型    |
| ------ | ------------------------ | ------- |
| 4      | unused                  | Integer |
| 5      | numberOfExaltedFactions | Integer |

#### VISIT\_BARBER\_SHOP = 48

| 列     | 字段            | 类型    |
| ------ | --------------- | ------- |
| 4      | unused          | Integer |
| 5      | numberOfVisits  | Integer |

#### EQUIP\_EPIC\_ITEM = 49

- [ItemLevel](item_template#itemlevel)

| 列     | 字段      | 类型    |
| ------ | --------- | ------- |
| 4      | itemSlot  | Integer |

#### ROLL\_NEED\_ON\_LOOT = 50

#### ROLL\_GREED\_ON\_LOOT = 51

| 列     | 字段       | 类型    |
| ------ | ---------- | ------- |
| 4      | rollValue  | Integer |
| 5      | count      | Integer |

#### HK\_CLASS = 52

| 列     | 字段                 | 类型    |
| ------ | -------------------- | ------- |
| 4      | [Class](chrclasses)  | iRefID  |
| 5      | count                | Integer |

#### HK\_RACE = 53

| 列     | 字段              | 类型    |
| ------ | ----------------- | ------- |
| 4      | [Race](chrraces)  | iRefID  |
| 5      | count             | Integer |

#### DO\_EMOTE = 54

- 关于目标的信息存储在哪里？

| 列     | 字段             | 类型    | 注释                                                                |
| ------ | ---------------- | ------- | ------------------------------------------------------------------- |
| 4      | [Emote](emotes)  | iRefID  |                                                                     |
| 5      | count            | Integer | 表情数量，总是需要特殊目标或满足要求                                 |

#### HEALING\_DONE = 55

#### GET\_KILLING\_BLOWS = 56

| 列     | 字段            | 类型    | 注释                        |
| ------ | --------------- | ------- | --------------------------- |
| 4      | unused          | Integer |                             |
| 5      | count           | Integer |                             |
| 6      | flag            | Integer | 3 表示战场治疗              |
| 7      | [Map](map)      | iRefID  |                             |

#### EQUIP\_ITEM = 57

| 列     | 字段                   | 类型    |
| ------ | ---------------------- | ------- |
| 4      | [Item](item_template)  | iRefID  |
| 5      | itemCount              | Integer |

#### MONEY\_FROM\_QUEST\_REWARD = 62

#### LOOT\_MONEY = 67

| 列     | 字段          | 类型    |
| ------ | ------------- | ------- |
| 4      | unused        | Integer |
| 5      | goldInCopper  | Integer |

#### USE\_GAMEOBJECT = 68

| 列     | 字段      | 类型    |
| ------ | --------- | ------- |
| 4      | goEntry   | Integer |
| 5      | useCount  | Integer |

#### SPECIAL\_PVP\_KILL = 70

- 这些特殊条件是否存储在 dbc 中？

| 列     | 字段       | 类型    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | killCount  | Integer |

#### FISH\_IN\_GAMEOBJECT = 72

| 列     | 字段       | 类型    |
| ------ | ---------- | ------- |
| 4      | goEntry    | Integer |
| 5      | lootCount  | Integer |

#### LEARN\_SKILLLINE\_SPELLS = 75

| 列     | 字段                    | 类型    |
| ------ | ----------------------- | ------- |
| 4      | [SkillLine](skillline)  | iRefID  |
| 5      | spellCount              | Integer |

#### WIN\_DUEL = 76

| 列     | 字段       | 类型    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | duelCount  | Integer |

#### HIGHEST\_POWER = 96

| 列     | 字段       | 类型    | 注释                                          |
| ------ | ---------- | ------- | --------------------------------------------- |
| 4      | powerType  | Integer | 0=法力，1=怒气，3=能量，6=符文能量             |

#### HIGHEST\_STAT = 97

| 列     | 字段      | 类型    | 注释                                                   |
| ------ | --------- | ------- | ------------------------------------------------------ |
| 4      | statType  | Integer | 4=精神，3=智力，2=耐力，1=敏捷，0=力量                  |

#### HIGHEST\_SPELLPOWER = 98

| 列     | 字段         | 类型   | 注释                                      |
| ------ | ------------ | ------ | ----------------------------------------- |
| 4      | spellSchool  | iRefID | [SkillLine](skillline) 或抗性              |

#### HIGHEST\_RATING = 100

| 列     | 字段        | 类型    |
| ------ | ----------- | ------- |
| 4      | ratingType  | Integer |

#### LOOT\_TYPE = 109

| 列     | 字段           | 类型    | 注释                                      |
| ------ | -------------- | ------- | ----------------------------------------- |
| 4      | lootType       | Integer | 3=钓鱼，2=偷窃，4=分解                     |
| 5      | lootTypeCount  | Integer |                                           |

#### LEARN\_SKILL\_LINE = 112

| 列     | 字段                    | 类型    |
| ------ | ----------------------- | ------- |
| 4      | [SkillLine](skillline)  | iRefID  |
| 5      | spellCount              | Integer |

#### EARN\_HONORABLE\_KILL = 113

| 列     | 字段       | 类型    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | killCount  | Integer |

#### ACCEPTED\_SUMMONS = 114

| 列     | 字段                                         | 类型    |
| ------ | -------------------------------------------- | ------- |
| 4      | unused                                       | Integer |
| 5      | 这里填 1，因为它是一个统计项                 | Integer |

#### ACHIVEMENTPOINTS\_REACHED = 115

| 列     | 字段    | 类型    |
| ------ | ------- | ------- |
| 4      | unused  | Integer |
| 5      | unused  | Integer |

// 这个东西真的让我很困惑... 也许它只用于"Over Ninethousand"，因为没有任何地方指定成就点数

#### RANDOM\_DUNGEON\_PLAYERCOUNT = 119

| 列     | 字段          | 类型    |
| ------ | ------------- | ------- |
| 4      | unused        | Integer |
| 5      | PlayerCount   | Integer |
