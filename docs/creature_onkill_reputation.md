# creature\_onkill\_reputation

[<-Back-to:World](database-world)

**The \`creature\_onkill\_reputation\` table**

This table controls the reputation given by creatures when killed by other players.

**Table Structure**

| Field                     | Type      | Attributes | Key | Null | Default | Extra | Comment             |
| ------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------- |
| [creature_id][1]          | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Creature Identifier |
| [RewOnKillRepFaction1][2] | SMALLINT  | SIGNED     |     | NO   | 0       |       |                     |
| [RewOnKillRepFaction2][3] | SMALLINT  | SIGNED     |     | NO   | 0       |       |                     |
| [MaxStanding1][4]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [IsTeamAward1][5]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [RewOnKillRepValue1][6]   | MEDIUMINT | SIGNED     |     | NO   | 0       |       |                     |
| [MaxStanding2][7]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [IsTeamAward2][8]         | TINYINT   | SIGNED     |     | NO   | 0       |       |                     |
| [RewOnKillRepValue2][9]   | MEDIUMINT | SIGNED     |     | NO   | 0       |       |                     |
| [TeamDependent][10]       | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                     |

[1]: #creature_id
[2]: #rewonkillrepfaction1
[3]: #rewonkillrepfaction2
[4]: #maxstanding1
[5]: #isteamaward1
[6]: #rewonkillrepvalue1
[7]: #maxstanding2
[8]: #isteamaward2
[9]: #rewonkillrepvalue2
[10]: #teamdependent

**Description of the fields**

### creature\_id

The template ID of the creature. See [creature\_template.entry](creature_template#creature_template-entry)

### RewOnKillRepFaction

The faction ID of the faction that the player will gain or lose points in. See Faction.dbc

### MaxStanding

The maximum standing that the creature will award reputation until. If the player achieves this standing or any other standing higher than this, the creature will not award any reputation.

| ID  | Rank       |
| --- | ---------- |
| 0   | Hated      |
| 1   | Hostile    |
| 2   | Unfriendly |
| 3   | Neutral    |
| 4   | Friendly   |
| 5   | Honored    |
| 6   | Revered    |
| 7   | Exalted    |

### IsTeamAward

Boolean 0 or 1 that controls if the player receives the reputation not only to the faction but also the faction team.

-   0: Player receives reputation only for the faction
-   1: Player receives reputation both for the faction and the faction's team

NOTE: The reputation value that the player gains for the team (if the field is 1) is half of the value specified in [RewOnKillRepValue](#creature_onkill_reputation-RewOnKillRepValue)

### RewOnKillRepValue

The reputation value that the player gains (or loses if it's negative) by killing the creature.

### TeamDependent

Boolean 0 or 1.

-   0: The creature will give reputation to the any player from both fields (RewOnKillRepFaction1 and RewOnKillRepFaction2) if both fields are non-zero.
-   1: The creature will award alliance players the reputation from RewOnKillRepFaction1 and will award horde players the reputation from RewOnKillRepFaction2
