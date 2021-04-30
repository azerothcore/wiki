# character\_aura

[<-Back-to:Characters](database-characters.md)

**The \`character\_aura\` table**

Contains aura information that is loaded when a character is loaded, so the auras that were on the character when it logged out are still kept when it logs back in. A spell can have up to three auras, one in each of its effects.

**Structure**

| Field                 | Type         | Attributes | Key | Null | Default | Extra | Comment                       |
|-----------------------|--------------|------------|-----|------|---------|-------|-------------------------------|
| [guid][1]             | INT      | UNSIGNED   | PRI | NO   |         |       | Global Unique Identifier      |
| [caster_guid][2]      | BIGINT   | UNSIGNED   | PRI | NO   |         |       | Full Global Unique Identifier |
| [item_guid][3]        | BIGINT   | UNSIGNED   | PRI | NO   |         |       |                               |
| [spell][4]            | MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |                               |
| [effect_mask][5]      | TINYINT   | UNSIGNED   | PRI | NO   |         |       |                               |
| [recalculate_mask][6] | TINYINT   | UNSIGNED   |     | NO   |         |       |                               |
| [stackcount][7]       | TINYINT   | UNSIGNED   |     | NO   |         |       |                               |
| [amount0][8]          | INT      | SIGNED     |     | NO   |         |       |                               |
| [amount1][9]          | INT      | SIGNED     |     | NO   |         |       |                               |
| [amount2][10]         | INT      | SIGNED     |     | NO   |         |       |                               |
| [base_amount0][11]    | INT      | SIGNED     |     | NO   |         |       |                               |
| [base_amount1][12]    | INT      | SIGNED     |     | NO   |         |       |                               |
| [base_amount2][13]    | INT      | SIGNED     |     | NO   |         |       |                               |
| [maxduration][14]     | INT      | SIGNED     |     | NO   |         |       |                               |
| [remaintime][15]      | INT      | SIGNED     |     | NO   |         |       |                               |
| [remaincharges][16]   | TINYINT   | UNSIGNED   |     | NO   |         |       |                               |

[1]: #guid
[2]: #caster_guid
[3]: #item_guid
[4]: #spell
[5]: #effect_mask
[6]: #recalculate_mask
[7]: #stackcount
[8]: #amount0
[9]: #amount1
[10]: #amount2
[11]: #base_amount0
[12]: #base_amount1
[13]: #base_amount2
[14]: #maxduration
[15]: #remaintime
[16]: #remaincharges

**Description of the fields**

### guid

The GUID of the target affected by the aura. See characters.guid

### caster\_guid

The GUID of the player who casted the aura. See characters.guid

### item\_guid

The GUID of the item which casted the aura. See item\_instance.guid

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

The maximum duration of the aura in ms.

### remaintime

The time remaining in ms on the aura. -1 means that the aura is indefinite.

### remaincharges

The number of charges remaining on the aura.
