# creature\_formations

[<-Back-to:World](database-world.md)

**The \`creature\_formations\` table**

This table allows to group mobs. Members of group will follow others, and attack their targets.

**Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|---------|------------|-----|------|---------|-------|---------|
| [leaderGUID][1] | INT | UNSIGNED   |     | NO   | NULL    |       |         |
| [memberGUID][2] | INT | UNSIGNED   | PRI | NO   | NULL    |       |         |
| [dist][3]       | FLOAT   | UNSIGNED   |     | NO   | NULL    |       |         |
| [angle][4]      | FLOAT   | UNSIGNED   |     | NO   | NULL    |       |         |
| [groupAI][5]    | INT | UNSIGNED   |     | NO   | NULL    |       |         |
| [point_1][6]    | INT | UNSIGNED   |     | NO   | 0       |       |         |
| [point_2][7]    | INT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #leaderguid
[2]: #memberguid
[3]: #dist
[4]: #angle
[5]: #groupai
[6]: #point_1
[7]: #point_2

## leaderGUID

GUID of group leader

## memberGUID

GUID of group member. NOTE: Is required to have an entry with `leaderGUID` and `memberGUID` with the `leaderGUID` in order to make the group work.
Example:

* Leader = 1
* Members = 2 and 3

| leaderGUID | memberGUID |
|------------|------------|
| 1          | 1          |
| 1          | 2          |
| 1          | 3          |

## dist

Maximum distance between group leader and member

Value must be >=0. If the value does not meet the condition the SQL will fail on `creature_formations_chk_1`.

## angle

Angle between leader and member
Note: Only degrees are used! Values should be between 0 and 360

![angle](assets/images/angle.png)

Value must be >=0. If the value does not meet the condition the SQL will fail on `creature_formations_chk_1`.

## groupAI

Sets group member behaviours, values are:

| Value | Behaviour                                                    |
|-------|--------------------------------------------------------------|
| 0     | Noone assists noone and member don't follow the leader       |
| 1     | The member aggroes if the leader aggroes                     |
| 2     | The leader aggroes if the member aggroes                     |
| 3     | Everyone assists everyone and member don't follow the leader |
| 4     | Everyone evades if any member evades (enters evade mode)     |
| 512   | Noone assists noone and member follow the leader             |
| 515   | Everyone assists everyone and member follow the leader       |

## point\_1  

## point\_2

These values are used to set leaderGUID pre ending path points for memberGUID's where the path is a straight return path and memberGUID's should not crossover to other side of leaderGUID on direction change.

If your leader has a path like the one below where he moves to point 5 then back to 1 you would set point\_1 = 4 and point\_2 = 8 on the memberGUID. If the memberGUID is at angle 90 up to point 5 it will switch to angle 270 for the return trip. This is only needed to keep creatures on the correct side. these values can be left at 0 for creatures following directly behind leaderGUID or any creatures in a circular path. 

```
	1     2     3     4    5

	-----<--------->------

       8    7      6
```
