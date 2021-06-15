# quest\_template

[<-Back-to:World](database-world.md)

**Table: quest\_template**

Contains all basic definitions of available quests.

## **Structure**

| Field                           | Type         | Attribute | Key | Null | Default | Extra | Comment |
|---------------------------------|--------------|-----------|-----|------|---------|-------|---------|
| [ID][1]                         | mediumint(8) | unsigned  | PRI | NO   | 0       |       |         |
| [QuestType][2]                  | tinyint(3)   | unsigned  |     | NO   | 2       |       |         |
| [QuestLevel][3]                 | smallint(6)  |           |     | NO   | 1       |       |         |
| [MinLevel][4]                   | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [QuestSortID][5]                | smallint(6)  |           |     | NO   | 0       |       |         |
| [QuestInfoID][6]                | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [SuggestedGroupNum][7]          | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RequiredFactionId1][8]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredFactionId2][9]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredFactionValue1][10]     | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredFactionValue2][11]     | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardNextQuest][12]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardXPDifficulty][13]        | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardMoney][14]               | int(11)      |           |     | NO   | 0       |       |         |
| [RewardBonusMoney][15]          | int(10)      | unsigned  |     | NO   | 0       |       |         |
| [RewardDisplaySpell][16]        | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardSpell][17]               | int(11)      |           |     | NO   | 0       |       |         |
| [RewardHonor][18]               | int(11)      |           |     | NO   | 0       |       |         |
| [RewardKillHonor][19]           | float        |           |     | NO   | 0       |       |         |
| [StartItem][20]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [Flags][21]                     | int(10)      | unsigned  |     | NO   | 0       |       |         |
| [RequiredPlayerKills][22]       | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardItem1][23]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount1][24]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardItem2][25]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount2][26]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardItem3][27]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount3][28]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardItem4][29]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardAmount4][30]             | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop1][31]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity1][32]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop2][33]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity2][34]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop3][35]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity3][36]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [ItemDrop4][37]                 | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [ItemDropQuantity4][38]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID1][39]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity1][40] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID2][41]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity2][42] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID3][43]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity3][44] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID4][45]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity4][46] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID5][47]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity5][48] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemID6][49]       | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardChoiceItemQuantity6][50] | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [POIContinent][51]              | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [POIx][52]                      | float        |           |     | NO   | 0       |       |         |
| [POIy][53]                      | float        |           |     | NO   | 0       |       |         |
| [POIPriority][54]               | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RewardTitle][55]               | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardTalents][56]             | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [RewardArenaPoints][57]         | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionID1][58]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue1][59]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride1][60]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID2][61]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue2][62]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride2][63]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID3][64]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue3][65]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride3][66]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID4][67]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue4][68]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride4][69]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionID5][70]          | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RewardFactionValue5][71]       | mediumint(9) |           |     | NO   | 0       |       |         |
| [RewardFactionOverride5][72]    | mediumint(9) |           |     | NO   | 0       |       |         |
| [TimeAllowed][73]               | int(10)      | unsigned  |     | NO   | 0       |       |         |
| [AllowableRaces][74]            | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [LogTitle][75]                  | text         |           |     | YES  |         |       |         |
| [LogDescription][76]            | text         |           |     | YES  |         |       |         |
| [QuestDescription][77]          | text         |           |     | YES  |         |       |         |
| [AreaDescription][78]           | text         |           |     | YES  |         |       |         |
| [QuestCompletionLog][79]        | text         |           |     | YES  |         |       |         |
| [RequiredNpcOrGo1][80]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo2][81]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo3][82]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGo4][83]          | mediumint(9) |           |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount1][84]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount2][85]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount3][86]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredNpcOrGoCount4][87]     | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId1][88]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId2][89]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId3][90]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId4][91]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId5][92]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemId6][93]           | mediumint(8) | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount1][94]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount2][95]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount3][96]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount4][97]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount5][98]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [RequiredItemCount6][99]        | smallint(5)  | unsigned  |     | NO   | 0       |       |         |
| [Unknown0][100]                 | tinyint(3)   | unsigned  |     | NO   | 0       |       |         |
| [ObjectiveText1][101]           | text         |           |     | YES  |         |       |         |
| [ObjectiveText2][102]           | text         |           |     | YES  |         |       |         |
| [ObjectiveText3][103]           | text         |           |     | YES  |         |       |         |
| [ObjectiveText4][104]           | text         |           |     | YES  |         |       |         |
| [VerifiedBuild][105]            | smallint(6)  |           |     | YES  | 0       |       |         |

