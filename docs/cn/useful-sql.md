---
tableofcontents: 1
---

# 实用 SQL 片段

## 简介
这些 SQL 查询旨在作为快速易用的工具，帮助识别和排查 AzerothCore 数据库中的问题。它们可作为排查数据库相关问题时快速查阅的参考。

## 掉落与参考掉落（RLT）问题

### 查找哪些生物会直接掉落某物品
注意：这不包括通过 RLT（参考掉落表）掉落的物品。
```sql
SET @ITEMID := XXXX;

SELECT ct.name, clt.chance, ct.maxlevel, it.ItemLevel
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
JOIN `item_template` it ON clt.item = it.entry
WHERE it.entry = @ITEMID;
```

### 查找某物品出现在哪些 RLT 中
```sql
SET @ITEMID = XXXX;

SELECT rlt.entry, it.name
FROM `reference_loot_template` rlt
JOIN `item_template` it ON rlt.Item = it.entry
WHERE rlt.item = @ITEMID;
```

### 查找哪些生物共享同一个 RLT
非递归查询。
```sql
SET @RLTENTRY := XXXX;

SELECT distinct ct.entry, ct.name
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
WHERE clt.Reference = @RLTENTRY;
```

### 统计给定 RLT 中物品的数量与等级信息
在判断哪些生物的掉落表中应包含特定 RLT 时非常有用。
```sql
SET @RLTENTRY := XXXX;

SELECT COUNT(rlt.Item), MIN(it.ItemLevel), MAX(it.ItemLevel), AVG(it.ItemLevel)
FROM `item_template` it 
JOIN `reference_loot_template` rlt ON it.entry = rlt.item 
WHERE rlt.entry = @RLTENTRY;
```

### 按名称递归查找物品
注意：此查询较复杂，Keira 无法正确运行，你必须从 MySQL 命令行运行。感谢 @anguaive 提供此查询。
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

## 其他问题
#### 根据刷新 GUID 查找生物信息
Bug 报告中有时只提供一个 GUID，而没有任何关于 NPC 的其他信息。此查询可查找该 GUID 所属的生物。
```sql
SET @CGUID := XXXX;

SELECT ct.entry, ct.name, ct.minlevel, ct.maxlevel
FROM `creature_template` ct 
JOIN `creature` c ON ct.entry = c.id
WHERE c.guid = @CGUID;
```

### 根据名称查找所有静态生物
你可以使用 NPC 名称的一部分（例如这里的 'Gordunni'），它会查找所有名称中包含该字符串的 NPC。
```sql
SET @NAME := 'gordunni';

SELECT c.guid, ct.name
FROM `creature` c
JOIN `creature_template` ct ON ct.entry = c.id
WHERE c.movementtype = 0 AND ct.name LIKE '%@NAME%';
```

### 查找使用某个法术的生物
注意：此查询较为粗略，仅当该法术位于其第一个动作槽位时才会生效。此处 XXXX 为法术 ID。
```sql
SET @SPELLID := XXXX;

SELECT ct.entry, ct.name, ct.maxlevel, ss.action_param1
FROM `creature_template` ct
JOIN `smart_scripts` ss ON ct.entry = ss.entryorguid
WHERE ss.action_param1 = @SPELLID;
```

### 计算生物的平均游荡距离
可用于修复静态生物。
```sql
SET @CID := XXXX;

SELECT c.id, AVG(c.wander_distance)
FROM `creature` c
WHERE c.id = @CID AND c.wander_distance > 0;
```

### 查找节点池的其他成员
给定一个节点 GUID，查找它是否属于某个节点池，并列出其他成员。
```sql
SET @GUID := XXXX;

SELECT * FROM `pool_gameobject` WHERE `pool_entry` IN (
SELECT `pool_entry` from `pool_gameobject` WHERE guid = @GUID);
```

### 查找某类对象的刷新计时器
给定对象名称，查找所有匹配该名称字符串的刷新的刷新计时器。
```sql
SELECT got.name, go.guid, go.spawntimesecs
FROM `gameobject_template` got
JOIN `gameobject` go ON got.entry = go.id
WHERE name LIKE '%name-of-object%' 
ORDER BY go.spawntimesecs
```

### 根据角色 GUID 列出背包内的物品
给定角色 GUID，显示背包内容，包含物品实例中对应的数量以及物品模板中对应的名称。
```sql
SET @GUID := XXXX;

SELECT ci.*, ii.itemEntry, it.name, ii.count
FROM character_inventory ci
JOIN item_instance ii ON ci.item = ii.guid
JOIN acore_world.item_template it ON ii.itemEntry = it.entry
WHERE ci.guid = @GUID;
```
