# battlemaster\_entry

[<-Back-to:World](database-world)

**The \`battlemaster\_entry\` table**

Holds information on which NPC can start what battleground or arena.

**Table: battlemaster\_entry's Structure**

| Field                      | Type |          | Null | Key | Default | Extra | Comment                  |
| :------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [entry](#entry)            | INT  | UNSIGNED | NO   | PRI | 0       |       | Entry of a creature      |
| [bg_template](#bgtemplate) | INT  | UNSIGNED | NO   |     | 0       |       | Battleground template id |

**Description of the table's fields**

### entry

The ID of the creature. See creature\_template.entry

### bg\_template

The battleground\_template.id.