[1]: #ID
[2]: #QuestType
[3]: #QuestLevel
[4]: #MinLevel
[5]: #QuestSortID
[6]: #QuestInfoID
[7]: #SuggestedGroupNum
[8]: #RequiredFactionId1
[9]: #RequiredFactionId2
[10]: #RequiredFactionValue1
[11]: #RequiredFactionValue2
[12]: #RewardNextQuest
[13]: #RewardXPDifficulty
[14]: #RewardMoney
[15]: #RewardBonusMoney
[16]: #RewardDisplaySpell
[17]: #RewardSpell
[18]: #RewardHonor
[19]: #RewardKillHonor
[20]: #StartItem
[21]: #Flags
[22]: #RequiredPlayerKills
[23]: #RewardItem1
[24]: #RewardAmount1
[25]: #RewardItem2
[26]: #RewardAmount2
[27]: #RewardItem3
[28]: #RewardAmount3
[29]: #RewardItem4
[30]: #RewardAmount4
[31]: #ItemDrop1
[32]: #ItemDropQuantity1
[33]: #ItemDrop2
[34]: #ItemDropQuantity2
[35]: #ItemDrop3
[36]: #ItemDropQuantity3
[37]: #ItemDrop4
[38]: #ItemDropQuantity4
[39]: #RewardChoiceItemID1
[40]: #RewardChoiceItemQuantity1
[41]: #RewardChoiceItemID2
[42]: #RewardChoiceItemQuantity2
[43]: #RewardChoiceItemID3
[44]: #RewardChoiceItemQuantity3
[45]: #RewardChoiceItemID4
[46]: #RewardChoiceItemQuantity4
[47]: #RewardChoiceItemID5
[48]: #RewardChoiceItemQuantity5
[49]: #RewardChoiceItemID6
[50]: #RewardChoiceItemQuantity6
[51]: #POIContinent
[52]: #POIx
[53]: #POIy
[54]: #POIPriority
[55]: #RewardTitle
[56]: #RewardTalents
[57]: #RewardArenaPoints
[58]: #RewardFactionID1
[59]: #RewardFactionValue1
[60]: #RewardFactionOverride1
[61]: #RewardFactionID2
[62]: #RewardFactionValue2
[63]: #RewardFactionOverride2
[64]: #RewardFactionID3
[65]: #RewardFactionValue3
[66]: #RewardFactionOverride3
[67]: #RewardFactionID4
[68]: #RewardFactionValue4
[69]: #RewardFactionOverride4
[70]: #RewardFactionID5
[71]: #RewardFactionValue5
[72]: #RewardFactionOverride5
[73]: #TimeAllowed
[74]: #AllowableRaces
[75]: #LogTitle
[76]: #LogDescription
[77]: #QuestDescription
[78]: #AreaDescription
[79]: #QuestCompletionLog
[80]: #RequiredNpcOrGo1
[81]: #RequiredNpcOrGo2
[82]: #RequiredNpcOrGo3
[83]: #RequiredNpcOrGo4
[84]: #RequiredNpcOrGoCount1
[85]: #RequiredNpcOrGoCount2
[86]: #RequiredNpcOrGoCount3
[87]: #RequiredNpcOrGoCount4
[88]: #RequiredItemId1
[89]: #RequiredItemId2
[90]: #RequiredItemId3
[91]: #RequiredItemId4
[92]: #RequiredItemId5
[93]: #RequiredItemId6
[94]: #RequiredItemCount1
[95]: #RequiredItemCount2
[96]: #RequiredItemCount3
[97]: #RequiredItemCount4
[98]: #RequiredItemCount5
[99]: #RequiredItemCount6
[100]: #Unknown0
[101]: #ObjectiveText1
[102]: #ObjectiveText2
[103]: #ObjectiveText3
[104]: #ObjectiveText4
[105]: #VerifiedBuild

**Description of the fields**

### ID

The quest ID. This column is the Primary Key for the Table. Each quest ID must be unique!

### QuestType

Accepted values: 0, 1, 2 or 3. Their meaning is described in table below.

| Value | Result                                                                                                   |
|-------|----------------------------------------------------------------------------------------------------------|
| 0     | Quest is enabled, but it is auto-completed when accepted; this skips quest objectives and quest details. |
| 1     | Quest is disabled (not yet implemented in the core).                                                     |
| 2     | Quest is enabled (does not auto-complete).                                                               |
| 3     | Quest is a World Quest.                                                                                  |

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

### SuggestedGroupNum

Recommended number of players to do the quest together.

### RequiredFactionId1

Faction ID 1 for an objective to achieve a certain reputation value with. See Faction.dbc

### RequiredFactionId2

Faction ID 2 for an objective to achieve a certain reputation value with. See Faction.dbc

### RequiredFactionValue1

Reputation value 1 that the player must achieve with the faction in [RepObjectiveFaction](#quest_template-RepObjectiveFaction) as part of the quest objectives.

### RequiredFactionValue2

Reputation value 2 that the player must achieve with the faction in [RepObjectiveFaction](#quest_template-RepObjectiveFaction) as part of the quest objectives.

### RewardNextQuest

**(Old field name: NextQuestIdChain)**

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

### RewardBonusMoney

The money a character at level 80 would get when they complete this quest.

### RewardDisplaySpell



### RewardSpell

Spell that is shown to be casted on quest completion in the quest log. Note that this spell will NOT be casted if [RewardSpellCast](#quest_template-RewardSpellCast) is non-zero. The spell in the other field will be casted instead, in which case the spell here only serves as the visual in the quest log.

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
|------------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
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


### POIx


### POIy


### POIPriority


### RewardTitle


### RewardTalents


### RewardArenaPoints


### RewardFactionID1


### RewardFactionValue1


### RewardFactionOverride1


### RewardFactionID2


### RewardFactionValue2


### RewardFactionOverride2


### RewardFactionID3


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

[Id](item_template#id) of required item to complete the quest.

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
