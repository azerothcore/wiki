---
tableofcontents: 1
---

# Snippets SQL útiles

## Introducción
Estas consultas SQL están pensadas para ser herramientas rápidas y fáciles de usar que ayuden a identificar y solucionar problemas en la base de datos de AzerothCore. Están aquí como una referencia rápida para ayudar al examinar problemas relacionados con la BD.

## Problemas de loot y reference loot

### Encontrar qué creatures dropean un item directamente
Ten en cuenta que esto no cuenta los items dropeados desde RLTs.
```sql
SET @ITEMID := XXXX;

SELECT ct.name, clt.chance, ct.maxlevel, it.ItemLevel
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
JOIN `item_template` it ON clt.item = it.entry
WHERE it.entry = @ITEMID;
```

### Encontrar en qué RLTs está un item
```sql
SET @ITEMID = XXXX;

SELECT rlt.entry, it.name
FROM `reference_loot_template` rlt
JOIN `item_template` it ON rlt.Item = it.entry
WHERE rlt.item = @ITEMID;
```

### Encontrar qué creatures comparten un RLT
No recursivo.
```sql
SET @RLTENTRY := XXXX;

SELECT distinct ct.entry, ct.name
FROM `creature_template` ct
JOIN `creature_loot_template` clt ON ct.lootid = clt.entry
WHERE clt.Reference = @RLTENTRY;
```

### Encontrar el número de items y estadísticas de nivel para los items de un RLT dado
Esto es útil al determinar qué creatures deberían tener un RLT concreto en sus tablas de drop.
```sql
SET @RLTENTRY := XXXX;

SELECT COUNT(rlt.Item), MIN(it.ItemLevel), MAX(it.ItemLevel), AVG(it.ItemLevel)
FROM `item_template` it 
JOIN `reference_loot_template` rlt ON it.entry = rlt.item 
WHERE rlt.entry = @RLTENTRY;
```

### Encontrar recursivamente un item por nombre
Ten en cuenta que esto es lo suficientemente complejo como para que Keira no lo ejecute correctamente: debes ejecutarlo desde un prompt de comandos de MySQL. Gracias a @anguaive por este.
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

## Problemas varios
#### Encontrar información de una creature a partir de un GUID de spawn
Los reportes de bugs a veces solo referencian un GUID sin ninguna otra información sobre un NPC. Esto encontrará la creature a la que pertenece un GUID.
```sql
SET @CGUID := XXXX;

SELECT ct.entry, ct.name, ct.minlevel, ct.maxlevel
FROM `creature_template` ct 
JOIN `creature` c ON ct.entry = c.id
WHERE c.guid = @CGUID;
```

### Encontrar todas las creatures estáticas dado un nombre
Podrías usar parte del nombre del NPC (como aquí, 'Gordunni') y encontrará todos los NPCs con esa cadena en su nombre.
```sql
SET @NAME := 'gordunni';

SELECT c.guid, ct.name
FROM `creature` c
JOIN `creature_template` ct ON ct.entry = c.id
WHERE c.movementtype = 0 AND ct.name LIKE '%@NAME%';
```

### Encontrar creatures que usan un hechizo determinado
Ten en cuenta que esto es un poco tosco, y solo funciona si el hechizo está en su primer slot de acción. En este caso, XXXX es el ID del hechizo.
```sql
SET @SPELLID := XXXX;

SELECT ct.entry, ct.name, ct.maxlevel, ss.action_param1
FROM `creature_template` ct
JOIN `smart_scripts` ss ON ct.entry = ss.entryorguid
WHERE ss.action_param1 = @SPELLID;
```

### Encontrar la distancia media de deambulación de una creature
Podría usarse para arreglar creatures estáticas.
```sql
SET @CID := XXXX;

SELECT c.id, AVG(c.wander_distance)
FROM `creature` c
WHERE c.id = @CID AND c.wander_distance > 0;
```

### Encontrar otros miembros de un pool de nodos
Dado un GUID de nodo, averigua si pertenece a un pool de nodos y lista los demás miembros.
```sql
SET @GUID := XXXX;

SELECT * FROM `pool_gameobject` WHERE `pool_entry` IN (
SELECT `pool_entry` from `pool_gameobject` WHERE guid = @GUID);
```

### Encontrar los temporizadores de respawn de una clase de objeto
Dado el nombre de un objeto, encuentra los temporizadores de respawn para todos los spawns que coinciden con esa cadena de nombre.
```sql
SELECT got.name, go.guid, go.spawntimesecs
FROM `gameobject_template` got
JOIN `gameobject` go ON got.entry = go.id
WHERE name LIKE '%name-of-object%' 
ORDER BY go.spawntimesecs
```

### Listar los items dentro del inventario según el GUID del personaje
Dado un GUID de personaje, muestra el inventario con el count correspondiente dentro del item instance y el nombre correspondiente dentro del item template.
```sql
SET @GUID := XXXX;

SELECT ci.*, ii.itemEntry, it.name, ii.count
FROM character_inventory ci
JOIN item_instance ii ON ci.item = ii.guid
JOIN acore_world.item_template it ON ii.itemEntry = it.entry
WHERE ci.guid = @GUID;
```
