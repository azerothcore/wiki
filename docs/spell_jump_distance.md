# spell_jump_distance

[<-Back-to:World](database-world)


**The `spell_jump_distance` table**

This table stores per-spell chain hop distance overrides. When present, the server loads `JumpDistance` and assigns it to `SpellInfo::JumpDistance`; `Spell::SearchChainTargets()` then uses this value to constrain chain-target hop radius.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id) | INT | UNSIGNED | PRI | NO | 0 | | Spell id (links to Spell.dbc) |
| [JumpDistance](#jumpdistance) | FLOAT | SIGNED | | NO | 0 | | Max hop distance in yards |

**Description of the fields**

### ID

Spell identifier this row applies to. See [Spell.dbc](spell).

### JumpDistance

Maximum chain-hop distance (in yards) for the spell. When > 0 the server will use this value instead of the default jump radius when searching chain targets.
