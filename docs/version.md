# version

[<-Back-to:World](database-world)

**The \`version\` table**

Includes information on current core and database version.

**Table Structure**

| Field               | Type         | Attributes | Key | Null | Default | Extra | Comment                         |
| ------------------- | ------------ | ---------- | --- | ---- | ------- | ----- | ------------------------------- |
| [core_version][1]   | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | Core revision dumped at startup |
| [core_revision][2]  | BIGINT       | UNSIGNED   |     | YES  | NULL    |       | Core revision hash              |
| [db_version][3]     | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | Version of world DB             |
| [script_version][4] | VARCHAR(120) | SIGNED     |     | YES  | NULL    |       | Version of scripts DB           |
| [cache_id][5]       | INT          | SIGNED     |     | YES  | 0       |       | Minor DB version                |

[1]: #core_version
[2]: #core_revision
[3]: #db_version
[4]: #script_version
[5]: #cache_id

**Description of the fields**

### core\_version

Full text description from the core  version your server is currently running on.
Example: TrinityCore rev. 8e48ef7863c5 2015-03-22 01:28:02 +0100 (6.x branch) (Win64, Release)

### core\_revision

Core Revision Hash your server is currently running on, i.e. **Unknown** or **8e48ef7863c5**

### db\_version

Database Version your server is currently running on. Example: **TDB .58**

### script\_version

`Version of scripts DB`

### cache\_id

`Minor DB version. Example: 58`
