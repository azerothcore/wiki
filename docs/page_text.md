# page\_text

[<-Back-to:World](database-world)

**The \`page\_text\` table**

This table holds the text for letter items or any items that when moused-over turn the cursor into a magnifying glass and on right-click will open up a window where you can read the contents of the letter.

**Table: page\_text's Structure**

| Field                           | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                       | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [Text](#text)                   | LONGTEXT |          | NO   |     |         |       |         |
| [NextPageID](#nextpageid)       | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [VerifiedBuild](#verifiedbuild) | INT      |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### ID

Unique identifier

### Text

The actual text. The message in this field will be shown as the text on a page.

### NextPageID

The ID of the next page. [page_text.id](#id).

### VerifiedBuild

This field is used to determine if this page originates from verified sniffs.

If value is 0 then it has not been parsed yet or it has been inherited from an older DB or another Core.

If value is above 0 then it has been parsed with sniffs from that specific client build.
