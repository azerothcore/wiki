# quest\_poi\_points

[<-Back-to:World](database-world)

**The \`quest\_poi\_points\` table**

Comes from sniffs. Visually speaking, this table is used to identify the X and Y coordinates on the map (not the minimap - the main map) where a quest's question mark should appear. Use the ".gps" command where you are standing to find these coordinates. In order to see changes, ".reload quest\_poi", close Wow.exe, then delete your cache folder.

**Table Structure**

| Field              | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [questid][1]       | INT      | unasigned  | PRI | NO   | 0       |       |         |
| [idx2][2]          | INT      | unasigned  | PRI | NO   | 0       |       |         |
| [x][3]             | INT      | unasigned  |     | NO   | 0       |       |         |
| [y][4]             | INT      | unasigned  |     | NO   | 0       |       |         |
| [VerifiedBuild][5] | SMALLINT | unasigned  |     | YES  | NULL    |       |         |

[1]: #questid
[2]: #idx2
[3]: #x
[4]: #y
[5]: #verifiedbuild

**Description of the fields**

### questid

The Quest Id from [quest\_poi.questid](quest_poi#questid)

### idx1

Used to group multiple entries from quest\_poi.id. You must manually increment this value by 1 for each new row in quest\_poi\_point with the same questId (0, 1, 2, 3...).

### idx2

Used to group multiple entries in the quest poi points to draw the polygon for that point of interest. The actual points are the corners of each polygon.

Example quest: Secreat Communication.

| QuestID | idx1 | idx2 | x     | y    | VerifiedBuild |
| ------- | ---- | ---- | ----- | ---- | ------------- |
| 8318    | 3    | 0    | -6231 | -51  | 0             |
| 8318    | 3    | 1    | -6236 | -19  | 0             |
| 8318    | 3    | 2    | -6241 | -52  | 0             |
| 8318    | 3    | 3    | -6316 | -282 | 0             |
| 8318    | 3    | 4    | -6413 | -282 | 0             |
| 8318    | 3    | 5    | -6483 | -250 | 0             |
| 8318    | 3    | 6    | -6483 | -217 | 0             |
| 8318    | 3    | 7    | -6326 | -7   | 0             |

**These points are all the little corners on the blue box. idx1 represents an area defined by the points of idx2 to draw the shape.**

![image](https://user-images.githubusercontent.com/1884642/119476187-bca11b00-bd45-11eb-95e5-876960f24457.png)

### x

The X position of the question mark on the map.

### y

The Y position of the question mark on the map.

### VerifiedBuild

VerifiedBuild
