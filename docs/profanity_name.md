# profanity\_name

[<-Back-to:Characters](database-characters)

**The \`profanity\_name\` table**

List of disallowed name fragments used by the profanity name filter to reject character, pet and similar names. See also [reserved_name](reserved_name) for fully reserved names.

**Table: profanity\_name's Structure**

| Field         | Type        |     | Null | Key | Default | Extra | Comment |
| :------------ | :---------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [name](#name) | VARCHAR(12) |     | NO   | PRI |         |       |         |

**Description of the table's fields**

### name

Disallowed name fragment (case-insensitive) that is blocked by the profanity filter.
