# vehicle_seat_addon

[<-Back-to:World](database-world)

**The `vehicle_seat_addon` table**

Provides per-seat overrides for vehicle seats. `SeatEntry` references a `VehicleSeat.dbc` entry and the remaining columns override the seat orientation and the position/parameters used when a passenger exits the seat.

**Table Structure**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [SeatEntry](#seatentry) | INT | UNSIGNED | PRI | NO |  |  | VehicleSeatEntry.dbc identifier |
| [SeatOrientation](#seatorientation) | FLOAT | SIGNED |  | YES | 0 |  | Seat Orientation override value |
| [ExitParamX](#exitparamx) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamY](#exitparamy) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamZ](#exitparamz) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamO](#exitparamo) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamValue](#exitparamvalue) | TINYINT(1) | SIGNED |  | YES | 0 |  |  |

**Description of the fields**

### SeatEntry

VehicleSeatEntry.dbc identifier

### SeatOrientation

Seat Orientation override value

### ExitParamX

_Undocumented._

### ExitParamY

_Undocumented._

### ExitParamZ

_Undocumented._

### ExitParamO

_Undocumented._

### ExitParamValue

_Undocumented._
