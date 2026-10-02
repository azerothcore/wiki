# creaturemodeldata\_dbc

[<-Back-to:World](database-world)

**The \`creaturemodeldata\_dbc\` table**

This table has the same columns as the client file `CreatureModelData.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: creaturemodeldata\_dbc's Structure**

| Field                                             | Type         | Attributes | Key | Null | Default | Extra | Comment |
| ------------------------------------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                                         | INT          | SIGNED     | PRI | NO   | 0       |       |         |
| [Flags](#flags)                                   | INT          | SIGNED     |     | NO   | 0       |       |         |
| [ModelName](#modelname)                           | VARCHAR(100) |            |     | YES  | NULL    |       |         |
| [SizeClass](#sizeclass)                           | INT          | SIGNED     |     | NO   | 0       |       |         |
| [ModelScale](#modelscale)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [BloodID](#bloodid)                               | INT          | SIGNED     |     | NO   | 0       |       |         |
| [FootprintTextureID](#footprinttextureid)         | INT          | SIGNED     |     | NO   | 0       |       |         |
| [FootprintTextureLength](#footprinttexturelength) | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [FootprintTextureWidth](#footprinttexturewidth)   | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [FootprintParticleScale](#footprintparticlescale) | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [FoleyMaterialID](#foleymaterialid)               | INT          | SIGNED     |     | NO   | 0       |       |         |
| [FootstepShakeSize](#footstepshakesize)           | INT          | SIGNED     |     | NO   | 0       |       |         |
| [DeathThudShakeSize](#deaththudshakesize)         | INT          | SIGNED     |     | NO   | 0       |       |         |
| [SoundID](#soundid)                               | INT          | SIGNED     |     | NO   | 0       |       |         |
| [CollisionWidth](#collisionwidth)                 | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [CollisionHeight](#collisionheight)               | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [MountHeight](#mountheight)                       | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [GeoBoxMinX](#geoboxminx)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [GeoBoxMinY](#geoboxminy)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [GeoBoxMinZ](#geoboxminz)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [GeoBoxMaxX](#geoboxmaxx)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [GeoBoxMaxY](#geoboxmaxy)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [GeoBoxMaxZ](#geoboxmaxz)                         | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [WorldEffectScale](#worldeffectscale)             | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [AttachedEffectScale](#attachedeffectscale)       | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [MissileCollisionRadius](#missilecollisionradius) | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [MissileCollisionPush](#missilecollisionpush)     | FLOAT        | SIGNED     |     | NO   | 0       |       |         |
| [MissileCollisionRaise](#missilecollisionraise)   | FLOAT        | SIGNED     |     | NO   | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### Flags

The core reads this column.

### ModelName

Not used by the core.

### SizeClass

Not used by the core.

### ModelScale

The core reads this column.

### BloodID

Not used by the core.

### FootprintTextureID

Not used by the core.

### FootprintTextureLength

Not used by the core.

### FootprintTextureWidth

Not used by the core.

### FootprintParticleScale

Not used by the core.

### FoleyMaterialID

Not used by the core.

### FootstepShakeSize

Not used by the core.

### DeathThudShakeSize

Not used by the core.

### SoundID

Not used by the core.

### CollisionWidth

The core reads this column.

### CollisionHeight

The core reads this column.

### MountHeight

The core reads this column.

### GeoBoxMinX

Not used by the core.

### GeoBoxMinY

Not used by the core.

### GeoBoxMinZ

Not used by the core.

### GeoBoxMaxX

Not used by the core.

### GeoBoxMaxY

Not used by the core.

### GeoBoxMaxZ

Not used by the core.

### WorldEffectScale

Not used by the core.

### AttachedEffectScale

Not used by the core.

### MissileCollisionRadius

Not used by the core.

### MissileCollisionPush

Not used by the core.

### MissileCollisionRaise

Not used by the core.
