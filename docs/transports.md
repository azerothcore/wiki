# transports

[<-Back-to:World](database-world)

**The \`transports\` table**

This table contains all type 15 transports (Boats and Zeppelins). All other transport types have their frame time read from TransportAnimation.dbc.

**Table: transports's Structure**

| Field                     | Type     |          | Null | Key | Default | Extra          | Comment |
| :------------------------ | :------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [guid](#guid)             | INT      | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [entry](#entry)           | INT      | UNSIGNED | NO   | UNI | 0       |                |         |
| [name](#name)             | TEXT     |          | YES  |     | NULL    |                |         |
| [ScriptName](#scriptname) | CHAR(64) |          | NO   |     | ''      |                |         |

**Description of the table's fields**

### guid

Unique identifier for transport. Each time you add a new guid simply add one (1) from max guid.

### entry

[gameobject_template.entry](gameobject_template#entry) to be used for this transport. It must be a type 15 gameobject.

### name

This is an arbitrary to describe the transport entry.

### ScriptName

The script name for this transport. References a script in ScriptDev or SmartAI.

**Note:** Transports have their own map: https://wow.tools/dbc/?dbc=map&build=3.3.5.12340#page=1&colFilter[1]=Transport
