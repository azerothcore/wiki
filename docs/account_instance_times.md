# account\_instance\_times

[<-Back-to:Characters](database-characters)

**The \`account\_instance\_times\` table**

This table controls how many instances the account's characters have been in last 1 hour. If there is 5 records per account, the player won't be able to enter another instance.

**Table Structure**

| Field            | Type   | Attributes | Key | Null | Default | Extra | Comment |
| ---------------- | ------ | ---------- | --- | ---- | ------- | ----- | ------- |
| [accountId][1]   | INT    | UNSIGNED   | PRI | NO   |         |       |         |
| [instanceId][2]  | INT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [releaseTime][3] | BIGINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #accountid
[2]: #instanceid
[3]: #releasetime

**Description of the fields**

### accountId

Account of the player. See [account.id](account#id).

### instanceId

This is the instance id which characters of this account has been past 5 hours.

### releaseTime

The time when the instances should be allowed again measured in Unix time.
