# guild\_member\_withdraw

[<-Back-to:Characters](database-characters)

**The \`guild\_member\_withdraw\` table**

**Table: guild\_member\_withdraw's Structure**

| Field      | Type  | Attributes | Key | Null | Default | Extra  | Comment |
| ---------- | ----- | ---------- | --- | ---- | ------- | ------ | ------- |
| [guid][1]  | INT   | UNSIGNED   | PRI | NO   |         |        |         |
| [tab0][2]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab1][3]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab2][4]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab3][5]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab4][6]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [tab5][7]  | INT   | UNSIGNED   |     | NO   | 0       |        |         |
| [money][8] | INT   | UNSIGNED   |     | NO   | 0       |        |         |

[1]: #guid
[2]: #tab
[3]: #tab
[4]: #tab
[5]: #tab
[6]: #tab
[7]: #tab
[8]: #money

**Description of the table's fields**

### guid

GUID of the guild member. See [characters.guid](characters#guid).

### tab

`tab0` to `tab5`. Number of item stacks the member has taken out of each guild bank tab today. Reset every day.

### money

Money the member has taken out of the guild bank today, in copper. Reset every day.
