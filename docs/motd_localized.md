# motd\_localized

[<-Back-to:Auth](database-auth)

**The \`motd\_localized\` table**

Holds translations of the message of the day in [motd](motd), per realm and client locale.

**Table: motd\_localized's Structure**

| Field               | Type       |     | Null | Key | Default | Extra | Comment |
| :------------------ | :--------- | :-- | :--: | :-: | :-----: | :---: | :------ |
| [realmid](#realmid) | INT        |     | NO   | PRI |         |       |         |
| [locale](#locale)   | VARCHAR(4) |     | NO   | PRI |         |       |         |
| [text](#text)       | LONGTEXT   |     | YES  |     | NULL    |       |         |

**Description of the table's fields**

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
