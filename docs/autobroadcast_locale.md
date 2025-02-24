# autobroadcast_locale

[<-Back-to:Auth](database-auth)

**The \`autobroadcast_locale\` table**

**Table Structure**

| Field        | Type        | Attributes | Key | Null | Default | Extra | Comment |
| ------------ | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [realmid][1] | INT         |            | PRI | NO   |         |       |         |
| [id][2]      | INT         |            | PRI | NO   |         |       |         |
| [locale][3]  | VARCHAR(4)  |            | PRI | NO   |         |       |         |
| [text][4]    | VARCHAR(45) |            |     | YES  |         |       |         |


[1]: #realmid
[2]: #id
[3]: #locale
[4]: #text

## Description of the fields

### realmid

RealmID for the autobroadcast to be sent

-1 for all realms

A specified realm is superior to -1 (All Realms)

### id

Autobroadcast ID

### locale

The locale for the autobroadcast. 
You can choose from the following:

| ID  | Language |
| --- | -------- |
| 1   | koKR     |
| 2   | frFR     |
| 3   | deDE     |
| 4   | zhCN     |
| 5   | zhTW     |
| 6   | esES     |
| 7   | esMX     |
| 8   | ruRU     |


### text

The text for the autobroadcast.
