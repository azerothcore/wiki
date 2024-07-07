# spell\_area

[<-Back-to:World](database-world)

**The \`spell\_area\` table**

This table is used to apply a specific spell aura to the player within an area in the game. When any player enters this area or somehow interacts with a quest, this aura will be handled accordingly.

**Table Structure**

| Field                   | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [spell][1]              | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [area][2]               | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [quest_start][3]        | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [quest_end][4]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [aura_spell][5]         | MEDIUMINT | SIGNED     | PRI | NO   |         |       |         |
| [racemask][6]           | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [gender][7]             | TINYINT   | UNSIGNED   | PRI | NO   |         |       |         |
| [flags][8]              | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [quest_start_status][9] | INT       | UNSIGNED   |     | NO   |         |       |         |
| [quest_end_status][10]  | INT       | UNSIGNED   |     | NO   |         |       |         |

[1]: #spell
[2]: #area
[3]: #quest_start
[4]: #quest_end
[5]: #aura_spell
[6]: #racemask
[7]: #gender
[8]: #flags
[9]: #quest_start_status
[10]: #quest_end_status

**Description of the fields**

### spell

The spell ID of the spell to be casted on the player. See [Spell.dbc](Spell).

### area

The area ID. Type ".gps" in-game and find the "Area:" number to use for this cell. Also see AreaTable.dbc.

### quest\_start

The entry of the quest which the player must have in the state defined by **quest\_start\_status**. See [quest\_template.id](quest_template#id).

### quest\_end

The entry of the quest which the player must not have in the state defined by **quest\_end\_status**. See [quest\_template.id](quest_template#id). Setting both **quest\_start** and **quest\_end** to the same value is useless.

### aura\_spell

If set, this value (plus or minus aura spell ID from Spell.dbc) imposes additional condition.

The value has the following effect:

- **< 0**  (negative values) If the player has aura **-aura\_spell** then the [spell](#spell_area-spell) will not be activated.
-   **0**   this column is ignored.
- **> 0**  (positive values) If the player has no aura **aura\_spell** then the [spell](#spell_area-spell) will not be activated.

### racemask

This ID is automatically called from [ChrRaces.dbc](chrraces). The bitmask is entered here.

- 0, 1791 = All Races
- 690 (2 + 16 + 32 + 128 + 512) = Horde Only
- 1101 (1 + 4 + 8 + 64 + 1024 ) = Alliance Only

### gender

The gender type this entry applies to. 0 = Male, 1 = Female, 2 = Any.

### flags

| Flag | Value | Name                          | Comment                                                                                                                   |
| ---- | ----- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 1    | 0x01  | SPELL\_AREA\_FLAG\_AUTOCAST   | If the spell should be automatically applied when the character enters the area. Also prevents the user from removing it. |
| 2    | 0x02  | SPELL\_AREA\_FLAG\_AUTOREMOVE | If the spell should be automatically removed when the character is **inside** the area (only works with quest updates)    |

Note: Spell is allways removed on leaving area, SPELL\_AREA\_FLAG\_AUTOREMOVE does not effect this.

Example:

- flags = 0 : Spell not added on enter (must be added manually), not automatically removed on quest update, but removed on leave.
- flags = 1 : Spell is automatically applied on enter, not automatically removed on quest update, but removed on leave.
- flags = 2 : Spell not added on enter (must be added manually), automatically removed on quest update and removed on leave.
- flags = 3 : (Default) Spell is automatically applied on enter, automatically removed on quest update and removed on leave.

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
