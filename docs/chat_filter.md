# chat\_filter

[<-Back-to:Characters](database-characters)

**The `chat_filter` table**

This table stores reserved words used by the core chat filter. When a matching entry is found, the message is blocked using case-insensitive substring matching.

The filter is controlled by the `ChatFilter.Whisper`, `ChatFilter.Say`, `ChatFilter.Yell`, and `ChatFilter.Emote` settings in `worldserver.conf`. Manage entries in-game with `.chatfilter list`, `.chatfilter add`, `.chatfilter remove`, and `.reload chat_filter`.

**Table Structure**

| Field     | Type         | Attributes | Key | Null | Default | Extra          | Comment |
| --------- | ------------ | ---------- | --- | ---- | ------- | -------------- | ------- |
| [ID](#id) | INT          | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [Word](#word) | VARCHAR(255) | SIGNED     |     | NO   |         |                |         |

**Description of the fields**

### ID

Unique row identifier.

### Word

Reserved word or phrase checked by the chat filter.
