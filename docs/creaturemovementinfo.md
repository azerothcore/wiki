# CreatureMovementInfo

[`Back-to:DBC`](dbc-index)

**CreatureMovementInfo.dbc**

**Version is : 3.3.5a**

Referenced by `creature_template.movementId`, see [creature_template](creature_template#movementid).

## Structure

| Column | Field                 | Type    | Notes                                                               |
| ------ | --------------------- | ------- | ------------------------------------------------------------------- |
| 1      | ID                    | Integer | Referenced by `creature_template.movementId`                        |
| 2      | smoothFacingChaseRate | Float   | Turn-in rate; `0` means no override, the higher the faster it turns |

## Content

The retail 3.3.5a file has 254 rows. A rate of `0` means no override, and only these rows are non-zero:

| ID  | smoothFacingChaseRate |
| --- | --------------------- |
| 1   | 2                     |
| 321 | 4                     |
| 341 | 5                     |
| 381 | 6                     |
| 401 | 5                     |
| 441 | 10                    |
| 541 | 10                    |
| 661 | 5                     |
| 681 | 5                     |
| 721 | 10                    |
| 741 | 10                    |
| 781 | 1                     |
| 801 | 0.25                  |
