# instance

[<-Back-to:Characters](database-characters)

**The \`instance\` table**

This table holds static information on all current instances that have not yet been reset.

**Table: instance's Structure**

| Field                                       | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)                                   | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [map](#map)                                 | SMALLINT | UNSIGNED | NO   | MUL | 0       |       |         |
| [resettime](#resettime)                     | INT      | UNSIGNED | NO   | MUL | 0       |       |         |
| [difficulty](#difficulty)                   | TINYINT  | UNSIGNED | NO   | MUL | 0       |       |         |
| [completedEncounters](#completedencounters) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [data](#data)                               | TINYTEXT |          | NO   |     |         |       |         |

**Description of the table's fields**

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

A bitmask of boss encounters that have been completed in this instance. Each bit corresponds to a boss encounter defined in the instance script.

### data

Specific data belonging to the individual instance.
