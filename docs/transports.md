# transports

[<-Back-to:World](database-world)

**The \`transports\` table**

This table contains all type 15 transports (Boats and Zeppelins). All other transport types have their frame time read from TransportAnimation.dbc.

**Table Structure**

| Field           | Type      | Attributes | Key    | Null | Default        | Extra | Comment |
| --------------- | --------- | ---------- | ------ | ---- | -------------- | ----- | ------- |
| [Guid][1]       | INT       | UNSIGNED   | PRI    | NO   | AUTO_INCREMENT |       |         |
| [Entry][2]      | MEDIUMINT | UNSIGNED   | UNIQUE | NO   | 0              |       |         |
| [Name][3]       | TEXT      |            |        | YES  | NULL           |       |         |
| [ScriptName][4] | CHAR(64)  |            |        | NO   | ' '            |       |         |

[1]: #guid
[2]: #entry
[3]: #name
[4]: #scriptname

**Description of the fields**

### guid

Unique identifier for transport. Each time you add a new guid simply add one (1) from max guid.

### entry

[gameobject_template.entry](gameobject_template#entry) to be used for this transport. It must be a type 15 gameobject.

### name

This is an arbitrary to describe the transport entry.

### ScriptName

`field-no-description|4`

**Note:** Transports have their own map: https://wow.tools/dbc/?dbc=map&build=3.3.5.12340#page=1&colFilter[1]=Transport
