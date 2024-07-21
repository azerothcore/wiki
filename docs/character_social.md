# character\_social

[<-Back-to:Characters](database-characters)

**The \`character\_social\` table**

Contains data about character's friends/ignored list.

**Table Structure**

| Field       | Type        | Attributes | Key | Null | Default | Extra | Comment                            |
| ----------- | ----------- | ---------- | --- | ---- | ------- | ----- | ---------------------------------- |
| [guid][1]   | INT         | UNSIGNED   | PRI | NO   | 0       |       | Character Global Unique Identifier |
| [friend][2] | INT         | UNSIGNED   | PRI | NO   | 0       |       | Friend Global Unique Identifier    |
| [flags][3]  | TINYINT     | UNSIGNED   | PRI | NO   | 0       |       | Friend Flags                       |
| [note][4]   | VARCHAR(48) | SIGNED     |     | NO   | ''      |       | Friend Note                        |

[1]: #guid
[2]: #friend
[3]: #flags
[4]: #note

**Description of the fields**

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
