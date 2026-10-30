# character\_aura

[<-Back-to:Characters](database-characters)

**The \`character\_aura\` table**

Contains aura information that is loaded when a character is loaded, so the auras that were on the character when it logged out are still kept when it logs back in. A spell can have up to three auras, one in each of its effects.

**Table: character\_aura's Structure**

| Field                               | Type    |          | Null | Key | Default | Extra | Comment                       |
| :---------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------------- |
| [guid](#guid)                       | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier      |
| [casterGuid](#casterguid)           | BIGINT  | UNSIGNED | NO   | PRI | 0       |       | Full Global Unique Identifier |
| [itemGuid](#itemguid)               | BIGINT  | UNSIGNED | NO   | PRI | 0       |       |                               |
| [spell](#spell)                     | INT     | UNSIGNED | NO   | PRI | 0       |       |                               |
| [effectMask](#effectmask)           | TINYINT | UNSIGNED | NO   | PRI | 0       |       |                               |
| [recalculateMask](#recalculatemask) | TINYINT | UNSIGNED | NO   |     | 0       |       |                               |
| [stackCount](#stackcount)           | TINYINT | UNSIGNED | NO   |     | 1       |       |                               |
| [amount0](#amount)                  | INT     |          | NO   |     | 0       |       |                               |
| [amount1](#amount)                  | INT     |          | NO   |     | 0       |       |                               |
| [amount2](#amount)                  | INT     |          | NO   |     | 0       |       |                               |
| [base_amount0](#baseamount0)        | INT     |          | NO   |     | 0       |       |                               |
| [base_amount1](#baseamount1)        | INT     |          | NO   |     | 0       |       |                               |
| [base_amount2](#baseamount2)        | INT     |          | NO   |     | 0       |       |                               |
| [maxDuration](#maxduration)         | INT     |          | NO   |     | 0       |       |                               |
| [remainTime](#remaintime)           | INT     |          | NO   |     | 0       |       |                               |
| [remainCharges](#remaincharges)     | TINYINT | UNSIGNED | NO   |     | 0       |       |                               |

**Description of the table's fields**

### guid

The GUID of the target affected by the aura. See [characters.guid](characters#guid).

### casterGuid

The GUID of the player who casted the aura. See [characters.guid](characters#guid).

### itemGuid

The GUID of the item which casted the aura. See [item\_instance.guid](item_instance#guid).

### spell

The spell from which the aura was applied. See [Spell.dbc](spell) column 1.

### effectMask

The effect index of the spell from which the aura came from. A spell has up to three effects, with the index being 0, 1, or 2.

### recalculateMask

Bitmask of the aura effects whose amount is recalculated, one bit per effect index.

### stackcount

Determines how many stacks of the spell the character has.

### amount

The modifier value associated with the aura.

### base\_amount0

The base amount of the first effect of the aura.

### base\_amount1

The base amount of the second effect of the aura.

### base\_amount2

The base amount of the third effect of the aura.

### maxduration

The maximum duration of the aura in ms.

### remaintime

The time remaining in ms on the aura. -1 means that the aura is indefinite.

### remaincharges

The number of charges remaining on the aura.
