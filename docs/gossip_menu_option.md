# gossip\_menu\_option

[<-Back-to:World](database-world)

**Table: gossip\_menu\_option**

This table holds information about menu options a gossip NPC can have. Examples of options: "Train me!", "I want to unlearn my talents"

**Table: gossip\_menu\_option's Structure**

| Field                                           | Type     |          | Null | Key | Default | Extra | Comment |
| :---------------------------------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [MenuID](#menuid)                               | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [OptionID](#optionid)                           | SMALLINT | UNSIGNED | NO   | PRI | 0       |       |         |
| [OptionIcon](#optionicon)                       | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [OptionText](#optiontext)                       | TEXT     |          | YES  |     | NULL    |       |         |
| [OptionBroadcastTextID](#optionbroadcasttextid) | INT      |          | NO   |     | 0       |       |         |
| [OptionType](#optiontype)                       | TINYINT  | UNSIGNED | NO   |     | 0       |       |         |
| [OptionNpcFlag](#optionnpcflag)                 | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [ActionMenuID](#actionmenuid)                   | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [ActionPoiID](#actionpoiid)                     | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [BoxCoded](#boxcoded)                           | TINYINT  | UNSIGNED | NO   |     | 0       |       |         |
| [BoxMoney](#boxmoney)                           | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [BoxText](#boxtext)                             | TEXT     |          | YES  |     | NULL    |       |         |
| [BoxBroadcastTextID](#boxbroadcasttextid)       | INT      |          | NO   |     | 0       |       |         |
| [VerifiedBuild](#verifiedbuild)                 | INT      |          | YES  |     | NULL    |       |         |

**Description of the table's fields**

### MenuID

Gossip entry from Gossip\_menu.entry this option is associated with.
If this is the default gossip option for the selected NPC, verify that the NPC has this value in it's [creature\_template.gossip\_menu\_id](creature_template#gossipmenuid) .

### OptionID

The id associated with this gossip\_menu\_option. Must be unique for a given menu\_id starting from 0 (zero).
Value increments by 1 if there are multiple options in the same gossip\_menu.

### OptionIcon

| Name                      | ID  | Description                                 |
| ------------------------- | --- | ------------------------------------------- |
| GOSSIP\_ICON\_CHAT        | 0   | White chat bubble                           |
| GOSSIP\_ICON\_VENDOR      | 1   | Brown bag                                   |
| GOSSIP\_ICON\_TAXI        | 2   | Flight                                      |
| GOSSIP\_ICON\_TRAINER     | 3   | Book                                        |
| GOSSIP\_ICON\_INTERACT\_1 | 4   | Interaction wheel                           |
| GOSSIP\_ICON\_INTERACT\_2 | 5   | Interaction wheel                           |
| GOSSIP\_ICON\_MONEY\_BAG  | 6   | Brown bag with yellow dot (gold)            |
| GOSSIP\_ICON\_TALK        | 7   | White chat bubble with black dots (**...**) |
| GOSSIP\_ICON\_TABARD      | 8   | Tabard                                      |
| GOSSIP\_ICON\_BATTLE      | 9   | Two swords                                  |
| GOSSIP\_ICON\_DOT         | 10  | Yellow dot                                  |

### OptionText

This is the text that you want to be displayed in the player selectable option. Examples would be: "Please train me.", "I would like to browse your goods.", "Learn Dual Spec".
If OptionBroadcastTextID contains a valid broadcast\_text.ID, it links to broadcast\_text so the content from broadcast\_text is displayed directly instead of the option\_text field content.

### OptionBroadcastTextID

The ID of the same text in broadcast\_text.ID.

### OptionType

| option_id Name                  | Value | npcflag Name (& comment)                                                    | npcflag value |
| ------------------------------- | ----- | --------------------------------------------------------------------------- | ------------- |
| GOSSIP_OPTION_NONE              | 0     | UNIT_NPC_FLAG_NONE                                                          | 0             |
| GOSSIP_OPTION_GOSSIP            | 1     | UNIT_NPC_FLAG_GOSSIP                                                        | 1             |
| GOSSIP_OPTION_QUESTGIVER        | 2     | UNIT_NPC_FLAG_QUESTGIVER                                                    | 2             |
| GOSSIP_OPTION_VENDOR            | 3     | UNIT_NPC_FLAG_VENDOR (Make sure there is npc_vendor data for this creature) | 128           |
| GOSSIP_OPTION_TAXIVENDOR        | 4     | UNIT_NPC_FLAG_TAXIVENDOR                                                    | 8192          |
| GOSSIP_OPTION_TRAINER           | 5     | UNIT_NPC_FLAG_TRAINER (Remember to set a (TrainerId, CreatureId) in creature_default_trainer)  | 16            |
| GOSSIP_OPTION_SPIRITHEALER      | 6     | UNIT_NPC_FLAG_SPIRITHEALER                                                  | 16384         |
| GOSSIP_OPTION_SPIRITGUIDE       | 7     | UNIT_NPC_FLAG_SPIRITGUIDE                                                   | 32768         |
| GOSSIP_OPTION_INNKEEPER         | 8     | UNIT_NPC_FLAG_INNKEEPER                                                     | 65536         |
| GOSSIP_OPTION_BANKER            | 9     | UNIT_NPC_FLAG_BANKER                                                        | 131072        |
| GOSSIP_OPTION_PETITIONER        | 10    | UNIT_NPC_FLAG_PETITIONER                                                    | 262144        |
| GOSSIP_OPTION_TABARDDESIGNER    | 11    | UNIT_NPC_FLAG_TABARDDESIGNER                                                | 524288        |
| GOSSIP_OPTION_BATTLEFIELD       | 12    | UNIT_NPC_FLAG_BATTLEFIELDPERSON                                             | 1048576       |
| GOSSIP_OPTION_AUCTIONEER        | 13    | UNIT_NPC_FLAG_AUCTIONEER                                                    | 2097152       |
| GOSSIP_OPTION_STABLEPET         | 14    | UNIT_NPC_FLAG_STABLE                                                        | 4194304       |
| GOSSIP_OPTION_ARMORER           | 15    | UNIT_NPC_FLAG_ARMORER (not used)                                            | 4096          |
| GOSSIP_OPTION_UNLEARNTALENTS    | 16    | UNIT_NPC_FLAG_TRAINER (bonus option for GOSSIP_OPTION_TRAINER)              | 16            |
| GOSSIP_OPTION_UNLEARNPETTALENTS | 17    | UNIT_NPC_FLAG_TRAINER (bonus option for GOSSIP_OPTION_TRAINER)              | 16            |
| GOSSIP_OPTION_LEARNDUALSPEC     | 18    | UNIT_NPC_FLAG_TRAINER (bonus option for GOSSIP_OPTION_TRAINER)              | 16            |
| GOSSIP_OPTION_OUTDOORPVP        | 19    | Added by code (option for outdoor PvP creatures)                            |               |
| GOSSIP_OPTION_MAX               |       |                                                                             |               |

### OptionNpcFlag

This is the npcflag ([Creature\_template.npcflag](creature_template#npcflag) that the NPC must have to have this option display. See comments (after //) in previous table)

### ActionMenuID

If you want to create a sub-menu, this is the ID ([gossip\_menu.MenuID](gossip_menu#menuid) / [gossip\_menu\_option.MenuID](gossip_menu_option#menuid)) to link to to create that sub-menu.

### ActionPoiID

If you want a POI (point of interest) to display on the minimap (like how a city guard places a marker when you ask directions), this is the \`entry\` from [Points\_of\_interest.entry](points_of_interest#id)

### BoxCoded

If you want a box to display where you have to enter a code, this is the field you use.

### BoxMoney

The amount of money the player has to pay for the selected option, appears in the confirmation box as amount of gold, silver, copper.
The DB value you insert here must be given in the number of copper, so 10 gold is entered as 100000 (10g 00s 00c).

### BoxText

This is the text of the window that appears that has "Yes" or "No" as clickable buttons. This is useful if you want a Yes/No confirmation window before the script executes. For example: "Are you sure you want to teleport to Dalaran?".
If BoxBroadCastTextID contains a valid broadcast\_text.ID, it links to broadcast\_text so the content from broadcast\_text is displayed directly instead of the box\_text field content.

### BoxBroadcastTextID

The ID of the same text in [broadcast\_text.ID](broadcast_text#id).

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is [client Build](realmlist#gamebuild) then it was parsed with WDB files from that specific client build and manually edited later for some special necessity.
