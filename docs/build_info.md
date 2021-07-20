# build\_info

[<-Back-to:Auth](database-auth.md)

Read in: [English :gb:](build_info) [Spanish :es:](es/build_info)

**The \`build\_info\` table**

**Structure**

| Field                 | Type         | Attributes | Key | Null | Default | Extra | Comment    |
| --------------------- | ------------ | ---------- | --- | ---- | ------- | ----- |----------- |
| [build][1]            | INT          | SIGNED     | PRI | NO   |         |       | Identifier |
| [majorVersion][2]     | INT          | SIGNED     |     | YES  |         |       |            |
| [minorVersion][3]     | INT          | SIGNED     |     | YES  |         |       |            |
| [bugfixVersion][4]    | INT          | SIGNED     |     | YES  |         |       |            |
| [hotfixVersion][5]    | CHAR(3)      | SIGNED     |     | YES  |         |       |            |
| [winAuthSeed][6]      | VARCHAR(32)  | SIGNED     |     | YES  |         |       |            |
| [win64AuthSeed][7]    | VARCHAR(32)  | SIGNED     |     | YES  |         |       |            |
| [mac64AuthSeed][8]    | VARCHAR(32)  | SIGNED     |     | YES  |         |       |            |
| [winChecksumSeed][9]  | VARCHAR(40)  | SIGNED     |     | YES  |         |       |            |
| [macChecksumSeed][10] | VARCHAR(40)  | SIGNED     |     | YES  |         |       |            |

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

**Description of the fields**

### build

The client build.

### majorVersion

`field-no-description|2`

### minorVersion

`field-no-description|3`

### bugfixVersion

`field-no-description|4`

### hotfixVersion

`field-no-description|5`

### winAuthSeed

`field-no-description|6`

### win64AuthSeed

`field-no-description|7`

### mac64AuthSeed

`field-no-description|8`

### winChecksumSeed

`field-no-description|9`

### macChecksumSeed

`field-no-description|10`
