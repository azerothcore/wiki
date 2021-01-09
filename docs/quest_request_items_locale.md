# quest\_request\_items\_locale

**Table: quest\_request\_items\_locale**

[<-Back-to:World](database-world.md)

**Structure**

| Field               | Type        | Attribute | Key | Null | Default | Extra | Comment |
|---------------------|-------------|-----------|-----|------|---------|-------|---------|
| [ID][1]             | int(10)     | unsigned  | PRI | NO   |         |       |         |
| [locale][2]         | varchar(4)  |           | PRI | NO   |         |       |         |
| [CompletionText][3] | text        |           |     | YES  | NULL    |       |         |
| [VerifiedBuild][4]  | smallint(6) |           |     | NO   |         |       |         |

[1]: #id
[2]: #locale
[3]: #completiontext
[4]: #verifiedbuild

**Description of the fields**

### ID

Is the quest ID, obtained from quest_template

### locale

It is the language in which you want to make the translation.
You can choose from the following:

| ID | Language |
|----|----------|
| 0  | enUS     |
| 1  | koKR     |
| 2  | frFR     |
| 3  | deDE     |
| 4  | zhCN     |
| 5  | zhTW     |
| 6  | esES     |
| 7  | esMX     |
| 8  | ruRU     |

### CompletionText

It is the text that is shown, while the quest is not completed.

### VerifiedBuild

### Example
```sql
DELETE FROM `quest_request_items_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_request_items_locale` (`ID`, `locale`, `CompletionText`, `VerifiedBuild`) VALUES`ID`, `locale`, `CompletionText`, `VerifiedBuild`
(2, "esES", "Sí, $gpoderoso:poderosa; $c, he presentido tu llegada. Confío que tienes más noticias que darme sobre tu caza.", 0);
```
