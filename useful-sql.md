# useful-sql.md

## Useful SQL snippets:

### Table of Contents
  * [Introduction](#introduction)
  * [Loot and Reference Loot Issues](#loot-and-reference-loot-issues)
    + [Find what creatures drop an item directly](#find-what-creatures-drop-an-item-directly)
    + [Find which RLTs an item is in](#find-which-rlts-an-item-is-in)
    + [Find which creatures share a RLT](#find-which-creatures-share-a-rlt)
    + [Find number of items and level statistics for items in a given RLT](#find-number-of-items-and-level-statistics-for-items-in-a-given-rlt)
    + [Recursively find an item by name](#recursively-find-an-item-by-name)
  * [Miscellaneous Issues](#miscellaneous-issues)
    + [Find creature information from a spawn GUID](#find-creature-information-from-a-spawn-guid)
    + [Find all static creatures given a name](#find-all-static-creatures-given-a-name)
    + [Find creatures that use a certain spell](#find-creatures-that-use-a-certain-spell)
    + [Find average wander distance for a creature](#find-average-wander-distance-for-a-creature)
    + [Find other members of a node pool](#find-other-members-of-a node-pool)

### Introduction
These SQL queries are intended to be fast and easy-to-use tools that can help identify and troubleshoot problems in the AzerothCore database. They're here to be a quick reference to help when looking at DB-related problems. If anyone else has any similar useful queries, let me know and I'll add them. Similarly, if you have a common problem for which you'd like a query written, feel free to get in touch.

### Loot and Reference Loot Issues

#### Find what creatures drop an item directly
Note that this doesn't count items dropped from RLTs.
```
SELECT ct.name, clt.chance, ct.maxlevel, it.ItemLevel
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
JOIN `item_template` it ON clt.item = it.entry
WHERE it.entry = XXXXX;
```

#### Find which RLTs an item is in
```
SELECT rlt.entry, it.entry, it.name
FROM `reference_loot_template` rlt
JOIN `item_template` it ON rlt.Item = it.entry
WHERE it.entry = XXXXX;
```

#### Find which creatures share a RLT
Non-recursive.
```
SELECT distinct ct.entry, ct.name
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
WHERE clt.Reference = XXXXX;
```

#### Find number of items and level statistics for items in a given RLT
This is useful when determining which creatures should have a particular RLT in their drop tables.
```
SELECT COUNT(rlt.Item), MIN(it.ItemLevel), MAX(it.ItemLevel), AVG(it.ItemLevel)
FROM `item_template` it 
JOIN `reference_loot_template` rlt ON it.entry = rlt.item 
WHERE rlt.entry = XXXXX;
```

#### Recursively find an item by name
Note this is complex enough that Keira won't run it properly - you will need to run it from a MySQL command prompt. Thanks to @anguaive for this one.
```
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

### Miscellaneous Issues
#### Find creature information from a spawn GUID
Bug reports sometimes just reference a GUID with no other information about an NPC. This will find the creature a GUID belongs to.
```
SELECT ct.entry, ct.name, ct.minlevel, ct.maxlevel
FROM `creature_template` ct 
JOIN `creature` c ON ct.entry = c.id
WHERE c.guid = XXXXX;
```

#### Find all static creatures given a name
You can just use part of the NPC's name (as here, 'Gordunni') and it will find all NPCs with that string in their name.
```
SELECT c.guid, ct.name
FROM `creature` c
JOIN `creature_template` ct ON ct.entry = c.id
WHERE c.movementtype = 0 AND ct.name LIKE '%gordunni%';
```

#### Find creatures that use a certain spell
Note this is a bit rough and ready, and only works if the spell is in their first action slot. In this case, XXXX is the spell ID.
```
SELECT ct.entry, ct.name, ct.maxlevel, ss.action_param1
FROM `creature_template` ct
JOIN `smart_scripts` ss ON ct.entry = ss.entryorguid
WHERE ss.action_param1 = XXXXX;
```

#### Find average wander distance for a creature
Handy for fixing static creatures.
```
SELECT c.id, AVG(c.wander_distance)
FROM `creature` c
WHERE c.id = XXXX;
```

#### Find other members of a node pool
Given a node GUID, find if it belongs to a node pool and list the other members.
```
SELECT * FROM `pool_gameobject` WHERE `pool_entry` IN (
SELECT `pool_entry` from `pool_gameobject` WHERE guid = XXXX);
```
