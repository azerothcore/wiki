---
tableofcontents: 1
---

# Useful SQL snippets

## Introduction
These SQL queries are intended to be fast and easy-to-use tools that can help identify and troubleshoot problems in the AzerothCore database. They're here to be a quick reference to help when looking at DB-related problems. If anyone else has any similar useful queries, let me know and I'll add them. Similarly, if you have a common problem for which you'd like a query written, feel free to get in touch.

## Loot and Reference Loot Issues

### Find what creatures drop an item directly
Note that this doesn't count items dropped from RLTs.
```sql
SELECT ct.name, clt.chance, ct.maxlevel, it.ItemLevel
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
JOIN `item_template` it ON clt.item = it.entry
WHERE it.entry = XXXXX;
```

### Find which RLTs an item is in
```sql
SELECT rlt.entry, it.name
FROM `reference_loot_template` rlt
JOIN `item_template` it ON rlt.Item = it.entry
WHERE rlt.item = XXXXX;
```

### Find which creatures share a RLT
Non-recursive.
```sql
SELECT distinct ct.entry, ct.name
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
WHERE clt.Reference = XXXXX;
```

### Find number of items and level statistics for items in a given RLT
This is useful when determining which creatures should have a particular RLT in their drop tables.
```sql
SELECT COUNT(rlt.Item), MIN(it.ItemLevel), MAX(it.ItemLevel), AVG(it.ItemLevel)
FROM `item_template` it 
JOIN `reference_loot_template` rlt ON it.entry = rlt.item 
WHERE rlt.entry = XXXXX;
```

### Recursively find an item by name
Note this is complex enough that Keira won't run it properly - you will need to run it from a MySQL command prompt. Thanks to @anguaive for this one.
```sql
SET @ITEM_NAME := 'insert name of item here';
SET @ITEM_ID := (SELECT `entry` FROM `item_template` WHERE `name` = @ITEM_NAME);

SELECT DISTINCT ct.name AS `creature`, @ITEM_NAME as `item` FROM (
    WITH RECURSIVE cte (`entry`, `item`, `reference`) AS (
    SELECT `entry`, `item`, `reference`
    FROM `reference_loot_template`
    WHERE `item` = @ITEM_ID
    UNION ALL
    SELECT r.entry, r.item, r.reference
    FROM `reference_loot_template` r
    INNER JOIN cte
    ON r.reference = cte.entry
    )
    SELECT clt.entry
    FROM cte
    JOIN `creature_loot_template` clt ON clt.reference = cte.entry
    UNION ALL
    SELECT entry
    FROM
    `creature_loot_template` 
    WHERE item = @ITEM_ID
) AS q
JOIN `creature_template` ct ON ct.lootid = q.entry
ORDER BY ct.name;
```

## Miscellaneous Issues
#### Find creature information from a spawn GUID
Bug reports sometimes just reference a GUID with no other information about an NPC. This will find the creature a GUID belongs to.
```sql
SELECT ct.entry, ct.name, ct.minlevel, ct.maxlevel
FROM `creature_template` ct 
JOIN `creature` c ON ct.entry = c.id
WHERE c.guid = XXXXX;
```

### Find all static creatures given a name
You can just use part of the NPC's name (as here, 'Gordunni') and it will find all NPCs with that string in their name.
```sql
SELECT c.guid, ct.name
FROM `creature` c
JOIN `creature_template` ct ON ct.entry = c.id
WHERE c.movementtype = 0 AND ct.name LIKE '%gordunni%';
```

### Find creatures that use a certain spell
Note this is a bit rough and ready, and only works if the spell is in their first action slot. In this case, XXXX is the spell ID.
```sql
SELECT ct.entry, ct.name, ct.maxlevel, ss.action_param1
FROM `creature_template` ct
JOIN `smart_scripts` ss ON ct.entry = ss.entryorguid
WHERE ss.action_param1 = XXXXX;
```

### Find average wander distance for a creature
Handy for fixing static creatures.
```sql
SELECT c.id, AVG(c.wander_distance)
FROM `creature` c
WHERE c.id = XXXX AND c.wander_distance > 0;
```

### Find other members of a node pool
Given a node GUID, find if it belongs to a node pool and list the other members.
```sql
SELECT * FROM `pool_gameobject` WHERE `pool_entry` IN (
SELECT `pool_entry` from `pool_gameobject` WHERE guid = XXXX);
```

### Find respawn timers for a class of object
Given a object's name, find the respawn timers for all spawns that match that name string.
```sql
SELECT got.name, go.guid, go.spawntimesecs
FROM `gameobject_template` got
JOIN `gameobject` go ON got.entry = go.id
WHERE name LIKE '%name-of-object%' 
ORDER BY go.spawntimesecs
```
