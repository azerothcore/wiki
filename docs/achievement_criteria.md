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

| Column | Field             | Type    | Notes                                                                |
| ------ | ----------------- | ------- | -------------------------------------------------------------------- |
| 1      | ID                | Integer | Criteria ID                                                          |
| 2      | Achievement       | iRefID  | Reference to the achievement this criteria is needed for.            |
| 3      | Type              | Integer | Which type is this criteria? This defines the rows below. See below. |
| 4      | asset_id          | Integer | Main requirement                                                     |
| 5      | Quantity          | Integer | Main requirement count                                               |
| 6      | start_event       | Integer | additional requirement 1 type                                        |
| 7      | start_asset       | Integer | additional requirement 1 value                                       |
| 8      | fail_event        | Integer | additional requirement 2 type                                        |
| 9      | fail_asset        | Integer | additional requirement 2 value                                       |
| 10-25  | Description       | Loc     | Criteria description.                                                |
| 26     | ?                 |         | Mostly 16712190, but not always                                      |
| 27     | Flags             | Integer | display flags: 1: shows progress bar (other flags I don't know)      |
| 28     | timer_start_event | Integer |                                                                      |
| 29     | timer_asset_id    | Integer |                                                                      |
| 30     | timer_time        | Integer | Complete quest in %i seconds.                                        |
| 31     | ui_order          | Integer |                                                                      |

**Description of the fields**

This describes rows 3 to 9 by type (row 2). There may be more types. Unlisted fields are zero.

This information is retrieved from DBCStructure.h.

#### KILL\_CREATURE = 0

*Also used for player deaths..*

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | creatureID | Integer |
| 5      | killCount  | Integer |

#### WIN\_BG = 1

*There are further criterias instead just winning*

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | [Map](Map) | iRefID  |
| 5      | winCount   | Integer |

#### REACH\_LEVEL = 5

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 4      | unused | Integer |
| 5      | level  | Integer |

#### REACH\_SKILL\_LEVEL = 7

| Column | Field      | Type    | Notes                               |
| ------ | ---------- | ------- | ----------------------------------- |
| 4      | skillID    | iRefID  | [SkillLine.dbc](SkillLine) or what? |
| 5      | skillLevel | Integer |                                     |

#### COMPLETE\_ACHIEVEMENT = 8

| Column | Field                      | Type   |
| ------ | -------------------------- | ------ |
| 4      | [Achievement](Achievement) | iRefID |

#### COMPLETE\_QUEST\_COUNT = 9

| Column | Field           | Type    |
| ------ | --------------- | ------- |
| 4      | unused          | Integer |
| 5      | totalQuestCount | Integer |

#### COMPLETE\_DAILY\_QUEST\_DAILY = 10

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 4      | unused       | Integer |
| 5      | numberOfDays | Integer |

#### COMPLETE\_QUESTS\_IN\_ZONE = 11

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | zoneID     | Integer |
| 5      | questCount | Integer |

#### DAMAGE\_DONE = 13

#### COMPLETE\_DAILY\_QUEST = 14

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | questCount | Integer |

#### COMPLETE\_BATTLEGROUND = 15

#### DEATH\_AT\_MAP = 16

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 4      | [Map](Map) | iRefID |

#### DEATH\_IN\_DUNGEON = 18

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 4      | manLimit | Integer |

#### COMPLETE\_RAID = 19

| Column | Field     | Type    | Notes              |
| ------ | --------- | ------- | ------------------ |
| 4      | groupSize | Integer | can be 5, 10 or 25 |

#### KILLED\_BY\_CREATURE = 20

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 4      | creatureEntry | Integer |

#### FALL\_WITHOUT\_DYING = 24

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | unused     | Integer |
| 5      | fallHeight | Integer |

#### DEATHS\_FROM = 26

| Column | Field               | Type   |
| ------ | ------------------- | ------ |
| 4      | EnvironmentalDamage | iRefID |

#### COMPLETE\_QUEST = 27

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | questID    | Integer |
| 5      | questCount | Integer |

#### BE\_SPELL\_TARGET = 28

#### BE\_SPELL\_TARGET2 = 69

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 4      | [Spell](Spell) | iRefID  |
| 5      | spellCount     | Integer |

#### CAST\_SPELL = 29

#### CAST\_SPELL2 = 110

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 4      | [Spell](Spell) | iRefID  |
| 5      | castCount      | Integer |

#### BG\_OBJECTIVE\_CAPTURE = 30

| Column | Field    | Type    | Notes                       |
| ------ | -------- | ------- | --------------------------- |
| 4      | unknow   | Integer | value 42 = capture the flag |
| 5      | count(?) | Integer | how many captures required  |

#### HONORABLE\_KILL\_AT\_AREA = 31

| Column | Field             | Type    |
| ------ | ----------------- | ------- |
| 4      | [Area](AreaTable) | iRefID  |
| 5      | killCount         | Integer |

#### WIN\_ARENA = 32

#### PLAY\_ARENA = 33

| Column | Field      | Type   |
| ------ | ---------- | ------ |
| 4      | [Map](Map) | iRefID |

#### LEARN\_SPELL = 34

| Column | Field          | Type   |
| ------ | -------------- | ------ |
| 4      | [Spell](Spell) | iRefID |

#### OWN\_ITEM = 36

#### WIN\_RATED\_ARENA = 37

| Column | Field  | Type    | Notes      |
| ------ | ------ | ------- | ---------- |
| 4      | unused | Integer |            |
| 5      | count  | Integer |            |
| 6      | flag   | Integer | 4=in a row |

#### HIGHEST\_TEAM\_RATING = 38

| Column | Field    | Type    | Notes   |
| ------ | -------- | ------- | ------- |
| 4      | teamtype | Integer | {2,3,5} |

#### REACH\_TEAM\_RATING = 39

| Column | Field      | Type    | Notes   |
| ------ | ---------- | ------- | ------- |
| 4      | teamtype   | Integer | {2,3,5} |
| 5      | teamrating | Integer |         |

#### LEARN\_SKILL\_LEVEL = 40

| Column | Field      | Type    | Notes                                                                     |
| ------ | ---------- | ------- | ------------------------------------------------------------------------- |
| 4      | skillID    | iRefID  | [SkillLine.dbc](SkillLine) or what?                                       |
| 5      | skillLevel | Integer | apprentice=1, journeyman=2, expert=3, artisan=4, master=5, grand master=6 |

#### USE\_ITEM = 41

#### LOOT\_ITEM = 42

#### EXPLORE\_AREA = 43

- This areaReference is **NOT** the index from [AreaTable.dbc.](AreaTable) It's from WorldMapOverlay.dbc.

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 4      | areaReference | Integer |

#### OWN\_RANK = 44

- This rank is **NOT** the index from [CharTitles.dbc](CharTitles)

| Column | Field | Type    |
| ------ | ----- | ------- |
| 4      | rank  | Integer |

#### BUY\_BANK\_SLOT = 45

| Column | Field         | Type    |
| ------ | ------------- | ------- |
| 4      | unused        | Integer |
| 5      | numberOfSlots | Integer |

#### GAIN\_REPUTATION = 46

| Column | Field              | Type    | Notes                                       |
| ------ | ------------------ | ------- | ------------------------------------------- |
| 4      | [Faction](Faction) | iRefID  |                                             |
| 5      | reputationAmount   | Integer | Total reputation amount, so 42000 = exalted |

#### GAIN\_EXALTED\_REPUTATION= 47

| Column | Field                   | Type    |
| ------ | ----------------------- | ------- |
| 4      | unused                  | Integer |
| 5      | numberOfExaltedFactions | Integer |

#### VISIT\_BARBER\_SHOP = 48

| Column | Field          | Type    |
| ------ | -------------- | ------- |
| 4      | unused         | Integer |
| 5      | numberOfVisits | Integer |

#### EQUIP\_EPIC\_ITEM = 49

- [ItemLevel](item_template#itemlevel)

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 4      | itemSlot | Integer |

#### ROLL\_NEED\_ON\_LOOT = 50

#### ROLL\_GREED\_ON\_LOOT = 51

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | rollValue | Integer |
| 5      | count     | Integer |

#### HK\_CLASS = 52

| Column | Field               | Type    |
| ------ | ------------------- | ------- |
| 4      | [Class](ChrClasses) | iRefID  |
| 5      | count               | Integer |

#### HK\_RACE = 53

| Column | Field            | Type    |
| ------ | ---------------- | ------- |
| 4      | [Race](ChrRaces) | iRefID  |
| 5      | count            | Integer |

#### DO\_EMOTE = 54

- where is the information about the target stored?

| Column | Field           | Type    | Notes                                                           |
| ------ | --------------- | ------- | --------------------------------------------------------------- |
| 4      | [Emote](Emotes) | iRefID  |                                                                 |
| 5      | count           | Integer | count of emotes, always required special target or requirements |

#### HEALING\_DONE = 55

#### GET\_KILLING\_BLOWS = 56

| Column | Field          | Type    | Notes                      |
| ------ | -------------- | ------- | -------------------------- |
| 4      | unused         | Integer |                            |
| 5      | count          | Integer |                            |
| 6      | flag           | Integer | 3 for battleground healing |
| 7      | [Map](Map.dbc) | iRefID  |                            |

#### EQUIP\_ITEM = 57

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 4      | [Item](Item) | iRefID  |
| 5      | itemCount    | Integer |

#### MONEY\_FROM\_QUEST\_REWARD= 62

#### LOOT\_MONEY = 67

| Column | Field        | Type    |
| ------ | ------------ | ------- |
| 4      | unused       | Integer |
| 5      | goldInCopper | Integer |

#### USE\_GAMEOBJECT = 68

| Column | Field    | Type    |
| ------ | -------- | ------- |
| 4      | goEntry  | Integer |
| 5      | useCount | Integer |

#### SPECIAL\_PVP\_KILL = 70

- Are those special criteria stored in the dbc?

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | unused    | Integer |
| 5      | killCount | Integer |

#### FISH\_IN\_GAMEOBJECT = 72

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | goEntry   | Integer |
| 5      | lootCount | Integer |

#### LEARN\_SKILLLINE\_SPELLS = 75

| Column | Field                  | Type    |
| ------ | ---------------------- | ------- |
| 4      | [SkillLine](SkillLine) | iRefID  |
| 5      | spellCount             | Integer |

#### WIN\_DUEL = 76

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | unused    | Integer |
| 5      | duelCount | Integer |

#### HIGHEST\_POWER = 96

| Column | Field     | Type    | Notes                                   |
| ------ | --------- | ------- | --------------------------------------- |
| 4      | powerType | Integer | 0=mana, 1=rage, 3=energy, 6=runic power |

#### HIGHEST\_STAT = 97

| Column | Field    | Type    | Notes                                         |
| ------ | -------- | ------- | --------------------------------------------- |
| 4      | statType | Integer | 4=spirit, 3=int, 2=stamina, 1=agi, 0=strength |

#### HIGHEST\_SPELLPOWER = 98

| Column | Field       | Type   | Notes                                 |
| ------ | ----------- | ------ | ------------------------------------- |
| 4      | spellSchool | iRefID | [SkillLine](SkillLine) or Resistances |

#### HIGHEST\_RATING = 100

| Column | Field      | Type    |
| ------ | ---------- | ------- |
| 4      | ratingType | Integer |

#### LOOT\_TYPE = 109

| Column | Field         | Type    | Notes                                  |
| ------ | ------------- | ------- | -------------------------------------- |
| 4      | lootType      | Integer | 3=fishing, 2=pickpocket, 4=disentchant |
| 5      | lootTypeCount | Integer |                                        |

#### LEARN\_SKILL\_LINE = 112

| Column | Field                  | Type    |
| ------ | ---------------------- | ------- |
| 4      | [SkillLine](SkillLine) | iRefID  |
| 5      | spellCount             | Integer |

#### EARN\_HONORABLE\_KILL = 113

| Column | Field     | Type    |
| ------ | --------- | ------- |
| 4      | unused    | Integer |
| 5      | killCount | Integer |

#### ACCEPTED\_SUMMONS = 114

| Column | Field                                       | Type    |
| ------ | ------------------------------------------- | ------- |
| 4      | unused                                      | Integer |
| 5      | Here comes a 1 in, because it's a Statistic | Integer |

#### ACHIVEMENTPOINTS\_REACHED = 115

| Column | Field  | Type    |
| ------ | ------ | ------- |
| 4      | unused | Integer |
| 5      | unused | Integer |

// This thing really confuses me... Maybe it is only used for "Over Ninethousand", because nowhere AchPoints are Specified

#### RANDOM\_DUNGEON\_PLAYERCOUNT = 119

| Column | Field       | Type    |
| ------ | ----------- | ------- |
| 4      | unused      | Integer |
| 5      | PlayerCount | Integer |
