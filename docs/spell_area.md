# spell\_area

[<-Back-to:World](database-world)

**The \`spell\_area\` table**

This table is used to apply a specific spell aura to the player within an area in the game. When any player enters this area or somehow interacts with a quest, this aura will be handled accordingly.

**Table: spell\_area's Structure**

| Field                                                  | Type    |          | Null | Key | Default | Extra | Comment |
| :----------------------------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [spell](#spell)                                        | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [area](#area)                                          | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [quest_start](#queststart)                             | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [quest_end](#questend)                                 | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [aura_spell](#auraspell)                               | INT     |          | NO   | PRI | 0       |       |         |
| [racemask](#racemask)                                  | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [gender](#gender)                                      | TINYINT | UNSIGNED | NO   | PRI | 2       |       |         |
| [autocast](#autocast)                                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [quest_start_status](#queststartstatus-questendstatus) | INT     |          | NO   |     | 64      |       |         |
| [quest_end_status](#queststartstatus-questendstatus)   | INT     |          | NO   |     | 11      |       |         |

**Description of the table's fields**

### spell

The spell ID of the spell to be casted on the player. See [Spell.dbc](spell).

### area

The area ID. Type ".gps" in-game and find the "Area:" number to use for this cell. Also see AreaTable.dbc.

### quest\_start

The entry of the quest which the player must have in the state defined by **quest\_start\_status**. See [quest\_template.id](quest_template#id).

### quest\_end

The entry of the quest which the player must not have in the state defined by **quest\_end\_status**. See [quest\_template.id](quest_template#id). Setting both **quest\_start** and **quest\_end** to the same value is useless.

### aura\_spell

If set, this value (plus or minus aura spell ID from Spell.dbc) imposes additional condition.

The value has the following effect:

- **< 0**  (negative values) If the player has aura **-aura\_spell** then the [spell](#spell) will not be activated.
-   **0**   this column is ignored.
- **> 0**  (positive values) If the player has no aura **aura\_spell** then the [spell](#spell) will not be activated.

### racemask

This ID is automatically called from [ChrRaces.dbc](chrraces). The bitmask is entered here.

- 0, 1791 = All Races
- 690 (2 + 16 + 32 + 128 + 512) = Horde Only
- 1101 (1 + 4 + 8 + 64 + 1024 ) = Alliance Only

### gender

The gender type this entry applies to. 0 = Male, 1 = Female, 2 = Any.

### autocast

1 if the aura is applied automatically when the player enters the area and meets the other requirements. 0 if the spell is only allowed to be cast in the area, for example by an item or a script.

The aura is always removed when the player leaves the area.

### quest\_start\_status, quest\_end\_status

Within **quest\_start\_status**, you can define the mask of quest status required for **quest\_start**.

Within **quest\_end\_status**,  you can define the mask of quest status required for **quest\_end**. 

Example:

Area 257 is a cavern on Teldrassil. What we want is simple : When the player take the 28725 quest, he have the aura in the cavern. When he finish the 28727 quest, the aura disappear.

You should have the spell 92237 when entering the cavern IF :

- The start quest 28725 is incomplete, complete or rewarded (2 | 8 | 64 = 74) 
- The end quest 28727 is not taked (none), incomplete or complete BUT not rewarded (1 | 2 | 8 = 11)

Here is the SQL for this example : 

```sql
INSERT INTO `spell_area` (`spell`, `area`, `quest_start`, `quest_end`, `autocast`, `quest_start_status`, `quest_end_status`) VALUES 
(92237, 257, 28725, 28727, 1, 74, 11);
```

| Quest Status                       | Flag          | Explanation                                                                         |
| ---------------------------------- | ------------- | ----------------------------------------------------------------------------------- |
| QUEST\_STATUS\_NONE = 0            | 1             | Player does not have or had quest at all. He could accept it, but he did not (yet). |
| QUEST\_STATUS\_COMPLETE = 1        | 2             | Player fulfilled objectives, but did not hand it in yet.                            |
| ~~QUEST\_STATUS\_UNAVAILABLE = 2~~ | 4 (NOT USED)  | (Not used)                                                                          |
| QUEST\_STATUS\_INCOMPLETE = 3      | 8             | Player did not fulfill objectives yet                                               |
| ~~QUEST\_STATUS\_AVAILABLE = 4~~   | 16 (NOT USED) | (Not used)                                                                          |
| QUEST\_STATUS\_FAILED = 5          | 32            | Player failed to fulfill objectives for any reason, e.g. time limit                 |
| QUEST\_STATUS\_REWARDED = 6        | 64            | Player handed quest in and this is sort of a post-quest interaction                 |

Example for a SQL

 For a \`quest\_end\_status\` that should contain QUEST\_STATUS\_NONE (1), QUEST\_STATUS\_COMPLETE (2) and QUEST\_STATUS\_INCOMPLETE (8):

``` sql
-- equivalent to `quest_end_status`= 11
UPDATE `spell_area` SET `quest_end_status`= (1|2|8) WHERE `spell`=XXXXX AND `area`=YYYY;
```

Some examples:

- An area could pacify all players (spell 39331)
- Another area could full heal every 1 second (spell 48591)
- Teleport player out of an area (spell 53141)
- Factions-specific buffs, e.g. in Icecrown Citadel:
- "Hellscream's Warsong" (spell 73822) for horde 
- "Strength of Wrynn" (spell 73828) for alliance
- Even region-based buffs, such as area 440 - Tanaris.
