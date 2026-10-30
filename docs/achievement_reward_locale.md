# achievement\_reward\_locale

[<-Back-to:World](database-world)

**The \`achievement\_reward\_locale\` table**

It is the table that stores the translations of the table `achievement_reward`, so that the game client can display the messages in different languages.

**Table: achievement\_reward\_locale's Structure**

| Field               | Type       |          | Null | Key | Default | Extra | Comment |
| :------------------ | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)           | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [Locale](#locale)   | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Subject](#subject) | TEXT       |          | YES  |     | NULL    |       |         |
| [Text](#text)       | TEXT       |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

It is the [ID](achievement_reward#id) of the achievement obtained from `achievement_reward`

### Locale

This is the language of the gaming client.

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

### Subject

It is the text of the column [Subject](achievement_reward#subject) of the table `achievement_reward`

### Text

It is the text of the column [Body](achievement_reward#body) of the table `achievement_reward`

### Example
```sql
DELETE FROM `achievement_reward_locale` WHERE `ID`=13 AND `Locale`="esES";
INSERT INTO `achievement_reward_locale` (`ID`, `Locale`, `Subject`, `Text`) VALUES
(13, "esES", "Nivel 80", "Alcanza el nivel 80.");
```
