# spell_cone

[<-Back-to:World](database-world)

**The `spell_cone` table**

This table stores cone-radius overrides used by cone target selection.
When a row exists, the value from `spell_cone.cone_radius` is used for cone radius calculation.
If no override exists, the core falls back to `spell_dbc.ConeRadius`, then to legacy hardcoded spell handling.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [id](#id) | INT | UNSIGNED | PRI | NO | 0 | | Spell identifier |
| [cone_radius](#cone_radius) | FLOAT | SIGNED | | NO | 1 | | Cone radius override (yards, schema default is 1) |

**Description of the fields**

### id

Spell identifier this row applies to.

### cone_radius

Cone radius (in yards) used by cone-angle calculation (90° base + object-size adjustment).
