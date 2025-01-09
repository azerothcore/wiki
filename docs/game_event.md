# game_event

[<-Back-to:World](database-world)

**The \`game_event\` table**

**Table Structure**

This table holds definitions for all game events that are activated or deactivated automatically by the Game Event System in the core.

| Field                        | Type         | Attributes | Key | Null | Default | Extra  | Comment                                                                                                                              |
| ---------------------------- | ------------ | ---------- | --- | ---- | ------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| [eventEntry](#evententry)    | TINYINT      | UNSIGNED   | PRI | NO   |         | Unique | Entry of the game event                                                                                                              |
| [start_time](#starttime)     | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute start date, the event will never start before                                                                               |
| [end_time](#endtime)         | TIMESTAMP    |            |     | YES  | NULL    |        | Absolute end date, the event will never start after; if NULL it will be implicitly set to 2 years in the future on each server start |
| [occurrence](#occurrence)    | BIGINT       | UNSIGNED   |     | NO   |         |        | Delay in minutes between occurrences of the event                                                                                    |
| [length](#length)            | BIGINT       | UNSIGNED   |     | NO   |         |        | Length in minutes of the event                                                                                                       |
| [holiday](#holiday)          | MEDIUMINT    | UNSIGNED   |     | NO   |         |        | Client side holiday id (from dbc)                                                                                                    |
| [holidayStage](holidaystage) | TINYINT      | UNSIGNED   |     | NO   |         |        |                                                                                                                                      |
| [description](#description)  | VARCHAR(255) | SIGNED     |     | YES  | NULL    |        | Description of the event displayed in console                                                                                        |
| [world_event](#worldevent)   | TINYINT      | UNSIGNED   |     | NO   |         |        | 0 if normal event, 1 if world event                                                                                                  |
| [announce](#announce)        | TINYINT      | UNSIGNED   |     | YES  | 2       |        | 0 dont announce, 1 announce, 2 value from config                                                                                     |

**Field Descriptions**

### eventEntry

Entry of the event. Keep it as low as possible and prevent making holes in the list. Higher the max id is, the more memory will be used to store the event data.

### start_time

Absolute start date of the event. The event will start occurring only if the local time at the server is after the one set here.

### end_time

Absolute end date of the event. The event will stop occurring if the local time at the server is after the one set here.

### occurrence

Number of minutes between 2 occurrences of the event. (2880 = 2 days, 1440 = 1 day, etc)

{% include warning.html content="Value can't be 0 or the server will crash." %}

### length

Number of minutes the event will last after the start of the occurrence. (2880 = 2 days, 1440 = 1 day, etc)
This value must be lower than occurrence one or the event will never stop.


### holiday

Holiday ID from  [Holidays DBC file](holidays). This is sent to the client to update the calender.

### description

String containing the name of the event displayed in console each time it starts or stops.

### world_event

This is a boolean field that determines if this game event is a world event or not. 0 = normal event, 1 = world event. For the world event to work, you need to at a minimum, populate [game_event_condition](game_event_condition) and [game_event_quest_condition](game_event_quest_condition).

### announce

| Value | Description                                        |
| ----- | -------------------------------------------------- |
| 0     | Don't announce the Event                           |
| 1     | Announce the description of the Event to the world |
| 2     | Use the `event.announce` settings from the config  |

## Example

(**Note:** make a database backup before making any changes to your database.)

Below are some SQL changes that can be made to the \`acore_world\` database that will cause three "Defias Cutpurse" NPCs appear and disappear every two (2) minutes from Elwynn Forest. This is designed to be a simple example and doesn't represent an improvement to the game world in anyway.

We're going to assume you're using the `mysql` commandline tool to manipulate the database, but you can use any tool you want that lets you run custom SQL queries.

Login to the game world using the WoW client and start by teleporting to the area we intend on working in. Use the following GM command, which might require `.gm on` first: `.go xyz -9168.486 86.90783 77.05649 0 0.006`. You'll see three NPCs walking around a tent, like this:

![npcs](https://github.com/user-attachments/assets/d0ecbb52-dd0d-453c-824e-bd13f4f6a791)

Next, connect to the AzerothCore MySQL database and ensure you're using the correct table: \`use acore_world\`.

Next, apply the following SQL to create a new event with ID 91 to your world (**note**: this will delete any existing event entry with an ID of 91):

```sql
DELETE FROM game_event WHERE eventEntry = 91;
INSERT INTO game_event (
	eventEntry,
	start_time,
	end_time,
	occurence,
	length,
	holiday,
	holidayStage,
	description,
	world_event,
	announce
) VALUES (
	91,
	"2000-01-01 14:00:00",
	"2030-12-31 14:00:00",
	2,
	1,
	0,
	0,
	"TESTING EVENT",
	0,
	1
);
```

This triggers once every `occurence` minutes or `2` minutes in this case. The event will last for `length` minutes or `1` minute for us, which means after one (`1`) minute the NPCs will be added back into the game world.

Now update the `game_event_creature` table by applying the following SQL:

```sql
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;

INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79888);
INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79889);
INSERT INTO game_event_creature (eventEntry,guid) VALUES (-91,79890);
```

This defines the specific NPCs GUIDs we want the game event to **despawn** _from_ the world for us. It doesn't spawn the creatures as they already exist. There are other `game_event_*` tables for managing other things too, much more complex things, but we're just selecting this table as it's an easy one to work with and use to demonstrate how events work. Note that we've set the `eventEntry` field to a **negative** value -- that is `-91` -- and not (positive) `91` because we want this event to **delete** the NPCs. Don't worry, when the event ends after `length` minutes, the NPCs will be respawned again. If you want the event to spawn creatures you've defined, then you'd a positive GUID.

Finally restart your AzerothCore world server. Because the game world has been restarted, and you had to log back into the game, you will have missed the first run of the event and therefore the announcement (which is set to `1` in our example SQL, above.) This means depending on how fast you teleport to the coordinates above, you may find the NPCs are still there or may have been removed.

When you hang around the area at the coordinates from above, you'll eventually see the NPCs despawn:

![no-npcs](https://github.com/user-attachments/assets/159cd3c5-3863-449f-a9a8-4f318fe7589c)

If you want to now remove this event from your database, the following SQL can be used:

```sql
DELETE FROM game_event WHERE eventEntry = 91;
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;
```

Have fun!
