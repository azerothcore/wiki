# destructiblemodeldata\_dbc

[<-Back-to:World](database-world)

**The \`destructiblemodeldata\_dbc\` table**

This table has the same columns as the client file `DestructibleModelData.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: destructiblemodeldata\_dbc's Structure**

| Field                                                       | Type |     | Null | Key | Default | Extra | Comment |
| :---------------------------------------------------------- | :--- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                                   | INT  |     | NO   | PRI | 0       |       |         |
| [State0Wmo](#state0wmo)                                     | INT  |     | NO   |     | 0       |       |         |
| [State0DestructionDoodadSet](#state0destructiondoodadset)   | INT  |     | NO   |     | 0       |       |         |
| [State0ImpactEffectDoodadSet](#state0impacteffectdoodadset) | INT  |     | NO   |     | 0       |       |         |
| [State0AmbientDoodadSet](#state0ambientdoodadset)           | INT  |     | NO   |     | 0       |       |         |
| [State1Wmo](#state1wmo)                                     | INT  |     | NO   |     | 0       |       |         |
| [State1DestructionDoodadSet](#state1destructiondoodadset)   | INT  |     | NO   |     | 0       |       |         |
| [State1ImpactEffectDoodadSet](#state1impacteffectdoodadset) | INT  |     | NO   |     | 0       |       |         |
| [State1AmbientDoodadSet](#state1ambientdoodadset)           | INT  |     | NO   |     | 0       |       |         |
| [State2Wmo](#state2wmo)                                     | INT  |     | NO   |     | 0       |       |         |
| [State2DestructionDoodadSet](#state2destructiondoodadset)   | INT  |     | NO   |     | 0       |       |         |
| [State2ImpactEffectDoodadSet](#state2impacteffectdoodadset) | INT  |     | NO   |     | 0       |       |         |
| [State2AmbientDoodadSet](#state2ambientdoodadset)           | INT  |     | NO   |     | 0       |       |         |
| [State3Wmo](#state3wmo)                                     | INT  |     | NO   |     | 0       |       |         |
| [State3DestructionDoodadSet](#state3destructiondoodadset)   | INT  |     | NO   |     | 0       |       |         |
| [State3ImpactEffectDoodadSet](#state3impacteffectdoodadset) | INT  |     | NO   |     | 0       |       |         |
| [State3AmbientDoodadSet](#state3ambientdoodadset)           | INT  |     | NO   |     | 0       |       |         |
| [Field17](#field)                                           | INT  |     | NO   |     | 0       |       |         |
| [Field18](#field)                                           | INT  |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it.

### State0Wmo

Not used by the core.

### State0DestructionDoodadSet

Not used by the core.

### State0ImpactEffectDoodadSet

The core reads this column.

### State0AmbientDoodadSet

Not used by the core.

### State1Wmo

Not used by the core.

### State1DestructionDoodadSet

Not used by the core.

### State1ImpactEffectDoodadSet

The core reads this column.

### State1AmbientDoodadSet

Not used by the core.

### State2Wmo

Not used by the core.

### State2DestructionDoodadSet

Not used by the core.

### State2ImpactEffectDoodadSet

The core reads this column.

### State2AmbientDoodadSet

Not used by the core.

### State3Wmo

Not used by the core.

### State3DestructionDoodadSet

Not used by the core.

### State3ImpactEffectDoodadSet

The core reads this column.

### State3AmbientDoodadSet

Not used by the core.

### Field

Not used by the core.
