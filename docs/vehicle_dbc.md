# vehicle\_dbc

[<-Back-to:World](database-world)

**The \`vehicle\_dbc\` table**

This table has the same columns as the client file `Vehicle.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: vehicle\_dbc's Structure**

| Field                                               | Type         |     | Null | Key | Default | Extra | Comment |
| :-------------------------------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                                           | INT          |     | NO   | PRI | 0       |       |         |
| [Flags](#flags)                                     | INT          |     | NO   |     | 0       |       |         |
| [TurnSpeed](#turnspeed)                             | FLOAT        |     | NO   |     | 0       |       |         |
| [PitchSpeed](#pitchspeed)                           | FLOAT        |     | NO   |     | 0       |       |         |
| [PitchMin](#pitchmin)                               | FLOAT        |     | NO   |     | 0       |       |         |
| [PitchMax](#pitchmax)                               | FLOAT        |     | NO   |     | 0       |       |         |
| [SeatID_1](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_2](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_3](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_4](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_5](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_6](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_7](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [SeatID_8](#seatid)                                 | INT          |     | NO   |     | 0       |       |         |
| [MouseLookOffsetPitch](#mouselookoffsetpitch)       | FLOAT        |     | NO   |     | 0       |       |         |
| [CameraFadeDistScalarMin](#camerafadedistscalarmin) | FLOAT        |     | NO   |     | 0       |       |         |
| [CameraFadeDistScalarMax](#camerafadedistscalarmax) | FLOAT        |     | NO   |     | 0       |       |         |
| [CameraPitchOffset](#camerapitchoffset)             | FLOAT        |     | NO   |     | 0       |       |         |
| [FacingLimitRight](#facinglimitright)               | FLOAT        |     | NO   |     | 0       |       |         |
| [FacingLimitLeft](#facinglimitleft)                 | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtTurnLingering](#mssltrgtturnlingering)     | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtPitchLingering](#mssltrgtpitchlingering)   | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtMouseLingering](#mssltrgtmouselingering)   | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtEndOpacity](#mssltrgtendopacity)           | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtArcSpeed](#mssltrgtarcspeed)               | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtArcRepeat](#mssltrgtarcrepeat)             | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtArcWidth](#mssltrgtarcwidth)               | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtImpactRadius_1](#mssltrgtimpactradius)     | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtImpactRadius_2](#mssltrgtimpactradius)     | FLOAT        |     | NO   |     | 0       |       |         |
| [MsslTrgtArcTexture](#mssltrgtarctexture)           | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [MsslTrgtImpactTexture](#mssltrgtimpacttexture)     | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [MsslTrgtImpactModel_1](#mssltrgtimpactmodel)       | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [MsslTrgtImpactModel_2](#mssltrgtimpactmodel)       | VARCHAR(100) |     | YES  |     | NULL    |       |         |
| [CameraYawOffset](#camerayawoffset)                 | FLOAT        |     | NO   |     | 0       |       |         |
| [UilocomotionType](#uilocomotiontype)               | INT          |     | NO   |     | 0       |       |         |
| [MsslTrgtImpactTexRadius](#mssltrgtimpacttexradius) | FLOAT        |     | NO   |     | 0       |       |         |
| [VehicleUIIndicatorID](#vehicleuiindicatorid)       | INT          |     | NO   |     | 0       |       |         |
| [PowerDisplayID_1](#powerdisplayid)                 | INT          |     | NO   |     | 0       |       |         |
| [PowerDisplayID_2](#powerdisplayid)                 | INT          |     | NO   |     | 0       |       |         |
| [PowerDisplayID_3](#powerdisplayid)                 | INT          |     | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `VehicleEntry::m_ID`.

### Flags

The core reads this column into `VehicleEntry::m_flags`.

### TurnSpeed

The core reads this column into `VehicleEntry::m_turnSpeed`.

### PitchSpeed

The core reads this column into `VehicleEntry::m_pitchSpeed`.

### PitchMin

The core reads this column into `VehicleEntry::m_pitchMin`.

### PitchMax

The core reads this column into `VehicleEntry::m_pitchMax`.

### SeatID

The core reads these columns into `VehicleEntry::m_seatID`.

### MouseLookOffsetPitch

The core reads this column into `VehicleEntry::m_mouseLookOffsetPitch`.

### CameraFadeDistScalarMin

The core reads this column into `VehicleEntry::m_cameraFadeDistScalarMin`.

### CameraFadeDistScalarMax

The core reads this column into `VehicleEntry::m_cameraFadeDistScalarMax`.

### CameraPitchOffset

The core reads this column into `VehicleEntry::m_cameraPitchOffset`.

### FacingLimitRight

The core reads this column into `VehicleEntry::m_facingLimitRight`.

### FacingLimitLeft

The core reads this column into `VehicleEntry::m_facingLimitLeft`.

### MsslTrgtTurnLingering

The core reads this column into `VehicleEntry::m_msslTrgtTurnLingering`.

### MsslTrgtPitchLingering

The core reads this column into `VehicleEntry::m_msslTrgtPitchLingering`.

### MsslTrgtMouseLingering

The core reads this column into `VehicleEntry::m_msslTrgtMouseLingering`.

### MsslTrgtEndOpacity

The core reads this column into `VehicleEntry::m_msslTrgtEndOpacity`.

### MsslTrgtArcSpeed

The core reads this column into `VehicleEntry::m_msslTrgtArcSpeed`.

### MsslTrgtArcRepeat

The core reads this column into `VehicleEntry::m_msslTrgtArcRepeat`.

### MsslTrgtArcWidth

The core reads this column into `VehicleEntry::m_msslTrgtArcWidth`.

### MsslTrgtImpactRadius

The core reads these columns into `VehicleEntry::m_msslTrgtImpactRadius`.

### MsslTrgtArcTexture

The core reads this column into `VehicleEntry::m_msslTrgtArcTexture`.

### MsslTrgtImpactTexture

The core reads this column into `VehicleEntry::m_msslTrgtImpactTexture`.

### MsslTrgtImpactModel

The core reads these columns into `VehicleEntry::m_msslTrgtImpactModel`.

### CameraYawOffset

The core reads this column into `VehicleEntry::m_cameraYawOffset`.

### UilocomotionType

The core reads this column into `VehicleEntry::m_uiLocomotionType`.

### MsslTrgtImpactTexRadius

The core reads this column into `VehicleEntry::m_msslTrgtImpactTexRadius`.

### VehicleUIIndicatorID

The core reads this column into `VehicleEntry::m_uiSeatIndicatorType`.

### PowerDisplayID

The core reads `PowerDisplayID_1` into `VehicleEntry::m_powerDisplayId`. `PowerDisplayID_2` and `PowerDisplayID_3` are not used by the core.
