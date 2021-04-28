# pet\_aura

[<-Back-to:Characters](database-characters.md)

**The \`pet\_aura\` table**

`table-no-description`

**Structure**

| Field                 | Type         | Attributes | Key | Null | Default | Extra | Comment                       |
|-----------------------|--------------|------------|-----|------|---------|-------|-------------------------------|
| [guid][1]             | int(10)      | unsigned   |     | NO   |         |       | Global Unique Identifier      |
| [caster_guid][2]      | BIGINT(20)   | unsigned   |     | NO   |         |       | Full Global Unique Identifier |
| [spell][3]            | MEDIUMINT(8) | unsigned   |     | NO   |         |       |                               |
| [effect_mask][4]      | TINYINT(3)   | unsigned   |     | NO   |         |       |                               |
| [recalculate_mask][5] | TINYINT(3)   | unsigned   |     | NO   |         |       |                               |
| [stackcount][6]       | TINYINT(3)   | unsigned   |     | NO   |         |       |                               |
| [amount0][7]          | MEDIUMINT(8) | signed     |     | NO   |         |       |                               |
| [amount1][8]          | MEDIUMINT(8) | signed     |     | NO   |         |       |                               |
| [amount2][9]          | MEDIUMINT(8) | signed     |     | NO   |         |       |                               |
| [base_amount0][10]    | MEDIUMINT(8) | signed     |     | NO   |         |       |                               |
| [base_amount1][11]    | MEDIUMINT(8) | signed     |     | NO   |         |       |                               |
| [base_amount2][12]    | MEDIUMINT(8) | signed     |     | NO   |         |       |                               |
| [maxduration][13]     | int(11)      | signed     |     | NO   |         |       |                               |
| [remaintime][14]      | int(11)      | signed     |     | NO   |         |       |                               |
| [remaincharges][15]   | TINYINT(3)   | unsigned   |     | NO   |         |       |                               |

[1]: #guid
[2]: #caster_guid
[3]: #spell
[4]: #effect_mask
[5]: #recalculate_mask
[6]: #stackcount
[7]: #amount0
[8]: #amount1
[9]: #amount2
[10]: #base_amount0
[11]: #base_amount1
[12]: #base_amount2
[13]: #maxduration
[14]: #remaintime
[15]: #remaincharges

**Description of the fields**

### guid

The GUID of the target affected by the aura. See character\_pet.id

### caster\_guid

The GUID of the player who casted the aura. See characters.guid

### spell

The spell from which the aura was applied. See Spell.dbc column 1

### effect\_mask

The effect index of the spell from which the aura came from. A spell has up to three effects, with the index being 0, 1, or 2.

### recalculate\_mask

`field-no-description|5`

### stackcount

Determines how many stacks of the spell the character has.

### amount

The modifier value associated with the aura.

### base\_amount

`field-no-description|8`

### maxduration

The maximum duration of the aura.

### remaintime

The time remaining in seconds on the aura. -1 means that the aura is indefinite.

### remaincharges

The number of charges remaining on the aura.
