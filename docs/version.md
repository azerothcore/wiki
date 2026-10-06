# version

[<-Back-to:World](database-world)

**The \`version\` table**

Includes information on current core and database version.

**Table: version's Structure**

| Field                          | Type         |     | Null | Key | Default | Extra | Comment                          |
| :----------------------------- | :----------- | :-- | :--: | :-: | :-----: | :---: | :------------------------------- |
| [core_version](#coreversion)   | VARCHAR(255) |     | NO   | PRI | ''      |       | Core revision dumped at startup. |
| [core_revision](#corerevision) | VARCHAR(120) |     | YES  |     | NULL    |       | Core revision hash               |
| [db_version](#dbversion)       | VARCHAR(120) |     | YES  |     | NULL    |       | Version of world DB.             |
| [cache_id](#cacheid)           | INT          |     | YES  |     | 0       |       | Minor DB version                 |

**Description of the table's fields**

### core\_version

Full text description from the core  version your server is currently running on.
Example: TrinityCore rev. 8e48ef7863c5 2015-03-22 01:28:02 +0100 (6.x branch) (Win64, Release)

### core\_revision

Core Revision Hash your server is currently running on, i.e. **Unknown** or **8e48ef7863c5**

### db\_version

Database Version your server is currently running on. Example: **TDB .58**

### cache\_id

`Minor DB version. Example: 58`
