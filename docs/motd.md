# motd

[<-Back-to:Auth](database-auth)

**The \`motd\` table**

Holds the message of the day for each realm. A realm id of -1 applies to all realms.

**Table: motd's Structure**

| Field        | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT      | SIGNED     | PRI | NO   |         |       |         |
| [text][2]    | LONGTEXT |            |     | YES  | NULL    |       |         |


[1]: #realmid
[2]: #text

**Description of the table's fields**

### realmid

RealmID for the Motd to be sent

-1 for all realms

A specified realm is superior to -1 (All Realms)

### text

The text for Motd
