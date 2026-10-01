# character\_stats

[<-返回:Characters](database-characters)

**\`character\_stats\` 表**

该表保存角色所有属性的相关信息。用于网站等外部应用程序。
参见 worldserver.conf 中的 PlayerSave.Stats.\*

**表结构**

| Field                   | Type  | Attributes | Key | Null | Default | Extra | Comment                            |
| ----------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]               | INT   | UNSIGNED   | PRI | NO   | 0       |       | 全局唯一标识符，低位部分           |
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

**字段说明**

### guid

角色 GUID。参见 [characters.guid](characters#guid)。

### maxhealth

角色拥有的最大生命值。

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

角色当前的力量值。

### agility

角色当前的敏捷值。

### stamina

角色当前的耐力值。

### intellect

角色当前的智力值。

### spirit

角色当前的精神值。

### armor

角色当前的护甲值。

### resHoly

角色当前的神圣抗性值。

### resFire

角色当前的火焰抗性值。

### resNature

角色当前的自然抗性值。

### resFrost

角色当前的冰霜抗性值。

### resShadow

角色当前的暗影抗性值。

### resArcane

角色当前的奥术抗性值。

### blockPct

角色当前的格挡几率。

该值必须 >=0。如果该值不满足条件，SQL 将在 \`character_stats_chk_1\` 上失败。

### dodgePct

角色当前的闪避几率。

该值必须 >=0。如果该值不满足条件，SQL 将在 \`character_stats_chk_1\` 上失败。

### parryPct

角色当前的招架几率。

该值必须 >=0。如果该值不满足条件，SQL 将在 \`character_stats_chk_1\` 上失败。

### critPct

角色当前的暴击几率。

该值必须 >=0。如果该值不满足条件，SQL 将在 \`character_stats_chk_1\` 上失败。

### rangedCritPct

角色当前的远程暴击几率。

该值必须 >=0。如果该值不满足条件，SQL 将在 \`character_stats_chk_1\` 上失败。

### spellCritPct

角色当前的法术暴击几率。

该值必须 >=0。如果该值不满足条件，SQL 将在 \`character_stats_chk_1\` 上失败。

### attackPower

角色当前的攻击强度。

### rangedAttackPower

角色当前的远程攻击强度。

### spellPower

角色当前的法术强度。

### resilience

角色当前的韧性值。
