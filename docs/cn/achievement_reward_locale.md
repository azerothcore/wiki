# achievement\_reward\_locale

[<-返回至:World](database-world)

**`achievement\_reward\_locale` 表**

此表用于存储 `achievement_reward` 表的翻译，以便游戏客户端可以用不同的语言显示这些消息。

**表结构**

| Field        | Type       | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ---------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]      | MEDIUMINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Locale][2]  | VARCHAR(4) |            | PRI | NO   |         |       |         |
| [Subject][3] | text       |            |     | YES  |         |       |         |
| [Text][4]    | text       |            |     | YES  |         |       |         |

[1]: #id
[2]: #locale
[3]: #subject
[4]: #text

**字段说明**

### ID

这是从 `achievement_reward` 获得的成就的 [ID](achievement_reward#id)

### Locale

这是游戏客户端的语言。

| ID  | 语言    |
| --- | ------- |
| 0   | enUS    |
| 1   | koKR    |
| 2   | frFR    |
| 3   | deDE    |
| 4   | zhCN    |
| 5   | zhTW    |
| 6   | esES    |
| 7   | esMX    |
| 8   | ruRU    |

### Subject

这是 `achievement_reward` 表中 [Subject](achievement_reward#subject) 列的文本

### Text

这是 `achievement_reward` 表中 [Body](achievement_reward#body) 列的文本

### 示例
```sql
DELETE FROM `achievement_reward_locale` WHERE `ID`=13 AND `Locale`="esES";
INSERT INTO `achievement_reward_locale` (`ID`, `Locale`, `Subject`, `Text`) VALUES
(13, "esES", "Nivel 80", "Alcanza el nivel 80.");
```
