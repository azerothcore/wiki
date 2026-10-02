# character\_declinedname

[<-Back-to:Characters](database-characters)

**The \`character\_declinedname\` table**

Holds the declined (grammatical case) forms of character names. The Russian client creates them when `DeclinedNames` is enabled in worldserver.conf, which is also the default when the realm zone is Russian.

**Table: character\_declinedname's Structure**

| Field              | Type        | Attributes | Key | Null | Default | Extra | Comment                  |
| ------------------ | ----------- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [guid][1]          | INT         | UNSIGNED   | PRI | NO   | 0       |       | Global Unique Identifier |
| [genitive][2]      | VARCHAR(15) |            |     | NO   | ''      |       |                          |
| [dative][3]        | VARCHAR(15) |            |     | NO   | ''      |       |                          |
| [accusative][4]    | VARCHAR(15) |            |     | NO   | ''      |       |                          |
| [instrumental][5]  | VARCHAR(15) |            |     | NO   | ''      |       |                          |
| [prepositional][6] | VARCHAR(15) |            |     | NO   | ''      |       |                          |

[1]: #guid
[2]: #genitive
[3]: #dative
[4]: #accusative
[5]: #instrumental
[6]: #prepositional

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
