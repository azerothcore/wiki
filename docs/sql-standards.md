---
tableofcontents: 1
redirect_from: /Dealing-with-SQL-files
---

# SQL Standards

## Queries

### General standards

We always use backticks \` around table- and column names. \`creature_loot_template\`.

We always use single quotes around string values ' ' but NEVER around an integer.

### INSERT & DELETE

We always DELETE before an INSERT to ensure we always put fields in the query and that no errors occur.

Wrong:

```sql
INSERT INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');

REPLACE INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```

Correct:

```sql
DELETE FROM `creature_loot_template` WHERE `entry` = 3 AND `item` = 884;
INSERT INTO `creature_loot_template` (`Entry`, `Item`, `Reference`, `Chance`, `QuestRequired`, `LootMode`, `GroupId`, `MinCount`, `MaxCount`, `Comment`) VALUES 
(3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```
---

When performing DELETE queries, always specify more than one field when possible.

Wrong:

```sql
DELETE FROM `creature_loot_template` WHERE `item` = 884;
```

Correct:

```sql
DELETE FROM `creature_loot_template` WHERE `entry` = 3 AND `item` = 884;
```

### UPDATE

Make sure your queries are precise so you avoid changing something you do not want to edit.

Rule of thumb, always include all primary keys in your WHERE clause.

Wrong:

```sql
UPDATE `creature_loot_template` SET `Chance` = 100 WHERE `item` = 884;
```

Correct:

```sql
UPDATE `creature_loot_template` SET `Chance` = 100 WHERE `entry` = 3 AND `item` = 884;
```

### Variables

Variables can be good where you change the same entry in several places to avoid mistakes.

Before:

```sql
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = 7727;

DELETE FROM `smart_scripts` WHERE `entryorguid` = 7727 AND `source_type` = 0;
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES 
(7727, 0, 0, 0, 0, 0, 100, 0, 2000, 4000, 2000, 4000, 0, 11, 930, 64, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - In Combat - Cast \'Chain Lightning\''),
(7727, 0, 1, 0, 2, 0, 100, 1, 0, 50, 0, 0, 0, 11, 8499, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-50% Health - Cast \'Fire Nova\' (No Repeat)'),
(7727, 0, 2, 0, 2, 0, 100, 0, 0, 30, 0, 0, 0, 11, 8005, 64, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-30% Health - Cast \'Healing Wave\'');
```

After:

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


### Compact queries

We always keep the code as compact as possible to limit the size of the files and decrease the number of queries needed to run.

Wrong:

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

Correct:

```sql
DELETE FROM `table_1` WHERE `entry` IN (1000, 2000, 3000);

INSERT INTO `table_1` VALUES
(1000, ...),
(2000, ...),
(3000, ...);

UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` IN (1000, 2000, 3000);
```

### Flags & Bits

For fields in the database where we work with flags it is always preffered that we add or remove flags instead of overriding them.

Wrong:

```sql
UPDATE `creature_template` SET `mechanic_immune_mask` = 617299803 WHERE `entry` = 7727;
```

Correct:

```sql
-- Adding flags
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`|64|256|1024 WHERE `entry` = 7727;

-- Removing flags
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`&~(64|256|1024) WHERE `entry` = 7727;
```

## Tables and Columns

### Integers

We do not define the width of an integer when we create new columns. (Width is deprecated in later versions of MySQL 8)

```
TINYINT(M)   -> TINYINT
SMALLINT(M)  -> SMALLINT
INT(M)       -> INT
MEDIUMINT(M) -> MEDIUMINT
BIGINT(M)    -> BIGINT

BOOL         -> Never used, synonym for TINYINT. 0 = false <>0 = true
```

### Float, Double, Decimal

These data types cannot be UNSIGNED and therefore we use CHECK CONSTRAINTS instead. (UNSIGNED Float, Double, Decimal is deprecated in later versions of MySQL 8)

```
FLOAT UNSIGNED -> CHECK (`column`>=0)
```

### Character Encoding

We use UTF8MB4 where you would previously use UTF8 or UTF8MB3. (utf8 is an alias and utf8mb3 is deprecated in later versions of MySQL 8)

```
utf8    -> utf8mb4
utf8mb3 -> utf8mb4
```

To be able to support MariaDB alongside MySQL we are limited to using `utf8mb4_general_ci` as coallation.

### Check Constraints

You can see [here](https://github.com/Azerothcore/azerothcore-wotlk/blob/master/data/sql/base/db_auth/realmlist.sql) how check contraints are made.

All active Check Constraints can be found by using this query:

```sql
-- MySQL 8.0
SELECT * FROM information_schema.CHECK_CONSTRAINTS;

-- MySQL 5.7
SELECT * FROM information_schema.TABLE_CONSTRAINTS;
```

## Note for SQL reviewer

When we work with GUID's, make sure that we use as low entries as possible to fill out the gaps in the database. This can easily be done with tools like [Unused GUID Searcher](https://github.com/azerothcore/unused-guid-search).
