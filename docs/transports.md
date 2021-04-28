[Database Structure](Database-Structure) > [World-Database](World-Database) > [transports](transports)

Column | Type | Description
--- | --- | ---
Guid | INT(10) unsigned | 
Entry | MEDIUMINT(8) unsigned | 
Name | text | 
ScriptName | char(64) | 

[1]: #guid
[2]: #entry
[3]: #name
[4]: #scriptname

**Description of the fields**

### Guid

Unique identifier for this transport. Each time a new one is added, it has to add +1 value of the previous number.

### Entry

[GameObject](gameobject_template) Entry to be used for this transport. It must be a GameObject whose Type is 15.

### Name

Name or comment used to detail the Transport entry.

##### Example:
Undercity, Tirisfal Glades and Grom'gol Base Camp, Stranglethorn Vale ("The Purple Princess")

### ScriptName

Undefined.
