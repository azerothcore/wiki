# creature\_onkill\_reputation

[<-Back-to:World](database-world)

**The \`creature\_onkill\_reputation\` table**

This table controls the reputation given by creatures when killed by other players.

**Table: creature\_onkill\_reputation's Structure**

| Field                                        | Type     |          | Null | Key | Default | Extra | Comment             |
| :------------------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------------------ |
| [creature_id](#creatureid)                   | INT      | UNSIGNED | NO   | PRI | 0       |       | Creature Identifier |
| [RewOnKillRepFaction1](#rewonkillrepfaction) | SMALLINT |          | NO   |     | 0       |       |                     |
| [RewOnKillRepFaction2](#rewonkillrepfaction) | SMALLINT |          | NO   |     | 0       |       |                     |
| [MaxStanding1](#maxstanding)                 | TINYINT  |          | NO   |     | 0       |       |                     |
| [IsTeamAward1](#isteamaward)                 | TINYINT  |          | NO   |     | 0       |       |                     |
| [RewOnKillRepValue1](#rewonkillrepvalue)     | FLOAT    |          | NO   |     | 0       |       |                     |
| [MaxStanding2](#maxstanding)                 | TINYINT  |          | NO   |     | 0       |       |                     |
| [IsTeamAward2](#isteamaward)                 | TINYINT  |          | NO   |     | 0       |       |                     |
| [RewOnKillRepValue2](#rewonkillrepvalue)     | FLOAT    |          | NO   |     | 0       |       |                     |
| [TeamDependent](#teamdependent)              | TINYINT  | UNSIGNED | NO   |     | 0       |       |                     |

**Description of the table's fields**

### creature\_id

The template ID of the creature. See [creature\_template.entry](creature_template#entry)

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

NOTE: The reputation value that the player gains for the team (if the field is 1) is half of the value specified in [RewOnKillRepValue](#rewonkillrepvalue)

### RewOnKillRepValue

The reputation value that the player gains (or loses if it's negative) by killing the creature.

### TeamDependent

Boolean 0 or 1.

-   0: The creature will give reputation to the any player from both fields (RewOnKillRepFaction1 and RewOnKillRepFaction2) if both fields are non-zero.
-   1: The creature will award alliance players the reputation from RewOnKillRepFaction1 and will award horde players the reputation from RewOnKillRepFaction2
