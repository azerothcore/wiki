# character\_gifts

[<-Back-to:Characters](database-characters)

**The \`character\_gifts\` table**

This table holds data about wrapped/gift items.

**Table: character\_gifts's Structure**

| Field                  | Type |          | Null | Key | Default | Extra | Comment |
| :--------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)          | INT  | UNSIGNED | NO   | MUL | 0       |       |         |
| [item_guid](#itemguid) | INT  | UNSIGNED | NO   | PRI | 0       |       |         |
| [entry](#entry)        | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [flags](#flags)        | INT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### item\_guid

The GUID of the item. See [item\_instance.guid](item_instance#guid).

### entry

The entry of the item. See [item\_template.entry](item_template#entry).

### flags

The item proto flags of the gifted item at the time it was wrapped.

*Note for future research: max flags 13369920? FieldFlags of ProtoFlags?*
