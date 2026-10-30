# quest\_template\_addon

[<-Back-to:World](database-world)

**Table: quest_template_addon**

Contains extra definitions like linking quests, dependencies and requirements for the quests defined in the [quest_template](quest_template) table to become available to the player.

**Table: quest\_template\_addon's Structure**

| Field                                           | Type      |          | Null | Key | Default | Extra | Comment                               |
| :---------------------------------------------- | :-------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------ |
| [ID](#id)                                       | INT       | UNSIGNED | NO   | PRI | 0       |       | Unique ID linked to quest_template.ID |
| [MaxLevel](#maxlevel)                           | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                       |
| [AllowableClasses](#allowableclasses)           | INT       | UNSIGNED | NO   |     | 0       |       |                                       |
| [SourceSpellID](#sourcespellid)                 | INT       | UNSIGNED | NO   |     | 0       |       |                                       |
| [PrevQuestID](#prevquestid)                     | INT       |          | NO   |     | 0       |       |                                       |
| [NextQuestID](#nextquestid)                     | INT       | UNSIGNED | NO   |     | 0       |       |                                       |
| [ExclusiveGroup](#exclusivegroup)               | INT       |          | NO   |     | 0       |       |                                       |
| [BreadcrumbForQuestId](#breadcrumbforquestid)   | MEDIUMINT | UNSIGNED | NO   |     | 0       |       |                                       |
| [RewardMailTemplateID](#rewardmailtemplateid)   | INT       | UNSIGNED | NO   |     | 0       |       |                                       |
| [RewardMailDelay](#rewardmaildelay)             | INT       | UNSIGNED | NO   |     | 0       |       |                                       |
| [RequiredSkillID](#requiredskillid)             | SMALLINT  | UNSIGNED | NO   |     | 0       |       |                                       |
| [RequiredSkillPoints](#requiredskillpoints)     | SMALLINT  | UNSIGNED | NO   |     | 0       |       |                                       |
| [RequiredMinRepFaction](#requiredminrepfaction) | SMALLINT  | UNSIGNED | NO   |     | 0       |       |                                       |
| [RequiredMaxRepFaction](#requiredmaxrepfaction) | SMALLINT  | UNSIGNED | NO   |     | 0       |       |                                       |
| [RequiredMinRepValue](#requiredminrepvalue)     | INT       |          | NO   |     | 0       |       |                                       |
| [RequiredMaxRepValue](#requiredmaxrepvalue)     | INT       |          | NO   |     | 0       |       |                                       |
| [ProvidedItemCount](#provideditemcount)         | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                       |
| [SpecialFlags](#specialflags)                   | INT       | UNSIGNED | NO   |     | 0       |       |                                       |

**Description of the table's fields**

### ID

Unique quest ID, matching the same quest ID in [quest_template.ID](quest_template#id)

### MaxLevel

Maximum player level at which a character can get the quest.

### AllowableClasses

Classes required to get the quest. 0 means the quest is available for all classes.
This field is a bitmask, you can combine class values. See [ChrClasses.dbc](chrclasses)

### SourceSpellID

The spell ID cast on player upon starting the quest.

### PrevQuestID

- **if value > 0:** Contains the previous quest id, that must be completed before this quest can be started.
- **If value < 0:** Contains the parent quest id, that must be active before this quest can be started.

### NextQuestID

Contains the next quest id, in case PrevQuestId of that other quest is not sufficient.

### ExclusiveGroup

- **if ExclusiveGroup > 0**

Allows to define a group of quests of which only one may be chosen and completed. E.g. if from quests 1200, 1201 and 1202 only one should be allowed to be chosen, insert 1200 into ExclusiveGroup of all 3 quests.

- **if ExclusiveGroup < 0**

Allows to define a group of quests of which all must be completed and rewarded to start next quest. E.g. if quest 1000 dependent from one of quests 1200, 1201 and 1202 and all this quests have same negative exclusive group then all this quest must be completed and rewarded before quest 1000 can be started.

Note: All quests that use an ExclusiveGroup must also have entries in [pool_template](pool_template) and [pool_quest](pool_quest).

### BreadcrumbForQuestId

If set, indicates that this quest is a breadcrumb leading to the quest with the specified ID. The two quests become mutually exclusive:

- This quest (the breadcrumb) becomes unavailable if the target quest is taken, complete, or rewarded.
- The target quest becomes unavailable if this quest is in progress or complete (but not if rewarded — completing the breadcrumb unlocks the target quest).

This single field replaces the need for multiple condition entries. `0` means no breadcrumb relationship.

### RewardMailTemplateID

If the quest gives as a reward an item from a possible list of items, the ID here corresponds to the proper loot template in [quest_mail_loot_template](loot_template). According to the rules in that loot template, items "looted" will be sent by mail at the completion of the quest.

### RewardMailDelay

How many seconds to wait until the mail is sent to the character that turned in a quest rewarding items from a loot template.

### RequiredSkillID

Skill required to know to accept the quest. See [SkillLine.dbc](skillline)
0 means no skill is required.

### RequiredSkillPoints

Skill points required to have in order to accept the quest.

### RequiredMinRepFaction

Faction ID for reputation requirement. See [Faction.dbc](faction).

### RequiredMaxRepFaction

The Faction ID for the faction that controls the maximum reputation value that the player can have and still get the quest. See [Faction.dbc](faction).

### RequiredMinRepValue

Players must have this reputation or higher in order to receive the quest.

### RequiredMaxRepValue

The maximum reputation value that the player can have with a faction and still get the quest. If the player has more reputation than the value in this field, the quest will not be able to be taken anymore.

### ProvidedItemCount

Number of items given to the player (inserted in the player's bags) upon accepting the quest.

### SpecialFlags

This field is a bitmask and is for controlling server side quest functions. Blizzard keeps these data server-side and they are not sent to the client, so we have to populate the field manually.

| Value | Hex      | Flag                                      | Comment                                                                                                                                                                                                                                  |
| :---- | :------: | :---------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | `0x0000` | QUEST_SPECIAL_FLAGS_NONE                  | No extra requirements.                                                                                                                                                                                                                   |
| 1     | `0x0001` | QUEST_SPECIAL_FLAGS_REPEATABLE            | Makes the quest repeatable.                                                                                                                                                                                                              |
| 2     | `0x0002` | QUEST_SPECIAL_FLAGS_EXPLORATION_OR_EVENT  | Makes the quest only completable by some external event (an entry in [areatrigger_involvedrelation](areatrigger_involvedrelation), spell effect quest complete or an entry in [spell_scripts](scripts) with command 7 as some examples). |
| 4     | `0x0004` | QUEST_SPECIAL_FLAGS_AUTO_ACCEPT           | Make quest auto-accept. As of patch 3.3.5a only quests in the starter area need this flag.                                                                                                                                               |
| 8     | `0x0008` | QUEST_SPECIAL_FLAGS_DF_QUEST              | Only used for Dungeon Finder quests.                                                                                                                                                                                                     |
| 16    | `0x0010` | QUEST_SPECIAL_FLAGS_MONTHLY               | Makes the quest monthly.                                                                                                                                                                                                                 |
| 32    | `0x0020` | QUEST_SPECIAL_FLAGS_CAST                  | The quest requires RequiredOrNpcGo killcredit (a spell cast), but NOT an actual NPC kill. This action usually involves killing an invisible "bunny" NPC.                                                                                 |
| 64    | `0x0040` | QUEST_SPECIAL_FLAGS_NO_REP_SPILLOVER      | Makes quest not share rewarded reputation with other allied factions.                                                                                                                                                                    |
| 128   | `0x0080` | QUEST_SPECIAL_FLAGS_CAN_FAIL_IN_ANY_STATE | Allows quest to fail in Player::FailQuest() independant of its current state, e.g. relevant for timed. quests that are 'completed' right from the beginning.                                                                             |
| 256   | `0x0100` | QUEST_SPECIAL_FLAGS_NO_LOREMASTER_COUNT   | This quest shouldn't count towards the Loremaster Achivement.                                                                                                                                                                            |
