# quest\_template

[<-Back-to:World](database-world)

**Table: quest\_template**

Contains all basic definitions of available quests.

## **Table Structure**

| Field                           | Type      | Attribute | Key | Null | Default | Extra | Comment |
| ------------------------------- | --------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]                         | MEDIUMINT | UNSIGNED  | PRI | NO   | 0       |       |         |
| [QuestType][2]                  | TINYINT   | UNSIGNED  |     | NO   | 2       |       |         |
| [QuestLevel][3]                 | SMALLINT  |           |     | NO   | 1       |       |         |
| [MinLevel][4]                   | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [QuestSortID][5]                | SMALLINT  |           |     | NO   | 0       |       |         |
| [QuestInfoID][6]                | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [SuggestedGroupNum][7]          | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionId1][8]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionId2][9]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredFactionValue1][10]     | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredFactionValue2][11]     | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardNextQuest][12]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardXPDifficulty][13]        | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardMoney][14]               | INT       |           |     | NO   | 0       |       |         |
| [RewardMoneyDifficulty][15]     | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardDisplaySpell][16]        | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardSpell][17]               | INT       |           |     | NO   | 0       |       |         |
| [RewardHonor][18]               | INT       |           |     | NO   | 0       |       |         |
| [RewardKillHonor][19]           | FLOAT     |           |     | NO   | 0       |       |         |
| [StartItem][20]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [Flags][21]                     | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredPlayerKills][22]       | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem1][23]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount1][24]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem2][25]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount2][26]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem3][27]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount3][28]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardItem4][29]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardAmount4][30]             | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop1][31]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity1][32]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop2][33]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity2][34]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop3][35]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity3][36]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDrop4][37]                 | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [ItemDropQuantity4][38]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID1][39]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity1][40] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID2][41]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity2][42] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID3][43]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity3][44] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID4][45]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity4][46] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID5][47]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity5][48] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemID6][49]       | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity6][50] | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [POIContinent][51]              | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [POIx][52]                      | FLOAT     |           |     | NO   | 0       |       |         |
| [POIy][53]                      | FLOAT     |           |     | NO   | 0       |       |         |
| [POIPriority][54]               | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardTitle][55]               | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardTalents][56]             | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardArenaPoints][57]         | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionID1][58]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue1][59]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride1][60]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID2][61]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue2][62]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride2][63]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID3][64]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue3][65]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride3][66]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID4][67]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue4][68]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride4][69]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionID5][70]          | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RewardFactionValue5][71]       | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RewardFactionOverride5][72]    | MEDIUMINT |           |     | NO   | 0       |       |         |
| [TimeAllowed][73]               | INT       | UNSIGNED  |     | NO   | 0       |       |         |
| [AllowableRaces][74]            | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [LogTitle][75]                  | TEXT      |           |     | YES  |         |       |         |
| [LogDescription][76]            | TEXT      |           |     | YES  |         |       |         |
| [QuestDescription][77]          | TEXT      |           |     | YES  |         |       |         |
| [AreaDescription][78]           | TEXT      |           |     | YES  |         |       |         |
| [QuestCompletionLog][79]        | TEXT      |           |     | YES  |         |       |         |
| [RequiredNpcOrGo1][80]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo2][81]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo3][82]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo4][83]          | MEDIUMINT |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount1][84]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount2][85]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount3][86]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount4][87]     | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId1][88]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId2][89]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId3][90]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId4][91]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId5][92]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemId6][93]           | MEDIUMINT | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount1][94]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount2][95]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount3][96]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount4][97]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount5][98]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [RequiredItemCount6][99]        | SMALLINT  | UNSIGNED  |     | NO   | 0       |       |         |
| [Unknown0][100]                 | TINYINT   | UNSIGNED  |     | NO   | 0       |       |         |
| [ObjectiveText1][101]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText2][102]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText3][103]           | TEXT      |           |     | YES  |         |       |         |
| [ObjectiveText4][104]           | TEXT      |           |     | YES  |         |       |         |
| [VerifiedBuild][105]            | SMALLINT  |           |     | YES  | 0       |       |         |

