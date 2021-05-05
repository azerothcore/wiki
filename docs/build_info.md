# account

[<-Back-to:Auth](database-auth.md)

**The \`build_info\` table**

**Structure**

| Field                 | Type         | Attributes | Key | Null | Default           | Extra          | Comment    |
|-----------------------|--------------|------------|-----|------|-------------------|----------------|------------|
| [build][1]            | INT          |            | PRI | NO   |                   |                | Identifier |
| [majorVersion][2]     | INT          |            |     | YES  |                   |                |            |
| [minorVersion][3]     | INT          |            |     | YES  |                   |                |            |
| [bugfixVersion][4]    | INT          |            |     | YES  |                   |                |            |
| [hotfixVersion][5]    | CHAR(3)      |            |     | YES  |                   |                |            |
| [winAuthSeed][6]      | VARCHAR(32)  |            |     | YES  |                   |                |            |
| [win64AuthSeed][7]    | VARCHAR(32)  |            |     | YES  |                   |                |            |
| [mac64AuthSeed][8]    | VARCHAR(32)  |            |     | YES  |                   |                |            |
| [winChecksumSeed][9]  | VARCHAR(40)  |            |     | YES  |                   |                |            |
| [macChecksumSeed][10] | VARCHAR(40)  |            |     | YES  |                   |                |            |

[1]: #build
[2]: #majorversion
[3]: #minorversion
[4]: #bugfixversion
[5]: #hotfixversion
[6]: #winauthseed
[7]: #win64authseed
[8]: #mac64authseed
[9]: #winchecksumseed
[10]: #macchecksumseed

## Description of the fields

### build

The client build.

### majorVersion

### minorVersion

### bugfixVersion

### hotfixVersion

### winAuthSeed

### win64AuthSeed

### mac64AuthSeed

### winChecksumSeed

### macChecksumSeed
