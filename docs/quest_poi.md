# quest\_poi

[<-Back-to:World](database-world)

**The \`quest\_poi\` table**

Comes from sniffs.

**Table: quest\_poi's Structure**

| Field                             | Type |          | Null | Key | Default | Extra | Comment |
| :-------------------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [QuestID](#questid)               | INT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [id](#id)                         | INT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [ObjectiveIndex](#objectiveindex) | INT  |          | NO   |     | 0       |       |         |
| [MapID](#mapid)                   | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [WorldMapAreaId](#worldmapareaid) | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [Floor](#floor)                   | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [Priority](#priority)             | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [Flags](#flags)                   | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)   | INT  |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### QuestID

The Quest Id from [quest\_template.id](quest_template#id)

### id

Used to group multiple entries from quest\_poi\_points.Idx1 it is the id of the POI.

### ObjectiveIndex

if -1 than position of npc where you can complete quest

### MapID

The Map id from [Map.dbc](map)

### WorldMapAreaId

The ID from [WorldMapArea.dbc](https://wowdev.wiki/DB/WorldMapArea).

### Floor

This is the ID from [AreaTable.dbc](areatable) of the POI.

### Priority

Sent to the client with the POI. Its exact effect is not known.

### Flags

Sent to the client with the POI. Its exact effect is not known.

### VerifiedBuild

Client build this row was verified against (from WDB/ADB extraction). `NULL` if not applicable.
