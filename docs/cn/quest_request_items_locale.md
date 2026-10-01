# quest\_request\_items\_locale

**表：quest\_request\_items\_locale**

[<-返回至:World](database-world)

**表结构**

| Field               | Type       | Attribute | Key | Null | Default | Extra | Comment |
| ------------------- | ---------- | --------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]             | INT        | UNSIGNED  | PRI | NO   |         |       |         |
| [locale][2]         | VARCHAR(4) |           | PRI | NO   |         |       |         |
| [CompletionText][3] | text       |           |     | YES  | NULL    |       |         |
| [VerifiedBuild][4]  | SMALLINT   |           |     | NO   |         |       |         |

[1]: #id
[2]: #locale
[3]: #completiontext
[4]: #verifiedbuild

**字段说明**

### ID

任务 ID，取自 quest_template。

### locale

这是你想要进行翻译的语言。
你可以从以下选项中选择：

| ID  | Language |
| --- | -------- |
| 0   | enUS     |
| 1   | koKR     |
| 2   | frFR     |
| 3   | deDE     |
| 4   | zhCN     |
| 5   | zhTW     |
| 6   | esES     |
| 7   | esMX     |
| 8   | ruRU     |

### CompletionText

这是任务尚未完成时显示的文本。

### VerifiedBuild

### 示例
```sql
DELETE FROM `quest_request_items_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_request_items_locale` (`ID`, `locale`, `CompletionText`, `VerifiedBuild`) VALUES`ID`, `locale`, `CompletionText`, `VerifiedBuild`
(2, "esES", "Sí, $gpoderoso:poderosa; $c, he presentido tu llegada. Confío que tienes más noticias que darme sobre tu caza.", 0);
```
