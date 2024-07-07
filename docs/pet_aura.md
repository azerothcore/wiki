# pet\_aura

[<-Back-to:Characters](database-characters)

**The \`pet\_aura\` table**

**Table Structure**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                       |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [guid][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier      |
| [casterGuid][2]      | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       | Full Global Unique Identifier |
| [spell][3]           | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [effectMask][4]      | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [recalculateMask][5] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |
| [stackCount][6]      | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                               |
| [amount0][7]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [amount1][8]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [amount2][9]         | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount0][10]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount1][11]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [base_amount2][12]   | MEDIUMINT | SIGNED     |     | NO   |         |       |                               |
| [maxDuration][13]    | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainTime][14]     | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainCharges][15]  | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |

[1]: #guid
[2]: #casterguid
[3]: #spell
[4]: #effectmask
[5]: #recalculatemask
[6]: #stackcount
[7]: #amount
[8]: #amount
[9]: #amount
[10]: #baseamount
[11]: #baseamount
[12]: #baseamount
[13]: #maxduration
[14]: #remaintime
[15]: #remaincharges

**Description of the fields**

### guid

The GUID of the target affected by the aura. See [character\_pet.id](character_pet#id).

### casterGuid

The GUID of the player who casted the aura. See [characters.guid](characters#guid).

### spell

The spell from which the aura was applied. See [Spell.dbc](spell) column 1.

### effectMask

The effect index of the spell from which the aura came from. A spell has up to three effects, with the index being 0, 1, or 2.

### recalculateMask

`field-no-description|5`

### stackCount

Determines how many stacks of the spell the character has.

### amount

The modifier value associated with the aura.

### base\_amount

`field-no-description|10-12`

### maxDuration

The maximum duration of the aura.

### remainTime

The time remaining in seconds on the aura. -1 means that the aura is indefinite.

### remainCharges

The number of charges remaining on the aura.
