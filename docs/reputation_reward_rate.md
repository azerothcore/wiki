# reputation\_reward\_rate

[<-Back-to:World](database-world.md)

**The \`reputation\_reward\_rate\` table**

Holds reputation multipliers for specific factions.

**Structure**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------------|--------------|------------|-----|------|---------|-------|---------|
| [faction][1]       | MEDIUMINT(8) | unsigned   | PRI | NO   | 0       |       |         |
| [quest_rate][2]    | FLOAT        | signed     |     | NO   | 1       |       |         |
| [creature_rate][3] | FLOAT        | signed     |     | NO   | 1       |       |         |
| [spell_rate][4]    | FLOAT        | signed     |     | NO   | 1       |       |         |

[1]: #faction
[2]: #quest_rate
[3]: #creature_rate
[4]: #spell_rate

**Description of the fields**

### faction

The ID of the faction these rates apply to.

### quest\_rate

The rate for reputation gain from quests.

### creature\_rate

The rate for reputation gain from creatures.

### spell\_rate

The rate for reputation gain from spells.
