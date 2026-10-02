# character\_pet\_declinedname

[<-Back-to:Characters](database-characters)

**The \`character\_pet\_declinedname\` table**

**Table: character\_pet\_declinedname's Structure**

| Field              | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id][1]            | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [owner][2]         | INT         | UNSIGNED   | MUL | NO   | 0       |       |         |
| [genitive][3]      | VARCHAR(12) |            |     | NO   | ''      |       |         |
| [dative][4]        | VARCHAR(12) |            |     | NO   | ''      |       |         |
| [accusative][5]    | VARCHAR(12) |            |     | NO   | ''      |       |         |
| [instrumental][6]  | VARCHAR(12) |            |     | NO   | ''      |       |         |
| [prepositional][7] | VARCHAR(12) |            |     | NO   | ''      |       |         |

[1]: #id
[2]: #owner
[3]: #genitive
[4]: #dative
[5]: #accusative
[6]: #instrumental
[7]: #prepositional

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
