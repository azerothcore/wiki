# quest\_template\_addon

[<-Back-to:World](database-world.md)

**Table: quest\_template\_addon**

Contains extra definitions like linking quests, dependencies and requirements for the quests defined in the [quest\_template](quest_template) table to become available to the player.

**Structure:**

| Field                       | Type         | Attributes | Key | Null | Default | Extra | Comment                               |
|-----------------------------|--------------|------------|-----|------|---------|-------|---------------------------------------|
| [ID][1]                     | MEDIUMINT(8) | unsigned   | PRI | NO   |         |       | Unique ID linked to quest_template.ID |
| [MaxLevel][2]               | TINYINT(3)   | unsigned   |     | NO   |         |       |                                       |
| [AllowableClasses][3]       | int(10)      | unsigned   |     | NO   |         |       |                                       |
| [SourceSpellID][4]          | MEDIUMINT(8) | unsigned   |     | NO   |         |       |                                       |
| [PrevQuestID][5]            | MEDIUMINT(8) |            |     | NO   |         |       |                                       |
| [NextQuestID][6]            | MEDIUMINT(8) |            |     | NO   |         |       |                                       |
| [ExclusiveGroup][7]         | MEDIUMINT(8) |            |     | NO   |         |       |                                       |
| [RewardMailTemplateID][8]   | MEDIUMINT(8) | unsigned   |     | NO   |         |       |                                       |
| [RewardMailDelay][9]        | int(10)      | unsigned   |     | NO   |         |       |                                       |
| [RequiredSkillID][10]       | SMALLINT(5)  | unsigned   |     | NO   |         |       |                                       |
| [RequiredSkillPoints][11]   | SMALLINT(5)  | unsigned   |     | NO   |         |       |                                       |
| [RequiredMinRepFaction][12] | SMALLINT(5)  | unsigned   |     | NO   |         |       |                                       |
| [RequiredMaxRepFaction][13] | SMALLINT(5)  | unsigned   |     | NO   |         |       |                                       |
| [RequiredMinRepValue][14]   | MEDIUMINT(8) |            |     | NO   |         |       |                                       |
| [RequiredMaxRepValue][15]   | MEDIUMINT(8) |            |     | NO   |         |       |                                       |
| [ProvidedItemCount][16]     | TINYINT(3)   | unsigned   |     | NO   |         |       |                                       |
| [SpecialFlags][17]          | TINYINT(3)   | unsigned   |     | NO   |         |       |                                       |

[1]: #id
[2]: #maxlevel
[3]: #allowableclasses
[4]: #sourcespellid
[5]: #prevquestid
[6]: #nextquestid
[7]: #exclusivegroup
[8]: #rewardmailtemplateid
[9]: #rewardmaildelay
[10]: #requiredskillid
[11]: #requiredskillpoints
[12]: #requiredminrepfaction
[13]: #requiredmaxrepfaction
[14]: #requiredminrepvalue
[15]: #requiredmaxrepvalue
[16]: #provideditemcount
[17]: #specialflags

**Description of the fields:**

### **ID**

Unique quest ID, matching the same quest ID in [quest\_template.ID](quest_template#id)

### **MaxLevel**

Maximum player level at which a character can get the quest.

### **AllowableClasses**

Classes required to get the quest. 0 means the quest is available for all classes.
This field is a bitmask, you can combine class values. See [ChrClasses.dbc](ChrClasses)

### **SourceSpellID**

The spell ID cast on player upon starting the quest.

### **PrevQuestID**

- **if value > 0:** Contains the previous quest id, that must be completed before this quest can be started.
- **If value < 0:** Contains the parent quest id, that must be active before this quest can be started.

See the [examples section](quest_template#examples-dealing-with-quests) for examples.

### **NextQuestID**

Contains the next quest id, in case PrevQuestId of that other quest is not sufficient.

See the [examples section](quest_template#examples-dealing-with-quests) for examples.

### **ExclusiveGroup**

- **if ExclusiveGroup > 0**

Allows to define a group of quests of which only one may be chosen and completed. E.g. if from quests 1200, 1201 and 1202 only one should be allowed to be chosen, insert 1200 into ExclusiveGroup of all 3 quests.

- **if ExclusiveGroup < 0**

Allows to define a group of quests of which all must be completed and rewarded to start next quest. E.g. if quest 1000 dependent from one of quests 1200, 1201 and 1202 and all this quests have same negative exclusive group then all this quest must be completed and rewarded before quest 1000 can be started.

Note: All quests that use an ExclusiveGroup must also have entries in [pool\_template](pool_template) and [pool\_quest](quest_template#examples-dealing-with-quests) for examples.

### **RewardMailTemplateID**

If the quest gives as a reward an item from a possible list of items, the ID here corresponds to the proper loot template in [quest\_mail\_loot\_template](loot_template). According to the rules in that loot template, items "looted" will be sent by mail at the completion of the quest.

### **RewardMailDelay**

How many seconds to wait until the mail is sent to the character that turned in a quest rewarding items from a loot template defined in [RewardMailTemplateId](quest_template#rewardmailtemplateid)

### **RequiredSkillID**

Skill required to know to accept the quest. See [SkillLine.dbc](SkillLine)
0 means no skill is required.

### **RequiredSkillPoints**

Skill points required to have in order to accept the quest.

### **RequiredMinRepFaction**

Faction ID for reputation requirement. See [Faction.dbc](Faction)

### **RequiredMaxRepFaction**

The Faction ID for the faction that controls the maximum reputation value that the player can have and still get the quest. See [Faction.dbc](Faction)

### **RequiredMinRepValue**

Players must have this reputation or higher in order to receive the quest.

### **RequiredMaxRepValue**

The maximum reputation value that the player can have with a faction and still get the quest. If the player has more reputation than the value in this field, the quest will not be able to be taken anymore.

### **ProvidedItemCount**

Number of items given to the player (inserted in the player's bags) upon accepting the quest.

### **SpecialFlags**

This field is a bitmask and is for controlling server side quest functions. Blizzard keeps these data server-side and they are not sent to the client, so we have to populate the field manually.

- 0: No extra requirements
- 1: Makes the quest repeatable.
- 2: Makes the quest only completable by some external event (an entry in [areatrigger\_involvedrelation](areatrigger_involvedrelation), spell effect quest complete or an entry in [spell\_scripts](scripts) with command 7 as some examples)
- 4: Make quest auto-accept. As of patch 3.3.5a only quests in the starter area need this flag.
- 8: Only used for Dungeon Finder quests
- 16: Makes the quest monthly
- 32: The quest requires RequiredOrNpcGo killcredit (a spell cast), but NOT an actual NPC kill. This action usually involves killing an invisible "bunny" NPC.
