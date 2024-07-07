# character\_gifts

[<-Back-to:Characters](database-characters)

**The \`character\_gifts\` table**

This table holds data about wrapped/gift items.

**Table Structure**

| Field          | Type | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ---- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [item_guid][2] | INT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [entry][3]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |
| [flags][4]     | INT  | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #item_guid
[3]: #entry
[4]: #flags

**Description of the fields**

### guid

The GUID of the character. See [characters.guid](characters#guid).

### item\_guid

The GUID of the item. See [item\_instance.guid](item_instance#guid).

### entry

The entry of the item. See [item\_template.entry](item_template#entry).

### flags

`field-no-description|4`

*Note for future research: max flags 13369920? FieldFlags of ProtoFlags?*
