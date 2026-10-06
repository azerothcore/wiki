# pet\_name\_generation

[<-Back-to:World](database-world)

**The \`pet\_name\_generation\` table**

This table holds pieces of names (first and last half) that are use for pet name generation.

**Table: pet\_name\_generation's Structure**

| Field           | Type     |          | Null | Key | Default | Extra | Comment |
| :-------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [id](#id)       | INT      | UNSIGNED | NO   | PRI |         |       |         |
| [word](#word)   | TINYTEXT |          | NO   |     |         |       |         |
| [entry](#entry) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [half](#half)   | TINYINT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### id

The ID of the entry. This is an auto increment field and this is an arbitrary number. When adding entries it is best to just let the database pick the next available ID number.

### word

The name part for this entry.

### entry

The entry from creature\_template.entry for the creature that you want this part of the name to be generated for.

### half

This determines whether this is the first or last half of the name for this entry.

-   0 First half
-   1 Last half
