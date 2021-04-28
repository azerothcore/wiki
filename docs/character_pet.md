# character\_pet

[<-Back-to:Characters](database-characters.md)

**The \`character\_pet\` table**

This table holds the pet data for each pet summoned by anyone in the game.

**Structure**

| Field                   | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-------------------------|--------------|------------|-----|------|---------|-------|---------|
| [id][1]                 | int(10)      | unsigned   | PRI | NO   |         |       |         |
| [entry][2]              | int(10)      | unsigned   |     | NO   |         |       |         |
| [owner][3]              | int(10)      | unsigned   |     | NO   |         |       |         |
| [modelid][4]            | int(10)      | unsigned   |     | YES  | 0       |       |         |
| [CreatedBySpell][5]     | MEDIUMINT(8) | unsigned   |     | NO   |         |       |         |
| [PetType][6]            | tinyint(3)   | unsigned   |     | NO   |         |       |         |
| [level][7]              | SMALLINT(5)  | unsigned   |     | NO   |         |       |         |
| [exp][8]                | int(10)      | unsigned   |     | NO   |         |       |         |
| [Reactstate][9]         | tinyint(3)   | unsigned   |     | NO   |         |       |         |
| [name][10]              | VARCHAR(21)  |            |     | NO   |         |       |         |
| [renamed][11]           | tinyint(3)   | unsigned   |     | NO   |         |       |         |
| [slot][12]              | tinyint(3)   | unsigned   |     | NO   |         |       |         |
| [curhealth][13]         | int(10)      | unsigned   |     | NO   |         |       |         |
| [curmana][14]           | int(10)      | unsigned   |     | NO   |         |       |         |
| [curhappiness][15]      | int(10)      | unsigned   |     | NO   |         |       |         |
| [savetime][16]          | int(10)      | unsigned   |     | NO   |         |       |         |
| [resettalents_cost][17] | int(10)      | unsigned   |     | NO   |         |       |         |
| [resettalents_time][18] | int(10)      | unsigned   |     | NO   |         |       |         |
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
