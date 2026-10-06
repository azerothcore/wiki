# autobroadcast

[<-Back-to:Auth](database-auth)

**The \`autobroadcast\` table**

This table contains the autobroadcast entries for your realms. Values like it's activity, position and Timer (\*.On, \*.Center, \*.Timer) are defined within the [worldserver.conf](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/apps/worldserver/worldserver.conf.dist). They are chosen randomly, based on their weight.

**Table: autobroadcast's Structure**

| Field               | Type     |          | Null | Key | Default | Extra          | Comment |
| :------------------ | :------- | :------- | :--: | :-: | :-----: | :------------: | :------ |
| [realmid](#realmid) | INT      |          | NO   | PRI | -1      |                |         |
| [id](#id)           | TINYINT  | UNSIGNED | NO   | PRI |         | AUTO_INCREMENT |         |
| [weight](#weight)   | TINYINT  | UNSIGNED | YES  |     | 1       |                |         |
| [text](#text)       | LONGTEXT |          | NO   |     |         |                |         |

**Description of the table's fields**

### realmid

The [realmlist.id](realmlist#id). Defines which realm this entry belongs to. Use **-1** for all realms to load this entry.

### id

Unique identifier key per realm. Entries with same id will override each other without warnings - this can be used to replace -1 realmid entry on a specific realm.

### weight

A non-negative integer. Entries with higher weight have more chance to get picked.

### text

The text to broadcast. Color and item/spell/quest link formating codes can be used.
