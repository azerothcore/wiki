# creature\_formations

[<-Back-to:World](database-world)

**The \`creature\_formations\` table**

This table allows to group mobs. Members of group will follow others, and attack their targets.

**Table: creature\_formations's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [leaderGUID](#leaderguid) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [memberGUID](#memberguid) | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [dist](#dist)             | FLOAT    |          | NO   |     | 0       |       |         |
| [angle](#angle)           | FLOAT    |          | NO   |     | 0       |       |         |
| [groupAI](#groupai)       | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [point_1](#point1)        | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [point_2](#point2)        | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### leaderGUID

GUID of group leader

### memberGUID

GUID of group member. NOTE: Is required to have an entry with `leaderGUID` and `memberGUID` with the `leaderGUID` in order to make the group work.
Example:

* Leader = 1
* Members = 2 and 3

| leaderGUID | memberGUID |
| ---------- | ---------- |
| 1          | 1          |
| 1          | 2          |
| 1          | 3          |

### dist

Maximum distance between group leader and member

Value must be >=0. If the value does not meet the condition the SQL will fail on `creature_formations_chk_1`.

### angle

Angle between leader and member
Note: Only degrees are used! Values should be between 0 and 360

![angle](assets/images/angle.png)

Value must be >=0. If the value does not meet the condition the SQL will fail on `creature_formations_chk_1`.

### groupAI

Sets group member behaviors, values are:

| Flag  | Bit | Name                                       | Comment                                                        |
| ----- | --- | ------------------------------------------ | -------------------------------------------------------------- |
|       | 0   |                                            | No one assists no one and member doesn't follow the leader     |
| 0x001 | 1   | GROUP_AI_FLAG_MEMBER_ASSIST_LEADER         | The member aggroes if the leader aggroes                       |
| 0x002 | 2   | GROUP_AI_FLAG_LEADER_ASSIST_MEMBER         | The leader aggroes if the member aggroes                       |
|       | 3   |                                            | Everyone assists everyone and member doesn't follow the leader |
| 0x004 | 4   | GROUP_AI_FLAG_EVADE_TOGETHER               | Everyone evades if any member evades (enters evade mode)       |
| 0x008 | 8   | GROUP_AI_FLAG_RESPAWN_ON_EVADE             | Everyone respawns if members evade    (enters evade mode)      |
| 0x010 | 16  | GROUP_AI_FLAG_DONT_RESPAWN_LEADER_ON_EVADE | Used with flag 0x008 to prevent leader from respawning         |
|       | 24  |                                            | Everyone but leader respawns if members evade                  |
| 0x200 | 512 | GROUP_AI_FLAG_FOLLOW_LEADER                | Noone assists noone and member follow the leader               |
|       | 515 |                                            | Everyone assists everyone and member follow the leader         |

### point\_1

Used together with [point\_2](#point2), see below.

### point\_2

These values are used to set leaderGUID pre ending path points for memberGUID's where the path is a straight return path and memberGUID's should not crossover to other side of leaderGUID on direction change.

If your leader has a path like the one below where he moves to point 5 then back to 1 you would set point\_1 = 4 and point\_2 = 8 on the memberGUID. If the memberGUID is at angle 90 up to point 5 it will switch to angle 270 for the return trip. This is only needed to keep creatures on the correct side. these values can be left at 0 for creatures following directly behind leaderGUID or any creatures in a circular path. 

```
	1     2     3     4    5

	-----<--------->------

       8    7      6
```
