# quest\_request\_items

[<-Back-to:World](database-world)

**The \`quest\_request\_items\` table**

This table basically handles 3 quest details:

1.  NPC Emote when quest is completed
2.  NPC Emote when quest is incomplete
3.  Completion text for quests requiring quest items

**Table Structure**

| Field                                   | Type      | Attributes | Key | NULL | Default | Comment |
| --------------------------------------- | --------- | ---------- | --- | ---- | ------- | ------- |
| [ID](#id)                               | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |         |
| [EmoteOnComplete](#emoteoncomplete)     | SMALLINT  | UNSIGNED   |     | NO   | 0       |         |
| [EmoteOnIncomplete](#emoteonincomplete) | SMALLINT  | UNSIGNED   |     | NO   | 0       |         |
| [CompletionText](#completiontext)       | text      |            |     | YES  | NULL    |         |
| [VerifiedBuild](#verifiedbuild)         | SMALLINT  |            |     | NO   | 0       |         |

**Description of the fields**

### ID

Quest ID for quests showing a completion text upon turning in an item delivery quest.
Primary Key for this table. Each quest ID must be unique.

### EmoteOnComplete

Emote (from [Emotes.dbc](Emotes) played by the quest ender NPC when all quest objectives are completed.

### EmoteOnIncomplete

Emote (from [Emotes.dbc](https://trinitycore.atlassian.net/wiki/display/tc/Emotes)) played by the quest ender NPC if any of the quest objectives are incomplete.

### CompletionText

Quest gossip text shown in the final gossip dialogue window when turning in an item delivery quest.
The quest item(s) involved in the quest can either be provided by the quest giver or collected by the player.

### VerifiedBuild

This field is used by the TrinityCore DB Team to determine whether a template has been verified from WDB files.

-   If value is 0, it has not been parsed yet.
-   If value is &gt; 0, it has been parsed with WDB files from that specific [Client Build](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild).
-   If value is -1, it is just a place holder until proper data are found on WDBs.
-   If value is -[Client Build](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild), it was parsed with WDB files from that specific [client build](https://trinitycore.atlassian.net/wiki/display/tc/realmlist#realmlist-gamebuild) and manually edited later for some specific necessity.

 
