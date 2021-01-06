# areatrigger\_scripts

[<-Back-to:World](database-world.md)

**The \`areatrigger\_scripts\` table**

Allows for an area trigger to be scripted with Trinity Script.

**Structure**

| Field           | Type         | Attributes | Key | Null | Default | Extra | Comment |
|-----------------|--------------|------------|-----|------|---------|-------|---------|
| [entry][1]      | mediumint(8) | signed     | PRI | NO   | NULL    |       |         |
| [ScriptName][2] | char(64)     | signed     |     | NO   | NULL    |       |         |

[1]: #entry
[2]: #scriptname

**Description of the fields**

### entry

This is the trigger identifier from [AreaTrigger.dbc](DBC-AreaTrigger)

### ScriptName

The ScriptName for when scripting it in the core.
This might also be 'SmartTrigger'. It will than use [SmartAI](smart_scripts).

### Examples

| entry | ScriptName        |
|-------|-------------------|
| 302   | at_sentry_point   |
| 962   | SmartTrigger      |
| 1447  | SmartTrigger      |
| 1526  | at_ring_of_law    |
| 1726  | at_scent_larkorwi |
