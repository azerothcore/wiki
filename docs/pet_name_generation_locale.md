# pet\_name\_generation\_locale

[<-Back-to:World](database-world)

**The \`pet\_name\_generation\_locale\` table**

This table holds pieces of names (first and last half) that are use for pet name generation for locale.

**Table: pet\_name\_generation\_locale's Structure**

| Field             | Type       |          | Null | Key | Default | Extra | Comment |
| :---------------- | :--------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)         | INT        | UNSIGNED | NO   | PRI |         |       |         |
| [Locale](#locale) | VARCHAR(4) |          | NO   | PRI |         |       |         |
| [Word](#word)     | TINYTEXT   |          | NO   |     |         |       |         |
| [Entry](#entry)   | INT        | UNSIGNED | NO   |     | 0       |       |         |
| [Half](#half)     | TINYINT    | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

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
