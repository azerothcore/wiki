# autobroadcast\_locale

[<-Back-to:Auth](database-auth)

**The \`autobroadcast\_locale\` table**

Holds translations of the messages in [autobroadcast](autobroadcast), one row per realm, message and client locale.

**Table: autobroadcast\_locale's Structure**

| Field               | Type       |     | Null | Key | Default | Extra | Comment |
| :------------------ | :--------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [realmid](#realmid) | INT        |     | NO   | PRI |         |       |         |
| [id](#id)           | INT        |     | NO   | PRI |         |       |         |
| [locale](#locale)   | VARCHAR(4) |     | NO   | PRI |         |       |         |
| [text](#text)       | LONGTEXT   |     | NO   |     |         |       |         |

**Description of the table's fields**

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
