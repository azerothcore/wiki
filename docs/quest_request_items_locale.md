# quest\_request\_items\_locale

[<-Back-to:World](database-world)

Holds translations of the completion text in [quest_request_items](quest_request_items).

**Table: quest\_request\_items\_locale's Structure**

| Field                             | Type       |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                         | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)                 | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [CompletionText](#completiontext) | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild)   | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

Is the quest ID, obtained from quest_template

### locale

It is the language in which you want to make the translation.
You can choose from the following:

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

It is the text that is shown, while the quest is not completed.

### VerifiedBuild

This field is used to determine if this translation originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

### Example
```sql
DELETE FROM `quest_request_items_locale` WHERE `ID`=2 AND `locale`='esES';
INSERT INTO `quest_request_items_locale` (`ID`, `locale`, `CompletionText`, `VerifiedBuild`) VALUES`ID`, `locale`, `CompletionText`, `VerifiedBuild`
(2, "esES", "Sí, $gpoderoso:poderosa; $c, he presentido tu llegada. Confío que tienes más noticias que darme sobre tu caza.", 0);
```
