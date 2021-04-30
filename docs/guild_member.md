# guild\_member

[<-Back-to:Characters](database-characters.md)

**The \`guild\_member\` table**

This table holds information on the members of all guilds, their ranks in the guild, and any notes made by them or by guild officers.

**Structure**

| Field                   | Type        | Attributes | Key    | Null | Default | Extra | Comment             |
|-------------------------|-------------|------------|--------|------|---------|-------|---------------------|
| [guildid][1]            | INT     | UNSIGNED   |        | NO   |         |       | Guild Identificator |
| [guid][2]               | INT     | UNSIGNED   | Unique | NO   |         |       |                     |
| [rank][3]               | TINYINT  | UNSIGNED   |        | NO   |         |       |                     |
| [pnote][4]              | VARCHAR(31) |            |        | NO   |         |       |                     |
| [offnote][5]            | VARCHAR(31) |            |        | NO   |         |       |                     |
| [BankResetTimeMoney][6] | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemMoney][7]       | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankResetTimeTab0][8]  | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemSlotsTab0][9]   | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankResetTimeTab1][10] | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemSlotsTab1][11]  | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankResetTimeTab2][12] | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemSlotsTab2][13]  | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankResetTimeTab3][14] | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemSlotsTab3][15]  | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankResetTimeTab4][16] | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemSlotsTab4][17]  | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankResetTimeTab5][18] | INT     | UNSIGNED   |        | NO   |         |       |                     |
| [BankRemSlotsTab5][19]  | INT     | UNSIGNED   |        | NO   |         |       |                     |

[1]: #guildid
[2]: #guid
[3]: #rank
[4]: #pnote
[5]: #offnote
[6]: #bankresettimemoney
[7]: #bankremmoney
[8]: #bankresettimetab0
[9]: #bankremslotstab0
[10]: #bankresettimetab1
[11]: #bankremslotstab1
[12]: #bankresettimetab2
[13]: #bankremslotstab2
[14]: #bankresettimetab3
[15]: #bankremslotstab3
[16]: #bankresettimetab4
[17]: #bankremslotstab4
[18]: #bankresettimetab5
[19]: #bankremslotstab5

**Description of the fields**

### guildid

The ID of the guild that the member is a part of. See guild.guildid

### guid

The GUID of the player. See characters.guid

### rank

The rank that the player has in the guild. See guild\_rank.rid

### pnote

The note set by the player that can be read by everyone.

### offnote

The note set by officers in the guild that can only be read by other officers of the guild.

### BankResetTimeMoney

`field-no-description|6`

### BankRemMoney

`field-no-description|7`

### BankResetTimeTab0-5

`field-no-description|8`

### BankRemSlotsTab0-5

`field-no-description|9`
