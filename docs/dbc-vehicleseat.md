# VehicleSeat.dbc

[`Back-to:DBC`](dbc-index)

**The \`VehicleSeat.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [vehicleseat_dbc](vehicleseat_dbc) table of the world database.

**Structure**

| Column | Field                   | Type   | vehicleseat\_dbc column                                            | Comment |
| :----: | :---------------------- | :----- | :----------------------------------------------------------------- | :------ |
| 0      | ID                      | uint32 | [ID](vehicleseat_dbc#id)                                           |         |
| 1      | Flags                   | uint32 | [Flags](vehicleseat_dbc#flags)                                     |         |
| 2      | AttachmentID            | int32  | [AttachmentID](vehicleseat_dbc#attachmentid)                       |         |
| 3      | AttachmentOffset_X      | float  | [AttachmentOffsetX](vehicleseat_dbc#attachmentoffsetx)             |         |
| 4      | AttachmentOffset_Y      | float  | [AttachmentOffsetY](vehicleseat_dbc#attachmentoffsety)             |         |
| 5      | AttachmentOffset_Z      | float  | [AttachmentOffsetZ](vehicleseat_dbc#attachmentoffsetz)             |         |
| 6      | EnterPreDelay           | float  | [EnterPreDelay](vehicleseat_dbc#enterpredelay)                     |         |
| 7      | EnterSpeed              | float  | [EnterSpeed](vehicleseat_dbc#enterspeed)                           |         |
| 8      | EnterGravity            | float  | [EnterGravity](vehicleseat_dbc#entergravity)                       |         |
| 9      | EnterMinDuration        | float  | [EnterMinDuration](vehicleseat_dbc#enterminduration)               |         |
| 10     | EnterMaxDuration        | float  | [EnterMaxDuration](vehicleseat_dbc#entermaxduration)               |         |
| 11     | EnterMinArcHeight       | float  | [EnterMinArcHeight](vehicleseat_dbc#enterminarcheight)             |         |
| 12     | EnterMaxArcHeight       | float  | [EnterMaxArcHeight](vehicleseat_dbc#entermaxarcheight)             |         |
| 13     | EnterAnimStart          | int32  | [EnterAnimStart](vehicleseat_dbc#enteranimstart)                   |         |
| 14     | EnterAnimLoop           | int32  | [EnterAnimLoop](vehicleseat_dbc#enteranimloop)                     |         |
| 15     | RideAnimStart           | int32  | [RideAnimStart](vehicleseat_dbc#rideanimstart)                     |         |
| 16     | RideAnimLoop            | int32  | [RideAnimLoop](vehicleseat_dbc#rideanimloop)                       |         |
| 17     | RideUpperAnimStart      | int32  | [RideUpperAnimStart](vehicleseat_dbc#rideupperanimstart)           |         |
| 18     | RideUpperAnimLoop       | int32  | [RideUpperAnimLoop](vehicleseat_dbc#rideupperanimloop)             |         |
| 19     | ExitPreDelay            | float  | [ExitPreDelay](vehicleseat_dbc#exitpredelay)                       |         |
| 20     | ExitSpeed               | float  | [ExitSpeed](vehicleseat_dbc#exitspeed)                             |         |
| 21     | ExitGravity             | float  | [ExitGravity](vehicleseat_dbc#exitgravity)                         |         |
| 22     | ExitMinDuration         | float  | [ExitMinDuration](vehicleseat_dbc#exitminduration)                 |         |
| 23     | ExitMaxDuration         | float  | [ExitMaxDuration](vehicleseat_dbc#exitmaxduration)                 |         |
| 24     | ExitMinArcHeight        | float  | [ExitMinArcHeight](vehicleseat_dbc#exitminarcheight)               |         |
| 25     | ExitMaxArcHeight        | float  | [ExitMaxArcHeight](vehicleseat_dbc#exitmaxarcheight)               |         |
| 26     | ExitAnimStart           | int32  | [ExitAnimStart](vehicleseat_dbc#exitanimstart)                     |         |
| 27     | ExitAnimLoop            | int32  | [ExitAnimLoop](vehicleseat_dbc#exitanimloop)                       |         |
| 28     | ExitAnimEnd             | int32  | [ExitAnimEnd](vehicleseat_dbc#exitanimend)                         |         |
| 29     | PassengerYaw            | float  | [PassengerYaw](vehicleseat_dbc#passengeryaw)                       |         |
| 30     | PassengerPitch          | float  | [PassengerPitch](vehicleseat_dbc#passengerpitch)                   |         |
| 31     | PassengerRoll           | float  | [PassengerRoll](vehicleseat_dbc#passengerroll)                     |         |
| 32     | PassengerAttachmentID   | int32  | [PassengerAttachmentID](vehicleseat_dbc#passengerattachmentid)     |         |
| 33     | VehicleEnterAnim        | int32  | [VehicleEnterAnim](vehicleseat_dbc#vehicleenteranim)               |         |
| 34     | VehicleExitAnim         | int32  | [VehicleExitAnim](vehicleseat_dbc#vehicleexitanim)                 |         |
| 35     | VehicleRideAnimLoop     | int32  | [VehicleRideAnimLoop](vehicleseat_dbc#vehiclerideanimloop)         |         |
| 36     | VehicleEnterAnimBone    | int32  | [VehicleEnterAnimBone](vehicleseat_dbc#vehicleenteranimbone)       |         |
| 37     | VehicleExitAnimBone     | int32  | [VehicleExitAnimBone](vehicleseat_dbc#vehicleexitanimbone)         |         |
| 38     | VehicleRideAnimLoopBone | int32  | [VehicleRideAnimLoopBone](vehicleseat_dbc#vehiclerideanimloopbone) |         |
| 39     | VehicleEnterAnimDelay   | float  | [VehicleEnterAnimDelay](vehicleseat_dbc#vehicleenteranimdelay)     |         |
| 40     | VehicleExitAnimDelay    | float  | [VehicleExitAnimDelay](vehicleseat_dbc#vehicleexitanimdelay)       |         |
| 41     | VehicleAbilityDisplay   | uint32 | [VehicleAbilityDisplay](vehicleseat_dbc#vehicleabilitydisplay)     |         |
| 42     | EnterUISoundID          | uint32 | [EnterUISoundID](vehicleseat_dbc#enteruisoundid)                   |         |
| 43     | ExitUISoundID           | uint32 | [ExitUISoundID](vehicleseat_dbc#exituisoundid)                     |         |
| 44     | UiSkin                  | int32  | [UiSkin](vehicleseat_dbc#uiskin)                                   |         |
| 45     | FlagsB                  | uint32 | [FlagsB](vehicleseat_dbc#flagsb)                                   |         |
| 46     | CameraEnteringDelay     | float  | [CameraEnteringDelay](vehicleseat_dbc#cameraenteringdelay)         |         |
| 47     | CameraEnteringDuration  | float  | [CameraEnteringDuration](vehicleseat_dbc#cameraenteringduration)   |         |
| 48     | CameraExitingDelay      | float  | [CameraExitingDelay](vehicleseat_dbc#cameraexitingdelay)           |         |
| 49     | CameraExitingDuration   | float  | [CameraExitingDuration](vehicleseat_dbc#cameraexitingduration)     |         |
| 50     | CameraOffset_X          | float  | [CameraOffsetX](vehicleseat_dbc#cameraoffsetx)                     |         |
| 51     | CameraOffset_Y          | float  | [CameraOffsetY](vehicleseat_dbc#cameraoffsety)                     |         |
| 52     | CameraOffset_Z          | float  | [CameraOffsetZ](vehicleseat_dbc#cameraoffsetz)                     |         |
| 53     | CameraPosChaseRate      | float  | [CameraPosChaseRate](vehicleseat_dbc#cameraposchaserate)           |         |
| 54     | CameraFacingChaseRate   | float  | [CameraFacingChaseRate](vehicleseat_dbc#camerafacingchaserate)     |         |
| 55     | CameraEnteringZoom      | float  | [CameraEnteringZoom](vehicleseat_dbc#cameraenteringzoom)           |         |
| 56     | CameraSeatZoomMin       | float  | [CameraSeatZoomMin](vehicleseat_dbc#cameraseatzoommin)             |         |
| 57     | CameraSeatZoomMax       | float  | [CameraSeatZoomMax](vehicleseat_dbc#cameraseatzoommax)             |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/VehicleSeat).
