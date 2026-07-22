# playercreateinfo_cast_spell

[<-Back-to:World](database-world)

**The `playercreateinfo_cast_spell` table**

Defines spells that are cast on a character immediately upon creation, filtered by race and class bitmasks. This complements [playercreateinfo_spell_custom](playercreateinfo_spell_custom), which grants spells as *known* rather than casting them.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [raceMask](#racemask) | INT | UNSIGNED |  | NO | 0 |  |  |
| [classMask](#classmask) | INT | UNSIGNED |  | NO | 0 |  |  |
| [spell](#spell) | INT | UNSIGNED |  | NO | 0 |  |  |
| [note](#note) | VARCHAR(255) |  |  | YES | (NULL) |  |  |

**Description of the fields**

### raceMask

Bitmask of races this cast applies to (`0` = all races).

### classMask

Bitmask of classes this cast applies to (`0` = all classes).

### spell

Spell id to cast on the newly created character.

### note

Optional free-text description of the entry.
