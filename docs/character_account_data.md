# character\_account\_data

[<-Back-to:Characters](database-characters)

**The \`character\_account\_data\` table**

Contains data about character settings.

**Table Structure**

| Field     | Type    | Attributes | Key | Null | Default | Extra | Comment |
| --------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [type][2] | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [time][3] | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [data][4] | BLOB    | SIGNED     |     | NO   |         |       |         |

[1]: #guid
[2]: #type
[3]: #time
[4]: #data

**Description of the fields**

### guid

The character global unique identifier. See [characters.guid](characters#guid).

### type

| Value | Description                  |
|------ | ---------------------------- |
| 1     | Config cache per character   |
| 3     | Bindings cache per character |
| 5     | Macros cache per character   |
| 6     | Layout cache per character   |
| 7     | Chat cache per character     |

### time

Time of last modification in Unixtime.

### data

No description can be written. You just must understand it's data.
