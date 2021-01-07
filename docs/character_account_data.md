# character\_account\_data

[<-Back-to:Characters](database-characters.md)

**The \`character\_account\_data\` table**

Contains data about character settings.

**Structure**

| Field     | Type       | Attributes | Key | Null | Default | Extra | Comment |
|-----------|------------|------------|-----|------|---------|-------|---------|
| [guid][1] | int(10)    | unsigned   | PRI | NO   | 0       |       |         |
| [type][2] | int(3)     | unsigned   | PRI | NO   | 0       |       |         |
| [time][3] | bigint(10) | unsigned   |     | NO   | 0       |       |         |
| [data][4] | blob       | signed     |     | NO   |         |       |         |

[1]: #guid
[2]: #type
[3]: #time
[4]: #data

**Description of the fields**

### guid

The character global unique identifier. See [Characters.guid](2129969.html#characters(table)-guid)

### type

| Value | Description                  |
|-------|------------------------------|
| 1     | Config cache per character   |
| 3     | Bindings cache per character |
| 5     | Macros cache per character   |
| 6     | Layout cache per character   |
| 7     | Chat cache per character     |

### time

Time of last modification in Unixtime

### data

No description can be written. You just must understand it's data.