[1]: #id
[2]: #questtype
[3]: #questlevel
[4]: #minlevel
[5]: #questsortid
[6]: #questinfoid
[7]: #suggestedgroupnum
[8]: #requiredfactionid1
[9]: #requiredfactionid2
[10]: #requiredfactionvalue1
[11]: #requiredfactionvalue2
[12]: #rewardnextquest
[13]: #rewardxpdifficulty
[14]: #rewardmoney
[15]: #rewardmoneydifficulty
[16]: #rewarddisplayspell
[17]: #rewardspell
[18]: #rewardhonor
[19]: #rewardkillhonor
[20]: #startitem
[21]: #flags
[22]: #requiredplayerkills
[23]: #rewarditem1
[24]: #rewardamount1
[25]: #rewarditem2
[26]: #rewardamount2
[27]: #rewarditem3
[28]: #rewardamount3
[29]: #rewarditem4
[30]: #rewardamount4
[31]: #itemdrop1
[32]: #itemdropquantity1
[33]: #itemdrop2
[34]: #itemdropquantity2
[35]: #itemdrop3
[36]: #itemdropquantity3
[37]: #itemdrop4
[38]: #itemdropquantity4
[39]: #rewardchoiceitemid1
[40]: #rewardchoiceitemquantity1
[41]: #rewardchoiceitemid2
[42]: #rewardchoiceitemquantity2
[43]: #rewardchoiceitemid3
[44]: #rewardchoiceitemquantity3
[45]: #rewardchoiceitemid4
[46]: #rewardchoiceitemquantity4
[47]: #rewardchoiceitemid5
[48]: #rewardchoiceitemquantity5
[49]: #rewardchoiceitemid6
[50]: #rewardchoiceitemquantity6
[51]: #poicontinent
[52]: #poix
[53]: #poiy
[54]: #poipriority
[55]: #rewardtitle
[56]: #rewardtalents
[57]: #rewardarenapoints
[58]: #rewardfactionid1
[59]: #rewardfactionvalue1
[60]: #rewardfactionoverride1
[61]: #rewardfactionid2
[62]: #rewardfactionvalue2
[63]: #rewardfactionoverride2
[64]: #rewardfactionid3
[65]: #rewardfactionvalue3
[66]: #rewardfactionoverride3
[67]: #rewardfactionid4
[68]: #rewardfactionvalue4
[69]: #rewardfactionoverride4
[70]: #rewardfactionid5
[71]: #rewardfactionvalue5
[72]: #rewardfactionoverride5
[73]: #timeallowed
[74]: #allowableraces
[75]: #logtitle
[76]: #logdescription
[77]: #questdescription
[78]: #areadescription
[79]: #questcompletionlog
[80]: #requirednpcorgo1
[81]: #requirednpcorgo2
[82]: #requirednpcorgo3
[83]: #requirednpcorgo4
[84]: #requirednpcorgocount1
[85]: #requirednpcorgocount2
[86]: #requirednpcorgocount3
[87]: #requirednpcorgocount4
[88]: #requireditemid1
[89]: #requireditemid2
[90]: #requireditemid3
[91]: #requireditemid4
[92]: #requireditemid5
[93]: #requireditemid6
[94]: #requireditemcount1
[95]: #requireditemcount2
[96]: #requireditemcount3
[97]: #requireditemcount4
[98]: #requireditemcount5
[99]: #requireditemcount6
[100]: #unknown0
[101]: #objectivetext1
[102]: #objectivetext2
[103]: #objectivetext3
[104]: #objectivetext4
[105]: #verifiedbuild


**Description of the fields**

### ID

The quest ID. This column is the Primary Key for the Table. Each quest ID must be unique!

### QuestType

Accepted values: 0, 1 or 2. Their meaning is described in table below.

| Value | Result                                                                                                   |
| ----- | -------------------------------------------------------------------------------------------------------- |
| 0     | Quest is enabled, but it is auto-completed when accepted; this skips quest objectives and quest details. |
| 1     | Quest is disabled (not yet implemented in the core).                                                     |
| 2     | Quest is enabled (does not auto-complete).                                                               |

### QuestLevel

Level of quest. Player receives full experience amount only if their level is less than or equal to Level+5. If Level is set to -1, the player's level will be used as (Quest)Level for the experience calculation.

### MinLevel

Minimum level at which a player can get the quest.

### QuestSortID

This field defines under what category the quest falls in the quest log.

If **value &gt; 0** then value is Zone IDs taken from AreaTable.dbc.

