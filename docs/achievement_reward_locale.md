# achievement\_reward\_locale

[<-Back-to:World](database-world.md)

**The \`achievement\_reward\_locale\` table**

**Structure**

| Field   | Type         | Attributes | Collation       | Null | Key | Default | Extra | Comment |
|---------|--------------|------------|-----------------|------|-----|---------|-------|---------|
| ID      | mediumint(8) | unsigned   |                 | NO   | PRI | 0       |       |         |
| Locale  | varchar(4)   |            | utf8_general_ci | NO   | PRI | (NULL)  |       |         |
| Subject | text         |            | utf8_general_ci | YES  |     | (NULL)  |       |         |
| Text    | text         |            | utf8_general_ci | YES  |     | (NULL)  |       |         |

**Description of the fields**

### ID

It is the ID of the achievement obtained from `achievement_reward`

### Locale

This is the language of the gaming client.

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

### Subject

It is the text of the column `Subject` of the table `achievement_reward`

### Text

It is the text of the column `Body` of the table `achievement_reward`
