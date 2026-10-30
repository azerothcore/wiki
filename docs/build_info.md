# build\_info

[<-Back-to:Auth](database-auth)

**The \`build\_info\` table**

Holds data about each client build. The core uses it to check whether a connecting client is supported.

**Table: build\_info's Structure**

| Field                               | Type        |     | Null | Key | Default | Extra | Comment    |
| :---------------------------------- | :---------- | :-- | :--: | :-: | :-----: | :---: | :--------- |
| [build](#build)                     | INT         |     | NO   | PRI |         |       | Identifier |
| [majorVersion](#majorversion)       | INT         |     | YES  |     | NULL    |       |            |
| [minorVersion](#minorversion)       | INT         |     | YES  |     | NULL    |       |            |
| [bugfixVersion](#bugfixversion)     | INT         |     | YES  |     | NULL    |       |            |
| [hotfixVersion](#hotfixversion)     | CHAR(3)     |     | YES  |     | NULL    |       |            |
| [winAuthSeed](#winauthseed)         | VARCHAR(32) |     | YES  |     | NULL    |       |            |
| [win64AuthSeed](#win64authseed)     | VARCHAR(32) |     | YES  |     | NULL    |       |            |
| [mac64AuthSeed](#mac64authseed)     | VARCHAR(32) |     | YES  |     | NULL    |       |            |
| [winChecksumSeed](#winchecksumseed) | VARCHAR(40) |     | YES  |     | NULL    |       |            |
| [macChecksumSeed](#macchecksumseed) | VARCHAR(40) |     | YES  |     | NULL    |       |            |

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
