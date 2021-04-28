# character\_pet

[<-Back-to:Characters](database-characters.md)

**The \`character\_pet\` table**

This table holds the pet data for each pet summoned by anyone in the game.

**Structure**

| Field                   | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------------------|--------------|------------|-----|------|---------|-------|---------|
| [id][1]                 | INT(10)      | UNSIGNED   | PRI | NO   |         |       |         |
| [entry][2]              | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [owner][3]              | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [modelid][4]            | INT(10)      | UNSIGNED   |     | YES  | 0       |       |         |
| [CreatedBySpell][5]     | MEDIUMINT(8) | UNSIGNED   |     | NO   |         |       |         |
| [PetType][6]            | TINYINT(3)   | UNSIGNED   |     | NO   |         |       |         |
| [level][7]              | SMALLINT(5)  | UNSIGNED   |     | NO   |         |       |         |
| [exp][8]                | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [Reactstate][9]         | TINYINT(3)   | UNSIGNED   |     | NO   |         |       |         |
| [name][10]              | VARCHAR(21)  |            |     | NO   |         |       |         |
| [renamed][11]           | TINYINT(3)   | UNSIGNED   |     | NO   |         |       |         |
| [slot][12]              | TINYINT(3)   | UNSIGNED   |     | NO   |         |       |         |
| [curhealth][13]         | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [curmana][14]           | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [curhappiness][15]      | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [savetime][16]          | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [resettalents_cost][17] | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [resettalents_time][18] | INT(10)      | UNSIGNED   |     | NO   |         |       |         |
| [abdata][19]            | text         |            |     | YES  | NULL    |       |         |

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
[17]: #resettalents_cost
[18]: #resettalents_time
[19]: #abdata

**Description of the fields**

### id

The special pet ID. This is a unique identifier among all pets.

### entry

The creature entry of this pet. See creature\_template.entry

### owner

The GUID of the pet's owner. See characters.guid

### modelid

The model ID to use to display the pet.

### CreatedBySpell

The ID of the spell that has created this pet. For hunters, this is usually the Tame Beast spell. For warlocks or other classes (mages), it is the spell ID that summoned the creature. See Spell.dbc column 1

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

### resettalents\_cost

The cost for the character to reset pet's talents, measured in copper.

### resettalents\_time

The date when the talents were reset, in Unix time.

### abdata

`field-no-description|19`
