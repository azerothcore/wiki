GM commands can be entered mainly in 2 ways. Either by typing it directly into the world console window. In the world console window the leading dot (.) is not mandantory, but you can use it. The other way is using the gm command ingame in the chat console of the wow client. There, all commands must start with a leading dot, f.ex.: .gm on

Note: Some commands are working only by selecting a player or a creature. These commands can not be used in the world console.

# GM Commands 3.x

|Command|Security|Syntax|Description|
|-------|--------|------|-----------|
|account addon|1|`.account addon #addon`|Set expansion addon level allowed. Addon values: 0 - normal, 1 - tbc, 2 - wotlk.|
|account create|4|`.account create $account $password`|Create account and set password to it.|
|account delete|4|`.account delete $account`|Delete account with all characters.|
|account lock country|0|`.account lock country [on/off]`|Allow login from account only from current used Country or remove this requirement.|
|account lock|0|`.account lock [on/off]`|Allow login from account only from current used IP or remove this requirement.|
|account onlinelist|4|`.account onlinelist`|Show list of online accounts.|
|account password|0|`.account password $old_password $new_password $new_password`|Change your account password.|
|account set addon|2|`.account set addon [$account] #addon`|Set user (possible targeted) expansion addon level allowed. Addon values: 0 - normal, 1 - tbc, 2 - wotlk.|
|account set gmlevel|4|`.account set gmlevel [$account] #level [#realmid]`|Set the security level for targeted player (can't be used at self) or for account $name to a level of #level on the realm #realmID. #level may range from 0 to 3. #reamID may be -1 for all realms.|
|account set password|4|`.account set password $account $password $password`|Set password for account.|
|account set|2|`.account set $subcommand`|Type .account set to see the list of possible subcommands or .help account set $subcommand to see info on subcommands|
|account|0|`.account`|Display the access level of your account.|
|achievement add|2|`.achievement add $achievement`|Add an achievement to the targeted player. $achievement: can be either achievement id or achievement link|
|achievement checkall|3|`.achievement checkall`|Check all achievement criteria of the selected player.|
|achievement|2|`.achievement $subcommand`|Type .achievement to see the list of possible subcommands or .help achievement $subcommand to see info on subcommands|
|additem|2|`.additem #itemid/[#itemname]/#shift-click-item-link #itemcount`|Adds the specified number of items of id #itemid (or exact (!) name $itemname in brackets, or link created by shift-click at item in inventory or recipe) to your or selected character inventory. If #itemcount is omitted, only one item will be added. **If #itemcount is negative, it will remove the item(s) from the character.**|
|additemset|2|`.additemset #itemsetid`|Add items from itemset of id #itemsetid to your or selected character inventory. Will add by one example each item from itemset.|
|announce|2|`.announce $MessageToBroadcast`|Send a global message to all players online in chat log.|
|appear|1|`.appear [$charactername]`|Teleport to the given character. Either specify the character name or click on the character's portrait,e.g. when you are in a group. Character can be offline.|
|arena captain|3|`.arena captain #TeamID $name`|A command to set new captain to the team. $name must be in the team|
|arena create|3|`.arena create $name "arena name" [2/3/5]`|Command to create a new Arena-team in game.|
|arena disband|3|`.arena disband #TeamID`|Command to disband Arena-team in game.|
|arena info|2|`.arena info #TeamID`|Command that show info about arena team|
|arena lookup|2|`.arena lookup $name`|Command that give a list of arenateam with the given $name|
|arena rename|3|`.arena rename "oldname" "newname"`|Command to rename Arena-team name.|
|aura|2|`.aura #spellid`|Add the aura from spell #spellid to the selected Unit.|
|ban account|2|`.ban account $account_name $bantime $reason`|Ban account and kick the player if ingame on any character. $bantime: negative value leads to permban, otherwise use a timestring like `4d20h3s`.|
|ban character|2|`.ban character $character_name $bantime $reason`|Ban character and kick that character if ingame. $bantime: negative value leads to permban, otherwise use a timestring like `4d20h3s`.|
|ban ip|2|`.ban ip $Ip $bantime $reason`|Ban IP. $bantime: negative value leads to permban, otherwise use a timestring like `4d20h3s`.|
|ban playeraccount|2|`.ban playeraccount $character_name $bantime $reason`|Ban an account based on the character's name and kick that character if ingame. $bantime: negative value leads to permban, otherwise use a timestring like `4d20h3s`.|
|ban|2|`.ban $subcommand`|Type .ban to see the list of possible subcommands or .help ban $subcommand to see info on subcommands|
|baninfo account|2|`.baninfo account $accountid`|Watch full information about a specific ban.|
|baninfo character|2|`.baninfo character $charactername`|Watch full information about a specific ban.|
|baninfo ip|2|`.baninfo ip $ip`|Watch full information about a specific ban.|
|baninfo|2|`.baninfo $subcommand`|Type .baninfo to see the list of possible subcommands or .help baninfo $subcommand to see info on subcommands|
|bank|2|`.bank`|Show your bank inventory.|
|banlist account|2|`.banlist account [$Name]`|Searches the banlist for a account name pattern or show full list account bans.|
|banlist character|2|`.banlist character $Name`|Searches the banlist for a character name pattern. Pattern required.|
|banlist ip|2|`.banlist ip [$Ip]`|Searches the banlist for a IP pattern or show full list of IP bans.|
|banlist|2|`.banlist $subcommand`|Type .banlist to see the list of possible subcommands or .help banlist $subcommand to see info on subcommands|
|bf enable|3|`.bf enable #battleid`||
|bf start|3|`.bf start #battleid`||
|bf stop|3|`.bf stop #battleid`||
|bf switch|3|`.bf switch #battleid`||
|bf timer|3|`.bf timer #battleid #timer`||
|bindsight|3|`.bindsight`|Binds vision to the selected unit indefinitely. Cannot be used while currently possessing a target.|
|cast back|2|`.cast back #spellid [triggered]`|Selected target will cast #spellid to your character. If 'trigered' or part provided then spell casted with triggered flag.|
|cast dest|2|`.cast dest #spellid #x #y #z [triggered]`|Selected target will cast #spellid at provided destination. If 'trigered' or part provided then spell casted with triggered flag.|
|cast dist|2|`.cast dist #spellid [#dist [triggered]]`|You will cast spell to pint at distance #dist. If 'trigered' or part provided then spell casted with triggered flag. Not all spells can be casted as area spells.|
|cast self|2|`.cast self #spellid [triggered]`|Cast #spellid by target at target itself. If 'trigered' or part provided then spell casted with triggered flag.|
|cast target|2|`.cast target #spellid [triggered]`|Selected target will cast #spellid to his victim. If 'trigered' or part provided then spell casted with triggered flag.|
|cast|2|`.cast #spellid [triggered]`|Cast #spellid to selected target. If no target selected cast to self. If 'trigered' or part provided then spell casted with triggered flag.|
|character changefaction|2|`.character changefaction $name`|Change character faction.|
|character changerace|2|`.character changerace $name`|Change character race.|
|character customize|2|`.character customize [$name]`|Mark selected in game or by $name in command character for customize at next login.|
|character deleted delete|4|`.character deleted delete #guid\$name`|Completely deletes the selected characters. If $name is supplied, only characters with that string in their name will be deleted, if #guid is supplied, only the character with that GUID will be deleted.|
|character deleted list|3|`.character deleted list [#guid\$name]`|Shows a list with all deleted characters. If $name is supplied, only characters with that string in their name will be selected, if #guid is supplied, only the character with that GUID will be selected.|
|character deleted purge|4|`.character deleted purge [#keepDays]`|Completely removes all characters from the database that where deleted more than #keepDays ago. If #keepDays not provided the used value from worldserver.conf option 'CharDelete.KeepDays'. If 'CharDelete.KeepDays' option is disabled (set to value 0) then this command can't be used without the specifying #keepDays parameter.|
|character deleted restore|3|`.character deleted restore #guid\$name [$newname] [#new account]`|Restores deleted characters. If $name is supplied, only characters with that string in their name will be restored, if $guid is supplied, only the character with that GUID will be restored. If $newname is set, the character will be restored with that name instead of the original one. If #newaccount is set, the character will be restored to specific account character list. This works only with one character!|
|character erase|4|`.character erase $name`|Delete character $name. Character finally deleted in case any deleting options.|
|character level|3|`.character level [$playername] [#level]`|Set the level of character with $playername (or the selected if not name provided) by #numberoflevels Or +1 if no #numberoflevels provided). If #numberoflevels is omitted, the level will be increase by 1. If #numberoflevels is 0, the same level will be restarted. If no character is selected and name not provided, increase your level. Command can be used for offline character. All stats and dependent values recalculated. At level decrease talents can be reset if need. Also at level decrease equipped items with greater level requirement can be lost.|
|character rename|2|`.character rename [$name]`|Mark selected in game or by $name in command character for rename at next login.|
|character reputation|2|`.character reputation [$player_name]`|Show reputation information for selected player or player find by $player_name.|
|character titles|2|`.character titles [$player_name]`|Show known titles list for selected player or player find by $player_name.|
|cheat casttime|2|`.cheat casttime [on/off]`|Enables or disables your character's spell cast times.|
|cheat cooldown|2|`.cheat cooldown [on/off]`|Enables or disables your character's spell cooldowns.|
|cheat god|2|`.cheat god [on/off]`|Enables or disables your character's ability to take damage.|
|cheat power|2|`.cheat power [on/off]`|Enables or disables your character's spell cost (e.g mana).|
|cheat status|2|`.cheat status`|Shows the cheats you currently have enabled.|
|cheat taxi|2|`.cheat taxi on/off`|Temporary grant access or remove to all taxi routes for the selected character. If no character is selected, hide or reveal all routes to you.Visited taxi nodes sill accessible after removing access.|
|cheat waterwalk|2|`.cheat waterwalk on/off`|Set on/off waterwalk state for selected player or self if no player selected.|
|cheat|2|`.cheat $subcommand`|Type .cheat to see the list of possible subcommands or .help cheat $subcommand to see info on subcommands|
|combatstop|2|`.combatstop [$playername]`|Stop combat for selected character. If selected non-player then command applied to self. If $playername provided then attempt applied to online player $playername.|
|cometome|3|`.cometome $parameter`|Make selected creature come to your current location (new position not saved to DB).|
|commands|0|`.commands`|Display a list of available commands for your account level.|
|cooldown|2|`.cooldown [#spell_id]`|Remove all (if spell_id not provided) or #spel_id spell cooldown from selected character or you (if no selection).|
|damage|2|`.damage $damage_amount [$school [$spellid]]`|Apply $damage to target. If not $school and $spellid provided then this flat clean melee damage without any modifiers. If $school provided then damage modified by armor reduction (if school physical), and target absorbing modifiers and result applied as melee damage to target. If spell provided then damage modified and applied as spell damage. $spellid can be shift-link.|
|debug areatriggers|3|`.debug areatriggers`|Toggle debug mode for areatriggers. In debug mode GM will be notified if reaching an areatrigger|
|debug arena|3|`.debug arena`|Toggle debug mode for arenas. In debug mode GM can start arena with single player.|
|debug bg|3|`.debug bg`|Toggle debug mode for battlegrounds. In debug mode GM can start battleground with single player.|
|debug entervehicle|3||Enter targeted vehicle.|
|debug getitemstate|3|`.debug getitemstate [unchanged\changed\new\removed\queue\check_all]`|Get specified item state of the items of the selected player.|
|debug getitemvalue|3|`.debug getitemvalue $guid $index`|Get value from item with $guid at $index.|
|debug getvalue|3|`.debug $field [1\0]`|1: get uint32 value of $field of the selected unit; 0: get float value of $field of the selected unit|
|debug hostil|1||Get hostile reference list of the selected unit.|
|debug itemexpire|3|`.debug itemexpire $guid`|Delete the item with $guid.|
|debug lootrecipient|3|`.debug lootrecipient`|Get loot recipient of the selected creature.|
|debug los|3|`.debug los`|Show information about the line of sight status.|
|debug Mod32Value|3|`.debug Mod32Value #field #value`|Add #value to field #field of your character.|
|debug moveflags|3|`.debug moveflags [$newMoveFlags [$newMoveFlags2]]`|No params given will output the current moveflags of the target|
|debug play cinematic|1|`.debug play cinematic #cinematicid`|Play cinematic #cinematicid for you. You stay at place while your mind fly.|
|debug play movie|1|`.debug play movie #movieid`|Play movie #movieid for you.|
|debug play sound|1|`.debug play sound #soundid`|Play sound with #soundid. Sound will be play only for you. Other players do not hear this. Warning: client may have more 5000 sounds...|
|debug send buyerror|3|`.debug send buyerror #errorid`|Test buy error id.|
|debug send channelnotify|3|`.debug send channelnotify #notifytype`|Send #notifytype to the channel "test".|
|debug send chatmmessage|3|`.debug send chatmmessage #msgtype`|Send a message "testtest" of type #msgtype.|
|debug send equiperror|3|`.debug send equiperror #errorid`|Test equip error id.|
|debug send largepacket|3|`.send largepacket`|Send large packet (>128000 bytes).|
|debug send opcode|3|`.debug send opcode`|Sends a packet to the current player as specified in the file "opcode.txt" which has to lie in the server's working directory. Example for the content of the file: `631 uint32 6146` which starts a different background music on the client: Opcode "SMSG_PLAY_MUSIC" (dec 631, hex 0x277) which needs in this case an uint32 to specify the sound ID (here: 6146 "Zone - Orgrimmar02").|
|debug send qinvalidmsg|3|`.debug send qinvalidmsg #questfailedreasons`|Send a quest failed message of type #questfailedreasons to the current player.|
|debug send qpartymsg|3|`.debug send qpartymsg #questsharemessages`|Send a quest share message of type #questsharemessages to the current player.|
|debug send sellerror|3|`.debug send sellerror #errorid`|Test sell error id.|
|debug send setphaseshift|3|`.debug send setphaseshift #phaseshift`|Send phase shift packet to the current player.|
|debug send spellfail|3|`.debug send spellfail #resultid [#arg1] [#arg2]`|Send spell fail packet to the current player using spell result #resultid and optional arguments #arg1 and #arg2.|
|debug setaurastate|3|`.debug setaurastate #aurastatetype`|Modify aura state of the selected unit (#aurastatetype > 0) or reset the state (#aurastatetype = 0).|
|debug setbit|3|`.debug setbit #fieldnumber #bitnumber`|Set bit #bitnumber of field #fieldnumber for the selected unit.|
|debug setitemvalue|3|`.debug getitemvalue $guid $index $value`|Set $value for item with $guid at $index.|
|debug setvalue|3|`.debug $field $value [1\0]`|1: set uint32 $value for $field of the selected unit; 0: set float $value for $field of the selected unit|
|debug spawnvehicle|3|`.debug spawnvehicle #entry [#vehicleid]`|Spawn vehicle with creature template #entry and optional #vehicleid.|
|debug unitstate|3|`.debug unitstate [#unitstate]`|Set #unitstate for the selected unit. If no parameter is specified show the unit state and the react state of the unit.|
|debug uws|3|`.debug uws #worldstate #value`|Send update world state for #worldstate and #value to the current player.|
|debug|2|`.debug $subcommand`|Type .debug to see the list of possible subcommands or .help debug $subcommand to see info on subcommands|
|deserter bg add|3|`.deserter bg add $time`|Adds the bg deserter debuff to your target with $time duration.|
|deserter bg remove|3|`.deserter bg remove`|Removes the bg deserter debuff from your target.|
|deserter instance add|3|`.deserter instance add $time`|Adds the instance deserter debuff to your target with $time duration.|
|deserter instance remove|3|`.deserter instance remove`|Removes the instance deserter debuff from your target.|
|dev|3|`.dev [on/off]`|Enable or Disable in game Dev tag or show current state if on/off not provided.|
|die|2|`.die`|Kill the selected player. If no player is selected, it will kill you.|
|disable add battleground|3|`.disable add battleground $entry $flag $comment`||
|disable add map|3|`.disable add map $entry $flag $comment`||
|disable add outdoorpvp|3|`.disable add outdoorpvp $entry $flag $comment`||
|disable add quest|3|`.disable add quest $entry $flag $comment`||
|disable add spell|3|`.disable add spell $entry $flag $comment`||
|disable add vmap|3|`.disable add vmap $entry $flag $comment`||
|disable remove battleground|3|`.disable remove battleground $entry`||
|disable remove map|3|`.disable remove map $entry`||
|disable remove outdoorpvp|3|`.disable remove outdoorpvp $entry`||
|disable remove quest|3|`.disable remove quest $entry`||
|disable remove spell|3|`.disable remove spell $entry`||
|disable remove vmap|3|`.disable remove vmap $entry`||
|dismount|0|`.dismount`|Dismount you, if you are mounted.|
|distance|3|`.distance`|Display the distance from your character to the selected creature.|
|event activelist|2|`.event activelist`|Show list of currently active events.|
|event start|2|`.event start #event_id`|Start event #event_id. Set start time for event to current moment (change not saved in DB).|
|event stop|2|`.event stop #event_id`|Stop event #event_id. Set start time for event to time in past that make current moment is event stop time (change not saved in DB).|
|event|2|`.event #event_id`|Show details about event with #event_id.|
|explorecheat|3|`.explorecheat [1\0]`|1: Set all zones to explored; 0: Set all zones to unexplored|
|flusharenapoints|3|`.flusharenapoints`|Use it to distribute arena points based on arena team ratings, and start a new week.|
|freeze|2|`.freeze (#player)`|"Freezes" #player and disables his chat. When using this without #name it will freeze your target.|
|gm chat|2|`.gm chat [on/off]`|Enable or disable chat GM MODE (show gm badge in messages) or show current state of on/off not provided.|
|gm fly|2|`.gm fly [on/off]`|Enable/disable gm fly mode.|
|gm ingame|0|`.gm ingame`|Display a list of available in game Game Masters.|
|gm list|3|`.gm list`|Display a list of all Game Masters accounts and security levels.|
|gm visible|2|`.gm visible on/off`|Output current visibility state or make GM visible(on) and invisible(off) for other players.|
|gm|1|`.gm [on/off]`|Enable or Disable in game GM MODE or show current state of on/off not provided.|
|gmannounce|2|`.gmannounce $announcement`|Send an announcement to online Gamemasters.|
|gmnameannounce|2|`.gmnameannounce $announcement`|Send an announcement to all online GM's, displaying the name of the sender.|
|gmnotify|2|`.gmnotify $notification`|Displays a notification on the screen of all online GM's.|
|go creature|1|Syntax:.go creature #creature_guid|Teleport your character to creature with guid #creature_guid..go creature #creature_nameTeleport your character to creature with this name..go creature id #creature_entryTeleport your character to a creature that was spawned from the template with this entry.If more than one creature is found, then you are teleported to the first that is found inside the database.|
|go gobject|1|`.go gobject #object_guid`|Teleport your character to gameobject with guid #object_guid|
|go graveyard|1|`.go graveyard #graveyardId`|Teleport to graveyard with the graveyardId specified.|
|go grid|1|`.go grid #gridX #gridY [#mapId]`|Teleport the gm to center of grid with provided indexes at map #mapId (or current map if it not provided).|
|go taxinode|1|`.go taxinode #taxinode`|Teleport player to taxinode coordinates. You can look up zone using .lookup taxinode $namepart|
|go ticket|2|`.go ticket #ticketid`|Teleports the user to the location where $ticketid was created.|
|go trigger|1|`.go trigger #trigger_id`|Teleport your character to areatrigger with id #trigger_id. Character will be teleported to trigger target if selected areatrigger is telporting trigger.|
|go xyz|1|`.go xyz #x #y [#z [#mapid [#orientation]]]`|Teleport player to point with (#x,#y,#z) coordinates at map #mapid with orientation #orientation. If z is not provided, ground/water level will be used. If mapid is not provided, the current map will be used. If #orientation is not provided, the current orientation will be used.|
|go zonexy|1|`.go zonexy #x #y [#zone]`|Teleport player to point with (#x,#y) client coordinates at ground(water) level in zone #zoneid or current zone if #zoneid not provided. You can look up zone using .lookup area $namepart|
|go|1|`.go $subcommand`|Type .go to see the list of possible subcommands or .help go $subcommand to see info on subcommands|
|gobject activate|2|`.gobject activate #guid`|Activates an object like a door or a button.|
|gobject add temp|2||Adds a temporary gameobject that is not saved to DB.|
|gobject add|3|`.gobject add #id`|Add a game object from game object templates to the world at your current location using the #id. spawntimesecs sets the spawntime, it is optional. Note: this is a copy of .gameobject.|
|gobject delete|3|`.gobject delete #go_guid`|Delete gameobject with guid #go_guid.|
|gobject info|1|`.gobject info [$object_entry]`|Query Gameobject information for selected gameobject or given entry.|
|gobject move|3|`.gobject move #goguid [#x #y #z]`|Move gameobject #goguid to character coordinates (or to (#x,#y,#z) coordinates if its provide).|
|gobject near|3|`.gobject near [#distance]`|Output gameobjects at distance #distance from player. Output gameobject guids and coordinates sorted by distance from character. If #distance not provided use 10 as default value.|
|gobject set phase|3|`.gobject set phase #guid #phasemask`|Gameobject with DB guid #guid phasemask changed to #phasemask with related world vision update for players. Gameobject state saved to DB and persistent.|
|gobject target|1|`.gobject target [#go_id\#go_name_part]`|Locate and show position nearest gameobject. If #go_id or #go_name_part provide then locate and show position of nearest gameobject with gameobject template id #go_id or name included #go_name_part as part.|
|gobject turn|3|`.gobject turn #goguid`|Set for gameobject #goguid orientation same as current character orientation.|
|gobject|2|`.gobject $subcommand`|Type .gobject to see the list of possible subcommands or .help gobject $subcommand to see info on subcommands|
|gps|1|`.gps [$name\$shift-link]`|Display the position information for a selected character or creature (also if player name $name provided then for named player, or if creature/gameobject shift-link provided then pointed creature/gameobject if it loaded). Position information includes X, Y, Z, and orientation, map Id and zone Id|
|group disband|2|`.group disband [$characterName]`|Disbands the given character's group.|
|group join|2|`.group join $AnyCharacterNameFromGroup [$CharacterName]`|Adds to group of player $AnyCharacterNameFromGroup player $CharacterName (or selected).|
|group leader|2|`.group leader [$characterName]`|Sets the given character as his group's leader.|
|group remove|2|`.group remove [$characterName]`|Removes the given character from his group.|
|group|2|`.group $subcommand`|Type .group to see the list of possible subcommands or .help group $subcommand to see info on subcommands|
|groupsummon|2|`.groupsummon [$charactername]`|Teleport the given character and his group to you. Teleported only online characters but original selected group member can be offline.|
|guid|2|`.guid`|Display the GUID for the selected character.|
|guild create|2|`.guild create [$GuildLeaderName] "$GuildName"`|Create a guild named $GuildName with the player $GuildLeaderName (or selected) as leader. Guild name must in quotes.|
|guild delete|2|`.guild delete "$GuildName"`|Delete guild $GuildName. Guild name must in quotes.|
|guild invite|2|`.guild invite [$CharacterName] "$GuildName"`|Add player $CharacterName (or selected) into a guild $GuildName. Guild name must in quotes.|
|guild rank|2|`.guild rank [$CharacterName] #Rank`|Set for player $CharacterName (or selected) rank #Rank in a guild.|
|guild uninvite|2|`.guild uninvite [$CharacterName]`|Remove player $CharacterName (or selected) from a guild.|
|guild|2|`.guild $subcommand`|Type .guild to see the list of possible subcommands or .help guild $subcommand to see info on subcommands|
|help|0|`.help [$command]`|Display usage instructions for the given $command. If no $command provided show list available commands.|
|hidearea|3|`.hidearea #areaid`|Hide the area of #areaid to the selected character. If no character is selected, hide this area to you.|
|~~honor add kill~~ NOT IMPLEMENTED|2|gi`.honor add kill`|Add the targeted unit as one of your pvp kills today (you only get honor if it's a racial leader or a player)|
|honor add|2|`.honor add $amount`|Add a certain amount of honor (gained today) to the selected player.|
|honor update|2|`.honor update`|Force the yesterday's honor fields to be updated with today's data, which will get reset for the selected player.|
|honor|2|`.honor $subcommand`|Type .honor to see the list of possible subcommands or .help honor $subcommand to see info on subcommands|
|instance getbossstate|1|`.instance getbossstate $bossId [$Name]`|Gets the current EncounterState for the provided boss id. If no character name is provided, the current map will be used as target.|
|instance listbinds|1|`.instance listbinds`|Lists the binds of the selected player.|
|instance savedata|3|`.instance savedata`|Save the InstanceData for the current player's map to the DB.|
|instance setbossstate|2|`.instance setbossstate $bossId $encounterState [$Name]`|Sets the EncounterState for the given boss id to a new value. EncounterStates range from 0 to 5. If no character name is provided, the current map will be used as target.|
|instance stats|1|`.instance stats`|Shows statistics about instances.|
|instance unbind|2|`.instance unbind <mapid\all> [difficulty]`|Clear all/some of player's binds|
|instance|1|`.instance $subcommand`|Type .instance to see the list of possible subcommands or .help instance $subcommand to see info on subcommands|
|itemmove|2|`.itemmove #sourceslotid #destinationslotid`|Move an item from slots #sourceslotid to #destinationslotid in your inventory Not yet implemented|
|kick|2|`.kick [$charactername] [$reason]`|Kick the given character name from the world with or without reason. If no character name is provided then the selected player (except for yourself) will be kicked. If no reason is provided, default is "No Reason".|
|learn all crafts|2|`.learn crafts`|Learn all professions and recipes.|
|learn all default|2|`.learn all default [$playername]`|Learn for selected/$playername player all default spells for his race/class and spells rewarded by completed quests.|
|learn all gm|2|`.learn all gm`|Learn all default spells for Game Masters.|
|learn all lang|2|`.learn all lang`|Learn all languages|
|learn all my class|2|`.learn all my class`|Learn all spells and talents available for his class.|
|learn all my pettalents|2|`.learn all my pettalents`|Learn all talents for your pet available for his creature type (only for hunter pets).|
|learn all my spells|2|`.learn all my spells`|Learn all spells (except talents and spells with first rank learned as talent) available for his class.|
|learn all my talents|2|`.learn all my talents`|Learn all talents (and spells with first rank learned as talent) available for his class.|
|learn all recipes|2|`.learn all recipes [$profession]`|Learns all recipes of specified profession and sets skill level to max. Example: .learn all recipes enchanting|
|learn|2|`.learn #spell [all]`|Selected character learn a spell of id #spell. If 'all' provided then all ranks learned.|
|levelup|2|`.levelup [$playername] [#numberoflevels]`|Increase/decrease the level of character with $playername (or the selected if not name provided) by #numberoflevels Or +1 if no #numberoflevels provided). If #numberoflevels is omitted, the level will be increase by 1. If #numberoflevels is 0, the same level will be restarted. If no character is selected and name not provided, increase your level. Command can be used for offline character. All stats and dependent values recalculated. At level decrease talents can be reset if need. Also at level decrease equipped items with greater level requirement can be lost.|
|lfg clean|3|`.flg clean`|Cleans current queue, only for debugging purposes.|
|lfg group|1|`.lfg group`|Shows information about all players in the group (state, roles, comment, dungeons selected).|
|lfg options|2|`.lfg options [new value]`|Shows current lfg options. New value is set if extra param is present.|
|lfg player|1|`.lfg player`|Shows information about player (state, roles, comment, dungeons selected).|
|lfg queue|1|`.lfg queue`|Shows info about current lfg queues.|
|linkgrave|3|`.linkgrave #graveyard_id [alliance\horde]`|Link current zone to graveyard for any (or alliance/horde faction ghosts). This let character ghost from zone teleport to graveyard after die if graveyard is nearest from linked to zone and accept ghost of this faction. Add only single graveyard at another map and only if no graveyards linked (or planned linked at same map).|
|list auras|1|`.list auras`|List auras (passive and active) of selected creature or player. If no creature or player is selected, list your own auras.|
|list creature|1|`.list creature #creature_id [#max_count]`|Output creatures with creature id #creature_id found in world. Output creature guids and coordinates sorted by distance from character. Will be output maximum #max_count creatures. If #max_count not provided use 10 as default value.|
|list gobject|1|`.list gobject #gameobject_id [#max_count]`|Output gameobjects with gameobject id #gameobject_id found in world. Output gameobject guids and coordinates sorted by distance from character. Will be output maximum #max_count gameobject. If #max_count not provided use 10 as default value.|
|list item|1|`.list item #item_id [#max_count]`|Output items with item id #item_id found in all character inventories, mails, auctions, and guild banks. Output item guids, item owner guid, owner account and owner name (guild name and guid in case guild bank). Will be output maximum #max_count items. If #max_count not provided use 10 as default value.|
|list|1|`.list $subcommand`|Type .list to see the list of possible subcommands or .help list $subcommand to see info on subcommands|
|lookup area|1|`.lookup area $namepart`|Looks up an area by $namepart, and returns all matches with their area ID's.|
|lookup creature|1|`.lookup creature $namepart`|Looks up a creature by $namepart, and returns all matches with their creature ID's.|
|lookup event|1|`.lookup event $name`|Attempts to find the ID of the event with the provided $name.|
|lookup faction|1|`.lookup faction $name`|Attempts to find the ID of the faction with the provided $name.|
|lookup gobject|1|`.lookup gobject $objname`|Return gameobject(s) ID matching $objname.|
|lookup item|1|`.lookup item $itemname`|Looks up an item by $itemname, and returns all matches with their Item ID's.|
|lookup itemset|1|`.lookup itemset $itemname`|Looks up an item set by $itemname, and returns all matches with their Item set ID's.|
|lookup map|1|`.lookup map $namepart`|Looks up a map by $namepart, and returns all matches with their map ID's.|
|lookup player account|2|`.lookup player account $account ($limit)`|Searchs players, which account username is $account with optional parametr $limit of results.|
|lookup player email|2|`.lookup player email $email ($limit)`|Searchs players, which account email is $email with optional parametr $limit of results.|
|lookup player ip|2|`.lookup player ip $ip ($limit)`|Searchs players, which account ast_ip is $ip with optional parametr $limit of results.|
|lookup quest|1|`.lookup quest $namepart`|Looks up a quest by $namepart, and returns all matches with their quest ID's.|
|lookup skill|1|`.lookup skill $$namepart`|Looks up a skill by $namepart, and returns all matches with their skill ID's.|
|lookup spell id|1|`.lookup spell id #spellid`|Looks up a spell by #spellid, and returns the match with its spell name.|
|lookup spell|1|`.lookup spell $namepart`|Looks up a spell by $namepart, and returns all matches with their spell ID's.|
|lookup taxinode|1|`.lookup taxinode $substring`|Search and output all taxinodes with provide $substring in name.|
|lookup teleport|1|`.lookup teleport $substring`|Search and output all .teleport command locations with provide $substring in name.|
|lookup title|1|`.lookup title $$namepart`|Looks up a title by $namepart, and returns all matches with their title ID's and index's.|
|lookup|1|`.lookup $subcommand`|Type .lookup to see the list of possible subcommands or .help lookup $subcommand to see info on subcommands|
|mailbox|1|`.mailbox`|Open mailbox.|
|maxskill|2|`.maxskill`|Sets all skills of the targeted player to their maximum values for its current level.|
|mmap loadedtiles|3|`.mmap loadedtiles`|To show which tiles are currently loaded.|
|mmap loc|3|`.mmap loc`|To print on which tile one is.|
|mmap path|3|`.mmap path`|To calculate and show a path to current select unit.|
|mmap stats|3|`.mmap stats`|To show information about current state of mmaps.|
|mmap testarea|3|`.mmap testarea`|To calculate paths for all nearby npcs to player.|
|modify arenapoints|1|`.modify arenapoints #value`|Add $amount arena points to the selected player.|
|modify bit|2|`.modify bit #field #bit`|Toggle the #bit bit of the #field field for the selected player. If no player is selected, modify your character.|
|modify drunk|2|`.modify drunk #value`|Set drunk level to #value (0..100). Value 0 remove drunk state, 100 is max drunked state.|
|modify energy|2|`.modify energy #energy`|Modify the energy of the selected player. If no player is selected, modify your energy.|
|modify faction|3|`.modify faction #factionid #flagid #npcflagid #dynamicflagid`|Modify the faction and flags of the selected creature. Without arguments, display the faction and flags of the selected creature.|
|modify gender|2|`.modify gender male/female`|Change gender of selected player.|
|modify honor|2|`.modify honor $amount`|Add $amount honor points to the selected player.|
|modify hp|2|`.modify hp #newhp`|Modify the hp of the selected player. If no player is selected, modify your hp.|
|modify mana|2|`.modify mana #newmana`|Modify the mana of the selected player. If no player is selected, modify your mana.|
|modify money|2|`.modify money #money`|Add or remove money to the selected player. If no player is selected, modify your money. #gold can be negative to remove money.|
|modify mount|2|`.modify mount #id #speed`|Display selected player as mounted at #id creature and set speed to #speed value.|
|modify phase|2|`.modify phase #phasemask`|Selected character phasemask changed to #phasemask with related world vision update. Change active until in game phase changed, or GM-mode enable/disable, or re-login. Character pts pasemask update to same value.|
|modify rage|2|`.modify rage #newrage`|Modify the rage of the selected player. If no player is selected, modify your rage.|
|modify reputation|2|`.modify reputation #repId (#repvalue \ $rankname [#delta])`|Sets the selected players reputation with faction #repId to #repvalue or to $reprank. If the reputation rank name is provided, the resulting reputation will be the lowest reputation for that rank plus the delta amount, if specified. You can use '.pinfo rep' to list all known reputation ids, or use '.lookup faction $name' to locate a specific faction id.|
|modify runicpower|2|`.modify runicpower #newrunicpower`|Modify the runic power of the selected player. If no player is selected, modify your runic power.|
|modify scale|2|`.modify scale #scale`|Modify size of the selected player or creature to "normal scale"*rate. If no player or creature is selected, modify your size. #rate may range from 0.1 to 10.|
|modify speed all|2|`.modify aspeed #rate`|Modify all speeds -run,swim,run back,swim back- of the selected player to "normalbase speed for this move type"*rate. If no player is selected, modify your speed. #rate may range from 0.1 to 50.|
|modify speed backwalk|2|`.modify speed backwalk #rate`|Modify the speed of the selected player while running backwards to "normal walk back speed"*rate. If no player is selected, modify your speed. #rate may range from 0.1 to 50.|
|modify speed fly|2|`.modify speed fly #rate`|Modify the flying speed of the selected player to "normal flying speed"*rate. If no player is selected, modify your speed. #rate may range from 0.1 to 50.|
|modify speed swim|2|`.modify speed swim #rate`|Modify the swim speed of the selected player to "normal swim speed"*rate. If no player is selected, modify your speed. #rate may range from 0.1 to 50.|
|modify speed walk|2|`.modify speed bwalk #rate`|Modify the speed of the selected player while running to "normal walk speed"*rate. If no player is selected, modify your speed. #rate may range from 0.1 to 50.|
|modify speed|2|`.modify speed $speedtype #rate`|Modify the running speed of the selected player to "normal base run speed"= 1. If no player is selected, modify your speed. $speedtypes may be fly, all, walk, backwalk, or swim. #rate may range from 0.1 to 50.|
|modify spell|2||TODO|
|modify standstate|2|`.modify standstate #emoteid`|Change the emote of your character while standing to #emoteid.|
|modify talentpoints|2|`.modify talentpoints #amount`|Set free talent points for selected character or character's pet. It will be reset to default expected at next levelup/login/quest reward.|
|modify|2|`.modify $subcommand`|Type .modify to see the list of possible subcommands or .help modify $subcommand to see info on subcommands|
|morph reset|1|`.morph reset`|Reset the original model for the selected target.|
|morph|1|`.morph #displayid`|Change your current model id to #displayid.|
|movegens|3|`.movegens`|Show movement generators stack for selected creature or player.|
|mute|2|`.mute [$playerName] $timeInMinutes [$reason]`|Disible chat messaging for any character from account of character $playerName (or currently selected) at $timeInMinutes minutes. Player can be offline.|
|mutehistory|2|`.mutehistory #accountname`|Show mute history for account #accountname.|
|nameannounce|2|`.nameannounce $announcement`|Send an announcement to all online players, displaying the name of the sender.|
|neargrave|2|`.neargrave [alliance\horde]`|Find nearest graveyard linked to zone (or only nearest from accepts alliance or horde faction ghosts).|
|notify|2|`.notify $MessageToBroadcast`|Send a global message to all players online in screen.|
|npc add formation|3|`.npc add formation $leader`|Add selected creature to a leader's formation.|
|npc add item|3|`.npc add item #itemId <#maxcount><#incrtime><#extendedcost>r`|Add item #itemid to item list of selected vendor. Also optionally set max count item in vendor item list and time to item count restoring and items ExtendedCost.|
|npc add move|3|`.npc add move #creature_guid [#waittime]`|Add your current location as a waypoint for creature with guid #creature_guid. And optional add wait time.|
|npc add temp|3|`.npc add temp`|Adds temporary NPC, not saved to database.|
|npc add|3|`.npc add #creatureid`|Spawn a creature by the given template id of #creatureid.|
|npc delete item|3|`.npc delete item #itemId`|Remove item #itemid from item list of selected vendor.|
|npc delete|3|`.npc delete [#guid]`|Delete creature with guid #guid (or the selected if no guid is provided)|
|npc follow stop|2|`.npc follow stop`|Selected creature (non pet) stop follow you.|
|npc follow|2|`.npc follow start`|Selected creature start follow you until death/fight/etc.|
|npc info|1|`.npc info`|Display a list of details for the selected creature. The list includes: - GUID, Faction, NPC flags, Entry ID, Model ID, - Level, - Health (current/maximum), - Field flags, dynamic flags, faction template, - Position information, - and the creature type, e.g. if the creature is a vendor.|
|npc move|3|`.npc move [#creature_guid]`|Move the targeted creature spawn point to your coordinates.|
|npc playemote|3|`.npc playemote #emoteid`|Make the selected creature emote with an emote of id #emoteid.|
|npc say|2|`.npc say $message`|Make selected creature say specified message.|
|npc set allowmove|3|`.npc set allowmove`|Enable or disable movement creatures in world. Not implemented.|
|npc set data|3|`.npc set data $field $data`|Sets data for the selected creature. Used for testing Scripting|
|npc set entry|3|`.npc set entry $entry`|Switch selected creature with another entry from creature_template. - New creature.id value not saved to DB.|
|npc set faction original|3|`.npc set faction original`|Revert the temporal faction of the selected creature.|
|npc set faction permanent|3|`.npc set faction permanent #factionid`|Permanently set the faction of the selected creature to #factionid.|
|npc set faction temp|3|`.npc set faction temp #factionid`|Temporarily set the faction of the selected creature to #factionid.|
|npc set flag|3|`.npc set flag #npcflag`|Set the NPC flags of creature template of the selected creature and selected creature to #npcflag. NPC flags will applied to all creatures of selected creature template after server restart or grid unload/load.|
|npc set level|3|`.npc set level #level`|Change the level of the selected creature to #level. #level may range from 1 to (CONFIG_MAX_PLAYER_LEVEL) + 3.|
|npc set link|3|`.npc set link $creatureGUID`|Links respawn of selected creature to the condition that $creatureGUID defined is alive.|
|npc set model|3|`.npc set model #displayid`|Change the model id of the selected creature to #displayid.|
|npc set movetype|3|`.npc set movetype [#creature_guid] stay/random/way [NODEL]`|Set for creature pointed by #creature_guid (or selected if #creature_guid not provided) movement type and move it to respawn position (if creature alive). Any existing waypoints for creature will be removed from the database if you do not use NODEL. If the creature is dead then movement type will applied at creature respawn. Make sure you use NODEL, if you want to keep the waypoints.|
|npc set phase|3|`.npc set phase #phasemask`|Selected unit or pet phasemask changed to #phasemask with related world vision update for players. In creature case state saved to DB and persistent. In pet case change active until in game phase changed for owner, owner re-login, or GM-mode enable/disable..|
|npc set spawntime|3|`.npc set spawntime #time`|Adjust spawntime of selected creature to time.|
|npc set wanderdistance|3|`.npc set wanderdistance #dist`|Adjust wanderdistance of selected creature to dist.|
|npc tame|2|`.npc tame`|Tame the selected creature (if it is tameable).|
|npc textemote|2|`.npc textemote #emoteid`|Make the selected creature to do textemote with an emote of id #emoteid.|
|npc whisper|2|`.npc whisper #playerguid #text`|Make the selected npc whisper #text to #playerguid.|
|npc yell|2|`.npc yell $message`|Make selected creature yell specified message.|
|npc|2|`.npc $subcommand`|Type .npc to see the list of possible subcommands or .help npc $subcommand to see info on subcommands|
|pdump load|3|`.pdump load $filename $account [$newname] [$newguid]`|Load character dump from dump file into character list of $account with saved or $newname, with saved (or first free) or $newguid guid.|
|pdump write|3|`.pdump write $filename $playerNameOrGUID`|Write character dump with name/guid $playerNameOrGUID to file $filename.|
|pdump|3|`.pdump $subcommand`|Type .pdump to see the list of possible subcommands or .help pdump $subcommand to see info on subcommands|
|pet create|2|`.pet create`|Creates a pet of the selected creature.|
|pet learn|2|`.pet learn`|Learn #spellid to pet.|
|pet unlearn|2|`.pet unlean`|unLearn #spellid to pet.|
|pet|2|`.pet $subcommand`|Type .pet to see the list of possible subcommands or .help pet $subcommand to see info on subcommands|
|pinfo|2|`.pinfo [$player_name/#GUID]`|Output account information for selected player or player find by $player_name or #GUID.|
|playall|2|`.playall #soundid`|Player a sound to whole server.|
|player learn|2|`.player learn #playername #spell [all]`|Learn spell #spell for the specified player. If 'all' is added then all ranks are learned.|
|player unlearn|2|`.player unlearn #playername #spell [all]`|Unlearn spell #spell for the specified player. If 'all' is added then all ranks are unlearned.|
|possess|2|`.possess`|Possesses indefinitely the selected creature.|
|quest add|2|`.quest add #quest_id`|Add to character quest log quest #quest_id. Quest started from item can't be added by this command but correct .additem call provided in command output.|
|quest complete|2|`.quest complete #questid`|Mark all quest objectives as completed for target character active quest. After this target character can go and get quest reward.|
|quest remove|2|`.quest remove #quest_id`|Set quest #quest_id state to not completed and not active (and remove from active quest list) for selected player.|
|quest reward|2|`.quest reward #questId`|Grants quest reward to selected player and removes quest from his log (quest must be in completed state).|
|quest|2|`.quest $subcommand`|Type .quest to see the list of possible subcommands or .help quest $subcommand to see info on subcommands|
|recall|2|`.recall [$playername]`|Teleport $playername or selected player to the place where he has been before last use of a teleportation command. If no $playername is entered and no player is selected, it will teleport you.|
|reload access_requirement|3|`.reload access_requirement`|Reload access_requirement table.|
|reload achievement_reward_locale|3|`.reload achievement_reward_locale`|Reload achievement_reward_locale table.|
|reload achievement_reward|3|`.reload achievement_reward`|Reload achievement_reward table.|
|reload acore_string|3|`.reload acore_string`|Reload acore_string table.|
|reload all achievement|3|`.reload all achievement`|Reload achievement_reward, achievement_criteria_data tables.|
|reload all area|3|`.reload all area`|Reload areatrigger_teleport, areatrigger_tavern, game_graveyard_zone tables.|
|reload all gossips|3|`.reload all gossips`|Reload gossip_menu, gossip_menu_option, gossip_scripts, points_of_interest tables.|
|reload all item|3|`.reload all item`|Reload page_text, item_enchantment_table tables.|
|reload all locales|3|`.reload all locales`|Reload all locales_* tables with reload support added and that can be safe reloaded.|
|reload all loot|3|`.reload all loot`|Reload all *_loot_template tables. This can be slow operation with lags for server run.|
|reload all npc|3|`.reload all npc`|Reload npc_option, npc_trainer, npc vendor, points of interest tables.|
|reload all quest|3|`.reload all quest`|Reload all quest related tables if reload support added for this table and this table can be safe reloaded.|
|reload all scripts|3|`.reload all scripts`|Reload gameobject_scripts, event_scripts, quest_end_scripts, quest_start_scripts, spell_scripts, db_script_string, waypoint_scripts tables.|
|reload all spell|3|`.reload all spell`|Reload all spell_* tables with reload support added and that can be safe reloaded.|
|reload all|3|`.reload all`|Reload all tables with reload support added and that can be safe reloaded.|
|reload areatrigger_involvedrelation|3|`.reload areatrigger_involvedrelation`|Reload areatrigger_involvedrelation table.|
|reload areatrigger_tavern|3|`.reload areatrigger_tavern`|Reload areatrigger_tavern table.|
|reload areatrigger_teleport|3|`.reload areatrigger_teleport`|Reload areatrigger_teleport table.|
|reload auctions|3|`.reload auctions`|Reload dynamic data tables from the database.|
|reload autobroadcast|3|`.reload autobroadcast`|Reload autobroadcast table.|
|reload battleground_template|3|`.reload battleground_template`|Reload battleground_template table.|
|reload broadcast_text|3|`.reload broadcast_text`|Reload broadcast_text table.|
|reload command|3|`.reload command`|Reload command table.|
|reload conditions|3||Reload conditions table.|
|reload config|3|`.reload config`|Reload config settings (by default stored in worldserver.conf). Not all settings can be change at reload: some new setting values will be ignored until restart, some values will applied with delay or only to new objects/maps, some values will explicitly rejected to change at reload.|
|reload creature_linked_respawn|2|`.reload creature_linked_respawn`|Reload creature_linked_respawn table.|
|reload creature_loot_template|3|`.reload creature_loot_template`|Reload creature_loot_template table.|
|reload creature_onkill_reputation|3|`.reload creature_onkill_reputation`|Reload creature_onkill_reputation table.|
|reload creature_questender|3|`.reload creature_questender`|Reload creature_questender table.|
|reload creature_queststarter|3|`.reload creature_queststarter`|Reload creature_queststarter table.|
|reload creature_template_locale|3|`.reload creature_template_locale`|Reload creature_template_locale table.|
|reload creature_template|3|`.reload creature_template $entry`|Reload the specified creature's template.|
|reload creature_text_locale|3|`.reload creature_text_locale`|Reload creature_text_locale table.|
|reload creature_text|3|`.reload creature_text`|Reload creature_text table.|
|reload disables|3|`.reload disables`|Reload disables table.|
|reload disenchant_loot_template|3|`.reload disenchant_loot_template`|Reload disenchant_loot_template table.|
|reload event_scripts|3|`.reload event_scripts`|Reload event_scripts table.|
|reload fishing_loot_template|3|`.reload fishing_loot_template`|Reload fishing_loot_template table.|
|reload game_tele|3|`.reload game_tele`|Reload game_tele table.|
|reload gameobject_loot_template|3|`.reload gameobject_loot_template`|Reload gameobject_loot_template table.|
|reload gameobject_questender|3|`.reload gameobject_questender`|Reload gameobject_questender table.|
|reload gameobject_queststarter|3|`.reload gameobject_queststarter`|Reload gameobject_queststarter table.|
|reload gameobject_template_locale|3|`.reload gameobject_template_locale`|Reload gameobject_template_locale table.|
|reload gm_tickets|3|`.reload gm_tickets`|Reload gm_tickets table.|
|reload gossip_menu_option_locale|3|`.reload gossip_menu_option_locale`|Reload gossip_menu_option_locale table.||reload item_enchantment_template|3|`.reload item_enchantment_template`|Reload item_enchantment_template table.|
|reload gossip_menu_option|3|`.reload gossip_menu_option`|Reload gossip_menu_option table.|
|reload gossip_menu|3|`.reload gossip_menu`|Reload gossip_menu table.|
|reload item_loot_template|3|`.reload item_loot_template`|Reload item_loot_template table.|
|reload item_set_name_locale|3|`.reload item_set_name_locale`|Reload item_set_name_locale table.|
|reload item_set_names|3|`.reload item_set_names`|Reload item_set_names table.|
|reload item_template_locale|3|`.reload item_template_locale`|Reload item_template_locale table.|
|reload lfg_dungeon_rewards|3|`.reload lfg_dungeon_rewards`|Reload lfg_dungeon_rewards table.|
|reload mail_level_reward|3|`.reload mail_level_reward`|Reload mail_level_reward table.|
|reload mail_loot_template|3|`.reload quest_mail_loot_template`|Reload quest_mail_loot_template table.|
|reload milling_loot_template|3|`.reload milling_loot_template`|Reload milling_loot_template table.|
|reload npc_spellclick_spells|3|`.reload npc_spellclick_spells`|Reload npc_spellclick_spells table.|
|reload npc_text_locale|3|`.reload npc_text_locale`|Reload npc_text_locale table.|
|reload npc_trainer|3|`.reload npc_trainer`|Reload npc_trainer table.|
|reload npc_vendor|3|`.reload npc_vendor`|Reload npc_vendor table.|
|reload page_text_locale|3|`.reload page_text_locale`|Reload page_tex_locale table.|
|reload page_text|3|`.reload page_text`|Reload page_text table.|
|reload pickpocketing_loot_template|3|`.reload pickpocketing_loot_template`|Reload pickpocketing_loot_template table.|
|reload points_of_interest_locale|3|`.reload points_of_interest_locale`|Reload points_of_interest_locale table.|
|reload points_of_interest|3|`.reload points_of_interest`|Reload points_of_interest table.|
|reload prospecting_loot_template|3|`.reload prospecting_loot_template`|Reload prospecting_loot_template table.|
|reload quest_offer_reward_locale|3|`.reload quest_offer_reward_locale`|Reload quest_offer_reward_locale table.|
|reload quest_poi|3|`.reload quest_poi`|Reload quest_poi table.|
|reload quest_request_item_locale|3|`.reload quest_request_item_locale`|Reload quest_request_item_locale table.|
|reload quest_template_locale|3|`.reload quest_template_locale`|Reload quest_template_locale table.|
|reload quest_template|3|`.reload quest_template`|Reload quest_template table.|
|reload reference_loot_template|3|`.reload reference_loot_template`|Reload reference_loot_template table.|
|reload reputation_reward_rate|3|`.reload reputation_reward_rate`|Reload reputation_reward_rate table.|
|reload reputation_spillover_template|3|`.reload reputation_spillover_template`|Reload reputation_spillover_template table.|
|reload reserved_name|3|`.reload reserved_name`|Reload reserved_name table.|
|reload skill_discovery_template|3|`.reload skill_discovery_template`|Reload skill_discovery_template table.|
|reload skill_extra_item_template|3|`.reload skill_extra_item_template`|Reload skill_extra_item_template table.|
|reload skill_fishing_base_level|3|`.reload skill_fishing_base_level`|Reload skill_fishing_base_level table.|
|reload skinning_loot_template|3|`.reload skinning_loot_template`|Reload skinning_loot_template table.|
|reload smart_scripts|3|`.reload smart_scripts`|Reload smart_scripts table.|
|reload spell_area|3|`.reload spell_area`|Reload spell_area table.|
|reload spell_bonus_data|3|`.reload spell_bonus_data`|Reload spell_bonus_data table.|
|reload spell_group_stack_rules|3|`.reload spell_group`|Reload spell_group_stack_rules table.|
|reload spell_group|3|`.reload spell_group`|Reload spell_group table.|
|reload spell_linked_spell|3|`.reload spell_linked_spell`|Reloads the spell_linked_spell DB table.|
|reload spell_loot_template|3|`.reload spell_loot_template`|Reload spell_loot_template table.|
|reload spell_pet_auras|3|`.reload spell_pet_auras`|Reload spell_pet_auras table.|
|reload spell_proc_event|3|`.reload spell_proc_event`|Reload spell_proc_event table.|
|reload spell_proc|3|`.reload spell_proc`|Reload spell_proc table.|
|reload spell_required|3|`.reload spell_required`|Reload spell_required table.|
|reload spell_scripts|3|`.reload spell_scripts`|Reload spell_scripts table.|
|reload spell_target_position|3|`.reload spell_target_position`|Reload spell_target_position table.|
|reload spell_threats|3|`.reload spell_threats`|Reload spell_threats table.|
|reload vehicle_accessory|3|`.reload vehicle_accessory`|Reloads GUID-based vehicle accessory definitions from the database.|
|reload vehicle_template_accessory|3|`.reload vehicle_template_accessory`|Reloads entry-based vehicle accessory definitions from the database.||reload warden_action|3|`.reload warden_action`|Reload warden_action table.|
|reload waypoint_data|3|`.reload waypoint_data`|Will reload waypoint_data table.|
|reload waypoint_scripts|3|`.reload waypoint_scripts`|Reload waypoint_scripts table.|
|reload|3|`.reload $subcommand`|Type .reload to see the list of possible subcommands or .help reload $subcommand to see info on subcommands|
|repairitems|2|`.repairitems`|Repair all selected player's items.|
|reset achievements|4|`.reset achievements [$playername]`|Reset achievements data for selected or named (online or offline) character. Achievements for persistance progress data like completed quests/etc re-filled at reset. Achievements for events like kills/casts/etc will lost.|
|reset all|4|`.reset all [spells/talents]`|Request reset spells or talents (including talents for all character's pets if any) at next login each existed character.|
|reset honor|3|`.reset honor [Playername]`|Reset all honor data for targeted character.|
|reset level|3|`.reset level [Playername]`|Reset level to 1 including reset stats and talents. Equipped items with greater level requirement can be lost.|
|reset spells|3|`.reset spells [Playername]`|Removes all non-original spells from spellbook. . Playername can be name of offline character.|
|reset stats|3|`.reset stats [Playername]`|Resets(recalculate) all stats of the targeted player to their original VALUESat current level.|
|reset talents|3|`.reset talents [Playername]`|Removes all talents of the targeted player or pet or named player Playername can be name of offline character. With player talents also will be reset talents for all character's pets if any.|
|reset|3|`.reset $subcommand`|Type .reset to see the list of possible subcommands or .help reset $subcommand to see info on subcommands|
|respawn|2|`.respawn`|Respawn target creature and GO without waiting for respawn time expiration. If no target provided, respawn all nearest creatures. |
|revive|2|`.revive`|Revive the selected player. If no player is selected, it will revive you.|
|save|0|`.save`|Saves your character.|
|saveall|2|`.saveall`|Save all characters in game.|
|send items|2|`.send items #playername "#subject" "#text" itemid1[:count1] itemid2[:count2] ... itemidN[:countN]`|Send a mail to a player. Subject and mail text must be in "". If for itemid not provided related count values then expected 1, if count > max items in stack then items will be send in required amount stacks. All stacks amount in mail limited to 12.|
|send mail|2|`.send mail #playername "#subject" "#text"`|Send a mail to a player. Subject and mail text must be in "".|
|send message|3|`.send message $playername $message`|Send screen message to player from ADMINISTRATOR. **Will return an error if player is offline (can be problematic with SOAP for example)!**|
|send money|2|`.send money #playername "#subject" "#text" #money`|Send mail with money to a player. Subject and mail text must be in "".|
|server corpses|2|`.server corpses`|Triggering corpses expire check in world.|
|server exit|4|`.server exit`|Terminate worldserver NOW. Exit code 0.|
|server idlerestart cancel|3|`.server idlerestart cancel`|Cancel the restart/shutdown timer if any.|
|server idlerestart|4|`.server idlerestart #delay [#exit_code]`|Restart the server after #delay seconds if no active connections are present (no players). Use #exit_code to change the exit code, default = 2.|
|server idleshutdown cancel|4|`.server idleshutdown cancel`|Cancel the restart/shutdown timer if any.|
|server idleshutdown|3|`.server idleshutdown #delay [#exit_code]`|Shut the server down after #delay seconds if no active connections are present (no players). Use #exit_code to change the exit code, default = 0.|
|server info|0|`.server info`|Display server version and the number of connected players.|
|server motd|0|`.server motd`|Show server Message of the day.|
|server restart cancel|3|`.server restart cancel`|Cancel the restart/shutdown timer if any.|
|server restart|3|`.server restart #delay [#exit_code]`|Restart the server after #delay seconds. Use #exit_code to change the exit code, default = 2.|
|server set closed|4|server set closed [on/off]|Sets whether the world accepts new client connectsions.|
|server set difftime|4|`.server set difftime $time`|$time (in milliseconds) update time diff is written to the log file.|
|server set loglevel|4|`.server set loglevel $facility $name $loglevel`|$facility can take the values: appender (a) or logger (l). $loglevel can take the values: disabled (0), trace (1), debug (2), info (3), warn (4), error (5) or fatal (6)|
|server set motd|3|`.server set motd $MOTD`|Set server Message of the day.|
|server shutdown cancel|3|`.server shutdown cancel`|Cancel the restart/shutdown timer if any.|
|server shutdown|3|`.server shutdown #delay [#exit_code]`|Shut the server down after #delay seconds. Use #exit_code to change the exit code, default = 0.|
|server togglequerylog|4|`.server togglequerylog`|Toggle SQL query log on/off.|
|server|3|`.server $subcommand`|Type .server to see the list of possible subcommands or .help server $subcommand to see info on subcommands|
|setskill|2|`.setskill #skill #level [#max]`|Set a skill of id #skill with a current skill value of #level and a maximum value of #max (or equal current maximum if not provide) for the selected character. If no character is selected, you learn the skill.|
|showarea|2|`.showarea #areaid`|Reveal the area of #areaid to the selected character. If no character is selected, reveal this area to you.|
|skirmish|3|`.skirmish [arena] [XvX] [Nick1] [Nick2] ... [NickN]`|[arena] can be "all" or comma-separated list of possible arenas (NA,BE,RL,DS,RV). [XvX] can be 1v1, 2v2, 3v3, 5v5. After [XvX] specify enough nicknames for that mode.|
|spect leave|0|`.spect leave`|Leave arena spectator.|
|spect reset|0|`.spect reset`|Reset arena spectator.|
|spect spectate|0|`.spect spectate #playername`|Start arena spectator, watch #playername.|
|spect version|0|`.spect version`|Check spectator addon version.|
|spect watch|0|`.spect watch #playername`|Watch #playername.|
|summon|2|`.summon [$charactername]`|Teleport the given character to you. Character can be offline.|
|teleport add|3|`.teleport add $name`|Add current your position to .teleport command target locations list with name $name.|
|teleport del|3|`.teleport del $name`|Remove location with name $name for .teleport command locations list.|
|teleport group|2|`.teleport group#location`|Teleport a selected player and his group members to a given location.|
|teleport name|2|`.teleport name [#playername] #location`|Teleport the given character to a given location. Character can be offline. To teleport to homebind, set #location to "$home" (without quotes).|
|teleport|1|`.teleport #location`|Teleport player to a given location.|
|ticket assign|2|`.ticket assign $ticketid $gmname`|Assigns the specified ticket to the specified Game Master.|
|ticket close|2|`.ticket close $ticketid`|Closes the specified ticket. Does not delete permanently.|
|ticket closedlist|2||Displays a list of closed GM tickets.|
|ticket comment|2|`.ticket comment $ticketid $comment`|Allows the adding or modifying of a comment to the specified ticket.|
|ticket delete|3|`.ticket delete $ticketid`|Deletes the specified ticket permanently. Ticket must be closed first.|
|ticket escalate|2|`.ticket escalate $ticketid`|Place the specified ticket in the escalation queue.|
|ticket escalatedlist|2||Show all tickets in the escalation queue.|
|ticket list|2||Displays a list of open GM tickets.|
|ticket onlinelist|2||Displays a list of open GM tickets whose owner is online.|
|ticket reset|2|`.ticket reset`|Removes all closed tickets and resets the counter, if no pending open tickets are existing.|
|ticket response append|2|`.ticket response append $ticketid $response`|Append response to the specified ticket (without newline).|
|ticket response appendln|2|`.ticket response appendln $ticketid $response`|Append response to the specified ticket (with newline).|
|ticket togglesystem|4|`.ticket togglesystem`|Toggle ticket system on/off.|
|ticket unassign|2|`.ticket unassign $ticketid`|Unassigns the specified ticket from the current assigned Game Master.|
|ticket viewid|2|`.ticket viewid $ticketid`|Returns details about specified ticket. Ticket must be open and not deleted.|
|ticket viewname|2|`.ticket viewname $creatorname`|Returns details about specified ticket. Ticket must be open and not deleted.|
|ticket|2|`.ticket $subcommand`|Type .ticket to see the list of possible subcommands or .help ticket $subcommand to see info on subcommands|
|titles add|2|`.titles add #title`|Add title #title (id or shift-link) to known titles list for selected player.|
|titles current|2|`.titles current #title`|Set title #title (id or shift-link) as current selected titl for selected player. If title not in known title list for player then it will be added to list.|
|titles remove|2|`.titles remove #title`|Remove title #title (id or shift-link) from known titles list for selected player.|
|titles set mask|2|`.titles set mask #mask`|Allows user to use all titles from #mask. #mask=0 disables the title-choose-field|
|unaura|2|`.unaura #spellid`|Remove aura due to spell #spellid from the selected Unit.|
|unban account|2|`.unban account $Name`|Unban accounts for account name pattern.|
|unban character|2|`.unban character $Name`|Unban accounts for character name pattern.|
|unban ip|2|`.unban ip $Ip`|Unban accounts for IP pattern.|
|unban|2|`.unban $subcommand`|Type .unban to see the list of possible subcommands or .help unban $subcommand to see info on subcommands|
|unbindsight|3|`.unbindsight`|Removes bound vision. Cannot be used while currently possessing a target.|
|unfreeze|2|`.unfreeze (#player)`|"Unfreezes" #player and enables his chat again. When using this without #name it will unfreeze your target.|
|unlearn|2|`.unlearn #spell [all]`|Unlearn for selected player a spell #spell. If 'all' provided then all ranks unlearned.|
|unmute|2|`.unmute [$playerName]`|Restore chat messaging for any character from account of character $playerName (or selected). Character can be ofline.|
|unpossess|2|`.unpossess`|If you are possessed, unpossesses yourself; otherwise unpossesses current possessed target.|
|unstuck|2|`.unstuck $playername [inn/graveyard/startzone]`|Teleports specified player to specified location. Default location is player's current hearth location.|
|wchange|3|`.wchange #weathertype #status`|Set current weather to #weathertype with an intensity of #status. #weathertype can be 1 for rain, 2 for snow, and 3 for sand. #status can be 0 for disabled, and 1 for enabled.|
|whispers|1|`.whispers on\off`|Enable/disable accepting whispers by GM from players. By default use worldserver.conf setting.|
|wp add|3|`.wp add`|Add a waypoint for the selected creature at your current position.|
|wp event|3|`.wp event $subcommand`|Type .path event to see the list of possible subcommands or .help path event $subcommand to see info on subcommands.|
|wp load|3|`.wp load $pathid`|Load pathid number for selected creature. Creature must have no waypoint data.|
|wp modify|3|`.wp modify $optionOptions:action`|Changes the value actionaction_chance Changes the value action_chancedel Deletes a selected waypointdelay Changes the value delaymove Moves a selected waypointmove_flag Changes the value move_flag|
|wp reload|3|`.wp reload $pathid`|Load path changes ingame - IMPORTANT: must be applied first for new paths before .wp load #pathid|
|wp show|3|`.wp show $optionOptions:on $pathid (or selected creature with loaded path)`|Show visual waypoints (Note: You must have GM on to see the waypoints)off Hide the visual waypoints.info Shows info for selected waypoint.first Shows visual the first waypoint.last Shows visual the last waypoint.|
|wp unload|3|`.wp unload`|Unload path for selected creature.|
|wpgps|4|`.wpgps`|Output current position to sql developer log as partial SQL query to be used in pathing|
