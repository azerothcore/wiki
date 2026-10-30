# character\_stats

[<-Back-to:Characters](database-characters)

**The \`character\_stats\` table**

This table holds information on all the stats regarding the character. Used for external applications such as websites.
See worldserver.conf: PlayerSave.Stats.\*

**Table: character\_stats's Structure**

| Field                                   | Type  |          | Null | Key | Default | Extra | Comment                            |
| :-------------------------------------- | :---- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [guid](#guid)                           | INT   | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier, Low part |
| [maxhealth](#maxhealth)                 | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower1](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower2](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower3](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower4](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower5](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower6](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [maxpower7](#maxpower)                  | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [strength](#strength)                   | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [agility](#agility)                     | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [stamina](#stamina)                     | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [intellect](#intellect)                 | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [spirit](#spirit)                       | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [armor](#armor)                         | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resHoly](#resholy)                     | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resFire](#resfire)                     | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resNature](#resnature)                 | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resFrost](#resfrost)                   | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resShadow](#resshadow)                 | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resArcane](#resarcane)                 | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [blockPct](#blockpct)                   | FLOAT |          | NO   |     | 0       |       |                                    |
| [dodgePct](#dodgepct)                   | FLOAT |          | NO   |     | 0       |       |                                    |
| [parryPct](#parrypct)                   | FLOAT |          | NO   |     | 0       |       |                                    |
| [critPct](#critpct)                     | FLOAT |          | NO   |     | 0       |       |                                    |
| [rangedCritPct](#rangedcritpct)         | FLOAT |          | NO   |     | 0       |       |                                    |
| [spellCritPct](#spellcritpct)           | FLOAT |          | NO   |     | 0       |       |                                    |
| [attackPower](#attackpower)             | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [rangedAttackPower](#rangedattackpower) | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [spellPower](#spellpower)               | INT   | UNSIGNED | NO   |     | 0       |       |                                    |
| [resilience](#resilience)               | INT   | UNSIGNED | NO   |     | 0       |       |                                    |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### maxhealth

Maximum amount of health that the character has.

### maxpower

| Value | Description |
| ----- | ----------- |
| 1     | mana        |
| 2     | rage        |
| 3     | focus       |
| 4     | energy      |
| 5     | happiness   |
| 6     | rune        |
| 7     | runic power |

### strength

Character's current strength value.

### agility

Character's current agility value.

### stamina

Character's current stamina value.

### intellect

Character's current intellect value.

### spirit

Character's current spirit value.

### armor

Character's current armor value.

### resHoly

Character's current holy resistance value.

### resFire

Character's current fire resistance value.

### resNature

Character's current nature resistance value.

### resFrost

Character's current frost resistance value.

### resShadow

Character's current shadow resistance value.

### resArcane

Character's current arcane resistance value.

### blockPct

Character's current block chance.

Value must be >=0. If the value does not meet the condition the SQL will fail on `character_stats_chk_1`.

### dodgePct

Character's current dodge chance.

Value must be >=0. If the value does not meet the condition the SQL will fail on `character_stats_chk_1`.

### parryPct

Character's current parry chance.

Value must be >=0. If the value does not meet the condition the SQL will fail on `character_stats_chk_1`.

### critPct

Character's current crit chance.

Value must be >=0. If the value does not meet the condition the SQL will fail on `character_stats_chk_1`.

### rangedCritPct

Character's current ranged crit chance.

Value must be >=0. If the value does not meet the condition the SQL will fail on `character_stats_chk_1`.

### spellCritPct

Character's current spell crit chance.

Value must be >=0. If the value does not meet the condition the SQL will fail on `character_stats_chk_1`.

### attackPower

Character's current attackpower.

### rangedAttackPower

Character's current ranged attackpower.

### spellPower

Character's current spellpower.

### resilience

Character's current resilience value.
