# character\_stats

[<-Back-to:Characters](database-characters.md)

**The \`character\_stats\` table**

This table holds information on all the stats regarding the character. Used for external applications such as websites.
See worldserver.conf: PlayerSave.Stats.\*

**Structure**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment                            |
|-------------------------|---------|------------|-----|------|---------|-------|------------------------------------|
| [guid][1]               | INT(10) | unsigned   | PRI | NO   |         |       | Global Unique Identifier, Low part |
| [maxhealth][2]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower1][3]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower2][4]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower3][5]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower4][6]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower5][7]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower6][8]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower7][9]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [strength][10]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [agility][11]           | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [stamina][12]           | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [intellect][13]         | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [spirit][14]            | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [armor][15]             | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resHoly][16]           | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resFire][17]           | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resNature][18]         | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resFrost][19]          | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resShadow][20]         | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resArcane][21]         | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [blockPct][22]          | FLOAT   | unsigned   |     | NO   |         |       |                                    |
| [dodgePct][23]          | FLOAT   | unsigned   |     | NO   |         |       |                                    |
| [parryPct][24]          | FLOAT   | unsigned   |     | NO   |         |       |                                    |
| [critPct][25]           | FLOAT   | unsigned   |     | NO   |         |       |                                    |
| [rangedCritPct][26]     | FLOAT   | unsigned   |     | NO   |         |       |                                    |
| [spellCritPct][27]      | FLOAT   | unsigned   |     | NO   |         |       |                                    |
| [attackPower][28]       | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [rangedAttackPower][29] | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [spellPower][30]        | INT(10) | unsigned   |     | NO   |         |       |                                    |
| [resilience][31]        | INT(10) | unsigned   |     | NO   |         |       |                                    |

[1]: #guid
[2]: #maxhealth
[3]: #maxpower1
[4]: #maxpower2
[5]: #maxpower3
[6]: #maxpower4
[7]: #maxpower5
[8]: #maxpower6
[9]: #maxpower7
[10]: #strength
[11]: #agility
[12]: #stamina
[13]: #intellect
[14]: #spirit
[15]: #armor
[16]: #resholy
[17]: #resfire
[18]: #resnature
[19]: #resfrost
[20]: #resshadow
[21]: #resarcane
[22]: #blockpct
[23]: #dodgepct
[24]: #parrypct
[25]: #critpct
[26]: #rangedcritpct
[27]: #spellcritpct
[28]: #attackpower
[29]: #rangedattackpower
[30]: #spellpower
[31]: #resilience

**Description of the fields**

### guid

The guid of the character.

### maxhealth

Maximum amount of health that the character has.

### maxpower

| Value | Description |
|-------|-------------|
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
