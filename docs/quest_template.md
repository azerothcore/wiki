# quest\_template

[<-Back-to:World](database-world.md)

**Table: quest\_template**

Contains all basic definitions of available quests.

## **Structure**

| Field                              | Type                 | Null | Key | Default | Extra | Comment |
|------------------------------------|----------------------|------|-----|---------|-------|---------|
| ID                                 | INT UNSIGNED     | NO   | PRI | 0       |       |         |
| QuestType                          | TINYINT UNSIGNED  | NO   |     | 2       |       |         |
| QuestLevel                         | INT              | NO   |     | -1      |       |         |
| QuestPackageID                     | INT UNSIGNED     | NO   |     | 0       |       |         |
| MinLevel                           | INT              | NO   |     | 0       |       |         |
| QuestSortID                        | SMALLINT          | NO   |     | 0       |       |         |
| QuestInfoID                        | SMALLINT UNSIGNED | NO   |     | 0       |       |         |
| SuggestedGroupNum                  | TINYINT UNSIGNED  | NO   |     | 0       |       |         |
| RewardNextQuest                    | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardXPDifficulty                 | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardXPMultiplier                 | FLOAT                | NO   |     | 1       |       |         |
| RewardMoney                        | INT              | NO   |     | 0       |       |         |
| RewardMoneyDifficulty              | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardMoneyMultiplier              | FLOAT                | NO   |     | 1       |       |         |
| RewardBonusMoney                   | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardDisplaySpell(X=1...3)        | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardSpell                        | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardHonor                        | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardKillHonor                    | INT UNSIGNED     | NO   |     | 0       |       |         |
| StartItem                          | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardArtifactXPDifficulty         | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardArtifactXPMultiplier         | FLOAT                | NO   |     | 1       |       |         |
| RewardArtifactCategoryID           | INT UNSIGNED     | NO   |     | 0       |       |         |
| Flags                              | INT UNSIGNED     | NO   |     | 0       |       |         |
| FlagsEx                            | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardItem(X=1...4)                | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardAmount(X=1...4)              | INT UNSIGNED     | NO   |     | 0       |       |         |
| ItemDrop(X=1...4)                  | INT UNSIGNED     | NO   |     | 0       |       |         |
| ItemDropQuantity(X=1...4)          | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardChoiceItemID(X=1...6)        | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardChoiceItemQuantity(X=1...6)  | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardChoiceItemDisplayID(X=1...6) | INT UNSIGNED     | NO   |     | 0       |       |         |
| POIContinent                       | INT UNSIGNED     | NO   |     | 0       |       |         |
| POIx                               | FLOAT                | NO   |     | 0       |       |         |
| POIy                               | FLOAT                | NO   |     | 0       |       |         |
| POIPriority                        | INT              | NO   |     | 0       |       |         |
| RewardTitle                        | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardArenaPoints                  | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardSkillLineID                  | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardNumSkillUps                  | INT UNSIGNED     | NO   |     | 0       |       |         |
| PortraitGiver                      | INT UNSIGNED     | NO   |     | 0       |       |         |
| PortraitTurnIn                     | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardFactionID(X=1...5)           | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardFactionValue(X=1...5)        | INT              | NO   |     | 0       |       |         |
| RewardFactionOverride(X=1...5)     | INT              | NO   |     | 0       |       |         |
| RewardFactionCapIn(X=1...5)        | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardFactionFlags                 | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardCurrencyID(X=1...4)          | INT UNSIGNED     | NO   |     | 0       |       |         |
| RewardCurrencyQty(X=1...4)         | INT UNSIGNED     | NO   |     | 0       |       |         |
| AcceptedSoundKitID                 | INT UNSIGNED     | NO   |     | 0       |       |         |
| CompleteSoundKitID                 | INT UNSIGNED     | NO   |     | 0       |       |         |
| AreaGroupID                        | INT UNSIGNED     | NO   |     | 0       |       |         |
| TimeAllowed                        | INT UNSIGNED     | NO   |     | 0       |       |         |
| AllowableRaces                     | INT              | NO   |     | -1      |       |         |
| QuestRewardID                      | INT UNSIGNED     | NO   |     | 0       |       |         |
| LogTitle                           | text                 | YES  |     | (NULL)  |       |         |
| LogDescription                     | text                 | YES  |     | (NULL)  |       |         |
| QuestDescription                   | text                 | YES  |     | (NULL)  |       |         |
| AreaDescription                    | text                 | YES  |     | (NULL)  |       |         |
| PortraitGiverText                  | text                 | YES  |     | (NULL)  |       |         |
| PortraitGiverName                  | text                 | YES  |     | (NULL)  |       |         |
| PortraitTurnInText                 | text                 | YES  |     | (NULL)  |       |         |
| PortraitTurnInName                 | text                 | YES  |     | (NULL)  |       |         |
| QuestCompletionLog                 | text                 | YES  |     | (NULL)  |       |         |
| VerifiedBuild                      | SMALLINT          | YES  |     | 0       |       |         |

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

