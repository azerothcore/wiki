# areatrigger\_template

[<-Back-to:World](database-world.md)

**The \`areatrigger\_template\` table**

This table contains the description of areatrigger.

**Structure**

| Field               | Type       | Attributes | Key | Null | Default | Extra | Comment    |
|---------------------|------------|------------|-----|------|---------|-------|------------|
| [id][1]             | int(10)    | unsigned   | PRI | NO   |         |       | Identifier |
| [Type][2]           | tinyint(3) | unsigned   |     | NO   | 0       |       |            |
| [Flags][3]          | int(10)    | unsigned   |     | NO   | 0       |       |            |
| [Data0][4]          | float      | signed     |     | NO   | 0       |       |            |
| [Data1][5]          | float      | signed     |     | NO   | 0       |       |            |
| [Data2][6]          | float      | signed     |     | NO   | 0       |       |            |
| [Data3][7]          | float      | signed     |     | NO   | 0       |       |            |
| [Data4][8]          | float      | signed     |     | NO   | 0       |       |            |
| [Data5][9]          | float      | signed     |     | NO   | 0       |       |            |
| [ScriptName][10]    | char(64)   | signed     |     | NO   | ''      |       |            |
| [VerifiedBuild][11] | int(10)    | signed     |     | YES  | 0       |       |            |

[1]: #id
[2]: #type
[3]: #flags
[4]: #data0
[5]: #data1
[6]: #data2
[7]: #data3
[8]: #data4
[9]: #data5
[10]: #scriptname
[11]: #verifiedbuild

**Description of the fields**

### Id

### Type

### Flags

### Data0

### Data1

### Data2

### Data3

### Data4

### Data5

### ScriptName

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific [client build](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") and manually edited later for some special necessity.
