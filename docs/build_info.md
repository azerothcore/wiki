# build\_info

[<-Back-to:Auth](database-auth)

**The \`build\_info\` table**

Holds data about each client build. The core uses it to check whether a connecting client is supported.

**Table: build\_info's Structure**

| Field                 | Type        | Attributes | Key | Null | Default | Extra | Comment    |
| --------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ---------- |
| [build][1]            | INT         | SIGNED     | PRI | NO   |         |       | Identifier |
| [majorVersion][2]     | INT         | SIGNED     |     | YES  | NULL    |       |            |
| [minorVersion][3]     | INT         | SIGNED     |     | YES  | NULL    |       |            |
| [bugfixVersion][4]    | INT         | SIGNED     |     | YES  | NULL    |       |            |
| [hotfixVersion][5]    | CHAR(3)     |            |     | YES  | NULL    |       |            |
| [winAuthSeed][6]      | VARCHAR(32) |            |     | YES  | NULL    |       |            |
| [win64AuthSeed][7]    | VARCHAR(32) |            |     | YES  | NULL    |       |            |
| [mac64AuthSeed][8]    | VARCHAR(32) |            |     | YES  | NULL    |       |            |
| [winChecksumSeed][9]  | VARCHAR(40) |            |     | YES  | NULL    |       |            |
| [macChecksumSeed][10] | VARCHAR(40) |            |     | YES  | NULL    |       |            |

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

**Description of the table's fields**

### build

The client build.

### majorVersion

Major version of the client, for example 3 for 3.3.5a.

### minorVersion

Minor version of the client, for example 3 for 3.3.5a.

### bugfixVersion

Bugfix version of the client, for example 5 for 3.3.5a.

### hotfixVersion

Hotfix letter of the client, for example a for 3.3.5a.

### winAuthSeed

Not used by the core.

### win64AuthSeed

Not used by the core.

### mac64AuthSeed

Not used by the core.

### winChecksumSeed

Hash, as a hex string, used to check the Windows client executable when it logs in. If empty, the check is skipped.

### macChecksumSeed

Hash, as a hex string, used to check the Mac client executable when it logs in. If empty, the check is skipped.
