# pet\_name\_generation\_locale

[<-Back-to:World](database-world)

**The \`pet\_name\_generation\_locale\` table**

This table holds pieces of names (first and last half) that are use for pet name generation for locale.

**Table Structure**

| Field       | Type      | Attributes | Key | Null | Default | Extra          | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [ID][1]     | MEDIUMINT | UNSIGNED   | PRI | NO   | NULL    | Auto increment |         |
| [locale][2] | VARCHAR   |            |     | NO   |         |                |         |
| [word][3]   | tinytext  | SIGNED     |     | NO   | NULL    |                |         |
| [entry][4]  | MEDIUMINT | UNSIGNED   |     | NO   | 0       |                |         |
| [half][5]   | TINYINT   | SIGNED     |     | NO   | 0       |                |         |

[1]: #id
[2]: #locale
[3]: #word
[4]: #entry
[5]: #half

**Description of the fields**

### ID

The ID of the entry. This field must match [pet_name_generation.id](pet_name_generation#id)

### Locale

This is the language of the client.

| Language |
| -------- |
| koKR     |
| frFR     |
| deDE     |
| zhCN     |
| zhTW     |
| esES     |
| esMX     |
| ruRU     |

### word

The name part for this entry.

### entry

The entry from creature\_template.entry for the creature that you want this part of the name to be generated for.

### half

This determines whether this is the first or last half of the name for this entry.

-   0 First half
-   1 Last half
