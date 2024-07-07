# character\_aura

[<-Back-to:Characters](database-characters)

**The \`character\_aura\` table**

Contains aura information that is loaded when a character is loaded, so the auras that were on the character when it logged out are still kept when it logs back in. A spell can have up to three auras, one in each of its effects.

**Table Structure**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                       |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------------- |
| [guid][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier      |
| [casterGuid][2]      | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       | Full Global Unique Identifier |
| [itemGuid][3]        | BIGINT    | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [spell][4]           | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [effectMask][5]      | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |                               |
| [recalculateMask][6] | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |
| [stackCount][7]      | TINYINT   | UNSIGNED   |     | NO   | 1       |       |                               |
| [amount0][8]         | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [amount1][9]         | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [amount2][10]        | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [base_amount0][11]   | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [base_amount1][12]   | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [base_amount2][13]   | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [maxDuration][14]    | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainTime][15]     | INT       | SIGNED     |     | NO   | 0       |       |                               |
| [remainCharges][16]  | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                               |

[1]: #guid
[2]: #casterguid
[3]: #itemguid
[4]: #spell
[5]: #effectmask
[6]: #recalculatemask
[7]: #stackcount
[8]: #amount
[9]: #amount
[10]: #amount
[11]: #baseamount0
[12]: #baseamount1
[13]: #baseamount2
[14]: #maxduration
[15]: #remaintime
[16]: #remaincharges

**Description of the fields**

### guid

The GUID of the target affected by the aura. See [characters.guid](characters#guid).

### casterGuid

The GUID of the player who casted the aura. See [characters.guid](characters#guid).

### itemGuid

The GUID of the item which casted the aura. See [item\_instance.guid](item\_instance#guid).

### spell

The spell from which the aura was applied. See [Spell.dbc](spell) column 1.

### effectMask

The effect index of the spell from which the aura came from. A spell has up to three effects, with the index being 0, 1, or 2.

### recalculateMask

`field-no-description|5`

### stackcount

Determines how many stacks of the spell the character has.

### amount

The modifier value associated with the aura.

### base\_amount0

`field-no-description|11`

### base\_amount1

`field-no-description|12`

### base\_amount2

`field-no-description|13`

### maxduration

The maximum duration of the aura in ms.

### remaintime

The time remaining in ms on the aura. -1 means that the aura is indefinite.

### remaincharges

The number of charges remaining on the aura.
