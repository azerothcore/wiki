# character\_stats

[<-Back-to:Characters](database-characters.md)

**The \`character\_stats\` table**

This table holds information on all the stats regarding the character. Used for external applications such as websites.
See worldserver.conf: PlayerSave.Stats.\*

**Structure**

| Field                   | Type    | Attributes | Key | Null | Default | Extra | Comment                            |
|-------------------------|---------|------------|-----|------|---------|-------|------------------------------------|
| [guid][1]               | int(10) | unsigned   | PRI | NO   |         |       | Global Unique Identifier, Low part |
| [maxhealth][2]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower1][3]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower2][4]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower3][5]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower4][6]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower5][7]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower6][8]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [maxpower7][9]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [strength][10]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [agility][11]           | int(10) | unsigned   |     | NO   |         |       |                                    |
| [stamina][12]           | int(10) | unsigned   |     | NO   |         |       |                                    |
| [intellect][13]         | int(10) | unsigned   |     | NO   |         |       |                                    |
| [spirit][14]            | int(10) | unsigned   |     | NO   |         |       |                                    |
| [armor][15]             | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resHoly][16]           | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resFire][17]           | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resNature][18]         | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resFrost][19]          | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resShadow][20]         | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resArcane][21]         | int(10) | unsigned   |     | NO   |         |       |                                    |
| [blockPct][22]          | float   | unsigned   |     | NO   |         |       |                                    |
| [dodgePct][23]          | float   | unsigned   |     | NO   |         |       |                                    |
| [parryPct][24]          | float   | unsigned   |     | NO   |         |       |                                    |
| [critPct][25]           | float   | unsigned   |     | NO   |         |       |                                    |
| [rangedCritPct][26]     | float   | unsigned   |     | NO   |         |       |                                    |
| [spellCritPct][27]      | float   | unsigned   |     | NO   |         |       |                                    |
| [attackPower][28]       | int(10) | unsigned   |     | NO   |         |       |                                    |
| [rangedAttackPower][29] | int(10) | unsigned   |     | NO   |         |       |                                    |
| [spellPower][30]        | int(10) | unsigned   |     | NO   |         |       |                                    |
| [resilience][31]        | int(10) | unsigned   |     | NO   |         |       |                                    |

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

### dodgePct

Character's current dodge chance.

### parryPct

Character's current parry chance.

### critPct

Character's current crit chance.

### rangedCritPct

Character's current ranged crit chance.

### spellCritPct

Character's current spell crit chance.

### attackPower

Character's current attackpower.

### rangedAttackPower

Character's current ranged attackpower.

### spellPower

Character's current spellpower.

### resilience

Character's current resilience value.
