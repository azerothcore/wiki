---
tableofcontents: 1
redirect_from: /Dealing-with-SQL-files
---

# SQL Standards

## Queries

### General standards

We always use backticks \` around the table- and column names. \`creature_loot_template\`.

We always use single quotes around string values ' ' but NEVER around an integer.

We never include the database name in queries.

### INSERT & DELETE

We always DELETE before an INSERT to ensure we always put fields in the query and that no errors occur.

Your DELETE statement should always include at least one column with the PRIMARY key.

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

When performing DELETE queries, always specify more than one field. In particular, specify at least one primary key present in the table and another accompanying field.

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

Variables can be good when you change the same entry in several places to avoid mistakes.

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

We always aim to keep the code as compact as possible, reducing file size and minimising the number of queries required. While this is generally good practice, bundling queries in a way that complicates review is counterproductive. For instance, mixing different SAI entities makes the code significantly harder to review and more prone to user error, so try to keep the queries compact, but not at the expense of making them harder to review.

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

For fields in the database where we work with flags, it is always preferred that we add or remove flags instead of overriding them.

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

### Naming of tables and columns

For the most part, tables should be written in snake case, and columns should be written in upper camel case.

Tables:

```
broadcast_text
creature_loot_template
points_of_interest
```

Columns:

```
MaleText
QuestRequired
PositionX
```

In the case of column names with acronyms (e.g. GUID, ID, NPC, etc) the letters in the acronym should be uppercase.

Wrong:

```
Itemguid
DisplayId
RequiredNpcOrGoCount
```

Correct:

```
ItemGUID
DisplayID
RequiredNPCOrGOCount
```

### Integers

We do not define the width of an integer when we create new columns. (Width is deprecated in later versions of MySQL 8)

```
TINYINT(M)   -> TINYINT
SMALLINT(M)  -> SMALLINT
INT(M)       -> INT
BIGINT(M)    -> BIGINT

BOOL         -> Never used, a synonym for TINYINT. 0 = false <>0 = true
```

We never use MEDIUMINT. Use INT instead!

### Float, Double, Decimal

These data types cannot be UNSIGNED and therefore we use CHECK CONSTRAINTS instead. (UNSIGNED Float, Double, Decimal is deprecated in later versions of MySQL 8)

```
FLOAT UNSIGNED -> CHECK (`column`>=0)
```

### Check Constraints

You can see [here](https://github.com/Azerothcore/azerothcore-wotlk/blob/master/data/sql/base/db_auth/realmlist.sql) how check constraints are made.

All active Check Constraints can be found by using this query:

```sql
SELECT * FROM information_schema.CHECK_CONSTRAINTS;
```

### Charset

We always use `utf8mb4` as the charset

### Collation

We always use `utf8mb4_unicode_ci` as the collation

The only exception is where we use a character name, here we need to use `utf8mb4_bin` to allow the name to be accent-sensitive.

### Engine

We always use `InnoDB` as the engine

### Row Format

We always use `DEFAULT` as the row format

### Dummy script for table

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

## Note for SQL reviewer

When we work with GUIDs, make sure that we use as low entries as possible to fill out the gaps in the database. This can easily be done with tools like [Unused GUID Searcher](https://github.com/azerothcore/unused-guid-search).
