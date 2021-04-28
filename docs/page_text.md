# page\_text

[<-Back-to:World](database-world.md)

**The \`page\_text\` table**

This table holds the text for letter items or any items that when moused-over turn the cursor into a magnifying glass and on right-click will open up a window where you can read the contents of the letter.

**Structure**

| Field            | Type         | Attributes | Key | Null | Default | Extra | Comment |
|------------------|--------------|------------|-----|------|---------|-------|---------|
| [entry][1]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [text][2]        | longtext     | SIGNED     |     | NO   | NULL    |       |         |
| [next_page][3]   | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [WDBVerified][4] | SMALLINT  | SIGNED     |     | YES  | 1       |       |         |

[1]: #entry
[2]: #text
[3]: #next_page
[4]: #wdbverified

**Description of the fields**

### entry

The ID of the text in the page. This number is unique to every text entry.

### text

The actual text. The message in this field will be shown as the text on a page.

### next\_page

The ID of the next page's text [entry](#page_text-entry).

### WDBVerified
