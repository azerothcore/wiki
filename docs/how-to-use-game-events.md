# How to use game events

This is a simple example that demonstrates how-to use the `game_event` and `game_event_creature` tables to trigger a repeating in-game event. This is a simple example, but it should be enough to give the reader a taste of what's required to start using in-game events.

**Note:** please make a database backup before making any changes to your database, including the ones below. This is just incase you overwrite something or do make breaking changes.

## Getting Started

Below are some SQL changes that can be made to the \`acore_world\` database that will cause three "Defias Cutpurse" NPCs appear and disappear every two (2) minutes from Elwynn Forest. This is designed to be a simple example and doesn't represent an improvement to the game world in anyway.

We're going to assume you're using the `mysql` commandline tool to manipulate the database, but you can use any tool you want that lets you run custom SQL queries.

Login to the game world using the WoW client and start by teleporting to the area we intend on working in. Use the following GM command, which might require `.gm on` first: `.go xyz -9168.486 86.90783 77.05649 0 0.006`. You'll see three NPCs walking around a tent, like this:

![NPCs Visible](assets/images/tutorials/game_event_example/npcs.png)

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

![No NPCs Visible](assets/images/tutorials/game_event_example/no-npcs.png)

## Undoing Everything

If you want to now remove this event from your database, the following SQL can be used:

```sql
DELETE FROM game_event WHERE eventEntry = 91;
DELETE FROM game_event_creature WHERE guid=79888;
DELETE FROM game_event_creature WHERE guid=79889;
DELETE FROM game_event_creature WHERE guid=79890;
```

You may need to reload AzerothCore's "World Server" for the changes above to take effect.
