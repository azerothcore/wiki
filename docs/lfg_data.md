# lfg\_data

[<-Back-to:Characters](database-characters.md)

**The \`lfg\_data\` table**

This table contains saved data for LFG. This table is constantly in use by the core.

**Structure**

| Field        | Type       | Attributes | Key | Null | Default | Extra | Comment                  |
|--------------|------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]    | int(10)    | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [dungeon][2] | int(10)    | unsigned   |     | NO   | 0       |       |                          |
| [state][3]   | tinyint(3) | unsigned   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #dungeon
[3]: #state

**Description of the fields**

### guid

The guid for this group.

### dungeon

The dungeon ID from dbc.

### state

The state for this group / dungeon.

Source: https://ascemu.github.io/Wiki/database/characters/lfg_data/
