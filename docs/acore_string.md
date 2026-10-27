# acore_string

[<-Back-to:World](database-world)

**The \`acore_string\` table**

This table holds all of the strings used internally by the server. It is provided for the main purpose of translation.

The translations in other languages are in [acore\_string\_locale](acore_string_locale).

**Table Structure**

| Field                | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]           | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [content_default][2] | text |            |     | NO   |         |       |         |

[1]: #entry
[2]: #contentdefault

**Description of the fields**

### entry

The ID that the core uses to identify a string. These IDs are contained and used internally and must correspond to what the core expects. The core will not operate if all IDs aren't in this table.

### content\_default

The English translation (locale ID 0).
