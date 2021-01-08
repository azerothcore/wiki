# quest\_poi

[<-Back-to:World](database-world.md)

**The \`quest\_poi\` table**

Comes from sniffs.

**Structure**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
|---------------------|---------|------------|-----|------|---------|-------|---------|
| [QuestID][1]        | int(10) | unsigned   | PRI | NO   | 0       |       |         |
| [id][2]             | int(10) | unsigned   | PRI | NO   | 0       |       |         |
| [ObjectiveIndex][3] | int(10) | unsigned   |     | NO   | 0       |       |         |
| [MapID][4]          | int(10) | unsigned   |     | NO   | 0       |       |         |
| [WorldMapAreaId][5] | int(10) | unsigned   |     | NO   | 0       |       |         |
| [Floor][6]          | int(10) | unsigned   |     | NO   | 0       |       |         |
| [Priority][7]       | int(10) | unsigned   |     | NO   | 0       |       |         |
| [Flags][8]          | int(10) | unsigned   |     | NO   | 0       |       |         |

[1]: #questid
[2]: #id
[3]: #objectiveindex
[4]: #mapid
[5]: #worldmapareaid
[6]: #floor
[7]: #priority
[8]: #flags

**Description of the fields**

### QuestID

The Quest Id from [quest\_template.id](quest_template#id)

### id

Used to group multiple entries from quest\_poi\_points.id it is the id of the POI.

### ObjectiveIndex

if -1 than position of npc where you can complete quest

### MapID

The Map id from [Map.dbc](Map)

### WorldMapAreaId

The ID from [WorldMapArea.dbc](WorldMapArea).

### Floor

This is the AreaID of the POI.

### Priority

`field-no-description|7`

### Flags

`field-no-description|8`
