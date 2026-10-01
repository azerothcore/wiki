# vehicle_seat_addon

[<-返回:World](database-world)

**\`vehicle_seat_addon\` 表**

为载具座位提供逐座位覆盖设置。`SeatEntry` 引用 `VehicleSeat.dbc` 条目，其余列用于覆盖座位朝向以及乘客离开座位时使用的位置/参数。

**表结构**

| Field | Type | Attributes | Key | Null | Default | Extra | Comment |
| ----- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [SeatEntry](#seatentry) | INT | UNSIGNED | PRI | NO |  |  | VehicleSeatEntry.dbc 标识符 |
| [SeatOrientation](#seatorientation) | FLOAT | SIGNED |  | YES | 0 |  | 座位朝向覆盖值 |
| [ExitParamX](#exitparamx) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamY](#exitparamy) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamZ](#exitparamz) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamO](#exitparamo) | FLOAT | SIGNED |  | YES | 0 |  |  |
| [ExitParamValue](#exitparamvalue) | TINYINT(1) | SIGNED |  | YES | 0 |  |  |

**字段描述**

### SeatEntry

VehicleSeatEntry.dbc 标识符

### SeatOrientation

座位朝向覆盖值

### ExitParamX

_未记录。_

### ExitParamY

_未记录。_

### ExitParamZ

_未记录。_

### ExitParamO

_未记录。_

### ExitParamValue

_未记录。_
