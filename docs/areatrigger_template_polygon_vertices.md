# areatrigger\_template\_polygon\_vertices

[<-Back-to:World](database-world.md)

**The \`areatrigger\_template\_polygon\_vertices\` table**

This table contains the description of the shape of an areatrigger.

**Structure**

| Field               | Type    | Attributes | Key | Null | Default | Extra | Comment |
|---------------------|---------|------------|-----|------|---------|-------|---------|
| [AreaTriggerId][1]  | int(10) | unsigned   | PRI | NO   |         |       |         |
| [Idx][2]            | int(10) | unsigned   | PRI | NO   |         |       |         |
| [VerticeX][3]       | float   | signed     |     | NO   | 0       |       |         |
| [VerticeY][4]       | float   | signed     |     | NO   | 0       |       |         |
| [VerticeTargetX][5] | float   | signed     |     | YES  | NULL    |       |         |
| [VerticeTargetY][6] | float   | signed     |     | YES  | NULL    |       |         |
| [VerifiedBuild][7]  | int(10) | unsigned   |     | NO   | 0       |       |         |

[1]: #areatriggerid
[2]: #idx
[3]: #verticex
[4]: #verticey
[5]: #verticetargetx
[6]: #verticetargety
[7]: #verifiedbuild

**Description of the fields**

### AreaTriggerId

### Idx

### VerticeX

### VerticeY

### VerticeTargetX

### VerticeTargetY

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.
