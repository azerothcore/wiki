# instance\_reset

[<-Back-to:Characters](database-characters.md)

**The \`instance\_reset\` table**

Date and time when heroic and raid instances will be reset (i.e. instances which have a fix reset interval, which is independent of the time, when some player(s) entered the instance). If Rate.InstanceResetTime is changed in the worldserver config, erase all data in this table and restart the server in order to repopulate it with the updated "resettime".

**Structure**

| Field           | Type        | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|-------------|------------|-----|------|---------|-------|---------|
| [mapid][1]      | smallint(5) | unsigned   | PRI | NO   | 0       |       |         |
| [difficulty][2] | tinyint(3)  | unsigned   | PRI | NO   | 0       |       |         |
| [resettime][3]  | int(10)     | unsigned   |     | NO   | 0       |       |         |

[1]: #mapid
[2]: #difficulty
[3]: #resettime

**Description of the fields**

### mapid

The map ID the instance is in. See Map.dbc

### difficulty

Dungeon difficulty

### resettime

The date/time when this instance (map) will be reset, in Unix time.
