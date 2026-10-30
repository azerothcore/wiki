# character\_pet

[<-Back-to:Characters](database-characters)

**The \`character\_pet\` table**

This table holds the pet data for each pet summoned by anyone in the game.

**Table: character\_pet's Structure**

| Field                             | Type        |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)                         | INT         | UNSIGNED | NO   | PRI | 0       |       |         |
| [entry](#entry)                   | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [owner](#owner)                   | INT         | UNSIGNED | NO   | MUL | 0       |       |         |
| [modelid](#modelid)               | INT         | UNSIGNED | YES  |     | 0       |       |         |
| [CreatedBySpell](#createdbyspell) | INT         | UNSIGNED | YES  |     | 0       |       |         |
| [PetType](#pettype)               | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [level](#level)                   | SMALLINT    | UNSIGNED | NO   |     | 1       |       |         |
| [exp](#exp)                       | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [Reactstate](#reactstate)         | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [name](#name)                     | VARCHAR(21) |          | NO   |     | Pet     |       |         |
| [renamed](#renamed)               | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |
| [slot](#slot)                     | TINYINT     | UNSIGNED | NO   | MUL | 0       |       |         |
| [curhealth](#curhealth)           | INT         | UNSIGNED | NO   |     | 1       |       |         |
| [curmana](#curmana)               | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [curhappiness](#curhappiness)     | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [savetime](#savetime)             | INT         | UNSIGNED | NO   |     | 0       |       |         |
| [abdata](#abdata)                 | TEXT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### id

The special pet ID. This is a unique identifier among all pets.

### entry

The creature entry of this pet. See [creature\_template.entry](creature_template#entry).

### owner

The GUID of the pet's owner. See [characters.guid](characters#guid).

### modelid

The model ID to use to display the pet.

### CreatedBySpell

The ID of the spell that has created this pet. For hunters, this is usually the Tame Beast spell. For warlocks or other classes (mages), it is the spell ID that summoned the creature. See [Spell.dbc](spell) column 1.

### PetType

The type of pet that this is. 0 = summoned pet, 1 = tamed pet

### level

The current level of the pet.

### exp

The current experience that this pet has. For summoned pets, this field is always 0.

### Reactstate

The current reaction state of the pet (passive, aggressive, etc).

### name

The pet's name.

### renamed

Boolean 1 or 0. 1 = Pet has been renamed, 0 = Pet has never been renamed and still uses the same name as the creature that was tamed.

### slot

- The pet slot that the pet is in.
- The slot is 0 for the active pet, which is with the player;
- 1-4 for pets in stable (slot 1-4)
- 100 for a pet which is with the player but currently dismissed.

### curhealth

The current pet health at the time it was saved to DB.

### curmana

The current pet mana at the time it was saved to DB.

### curhappiness

The current pet happiness.

### savetime

The time when the pet was last saved, in Unix time.

### abdata

The action bar of the pet. Ten pairs of `type action` separated by spaces, one pair per button: the type of the button and the spell or command on it.
