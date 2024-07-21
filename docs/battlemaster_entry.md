# battlemaster\_entry

[<-Back-to:World](database-world)

**The \`battlemaster\_entry\` table**

Holds information on which NPC can start what battleground or arena.

**Table Structure**

| Field            | Type      | Attributes | Key | Null | Default | Extra | Comment                 |
| ---------------- | --------- | ---------- | --- | ---- | ------- | ----- | ----------------------- |
| [entry][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       | Entry of a creature     |
| [bg_template][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       | Batleground template id |

[1]: #entry
[2]: #bg_template

**Description of the fields**

### entry

The ID of the creature. See creature\_template.entry

### bg\_template

The battleground\_template.id.
