# account\_instance\_times

[<-Back-to:Characters](database-characters)

**The \`account\_instance\_times\` table**

This table controls how many instances the account's characters have been in last 1 hour. If there is 5 records per account, the player won't be able to enter another instance.

**Table: account\_instance\_times's Structure**

| Field                       | Type   |          | Null | Key | Default | Extra | Comment |
| :-------------------------- | :----- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [accountId](#accountid)     | INT    | UNSIGNED | NO   | PRI |         |       |         |
| [instanceId](#instanceid)   | INT    | UNSIGNED | NO   | PRI | 0       |       |         |
| [releaseTime](#releasetime) | BIGINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### accountId

Account of the player. See [account.id](account#id).

### instanceId

This is the instance id which characters of this account has been past 5 hours.

### releaseTime

The time when the instances should be allowed again measured in Unix time.
