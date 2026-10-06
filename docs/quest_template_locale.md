# quest\_template\_locale

[<-Back-to:World](database-world)

**The \`quest\_template\_locale\` table**

This table is used to provide to localized clients with localized string for quest templates.

**Table: quest\_template\_locale's Structure**

| Field                             | Type       |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                         | INT        | UNSIGNED | NO   | PRI | 0       |       |         |
| [locale](#locale)                 | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Title](#title)                   | TEXT       |          | YES  |     | NULL    |       |         |
| [Details](#details)               | TEXT       |          | YES  |     | NULL    |       |         |
| [Objectives](#objectives)         | TEXT       |          | YES  |     | NULL    |       |         |
| [EndText](#endtext)               | TEXT       |          | YES  |     | NULL    |       |         |
| [CompletedText](#completedtext)   | TEXT       |          | YES  |     | NULL    |       |         |
| [ObjectiveText1](#objectivetext1) | TEXT       |          | YES  |     | NULL    |       |         |
| [ObjectiveText2](#objectivetext2) | TEXT       |          | YES  |     | NULL    |       |         |
| [ObjectiveText3](#objectivetext3) | TEXT       |          | YES  |     | NULL    |       |         |
| [ObjectiveText4](#objectivetext4) | TEXT       |          | YES  |     | NULL    |       |         |
| [VerifiedBuild](#verifiedbuild)   | INT        |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

This is the ID of the quest to be translated.

### locale

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

### Title

Translation of [quest\_template.LogTitle](quest_template#logtitle).

### Details

Translation of [quest\_template.QuestDescription](quest_template#questdescription).

### Objectives

Translation of [quest\_template.LogDescription](quest_template#logdescription).

### EndText

Translation of [quest\_template.AreaDescription](quest_template#areadescription).

### CompletedText

Translation of [quest\_template.QuestCompletionLog](quest_template#questcompletionlog).

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

This field is used to determine if this translation originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.

### Example
```sql
DELETE FROM `quest_template_locale` WHERE `ID`=62 AND `locale`="esES";

INSERT INTO `quest_template_locale` (`ID`, `locale`, `Title`, `Details`, `Objectives`, `EndText`, `CompletedText`, `ObjectiveText1`, `ObjectiveText2`, `ObjectiveText3`, `ObjectiveText4`, `VerifiedBuild`) VALUES
(62, "esES", "La Mina Abisal", "¡La mina de Villanorte no es la única que tiene problemas! Según mis informes, la Mina Abisal de Elwynn también ha sido ocupada por los kóbolds.$B$BExplora la mina y comprueba la veracidad de mis informes. Luego vuelve aquí. La mina está hacia el sur de Villadorada, entre La Granja Pedregosa y la granja Maclure.", "Explora la Mina Abisal y vuelve junto al alguacil Dughan a Villadorada.", "Explora la Mina Abisal", "Vuelve con: Alguacil Dughan. Zona: Villadorada, Bosque de Elwynn.", "", "", "", "", 18019);
```
