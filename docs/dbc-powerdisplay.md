# PowerDisplay.dbc

[`Back-to:DBC`](dbc-index)

**The \`PowerDisplay.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [powerdisplay_dbc](powerdisplay_dbc) table of the world database.

**Structure**

| Column | Field               | Type   | powerdisplay\_dbc column                                    | Comment |
| :----: | :------------------ | :----- | :---------------------------------------------------------- | :------ |
| 0      | ID                  | uint32 | [ID](powerdisplay_dbc#id)                                   |         |
| 1      | ActualType          | uint32 | [ActualType](powerdisplay_dbc#actualtype)                   |         |
| 2      | GlobalStringBaseTag | string | [GlobalstringBaseTag](powerdisplay_dbc#globalstringbasetag) |         |
| 3      | Red                 | uint8  | [Red](powerdisplay_dbc#red)                                 |         |
| 4      | Green               | uint8  | [Green](powerdisplay_dbc#green)                             |         |
| 5      | Blue                | uint8  | [Blue](powerdisplay_dbc#blue)                               |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/PowerDisplay).
