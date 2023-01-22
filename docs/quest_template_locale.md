# quest\_template\_locale

[<-Back-to:World](database-world.md)

**The \`quest\_template\_locale\` table**

This table is used to provide to localized clients with localized string for quest templates.

**Structure**

| Field                   | Type         | Attribute | Key | Null | Default | Extra | Comment |
|-------------------------|--------------|-----------|-----|------|---------|-------|---------|
| [ID][1]                 | MEDIUMINT    | UNSIGNED  | PRI | NO   | 0       |       |         |
| [Locale][2]             | VARCHAR(4)   |           | PRI | NO   |         |       |         |
| [LogTitle][3]           | TEXT         |           |     | YES  |         |       |         |
| [QuestDescription][4]   | TEXT         |           |     | YES  |         |       |         |
| [LogDescription][5]     | TEXT         |           |     | YES  |         |       |         |
| [AreaDescription][6]    | TEXT         |           |     | YES  |         |       |         |
| [QuestCompletionLog][7] | TEXT         |           |     | YES  |         |       |         |
| [ObjectiveText1][8]     | TEXT         |           |     | YES  |         |       |         |
| [ObjectiveText2][9]     | TEXT         |           |     | YES  |         |       |         |
| [ObjectiveText3][10]    | TEXT         |           |     | YES  |         |       |         |
| [ObjectiveText4][11]    | TEXT         |           |     | YES  |         |       |         |
| [VerifiedBuild][12]     | SMALLINT     |           |     | YES  | 0       |       |         |

[1]: #id
[2]: #locale
[3]: #logtitle
[4]: #questdescription
[5]: #logdescription
[6]: #areadescription
[7]: #questcompletionlog
[8]: #objectivetext1
[9]: #objectivetext2
[10]: #objectivetext3
[11]: #objectivetext4
[12]: #verifiedbuild

**Description of the fields**

### ID

This is the ID of the quest to be translated.

### Locale

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

### LogTitle

The title of the quest in the respective language.

### QuestDescription

Detail of the quest.

### LogDescription

This is the text that is displayed when it is completed.

### AreaDescription

This is the text that is displayed until the quest is completed.

### QuestCompletionLog

This is the text that is displayed in the quest log when the quest is completed.

### ObjectiveText1

This is objective 1 of the search.
In other words, it is the text that accompanies the counters.

### ObjectiveText2

This is objective 2 of the search.
In other words, it is the text that accompanies the counters.

### ObjectiveText3

This is objective 3 of the search.
In other words, it is the text that accompanies the counters.

### ObjectiveText4

This is objective 4 of the search.
In other words, it is the text that accompanies the counters.

### VerifiedBuild

This is the game build the quest information was sniffed/parsed from.

### Example
```sql
DELETE FROM `quest_template_locale` WHERE `ID`=62 AND `Locale`="esES";

INSERT INTO `quest_template_locale` (`ID`, `Locale`, `LogTitle`, `QuestDescription`, `LogDescription`, `AreaDescription`, `QuestCompletionLog`, `ObjectiveText1`, `ObjectiveText2`, `ObjectiveText3`, `ObjectiveText4`, `VerifiedBuild`) VALUES
(62, "esES", "La Mina Abisal", "¡La mina de Villanorte no es la única que tiene problemas! Según mis informes, la Mina Abisal de Elwynn también ha sido ocupada por los kóbolds.$B$BExplora la mina y comprueba la veracidad de mis informes. Luego vuelve aquí. La mina está hacia el sur de Villadorada, entre La Granja Pedregosa y la granja Maclure.", "Explora la Mina Abisal y vuelve junto al alguacil Dughan a Villadorada.", "Explora la Mina Abisal", "Vuelve con: Alguacil Dughan. Zona: Villadorada, Bosque de Elwynn.", "", "", "", "", 18019);
```
