# Database Table Template

Every database table page in the wiki follows the same layout. Use this page when you add a new table page or fill in an existing one.

## Required parts

A table page has these parts, in this order:

1. **Title**: the table name exactly as it is in the database, with underscores escaped (`# creature\_addon`).
2. **Back link**: a link to the database the table belongs to: [Auth](database-auth), [Characters](database-characters) or [World](database-world).
3. **Summary**: a short description of what the table is for and how the core uses it.
4. **Table: table\_name's Structure**: one row per column, with the column name linking to its description below. Copy the type, attributes, key, null and default values from the table's `CREATE TABLE` in the core, and keep the columns in the same order.
5. **Description of the table's fields**: one `###` heading per column, in the same order as the structure table. Columns that repeat, such as `tut0` to `tut7` or the locale columns of a DBC table, may share one heading, as long as every one of them links to it from the structure table.

## Filling in the structure table

The structure table always has these eight columns: Field, Type, Attributes, Key, Null, Default, Extra and Comment.

- **Field**: the column name exactly as it is in the database, linking to its description.
- **Type**: the type in uppercase, without the display width of integers: `INT`, not `int(10)`. Keep the length of text types: `VARCHAR(50)`.
- **Attributes**: `UNSIGNED` or `SIGNED` for number columns, empty for text columns. For an `ENUM`, list its values here.
- **Key**: `PRI`, `UNI` or `MUL`, as MySQL shows it for the column, or empty.
- **Null**: `YES` or `NO`.
- **Default**: the default value, `NULL` when the default is null, `''` for an empty string, or empty when the column has no default.
- **Extra**: `AUTO_INCREMENT` and similar, or empty.
- **Comment**: the column comment from the database, if it has one.

## Describing the fields

- Describe what the AzerothCore core does with the column. The wikis of other projects can be a hint, but only write what matches the AzerothCore source.
- Every column gets a description. Do not leave a heading empty and do not write `TODO`.
- If the purpose of a column is not known, say so in one sentence, for example "Not used by the core."
- When a column takes a fixed set of values, list them in a table with the value and what it means.
- When a column is a flag field, list each flag with its value, and explain that flags are added together.
- When a column refers to another table, link to that table's field, for example [creature\_template.entry](creature_template#entry).
- Link anchors are the column name in lowercase with underscores removed, so the `path_id` column links to `#pathid`.

## DBC tables

Tables whose name ends in `_dbc` hold rows that replace or add to the data the core loads from a client `.dbc` file. Their pages follow the same layout, with these additions:

- The summary names the `.dbc` file the table belongs to.
- Each description says whether the core reads the column. The format string of the file in [`DBCfmt.h`](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/shared/DataStores/DBCfmt.h) shows this.
- The 16 text columns of a localized field are read by position, not by name, and only the nine locales in the core's `LocaleConstant` list are supported in 3.3.5a. Say this in the description, because the column names suggest otherwise.

## Template

Copy this into the new page and replace the placeholders.

```markdown
# table\_name

[<-Back-to:World](database-world)

**The \`table\_name\` table**

What the table is for and how the core uses it.

**Table: table\_name's Structure**

| Field                  | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID](#id)              | INT         | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Name](#name)          | VARCHAR(50) |            |     | NO   |         |       |         |
| [some_flag](#someflag) | TINYINT     | UNSIGNED   |     | NO   | 0       |       |         |

**Description of the table's fields**

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

After adding the page, add the table to the list on [database-auth](database-auth), [database-characters](database-characters) or [database-world](database-world), and to the same database on the [Database Index](database-index).
