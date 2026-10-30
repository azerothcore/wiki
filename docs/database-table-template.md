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

The structure table always has these eight columns, in the order MySQL lists them: Field, Type, a second Type column with an empty header, Null, Key, Default, Extra and Comment. Copy the header and the alignment row from the example below: Null, Key, Default and Extra are centred, the rest is left-aligned.

- **Field**: the column name exactly as it is in the database, linking to its description. Write the link inline, `[name](#name)`, not as a numbered reference (`[name][1]`).
- **Type**: the type in uppercase, without the display width of integers: `INT`, not `int(10)`. Keep the length of text types: `VARCHAR(50)`.
- **Second Type column (empty header)**: `UNSIGNED` for unsigned number columns, empty for everything else. A signed column is not marked, as in MySQL. For an `ENUM`, list its values here.
- **Null**: `YES` or `NO`.
- **Key**: `PRI`, `UNI` or `MUL`, as MySQL shows it for the column, or empty.
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

## Column alignment

The second row of a table, the one made of dashes, sets how each column is aligned. Always write it with the colons, so the alignment does not depend on the theme:

| Dashes row | Alignment | Use it for |
| :--------- | :-------- | :--------- |
| `:---`     | left      | Names, types, text, comments and the decimal Value of a list. |
| `:--:`     | centre    | Short fixed values that are compared down the column: Null, Key, Default, Extra and Hex. |
| `---:`     | right     | Not used in table pages. |

The examples on this page already have the right dashes row, so copy it together with the header.

## Value lists

A field that takes one value out of a fixed list gets a table with these three columns:

| Value | Name           | Comment                 |
| :---- | :------------- | :---------------------- |
| 0     | EXAMPLE_NONE   | What the value means    |
| 1     | EXAMPLE_FIRST  |                         |
| 2     | EXAMPLE_SECOND |                         |

Use the name the value has in the core, or a short label when the core has no name for it.

## Bitmask tables

A field that holds flags gets a table with these four columns, in this order:

| Value | Hex    | Flag           | Comment                          |
| :---- | :----: | :------------- | :------------------------------- |
| 1     | `0x01` | EXAMPLE_FLAG_A | What the core does with the flag |
| 2     | `0x02` | EXAMPLE_FLAG_B |                                  |
| 4     | `0x04` | EXAMPLE_FLAG_C |                                  |

- **Value**: the decimal value, as it is stored in the database.
- **Hex**: the same value in hexadecimal, centred. Every row of a table has the same number of digits: enough for its biggest value, rounded up to 2, 4, 8 or 16 digits (`0x01`, `0x0001`, `0x00000001`).
- **Flag**: the name of the flag in the core, or a short label when the core has no name for it.
- **Comment**: what the flag does. Leave it empty when there is nothing to add. When the flag belongs to an ID, such as a class or a race, this column holds that ID and is named after it: `Class ID`, `Race ID`.

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

| Field                  | Type        |          | Null | Key | Default | Extra | Comment |
| :--------------------- | :---------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)              | INT         | UNSIGNED | NO   | PRI | 0       |       |         |
| [Name](#name)          | VARCHAR(50) |          | NO   |     |         |       |         |
| [some_flag](#someflag) | TINYINT     | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

What the ID identifies.

### Name

What the name is used for.

### some\_flag

What the flag controls.

| Value | Hex    | Flag      | Comment              |
| :---- | :----: | :-------- | :------------------- |
| 1     | `0x01` | FLAG_ONE  | What this flag does. |
| 2     | `0x02` | FLAG_TWO  | What this flag does. |
| 4     | `0x04` | FLAG_FOUR | What this flag does. |
```

## After adding the page

A new table page has to be linked from two lists. Both are in alphabetical order. The script `tools/update_table_lists.py` in the wiki repository adds the lines for you: run `python tools/update_table_lists.py`, or add `--check` to only see what is missing. By hand, the steps are:

1. **The page of its database**: [database-auth](database-auth), [database-characters](database-characters) or [database-world](database-world). Add `- [table_name](table_name)` under the heading of its first letter, and add that heading if the letter is new.
2. **The [Database Index](database-index)**: add the same line inside the folded list of that database.

The number of tables shown in the sidebar and on the Database Index is counted from the lists on the Database Index, so there is nothing else to update.
