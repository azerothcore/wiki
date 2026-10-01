---
tableofcontents: 1
redirect_from: /cn/Dealing-with-SQL-files
---

# SQL 规范

## 查询语句

### 通用规范

我们始终在表名和列名周围使用反引号 \`。例如 \`creature_loot_template\`。

我们始终在字符串值周围使用单引号 ' '，但绝不用于整数。

我们绝不在查询中写数据库名。

### INSERT 与 DELETE

我们总是在 INSERT 之前先执行 DELETE，以确保查询中始终写入字段并且不会发生错误。

你的 DELETE 语句应始终至少包含一个带有 PRIMARY key（主键）的列。

错误示例：

```sql
INSERT INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');

REPLACE INTO `creature_loot_template` (3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```

正确示例：

```sql
DELETE FROM `creature_loot_template` WHERE `entry` = 3 AND `item` = 884;
INSERT INTO `creature_loot_template` (`Entry`, `Item`, `Reference`, `Chance`, `QuestRequired`, `LootMode`, `GroupId`, `MinCount`, `MaxCount`, `Comment`) VALUES 
(3, 884, 0, 40, 1, 1, 0, 1, 1, 'Comment');
```
---

执行 DELETE 查询时，务必指定多于一个字段。特别是，至少要指定表中存在的一个主键，以及另一个伴随字段。

错误示例：

```sql
DELETE FROM `creature_loot_template` WHERE `item` = 884;
```

正确示例：

```sql
DELETE FROM `creature_loot_template` WHERE `entry` = 3 AND `item` = 884;
```

### UPDATE

确保你的查询足够精确，以避免修改到不想编辑的内容。

经验法则：始终在 WHERE 子句中包含所有主键。

错误示例：

```sql
UPDATE `creature_loot_template` SET `Chance` = 100 WHERE `item` = 884;
```

正确示例：

```sql
UPDATE `creature_loot_template` SET `Chance` = 100 WHERE `entry` = 3 AND `item` = 884;
```

### Spawn 的 DELETE 与 UPDATE

对于 spawn 表（`creature`、`gameobject`），`DELETE` 和 `UPDATE` 语句都必须只作用于该表本身，并且在 `WHERE` 子句中同时按 `id` 和 `guid` 进行过滤。可以使用 `=`、`IN` 或 `BETWEEN`，但绝不能使用 `OR`。

错误示例：

```sql
UPDATE `creature` SET `spawntimesecs` = 300 WHERE `guid` = 12345;
```

正确示例：

```sql
UPDATE `creature` SET `spawntimesecs` = 300 WHERE `id` = 1234 AND `guid` = 12345;
```

### 变量

当你在多个地方修改同一个条目时，使用变量可以避免出错。

修改前：

```sql
UPDATE `creature_template` SET `AIName` = 'SmartAI' WHERE `entry` = 7727;

DELETE FROM `smart_scripts` WHERE `entryorguid` = 7727 AND `source_type` = 0;
INSERT INTO `smart_scripts` (`entryorguid`, `source_type`, `id`, `link`, `event_type`, `event_phase_mask`, `event_chance`, `event_flags`, `event_param1`, `event_param2`, `event_param3`, `event_param4`, `event_param5`, `action_type`, `action_param1`, `action_param2`, `action_param3`, `action_param4`, `action_param5`, `action_param6`, `target_type`, `target_param1`, `target_param2`, `target_param3`, `target_param4`, `target_x`, `target_y`, `target_z`, `target_o`, `comment`) VALUES 
(7727, 0, 0, 0, 0, 0, 100, 0, 2000, 4000, 2000, 4000, 0, 11, 930, 64, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - In Combat - Cast \'Chain Lightning\''),
(7727, 0, 1, 0, 2, 0, 100, 1, 0, 50, 0, 0, 0, 11, 8499, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-50% Health - Cast \'Fire Nova\' (No Repeat)'),
(7727, 0, 2, 0, 2, 0, 100, 0, 0, 30, 0, 0, 0, 11, 8005, 64, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 'Grimtotem Shaman - Between 0-30% Health - Cast \'Healing Wave\'');
```

修改后：

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


### 紧凑查询

我们始终力求让代码尽可能紧凑，以减小文件大小并尽量减少所需的查询数量。虽然这通常是好的做法，但将查询捆绑到让评审变得复杂的地步反而适得其反。例如，混合不同的 SAI 实体会使代码明显更难评审，也更容易让用户出错，所以请尽量让查询保持紧凑，但不要以牺牲可评审性为代价。

错误示例：

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

正确示例：

```sql
DELETE FROM `table_1` WHERE `entry` IN (1000, 2000, 3000);

INSERT INTO `table_1` VALUES
(1000, ...),
(2000, ...),
(3000, ...);

UPDATE `table_1` SET `field_1` = 'someValue' WHERE `entry` IN (1000, 2000, 3000);
```

### 标记与位（Flags & Bits）

对于数据库中需要使用标记的字段，我们总是倾向于添加或移除标记，而不是直接覆盖它们。

错误示例：

```sql
UPDATE `creature_template` SET `mechanic_immune_mask` = 617299803 WHERE `entry` = 7727;
```

正确示例：

```sql
-- 添加标记
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`|64|256|1024 WHERE `entry` = 7727;

-- 移除标记
UPDATE `creature_template` SET `mechanic_immune_mask`=`mechanic_immune_mask`&~(64|256|1024) WHERE `entry` = 7727;
```

## 表与列

### 表和列的命名

在大多数情况下，表名应使用蛇形命名法（snake case），列名应使用大驼峰命名法（upper camel case）。

表：

```
broadcast_text
creature_loot_template
points_of_interest
```

列：

```
MaleText
QuestRequired
PositionX
```

对于包含缩写（例如 GUID、ID、NPC 等）的列名，缩写中的字母应大写。

错误示例：

```
Itemguid
DisplayId
RequiredNpcOrGoCount
```

正确示例：

```
ItemGUID
DisplayID
RequiredNPCOrGOCount
```

### 整数

我们创建新列时不会定义整数的宽度。（在 MySQL 8 的较新版本中，宽度已被弃用）

```
TINYINT(M)   -> TINYINT
SMALLINT(M)  -> SMALLINT
INT(M)       -> INT
BIGINT(M)    -> BIGINT

BOOL         -> 从不使用，它是 TINYINT 的同义词。0 = false <>0 = true
```

我们从不使用 MEDIUMINT。请改用 INT！

### Float、Double、Decimal

这些数据类型不能是 UNSIGNED，因此我们改用 CHECK CONSTRAINTS（检查约束）。（在 MySQL 8 的较新版本中，UNSIGNED 的 Float、Double、Decimal 已被弃用）

```
FLOAT UNSIGNED -> CHECK (`column`>=0)
```

### 检查约束

你可以[在此处](https://github.com/Azerothcore/azerothcore-wotlk/blob/master/data/sql/base/db_auth/realmlist.sql)查看检查约束是如何编写的。

所有启用的检查约束都可以通过以下查询找到：

```sql
SELECT * FROM information_schema.CHECK_CONSTRAINTS;
```

### 字符集

我们始终使用 `utf8mb4` 作为字符集

### 排序规则

我们始终使用 `utf8mb4_unicode_ci` 作为排序规则

唯一的例外是当我们使用角色名称时，这里需要使用 `utf8mb4_bin` 以允许名称区分重音。

### 引擎

我们始终使用 `InnoDB` 作为存储引擎

### 行格式

我们始终使用 `DEFAULT` 作为行格式

### 建表参考脚本

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

## 给 SQL 评审者的提示

在处理 GUID 时，请确保尽量使用较低的条目来填补数据库中的空缺。这可以通过 [Unused GUID Searcher](https://github.com/azerothcore/unused-guid-search) 之类的工具轻松完成。
