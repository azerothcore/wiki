# loot_template

[<-Back-to:World](database-world)

**The \*_loot_template tables**

**Table Structure**

| Field                           | Type         | Attributes | Key | Null | Default | Extra | Comment                       |
| ------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [Entry](#entry)                 | INT          | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [Item](#item)                   | INT          | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [Reference](#reference)         | INT          |            |     | NO   | 0       |       |                               |
| [Chance](#chance)               | FLOAT        |            |     | NO   | 0       |       |                               |
| [QuestRequired](#questrequired) | TINYINT      |            |     | NO   | 0       |       |                               |
| [LootMode](#lootmode)           | SMALLINT     | UNSIGNED   |     | NO   | 1       |       |                               |
| [GroupId](#groupid)             | TINYINT      | UNSIGNED   |     | NO   | 0       |       | PRI in creature_loot_template |
| [MinCount](#mincount)           | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                               |
| [MaxCount](#maxcount)           | TINYINT      | UNSIGNED   |     | NO   | 1       |       |                               |
| [Comment](#comment)             | VARCHAR(255) |            |     | YES  | NULL    |       | TEXT in player_loot_template  |

**Description of the fields**

### Entry

| Table                     | Entry                                                                | Comment                                                                                   |
| ------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| creature_loot_template    | [creature_template.lootid](creature_template#lootid)                 | Usually the same as [creature_template.entry](creature_template#entry)                    |
| disenchant_loot_template  | [item_template.DisenchantID](item_template#disenchantid)             |                                                                                           |
| fishing_loot_template     | area id                                                              |                                                                                           |
| gameobject_loot_template  | [gameobject_template.data1](gameobject_template#data023)             | Need to have gamobject type GAMEOBJECT_TYPE_CHEST (3) or GAMEOBJECT_TYPE_FISHINGHOLE (25) |
| item_loot_template        | [item_template.entry](item_template#entry)                           |                                                                                           |
| mail_loot_template        | mail template id                                                     |                                                                                           |
| milling_loot_template     | [item_template.entry](item_template#entry)                           |                                                                                           |
| pickpocket_loot_template  | [creature_template.pickpocketloot](creature_template#pickpocketloot) |                                                                                           |
| player_loot_template      | TeamID (0 Horde/1 Alliance)                                          | Only drops in BGs as insignia removal.                                                    |
| prospecting_loot_template | [item_template.entry](item_template#entry)                           |                                                                                           |
| reference_loot_template   | [\*_loot_template.reference](loot_template#reference)                |                                                                                           |
| skinning_loot_template    | [creature_template.skinloot](creature_template#skinloot)             | Also includes minable/herbable loot from creatures                                        |
| spell_loot_template       | SpellID                                                              |                                                                                           |

### Item

[item_template.entry](item_template#entry)

### Reference

[reference_loot_template.entry](loot_template#entry).

Uses the entries in the referenced template in the current template.

**Note: Self reference is never allowed. This will lead to a crash.**

### Chance

Chance for loot to drop. Chance can never exceed a total of 100 for all entries with the same [GroupID](#groupid).

If the field is left at 0 the chance will be even across all entries with the same [GroupID](#groupid) and chance = 0.

### QuestRequired

0 - Loot is always available.

1 - Loot can only drop if the player has a quest with the item id specified in [quest_template.RequiredItemId1-6](quest_template#requireditemid1).

### LootMode

Bitmask.

Used to separate conditional loot. Such as Hardmode loot in Ulduar. The active lootmode(s) can be changed at any time by the core.

In most cases this field is left as 1.

### GroupId

Used to group items within the same loot template.

- Only one item from the group can drop.
- If the total [chance](#chance) for the group is 100 then one item will always drop.
- If the total [chance](#chance) for the group is less than 100, then there is a risk of empty loot.

Referenced loot can not be a part of a group.

**Note: The client can only display 16 items in the loot windows, this includes gold. Therefore it is not recomended to use more than 16 groups.**

### MinCount

Minimum amount of an item to drop in a single loot. Cannot be 0.

### MaxCount

| Table                    | Comment                                                                                                                                                                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*_loot_template         | Maximum amount of an item to drop in a single loot.                                                                                                                                                                                     |
| referenced_loot_template | How many times a referenced loot template should be processed. **Note: The core only rolls chance per loot definition once. If the initial reference roll was lost, it will skip the current loot completely, regardless of MaxCount.** |

### Comment

Comment