if **value &lt; 0** then (**-value**) is quest sort id: (in general profession or class quests. Also see [RequiredSkillPoints](#quest_template-RequiredSkillPoints) ) Value is ID from QuestSort.dbc

### QuestInfoID

These values are ID taken from [QuestInfo.dbc](QuestInfo)

| Value | Result       |
| ----- | ------------ |
| 0     | None         |
| 1     | Group        |
| 21    | Life         |
| 41    | PvP          |
| 62    | Raid         |
| 81    | Dungeon      |
| 82    | Event        |
| 83    | Legendary    |
| 84    | Escort       |
| 85    | Heroic       |
| 88    | Raid (10)    |
| 89    | Raid (25)    |

### SuggestedGroupNum

Recommended number of players to do the quest together.

### RewardFactionId1

Faction Id (from Faction.dbc) for which the quest give reputation points.
Number of gain or lost reputation points for Faction at quest completion. This is special reputation rewarding. Normal reputation reward to quest rewarding creature faction calculated and added automatically.

### RewardFactionId2

Faction Id (from Faction.dbc) for which the quest give reputation points.
Number of gain or lost reputation points for Faction at quest completion. This is special reputation rewarding. Normal reputation reward to quest rewarding creature faction calculated and added automatically.

### RewardFactionValueId1

This field is used for reputation lookup in QuestFactionReward.dbc if quest_template#RewardFactionValueId is 0. Value X in this field indicates RepX column of QuestFactionReward.dbc. If RewardRepValueId is positive, reputation from the first row of QuestFactionReward.dbc will be used, for negative values the second row is used.

### RewardFactionValueId2
This field is used for reputation lookup in QuestFactionReward.dbc if quest_template#RewardFactionValueId is 0. Value X in this field indicates RepX column of QuestFactionReward.dbc. If RewardRepValueId is positive, reputation from the first row of QuestFactionReward.dbc will be used, for negative values the second row is used.

### RewardNextQuest

** RewardNextQuest (Old field name: NextQuestIdChain)**

The quest entry from a **creature** or **gameobject** that ends a quest and starts a new one. The result is, that if you end the quest, the new quest instantly appears from the quest giver.

See the [examples section](#quest_template-Examples) for examples.

### RewardXPDifficulty

According to the [Level](#quest_template-Level), the basic experience with index *RewardXPDifficulty* is taken from QuestXP.dbc.

This field also controls the XP given as the XP is calculated from the value in this field by the following formula. If the quest is repeatable, XP will be given only once. The total XP that a character will receive is also affected by the level difference between the character's level and the quest's level.

The formula for calculating XP from the value in this field:
- **QuestLevel &gt;= 65:** XP = RewMoneyMaxLevel / 6.0
- **QuestLevel h1. 64:** XP = RewMoneyMaxLevel / 4.8
- **QuestLevel 63:** XP = RewMoneyMaxLevel / 3.6
- **QuestLevel h1. 62:** XP = RewMoneyMaxLevel / 2.4
- **QuestLevel 61:** XP = RewMoneyMaxLevel / 1.2
- **QuestLevel &lt;= 60:** XP = RewMoneyMaxLevel / 0.6

### RewardMoney

Money earned by completing the quest (if value &gt; 0) or money requirement to complete the quest (if value &lt; 0) .

### RewardMoneyDifficulty

ID refers to one of the money factor included in [MoneyFactor](quest_money_reward) ordered by level.

### RewardDisplaySpell

Spell that is shown to be casted on quest completion in the quest log. Note that this spell will NOT be casted if [RewardSpell](#quest_template-RewardSpell) is non-zero. The spell in the other field will be casted instead, in which case the spell here only serves as the visual in the quest log.

### RewardSpell

Spell that is shown to be casted on quest completion in the quest log. Note that this spell will NOT be casted if [RewardSpell](quest_template#rewardspell) is non-zero. The spell in the other field will be casted instead, in which case the spell here only serves as the visual in the quest log.

NOTE: This field comes straight from the WDB and should not be changed.

### RewardHonor

Number of honorable kill honor rewarded for completing this quest.

Example: An example value is 15 for quest 8388: At level 80 an honorable kill is 124 honor worth. Multiply this with 15 and you receive 1860, after the multiplication the value is rounded up. So the honor rewarded at level 80 is 1860 for this quest.

### RewardKillHonor


### StartItem

Items given by the quest giver at beginning of the quest. Items will be deleted when quest is abandoned.

### Flags

This flag field defines more specifically the type of quest it is. Aside from the daily flag and sharable flag, this field is used just for grouping purposes and NOT for any other quest requirements. The quest requirements are calculated from non-zero values in other quest template fields. Also, while some of these flags are known, others have yet an unknown purpose and the comments below is simply guesswork on them.

| Flag       | Name                                 | Comments                                                                                                                                                               |
| ---------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0          | QUEST_FLAGS_NONE                     | No flags, so no groups assigned to this quest.                                                                                                                         |
| 1          | QUEST_FLAGS_STAY_ALIVE               | If the player dies, the quest is failed.                                                                                                                               |
| 2          | QUEST_FLAGS_PARTY_ACCEPT             | Escort quests or any other event-driven quests. If player in party, all players that can accept this quest will receive confirmation box to accept quest.              |
| 4          | QUEST_FLAGS_EXPLORATION              | Involves the activation of an areatrigger.                                                                                                                             |
| 8          | QUEST_FLAGS_SHARABLE                 | Allows the quest to be shared with other players.                                                                                                                      |
| 16         | QUEST_FLAGS_HAS_CONDITION            | Not used currently                                                                                                                                                     |
| 32         | QUEST_FLAGS_HIDE_REWARD_POI          | Not used currently: Unsure of content                                                                                                                                  |
| 64         | QUEST_FLAGS_RAID                     | Can be completed while in raid                                                                                                                                         |
| 128        | QUEST_FLAGS_TBC                      | Not used currently: Available if TBC expansion enabled only                                                                                                            |
| 256        | QUEST_FLAGS_NO_MONEY_FROM_XP         | Not used currently: Experience is not converted to gold at max level                                                                                                   |
| 512        | QUEST_FLAGS_HIDDEN_REWARDS           | Item and monetary rewards are hidden in the initial quest details page and in the quest log but will appear once ready to be rewarded.                                 |
| 1024       | QUEST_FLAGS_TRACKING                 | These quests are automatically rewarded on quest complete and they will never appear in quest log client side.                                                         |
| 2048       | QUEST_FLAGS_DEPRECATE_REPUTATION     | Not used currently                                                                                                                                                     |
| 4096       | QUEST_FLAGS_DAILY                    | Daily repeatable quests (only flag that the core applies specific behavior for)                                                                                        |
| 8192       | QUEST_FLAGS_FLAGS_PVP                | Having this quest in log forces PvP flag                                                                                                                               |
| 16384      | QUEST_FLAGS_UNAVAILABLE              | Used on quests that are not generically available                                                                                                                      |
| 32768      | QUEST_FLAGS_WEEKLY                   | Weekly repeatable quests (only flag that the core applies specific behavior for)                                                                                       |
| 65536      | QUEST_FLAGS_AUTOCOMPLETE             | Auto complete                                                                                                                                                          |
| 131072     | QUEST_FLAGS_DISPLAY_ITEM_IN_TRACKER  | Displays usable item in quest tracker                                                                                                                                  |
| 262144     | QUEST_FLAGS_OBJ_TEXT                 | Use Objective text as Complete text                                                                                                                                    |
| 524288     | QUEST_FLAGS_AUTO_ACCEPT              | The client recognizes this flag as auto-accept. However, NONE of the current quests (3.3.5a) have this flag. Maybe blizz used to use it, or will use it in the future. |
| 1048576    | QUEST_FLAGS_PLAYER_CAST_ON_ACCEPT    | Quests with this flag player submit automatically by special button in player GUI                                                                                      |
| 2097152    | QUEST_FLAGS_PLAYER_CAST_ON_COMPLETE  | Automatically suggestion of accepting quest. Not from npc.                                                                                                             |
| 4194304    | QUEST_FLAGS_UPDATE_PHASE_SHIFT       |                                                                                                                                                                        |
| 8388608    | QUEST_FLAGS_SOR_WHITELIST            |                                                                                                                                                                        |
| 16777216   | QUEST_FLAGS_LAUNCH_GOSSIP_COMPLETE   |                                                                                                                                                                        |
| 54432      | QUEST_FLAGS_REMOVE_EXTRA_GET_ITEMS   |                                                                                                                                                                        |
| 67108864   | QUEST_FLAGS_HIDE_UNTIL_DISCOVERED    |                                                                                                                                                                        |
| 134217728  | QUEST_FLAGS_PORTRAIT_IN_QUEST_LOG    |                                                                                                                                                                        |
| 268435456  | QUEST_FLAGS_SHOW_ITEM_WHEN_COMPLETED |                                                                                                                                                                        |
| 536870912  | QUEST_FLAGS_LAUNCH_GOSSIP_ACCEPT     |                                                                                                                                                                        |
| 1073741824 | QUEST_FLAGS_ITEMS_GLOW_WHEN_DONE     |                                                                                                                                                                        |
| 2147483648 | QUEST_FLAGS_FAIL_ON_LOGOUT           |                                                                                                                                                                        |

Like all flag based fields, **QuestFlags** can be added for the different types of quest.

Note that some flags may not be supported by core.

### RequiredPlayerKills

Displays how much players you need to kill betd class=td class=a class=/td data-linked-resource-default-alias=fore completing the quest.

### RewardItem1

[item Id 1](item_template#entry) given for reward (no choice).

### RewardAmount1

Amount to be obtained from the above-mentioned item

### RewardItem2

[item Id 2](item_template#entry) given for reward (no choice).

### RewardAmount2

Amount to be obtained from the above-mentioned item

### RewardItem3

[item Id 3](item_template#entry) given for reward (no choice).

### RewardAmount3

Amount to be obtained from the above-mentioned item

### RewardItem4

[item Id 4](item_template#entry) given for reward (no choice).

### RewardAmount4

Amount to be obtained from the above-mentioned item

### ItemDrop1



### ItemDropQuantity1



### ItemDrop2



### ItemDropQuantity2



### ItemDrop3



### ItemDropQuantity3



### ItemDrop4



### ItemDropQuantity4



### RewardChoiceItemID1



### RewardChoiceItemQuantity1


### RewardChoiceItemID2


### RewardChoiceItemQuantity2


### RewardChoiceItemID3


### RewardChoiceItemQuantity3


### RewardChoiceItemID4


### RewardChoiceItemQuantity4


### RewardChoiceItemID5


### RewardChoiceItemQuantity5


### RewardChoiceItemID6


### RewardChoiceItemQuantity6


### POIContinent

MapId of a quest point of interest (POI - Point Of Interest). POI will be shown on the map when quest is active.

### POIx

X coordinate of quest POI.

### POIy

Y coordinate of quest POI.

### POIPriority

TODO

### RewardTitle


### RewardTalents


### RewardArenaPoints


### RewardFactionID1


### RewardFactionValue1


### RewardFactionOverride1


### RewardFactionID2


### RewardFactionValue2


### ItemDrop


### RewardFactionOverride2


### RewardFactionID3


### ItemDropQuantity

The maximum number of copies of the item in ItemDrop that can be picked up (and dropped by the core).

### RewardFactionValue3


### RewardFactionOverride3


### RewardFactionID4


### RewardFactionValue4


### RewardFactionOverride4


### RewardFactionID5


### RewardFactionValue5


### RewardFactionOverride5


### TimeAllowed


### AllowableRaces


### LogTitle

Title of the quest.

### LogDescription

Objectives of the quest. If empty, quest is an auto-complete quest that can be immediately finished without accepting it first.

### QuestDescription

The quest text. You can use certain placeholders that will be filled in in-game: $B - line break, $N - name, $R - race, $C - class, $Gmale:female; (male and female can be replace with any synonymn you want, but the order must stay the same. IE: boy:girl / man:woman / sir:madam / dude:chick)

### AreaDescription


### QuestCompletionLog

Text sent to player when the player tries to talk to the NPC with the quest active but incomplete. (The text under the "Progress" title in Wowhead.) You can use certain placeholders that will be filled in in-game: $B - line break, $N - name, $R - race, $C - class, $Gmale:female; (male and female can be replace with any synonymn you want, but the order must stay the same. IE: boy:girl / man:woman / sir:madam / dude:chick)

### RequiredNpcOrGo1
### RequiredNpcOrGo2
### RequiredNpcOrGo3
### RequiredNpcOrGo4

- Value &gt; 0:required creature\_template ID the player needs to kill/cast on in order to complete the quest.
- Value &lt; 0:required gameobject\_template ID the player needs to cast on in order to complete the quest.
- If\*RequiredSpellCast\*is != 0, the objective is to cast on target, else kill.

NOTE: If RequiredSpellCast is != 0 and the spell has effects Send Event or Quest Complete, this field may be left empty.

### RequiredNpcOrGoCount1
### RequiredNpcOrGoCount2
### RequiredNpcOrGoCount3
### RequiredNpcOrGoCount4

The number of times the creature or gameobject must be killed or casted upon.

### RequiredItemId1
### RequiredItemId2
### RequiredItemId3
### RequiredItemId4
### RequiredItemId5
### RequiredItemId6

[Id](item_template#entry) of required item to complete the quest.

### RequiredItemCount1
### RequiredItemCount2
### RequiredItemCount3
### RequiredItemCount4
### RequiredItemCount5
### RequiredItemCount6

Amount of required items

### Unknown0


### ObjectiveText1
### ObjectiveText2
### ObjectiveText3
### ObjectiveText4

Used to define non-standard objective texts, that show up in the questlog. Example, "Heal fallen warrior" and the number gets added by Count values.

### VerifiedBuild
