# guild\_member\_withdraw

[<-Back-to:Characters](database-characters)

**The \`guild\_member\_withdraw\` table**

Holds how much each guild member has withdrawn from the guild bank today, per tab and in money.

**Table: guild\_member\_withdraw's Structure**

| Field           | Type |          | Null | Key | Default | Extra | Comment |
| :-------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [guid](#guid)   | INT  | UNSIGNED | NO   | PRI |         |       |         |
| [tab0](#tab)    | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [tab1](#tab)    | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [tab2](#tab)    | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [tab3](#tab)    | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [tab4](#tab)    | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [tab5](#tab)    | INT  | UNSIGNED | NO   |     | 0       |       |         |
| [money](#money) | INT  | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### guid

GUID of the guild member. See [characters.guid](characters#guid).

### tab

`tab0` to `tab5`. Number of item stacks the member has taken out of each guild bank tab today. Reset every day.

### money

Money the member has taken out of the guild bank today, in copper. Reset every day.
