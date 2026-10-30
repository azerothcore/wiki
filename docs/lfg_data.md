# lfg\_data

[<-Back-to:Characters](database-characters)

**The \`lfg\_data\` table**

This table contains saved data for LFG. This table is constantly in use by the core.

**Table: lfg\_data's Structure**

| Field               | Type    |          | Null | Key | Default | Extra | Comment                  |
| :------------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :----------------------- |
| [guid](#guid)       | INT     | UNSIGNED | NO   | PRI | 0       |       | Global Unique Identifier |
| [dungeon](#dungeon) | INT     | UNSIGNED | NO   |     | 0       |       |                          |
| [state](#state)     | TINYINT | UNSIGNED | NO   |     | 0       |       |                          |

**Description of the table's fields**

### guid

The guid for this group.

### dungeon

The dungeon ID from dbc.

### state

The state for this group/dungeon.
