---
tableofcontents: 1
redirect_from: /Dealing-with-SQL-files
---

# Estándares de SQL

## Consultas

### Estándares generales

Siempre usamos backticks \` alrededor de los nombres de tabla y columna. \`creature_loot_template\`.

Siempre usamos comillas simples alrededor de los valores de cadena ' ', pero NUNCA alrededor de un entero.

Nunca incluimos el nombre de la base de datos en las consultas.

### INSERT & DELETE

Siempre hacemos DELETE antes de un INSERT para asegurar que siempre ponemos los campos en la consulta y que no ocurren errores.

Tu sentencia DELETE debería incluir siempre al menos una columna con la clave PRIMARY.

Incorrecto:

```sql
INSERT INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');

REPLACE INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```

Correcto:

```sql
DELETE FROM `creature_loot_template` WHERE `entry` = 3 AND `item` = 884;
INSERT INTO `creature_loot_template` (`Entry`, `Item`, `Reference`, `Chance`, `QuestRequired`, `LootMode`, `GroupId`, `MinCount`, `MaxCount`, `Comment`) VALUES 
(3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```
---

Al realizar consultas DELETE, especifica siempre más de un campo. En particular, especifica al menos una clave primaria presente en la tabla y otro campo acompañante.

Incorrecto:

```sql
DELETE FROM `creature_loot_template` WHERE `item` = 884;
```

Correcto:

```sql
DELETE FROM `creature_loot_template` WHERE `entry` = 3 AND `item` = 884;
```

### UPDATE

Asegúrate de que tus consultas sean precisas para evitar cambiar algo que no querías editar.

Como regla general, incluye siempre todas las claves primarias en tu cláusula WHERE.

Incorrecto:

```sql
UPDATE `creature_loot_template` SET `Chance` = 100 WHERE `item` = 884;
```

Correcto:

```sql
UPDATE `creature_loot_template` SET `Chance` = 100 WHERE `entry` = 3 AND `item` = 884;
```

### Variables

Las variables pueden ser buenas cuando cambias la misma entry en varios lugares, para evitar errores.

Antes:

```sql
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = 7727;

DELETE FROM `smart_scripts` WHERE `entryorguid` = 7727 AND `source_type` = 0;
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES 
(7727, 0, 0, 0, 0, 0, 100, 0, 2000, 4000, 2000, 4000, 0, 11, 930, 64, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - In Combat - Cast \'Chain Lightning\''),
(7727, 0, 1, 0, 2, 0, 100, 1, 0, 50, 0, 0, 0, 11, 8499, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-50% Health - Cast \'Fire Nova\' (No Repeat)'),
(7727, 0, 2, 0, 2, 0, 100, 0, 0, 30, 0, 0, 0, 11, 8005, 64, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-30% Health - Cast \'Healing Wave\'');
```

Después:

```sql
-- Grimtotem Shaman SAI
SET @ENTRY := 7727;
SET @SPELL1 := 930;
SET @SPELL2 := 8499;
SET @SPELL3 := 8005;

UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = @ENTRY;

DELETE FROM `smart_scripts` WHERE `entryorguid` = @ENTRY AND `source_type` = 0;
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES 
(@ENTRY, 0, 0, 0, 0, 0, 100, 0, 2000, 4000, 2000, 4000, 0, 11, @SPELL1, 64, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - In Combat - Cast \'Chain Lightning\''),
(@ENTRY, 0, 1, 0, 2, 0, 100, 1, 0, 50, 0, 0, 0, 11, @SPELL2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-50% Health - Cast \'Fire Nova\' (No Repeat)'),
(@ENTRY, 0, 2, 0, 2, 0, 100, 0, 0, 30, 0, 0, 0, 11, @SPELL3, 64, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-30% Health - Cast \'Healing Wave\'');
```


### Consultas compactas

Siempre buscamos mantener el código lo más compacto posible, reduciendo el tamaño del archivo y minimizando el número de consultas necesarias. Aunque esto es generalmente una buena práctica, agrupar consultas de una forma que complique la revisión es contraproducente. Por ejemplo, mezclar diferentes entidades SAI hace el código significativamente más difícil de revisar y más propenso a errores del usuario, así que intenta mantener las consultas compactas, pero no a costa de hacerlas más difíciles de revisar.

Incorrecto:

```sql
DELETE FROM `table_1` WHERE `entry` = 1000;
DELETE FROM `table_1` WHERE `entry` = 2000;
DELETE FROM `table_1` WHERE `entry` = 3000;


INSERT INTO `table_1` VALUES (1000, ...);
INSERT INTO `table_1` VALUES (2000, ...);
INSERT INTO `table_1` VALUES (3000, ...);

UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` = 1000;
UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` = 2000;
UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` = 3000;
```

Correcto:

```sql
DELETE FROM `table_1` WHERE `entry` IN (1000, 2000, 3000);

INSERT INTO `table_1` VALUES
(1000, ...),
(2000, ...),
(3000, ...);

UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` IN (1000, 2000, 3000);
```

### Flags y bits

Para los campos de la base de datos donde trabajamos con flags, siempre es preferible añadir o quitar flags en lugar de sobrescribirlos.

Incorrecto:

```sql
UPDATE `creature_template` SET `mechanic_immune_mask` = 617299803 WHERE `entry` = 7727;
```

Correcto:

```sql
-- Adding flags
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`|64|256|1024 WHERE `entry` = 7727;

-- Removing flags
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`&~(64|256|1024) WHERE `entry` = 7727;
```

## Tablas y columnas

### Nomenclatura de tablas y columnas

En su mayor parte, las tablas deben escribirse en snake case, y las columnas deben escribirse en upper camel case.

Tablas:

```
broadcast_text
creature_loot_template
points_of_interest
```

Columnas:

```
MaleText
QuestRequired
PositionX
```

En el caso de nombres de columna con acrónimos (p. ej. GUID, ID, NPC, etc.) las letras del acrónimo deben ir en mayúsculas.

Incorrecto:

```
Itemguid
DisplayId
RequiredNpcOrGoCount
```

Correcto:

```
ItemGUID
DisplayID
RequiredNPCOrGOCount
```

### Enteros

No definimos el ancho de un entero cuando creamos nuevas columnas. (El ancho está deprecado en versiones posteriores de MySQL 8)

```
TINYINT(M)   -> TINYINT
SMALLINT(M)  -> SMALLINT
INT(M)       -> INT
BIGINT(M)    -> BIGINT

BOOL         -> Never used, a synonym for TINYINT. 0 = false <>0 = true
```

¡Nunca usamos MEDIUMINT. Usa INT en su lugar!

### Float, Double, Decimal

Estos tipos de dato no pueden ser UNSIGNED y, por tanto, usamos CHECK CONSTRAINTS en su lugar. (UNSIGNED Float, Double, Decimal está deprecado en versiones posteriores de MySQL 8)

```
FLOAT UNSIGNED -> CHECK (`column`>=0)
```

### Check Constraints

Puedes ver [aquí](https://github.com/Azerothcore/azerothcore-wotlk/blob/master/data/sql/base/db_auth/realmlist.sql) cómo se hacen los check constraints.

Todos los check constraints activos se pueden encontrar usando esta consulta:

```sql
SELECT * FROM information_schema.CHECK_CONSTRAINTS;
```

### Charset

Siempre usamos `utf8mb4` como charset

### Collation

Siempre usamos `utf8mb4_unicode_ci` como collation

La única excepción es donde usamos un nombre de personaje; aquí necesitamos usar `utf8mb4_bin` para permitir que el nombre sea sensible a los acentos.

### Engine

Siempre usamos `InnoDB` como engine

### Row Format

Siempre usamos `DEFAULT` como row format

### Script de ejemplo para una tabla

```sql
DROP TABLE IF EXISTS `our_table_name`;
CREATE TABLE `our_table_name` (
  `aColumnName` INT UNSIGNED NOT NULL DEFAULT '69' COMMENT 'ColumnComment',
  `aSecondName` VARCHAR(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`aColumnName`),
  CONSTRAINT `our_table_name_chk_1` CHECK (`aColumnName` >= 0)
)
COMMENT = 'TableComment'
CHARSET = utf8mb4
COLLATE = utf8mb4_unicode_ci
ENGINE = InnoDB
ROW_FORMAT = DEFAULT
;
```

## Nota para el revisor de SQL

Cuando trabajamos con GUIDs, asegúrate de que usamos entries lo más bajos posible para rellenar los huecos en la base de datos. Esto se puede hacer fácilmente con herramientas como [Unused GUID Searcher](https://github.com/azerothcore/unused-guid-search).
