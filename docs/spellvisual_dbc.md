# spellvisual\_dbc

[<-Back-to:World](database-world)

**The \`spellvisual\_dbc\` table**

This table has the same columns as the client file `SpellVisual.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellvisual\_dbc's Structure**

| Field                                                         | Type  | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------------------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                                                     | INT   | SIGNED     | PRI | NO   | 0       |       |         |
| [PrecastKit](#precastkit)                                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [CastKit](#castkit)                                           | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ImpactKit](#impactkit)                                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [StateKit](#statekit)                                         | INT   | SIGNED     |     | NO   | 0       |       |         |
| [StateDoneKit](#statedonekit)                                 | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ChannelKit](#channelkit)                                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [HasMissile](#hasmissile)                                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileModel](#missilemodel)                                 | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissilePathType](#missilepathtype)                           | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileDestinationAttachment](#missiledestinationattachment) | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileSound](#missilesound)                                 | INT   | SIGNED     |     | NO   | 0       |       |         |
| [AnimEventSoundID](#animeventsoundid)                         | INT   | SIGNED     |     | NO   | 0       |       |         |
| [Flags](#flags)                                               | INT   | SIGNED     |     | NO   | 0       |       |         |
| [CasterImpactKit](#casterimpactkit)                           | INT   | SIGNED     |     | NO   | 0       |       |         |
| [TargetImpactKit](#targetimpactkit)                           | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileAttachment](#missileattachment)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileFollowGroundHeight](#missilefollowgroundheight)       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileFollowGroundDropSpeed](#missilefollowgrounddropspeed) | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileFollowGroundApproach](#missilefollowgroundapproach)   | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileFollowGroundFlags](#missilefollowgroundflags)         | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileMotion](#missilemotion)                               | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileTargetingKit](#missiletargetingkit)                   | INT   | SIGNED     |     | NO   | 0       |       |         |
| [InstantAreaKit](#instantareakit)                             | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ImpactAreaKit](#impactareakit)                               | INT   | SIGNED     |     | NO   | 0       |       |         |
| [PersistentAreaKit](#persistentareakit)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [MissileCastOffsetX](#missilecastoffsetx)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [MissileCastOffsetY](#missilecastoffsety)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [MissileCastOffsetZ](#missilecastoffsetz)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [MissileImpactOffsetX](#missileimpactoffsetx)                 | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [MissileImpactOffsetY](#missileimpactoffsety)                 | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [MissileImpactOffsetZ](#missileimpactoffsetz)                 | FLOAT | SIGNED     |     | NO   | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it only to index the rows and does not store it.

### PrecastKit

Not used by the core.

### CastKit

Not used by the core.

### ImpactKit

Not used by the core.

### StateKit

Not used by the core.

### StateDoneKit

Not used by the core.

### ChannelKit

Not used by the core.

### HasMissile

The core reads this column.

### MissileModel

The core reads this column.

### MissilePathType

Not used by the core.

### MissileDestinationAttachment

Not used by the core.

### MissileSound

Not used by the core.

### AnimEventSoundID

Not used by the core.

### Flags

Not used by the core.

### CasterImpactKit

Not used by the core.

### TargetImpactKit

Not used by the core.

### MissileAttachment

Not used by the core.

### MissileFollowGroundHeight

Not used by the core.

### MissileFollowGroundDropSpeed

Not used by the core.

### MissileFollowGroundApproach

Not used by the core.

### MissileFollowGroundFlags

Not used by the core.

### MissileMotion

Not used by the core.

### MissileTargetingKit

Not used by the core.

### InstantAreaKit

Not used by the core.

### ImpactAreaKit

Not used by the core.

### PersistentAreaKit

Not used by the core.

### MissileCastOffsetX

Not used by the core.

### MissileCastOffsetY

Not used by the core.

### MissileCastOffsetZ

Not used by the core.

### MissileImpactOffsetX

Not used by the core.

### MissileImpactOffsetY

Not used by the core.

### MissileImpactOffsetZ

Not used by the core.
