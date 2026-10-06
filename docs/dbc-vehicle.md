# Vehicle.dbc

[`Back-to:DBC`](dbc-index)

**The \`Vehicle.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [vehicle_dbc](vehicle_dbc) table of the world database.

**Structure**

| Column | Field                   | Type   | vehicle\_dbc column                                            | Comment                                                |
| :----: | :---------------------- | :----- | :------------------------------------------------------------- | :----------------------------------------------------- |
| 0      | ID                      | uint32 | [ID](vehicle_dbc#id)                                           |                                                        |
| 1      | Flags                   | uint32 | [Flags](vehicle_dbc#flags)                                     |                                                        |
| 2      | TurnSpeed               | float  | [TurnSpeed](vehicle_dbc#turnspeed)                             |                                                        |
| 3      | PitchSpeed              | float  | [PitchSpeed](vehicle_dbc#pitchspeed)                           |                                                        |
| 4      | PitchMin                | float  | [PitchMin](vehicle_dbc#pitchmin)                               |                                                        |
| 5      | PitchMax                | float  | [PitchMax](vehicle_dbc#pitchmax)                               |                                                        |
| 6      | SeatID_0                | uint32 | [SeatID_1](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 7      | SeatID_1                | uint32 | [SeatID_2](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 8      | SeatID_2                | uint32 | [SeatID_3](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 9      | SeatID_3                | uint32 | [SeatID_4](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 10     | SeatID_4                | uint32 | [SeatID_5](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 11     | SeatID_5                | uint32 | [SeatID_6](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 12     | SeatID_6                | uint32 | [SeatID_7](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 13     | SeatID_7                | uint32 | [SeatID_8](vehicle_dbc#seatid)                                 | ID in [VehicleSeat.dbc](dbc-vehicleseat)               |
| 14     | MouseLookOffsetPitch    | float  | [MouseLookOffsetPitch](vehicle_dbc#mouselookoffsetpitch)       |                                                        |
| 15     | CameraFadeDistScalarMin | float  | [CameraFadeDistScalarMin](vehicle_dbc#camerafadedistscalarmin) |                                                        |
| 16     | CameraFadeDistScalarMax | float  | [CameraFadeDistScalarMax](vehicle_dbc#camerafadedistscalarmax) |                                                        |
| 17     | CameraPitchOffset       | float  | [CameraPitchOffset](vehicle_dbc#camerapitchoffset)             |                                                        |
| 18     | FacingLimitRight        | float  | [FacingLimitRight](vehicle_dbc#facinglimitright)               |                                                        |
| 19     | FacingLimitLeft         | float  | [FacingLimitLeft](vehicle_dbc#facinglimitleft)                 |                                                        |
| 20     | MsslTrgtTurnLingering   | float  | [MsslTrgtTurnLingering](vehicle_dbc#mssltrgtturnlingering)     |                                                        |
| 21     | MsslTrgtPitchLingering  | float  | [MsslTrgtPitchLingering](vehicle_dbc#mssltrgtpitchlingering)   |                                                        |
| 22     | MsslTrgtMouseLingering  | float  | [MsslTrgtMouseLingering](vehicle_dbc#mssltrgtmouselingering)   |                                                        |
| 23     | MsslTrgtEndOpacity      | float  | [MsslTrgtEndOpacity](vehicle_dbc#mssltrgtendopacity)           |                                                        |
| 24     | MsslTrgtArcSpeed        | float  | [MsslTrgtArcSpeed](vehicle_dbc#mssltrgtarcspeed)               |                                                        |
| 25     | MsslTrgtArcRepeat       | float  | [MsslTrgtArcRepeat](vehicle_dbc#mssltrgtarcrepeat)             |                                                        |
| 26     | MsslTrgtArcWidth        | float  | [MsslTrgtArcWidth](vehicle_dbc#mssltrgtarcwidth)               |                                                        |
| 27     | MsslTrgtImpactRadius_0  | float  | [MsslTrgtImpactRadius_1](vehicle_dbc#mssltrgtimpactradius)     |                                                        |
| 28     | MsslTrgtImpactRadius_1  | float  | [MsslTrgtImpactRadius_2](vehicle_dbc#mssltrgtimpactradius)     |                                                        |
| 29     | MsslTrgtArcTexture      | string | [MsslTrgtArcTexture](vehicle_dbc#mssltrgtarctexture)           |                                                        |
| 30     | MsslTrgtImpactTexture   | string | [MsslTrgtImpactTexture](vehicle_dbc#mssltrgtimpacttexture)     |                                                        |
| 31     | MsslTrgtImpactModel_0   | string | [MsslTrgtImpactModel_1](vehicle_dbc#mssltrgtimpactmodel)       |                                                        |
| 32     | MsslTrgtImpactModel_1   | string | [MsslTrgtImpactModel_2](vehicle_dbc#mssltrgtimpactmodel)       |                                                        |
| 33     | CameraYawOffset         | float  | [CameraYawOffset](vehicle_dbc#camerayawoffset)                 |                                                        |
| 34     | UiLocomotionType        | uint32 | [UilocomotionType](vehicle_dbc#uilocomotiontype)               |                                                        |
| 35     | MsslTrgtImpactTexRadius | float  | [MsslTrgtImpactTexRadius](vehicle_dbc#mssltrgtimpacttexradius) |                                                        |
| 36     | VehicleUIIndicatorID    | uint32 | [VehicleUIIndicatorID](vehicle_dbc#vehicleuiindicatorid)       | ID in [VehicleUIIndicator.dbc](dbc-vehicleuiindicator) |
| 37     | PowerDisplayID_0        | int32  | [PowerDisplayID_1](vehicle_dbc#powerdisplayid)                 | ID in [PowerDisplay.dbc](dbc-powerdisplay)             |
| 38     | PowerDisplayID_1        | int32  | [PowerDisplayID_2](vehicle_dbc#powerdisplayid)                 |                                                        |
| 39     | PowerDisplayID_2        | int32  | [PowerDisplayID_3](vehicle_dbc#powerdisplayid)                 |                                                        |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/Vehicle).
