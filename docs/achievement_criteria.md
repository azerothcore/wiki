---
redirect_from: "/Achievement_Criteria"
---

# Achievement Criteria

[`Back-to:DBC`](dbc-index)

**Achievement\_Criteria.dbc**

This DBC has been added with WoW 3.0.1.8303 and contains the needed criteria to obtain an achievement.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db)  

## Structure

| Column | Field                          | Type   | achievement\_criteria\_dbc column                                 | Comment                                                                                                                                                |
| :----: | :----------------------------- | :----- | :---------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | ID                             | uint32 | [ID](achievement_criteria_dbc#id)                                 | Criteria ID                                                                                                                                            |
| 1      | AchievementID                  | uint32 | [Achievement_Id](achievement_criteria_dbc#achievementid)          | Reference to the achievement this criteria is needed for. ID in [Achievement.dbc](achievement) (147 of the 1921 values used here are not in that file) |
| 2      | Type                           | uint32 | [Type](achievement_criteria_dbc#type)                             | Which type is this criteria? This defines the rows below. See below.                                                                                   |
| 3      | Asset                          | uint32 | [Asset_Id](achievement_criteria_dbc#assetid)                      | Main requirement                                                                                                                                       |
| 4      | Quantity                       | uint32 | [Quantity](achievement_criteria_dbc#quantity)                     | Main requirement count                                                                                                                                 |
| 5      | AdditionalRequirements_Type_0  | uint32 | [Start_Event](achievement_criteria_dbc#startevent)                | additional requirement 1 type                                                                                                                          |
| 6      | AdditionalRequirements_Asset_0 | uint32 | [Start_Asset](achievement_criteria_dbc#startasset)                | additional requirement 1 value                                                                                                                         |
| 7      | AdditionalRequirements_Type_1  | uint32 | [Fail_Event](achievement_criteria_dbc#failevent)                  | additional requirement 2 type                                                                                                                          |
| 8      | AdditionalRequirements_Asset_1 | uint32 | [Fail_Asset](achievement_criteria_dbc#failasset)                  | additional requirement 2 value                                                                                                                         |
| 9      | Description_0                  | string | [Description_Lang_enUS](achievement_criteria_dbc#descriptionlang) | Criteria description. Assumed enUS                                                                                                                     |
| 10     | Description_1                  | string | [Description_Lang_enGB](achievement_criteria_dbc#descriptionlang) | Assumed enGB, not used in 3.3.5a                                                                                                                       |
| 11     | Description_2                  | string | [Description_Lang_koKR](achievement_criteria_dbc#descriptionlang) | Assumed koKR                                                                                                                                           |
| 12     | Description_3                  | string | [Description_Lang_frFR](achievement_criteria_dbc#descriptionlang) | Assumed frFR                                                                                                                                           |
| 13     | Description_4                  | string | [Description_Lang_deDE](achievement_criteria_dbc#descriptionlang) | Assumed deDE                                                                                                                                           |
| 14     | Description_5                  | string | [Description_Lang_enCN](achievement_criteria_dbc#descriptionlang) | Assumed enCN, not used in 3.3.5a                                                                                                                       |
| 15     | Description_6                  | string | [Description_Lang_zhCN](achievement_criteria_dbc#descriptionlang) | Assumed zhCN                                                                                                                                           |
| 16     | Description_7                  | string | [Description_Lang_enTW](achievement_criteria_dbc#descriptionlang) | Assumed enTW, not used in 3.3.5a                                                                                                                       |
| 17     | Description_8                  | string | [Description_Lang_zhTW](achievement_criteria_dbc#descriptionlang) | Assumed zhTW                                                                                                                                           |
| 18     | Description_9                  | string | [Description_Lang_esES](achievement_criteria_dbc#descriptionlang) | Assumed esES                                                                                                                                           |
| 19     | Description_10                 | string | [Description_Lang_esMX](achievement_criteria_dbc#descriptionlang) | Assumed esMX                                                                                                                                           |
| 20     | Description_11                 | string | [Description_Lang_ruRU](achievement_criteria_dbc#descriptionlang) | Assumed ruRU                                                                                                                                           |
| 21     | Description_12                 | string | [Description_Lang_ptPT](achievement_criteria_dbc#descriptionlang) | Assumed ptPT, not used in 3.3.5a                                                                                                                       |
| 22     | Description_13                 | string | [Description_Lang_ptBR](achievement_criteria_dbc#descriptionlang) | Assumed ptBR, not used in 3.3.5a                                                                                                                       |
| 23     | Description_14                 | string | [Description_Lang_itIT](achievement_criteria_dbc#descriptionlang) | Assumed itIT, not used in 3.3.5a                                                                                                                       |
| 24     | Description_15                 | string | [Description_Lang_Unk](achievement_criteria_dbc#descriptionlang)  | Unknown language, unsure of the usage in 3.3.5a                                                                                                        |
| 25     | Description_lang_mask          | uint32 | [Description_Lang_Mask](achievement_criteria_dbc#descriptionlang) | Mostly 16712190, but not always. Assumed flags of the localized text                                                                                   |
| 26     | Flags                          | uint32 | [Flags](achievement_criteria_dbc#flags)                           | display flags: 1: shows progress bar (other flags I don't know)                                                                                        |
| 27     | StartEvent                     | uint32 | [Timer_Start_Event](achievement_criteria_dbc#timerstartevent)     |                                                                                                                                                        |
| 28     | StartAsset                     | uint32 | [Timer_Asset_Id](achievement_criteria_dbc#timerassetid)           |                                                                                                                                                        |
| 29     | StartTimer                     | uint32 | [Timer_Time](achievement_criteria_dbc#timertime)                  | Complete quest in %i seconds.                                                                                                                          |
| 30     | UiOrder                        | uint32 | [Ui_Order](achievement_criteria_dbc#uiorder)                      |                                                                                                                                                        |

The language of each of the 16 text columns of a localized field is assumed from the column names of the `_dbc` tables. A language is marked as not used in 3.3.5a when it is not in the core's locale list.

**Description of the fields**

This describes columns 3 to 8 by type (column 2), numbered from 0 as in the structure table above. There may be more types. Unlisted fields are zero.

The field names are the ones of the `AchievementCriteriaEntry` struct in AzerothCore's [DBCStructure.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/DataStores/DBCStructure.h), and the type names are the ones of `AchievementCriteriaTypes` in [DBCEnums.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/DataStores/DBCEnums.h), without the `ACHIEVEMENT_CRITERIA_TYPE_` prefix. Types 30, 114, 115 and 119, and the last columns listed for types 37 and 56, are not described in DBCStructure.h: they are kept from earlier documentation.

#### KILL\_CREATURE = 0

*Also used for player deaths..*

| Column | Field                                 | Type    |
| ------ | ------------------------------------- | ------- |
| 3      | [creatureID](creature_template#entry) | iRefID  |
| 4      | creatureCount                         | Integer |

#### WIN\_BG = 1

*There are further criterias instead just winning*

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 3      | [Map](map) | iRefID  |
| 4      | winCount   | Integer |

#### REACH\_LEVEL = 5

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 3      | unused | Integer |
| 4      | level  | Integer |

#### REACH\_SKILL\_LEVEL = 7

| Column | Field                | Type    | Notes                               |
| ------ | -------------------- | ------- | ----------------------------------- |
| 3      | [skillID](skillline) | iRefID  | ID in [SkillLine.dbc](skillline) |
| 4      | skillLevel           | Integer |                                     |

#### COMPLETE\_ACHIEVEMENT = 8

| Column | Field                      | Type   |
| ------ | -------------------------- | ------ |
| 3      | [Achievement](achievement) | iRefID |

#### COMPLETE\_QUEST\_COUNT = 9

| Column | Field           | Type    |
| ------ | --------------- | ------- |
| 3      | unused          | Integer |
| 4      | totalQuestCount | Integer |

#### COMPLETE\_DAILY\_QUEST\_DAILY = 10

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 3      | unused       | Integer |
| 4      | numberOfDays | Integer |

#### COMPLETE\_QUESTS\_IN\_ZONE = 11

| Column | Field               | Type    |
| ------ | ------------------- | ------- |
| 3      | [zoneID](areatable) | iRefID  |
| 4      | questCount          | Integer |

#### DAMAGE\_DONE = 13

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 3      | unused | Integer |
| 4      | count  | Integer |

#### COMPLETE\_DAILY\_QUEST = 14

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 3      | unused     | Integer |
| 4      | questCount | Integer |

#### COMPLETE\_BATTLEGROUND = 15

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 3      | [Map](map) | iRefID |

#### DEATH\_AT\_MAP = 16

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 3      | [Map](map) | iRefID |

#### DEATH\_IN\_DUNGEON = 18

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 3      | manLimit | Integer |

#### COMPLETE\_RAID = 19

| Column | Field     | Type    | Notes              |
| ------ | --------- | ------- | ------------------ |
| 3      | groupSize | Integer | can be 5, 10 or 25 |

#### KILLED\_BY\_CREATURE = 20

| Column | Field                                    | Type   |
| ------ | ---------------------------------------- | ------ |
| 3      | [creatureEntry](creature_template#entry) | iRefID |

#### FALL\_WITHOUT\_DYING = 24

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 3      | unused     | Integer |
| 4      | fallHeight | Integer |

#### DEATHS\_FROM = 26

| Column | Field               | Type   |
| ------ | ------------------- | ------ |
| 3      | EnvironmentalDamage | iRefID |

#### COMPLETE\_QUEST = 27

| Column | Field                        | Type    |
| ------ | ---------------------------- | ------- |
| 3      | [questID](quest_template#id) | iRefID  |
| 4      | questCount                   | Integer |

#### BE\_SPELL\_TARGET = 28

Uses the same columns as BE\_SPELL\_TARGET2 below.

#### BE\_SPELL\_TARGET2 = 69

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 3      | [Spell](spell) | iRefID  |
| 4      | spellCount     | Integer |

#### CAST\_SPELL = 29

Uses the same columns as CAST\_SPELL2 below.

#### CAST\_SPELL2 = 110

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 3      | [Spell](spell) | iRefID  |
| 4      | castCount      | Integer |

#### BG\_OBJECTIVE\_CAPTURE = 30

| Column | Field    | Type    | Notes                       |
| ------ | -------- | ------- | --------------------------- |
| 3      | unknow   | Integer | value 42 = capture the flag |
| 4      | count(?) | Integer | how many captures required  |

#### HONORABLE\_KILL\_AT\_AREA = 31

| Column | Field             | Type    |
| ------ | ----------------- | ------- |
| 3      | [Area](areatable) | iRefID  |
| 4      | killCount         | Integer |

#### WIN\_ARENA = 32

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 3      | [Map](map) | iRefID  |
| 4      | count      | Integer |

#### PLAY\_ARENA = 33

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 3      | [Map](map) | iRefID |

#### LEARN\_SPELL = 34

| Column | Field          | Type   |
| ------ | -------------- | ------ |
| 3      | [Spell](spell) | iRefID |

#### OWN\_ITEM = 36

| Column | Field                 | Type    |
| ------ | --------------------- | ------- |
| 3      | [Item](item_template) | iRefID  |
| 4      | itemCount             | Integer |

#### WIN\_RATED\_ARENA = 37

| Column | Field  | Type    | Notes      |
| ------ | ------ | ------- | ---------- |
| 3      | unused | Integer |            |
| 4      | count  | Integer |            |
| 5      | flag   | Integer | 4=in a row |

#### HIGHEST\_TEAM\_RATING = 38

| Column | Field    | Type    | Notes   |
| ------ | -------- | ------- | ------- |
| 3      | teamtype | Integer | {2,3,5} |

#### REACH\_TEAM\_RATING = 39

| Column | Field          | Type    | Notes   |
| ------ | -------------- | ------- | ------- |
| 3      | teamtype       | Integer | {2,3,5} |
| 4      | PersonalRating | Integer |         |

#### LEARN\_SKILL\_LEVEL = 40

| Column | Field                | Type    | Notes                                                                     |
| ------ | -------------------- | ------- | ------------------------------------------------------------------------- |
| 3      | [skillID](skillline) | iRefID  | ID in [SkillLine.dbc](skillline)                                       |
| 4      | skillLevel           | Integer | apprentice=1, journeyman=2, expert=3, artisan=4, master=5, grand master=6 |

#### USE\_ITEM = 41

| Column | Field                 | Type    |
| ------ | --------------------- | ------- |
| 3      | [Item](item_template) | iRefID  |
| 4      | itemCount             | Integer |

#### LOOT\_ITEM = 42

| Column | Field                 | Type    |
| ------ | --------------------- | ------- |
| 3      | [Item](item_template) | iRefID  |
| 4      | itemCount             | Integer |

#### EXPLORE\_AREA = 43

- This areaReference is **NOT** the index from [AreaTable.dbc.](areatable) It's from WorldMapOverlay.dbc.

| Column | Field                                | Type   |
| ------ | ------------------------------------ | ------ |
| 3      | [areaReference](dbc-worldmapoverlay) | iRefID |

#### OWN\_RANK = 44

- This rank is **NOT** the index from [CharTitles.dbc](https://wowdev.wiki/DB/CharTitles)

| Column | Field | Type    |
| ------ | ----- | ------- |
| 3      | rank  | Integer |

#### BUY\_BANK\_SLOT = 45

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 3      | unused        | Integer |
| 4      | numberOfSlots | Integer |

#### GAIN\_REPUTATION = 46

| Column | Field              | Type    | Notes                                       |
| ------ | ------------------ | ------- | ------------------------------------------- |
| 3      | [Faction](faction) | iRefID  |                                             |
| 4      | reputationAmount   | Integer | Total reputation amount, so 42000 = exalted |

#### GAIN\_EXALTED\_REPUTATION= 47

| Column | Field                   | Type    |
| ------ | ----------------------- | ------- |
| 3      | unused                  | Integer |
| 4      | numberOfExaltedFactions | Integer |

#### VISIT\_BARBER\_SHOP = 48

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 3      | unused         | Integer |
| 4      | numberOfVisits | Integer |

#### EQUIP\_EPIC\_ITEM = 49

- [ItemLevel](item_template#itemlevel)

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 3      | itemSlot | Integer |
| 4      | count    | Integer |

#### ROLL\_NEED\_ON\_LOOT = 50

Uses the same columns as ROLL\_GREED\_ON\_LOOT below.

#### ROLL\_GREED\_ON\_LOOT = 51

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 3      | rollValue | Integer |
| 4      | count     | Integer |

#### HK\_CLASS = 52

| Column | Field               | Type    |
| ------ | ------------------- | ------- |
| 3      | [Class](chrclasses) | iRefID  |
| 4      | count               | Integer |

#### HK\_RACE = 53

| Column | Field            | Type    |
| ------ | ---------------- | ------- |
| 3      | [Race](chrraces) | iRefID  |
| 4      | count            | Integer |

#### DO\_EMOTE = 54

- where is the information about the target stored?

| Column | Field                     | Type    | Notes                                                           |
| ------ | ------------------------- | ------- | --------------------------------------------------------------- |
| 3      | [emoteID](dbc-emotestext) | iRefID  |                                                                 |
| 4      | count                     | Integer | count of emotes, always required special target or requirements |

#### HEALING\_DONE = 55

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 3      | unused | Integer |
| 4      | count  | Integer |

#### GET\_KILLING\_BLOWS = 56

| Column | Field          | Type    | Notes                      |
| ------ | -------------- | ------- | -------------------------- |
| 3      | unused         | Integer |                            |
| 4      | count          | Integer |                            |
| 5      | flag           | Integer | 3 for battleground healing |
| 6      | [Map](map) | iRefID  |                            |

#### EQUIP\_ITEM = 57

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 3      | [Item](item_template) | iRefID  |
| 4      | count        | Integer |

#### MONEY\_FROM\_QUEST\_REWARD= 62

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 3      | unused       | Integer |
| 4      | goldInCopper | Integer |

#### LOOT\_MONEY = 67

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 3      | unused       | Integer |
| 4      | goldInCopper | Integer |

#### USE\_GAMEOBJECT = 68

| Column | Field                                | Type    |
| ------ | ------------------------------------ | ------- |
| 3      | [goEntry](gameobject_template#entry) | iRefID  |
| 4      | useCount                             | Integer |

#### SPECIAL\_PVP\_KILL = 70

- Are those special criteria stored in the dbc?

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 3      | unused    | Integer |
| 4      | killCount | Integer |

#### FISH\_IN\_GAMEOBJECT = 72

| Column | Field                                | Type    |
| ------ | ------------------------------------ | ------- |
| 3      | [goEntry](gameobject_template#entry) | iRefID  |
| 4      | lootCount                            | Integer |

#### LEARN\_SKILLLINE\_SPELLS = 75

| Column | Field                  | Type    |
| ------ | ---------------------- | ------- |
| 3      | [SkillLine](skillline) | iRefID  |
| 4      | spellCount             | Integer |

#### WIN\_DUEL = 76

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 3      | unused    | Integer |
| 4      | duelCount | Integer |

#### HIGHEST\_POWER = 96

| Column | Field     | Type    | Notes                                   |
| ------ | --------- | ------- | --------------------------------------- |
| 3      | powerType | Integer | 0=mana, 1=rage, 3=energy, 6=runic power |

#### HIGHEST\_STAT = 97

| Column | Field    | Type    | Notes                                         |
| ------ | -------- | ------- | --------------------------------------------- |
| 3      | statType | Integer | 4=spirit, 3=int, 2=stamina, 1=agi, 0=strength |

#### HIGHEST\_SPELLPOWER = 98

| Column | Field       | Type   | Notes                                 |
| ------ | ----------- | ------ | ------------------------------------- |
| 3      | spellSchool | iRefID | [SkillLine](skillline) or Resistances |

#### HIGHEST\_RATING = 100

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 3      | ratingType | Integer |

#### LOOT\_TYPE = 109

| Column | Field         | Type    | Notes                                  |
| ------ | ------------- | ------- | -------------------------------------- |
| 3      | lootType      | Integer | 3=fishing, 2=pickpocket, 4=disentchant |
| 4      | lootTypeCount | Integer |                                        |

#### LEARN\_SKILL\_LINE = 112

| Column | Field                  | Type    |
| ------ | ---------------------- | ------- |
| 3      | [SkillLine](skillline) | iRefID  |
| 4      | spellCount             | Integer |

#### EARN\_HONORABLE\_KILL = 113

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 3      | unused    | Integer |
| 4      | killCount | Integer |

#### ACCEPTED\_SUMMONINGS = 114

| Column | Field                                       | Type    |
| ------ | ------------------------------------------- | ------- |
| 3      | unused                                      | Integer |
| 4      | Here comes a 1 in, because it's a Statistic | Integer |

#### EARN\_ACHIEVEMENT\_POINTS = 115

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 3      | unused | Integer |
| 4      | unused | Integer |

// This thing really confuses me... Maybe it is only used for "Over Ninethousand", because nowhere AchPoints are Specified

#### USE\_LFD\_TO\_GROUP\_WITH\_PLAYERS = 119

| Column | Field       | Type    |
| ------ | ----------- | ------- |
| 3      | unused      | Integer |
| 4      | PlayerCount | Integer |
