# item\_set\_names

[<-Back-to:World](database-world.md)

**The \`item\_set\_names\` table**

`table-no-description`

**Structure**

| Field              | Type         | Attributes | Key | Null | Default | Extra | Comment |
|--------------------|--------------|------------|-----|------|---------|-------|---------|
| [entry][1]         | mediumint(8) | unsigned   | PRI | NO   |         |       |         |
| [name][2]          | varchar(255) | signed     |     | NO   |         |       |         |
| [InventoryType][3] | tinyint(3)   | unsigned   |     | NO   | 0       |       |         |
| [WDBVerified][4]   | smallint(5)  | unsigned   |     | NO   | 1       |       |         |

[1]: #entry
[2]: #name
[3]: #inventorytype
[4]: #wdbverified

**Description of the fields**

### entry

Entry from item\_template

### name

Name of the item

### InventoryType

`field-no-description|3`

### WDBVerified

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
