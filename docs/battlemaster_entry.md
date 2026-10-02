# battlemaster\_entry

[<-Back-to:World](database-world)

**The \`battlemaster\_entry\` table**

Holds information on which NPC can start what battleground or arena.

**Table: battlemaster\_entry's Structure**

| Field            | Type | Attributes | Key | Null | Default | Extra | Comment                  |
| ---------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------------------------ |
| [entry][1]       | INT  | UNSIGNED   | PRI | NO   | 0       |       | Entry of a creature      |
| [bg_template][2] | INT  | UNSIGNED   |     | NO   | 0       |       | Battleground template id |

[1]: #entry
[2]: #bgtemplate

**Description of the table's fields**

### entry

The ID of the creature. See creature\_template.entry

### bg\_template

The battleground\_template.id.
