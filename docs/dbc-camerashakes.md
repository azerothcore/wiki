# CameraShakes.dbc

[`Back-to:DBC`](dbc-index)

**The \`CameraShakes.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore does not load this file: only the client uses it.

**Structure**

| Column | Field       | Type   | Comment |
| :----: | :---------- | :----- | :------ |
| 0      | ID          | uint32 |         |
| 1      | ShakeType   | uint32 |         |
| 2      | Direction   | uint32 |         |
| 3      | Amplitude   | float  |         |
| 4      | Frequency   | float  |         |
| 5      | Duration    | float  |         |
| 6      | Phase       | float  |         |
| 7      | Coefficient | float  |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/CameraShakes).
