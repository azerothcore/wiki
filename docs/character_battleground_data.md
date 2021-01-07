# character\_battleground\_data

[<-Back-to:Characters](database-characters.md)

**The \`character\_battleground\_data\` table**

This table holds information for each character in a battleground. Also hold info about their last position before joining the battleground.

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment                  |
|------------------|--------------|------------|-----|------|---------|-------|--------------------------|
| [guid][1]        | int(10)      | unsigned   | PRI | NO   | 0       |       | Global Unique Identifier |
| [instanceId][2]  | int(10)      | unsigned   |     | NO   | 0       |       | Instance Identifier      |
| [team][3]        | smallint(5)  | unsigned   |     | NO   |         |       |                          |
| [joinX][4]       | float        | signed     |     | NO   | 0       |       |                          |
| [joinY][5]       | float        | signed     |     | NO   | 0       |       |                          |
| [joinZ][6]       | float        | signed     |     | NO   | 0       |       |                          |
| [joinO][7]       | float        | signed     |     | NO   | 0       |       |                          |
| [joinMapId][8]   | smallint(5)  | unsigned   |     | NO   | 0       |       | Map Identifier           |
| [taxiStart][9]   | int(10)      | unsigned   |     | NO   | 0       |       |                          |
| [taxiEnd][10]    | int(10)      | unsigned   |     | NO   | 0       |       |                          |
| [mountSpell][11] | mediumint(8) | unsigned   |     | NO   | 0       |       |                          |

[1]: #guid
[2]: #instanceid
[3]: #team
[4]: #joinx
[5]: #joiny
[6]: #joinz
[7]: #joino
[8]: #joinmapid
[9]: #taxistart
[10]: #taxiend
[11]: #mountspell

**Description of the fields**

### guid

The character guid. See [characters.guid](2129969.html#characters(table)-id).

### instanceId

This is the battleground instanceId. It's shared with [instance.id](instance_2130197.html#instance-id), but instead of putting data in that table, it's here.

### team

teamId:

| ID  | Description |
|-----|-------------|
| 0   | GM          |
| 67  | Horde       |
| 469 | Alliance    |

### joinX

Character's last X position before joining a battleground.

### joinY

Character's last Y position before joining a battleground.

### joinZ

Character's last Z position before joining a battleground.

### joinO

Character's last orientation bbefore joining a battleground.

### joinMapId

Character's last mapId before joining a battleground.

### taxiStart

Character's last taxi node before joining a battleground.

### taxiEnd

Character's heading taxi node before joining a battleground.

### mountSpell

The mount spell ID. See Spell.dbc column 1
