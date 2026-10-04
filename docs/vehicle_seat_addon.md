# vehicle\_seat\_addon

[<-Back-to:World](database-world)

**The \`vehicle\_seat\_addon\` table**

Provides per-seat overrides for vehicle seats. `SeatEntry` references a `VehicleSeat.dbc` entry and the remaining columns override the seat orientation and the position/parameters used when a passenger exits the seat.

**Table: vehicle\_seat\_addon's Structure**

| Field                               | Type       |          | Null | Key | Default | Extra | Comment                         |
| :---------------------------------- | :--------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------ |
| [SeatEntry](#seatentry)             | INT        | UNSIGNED | NO   | PRI |         |       | VehicleSeatEntry.dbc identifier |
| [SeatOrientation](#seatorientation) | FLOAT      |          | YES  |     | 0       |       | Seat Orientation override value |
| [ExitParamX](#exitparamx)           | FLOAT      |          | YES  |     | 0       |       |                                 |
| [ExitParamY](#exitparamy)           | FLOAT      |          | YES  |     | 0       |       |                                 |
| [ExitParamZ](#exitparamz)           | FLOAT      |          | YES  |     | 0       |       |                                 |
| [ExitParamO](#exitparamo)           | FLOAT      |          | YES  |     | 0       |       |                                 |
| [ExitParamValue](#exitparamvalue)   | TINYINT(1) |          | YES  |     | 0       |       |                                 |

**Description of the table's fields**

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
