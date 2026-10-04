# world\_state

[<-Back-to:Characters](database-characters)

**The \`world\_state\` table**

Persists server-wide world state values so they survive restarts. Each row holds a serialized blob of world-state data keyed by an internal save `Id`.

**Table: world\_state's Structure**

| Field         | Type     |          | Null | Key | Default | Extra | Comment          |
| :------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :--------------- |
| [Id](#id)     | INT      | UNSIGNED | NO   | PRI |         |       | Internal save ID |
| [Data](#data) | LONGTEXT |          | YES  |     | NULL    |       |                  |

**Description of the table's fields**

### Id

Internal world-state save identifier.

### Data

Serialized world-state payload.
