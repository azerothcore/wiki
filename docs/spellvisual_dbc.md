# spellvisual\_dbc

[<-Back-to:World](database-world)

**The \`spellvisual\_dbc\` table**

This table has the same columns as the client file `SpellVisual.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellvisual\_dbc's Structure**

| Field                                                         | Type  |     | Null | Key | Default | Extra | Comment |
| :------------------------------------------------------------ | :---- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                                     | INT   |     | NO   | PRI | 0       |       |         |
| [PrecastKit](#precastkit)                                     | INT   |     | NO   |     | 0       |       |         |
| [CastKit](#castkit)                                           | INT   |     | NO   |     | 0       |       |         |
| [ImpactKit](#impactkit)                                       | INT   |     | NO   |     | 0       |       |         |
| [StateKit](#statekit)                                         | INT   |     | NO   |     | 0       |       |         |
| [StateDoneKit](#statedonekit)                                 | INT   |     | NO   |     | 0       |       |         |
| [ChannelKit](#channelkit)                                     | INT   |     | NO   |     | 0       |       |         |
| [HasMissile](#hasmissile)                                     | INT   |     | NO   |     | 0       |       |         |
| [MissileModel](#missilemodel)                                 | INT   |     | NO   |     | 0       |       |         |
| [MissilePathType](#missilepathtype)                           | INT   |     | NO   |     | 0       |       |         |
| [MissileDestinationAttachment](#missiledestinationattachment) | INT   |     | NO   |     | 0       |       |         |
| [MissileSound](#missilesound)                                 | INT   |     | NO   |     | 0       |       |         |
| [AnimEventSoundID](#animeventsoundid)                         | INT   |     | NO   |     | 0       |       |         |
| [Flags](#flags)                                               | INT   |     | NO   |     | 0       |       |         |
| [CasterImpactKit](#casterimpactkit)                           | INT   |     | NO   |     | 0       |       |         |
| [TargetImpactKit](#targetimpactkit)                           | INT   |     | NO   |     | 0       |       |         |
| [MissileAttachment](#missileattachment)                       | INT   |     | NO   |     | 0       |       |         |
| [MissileFollowGroundHeight](#missilefollowgroundheight)       | INT   |     | NO   |     | 0       |       |         |
| [MissileFollowGroundDropSpeed](#missilefollowgrounddropspeed) | INT   |     | NO   |     | 0       |       |         |
| [MissileFollowGroundApproach](#missilefollowgroundapproach)   | INT   |     | NO   |     | 0       |       |         |
| [MissileFollowGroundFlags](#missilefollowgroundflags)         | INT   |     | NO   |     | 0       |       |         |
| [MissileMotion](#missilemotion)                               | INT   |     | NO   |     | 0       |       |         |
| [MissileTargetingKit](#missiletargetingkit)                   | INT   |     | NO   |     | 0       |       |         |
| [InstantAreaKit](#instantareakit)                             | INT   |     | NO   |     | 0       |       |         |
| [ImpactAreaKit](#impactareakit)                               | INT   |     | NO   |     | 0       |       |         |
| [PersistentAreaKit](#persistentareakit)                       | INT   |     | NO   |     | 0       |       |         |
| [MissileCastOffsetX](#missilecastoffsetx)                     | FLOAT |     | NO   |     | 0       |       |         |
| [MissileCastOffsetY](#missilecastoffsety)                     | FLOAT |     | NO   |     | 0       |       |         |
| [MissileCastOffsetZ](#missilecastoffsetz)                     | FLOAT |     | NO   |     | 0       |       |         |
| [MissileImpactOffsetX](#missileimpactoffsetx)                 | FLOAT |     | NO   |     | 0       |       |         |
| [MissileImpactOffsetY](#missileimpactoffsety)                 | FLOAT |     | NO   |     | 0       |       |         |
| [MissileImpactOffsetZ](#missileimpactoffsetz)                 | FLOAT |     | NO   |     | 0       |       |         |

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
