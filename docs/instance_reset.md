# instance\_reset

[<-Back-to:Characters](database-characters)

**The \`instance\_reset\` table**

Date and time when heroic and raid instances will be reset (i.e. instances which have a fix reset interval, which is independent of the time, when some player(s) entered the instance). If Rate.InstanceResetTime is changed in the worldserver config, erase all data in this table and restart the server in order to repopulate it with the updated "resettime".

**Table: instance\_reset's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [mapid](#mapid)           | SMALLINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [difficulty](#difficulty) | TINYINT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [resettime](#resettime)   | INT      | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### mapid

The map ID the instance is in. See [Map.dbc](map).

### difficulty

Dungeon difficulty.

### resettime

The date/time when this instance (map) will be reset, in Unix time.
