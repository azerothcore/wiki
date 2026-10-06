# quest\_template

[<-Back-to:World](database-world)

**Table: quest\_template**

Contains all basic definitions of available quests.

**Table: quest\_template's Structure**

| Field                                                   | Type     | Attributes | Key | Null | Default | Extra | Comment                                  |
| ------------------------------------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------------- |
| [ID](#id)                                               | INT      | UNSIGNED   | PRI | NO   | 0       |       |                                          |
| [QuestType](#questtype)                                 | TINYINT  | UNSIGNED   |     | NO   | 2       |       |                                          |
| [QuestLevel](#questlevel)                               | SMALLINT | SIGNED     |     | NO   | 1       |       |                                          |
| [MinLevel](#minlevel)                                   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [QuestSortID](#questsortid)                             | SMALLINT | SIGNED     |     | NO   | 0       |       |                                          |
| [QuestInfoID](#questinfoid)                             | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [SuggestedGroupNum](#suggestedgroupnum)                 | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredFactionId1](#requiredfactionid1)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredFactionId2](#requiredfactionid2)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredFactionValue1](#requiredfactionvalue1)         | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RequiredFactionValue2](#requiredfactionvalue2)         | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardNextQuest](#rewardnextquest)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardXPDifficulty](#rewardxpdifficulty)               | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardMoney](#rewardmoney)                             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardMoneyDifficulty](#rewardmoneydifficulty)         | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardDisplaySpell](#rewarddisplayspell)               | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardSpell](#rewardspell)                             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardHonor](#rewardhonor)                             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardKillHonor](#rewardkillhonor)                     | FLOAT    | SIGNED     |     | NO   | 0       |       |                                          |
| [StartItem](#startitem)                                 | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [Flags](#flags)                                         | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredPlayerKills](#requiredplayerkills)             | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardItem1](#rewarditem1)                             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardAmount1](#rewardamount1)                         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardItem2](#rewarditem2)                             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardAmount2](#rewardamount2)                         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardItem3](#rewarditem3)                             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardAmount3](#rewardamount3)                         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardItem4](#rewarditem4)                             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardAmount4](#rewardamount4)                         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDrop1](#itemdrop1)                                 | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDropQuantity1](#itemdropquantity1)                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDrop2](#itemdrop2)                                 | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDropQuantity2](#itemdropquantity2)                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDrop3](#itemdrop3)                                 | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDropQuantity3](#itemdropquantity3)                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDrop4](#itemdrop4)                                 | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ItemDropQuantity4](#itemdropquantity4)                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemID1](#rewardchoiceitemid1)             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemQuantity1](#rewardchoiceitemquantity1) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemID2](#rewardchoiceitemid2)             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemQuantity2](#rewardchoiceitemquantity2) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemID3](#rewardchoiceitemid3)             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemQuantity3](#rewardchoiceitemquantity3) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemID4](#rewardchoiceitemid4)             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemQuantity4](#rewardchoiceitemquantity4) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemID5](#rewardchoiceitemid5)             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemQuantity5](#rewardchoiceitemquantity5) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemID6](#rewardchoiceitemid6)             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardChoiceItemQuantity6](#rewardchoiceitemquantity6) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [POIContinent](#poicontinent)                           | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [POIx](#poix)                                           | FLOAT    | SIGNED     |     | NO   | 0       |       |                                          |
| [POIy](#poiy)                                           | FLOAT    | SIGNED     |     | NO   | 0       |       |                                          |
| [POIPriority](#poipriority)                             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardTitle](#rewardtitle)                             | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardTalents](#rewardtalents)                         | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardArenaPoints](#rewardarenapoints)                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RewardFactionID1](#rewardfactionid1)                   | SMALLINT | UNSIGNED   |     | NO   | 0       |       | faction id from Faction.dbc in this case |
| [RewardFactionValue1](#rewardfactionvalue1)             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionOverride1](#rewardfactionoverride1)       | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionID2](#rewardfactionid2)                   | SMALLINT | UNSIGNED   |     | NO   | 0       |       | faction id from Faction.dbc in this case |
| [RewardFactionValue2](#rewardfactionvalue2)             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionOverride2](#rewardfactionoverride2)       | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionID3](#rewardfactionid3)                   | SMALLINT | UNSIGNED   |     | NO   | 0       |       | faction id from Faction.dbc in this case |
| [RewardFactionValue3](#rewardfactionvalue3)             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionOverride3](#rewardfactionoverride3)       | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionID4](#rewardfactionid4)                   | SMALLINT | UNSIGNED   |     | NO   | 0       |       | faction id from Faction.dbc in this case |
| [RewardFactionValue4](#rewardfactionvalue4)             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionOverride4](#rewardfactionoverride4)       | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionID5](#rewardfactionid5)                   | SMALLINT | UNSIGNED   |     | NO   | 0       |       | faction id from Faction.dbc in this case |
| [RewardFactionValue5](#rewardfactionvalue5)             | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RewardFactionOverride5](#rewardfactionoverride5)       | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [TimeAllowed](#timeallowed)                             | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [AllowableRaces](#allowableraces)                       | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [LogTitle](#logtitle)                                   | TEXT     |            |     | YES  | NULL    |       |                                          |
| [LogDescription](#logdescription)                       | TEXT     |            |     | YES  | NULL    |       |                                          |
| [QuestDescription](#questdescription)                   | TEXT     |            |     | YES  | NULL    |       |                                          |
| [AreaDescription](#areadescription)                     | TEXT     |            |     | YES  | NULL    |       |                                          |
| [QuestCompletionLog](#questcompletionlog)               | TEXT     |            |     | YES  | NULL    |       |                                          |
| [RequiredNpcOrGo1](#requirednpcorgo1)                   | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGo2](#requirednpcorgo2)                   | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGo3](#requirednpcorgo3)                   | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGo4](#requirednpcorgo4)                   | INT      | SIGNED     |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGoCount1](#requirednpcorgocount1)         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGoCount2](#requirednpcorgocount2)         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGoCount3](#requirednpcorgocount3)         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredNpcOrGoCount4](#requirednpcorgocount4)         | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemId1](#requireditemid1)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemId2](#requireditemid2)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemId3](#requireditemid3)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemId4](#requireditemid4)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemId5](#requireditemid5)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemId6](#requireditemid6)                     | INT      | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemCount1](#requireditemcount1)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemCount2](#requireditemcount2)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemCount3](#requireditemcount3)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemCount4](#requireditemcount4)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemCount5](#requireditemcount5)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [RequiredItemCount6](#requireditemcount6)               | SMALLINT | UNSIGNED   |     | NO   | 0       |       |                                          |
| [Unknown0](#unknown0)                                   | TINYINT  | UNSIGNED   |     | NO   | 0       |       |                                          |
| [ObjectiveText1](#objectivetext1)                       | TEXT     |            |     | YES  | NULL    |       |                                          |
| [ObjectiveText2](#objectivetext2)                       | TEXT     |            |     | YES  | NULL    |       |                                          |
| [ObjectiveText3](#objectivetext3)                       | TEXT     |            |     | YES  | NULL    |       |                                          |
| [ObjectiveText4](#objectivetext4)                       | TEXT     |            |     | YES  | NULL    |       |                                          |
| [VerifiedBuild](#verifiedbuild)                         | INT      | SIGNED     |     | YES  | NULL    |       |                                          |

**Description of the table's fields**

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

Level of the quest. It sets the quest's color in the quest log and the experience it rewards, see [RewardXPDifficulty](#rewardxpdifficulty). If set to -1, the player's level is used as the quest level.

### MinLevel

Minimum level at which a player can get the quest.

### QuestSortID

This field defines under what category the quest falls in the quest log.

If **value &gt; 0** then value is Zone IDs taken from AreaTable.dbc.

If **value &lt; 0** then (**-value**) is an ID from QuestSort.dbc, in general profession, class or holiday quests. Also see [RequiredSkillPoints](quest_template_addon#requiredskillpoints).

### QuestInfoID

These values are ID taken from [QuestInfo.dbc](https://wowdev.wiki/DB/QuestInfo)

| Value | Result    |
| ----- | --------- |
| 0     | None      |
| 1     | Group     |
| 21    | Life      |
| 41    | PvP       |
| 62    | Raid      |
| 81    | Dungeon   |
| 82    | Event     |
| 83    | Legendary |
| 84    | Escort    |
| 85    | Heroic    |
| 88    | Raid (10) |
| 89    | Raid (25) |

A quest can only be completed inside a raid group if it is a Raid, Raid (10) or Raid (25) quest, unless `Quests.IgnoreRaid` is enabled in `worldserver.conf`.

### SuggestedGroupNum

Recommended number of players to do the quest together.

### RequiredFactionId1

Faction ID from Faction.dbc for a reputation objective. The quest is complete once the player's reputation with this faction reaches [RequiredFactionValue1](#requiredfactionvalue1). The faction and value are shown in the quest log.

### RequiredFactionId2

Faction ID from Faction.dbc for a second reputation objective, used for the opposing faction. The quest is complete once the player's reputation with this faction reaches [RequiredFactionValue2](#requiredfactionvalue2).

Unlike the first objective, the player can only accept the quest while their reputation with this faction is below the value.

### RequiredFactionValue1

The reputation value the player needs with [RequiredFactionId1](#requiredfactionid1). Has no effect if RequiredFactionId1 is 0.

### RequiredFactionValue2

The reputation value the player needs with [RequiredFactionId2](#requiredfactionid2). Has no effect if RequiredFactionId2 is 0.

### RewardNextQuest

The [ID](#id) of a quest that the same creature or gameobject offers right after this quest is turned in. When the player completes this quest, the next quest opens immediately without the player having to talk to the quest giver again.

### RewardXPDifficulty

Index (0-9) of the experience column in QuestXP.dbc. The base experience is read from the row of the [QuestLevel](#questlevel) and this column.

The experience is then reduced by the difference between the player's level and the quest level:

| Player level              | Experience |
| ------------------------- | ---------- |
| QuestLevel + 5 or lower   | 100%       |
| QuestLevel + 6            | 80%        |
| QuestLevel + 7            | 60%        |
| QuestLevel + 8            | 40%        |
| QuestLevel + 9            | 20%        |
| QuestLevel + 10 or higher | 10%        |

A repeatable quest only gives experience the first time, unless it is a daily, weekly, monthly or Dungeon Finder quest. At the maximum level, the experience is converted to money instead, 6 copper per experience point, unless the quest has the `QUEST_FLAGS_NO_MONEY_FROM_XP` flag.

### RewardMoney

Money earned by completing the quest (if value &gt; 0) or money requirement to complete the quest (if value &lt; 0).

### RewardMoneyDifficulty

ID refers to one of the money factor included in [quest\_money\_reward](quest_money_reward) ordered by level. If set, the money reward is taken from there based on the player's level instead of from [RewardMoney](#rewardmoney).

### RewardDisplaySpell

Spell that is shown to be cast on quest completion in the quest log. Note that this spell will NOT be cast if [RewardSpell](#rewardspell) is non-zero. The spell in the other field will be cast instead, in which case the spell here only serves as the visual in the quest log.

### RewardSpell

Spell cast on the player when the quest is rewarded. If set, it is cast instead of [RewardDisplaySpell](#rewarddisplayspell).

The quest giver casts the spell on the player, unless the spell teaches a spell, creates an item or can only be self cast. Then the player casts it on themself.

### RewardHonor

A fixed amount of honor rewarded for completing this quest. It is added on top of the honor from [RewardKillHonor](#rewardkillhonor).

### RewardKillHonor

Honor rewarded for completing this quest, counted in honorable kills. The honor of one honorable kill depends on the player's level, so the reward grows with the player's level.

### StartItem

Item given by the quest giver at the beginning of the quest. The item will be deleted when the quest is abandoned. The number of items is set in [ProvidedItemCount](quest_template_addon#provideditemcount).

### Flags

This flag field defines more specifically the type of quest it is. The quest requirements are calculated from non-zero values in other quest template fields.

| Flag   | Name                                | Comments                                                                                                                                              |
| ------ | ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0      | QUEST_FLAGS_NONE                    | No flags.                                                                                                                                             |
| 1      | QUEST_FLAGS_STAY_ALIVE              | If the player dies, the quest is failed.                                                                                                              |
| 2      | QUEST_FLAGS_PARTY_ACCEPT            | Escort quests or any other event-driven quests. If player in party, all players that can accept this quest will receive confirmation box to accept quest. |
| 4      | QUEST_FLAGS_EXPLORATION             | Involves the activation of an areatrigger.                                                                                                            |
| 8      | QUEST_FLAGS_SHARABLE                | Allows the quest to be shared with other players.                                                                                                     |
| 16     | QUEST_FLAGS_HAS_CONDITION           | Not used currently.                                                                                                                                   |
| 32     | QUEST_FLAGS_HIDE_REWARD_POI         | Not used currently.                                                                                                                                   |
| 64     | QUEST_FLAGS_RAID                    | Not used by the core. Use [QuestInfoID](#questinfoid) to make a raid quest.                                                                            |
| 128    | QUEST_FLAGS_TBC                     | Not used currently: Available if TBC expansion enabled only.                                                                                          |
| 256    | QUEST_FLAGS_NO_MONEY_FROM_XP        | Experience is not converted to money at the maximum level.                                                                                            |
| 512    | QUEST_FLAGS_HIDDEN_REWARDS          | Item and monetary rewards are hidden in the initial quest details page and in the quest log but will appear once ready to be rewarded.                |
| 1024   | QUEST_FLAGS_TRACKING                | These quests are automatically rewarded on quest complete and they will never appear in quest log client side.                                        |
| 2048   | QUEST_FLAGS_DEPRECATE_REPUTATION    | Not used currently.                                                                                                                                   |
| 4096   | QUEST_FLAGS_DAILY                   | Daily repeatable quest.                                                                                                                               |
| 8192   | QUEST_FLAGS_FLAGS_PVP               | Having this quest in log forces PvP flag.                                                                                                             |
| 16384  | QUEST_FLAGS_UNAVAILABLE             | Used on quests that are not generically available.                                                                                                    |
| 32768  | QUEST_FLAGS_WEEKLY                  | Weekly repeatable quest.                                                                                                                              |
| 65536  | QUEST_FLAGS_AUTOCOMPLETE            | Auto complete.                                                                                                                                        |
| 131072 | QUEST_FLAGS_DISPLAY_ITEM_IN_TRACKER | Displays usable item in quest tracker.                                                                                                                |
| 262144 | QUEST_FLAGS_OBJ_TEXT                | Use Objective text as Complete text.                                                                                                                  |
| 524288 | QUEST_FLAGS_AUTO_ACCEPT             | The client recognizes this flag as auto-accept. However, NONE of the current quests (3.3.5a) have this flag.                                          |

Like all flag based fields, **Flags** can be added for the different types of quest. Higher flags were added in later expansions and are not used in 3.3.5a.

Note that some flags may not be supported by core.

### RequiredPlayerKills

Number of enemy players the player needs to kill to complete the quest.

### RewardItem1

[Item ID](item_template#entry) given as a reward. All RewardItem items are given, the player does not choose between them.

### RewardAmount1

Number of [RewardItem1](#rewarditem1) items given.

### RewardItem2

See [RewardItem1](#rewarditem1).

### RewardAmount2

Number of [RewardItem2](#rewarditem2) items given.

### RewardItem3

See [RewardItem1](#rewarditem1).

### RewardAmount3

Number of [RewardItem3](#rewarditem3) items given.

### RewardItem4

See [RewardItem1](#rewarditem1).

### RewardAmount4

Number of [RewardItem4](#rewarditem4) items given.

### ItemDrop1

[Item ID](item_template#entry) of an item the player needs while on the quest, but that is not a quest objective, for example an item that has to be used on a target. Creatures and gameobjects only drop the item while the player has fewer than the needed amount.

When the quest is completed or abandoned, the core removes these items from the player if they are quest items.

### ItemDropQuantity1

The maximum number of [ItemDrop1](#itemdrop1) items the player can pick up, and the number the core removes when the quest ends. If 0, the item's stack size is used as the maximum.

### ItemDrop2

See [ItemDrop1](#itemdrop1).

### ItemDropQuantity2

See [ItemDropQuantity1](#itemdropquantity1).

### ItemDrop3

See [ItemDrop1](#itemdrop1).

### ItemDropQuantity3

See [ItemDropQuantity1](#itemdropquantity1).

### ItemDrop4

See [ItemDrop1](#itemdrop1).

### ItemDropQuantity4

See [ItemDropQuantity1](#itemdropquantity1).

### RewardChoiceItemID1

[Item ID](item_template#entry) of an item the player can choose as a reward. The player picks one of the RewardChoiceItemID items.

### RewardChoiceItemQuantity1

Number of [RewardChoiceItemID1](#rewardchoiceitemid1) items given if the player chooses it.

### RewardChoiceItemID2

See [RewardChoiceItemID1](#rewardchoiceitemid1).

### RewardChoiceItemQuantity2

Number of [RewardChoiceItemID2](#rewardchoiceitemid2) items given if the player chooses it.

### RewardChoiceItemID3

See [RewardChoiceItemID1](#rewardchoiceitemid1).

### RewardChoiceItemQuantity3

Number of [RewardChoiceItemID3](#rewardchoiceitemid3) items given if the player chooses it.

### RewardChoiceItemID4

See [RewardChoiceItemID1](#rewardchoiceitemid1).

### RewardChoiceItemQuantity4

Number of [RewardChoiceItemID4](#rewardchoiceitemid4) items given if the player chooses it.

### RewardChoiceItemID5

See [RewardChoiceItemID1](#rewardchoiceitemid1).

### RewardChoiceItemQuantity5

Number of [RewardChoiceItemID5](#rewardchoiceitemid5) items given if the player chooses it.

### RewardChoiceItemID6

See [RewardChoiceItemID1](#rewardchoiceitemid1).

### RewardChoiceItemQuantity6

Number of [RewardChoiceItemID6](#rewardchoiceitemid6) items given if the player chooses it.

### POIContinent

MapId of a quest point of interest (POI - Point Of Interest). POI will be shown on the map when quest is active.

### POIx

X coordinate of quest POI.

### POIy

Y coordinate of quest POI.

### POIPriority

Sent to the client together with the POI. Its exact effect in the client is not known.

### RewardTitle

ID from CharTitles.dbc of a title the player gets when the quest is rewarded.

### RewardTalents

Number of extra talent points the player gets when the quest is rewarded.

### RewardArenaPoints

Number of arena points the player gets when the quest is rewarded.

### RewardFactionID1

Faction ID from Faction.dbc that the player gets reputation with when the quest is rewarded.

This is on top of the reputation the player gets for turning the quest in to a creature of a faction.

### RewardFactionValue1

Sets the amount of reputation for [RewardFactionID1](#rewardfactionid1) by looking it up in QuestFactionReward.dbc. The value is the column (1-9) to use. A positive value uses the first row, which gives reputation. A negative value uses the second row, which removes reputation.

Only used if [RewardFactionOverride1](#rewardfactionoverride1) is 0.

### RewardFactionOverride1

The amount of reputation for [RewardFactionID1](#rewardfactionid1), multiplied by 100. For example, 25000 gives 250 reputation and -2500 removes 25 reputation. If set, [RewardFactionValue1](#rewardfactionvalue1) is ignored.

### RewardFactionID2

See [RewardFactionID1](#rewardfactionid1).

### RewardFactionValue2

See [RewardFactionValue1](#rewardfactionvalue1).

### RewardFactionOverride2

See [RewardFactionOverride1](#rewardfactionoverride1).

### RewardFactionID3

See [RewardFactionID1](#rewardfactionid1).

### RewardFactionValue3

See [RewardFactionValue1](#rewardfactionvalue1).

### RewardFactionOverride3

See [RewardFactionOverride1](#rewardfactionoverride1).

### RewardFactionID4

See [RewardFactionID1](#rewardfactionid1).

### RewardFactionValue4

See [RewardFactionValue1](#rewardfactionvalue1).

### RewardFactionOverride4

See [RewardFactionOverride1](#rewardfactionoverride1).

### RewardFactionID5

See [RewardFactionID1](#rewardfactionid1).

### RewardFactionValue5

See [RewardFactionValue1](#rewardfactionvalue1).

### RewardFactionOverride5

See [RewardFactionOverride1](#rewardfactionoverride1).

### TimeAllowed

Time in seconds the player has to complete the quest. If the time runs out, the quest fails. 0 means no time limit.

### AllowableRaces

Bitmask of the races that can take the quest. 0 means all races.

| Value | Race      |
| ----- | --------- |
| 1     | Human     |
| 2     | Orc       |
| 4     | Dwarf     |
| 8     | Night Elf |
| 16    | Undead    |
| 32    | Tauren    |
| 64    | Gnome     |
| 128   | Troll     |
| 512   | Blood Elf |
| 1024  | Draenei   |

Add the values together to allow several races. For example, 1101 allows all Alliance races and 690 allows all Horde races.

### LogTitle

Title of the quest.

### LogDescription

Objectives of the quest. If empty, quest is an auto-complete quest that can be immediately finished without accepting it first.

### QuestDescription

The quest text. You can use certain placeholders that will be filled in in-game: $B - line break, $N - name, $R - race, $C - class, $Gmale:female; (male and female can be replaced with any synonym you want, but the order must stay the same. IE: boy:girl / man:woman / sir:madam)

### AreaDescription

An extra objective line shown in the quest log for objectives that are not kills or items, such as exploring an area or escorting a creature. For example, "Scout through the Fargodeep Mine".

These objectives are completed by an areatrigger, a spell or a script, see the `QUEST_SPECIAL_FLAGS_EXPLORATION_OR_EVENT` flag in [quest\_template\_addon.SpecialFlags](quest_template_addon#specialflags).

### QuestCompletionLog

Text shown in the quest log when all objectives are done, for example "Return to Marshal McBride in Northshire Abbey." You can use the same placeholders as in [QuestDescription](#questdescription).

### RequiredNpcOrGo1

- Value &gt; 0: required [creature\_template](creature_template) ID the player needs to kill or cast on in order to complete the quest.
- Value &lt; 0: required [gameobject\_template](gameobject_template) ID the player needs to cast on in order to complete the quest.
- If the quest has the `QUEST_SPECIAL_FLAGS_CAST` flag in [quest\_template\_addon.SpecialFlags](quest_template_addon#specialflags), the objective is to cast a spell on the target instead of killing it.

### RequiredNpcOrGo2

See [RequiredNpcOrGo1](#requirednpcorgo1).

### RequiredNpcOrGo3

See [RequiredNpcOrGo1](#requirednpcorgo1).

### RequiredNpcOrGo4

See [RequiredNpcOrGo1](#requirednpcorgo1).

### RequiredNpcOrGoCount1

The number of times the creature or gameobject in [RequiredNpcOrGo1](#requirednpcorgo1) must be killed or cast upon.

### RequiredNpcOrGoCount2

See [RequiredNpcOrGoCount1](#requirednpcorgocount1).

### RequiredNpcOrGoCount3

See [RequiredNpcOrGoCount1](#requirednpcorgocount1).

### RequiredNpcOrGoCount4

See [RequiredNpcOrGoCount1](#requirednpcorgocount1).

### RequiredItemId1

[Item ID](item_template#entry) of an item the player needs to complete the quest.

### RequiredItemId2

See [RequiredItemId1](#requireditemid1).

### RequiredItemId3

See [RequiredItemId1](#requireditemid1).

### RequiredItemId4

See [RequiredItemId1](#requireditemid1).

### RequiredItemId5

See [RequiredItemId1](#requireditemid1).

### RequiredItemId6

See [RequiredItemId1](#requireditemid1).

### RequiredItemCount1

Number of [RequiredItemId1](#requireditemid1) items the player needs.

### RequiredItemCount2

See [RequiredItemCount1](#requireditemcount1).

### RequiredItemCount3

See [RequiredItemCount1](#requireditemcount1).

### RequiredItemCount4

See [RequiredItemCount1](#requireditemcount1).

### RequiredItemCount5

See [RequiredItemCount1](#requireditemcount1).

### RequiredItemCount6

See [RequiredItemCount1](#requireditemcount1).

### Unknown0

Not used by the core.

### ObjectiveText1

Used to define non-standard objective texts that show up in the quest log, for example "Heal fallen warrior". The count from [RequiredNpcOrGoCount1](#requirednpcorgocount1) is added after the text.

### ObjectiveText2

See [ObjectiveText1](#objectivetext1).

### ObjectiveText3

See [ObjectiveText1](#objectivetext1).

### ObjectiveText4

See [ObjectiveText1](#objectivetext1).

### VerifiedBuild

This field is used by the TrinityDB Team to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
