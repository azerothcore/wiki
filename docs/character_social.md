# character\_social

[<-Back-to:Characters](database-characters)

**The \`character\_social\` table**

Contains data about character's friends/ignored list.

**Table: character\_social's Structure**

| Field             | Type        |          | Null | Key | Default | Extra | Comment                            |
| :---------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :--------------------------------- |
| [guid](#guid)     | INT         | UNSIGNED | NO   | PRI | 0       |       | Character Global Unique Identifier |
| [friend](#friend) | INT         | UNSIGNED | NO   | PRI | 0       |       | Friend Global Unique Identifier    |
| [flags](#flags)   | TINYINT     | UNSIGNED | NO   | PRI | 0       |       | Friend Flags                       |
| [note](#note)     | VARCHAR(48) |          | NO   |     | ''      |       | Friend Note                        |

**Description of the table's fields**

### guid

The character guid. See [characters.guid](characters#guid).

### friend

The GUID of the friend/ignored. See [characters.guid](characters#guid).

### flags

| Value | Description                                                               |
|------ | ------------------------------------------------------------------------- |
| 0     | Unused entry - previously listed as friend or blocked (removed/unblocked) |
| 1     | Added as friend                                                           |
| 2     | Added as blocked user                                                     |
| 3     | Added as friend, and in ignorelist as well                                |

### note

Note about the friend (which appears beside the friend's name in friend list in Client).

Important note: There can be only 50 friend and 50 ignored characters. If you have problems with friends disappearing, try removing some of them first.
