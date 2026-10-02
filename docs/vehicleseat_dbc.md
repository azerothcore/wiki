# vehicleseat\_dbc

[<-Back-to:World](database-world)

**The \`vehicleseat\_dbc\` table**

This table has the same columns as the client file `VehicleSeat.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: vehicleseat\_dbc's Structure**

| Field                                               | Type  | Attributes | Key | Null | Default | Extra | Comment |
| --------------------------------------------------- | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)                                           | INT   | SIGNED     | PRI | NO   | 0       |       |         |
| [Flags](#flags)                                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [AttachmentID](#attachmentid)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [AttachmentOffsetX](#attachmentoffsetx)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [AttachmentOffsetY](#attachmentoffsety)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [AttachmentOffsetZ](#attachmentoffsetz)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterPreDelay](#enterpredelay)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterSpeed](#enterspeed)                           | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterGravity](#entergravity)                       | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterMinDuration](#enterminduration)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterMaxDuration](#entermaxduration)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterMinArcHeight](#enterminarcheight)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterMaxArcHeight](#entermaxarcheight)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [EnterAnimStart](#enteranimstart)                   | INT   | SIGNED     |     | NO   | 0       |       |         |
| [EnterAnimLoop](#enteranimloop)                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [RideAnimStart](#rideanimstart)                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [RideAnimLoop](#rideanimloop)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [RideUpperAnimStart](#rideupperanimstart)           | INT   | SIGNED     |     | NO   | 0       |       |         |
| [RideUpperAnimLoop](#rideupperanimloop)             | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ExitPreDelay](#exitpredelay)                       | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitSpeed](#exitspeed)                             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitGravity](#exitgravity)                         | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitMinDuration](#exitminduration)                 | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitMaxDuration](#exitmaxduration)                 | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitMinArcHeight](#exitminarcheight)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitMaxArcHeight](#exitmaxarcheight)               | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [ExitAnimStart](#exitanimstart)                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ExitAnimLoop](#exitanimloop)                       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ExitAnimEnd](#exitanimend)                         | INT   | SIGNED     |     | NO   | 0       |       |         |
| [PassengerYaw](#passengeryaw)                       | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [PassengerPitch](#passengerpitch)                   | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [PassengerRoll](#passengerroll)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [PassengerAttachmentID](#passengerattachmentid)     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleEnterAnim](#vehicleenteranim)               | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleExitAnim](#vehicleexitanim)                 | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleRideAnimLoop](#vehiclerideanimloop)         | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleEnterAnimBone](#vehicleenteranimbone)       | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleExitAnimBone](#vehicleexitanimbone)         | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleRideAnimLoopBone](#vehiclerideanimloopbone) | INT   | SIGNED     |     | NO   | 0       |       |         |
| [VehicleEnterAnimDelay](#vehicleenteranimdelay)     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [VehicleExitAnimDelay](#vehicleexitanimdelay)       | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [VehicleAbilityDisplay](#vehicleabilitydisplay)     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [EnterUISoundID](#enteruisoundid)                   | INT   | SIGNED     |     | NO   | 0       |       |         |
| [ExitUISoundID](#exituisoundid)                     | INT   | SIGNED     |     | NO   | 0       |       |         |
| [UiSkin](#uiskin)                                   | INT   | SIGNED     |     | NO   | 0       |       |         |
| [FlagsB](#flagsb)                                   | INT   | SIGNED     |     | NO   | 0       |       |         |
| [CameraEnteringDelay](#cameraenteringdelay)         | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraEnteringDuration](#cameraenteringduration)   | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraExitingDelay](#cameraexitingdelay)           | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraExitingDuration](#cameraexitingduration)     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraOffsetX](#cameraoffsetx)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraOffsetY](#cameraoffsety)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraOffsetZ](#cameraoffsetz)                     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraPosChaseRate](#cameraposchaserate)           | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraFacingChaseRate](#camerafacingchaserate)     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraEnteringZoom](#cameraenteringzoom)           | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraSeatZoomMin](#cameraseatzoommin)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [CameraSeatZoomMax](#cameraseatzoommax)             | FLOAT | SIGNED     |     | NO   | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `VehicleSeatEntry::m_ID`.

### Flags

The core reads this column into `VehicleSeatEntry::m_flags`.

### AttachmentID

The core reads this column into `VehicleSeatEntry::m_attachmentID`.

### AttachmentOffsetX

The core reads this column into `VehicleSeatEntry::m_attachmentOffsetX`.

### AttachmentOffsetY

The core reads this column into `VehicleSeatEntry::m_attachmentOffsetY`.

### AttachmentOffsetZ

The core reads this column into `VehicleSeatEntry::m_attachmentOffsetZ`.

### EnterPreDelay

The core reads this column into `VehicleSeatEntry::m_enterPreDelay`.

### EnterSpeed

The core reads this column into `VehicleSeatEntry::m_enterSpeed`.

### EnterGravity

The core reads this column into `VehicleSeatEntry::m_enterGravity`.

### EnterMinDuration

The core reads this column into `VehicleSeatEntry::m_enterMinDuration`.

### EnterMaxDuration

The core reads this column into `VehicleSeatEntry::m_enterMaxDuration`.

### EnterMinArcHeight

The core reads this column into `VehicleSeatEntry::m_enterMinArcHeight`.

### EnterMaxArcHeight

The core reads this column into `VehicleSeatEntry::m_enterMaxArcHeight`.

### EnterAnimStart

The core reads this column into `VehicleSeatEntry::m_enterAnimStart`.

### EnterAnimLoop

The core reads this column into `VehicleSeatEntry::m_enterAnimLoop`.

### RideAnimStart

The core reads this column into `VehicleSeatEntry::m_rideAnimStart`.

### RideAnimLoop

The core reads this column into `VehicleSeatEntry::m_rideAnimLoop`.

### RideUpperAnimStart

The core reads this column into `VehicleSeatEntry::m_rideUpperAnimStart`.

### RideUpperAnimLoop

The core reads this column into `VehicleSeatEntry::m_rideUpperAnimLoop`.

### ExitPreDelay

The core reads this column into `VehicleSeatEntry::m_exitPreDelay`.

### ExitSpeed

The core reads this column into `VehicleSeatEntry::m_exitSpeed`.

### ExitGravity

The core reads this column into `VehicleSeatEntry::m_exitGravity`.

### ExitMinDuration

The core reads this column into `VehicleSeatEntry::m_exitMinDuration`.

### ExitMaxDuration

The core reads this column into `VehicleSeatEntry::m_exitMaxDuration`.

### ExitMinArcHeight

The core reads this column into `VehicleSeatEntry::m_exitMinArcHeight`.

### ExitMaxArcHeight

The core reads this column into `VehicleSeatEntry::m_exitMaxArcHeight`.

### ExitAnimStart

The core reads this column into `VehicleSeatEntry::m_exitAnimStart`.

### ExitAnimLoop

The core reads this column into `VehicleSeatEntry::m_exitAnimLoop`.

### ExitAnimEnd

The core reads this column into `VehicleSeatEntry::m_exitAnimEnd`.

### PassengerYaw

The core reads this column into `VehicleSeatEntry::m_passengerYaw`.

### PassengerPitch

The core reads this column into `VehicleSeatEntry::m_passengerPitch`.

### PassengerRoll

The core reads this column into `VehicleSeatEntry::m_passengerRoll`.

### PassengerAttachmentID

The core reads this column into `VehicleSeatEntry::m_passengerAttachmentID`.

### VehicleEnterAnim

The core reads this column into `VehicleSeatEntry::m_vehicleEnterAnim`.

### VehicleExitAnim

The core reads this column into `VehicleSeatEntry::m_vehicleExitAnim`.

### VehicleRideAnimLoop

The core reads this column into `VehicleSeatEntry::m_vehicleRideAnimLoop`.

### VehicleEnterAnimBone

The core reads this column into `VehicleSeatEntry::m_vehicleEnterAnimBone`.

### VehicleExitAnimBone

The core reads this column into `VehicleSeatEntry::m_vehicleExitAnimBone`.

### VehicleRideAnimLoopBone

The core reads this column into `VehicleSeatEntry::m_vehicleRideAnimLoopBone`.

### VehicleEnterAnimDelay

The core reads this column into `VehicleSeatEntry::m_vehicleEnterAnimDelay`.

### VehicleExitAnimDelay

The core reads this column into `VehicleSeatEntry::m_vehicleExitAnimDelay`.

### VehicleAbilityDisplay

The core reads this column into `VehicleSeatEntry::m_vehicleAbilityDisplay`.

### EnterUISoundID

The core reads this column into `VehicleSeatEntry::m_enterUISoundID`.

### ExitUISoundID

The core reads this column into `VehicleSeatEntry::m_exitUISoundID`.

### UiSkin

The core reads this column into `VehicleSeatEntry::m_uiSkin`.

### FlagsB

The core reads this column into `VehicleSeatEntry::m_flagsB`.

### CameraEnteringDelay

Not used by the core.

### CameraEnteringDuration

Not used by the core.

### CameraExitingDelay

Not used by the core.

### CameraExitingDuration

Not used by the core.

### CameraOffsetX

Not used by the core.

### CameraOffsetY

Not used by the core.

### CameraOffsetZ

Not used by the core.

### CameraPosChaseRate

Not used by the core.

### CameraFacingChaseRate

Not used by the core.

### CameraEnteringZoom

Not used by the core.

### CameraSeatZoomMin

Not used by the core.

### CameraSeatZoomMax

Not used by the core.
