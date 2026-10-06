# character\_pet\_declinedname

[<-Back-to:Characters](database-characters)

**The \`character\_pet\_declinedname\` table**

Holds the declined (grammatical case) forms of pet names. The Russian client creates them when `DeclinedNames` is enabled in worldserver.conf, which is also the default when the realm zone is Russian.

**Table: character\_pet\_declinedname's Structure**

| Field                           | Type        |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)                       | INT         | UNSIGNED | NO   | PRI | 0       |       |         |
| [owner](#owner)                 | INT         | UNSIGNED | NO   | MUL | 0       |       |         |
| [genitive](#genitive)           | VARCHAR(12) |          | NO   |     | ''      |       |         |
| [dative](#dative)               | VARCHAR(12) |          | NO   |     | ''      |       |         |
| [accusative](#accusative)       | VARCHAR(12) |          | NO   |     | ''      |       |         |
| [instrumental](#instrumental)   | VARCHAR(12) |          | NO   |     | ''      |       |         |
| [prepositional](#prepositional) | VARCHAR(12) |          | NO   |     | ''      |       |         |

**Description of the table's fields**

### id

ID of the pet. See [character\_pet.id](character_pet#id).

### owner

GUID of the character that owns the pet. See [characters.guid](characters#guid).

### genitive

The name in the genitive case.

### dative

The name in the dative case.

### accusative

The name in the accusative case.

### instrumental

The name in the instrumental case.

### prepositional

The name in the prepositional case.
