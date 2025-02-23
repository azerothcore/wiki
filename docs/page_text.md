# page\_text

[<-Back-to:World](database-world)

**The \`page\_text\` table**

This table holds the text for letter items or any items that when moused-over turn the cursor into a magnifying glass and on right-click will open up a window where you can read the contents of the letter.

**Table Structure**

| Field              | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [ID][1]            | INT       | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Text][2]          | LONGTEXT  | SIGNED     |     | NO   |         |       |         |
| [NextPageID][3]    | INT       | UNSIGNED   |     | NO   | 0       |       |         |
| [VerifiedBuild][4] | INT       | SIGNED     |     | YES  | NULL    |       |         |

[1]: #id
[2]: #text
[3]: #nextpageid
[4]: #verifiedbuild

**Description of the fields**

### ID

Unique identifier

### Text

The actual text. The message in this field will be shown as the text on a page.

### NextPageID

The ID of the next page. [page_text.id](#id).

### VerifiedBuild
