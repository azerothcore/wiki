# creature\_formations

[<-Back-to:World](database-world.md)

**The \`creature\_formations\` table**

This table allows to group mobs. Members of group will follow others, and attack their targets.

**Structure**

| Field           | Type    | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|---------|------------|-----|------|---------|-------|---------|
| [leaderGUID][1] | int(11) | unsigned   |     | NO   | NULL    |       |         |
| [memberGUID][2] | int(11) | unsigned   | PRI | NO   | NULL    |       |         |
| [dist][3]       | float   | unsigned   |     | NO   | NULL    |       |         |
| [angle][4]      | float   | unsigned   |     | NO   | NULL    |       |         |
| [groupAI][5]    | int(11) | unsigned   |     | NO   | NULL    |       |         |
| [point_1][6]    | int(11) | unsigned   |     | NO   | 0       |       |         |
| [point_2][7]    | int(11) | unsigned   |     | NO   | 0       |       |         |

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

GUID of group member

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

If your leader has a path like the one below where he moves to point 5 then back to 1 you would set point\_1 = 4 and point\_2 = 8 on the memberGUID. If the memberGUID is at angle 90 up to point 5 it will switch to angle 270 for the return trip. This is only needed to keep creatures on the correct side. these values can be left at 0 for creatures following directly behind leaderGUID or any creatures in a circular path.

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [followangle2.png](attachments/2129997/2130322.png) (image/png)
