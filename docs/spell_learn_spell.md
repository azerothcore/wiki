# spell\_learn\_spell

[<-Back-to:World](database-world)

**The \`spell\_learn\_spell\` table**

This table holds information on spells that should be learned at the same time a player learns another spell. For example the few spells that are automatically learned when a player first learns a new profession. All fields in this table use spell IDs from Spell.dbc.

NOTE: Spells with spell effects SPELL\_EFFECT\_LEARN\_SPELL should NOT be included in this table.

**Table Structure**

| Field        | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]   | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SpellID][2] | SMALLINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Active][3]  | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #spellid
[3]: #active

**Description of the fields**

### entry

The entry of the spell that the player learns, either from a trainer or from anywhere else (.learn for example).

### SpellID

The entry of the spell that will be automatically learned by the player when the player learns the spell specified in [entry](#spell_learn_spell-entry).

### Active

Defines whether spell is shown in spell book or not.
