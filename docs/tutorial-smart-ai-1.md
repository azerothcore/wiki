# Introduction to SmartAI

## What type of waypoint will I use?

SmartAI allows us to use 2 different waypoint tables:

waypoint_data, which is used in cpp and in more general patrols
waypoints, a type which was made specifically for SmartAI


# Scripting a Simple Scripted Patrol

For this we'll script a simple patrol RP, a script that plays every now and then on a timer and involves a path.
When making blizzlike scripts, most of this data can be gathered in sniffs. Using tools like a parser, WDBE, or WaypointCreator we can extract waypoints, and then script in what actions are to be taken.
In a parsed file, you can search for the unique creature GUID, and see what actions are done. For example, NPCFlag, UnitFlag, StandState, EmoteState and Oneshot Emotes all can be found in the parsed file. Some actions will eventually be hidden, but then we can get creative or even investigate further. In Black Temple, for example, there are creatures that execute an Eat Emote by casting a serverside spell, but that isn't common.

The event we will be implementing contains only StandStates and spoken lines.
First we detail what will happen and when:

```
UPDATE `creature` SET `MovementType` = 2 WHERE `id1` = 23600 AND `guid` = 18604;

DELETE FROM `creature_addon` WHERE (`guid` IN (18604));
INSERT INTO `creature_addon` (`guid`, `path_id`, `mount`, `bytes1`, `bytes2`, `emote`, `visibilityDistanceType`, `auras`) VALUES
(18604, 186040, 0, 0, 1, 0, 0, NULL);

DELETE FROM `waypoint_data` WHERE `id` = 186040;
INSERT INTO `waypoint_data` (`id`, `point`, `position_x`, `position_y`, `position_z`, `orientation`, `delay`) VALUES
(186040, 1, -4044.12, -3393.59, 38.1363, NULL, 6000), -- 1s, Talk 0, 5s, Talk 1
(186040, 2, -4044.21, -3394.23, 38.3905, NULL, 0),
(186040, 3, -4042.96, -3396.48, 38.3905, NULL, 0),
(186040, 4, -4041.71, -3397.23, 38.3905, NULL, 0),
(186040, 5, -4040.8, -3396.88, 38.1447, NULL, 16000), -- 2s, Emote 16, 6s, Talk 2, 6s, Garion Talk 0
(186040, 6, -4043.67, -3395.27, 38.1634, NULL, 0),
(186040, 7, -4043.67, -3395.27, 38.1634, 3.87463, 240000);
```

Breaking down this line by line:

```
UPDATE `creature` SET `MovementType` = 2 WHERE `id1` = 23600 AND `guid` = 18604;
```

We're not placing a new creature, just adding behaviour to an existing one, so we will just modify its MovementType, which tells it will use the path set in its creature_addon entry.

```
DELETE FROM `creature_addon` WHERE (`guid` IN (18604));
INSERT INTO `creature_addon` (`guid`, `path_id`, `mount`, `bytes1`, `bytes2`, `emote`, `visibilityDistanceType`, `auras`) VALUES
(18604, 186040, 0, 0, 1, 0, 0, NULL);
```

This is its creature_addon entry. Patrols have, by convention, ids equal to GUID*10. The most common value for bytes2, also known as SheateState, is 1, which represents the melee weapons of the creature. This also contains RP-related items such as lanterns, bottles and such.

```
DELETE FROM `waypoint_data` WHERE `id` = 186040;
INSERT INTO `waypoint_data` (`id`, `point`, `position_x`, `position_y`, `position_z`, `orientation`, `delay`) VALUES
(186040, 1, -4044.12, -3393.59, 38.1363, NULL, 6000), -- 1s, Talk 0, 5s, Talk 1
(186040, 2, -4044.21, -3394.23, 38.3905, NULL, 0),
(186040, 3, -4042.96, -3396.48, 38.3905, NULL, 0),
(186040, 4, -4041.71, -3397.23, 38.3905, NULL, 0),
(186040, 5, -4040.8, -3396.88, 38.1447, NULL, 16000), -- 2s, Emote 16, 6s, Talk 2, 6s, Garion Talk 0
(186040, 6, -4043.67, -3395.27, 38.1634, NULL, 0),
(186040, 7, -4043.67, -3395.27, 38.1634, 3.87463, 180000);
```

This is the waypoint patrol the creature is assigned to. I've shortened it to not contain columns we'll not use.
The x,y,z values are self-explanatory. An orientation change requires an extra point copied from the one before, otherwise it's null. Delay will dictate the wait time after that waypoint is reached, as such, after the creature finishes the path on point 7, it will wait 3 minutes before starting the patrol again.
I also added a few comments detailing what actions are taken on which waypoints. It's a simplified version of what we'll be writing in the Actionlist.

## Setting up the main events

I use Keira to edit SmartAI, so that's what we'll use in this tutorial.

[Image of Editor

Since we're using patrols, we'll use a special event, called WAYPOINT_DATA_REACHED. If we used Event 40 (WAYPOINT_REACHED), it would **not** work. Because it will only trigger on waypoints in the `waypoints` table, that is specific to SmartAI and we don't use for the more generic patrols such as this one.
Keira will then generate an output we will copy and paste.

```
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = 23600;
DELETE FROM `smart_scripts` WHERE (`source_type` = 0 AND `entryorguid` = 23600);
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `event_param6`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES
(23600, 0, 0, 0, 108, 0, 100, 0, 1, 0, 0, 0, 0, 0, 80, 2360000, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - On Point 1 of Path Any Reached - Run Script'),
(23600, 0, 1, 0, 108, 0, 100, 0, 5, 0, 0, 0, 0, 0, 80, 2360001, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - On Point 5 of Path Any Reached - Run Script');
```

This seems simpler than what I described in the comments. This is because we don't actually take the actions here. We'll use a different mechanic of SmartAI, called Actionlists, or Script9, which is a sequence of actions taken on timers provided. Thus we can make delayed actions much easier. Script IDs for Actionlists are, by convention, numbered CreatureEntry*100, adding +1 to every unique list.
In here we use only one path ID so we leave it as 0, because we don't expect any other patrols.

Now we'll open the Actionlist Editor and make both Scripts.

```
DELETE FROM `smart_scripts` WHERE (`source_type` = 9 AND `entryorguid` IN (2360000, 2360001));
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `event_param6`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES
(2360000, 9, 0, 0, 0, 0, 100, 0, 1000, 1000, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 0'),
(2360000, 9, 1, 0, 0, 0, 100, 0, 5000, 5000, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 1'),

(2360001, 9, 0, 0, 0, 0, 100, 0, 2000, 2000, 0, 0, 0, 0, 5, 16, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Play Emote 16'),
(2360001, 9, 1, 0, 0, 0, 100, 0, 6000, 6000, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 2'),
(2360001, 9, 2, 0, 0, 0, 100, 0, 6000, 6000, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 19, 23601, 0, 0, 0, 0, 0, 0, 0, 'Apprentice Morlann - Actionlist - Say Line 0 (Apprentice Garion)');
```

So this is what will happen:
1. The creature spawns and starts the patrol for the first time
2. When a point is reached, it'll fire the Event, checks if the point reached is 1 or 5, if so, the actions is played
3. The action is taken and the creature is assigned an Actionlist, which will play a sequence of delayed actions
4. Once the patrol is finished, it'll wait 3 minutes and then restart
