# pet\_aura

[<-Back-to:Characters](database-characters)

**The \`pet\_aura\` table**

Stores the auras a pet had when it was saved, so they can be restored when the pet is loaded again.

**Table: pet\_aura's Structure**

| Field                               | Type    |          | Null | Key | Default | Extra | Comment                       |
| :---------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :---------------------------- |
| [guid](#guid)                       | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier      |
| [casterGuid](#casterguid)           | BIGINT  | UNSIGNED | NO   | PRI | 0       |       | Full Global Unique Identifier |
| [spell](#spell)                     | INT     | UNSIGNED | NO   | PRI | 0       |       |                               |
| [effectMask](#effectmask)           | TINYINT | UNSIGNED | NO   | PRI | 0       |       |                               |
| [recalculateMask](#recalculatemask) | TINYINT | UNSIGNED | NO   |     | 0       |       |                               |
| [stackCount](#stackcount)           | TINYINT | UNSIGNED | NO   |     | 1       |       |                               |
| [amount0](#amount)                  | INT     |          | YES  |     | NULL    |       |                               |
| [amount1](#amount)                  | INT     |          | YES  |     | NULL    |       |                               |
| [amount2](#amount)                  | INT     |          | YES  |     | NULL    |       |                               |
| [base_amount0](#baseamount)         | INT     |          | YES  |     | NULL    |       |                               |
| [base_amount1](#baseamount)         | INT     |          | YES  |     | NULL    |       |                               |
| [base_amount2](#baseamount)         | INT     |          | YES  |     | NULL    |       |                               |
| [maxDuration](#maxduration)         | INT     |          | NO   |     | 0       |       |                               |
| [remainTime](#remaintime)           | INT     |          | NO   |     | 0       |       |                               |
| [remainCharges](#remaincharges)     | TINYINT | UNSIGNED | NO   |     | 0       |       |                               |

**Description of the table's fields**

### guid

The GUID of the target affected by the aura. See [character\_pet.id](character_pet#id).

### casterGuid

The GUID of the player who casted the aura. See [characters.guid](characters#guid).

### spell

The spell from which the aura was applied. See [Spell.dbc](spell) column 1.

### effectMask

The effect index of the spell from which the aura came from. A spell has up to three effects, with the index being 0, 1, or 2.

### recalculateMask

Bitmask of the aura effects whose amount is recalculated, one bit per effect index.

### stackCount

Determines how many stacks of the spell the character has.

### amount

The modifier value associated with the aura.

### base\_amount

The base amount of each effect of the aura.

### maxDuration

The maximum duration of the aura.

### remainTime

The time remaining in seconds on the aura. -1 means that the aura is indefinite.

### remainCharges

The number of charges remaining on the aura.
