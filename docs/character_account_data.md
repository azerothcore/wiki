# character\_account\_data

[<-Back-to:Characters](database-characters)

**The \`character\_account\_data\` table**

Contains data about character settings.

**Table: character\_account\_data's Structure**

| Field         | Type    |          | Null | Key | Default | Extra | Comment |
| :------------ | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid) | INT     | UNSIGNED | NO   | PRI | 0       |       |         |
| [type](#type) | TINYINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [time](#time) | INT     | UNSIGNED | NO   |     | 0       |       |         |
| [data](#data) | BLOB    |          | NO   |     |         |       |         |

**Description of the table's fields**

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

The data itself, as the client sent it. What it contains depends on [type](#type).