### LimitTime

Time in seconds that the player has to complete this quest.

### ~~RequiredClasses~~

~~This field is a bitmask, you can combine class values. See [ChrClasses.dbc](ChrClasses)~~

### AllowableRaces

Races allowed to get the quest. 0 means the quest is accessible for all races. Field value is a decimal value which must transform to an 8 bits binary in order to be understandable. In binary form, each different bit represents a different race. They're assigned as follows :

**Race**

These values are 2^ID taken from ChrRaces.dbc

Examples:

0,1791 = All Races

690 (2 + 16 + 32 + 128 + 512) = Horde Quest

1101 (1 + 4 + 8 + 64 + 1024) = Alliance Quest

### RepObjectiveFaction

Faction ID for an objective to achieve a certain reputation value with. See Faction.dbc

### RepObjectiveValue

Reputation value that the player must achieve with the faction in [RepObjectiveFaction](#quest_template-RepObjectiveFaction) as part of the quest objectives.

### RewardNextQuest

**(Old field name: NextQuestIdChain)**

The quest entry from a **creature** or **gameobject** that ends a quest and starts a new one. The result is, that if you end the quest, the new quest instantly appears from the quest giver.

See the [examples section](#quest_template-Examples) for examples.

### RewardXPDifficulty

According to the [Level](#quest_template-Level), the basic experience with index *RewardXPDifficulty* is taken from QuestXP.dbc.

This field also controls the XP given as the XP is calculated from the value in this field by the following formula. If the quest is repeatable, XP will be given only once. The total XP that a character will receive is also affected by the level difference between the character's level and the quest's level.

The formula for calculating XP from the value in this field:
**QuestLevel &gt;= 65:** XP = RewMoneyMaxLevel / 6.0
**QuestLevel h1. 64:** XP = RewMoneyMaxLevel / 4.8
**QuestLevel 63:** XP = RewMoneyMaxLevel / 3.6
**QuestLevel h1. 62:** XP = RewMoneyMaxLevel / 2.4
**QuestLevel 61:** XP = RewMoneyMaxLevel / 1.2
**QuestLevel &lt;= 60:** XP = RewMoneyMaxLevel / 0.6

### RewardMoney

Money earned by completing the quest (if value &gt; 0) or money requirement to complete the quest (if value &lt; 0) .

### RewardBonusMoney

The money a character at level 80 would get when they complete this quest.

### RewardSpell

Spell that is shown to be casted on quest completion in the quest log. Note that this spell will NOT be casted if [RewardSpellCast](#quest_template-RewardSpellCast) is non-zero. The spell in the other field will be casted instead, in which case the spell here only serves as the visual in the quest log.

NOTE: This field comes straight from the WDB and should not be changed.

### RewardSpellCast

Spell that will always be casted at player when completing the quest. This can be learn spell and player learned some spell in result, or buff spell, for example. If this field is non-zero then this spell will ALWAYS be casted and the spell in [RewardSpell](#quest_template-RewardSpell) will not.

NOTE: This field comes straight from the WDB and should not be changed.

### RewardHonor

Number of honorable kill honor rewarded for completing this quest.

Example: An example value is 15 for quest 8388: At level 80 an honorable kill is 124 honor worth. Multiply this with 15 and you receive 1860, after the multiplication the value is rounded up. So the honor rewarded at level 80 is 1860 for this quest.

### RewardHonorMultiplier

Multiplies [RewardHonor](#quest_template-RewardHonor), so if value is 2, it will give double.

**WARNING:** If this field is 1 and [RewardHonor](#quest_template-RewardHonor) is 0, the quest will reward default honor kill value (124 honor at level 80)

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

### RewardTitleId

The title the character will receive upon completion of the quest. See [CharTitles.dbc](CharTitles)

### RequiredPlayerKills

Displays how much players you need to kill betd class=td class=a class=/td data-linked-resource-default-alias=fore completing the quest.

### RewardTalents

Will give X bonus talents to the player completed the quest. Leave"0"for No Bonus Talent Points.''

### RewardArenaPoints

Will Give X Arena Points to the player that completes the quest. Leave"0"For no Arena Points Reward.

### RewardChoiceItemId

Id of item available for reward choice.
Number of Charges in rewarded item available.

### RewardChoiceItemCount

Will choose how many items will be added for reward. E.g "RewardChoiceItemId" is the reward item and "RewardChoiceItemCount" is the count of how many items will be added as a reward.

### RewardItemId

[item Id](item_template#entry) given for reward (no choice).

### RewardItemCount

`field-no-description|46`

### RewardFactionId

Faction Id (from [Faction.dbc](Faction)) for which the quest give reputation points.
Number of gain or lost reputation points for Faction at quest completion. This is special reputation rewarding. Normal reputation reward to quest rewarding creature faction calculated and added automatically.

### RewardFactionValueId

This field is used for reputation lookup in [QuestFactionReward.dbc](QuestFactionReward) if [RewardFactionValueId](#quest_template-RewardFactionValueId) is 0. Value X in this field indicates RepX column of [QuestFactionReward.dbc](QuestFactionReward). If RewardRepValueId is positive, reputation from the first row of QuestFactionReward.dbc will be used, for negative values the second row is used.

### RewardFactionValueIdOverride

This field is used to give reputation values not present in QuestFactionReward.dbc or to override them if [RewardRepValueId](#quest_template-RewardRepValueId) is wrong for some reason. The value in this field is 100× the intended reputation reward (if you want to give 400 rep, put 40000 in RewardFactionValueIdOverride).

### POIContinent

MapId of a quest point of interest (POI - Point Of Interest). POI will be shown on the map when quest is active.

### POIx

X coordinate of quest POI.

### POIy

Y coordinate of quest POI.

### POIPriority

TODO

### Title

Title of the quest.

### Objectives

Objectives of the quest. If empty, quest is an auto-complete quest that can be immediately finished without accepting it first.

### Details

The quest text. You can use certain placeholders that will be filled in in-game: $B - line break, $N - name, $R - race, $C - class, $Gmale:female; (male and female can be replace with any synonymn you want, but the order must stay the same. IE: boy:girl / man:woman / sir:madam / dude:chick)

### OfferRewardText

First text send to the player by the NPC when completing the quest. You can use certain placeholders that will be filled in in-game: $B - line break, $N - name, $R - race, $C - class, $Gmale:female; (male and female can be replace with any synonymn you want, but the order must stay the same. IE: boy:girl / man:woman / sir:madam / dude:chick)

### RequestItemsText

Text sent to player when the player tries to talk to the NPC with the quest active but incomplete. (The text under the "Progress" title in Wowhead.) You can use certain placeholders that will be filled in in-game: $B - line break, $N - name, $R - race, $C - class, $Gmale:female; (male and female can be replace with any synonymn you want, but the order must stay the same. IE: boy:girl / man:woman / sir:madam / dude:chick)

### RequiredNpcOrGo

Value &gt; 0:required creature\_template ID the player needs to kill/cast on in order to complete the quest.
Value &lt; 0:required gameobject\_template ID the player needs to cast on in order to complete the quest.
If\*RequiredSpellCast\*is != 0, the objective is to cast on target, else kill.
NOTE: If RequiredSpellCast is != 0 and the spell has effects Send Event or Quest Complete, this field may be left empty.

### RequiredNpcOrGoCount

The number of times the creature or gameobject must be killed or casted upon.

### RequiredSourceItemId

Item ID that is needed indirectly by the quest. For example, the quests asks for item X but the only way to get item X is by activating item Y; however, item Y is also a quest item. Therefore you set item Y's ID in this field. This requirement will not appear in the quest text, it is just for the core to know when to drop a quest item that isn't in the RequiredItemId field but is still needed by the quest.

### RequiredSourceItemCount

The maximum number of copies of the item in RequiredSourceItemId that can be picked up (and dropped by the core).

### RequiredItemId
[Item\_template](item_template#id) 

Id of required item to complete the quest.

### RequiredItemCount

Amount of required items

### RequiredSpell

Spell Id required to cast on [RequiredNpcOrGo](quest_template#RequiredNpcOrGo) to update Objective.

### ObjectiveText

Used to define non-standard objective texts, that show up in the questlog. Example, "Heal fallen warrior" and the number gets added by Count values.

### DetailsEmote

`field-no-description|69`

### DetailsEmoteDelay

Emote delay in ms

### OfferRewardEmote

Emote played by the NPC at the time the character is rewarded for the quest.

### OfferRewardEmoteDelay

Emote delay in ms

### WDBVerified

## **Examples dealing with quests**

Always use PrevQuestId before using NextQuestId. NextQuestId is considered optional and to be used only when PrevQuestId is not sufficient

### Basic quest

Single, stand-alone quest with no prerequisites

```
    questA
```

```sql
entry = questA        PrevQuestId = 0        NextQuestId = 0        ExclusiveGroup = 0        NextQuestInChain = 0
```

### Prequest

When this quest require another quest to be rewarded

```
    questA
```

```sql
entry = questA        PrevQuestId = questX   NextQuestId = 0        ExclusiveGroup = 0        NextQuestInChain = 0
```

### Chain of quests

Player get quests in a strict chain that must be completed in a specific order.

```
    questA
      |
    questB
      |
    questC
      |
    questD
```

```sql
entry = questA      PrevQuestId = 0          NextQuestId = 0       ExclusiveGroup = 0       NextQuestInChain = questB
entry = questB      PrevQuestId = questA     NextQuestId = 0       ExclusiveGroup = 0       NextQuestInChain = questC
entry = questC      PrevQuestId = questB     NextQuestId = 0       ExclusiveGroup = 0       NextQuestInChain = questD
entry = questD      PrevQuestId = questC     NextQuestId = 0       ExclusiveGroup = 0       NextQuestInChain = 0
```

### Chain of quests with multiple start quests.

Player should only be allowed to complete one of three possible

```sql
    questA     questB    questC
      \           |         /
        ------ questD -----
                  |
               questE
```

```sql
entry = questA      PrevQuestId = 0        NextQuestId = questD    ExclusiveGroup = questA    NextQuestInChain = questD    
entry = questB      PrevQuestId = 0        NextQuestId = questD    ExclusiveGroup = questA    NextQuestInChain = questD
entry = questC      PrevQuestId = 0        NextQuestId = questD    ExclusiveGroup = questA    NextQuestInChain = questD
entry = questD      PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0         NextQuestInChain = questE
entry = questE      PrevQuestId = questD   NextQuestId = 0         ExclusiveGroup = 0         NextQuestInChain = 0
```

### Chain of quests with multiple start quests.

Player must complete all three initial quests before D becomes available

```sql
    questA    questB    questC
      \         |          /
       ------ questD -----
                |
              questE
```

```sql
entry = questA      PrevQuestId = 0        NextQuestId = questD   ExclusiveGroup = -questA    NextQuestInChain = questD
entry = questB      PrevQuestId = 0        NextQuestId = questD   ExclusiveGroup = -questA    NextQuestInChain = questD
entry = questC      PrevQuestId = 0        NextQuestId = questD   ExclusiveGroup = -questA    NextQuestInChain = questD
entry = questD      PrevQuestId = 0        NextQuestId = 0        ExclusiveGroup = 0          NextQuestInChain = questE
entry = questE      PrevQuestId = questD   NextQuestId = 0        ExclusiveGroup = 0          NextQuestInChain = 0
```

### Quests with split and a child quest

Completing A unlocks B and C that can be done at the same time. They both need to be completed before D becomes available. X is needed to obtain item for C and this quest should only be available if C is active

```sql
                questA
              /        \
          questB     questC  -  questX
              \        /
                questD
```

```sql
entry = questA       PrevQuestId = 0        NextQuestId = 0        ExclusiveGroup = 0         NextQuestInChain = 0
entry = questB       PrevQuestId = questA   NextQuestId = questD   ExclusiveGroup = -questB   NextQuestInChain = 0
entry = questC       PrevQuestId = questA   NextQuestId = questD   ExclusiveGroup = -questB   NextQuestInChain = 0
entry = questX       PrevQuestId = -questC  NextQuestId = 0        ExclusiveGroup = 0         NextQuestInChain = 0
entry = questD       PrevQuestId = 0        NextQuestId = 0        ExclusiveGroup = 0         NextQuestInChain = 0
```

### Multiple quest chains, leading to one final quest

Player may complete (not required to) X, but has to complete all three quest chains before final quest becomes available

```sql
                *questX*
                   |
    *questA*    *questC*    *questE*
       |           |            |
    *questB*    *questD*    *questF*
       \           |           /
         ------ *questG* -----
```

```sql
PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questC    entry = questX
PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questB    entry = questA
PrevQuestId = questA   NextQuestId = questG    ExclusiveGroup = -questB    NextQuestInChain = 0         entry = questB
PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questD    entry = questC
PrevQuestId = questC   NextQuestId = questG    ExclusiveGroup = -questB    NextQuestInChain = 0         entry = questD
PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questF    entry = questE
PrevQuestId = questE   NextQuestId = questG    ExclusiveGroup = -questB    NextQuestInChain = 0         entry = questF

PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questG
```

### Complicated

Player must first complete A, then B to unlock the chain from C to E. Three other quests in a group will also be unlocked, those can be done at the same time. The three grouped quests must all be completed before I becomes available. Completion of E and I is required to obtain the final quest.

```sql
                *questA*
                   |
                *questB*
              /          \
          *questC*     *questF*
             |         *questG*
          *questD*     *questH*
             |            |
          *questE*     *questI*
             \           /
                *questJ*
```

```sql
PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questB    entry = questA
PrevQuestId = questA   NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questB

PrevQuestId = questB   NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questD    entry = questC
PrevQuestId = questC   NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questE    entry = questD
PrevQuestId = questD   NextQuestId = questJ    ExclusiveGroup = -questE    NextQuestInChain = 0         entry = questE

PrevQuestId = questB   NextQuestId = questI    ExclusiveGroup = -questF    NextQuestInChain = 0         entry = questF
PrevQuestId = questB   NextQuestId = questI    ExclusiveGroup = -questF    NextQuestInChain = 0         entry = questG
PrevQuestId = questB   NextQuestId = questI    ExclusiveGroup = -questF    NextQuestInChain = 0         entry = questH

PrevQuestId = 0        NextQuestId = questJ    ExclusiveGroup = -questE    NextQuestInChain = 0         entry = questI

PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questJ
```

### Impossible - many quests may unlock many

Player can choose between two alternative chains (Chain A or B, but not both chains). A2 or B2 should unlock C, D and E when complete. When all three complete, F should be unlocked. If player get A3 or B3 after complete F, depends on if chain A or B was chosen

```sql
                *questA1*           *questB1*
                    |                   |
                *questA2*           *questB2*
                    \                  /
                     ---- *questC* ----
                          *questD*
                          *questE*
                             |
                          *questF*
                         /        \
                    *questA3*   *questB3*
```

```sql
PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questA2   entry = questA1
PrevQuestId = questA1  NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questA2

PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = questB2   entry = questB1
PrevQuestId = questB1  NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questB2

PrevQuestId = 0        NextQuestId = questF    ExclusiveGroup = -questC    NextQuestInChain = 0         entry = questC
PrevQuestId = 0        NextQuestId = questF    ExclusiveGroup = -questC    NextQuestInChain = 0         entry = questD
PrevQuestId = 0        NextQuestId = questF    ExclusiveGroup = -questC    NextQuestInChain = 0         entry = questE

PrevQuestId = 0        NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questF

PrevQuestId = questF   NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questA3
PrevQuestId = questF   NextQuestId = 0         ExclusiveGroup = 0          NextQuestInChain = 0         entry = questB3
```

Note:

If player can choose between chain A or B may be determined by faction status (aldor or scryer), using ReqMinRepFaction = 1. Player should not be able to be neutral+1 with both at the same time. This may be the common threshold to obtain aldor or scryer quests (this is unsure). If that is the case, only the unlock of C, D and E after complete A2 *or* B2 is the impossible part.\_Note 2: With the [Conditions](conditions) table now every quest chain is possible.
