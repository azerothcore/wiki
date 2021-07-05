# autobroadcast

[<-Back-to:Auth](database-auth.md)

**The \`autobroadcast\` table**

This table contains the autobroadcast entries for your realms. Values like it's activity, position and Timer (\*.On, \*.Center, \*.Timer) are defined within the [worldserver.conf](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/worldserver/worldserver.conf.dist). They are chosen randomly, based on their weight.

**Structure**

| Field        | Type     | Attributes | Key | Null | Default | Extra          | Comment |
| ------------ | -------- | ---------- | --- | ---- | ------- | -------------- | ------- |
| [realmid][1] | INT      | SIGNED     | PRI | NO   | -1      |                |         |
| [id][2]      | TINYINT  | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |         |
| [weight][3]  | TINYINT  | UNSIGNED   |     | YES  | 1       |                |         |
| [text][4]    | LONGTEXT |            |     | NO   |         |                |         |

[1]: #realmid
[2]: #id
[3]: #weight
[4]: #text

**Description of the fields**

### realmid

The [realmlist.id](realmlist). Defines which realm this entry belongs to. Use **-1** for all realms to load this entry.

### id

Unique identifier key per realm. Entries with same id will override each other without warnings - this can be used to replace -1 realmid entry on a specific realm.

### weight

A non-negative integer. Entries with higher weight have more chance to get picked.

### text

The text to broadcast. Color and item/spell/quest link formating codes can be used.
