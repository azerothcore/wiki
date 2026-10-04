# spell\_pet\_auras

[<-Back-to:World](database-world)

**The \`spell\_pet\_auras\` table**

Auras that a spell of the owner applies to their pet, for example talents that improve the pet.

**Table: spell\_pet\_auras's Structure**

| Field                 | Type    |          | Null | Key | Default | Extra | Comment         |
| :-------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :-------------- |
| [spell](#spell)       | INT     | UNSIGNED | NO   | PRI |         |       | dummy spell id  |
| [effectId](#effectid) | TINYINT | UNSIGNED | NO   | PRI | 0       |       |                 |
| [pet](#pet)           | INT     | UNSIGNED | NO   | PRI | 0       |       | pet id; 0 = all |
| [aura](#aura)         | INT     | UNSIGNED | NO   |     |         |       | pet aura id     |

**Description of the table's fields**

### spell

The spell of the owner. It must have a dummy effect or a dummy aura.

### effectId

The effect of the spell that applies the pet aura.

### pet

Entry of the pet that gets the aura. 0 for all pets. See [creature\_template.entry](creature_template#entry).

### aura

The aura applied to the pet.
