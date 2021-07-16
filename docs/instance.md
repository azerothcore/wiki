# instance

[<-Back-to:Characters](database-characters.md)

**The \`instance\` table**

This table holds static information on all current instances that have not yet been reset.

**Structure**

| Field                    | Type     | Attributes | Key | Null | Default | Extra | Comment |
|------------------------- | -------- | ---------- | --- | ---- | ------- | ----- | --------|
| [id][1]                  | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [map][2]                 | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [resettime][3]           | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [difficulty][4]          | TINYINT  | UNSIGNED   |     | NO   | 0       |       |         |
| [completedEncounters][5] | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [data][6]                | TINYTEXT | SIGNED     |     | NO   |         |       |         |

[1]: #id
[2]: #map
[3]: #resettime
[4]: #difficulty
[5]: #completedencounters
[6]: #data

**Description of the fields**

### id

The instance ID. This number is unique to every instance.

### map

The map ID the instance is in. See [Map.dbc](map).

### resettime

The time when the instance will be reset, in Unix time. This field is zero for raid and heroic instances.
The resettime of raid and heroic instances for every specific group is stored in table [instance\_reset](instance_reset).

### difficulty

The difficulty of the current instance.

| Value | Description   |
| ----- | ------------- |
| 0     | 10-man Normal |
| 1     | 25-man Normal |
| 2     | 10-man Heroic |
| 3     | 25-man Heroic |

### completedEncounters

`field-no-description|5`

### data

Specific data belonging to the individual instance.