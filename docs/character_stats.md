# character\_stats

[<-Back-to:Characters](database-characters)

**The \`character\_stats\` table**

This table holds information on all the stats regarding the character. Used for external applications such as websites.
See worldserver.conf: PlayerSave.Stats.\*

**Table Structure**

| Field                   | Type  | Attributes | Key | Null | Default | Extra | Comment                            |
| ----------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]               | INT   | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier, Low part |
| [maxhealth][2]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower1][3]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower2][4]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower3][5]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower4][6]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower5][7]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower6][8]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [maxpower7][9]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [strength][10]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [agility][11]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [stamina][12]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [intellect][13]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [spirit][14]            | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [armor][15]             | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resHoly][16]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resFire][17]           | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resNature][18]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resFrost][19]          | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resShadow][20]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resArcane][21]         | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [blockPct][22]          | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [dodgePct][23]          | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [parryPct][24]          | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [critPct][25]           | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [rangedCritPct][26]     | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [spellCritPct][27]      | FLOAT | SIGNED     |     | NO   | 0       |       |                                    |
| [attackPower][28]       | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [rangedAttackPower][29] | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [spellPower][30]        | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |
| [resilience][31]        | INT   | UNSIGNED   |     | NO   | 0       |       |                                    |

[1]: #guid
[2]: #maxhealth
[3]: #maxpower
[4]: #maxpower
[5]: #maxpower
[6]: #maxpower
[7]: #maxpower
[8]: #maxpower
[9]: #maxpower
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
