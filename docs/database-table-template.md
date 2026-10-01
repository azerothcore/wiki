# Database Table Template

Every database table page in the wiki follows the same layout. Use this page when you add a new table page or fill in an existing one.

## Required parts

A table page has these parts, in this order:

1. **Title**: the table name exactly as it is in the database, with underscores escaped (`# creature\_addon`).
2. **Back link**: a link to the database the table belongs to: [Auth](database-auth), [Characters](database-characters) or [World](database-world).
3. **Summary**: a short description of what the table is for and how the core uses it.
4. **Table Structure**: one row per column, with the column name linking to its description below. Copy the type, attributes, key, null and default values from the table's `CREATE TABLE` in the core, and keep the columns in the same order.
5. **Description of the fields**: one `###` heading per column, in the same order as the structure table.

## Describing the fields

- Every column gets a description. Do not leave a heading empty and do not write `TODO`.
- If the purpose of a column is not known, say so in one sentence, for example "Not used by the core."
- When a column takes a fixed set of values, list them in a table with the value and what it means.
- When a column is a flag field, list each flag with its value, and explain that flags are added together.
- When a column refers to another table, link to that table's field, for example [creature\_template.entry](creature_template#entry).
- Link anchors are the column name in lowercase with underscores removed, so the `path_id` column links to `#pathid`.

## Template

Copy this into the new page and replace the placeholders.

```markdown
# table\_name

[<-Back-to:World](database-world)

**The \`table\_name\` table**

What the table is for and how the core uses it.

**Table Structure**

| Field                  | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)              | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Name](#name)          | VARCHAR(50) |            |     | NO   |         |       |         |
| [some_flag](#someflag) | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |

**Description of the fields**

### ID

What the ID identifies.

### Name

What the name is used for.

### some\_flag

What the flag controls.

| Value | Name      | Description          |
| ----- | --------- | -------------------- |
| 0     | FLAG_NONE | No effect.           |
| 1     | FLAG_ONE  | What this flag does. |
| 2     | FLAG_TWO  | What this flag does. |
```

After adding the page, add the table to the list on [database-auth](database-auth), [database-characters](database-characters) or [database-world](database-world).
