# character\_pet

[<-Back-to:Characters](database-characters)

**The \`character\_pet\` table**

This table holds the pet data for each pet summoned by anyone in the game.

**Table Structure**

| Field               | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]             | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [entry][2]          | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [owner][3]          | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [modelid][4]        | INT         | UNSIGNED   |     | YES  | 0       |       |         |
| [CreatedBySpell][5] | MEDIUMINT   | UNSIGNED   |     | NO   | 0       |       |         |
| [PetType][6]        | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [level][7]          | SMALLINT    | UNSIGNED   |     | NO   | 0       |       |         |
| [exp][8]            | INT         | UNSIGNED   |     | NO   | 1       |       |         |
| [Reactstate][9]     | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [name][10]          | VARCHAR(21) | SIGNED     |     | NO   | 0       |       |         |
| [renamed][11]       | TINYINT     | UNSIGNED   |     | NO   | Pet     |       |         |
| [slot][12]          | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |
| [curhealth][13]     | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [curmana][14]       | INT         | UNSIGNED   |     | NO   | 1       |       |         |
| [curhappiness][15]  | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [savetime][16]      | INT         | UNSIGNED   |     | NO   | 0       |       |         |
| [abdata][17]        | TEXT        | SIGNED     |     | YES  | 0       |       |         |

[1]: #id
[2]: #entry
[3]: #owner
[4]: #modelid
[5]: #createdbyspell
[6]: #pettype
[7]: #level
[8]: #exp
[9]: #reactstate
[10]: #name
[11]: #renamed
[12]: #slot
[13]: #curhealth
[14]: #curmana
[15]: #curhappiness
[16]: #savetime
[17]: #abdata

**Description of the fields**

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

`field-no-description|17`
