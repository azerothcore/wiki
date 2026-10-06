# character\_declinedname

[<-Back-to:Characters](database-characters)

**The \`character\_declinedname\` table**

Holds the declined (grammatical case) forms of character names. The Russian client creates them when `DeclinedNames` is enabled in worldserver.conf, which is also the default when the realm zone is Russian.

**Table: character\_declinedname's Structure**

| Field                           | Type        |          | Null | Key | Default | Extra | Comment                  |
| :------------------------------ | :---------- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)                   | INT         | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [genitive](#genitive)           | VARCHAR(15) |          | NO   |     | ''      |       |                          |
| [dative](#dative)               | VARCHAR(15) |          | NO   |     | ''      |       |                          |
| [accusative](#accusative)       | VARCHAR(15) |          | NO   |     | ''      |       |                          |
| [instrumental](#instrumental)   | VARCHAR(15) |          | NO   |     | ''      |       |                          |
| [prepositional](#prepositional) | VARCHAR(15) |          | NO   |     | ''      |       |                          |

**Description of the table's fields**

### guid

GUID of the character. See [characters.guid](characters#guid).

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
