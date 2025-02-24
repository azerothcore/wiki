# quest_template_addon

[<-Back-to:World](database-world)

**Table: quest_template_addon**

Contains extra definitions like linking quests, dependencies and requirements for the quests defined in the [quest_template](quest_template) table to become available to the player.

**Structure:**

| Field                                           | Type      | Attributes | Key | Null | Default | Extra | Comment                               |
| ----------------------------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------- |
| [ID](#id)                                       | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       | Unique ID linked to quest_template.ID |
| [MaxLevel](#maxlevel)                           | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |
| [AllowableClasses](#allowableclasses)           | INT       | UNSIGNED   |     | NO   |         |       |                                       |
| [SourceSpellID](#sourcespellid)                 | MEDIUMINT | UNSIGNED   |     | NO   |         |       |                                       |
| [PrevQuestID](#prevquestid)                     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [NextQuestID](#nextquestid)                     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [ExclusiveGroup](#exclusivegroup)               | MEDIUMINT |            |     | NO   |         |       |                                       |
| [RewardMailTemplateID](#rewardmailtemplateid)   | MEDIUMINT | UNSIGNED   |     | NO   |         |       |                                       |
| [RewardMailDelay](#rewardmaildelay)             | INT       | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredSkillID](#requiredskillid)             | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredSkillPoints](#requiredskillpoints)     | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMinRepFaction](#requiredminrepfaction) | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMaxRepFaction](#requiredmaxrepfaction) | SMALLINT  | UNSIGNED   |     | NO   |         |       |                                       |
| [RequiredMinRepValue](#requiredminrepvalue)     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [RequiredMaxRepValue](#requiredmaxrepvalue)     | MEDIUMINT |            |     | NO   |         |       |                                       |
| [ProvidedItemCount](#provideditemcount)         | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |
| [SpecialFlags](#specialflags)                   | TINYINT   | UNSIGNED   |     | NO   |         |       |                                       |

**Description of the fields:**

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

Note: All quests that use an ExclusiveGroup must also have entries in [pool_template](pool_template) and [pool_quest](quest_template#examples-dealing-with-quests) for examples.

### RewardMailTemplateID

If the quest gives as a reward an item from a possible list of items, the ID here corresponds to the proper loot template in [quest_mail_loot_template](loot_template). According to the rules in that loot template, items "looted" will be sent by mail at the completion of the quest.

### RewardMailDelay

How many seconds to wait until the mail is sent to the character that turned in a quest rewarding items from a loot template.

### RequiredSkillID

Skill required to know to accept the quest. See [SkillLine.dbc](SkillLine)
0 means no skill is required.

### RequiredSkillPoints

Skill points required to have in order to accept the quest.

### RequiredMinRepFaction

Faction ID for reputation requirement. See [Faction.dbc](Faction).

### RequiredMaxRepFaction

The Faction ID for the faction that controls the maximum reputation value that the player can have and still get the quest. See [Faction.dbc](Faction).

### RequiredMinRepValue

Players must have this reputation or higher in order to receive the quest.

### RequiredMaxRepValue

The maximum reputation value that the player can have with a faction and still get the quest. If the player has more reputation than the value in this field, the quest will not be able to be taken anymore.

### ProvidedItemCount

Number of items given to the player (inserted in the player's bags) upon accepting the quest.

### SpecialFlags

This field is a bitmask and is for controlling server side quest functions. Blizzard keeps these data server-side and they are not sent to the client, so we have to populate the field manually.

| Flag                                      | Value | Description                                                                                                                                                                                                                              |
| ----------------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| QUEST_SPECIAL_FLAGS_NONE                  | 0     | No extra requirements.                                                                                                                                                                                                                   |
| QUEST_SPECIAL_FLAGS_REPEATABLE            | 1     | Makes the quest repeatable.                                                                                                                                                                                                              |
| QUEST_SPECIAL_FLAGS_EXPLORATION_OR_EVENT  | 2     | Makes the quest only completable by some external event (an entry in [areatrigger_involvedrelation](areatrigger_involvedrelation), spell effect quest complete or an entry in [spell_scripts](scripts) with command 7 as some examples). |
| QUEST_SPECIAL_FLAGS_AUTO_ACCEPT           | 4     | Make quest auto-accept. As of patch 3.3.5a only quests in the starter area need this flag.                                                                                                                                               |
| QUEST_SPECIAL_FLAGS_DF_QUEST              | 8     | Only used for Dungeon Finder quests.                                                                                                                                                                                                     |
| QUEST_SPECIAL_FLAGS_MONTHLY               | 16    | Makes the quest monthly.                                                                                                                                                                                                                 |
| QUEST_SPECIAL_FLAGS_CAST                  | 32    | The quest requires RequiredOrNpcGo killcredit (a spell cast), but NOT an actual NPC kill. This action usually involves killing an invisible "bunny" NPC.                                                                                 |
| QUEST_SPECIAL_FLAGS_NO_REP_SPILLOVER      | 64    | Makes quest not share rewarded reputation with other allied factions.                                                                                                                                                                    |
| QUEST_SPECIAL_FLAGS_CAN_FAIL_IN_ANY_STATE | 128   | Allows quest to fail in Player::FailQuest() independant of its current state, e.g. relevant for timed. quests that are 'completed' right from the beginning.                                                                             |
| QUEST_SPECIAL_FLAGS_NO_LOREMASTER_COUNT   | 256   | This quest shouldn't count towards the Loremaster Achivement.                                                                                                                                                                            |
