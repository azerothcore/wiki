# chat\_filter

[<-Back-to:Characters](database-characters)

**The \`chat\_filter\` table**

This table stores reserved words used by the core chat filter. When a matching entry is found, the message is blocked using case-insensitive substring matching.

The filter is controlled by the `ChatFilter.Whisper`, `ChatFilter.Say`, `ChatFilter.Yell`, and `ChatFilter.Emote` settings in `worldserver.conf`. Manage entries in-game with `.chatfilter list`, `.chatfilter add`, `.chatfilter remove`, and `.reload chat_filter`.

**Table: chat\_filter's Structure**

| Field         | Type         |          | Null | Key | Default | Extra          | Comment |
| :------------ | :----------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [ID](#id)     | INT          | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [Word](#word) | VARCHAR(255) |          | NO   |     |         |                |         |

**Description of the table's fields**

### ID

Unique row identifier.

### Word

Reserved word or phrase checked by the chat filter.
