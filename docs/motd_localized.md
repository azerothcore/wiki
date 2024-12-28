# motd

[<-Back-to:Auth](database-auth)

**The \`motd_localized\` table**

**Table Structure**

| Field        | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT      | SIGNED     | PRI | NO   |         |       |         |
| [locale][2]  | VARCHAR(4) |          |     | NO   |         |       |         |
| [text][3]    | LONGTEXT |            |     | YES   | NULL |       |         |


[1]: #realmid
[2]: #locale
[3]: #text

## Description of the fields

### realmid

RealmID for the Motd to be sent

-1 for all realms

A specified realm is superior to -1 (All Realms)

### locale

The locale for the localized motd. 
You can choose from the following:

| ID | Language |
|----|----------|
| 1  | koKR     |
| 2  | frFR     |
| 3  | deDE     |
| 4  | zhCN     |
| 5  | zhTW     |
| 6  | esES     |
| 7  | esMX     |
| 8  | ruRU     |


### text

The text for the localized Motd
