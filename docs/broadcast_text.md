# broadcast\_text

**The \`broadcast\_text\` table**

 

This table (ref <https://github.com/TrinityCore/TrinityCore/commit/60e87db>) will have **everything** you need for your scripts' texts, such as: [gossips](gossip_menu_option), [creature texts](creature_text) and [npc\_text](npc_text)s.

Its purpose is (will be) used as a globalized table containing the texts as mentionned above, and things like their sounds, their emotes and the languages in which the texts should be said.

All the values are from sniffs (ADBVerified) so, don't add things in it - Kinzcool.

 **Values from this table come from sniffs (retail data) and should not be changed unless you are absolutelly sure they have been wrongly changed before.**
 
 **Most of the time, the values here are correct and your script needs to be fixed. Please ensure your script works correctly before suggesting changes to this table.**

**Structure**

| Field                                    | Type        | Attributes | Key | Null | Default | Extra | Comment |
|------------------------------------------|-------------|------------|-----|------|---------|-------|---------|
| [ID](#broadcast_text-ID)                 | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [Language](#broadcast_text-Language)     | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| [MaleText](#broadcast_text-MaleText)     | text        | SIGNED     |     | YES  | NULL    |       |         |
| [FemaleText](#broadcast_text-FemaleText) | text        | SIGNED     |     | YES  | NULL    |       |         |
| EmoteID1                                 | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteID2                                 | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteID3                                 | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay1                              | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay2                              | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| EmoteDelay3                              | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| SoundId                                  | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| UnkEmoteID                               | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| Type                                     | INT     | UNSIGNED   |     | NO   | 0       |       |         |
| WDBVerified                              | SMALLINT | SIGNED     |     | NO   | 0       |       |         |

### Description of the fields

 

### ID

The unique ID value for the text.

### Language

The language in what the text will be broadcasted.

IDs from Languages.dbc

### MaleText

The text that the male creature will broadcast, or male characters can read from gossip menu.

### FemaleText

The text that the female creature will broadcast, or female characters can read from gossip menu.

### EmoteID\[1-3\]

The emotes played when the texts are broadcast.

IDs from Emotes.dbc

### EmoteDelay\[1-3\]

The delays of the broadcast emotes.

### SoundId

The sounds played when the texts are broadcast.

IDs from SoundEntries.dbc

### UnkEmoteID

An emote.

### Type

 

#### WDBVerified

This field was used to determine whether a template has been verified from WDB files (ADB files for this one).

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific [client build](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") and manually edited later for some special necessity.

 
