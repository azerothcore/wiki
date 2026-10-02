# spell\_pet\_auras

[<-Back-to:World](database-world)

**The \`spell\_pet\_auras\` table**

Auras that a spell of the owner applies to their pet, for example talents that improve the pet.

**Table: spell\_pet\_auras's Structure**

| Field         | Type    | Attributes | Key | Null | Default | Extra | Comment         |
| ------------- | ------- | ---------- | --- | ---- | ------- | ----- | --------------- |
| [spell][1]    | INT     | UNSIGNED   | PRI | NO   |         |       | dummy spell id  |
| [effectId][2] | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |                 |
| [pet][3]      | INT     | UNSIGNED   | PRI | NO   | 0       |       | pet id; 0 = all |
| [aura][4]     | INT     | UNSIGNED   |     | NO   |         |       | pet aura id     |

[1]: #spell
[2]: #effectid
[3]: #pet
[4]: #aura

**Description of the table's fields**

### spell

The spell of the owner. It must have a dummy effect or a dummy aura.

### effectId

The effect of the spell that applies the pet aura.

### pet

Entry of the pet that gets the aura. 0 for all pets. See [creature\_template.entry](creature_template#entry).

### aura

The aura applied to the pet.
