# rbac\_permissions

[<-Back-to:Auth](database-auth)

**The \`rbac\_permissions\` table**

This table defines all available RBAC permissions. Each permission represents a single capability — a gameplay privilege, a command, or a role that bundles other permissions together.

For a system overview, see [RBAC](rbac).

**Table: rbac\_permissions's Structure**

| Field         | Type         |          | Null | Key | Default | Extra | Comment         |
| :------------ | :----------- | :------- | :--: | :-: | :-----: | :---: | :-------------- |
| [id](#id)     | INT          | UNSIGNED | NO   | PRI | 0       |       | Permission id   |
| [name](#name) | VARCHAR(100) |          | NO   |     |         |       | Permission name |

**Description of the table's fields**

### id

The unique permission identifier. ID ranges are:

| Range | Purpose |
| ----- | ------- |
| 1–53 | Gameplay permissions (instant logout, skip queue, join BG, etc.) |
| 192–195 | Security-level roles (Administrator, Gamemaster, Moderator, Player) |
| 196–199 | Command roles (Admin Commands, GM Commands, Mod Commands, Player Commands) |
| 200 and above | Individual command permissions (one per `.command`) |

### name

A human-readable name describing the permission. Follows conventions:

- Gameplay permissions: descriptive name (e.g. `Instant logout`, `Skip Queue`)
- Roles: prefixed with `Role:` (e.g. `Role: Sec Level Administrator`)
- Commands: prefixed with `Command:` (e.g. `Command: rbac account list`)

<!-- rbac-default-data:start -->

**Default permissions**

These are the permissions a clean AzerothCore database comes with. *Constant* is the name the core uses for the permission in [RBAC.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Accounts/RBAC.h). *Granted by* is the role that includes the permission in [rbac_linked_permissions](rbac_linked_permissions); a permission with no role is not given to anyone by default.

<button type="button" class="details-toggle" onclick="var d=document.querySelectorAll('#git-wiki-content details'),o=!Array.prototype.every.call(d,function(e){return e.open});d.forEach(function(e){e.open=o});this.textContent=o?'Collapse all':'Expand all'">Expand all</button>

<details>
<summary>Gameplay permissions (ID 1 to 53)</summary>

| ID  | Name                                                           | Constant                                               | Granted by          |
| :-- | :------------------------------------------------------------- | :----------------------------------------------------- | :------------------ |
| 1   | Instant logout                                                 | `RBAC_PERM_INSTANT_LOGOUT`                             | 194 (Moderator)     |
| 2   | Skip Queue                                                     | `RBAC_PERM_SKIP_QUEUE`                                 | 194 (Moderator)     |
| 3   | Join Normal Battleground                                       | `RBAC_PERM_JOIN_NORMAL_BG`                             | 195 (Player)        |
| 4   | Join Random Battleground                                       | `RBAC_PERM_JOIN_RANDOM_BG`                             | 195 (Player)        |
| 5   | Join Arenas                                                    | `RBAC_PERM_JOIN_ARENAS`                                | 195 (Player)        |
| 6   | Join Dungeon Finder                                            | `RBAC_PERM_JOIN_DUNGEON_FINDER`                        | 195 (Player)        |
| 7   | Skip idle connection check                                     | `RBAC_PERM_IGNORE_IDLE_CONNECTION`                     | 192 (Administrator) |
| 8   | Cannot earn achievements                                       | `RBAC_PERM_CANNOT_EARN_ACHIEVEMENTS`                   |                     |
| 9   | Cannot earn realm first achievements                           | `RBAC_PERM_CANNOT_EARN_REALM_FIRST_ACHIEVEMENTS`       | 194 (Moderator)     |
| 11  | Log GM trades                                                  | `RBAC_PERM_LOG_GM_TRADE`                               | 194 (Moderator)     |
| 13  | Skip Instance required bosses check                            | `RBAC_PERM_SKIP_CHECK_INSTANCE_REQUIRED_BOSSES`        | 194 (Moderator)     |
| 14  | Skip character creation team mask check                        | `RBAC_PERM_SKIP_CHECK_CHARACTER_CREATION_TEAMMASK`     | 194 (Moderator)     |
| 15  | Skip character creation class mask check                       | `RBAC_PERM_SKIP_CHECK_CHARACTER_CREATION_CLASSMASK`    | 194 (Moderator)     |
| 16  | Skip character creation race mask check                        | `RBAC_PERM_SKIP_CHECK_CHARACTER_CREATION_RACEMASK`     | 194 (Moderator)     |
| 17  | Skip character creation reserved name check                    | `RBAC_PERM_SKIP_CHECK_CHARACTER_CREATION_RESERVEDNAME` | 194 (Moderator)     |
| 18  | Skip character creation death knight min level check           | `RBAC_PERM_SKIP_CHECK_CHARACTER_CREATION_DEATH_KNIGHT` | 194 (Moderator)     |
| 19  | Skip needed requirements to use channel check                  | `RBAC_PERM_SKIP_CHECK_CHAT_CHANNEL_REQ`                | 194 (Moderator)     |
| 20  | Skip disable map check                                         | `RBAC_PERM_SKIP_CHECK_DISABLE_MAP`                     | 194 (Moderator)     |
| 21  | Skip reset talents when used more than allowed check           | `RBAC_PERM_SKIP_CHECK_MORE_TALENTS_THAN_ALLOWED`       | 192 (Administrator) |
| 22  | Skip spam chat check                                           | `RBAC_PERM_SKIP_CHECK_CHAT_SPAM`                       | 194 (Moderator)     |
| 23  | Skip over-speed ping check                                     | `RBAC_PERM_SKIP_CHECK_OVERSPEED_PING`                  | 194 (Moderator)     |
| 24  | Two side faction characters on the same account                | `RBAC_PERM_TWO_SIDE_CHARACTER_CREATION`                | 195 (Player)        |
| 25  | Allow say chat between factions                                | `RBAC_PERM_TWO_SIDE_INTERACTION_CHAT`                  | 194 (Moderator)     |
| 26  | Allow channel chat between factions                            | `RBAC_PERM_TWO_SIDE_INTERACTION_CHANNEL`               | 194 (Moderator)     |
| 27  | Two side mail interaction                                      | `RBAC_PERM_TWO_SIDE_INTERACTION_MAIL`                  | 194 (Moderator)     |
| 28  | See two side who list                                          | `RBAC_PERM_TWO_SIDE_WHO_LIST`                          | 194 (Moderator)     |
| 29  | Add friends of other faction                                   | `RBAC_PERM_TWO_SIDE_ADD_FRIEND`                        | 194 (Moderator)     |
| 30  | Save character without delay with .save command                | `RBAC_PERM_COMMANDS_SAVE_WITHOUT_DELAY`                | 194 (Moderator)     |
| 31  | Use params with .unstuck command                               | `RBAC_PERM_COMMANDS_USE_UNSTUCK_WITH_ARGS`             | 194 (Moderator)     |
| 32  | Can be assigned tickets with .assign ticket command            | `RBAC_PERM_COMMANDS_BE_ASSIGNED_TICKET`                | 194 (Moderator)     |
| 33  | Notify if a command was not found                              | `RBAC_PERM_COMMANDS_NOTIFY_COMMAND_NOT_FOUND_ERROR`    | 194 (Moderator)     |
| 34  | Check if should appear in list using .gm ingame command        | `RBAC_PERM_COMMANDS_APPEAR_IN_GM_LIST`                 | 194 (Moderator)     |
| 35  | See all security levels with who command                       | `RBAC_PERM_WHO_SEE_ALL_SEC_LEVELS`                     | 194 (Moderator)     |
| 36  | Filter whispers                                                | `RBAC_PERM_CAN_FILTER_WHISPERS`                        | 194 (Moderator)     |
| 37  | Use staff badge in chat                                        | `RBAC_PERM_CHAT_USE_STAFF_BADGE`                       | 194 (Moderator)     |
| 38  | Resurrect with full Health Points                              | `RBAC_PERM_RESURRECT_WITH_FULL_HPS`                    | 194 (Moderator)     |
| 39  | Restore saved gm setting states                                | `RBAC_PERM_RESTORE_SAVED_GM_STATE`                     | 194 (Moderator)     |
| 40  | Allows to add a gm to friend list                              | `RBAC_PERM_ALLOW_GM_FRIEND`                            | 194 (Moderator)     |
| 41  | Use Config option START_GM_LEVEL to assign new character level | `RBAC_PERM_USE_START_GM_LEVEL`                         | 194 (Moderator)     |
| 42  | Allows to use CMSG_WORLD_TELEPORT opcode                       | `RBAC_PERM_OPCODE_WORLD_TELEPORT`                      | 192 (Administrator) |
| 43  | Allows to use CMSG_WHOIS opcode                                | `RBAC_PERM_OPCODE_WHOIS`                               | 192 (Administrator) |
| 44  | Receive global GM messages/texts                               | `RBAC_PERM_RECEIVE_GLOBAL_GM_TEXTMESSAGE`              | 194 (Moderator)     |
| 45  | Join channels without announce                                 | `RBAC_PERM_SILENTLY_JOIN_CHANNEL`                      | 193 (Gamemaster)    |
| 46  | Change channel settings without being channel moderator        | `RBAC_PERM_CHANGE_CHANNEL_NOT_MODERATOR`               | 194 (Moderator)     |
| 47  | Can ignore lower security checks                               | `RBAC_PERM_CAN_IGNORE_LOWER_SECURITY_CHECK`            | 194 (Moderator)     |
| 48  | Enable IP, Last Login and EMail output in pinfo                | `RBAC_PERM_COMMANDS_PINFO_CHECK_PERSONAL_DATA`         | 193 (Gamemaster)    |
| 49  | Forces to enter the email for confirmation on password change  | `RBAC_PERM_EMAIL_CONFIRM_FOR_PASS_CHANGE`              | 195 (Player)        |
| 50  | Allow user to check his own email with .account                | `RBAC_PERM_MAY_CHECK_OWN_EMAIL`                        |                     |
| 51  | Allow trading between factions                                 | `RBAC_PERM_ALLOW_TWO_SIDE_TRADE`                       | 194 (Moderator)     |
| 52  | No battleground deserter debuff                                | `RBAC_PERM_NO_BATTLEGROUND_DESERTER_DEBUFF`            | 193 (Gamemaster)    |
| 53  | Can be AFK on the battleground                                 | `RBAC_PERM_CAN_AFK_ON_BATTLEGROUND`                    | 193 (Gamemaster)    |

</details>

<details>
<summary>Roles (ID 192 to 199)</summary>

| ID  | Name                          | Constant                  | Granted by          |
| :-- | :---------------------------- | :------------------------ | :------------------ |
| 192 | Role: Sec Level Administrator |                           |                     |
| 193 | Role: Sec Level Gamemaster    |                           | 192 (Administrator) |
| 194 | Role: Sec Level Moderator     |                           | 193 (Gamemaster)    |
| 195 | Role: Sec Level Player        |                           | 194 (Moderator)     |
| 196 | Role: Administrator Commands  | `RBAC_ROLE_ADMINISTRATOR` | 192 (Administrator) |
| 197 | Role: Gamemaster Commands     | `RBAC_ROLE_GAMEMASTER`    | 193 (Gamemaster)    |
| 198 | Role: Moderator Commands      | `RBAC_ROLE_MODERATOR`     | 194 (Moderator)     |
| 199 | Role: Player Commands         | `RBAC_ROLE_PLAYER`        | 195 (Player)        |

</details>

<details>
<summary>Command permissions (ID 200 to 945)</summary>

| ID  | Name                                           | Constant                                                  | Granted by                                 |
| :-- | :--------------------------------------------- | :-------------------------------------------------------- | :----------------------------------------- |
| 200 | Command: rbac                                  | `RBAC_PERM_COMMAND_RBAC`                                  | 196 (Administrator Commands)               |
| 201 | Command: rbac account                          | `RBAC_PERM_COMMAND_RBAC_ACC`                              | 196 (Administrator Commands)               |
| 202 | Command: rbac account list                     | `RBAC_PERM_COMMAND_RBAC_ACC_PERM_LIST`                    | 196 (Administrator Commands)               |
| 203 | Command: rbac account grant                    | `RBAC_PERM_COMMAND_RBAC_ACC_PERM_GRANT`                   | 196 (Administrator Commands)               |
| 204 | Command: rbac account deny                     | `RBAC_PERM_COMMAND_RBAC_ACC_PERM_DENY`                    | 196 (Administrator Commands)               |
| 205 | Command: rbac account revoke                   | `RBAC_PERM_COMMAND_RBAC_ACC_PERM_REVOKE`                  | 196 (Administrator Commands)               |
| 206 | Command: rbac list                             | `RBAC_PERM_COMMAND_RBAC_LIST`                             | 196 (Administrator Commands)               |
| 217 | Command: account                               | `RBAC_PERM_COMMAND_ACCOUNT`                               | 199 (Player Commands)                      |
| 218 | Command: account addon                         | `RBAC_PERM_COMMAND_ACCOUNT_ADDON`                         | 199 (Player Commands)                      |
| 219 | Command: account create                        | `RBAC_PERM_COMMAND_ACCOUNT_CREATE`                        | 196 (Administrator Commands)               |
| 220 | Command: account delete                        | `RBAC_PERM_COMMAND_ACCOUNT_DELETE`                        | 196 (Administrator Commands)               |
| 221 | Command: account lock                          | `RBAC_PERM_COMMAND_ACCOUNT_LOCK`                          | 199 (Player Commands)                      |
| 222 | Command: account lock country                  | `RBAC_PERM_COMMAND_ACCOUNT_LOCK_COUNTRY`                  | 199 (Player Commands)                      |
| 223 | Command: account lock ip                       | `RBAC_PERM_COMMAND_ACCOUNT_LOCK_IP`                       | 199 (Player Commands)                      |
| 224 | Command: account onlinelist                    | `RBAC_PERM_COMMAND_ACCOUNT_ONLINE_LIST`                   | 196 (Administrator Commands)               |
| 225 | Command: account password                      | `RBAC_PERM_COMMAND_ACCOUNT_PASSWORD`                      | 199 (Player Commands)                      |
| 226 | Command: account set                           | `RBAC_PERM_COMMAND_ACCOUNT_SET`                           | 196 (Administrator Commands)               |
| 227 | Command: account set addon                     | `RBAC_PERM_COMMAND_ACCOUNT_SET_ADDON`                     | 196 (Administrator Commands)               |
| 228 | Command: account set gmlevel                   | `RBAC_PERM_COMMAND_ACCOUNT_SET_SECLEVEL`                  | 196 (Administrator Commands)               |
| 229 | Command: account set password                  | `RBAC_PERM_COMMAND_ACCOUNT_SET_PASSWORD`                  | 196 (Administrator Commands)               |
| 231 | Command: achievement add                       | `RBAC_PERM_COMMAND_ACHIEVEMENT_ADD`                       | 197 (Gamemaster Commands)                  |
| 232 | Command: achievement checkall                  | `RBAC_PERM_COMMAND_ACHIEVEMENT_CHECKALL`                  | 197 (Gamemaster Commands)                  |
| 233 | Command: arena captain                         | `RBAC_PERM_COMMAND_ARENA_CAPTAIN`                         | 197 (Gamemaster Commands)                  |
| 234 | Command: arena create                          | `RBAC_PERM_COMMAND_ARENA_CREATE`                          | 197 (Gamemaster Commands)                  |
| 235 | Command: arena disband                         | `RBAC_PERM_COMMAND_ARENA_DISBAND`                         | 197 (Gamemaster Commands)                  |
| 236 | Command: arena info                            | `RBAC_PERM_COMMAND_ARENA_INFO`                            | 197 (Gamemaster Commands)                  |
| 237 | Command: arena lookup                          | `RBAC_PERM_COMMAND_ARENA_LOOKUP`                          | 197 (Gamemaster Commands)                  |
| 238 | Command: arena rename                          | `RBAC_PERM_COMMAND_ARENA_RENAME`                          | 197 (Gamemaster Commands)                  |
| 240 | Command: ban account                           | `RBAC_PERM_COMMAND_BAN_ACCOUNT`                           | 198 (Moderator Commands)                   |
| 241 | Command: ban character                         | `RBAC_PERM_COMMAND_BAN_CHARACTER`                         | 198 (Moderator Commands)                   |
| 242 | Command: ban ip                                | `RBAC_PERM_COMMAND_BAN_IP`                                | 198 (Moderator Commands)                   |
| 243 | Command: ban playeraccount                     | `RBAC_PERM_COMMAND_BAN_PLAYERACCOUNT`                     | 198 (Moderator Commands)                   |
| 245 | Command: baninfo account                       | `RBAC_PERM_COMMAND_BANINFO_ACCOUNT`                       | 198 (Moderator Commands)                   |
| 246 | Command: baninfo character                     | `RBAC_PERM_COMMAND_BANINFO_CHARACTER`                     | 198 (Moderator Commands)                   |
| 247 | Command: baninfo ip                            | `RBAC_PERM_COMMAND_BANINFO_IP`                            | 198 (Moderator Commands)                   |
| 249 | Command: banlist account                       | `RBAC_PERM_COMMAND_BANLIST_ACCOUNT`                       | 198 (Moderator Commands)                   |
| 250 | Command: banlist character                     | `RBAC_PERM_COMMAND_BANLIST_CHARACTER`                     | 198 (Moderator Commands)                   |
| 251 | Command: banlist ip                            | `RBAC_PERM_COMMAND_BANLIST_IP`                            | 198 (Moderator Commands)                   |
| 253 | Command: unban account                         | `RBAC_PERM_COMMAND_UNBAN_ACCOUNT`                         | 198 (Moderator Commands)                   |
| 254 | Command: unban character                       | `RBAC_PERM_COMMAND_UNBAN_CHARACTER`                       | 198 (Moderator Commands)                   |
| 255 | Command: unban ip                              | `RBAC_PERM_COMMAND_UNBAN_IP`                              | 198 (Moderator Commands)                   |
| 256 | Command: unban playeraccount                   | `RBAC_PERM_COMMAND_UNBAN_PLAYERACCOUNT`                   | 198 (Moderator Commands)                   |
| 258 | Command: bf start                              | `RBAC_PERM_COMMAND_BF_START`                              | 196 (Administrator Commands)               |
| 259 | Command: bf stop                               | `RBAC_PERM_COMMAND_BF_STOP`                               | 196 (Administrator Commands)               |
| 260 | Command: bf switch                             | `RBAC_PERM_COMMAND_BF_SWITCH`                             | 196 (Administrator Commands)               |
| 261 | Command: bf timer                              | `RBAC_PERM_COMMAND_BF_TIMER`                              | 196 (Administrator Commands)               |
| 262 | Command: bf enable                             | `RBAC_PERM_COMMAND_BF_ENABLE`                             | 196 (Administrator Commands)               |
| 263 | Command: account email                         | `RBAC_PERM_COMMAND_ACCOUNT_EMAIL`                         | 199 (Player Commands)                      |
| 265 | Command: account set sec email                 | `RBAC_PERM_COMMAND_ACCOUNT_SET_SEC_EMAIL`                 | 196 (Administrator Commands)               |
| 266 | Command: account set sec regmail               | `RBAC_PERM_COMMAND_ACCOUNT_SET_SEC_REGMAIL`               | 196 (Administrator Commands)               |
| 267 | Command: cast                                  | `RBAC_PERM_COMMAND_CAST`                                  | 197 (Gamemaster Commands)                  |
| 268 | Command: cast back                             | `RBAC_PERM_COMMAND_CAST_BACK`                             | 197 (Gamemaster Commands)                  |
| 269 | Command: cast dist                             | `RBAC_PERM_COMMAND_CAST_DIST`                             | 197 (Gamemaster Commands)                  |
| 270 | Command: cast self                             | `RBAC_PERM_COMMAND_CAST_SELF`                             | 197 (Gamemaster Commands)                  |
| 271 | Command: cast target                           | `RBAC_PERM_COMMAND_CAST_TARGET`                           | 197 (Gamemaster Commands)                  |
| 272 | Command: cast dest                             | `RBAC_PERM_COMMAND_CAST_DEST`                             | 197 (Gamemaster Commands)                  |
| 274 | Command: character customize                   | `RBAC_PERM_COMMAND_CHARACTER_CUSTOMIZE`                   | 197 (Gamemaster Commands)                  |
| 275 | Command: character changefaction               | `RBAC_PERM_COMMAND_CHARACTER_CHANGEFACTION`               | 197 (Gamemaster Commands)                  |
| 276 | Command: character changerace                  | `RBAC_PERM_COMMAND_CHARACTER_CHANGERACE`                  | 197 (Gamemaster Commands)                  |
| 278 | Command: character deleted delete              | `RBAC_PERM_COMMAND_CHARACTER_DELETED_DELETE`              | 196 (Administrator Commands)               |
| 279 | Command: character deleted list                | `RBAC_PERM_COMMAND_CHARACTER_DELETED_LIST`                | 197 (Gamemaster Commands)                  |
| 280 | Command: character deleted restore             | `RBAC_PERM_COMMAND_CHARACTER_DELETED_RESTORE`             | 197 (Gamemaster Commands)                  |
| 281 | Command: character deleted old                 | `RBAC_PERM_COMMAND_CHARACTER_DELETED_OLD`                 | 196 (Administrator Commands)               |
| 282 | Command: character erase                       | `RBAC_PERM_COMMAND_CHARACTER_ERASE`                       | 196 (Administrator Commands)               |
| 283 | Command: character level                       | `RBAC_PERM_COMMAND_CHARACTER_LEVEL`                       | 197 (Gamemaster Commands)                  |
| 284 | Command: character rename                      | `RBAC_PERM_COMMAND_CHARACTER_RENAME`                      | 197 (Gamemaster Commands)                  |
| 285 | Command: character reputation                  | `RBAC_PERM_COMMAND_CHARACTER_REPUTATION`                  | 197 (Gamemaster Commands)                  |
| 286 | Command: character titles                      | `RBAC_PERM_COMMAND_CHARACTER_TITLES`                      | 197 (Gamemaster Commands)                  |
| 287 | Command: levelup                               | `RBAC_PERM_COMMAND_LEVELUP`                               | 197 (Gamemaster Commands)                  |
| 289 | Command: pdump load                            | `RBAC_PERM_COMMAND_PDUMP_LOAD`                            | 196 (Administrator Commands)               |
| 290 | Command: pdump write                           | `RBAC_PERM_COMMAND_PDUMP_WRITE`                           | 196 (Administrator Commands)               |
| 292 | Command: cheat casttime                        | `RBAC_PERM_COMMAND_CHEAT_CASTTIME`                        | 197 (Gamemaster Commands)                  |
| 293 | Command: cheat cooldown                        | `RBAC_PERM_COMMAND_CHEAT_COOLDOWN`                        | 197 (Gamemaster Commands)                  |
| 294 | Command: cheat explore                         | `RBAC_PERM_COMMAND_CHEAT_EXPLORE`                         | 197 (Gamemaster Commands)                  |
| 295 | Command: cheat god                             | `RBAC_PERM_COMMAND_CHEAT_GOD`                             | 197 (Gamemaster Commands)                  |
| 296 | Command: cheat power                           | `RBAC_PERM_COMMAND_CHEAT_POWER`                           | 197 (Gamemaster Commands)                  |
| 297 | Command: cheat status                          | `RBAC_PERM_COMMAND_CHEAT_STATUS`                          | 197 (Gamemaster Commands)                  |
| 298 | Command: cheat taxi                            | `RBAC_PERM_COMMAND_CHEAT_TAXI`                            | 197 (Gamemaster Commands)                  |
| 299 | Command: cheat waterwalk                       | `RBAC_PERM_COMMAND_CHEAT_WATERWALK`                       | 197 (Gamemaster Commands)                  |
| 300 | Command: debug                                 | `RBAC_PERM_COMMAND_DEBUG`                                 | 197 (Gamemaster Commands)                  |
| 343 | Command: deserter bg add                       | `RBAC_PERM_COMMAND_DESERTER_BG_ADD`                       | 197 (Gamemaster Commands)                  |
| 344 | Command: deserter bg remove                    | `RBAC_PERM_COMMAND_DESERTER_BG_REMOVE`                    | 197 (Gamemaster Commands)                  |
| 346 | Command: deserter instance add                 | `RBAC_PERM_COMMAND_DESERTER_INSTANCE_ADD`                 | 197 (Gamemaster Commands)                  |
| 347 | Command: deserter instance remove              | `RBAC_PERM_COMMAND_DESERTER_INSTANCE_REMOVE`              | 197 (Gamemaster Commands)                  |
| 350 | Command: disable add achievement_criteria      | `RBAC_PERM_COMMAND_DISABLE_ADD_ACHIEVEMENT_CRITERIA`      | 196 (Administrator Commands)               |
| 351 | Command: disable add battleground              | `RBAC_PERM_COMMAND_DISABLE_ADD_BATTLEGROUND`              | 196 (Administrator Commands)               |
| 352 | Command: disable add map                       | `RBAC_PERM_COMMAND_DISABLE_ADD_MAP`                       | 196 (Administrator Commands)               |
| 353 | Command: disable add mmap                      | `RBAC_PERM_COMMAND_DISABLE_ADD_MMAP`                      | 196 (Administrator Commands)               |
| 354 | Command: disable add outdoorpvp                | `RBAC_PERM_COMMAND_DISABLE_ADD_OUTDOORPVP`                | 196 (Administrator Commands)               |
| 355 | Command: disable add quest                     | `RBAC_PERM_COMMAND_DISABLE_ADD_QUEST`                     | 196 (Administrator Commands)               |
| 356 | Command: disable add spell                     | `RBAC_PERM_COMMAND_DISABLE_ADD_SPELL`                     | 196 (Administrator Commands)               |
| 357 | Command: disable add vmap                      | `RBAC_PERM_COMMAND_DISABLE_ADD_VMAP`                      | 196 (Administrator Commands)               |
| 359 | Command: disable remove achievement_criteria   | `RBAC_PERM_COMMAND_DISABLE_REMOVE_ACHIEVEMENT_CRITERIA`   | 196 (Administrator Commands)               |
| 360 | Command: disable remove battleground           | `RBAC_PERM_COMMAND_DISABLE_REMOVE_BATTLEGROUND`           | 196 (Administrator Commands)               |
| 361 | Command: disable remove map                    | `RBAC_PERM_COMMAND_DISABLE_REMOVE_MAP`                    | 196 (Administrator Commands)               |
| 362 | Command: disable remove mmap                   | `RBAC_PERM_COMMAND_DISABLE_REMOVE_MMAP`                   | 196 (Administrator Commands)               |
| 363 | Command: disable remove outdoorpvp             | `RBAC_PERM_COMMAND_DISABLE_REMOVE_OUTDOORPVP`             | 196 (Administrator Commands)               |
| 364 | Command: disable remove quest                  | `RBAC_PERM_COMMAND_DISABLE_REMOVE_QUEST`                  | 196 (Administrator Commands)               |
| 365 | Command: disable remove spell                  | `RBAC_PERM_COMMAND_DISABLE_REMOVE_SPELL`                  | 196 (Administrator Commands)               |
| 366 | Command: disable remove vmap                   | `RBAC_PERM_COMMAND_DISABLE_REMOVE_VMAP`                   | 196 (Administrator Commands)               |
| 367 | Command: event info                            | `RBAC_PERM_COMMAND_EVENT_INFO`                            | 197 (Gamemaster Commands)                  |
| 368 | Command: event activelist                      | `RBAC_PERM_COMMAND_EVENT_ACTIVELIST`                      | 197 (Gamemaster Commands)                  |
| 369 | Command: event start                           | `RBAC_PERM_COMMAND_EVENT_START`                           | 197 (Gamemaster Commands)                  |
| 370 | Command: event stop                            | `RBAC_PERM_COMMAND_EVENT_STOP`                            | 197 (Gamemaster Commands)                  |
| 371 | Command: gm                                    | `RBAC_PERM_COMMAND_GM`                                    | 197 (Gamemaster Commands)                  |
| 372 | Command: gm chat                               | `RBAC_PERM_COMMAND_GM_CHAT`                               | 197 (Gamemaster Commands)                  |
| 373 | Command: gm fly                                | `RBAC_PERM_COMMAND_GM_FLY`                                | 197 (Gamemaster Commands)                  |
| 374 | Command: gm ingame                             | `RBAC_PERM_COMMAND_GM_INGAME`                             | 199 (Player Commands)                      |
| 375 | Command: gm list                               | `RBAC_PERM_COMMAND_GM_LIST`                               | 199 (Player Commands)                      |
| 376 | Command: gm visible                            | `RBAC_PERM_COMMAND_GM_VISIBLE`                            | 197 (Gamemaster Commands)                  |
| 377 | Command: go                                    | `RBAC_PERM_COMMAND_GO`                                    | 197 (Gamemaster Commands)                  |
| 388 | Command: gobject activate                      | `RBAC_PERM_COMMAND_GOBJECT_ACTIVATE`                      | 197 (Gamemaster Commands)                  |
| 389 | Command: gobject add                           | `RBAC_PERM_COMMAND_GOBJECT_ADD`                           | 197 (Gamemaster Commands)                  |
| 390 | Command: gobject add temp                      | `RBAC_PERM_COMMAND_GOBJECT_ADD_TEMP`                      | 197 (Gamemaster Commands)                  |
| 391 | Command: gobject delete                        | `RBAC_PERM_COMMAND_GOBJECT_DELETE`                        | 197 (Gamemaster Commands)                  |
| 392 | Command: gobject info                          | `RBAC_PERM_COMMAND_GOBJECT_INFO`                          | 197 (Gamemaster Commands)                  |
| 393 | Command: gobject move                          | `RBAC_PERM_COMMAND_GOBJECT_MOVE`                          | 197 (Gamemaster Commands)                  |
| 394 | Command: gobject near                          | `RBAC_PERM_COMMAND_GOBJECT_NEAR`                          | 197 (Gamemaster Commands)                  |
| 396 | Command: gobject set phase                     | `RBAC_PERM_COMMAND_GOBJECT_SET_PHASE`                     | 197 (Gamemaster Commands)                  |
| 397 | Command: gobject set state                     | `RBAC_PERM_COMMAND_GOBJECT_SET_STATE`                     | 197 (Gamemaster Commands)                  |
| 398 | Command: gobject target                        | `RBAC_PERM_COMMAND_GOBJECT_TARGET`                        | 197 (Gamemaster Commands)                  |
| 399 | Command: gobject turn                          | `RBAC_PERM_COMMAND_GOBJECT_TURN`                          | 197 (Gamemaster Commands)                  |
| 401 | Command: guild                                 | `RBAC_PERM_COMMAND_GUILD`                                 | 197 (Gamemaster Commands)                  |
| 402 | Command: guild create                          | `RBAC_PERM_COMMAND_GUILD_CREATE`                          | 197 (Gamemaster Commands)                  |
| 403 | Command: guild delete                          | `RBAC_PERM_COMMAND_GUILD_DELETE`                          | 197 (Gamemaster Commands)                  |
| 404 | Command: guild invite                          | `RBAC_PERM_COMMAND_GUILD_INVITE`                          | 197 (Gamemaster Commands)                  |
| 405 | Command: guild uninvite                        | `RBAC_PERM_COMMAND_GUILD_UNINVITE`                        | 197 (Gamemaster Commands)                  |
| 406 | Command: guild rank                            | `RBAC_PERM_COMMAND_GUILD_RANK`                            | 197 (Gamemaster Commands)                  |
| 407 | Command: guild rename                          | `RBAC_PERM_COMMAND_GUILD_RENAME`                          | 197 (Gamemaster Commands)                  |
| 409 | Command: honor add                             | `RBAC_PERM_COMMAND_HONOR_ADD`                             | 197 (Gamemaster Commands)                  |
| 410 | Command: honor add kill                        | `RBAC_PERM_COMMAND_HONOR_ADD_KILL`                        | 197 (Gamemaster Commands)                  |
| 411 | Command: honor update                          | `RBAC_PERM_COMMAND_HONOR_UPDATE`                          | 197 (Gamemaster Commands)                  |
| 413 | Command: instance listbinds                    | `RBAC_PERM_COMMAND_INSTANCE_LISTBINDS`                    | 197 (Gamemaster Commands)                  |
| 414 | Command: instance unbind                       | `RBAC_PERM_COMMAND_INSTANCE_UNBIND`                       | 197 (Gamemaster Commands)                  |
| 415 | Command: instance stats                        | `RBAC_PERM_COMMAND_INSTANCE_STATS`                        | 197 (Gamemaster Commands)                  |
| 416 | Command: instance savedata                     | `RBAC_PERM_COMMAND_INSTANCE_SAVEDATA`                     | 197 (Gamemaster Commands)                  |
| 417 | Command: learn                                 | `RBAC_PERM_COMMAND_LEARN`                                 | 197 (Gamemaster Commands)                  |
| 419 | Command: learn all my                          | `RBAC_PERM_COMMAND_LEARN_ALL_MY`                          | 197 (Gamemaster Commands)                  |
| 420 | Command: learn all my class                    | `RBAC_PERM_COMMAND_LEARN_ALL_MY_CLASS`                    | 197 (Gamemaster Commands)                  |
| 421 | Command: learn my pettalents                   | `RBAC_PERM_COMMAND_LEARN_MY_PETTALENTS`                   | 197 (Gamemaster Commands)                  |
| 422 | Command: learn all my spells                   | `RBAC_PERM_COMMAND_LEARN_ALL_MY_SPELLS`                   | 197 (Gamemaster Commands)                  |
| 423 | Command: learn all talents                     | `RBAC_PERM_COMMAND_LEARN_ALL_TALENTS`                     | 197 (Gamemaster Commands)                  |
| 424 | Command: learn all gm                          | `RBAC_PERM_COMMAND_LEARN_ALL_GM`                          | 197 (Gamemaster Commands)                  |
| 425 | Command: learn all crafts                      | `RBAC_PERM_COMMAND_LEARN_ALL_CRAFTS`                      | 197 (Gamemaster Commands)                  |
| 426 | Command: learn all default                     | `RBAC_PERM_COMMAND_LEARN_ALL_DEFAULT`                     | 197 (Gamemaster Commands)                  |
| 427 | Command: learn all lang                        | `RBAC_PERM_COMMAND_LEARN_ALL_LANG`                        | 197 (Gamemaster Commands)                  |
| 428 | Command: learn all recipes                     | `RBAC_PERM_COMMAND_LEARN_ALL_RECIPES`                     | 197 (Gamemaster Commands)                  |
| 429 | Command: unlearn                               | `RBAC_PERM_COMMAND_UNLEARN`                               | 197 (Gamemaster Commands)                  |
| 431 | Command: lfg player                            | `RBAC_PERM_COMMAND_LFG_PLAYER`                            | 197 (Gamemaster Commands)                  |
| 432 | Command: lfg group                             | `RBAC_PERM_COMMAND_LFG_GROUP`                             | 197 (Gamemaster Commands)                  |
| 433 | Command: lfg queue                             | `RBAC_PERM_COMMAND_LFG_QUEUE`                             | 197 (Gamemaster Commands)                  |
| 434 | Command: lfg clean                             | `RBAC_PERM_COMMAND_LFG_CLEAN`                             | 197 (Gamemaster Commands)                  |
| 435 | Command: lfg options                           | `RBAC_PERM_COMMAND_LFG_OPTIONS`                           | 197 (Gamemaster Commands)                  |
| 436 | Command: lfg cooldown                          | `RBAC_PERM_COMMAND_LFG_COOLDOWN`                          | 197 (Gamemaster Commands)                  |
| 437 | Command: list creature                         | `RBAC_PERM_COMMAND_LIST_CREATURE`                         | 197 (Gamemaster Commands)                  |
| 438 | Command: list item                             | `RBAC_PERM_COMMAND_LIST_ITEM`                             | 197 (Gamemaster Commands)                  |
| 439 | Command: list object                           | `RBAC_PERM_COMMAND_LIST_OBJECT`                           | 197 (Gamemaster Commands)                  |
| 440 | Command: list auras                            | `RBAC_PERM_COMMAND_LIST_AURAS`                            | 197 (Gamemaster Commands)                  |
| 441 | Command: list mail                             | `RBAC_PERM_COMMAND_LIST_MAIL`                             | 197 (Gamemaster Commands)                  |
| 442 | Command: lookup                                | `RBAC_PERM_COMMAND_LOOKUP`                                | 199 (Player Commands)                      |
| 443 | Command: lookup area                           | `RBAC_PERM_COMMAND_LOOKUP_AREA`                           | 199 (Player Commands)                      |
| 444 | Command: lookup creature                       | `RBAC_PERM_COMMAND_LOOKUP_CREATURE`                       | 199 (Player Commands)                      |
| 445 | Command: lookup event                          | `RBAC_PERM_COMMAND_LOOKUP_EVENT`                          | 197 (Gamemaster Commands)                  |
| 446 | Command: lookup faction                        | `RBAC_PERM_COMMAND_LOOKUP_FACTION`                        | 199 (Player Commands)                      |
| 447 | Command: lookup item                           | `RBAC_PERM_COMMAND_LOOKUP_ITEM`                           | 199 (Player Commands)                      |
| 448 | Command: lookup itemset                        | `RBAC_PERM_COMMAND_LOOKUP_ITEMSET`                        | 197 (Gamemaster Commands)                  |
| 449 | Command: lookup object                         | `RBAC_PERM_COMMAND_LOOKUP_OBJECT`                         | 197 (Gamemaster Commands)                  |
| 450 | Command: lookup quest                          | `RBAC_PERM_COMMAND_LOOKUP_QUEST`                          | 199 (Player Commands)                      |
| 451 | Command: lookup player                         | `RBAC_PERM_COMMAND_LOOKUP_PLAYER`                         | 197 (Gamemaster Commands)                  |
| 452 | Command: lookup player ip                      | `RBAC_PERM_COMMAND_LOOKUP_PLAYER_IP`                      | 197 (Gamemaster Commands)                  |
| 453 | Command: lookup player account                 | `RBAC_PERM_COMMAND_LOOKUP_PLAYER_ACCOUNT`                 | 197 (Gamemaster Commands)                  |
| 454 | Command: lookup player email                   | `RBAC_PERM_COMMAND_LOOKUP_PLAYER_EMAIL`                   | 197 (Gamemaster Commands)                  |
| 455 | Command: lookup skill                          | `RBAC_PERM_COMMAND_LOOKUP_SKILL`                          | 199 (Player Commands)                      |
| 456 | Command: lookup spell                          | `RBAC_PERM_COMMAND_LOOKUP_SPELL`                          | 199 (Player Commands)                      |
| 457 | Command: lookup spell id                       | `RBAC_PERM_COMMAND_LOOKUP_SPELL_ID`                       | 197 (Gamemaster Commands)                  |
| 458 | Command: lookup taxinode                       | `RBAC_PERM_COMMAND_LOOKUP_TAXINODE`                       | 197 (Gamemaster Commands)                  |
| 459 | Command: lookup tele                           | `RBAC_PERM_COMMAND_LOOKUP_TELE`                           | 199 (Player Commands)                      |
| 460 | Command: lookup title                          | `RBAC_PERM_COMMAND_LOOKUP_TITLE`                          | 197 (Gamemaster Commands)                  |
| 461 | Command: lookup map                            | `RBAC_PERM_COMMAND_LOOKUP_MAP`                            | 197 (Gamemaster Commands)                  |
| 462 | Command: announce                              | `RBAC_PERM_COMMAND_ANNOUNCE`                              | 198 (Moderator Commands)                   |
| 463 | Command: channel                               | `RBAC_PERM_COMMAND_CHANNEL`                               | 196 (Administrator Commands)               |
| 464 | Command: channel set                           | `RBAC_PERM_COMMAND_CHANNEL_SET`                           | 196 (Administrator Commands)               |
| 465 | Command: channel set ownership                 | `RBAC_PERM_COMMAND_CHANNEL_SET_OWNERSHIP`                 | 196 (Administrator Commands)               |
| 466 | Command: gmannounce                            | `RBAC_PERM_COMMAND_GMANNOUNCE`                            | 198 (Moderator Commands)                   |
| 467 | Command: gmnameannounce                        | `RBAC_PERM_COMMAND_GMNAMEANNOUNCE`                        | 198 (Moderator Commands)                   |
| 468 | Command: gmnotify                              | `RBAC_PERM_COMMAND_GMNOTIFY`                              | 198 (Moderator Commands)                   |
| 469 | Command: nameannounce                          | `RBAC_PERM_COMMAND_NAMEANNOUNCE`                          | 198 (Moderator Commands)                   |
| 470 | Command: notify                                | `RBAC_PERM_COMMAND_NOTIFY`                                | 198 (Moderator Commands)                   |
| 472 | Command: group                                 | `RBAC_PERM_COMMAND_GROUP`                                 | 197 (Gamemaster Commands)                  |
| 473 | Command: group leader                          | `RBAC_PERM_COMMAND_GROUP_LEADER`                          | 197 (Gamemaster Commands)                  |
| 474 | Command: group disband                         | `RBAC_PERM_COMMAND_GROUP_DISBAND`                         | 197 (Gamemaster Commands)                  |
| 475 | Command: group remove                          | `RBAC_PERM_COMMAND_GROUP_REMOVE`                          | 197 (Gamemaster Commands)                  |
| 476 | Command: group join                            | `RBAC_PERM_COMMAND_GROUP_JOIN`                            | 197 (Gamemaster Commands)                  |
| 477 | Command: group list                            | `RBAC_PERM_COMMAND_GROUP_LIST`                            | 197 (Gamemaster Commands)                  |
| 478 | Command: group summon                          | `RBAC_PERM_COMMAND_GROUP_SUMMON`                          | 197 (Gamemaster Commands)                  |
| 479 | Command: pet                                   | `RBAC_PERM_COMMAND_PET`                                   | 197 (Gamemaster Commands)                  |
| 480 | Command: pet create                            | `RBAC_PERM_COMMAND_PET_CREATE`                            | 197 (Gamemaster Commands)                  |
| 481 | Command: pet learn                             | `RBAC_PERM_COMMAND_PET_LEARN`                             | 197 (Gamemaster Commands)                  |
| 482 | Command: pet unlearn                           | `RBAC_PERM_COMMAND_PET_UNLEARN`                           | 197 (Gamemaster Commands)                  |
| 483 | Command: send                                  | `RBAC_PERM_COMMAND_SEND`                                  | 197 (Gamemaster Commands)                  |
| 484 | Command: send items                            | `RBAC_PERM_COMMAND_SEND_ITEMS`                            | 197 (Gamemaster Commands)                  |
| 485 | Command: send mail                             | `RBAC_PERM_COMMAND_SEND_MAIL`                             | 197 (Gamemaster Commands)                  |
| 486 | Command: send message                          | `RBAC_PERM_COMMAND_SEND_MESSAGE`                          | 197 (Gamemaster Commands)                  |
| 487 | Command: send money                            | `RBAC_PERM_COMMAND_SEND_MONEY`                            | 197 (Gamemaster Commands)                  |
| 488 | Command: additem                               | `RBAC_PERM_COMMAND_ADDITEM`                               | 197 (Gamemaster Commands)                  |
| 489 | Command: additemset                            | `RBAC_PERM_COMMAND_ADDITEMSET`                            | 197 (Gamemaster Commands)                  |
| 490 | Command: appear                                | `RBAC_PERM_COMMAND_APPEAR`                                | 197 (Gamemaster Commands)                  |
| 491 | Command: aura                                  | `RBAC_PERM_COMMAND_AURA`                                  | 197 (Gamemaster Commands)                  |
| 492 | Command: bank                                  | `RBAC_PERM_COMMAND_BANK`                                  | 197 (Gamemaster Commands)                  |
| 493 | Command: bindsight                             | `RBAC_PERM_COMMAND_BINDSIGHT`                             | 197 (Gamemaster Commands)                  |
| 494 | Command: combatstop                            | `RBAC_PERM_COMMAND_COMBATSTOP`                            | 197 (Gamemaster Commands)                  |
| 495 | Command: cometome                              | `RBAC_PERM_COMMAND_COMETOME`                              | 197 (Gamemaster Commands)                  |
| 496 | Command: commands                              | `RBAC_PERM_COMMAND_COMMANDS`                              | 199 (Player Commands)                      |
| 497 | Command: cooldown                              | `RBAC_PERM_COMMAND_COOLDOWN`                              | 197 (Gamemaster Commands)                  |
| 498 | Command: damage                                | `RBAC_PERM_COMMAND_DAMAGE`                                | 197 (Gamemaster Commands)                  |
| 499 | Command: dev                                   | `RBAC_PERM_COMMAND_DEV`                                   | 197 (Gamemaster Commands)                  |
| 500 | Command: die                                   | `RBAC_PERM_COMMAND_DIE`                                   | 197 (Gamemaster Commands)                  |
| 501 | Command: dismount                              | `RBAC_PERM_COMMAND_DISMOUNT`                              | 199 (Player Commands)                      |
| 502 | Command: distance                              | `RBAC_PERM_COMMAND_DISTANCE`                              | 197 (Gamemaster Commands)                  |
| 503 | Command: flusharenapoints                      | `RBAC_PERM_COMMAND_FLUSHARENAPOINTS`                      | 196 (Administrator Commands)               |
| 504 | Command: freeze                                | `RBAC_PERM_COMMAND_FREEZE`                                | 197 (Gamemaster Commands)                  |
| 505 | Command: gps                                   | `RBAC_PERM_COMMAND_GPS`                                   | 199 (Player Commands)                      |
| 506 | Command: guid                                  | `RBAC_PERM_COMMAND_GUID`                                  | 197 (Gamemaster Commands)                  |
| 507 | Command: help                                  | `RBAC_PERM_COMMAND_HELP`                                  | 199 (Player Commands)                      |
| 508 | Command: hidearea                              | `RBAC_PERM_COMMAND_HIDEAREA`                              | 197 (Gamemaster Commands)                  |
| 509 | Command: itemmove                              | `RBAC_PERM_COMMAND_ITEMMOVE`                              | 197 (Gamemaster Commands)                  |
| 510 | Command: kick                                  | `RBAC_PERM_COMMAND_KICK`                                  | 198 (Moderator Commands)                   |
| 511 | Command: linkgrave                             | `RBAC_PERM_COMMAND_LINKGRAVE`                             | 196 (Administrator Commands)               |
| 512 | Command: listfreeze                            | `RBAC_PERM_COMMAND_LISTFREEZE`                            | 197 (Gamemaster Commands)                  |
| 513 | Command: maxskill                              | `RBAC_PERM_COMMAND_MAXSKILL`                              | 197 (Gamemaster Commands)                  |
| 514 | Command: movegens                              | `RBAC_PERM_COMMAND_MOVEGENS`                              | 197 (Gamemaster Commands)                  |
| 515 | Command: mute                                  | `RBAC_PERM_COMMAND_MUTE`                                  | 198 (Moderator Commands)                   |
| 516 | Command: neargrave                             | `RBAC_PERM_COMMAND_NEARGRAVE`                             | 197 (Gamemaster Commands)                  |
| 517 | Command: pinfo                                 | `RBAC_PERM_COMMAND_PINFO`                                 | 198 (Moderator Commands)                   |
| 518 | Command: playall                               | `RBAC_PERM_COMMAND_PLAYALL`                               | 197 (Gamemaster Commands)                  |
| 519 | Command: possess                               | `RBAC_PERM_COMMAND_POSSESS`                               | 197 (Gamemaster Commands)                  |
| 520 | Command: recall                                | `RBAC_PERM_COMMAND_RECALL`                                | 197 (Gamemaster Commands)                  |
| 521 | Command: repairitems                           | `RBAC_PERM_COMMAND_REPAIRITEMS`                           | 197 (Gamemaster Commands)                  |
| 522 | Command: respawn                               | `RBAC_PERM_COMMAND_RESPAWN`                               | 197 (Gamemaster Commands)                  |
| 523 | Command: revive                                | `RBAC_PERM_COMMAND_REVIVE`                                | 197 (Gamemaster Commands)                  |
| 524 | Command: saveall                               | `RBAC_PERM_COMMAND_SAVEALL`                               | 196 (Administrator Commands)               |
| 525 | Command: save                                  | `RBAC_PERM_COMMAND_SAVE`                                  | 199 (Player Commands)                      |
| 526 | Command: setskill                              | `RBAC_PERM_COMMAND_SETSKILL`                              | 197 (Gamemaster Commands)                  |
| 527 | Command: showarea                              | `RBAC_PERM_COMMAND_SHOWAREA`                              | 197 (Gamemaster Commands)                  |
| 528 | Command: summon                                | `RBAC_PERM_COMMAND_SUMMON`                                | 197 (Gamemaster Commands)                  |
| 529 | Command: unaura                                | `RBAC_PERM_COMMAND_UNAURA`                                | 197 (Gamemaster Commands)                  |
| 530 | Command: unbindsight                           | `RBAC_PERM_COMMAND_UNBINDSIGHT`                           | 197 (Gamemaster Commands)                  |
| 531 | Command: unfreeze                              | `RBAC_PERM_COMMAND_UNFREEZE`                              | 197 (Gamemaster Commands)                  |
| 532 | Command: unmute                                | `RBAC_PERM_COMMAND_UNMUTE`                                | 198 (Moderator Commands)                   |
| 533 | Command: unpossess                             | `RBAC_PERM_COMMAND_UNPOSSESS`                             | 197 (Gamemaster Commands)                  |
| 534 | Command: unstuck                               | `RBAC_PERM_COMMAND_UNSTUCK`                               | 199 (Player Commands)                      |
| 535 | Command: wchange                               | `RBAC_PERM_COMMAND_WCHANGE`                               | 197 (Gamemaster Commands)                  |
| 536 | Command: mmap                                  | `RBAC_PERM_COMMAND_MMAP`                                  | 197 (Gamemaster Commands)                  |
| 537 | Command: mmap loadedtiles                      | `RBAC_PERM_COMMAND_MMAP_LOADEDTILES`                      | 197 (Gamemaster Commands)                  |
| 538 | Command: mmap loc                              | `RBAC_PERM_COMMAND_MMAP_LOC`                              | 197 (Gamemaster Commands)                  |
| 539 | Command: mmap path                             | `RBAC_PERM_COMMAND_MMAP_PATH`                             | 197 (Gamemaster Commands)                  |
| 540 | Command: mmap stats                            | `RBAC_PERM_COMMAND_MMAP_STATS`                            | 197 (Gamemaster Commands)                  |
| 541 | Command: mmap testarea                         | `RBAC_PERM_COMMAND_MMAP_TESTAREA`                         | 197 (Gamemaster Commands)                  |
| 542 | Command: morph                                 | `RBAC_PERM_COMMAND_MORPH`                                 | 197 (Gamemaster Commands)                  |
| 543 | Command: demorph                               | `RBAC_PERM_COMMAND_DEMORPH`                               | 197 (Gamemaster Commands)                  |
| 544 | Command: modify                                | `RBAC_PERM_COMMAND_MODIFY`                                | 197 (Gamemaster Commands)                  |
| 545 | Command: modify arenapoints                    | `RBAC_PERM_COMMAND_MODIFY_ARENAPOINTS`                    | 197 (Gamemaster Commands)                  |
| 546 | Command: modify bit                            | `RBAC_PERM_COMMAND_MODIFY_BIT`                            | 197 (Gamemaster Commands)                  |
| 547 | Command: modify drunk                          | `RBAC_PERM_COMMAND_MODIFY_DRUNK`                          | 197 (Gamemaster Commands)                  |
| 548 | Command: modify energy                         | `RBAC_PERM_COMMAND_MODIFY_ENERGY`                         | 197 (Gamemaster Commands)                  |
| 549 | Command: modify faction                        | `RBAC_PERM_COMMAND_MODIFY_FACTION`                        | 197 (Gamemaster Commands)                  |
| 550 | Command: modify gender                         | `RBAC_PERM_COMMAND_MODIFY_GENDER`                         | 197 (Gamemaster Commands)                  |
| 551 | Command: modify honor                          | `RBAC_PERM_COMMAND_MODIFY_HONOR`                          | 197 (Gamemaster Commands)                  |
| 552 | Command: modify hp                             | `RBAC_PERM_COMMAND_MODIFY_HP`                             | 197 (Gamemaster Commands)                  |
| 553 | Command: modify mana                           | `RBAC_PERM_COMMAND_MODIFY_MANA`                           | 197 (Gamemaster Commands)                  |
| 554 | Command: modify money                          | `RBAC_PERM_COMMAND_MODIFY_MONEY`                          | 197 (Gamemaster Commands)                  |
| 555 | Command: modify mount                          | `RBAC_PERM_COMMAND_MODIFY_MOUNT`                          | 197 (Gamemaster Commands)                  |
| 556 | Command: modify phase                          | `RBAC_PERM_COMMAND_MODIFY_PHASE`                          | 197 (Gamemaster Commands)                  |
| 557 | Command: modify rage                           | `RBAC_PERM_COMMAND_MODIFY_RAGE`                           | 197 (Gamemaster Commands)                  |
| 558 | Command: modify reputation                     | `RBAC_PERM_COMMAND_MODIFY_REPUTATION`                     | 197 (Gamemaster Commands)                  |
| 559 | Command: modify runicpower                     | `RBAC_PERM_COMMAND_MODIFY_RUNICPOWER`                     | 197 (Gamemaster Commands)                  |
| 560 | Command: modify scale                          | `RBAC_PERM_COMMAND_MODIFY_SCALE`                          | 197 (Gamemaster Commands)                  |
| 561 | Command: modify speed                          | `RBAC_PERM_COMMAND_MODIFY_SPEED`                          | 197 (Gamemaster Commands)                  |
| 562 | Command: modify speed all                      | `RBAC_PERM_COMMAND_MODIFY_SPEED_ALL`                      | 197 (Gamemaster Commands)                  |
| 563 | Command: modify speed backwalk                 | `RBAC_PERM_COMMAND_MODIFY_SPEED_BACKWALK`                 | 197 (Gamemaster Commands)                  |
| 564 | Command: modify speed fly                      | `RBAC_PERM_COMMAND_MODIFY_SPEED_FLY`                      | 197 (Gamemaster Commands)                  |
| 565 | Command: modify speed walk                     | `RBAC_PERM_COMMAND_MODIFY_SPEED_WALK`                     | 197 (Gamemaster Commands)                  |
| 566 | Command: modify speed swim                     | `RBAC_PERM_COMMAND_MODIFY_SPEED_SWIM`                     | 197 (Gamemaster Commands)                  |
| 567 | Command: modify spell                          | `RBAC_PERM_COMMAND_MODIFY_SPELL`                          | 197 (Gamemaster Commands)                  |
| 568 | Command: modify standstate                     | `RBAC_PERM_COMMAND_MODIFY_STANDSTATE`                     | 197 (Gamemaster Commands)                  |
| 569 | Command: modify talentpoints                   | `RBAC_PERM_COMMAND_MODIFY_TALENTPOINTS`                   | 197 (Gamemaster Commands)                  |
| 571 | Command: npc add                               | `RBAC_PERM_COMMAND_NPC_ADD`                               | 197 (Gamemaster Commands)                  |
| 572 | Command: npc add formation                     | `RBAC_PERM_COMMAND_NPC_ADD_FORMATION`                     | 197 (Gamemaster Commands)                  |
| 573 | Command: npc add item                          | `RBAC_PERM_COMMAND_NPC_ADD_ITEM`                          | 197 (Gamemaster Commands)                  |
| 574 | Command: npc add move                          | `RBAC_PERM_COMMAND_NPC_ADD_MOVE`                          | 197 (Gamemaster Commands)                  |
| 575 | Command: npc add temp                          | `RBAC_PERM_COMMAND_NPC_ADD_TEMP`                          | 197 (Gamemaster Commands)                  |
| 576 | Command: npc delete                            | `RBAC_PERM_COMMAND_NPC_DELETE`                            | 197 (Gamemaster Commands)                  |
| 577 | Command: npc delete item                       | `RBAC_PERM_COMMAND_NPC_DELETE_ITEM`                       | 197 (Gamemaster Commands)                  |
| 578 | Command: npc follow                            | `RBAC_PERM_COMMAND_NPC_FOLLOW`                            | 197 (Gamemaster Commands)                  |
| 579 | Command: npc follow stop                       | `RBAC_PERM_COMMAND_NPC_FOLLOW_STOP`                       | 197 (Gamemaster Commands)                  |
| 580 | Command: npc set                               | `RBAC_PERM_COMMAND_NPC_SET`                               | 197 (Gamemaster Commands)                  |
| 581 | Command: npc set allowmove                     | `RBAC_PERM_COMMAND_NPC_SET_ALLOWMOVE`                     | 197 (Gamemaster Commands)                  |
| 582 | Command: npc set entry                         | `RBAC_PERM_COMMAND_NPC_SET_ENTRY`                         | 197 (Gamemaster Commands)                  |
| 583 | Command: npc set factionid                     | `RBAC_PERM_COMMAND_NPC_SET_FACTIONID`                     | 197 (Gamemaster Commands)                  |
| 584 | Command: npc set flag                          | `RBAC_PERM_COMMAND_NPC_SET_FLAG`                          | 197 (Gamemaster Commands)                  |
| 585 | Command: npc set level                         | `RBAC_PERM_COMMAND_NPC_SET_LEVEL`                         | 197 (Gamemaster Commands)                  |
| 586 | Command: npc set link                          | `RBAC_PERM_COMMAND_NPC_SET_LINK`                          | 197 (Gamemaster Commands)                  |
| 587 | Command: npc set model                         | `RBAC_PERM_COMMAND_NPC_SET_MODEL`                         | 197 (Gamemaster Commands)                  |
| 588 | Command: npc set movetype                      | `RBAC_PERM_COMMAND_NPC_SET_MOVETYPE`                      | 197 (Gamemaster Commands)                  |
| 589 | Command: npc set phase                         | `RBAC_PERM_COMMAND_NPC_SET_PHASE`                         | 197 (Gamemaster Commands)                  |
| 590 | Command: npc set spawndist                     | `RBAC_PERM_COMMAND_NPC_SET_SPAWNDIST`                     | 197 (Gamemaster Commands)                  |
| 591 | Command: npc set spawntime                     | `RBAC_PERM_COMMAND_NPC_SET_SPAWNTIME`                     | 197 (Gamemaster Commands)                  |
| 592 | Command: npc set data                          | `RBAC_PERM_COMMAND_NPC_SET_DATA`                          | 197 (Gamemaster Commands)                  |
| 593 | Command: npc info                              | `RBAC_PERM_COMMAND_NPC_INFO`                              | 197 (Gamemaster Commands)                  |
| 594 | Command: npc near                              | `RBAC_PERM_COMMAND_NPC_NEAR`                              | 197 (Gamemaster Commands)                  |
| 595 | Command: npc move                              | `RBAC_PERM_COMMAND_NPC_MOVE`                              | 197 (Gamemaster Commands)                  |
| 596 | Command: npc playemote                         | `RBAC_PERM_COMMAND_NPC_PLAYEMOTE`                         | 197 (Gamemaster Commands)                  |
| 597 | Command: npc say                               | `RBAC_PERM_COMMAND_NPC_SAY`                               | 197 (Gamemaster Commands)                  |
| 598 | Command: npc textemote                         | `RBAC_PERM_COMMAND_NPC_TEXTEMOTE`                         | 197 (Gamemaster Commands)                  |
| 599 | Command: npc whisper                           | `RBAC_PERM_COMMAND_NPC_WHISPER`                           | 197 (Gamemaster Commands)                  |
| 600 | Command: npc yell                              | `RBAC_PERM_COMMAND_NPC_YELL`                              | 197 (Gamemaster Commands)                  |
| 601 | Command: npc tame                              | `RBAC_PERM_COMMAND_NPC_TAME`                              | 197 (Gamemaster Commands)                  |
| 602 | Command: quest                                 | `RBAC_PERM_COMMAND_QUEST`                                 | 197 (Gamemaster Commands)                  |
| 603 | Command: quest add                             | `RBAC_PERM_COMMAND_QUEST_ADD`                             | 197 (Gamemaster Commands)                  |
| 604 | Command: quest complete                        | `RBAC_PERM_COMMAND_QUEST_COMPLETE`                        | 197 (Gamemaster Commands)                  |
| 605 | Command: quest remove                          | `RBAC_PERM_COMMAND_QUEST_REMOVE`                          | 197 (Gamemaster Commands)                  |
| 606 | Command: quest reward                          | `RBAC_PERM_COMMAND_QUEST_REWARD`                          | 197 (Gamemaster Commands)                  |
| 607 | Command: reload                                | `RBAC_PERM_COMMAND_RELOAD`                                | 196 (Administrator Commands)               |
| 608 | Command: reload access_requirement             | `RBAC_PERM_COMMAND_RELOAD_ACCESS_REQUIREMENT`             | 196 (Administrator Commands)               |
| 609 | Command: reload achievement_criteria_data      | `RBAC_PERM_COMMAND_RELOAD_ACHIEVEMENT_CRITERIA_DATA`      | 196 (Administrator Commands)               |
| 610 | Command: reload achievement_reward             | `RBAC_PERM_COMMAND_RELOAD_ACHIEVEMENT_REWARD`             | 196 (Administrator Commands)               |
| 611 | Command: reload all                            | `RBAC_PERM_COMMAND_RELOAD_ALL`                            | 196 (Administrator Commands)               |
| 612 | Command: reload all achievement                | `RBAC_PERM_COMMAND_RELOAD_ALL_ACHIEVEMENT`                | 196 (Administrator Commands)               |
| 613 | Command: reload all area                       | `RBAC_PERM_COMMAND_RELOAD_ALL_AREA`                       | 196 (Administrator Commands)               |
| 614 | Command: reload broadcast_text                 | `RBAC_PERM_COMMAND_RELOAD_BROADCAST_TEXT`                 | 196 (Administrator Commands)               |
| 615 | Command: reload all gossips                    | `RBAC_PERM_COMMAND_RELOAD_ALL_GOSSIP`                     | 196 (Administrator Commands)               |
| 616 | Command: reload all item                       | `RBAC_PERM_COMMAND_RELOAD_ALL_ITEM`                       | 196 (Administrator Commands)               |
| 617 | Command: reload all locales                    | `RBAC_PERM_COMMAND_RELOAD_ALL_LOCALES`                    | 196 (Administrator Commands)               |
| 618 | Command: reload all loot                       | `RBAC_PERM_COMMAND_RELOAD_ALL_LOOT`                       | 196 (Administrator Commands)               |
| 619 | Command: reload all npc                        | `RBAC_PERM_COMMAND_RELOAD_ALL_NPC`                        | 196 (Administrator Commands)               |
| 620 | Command: reload all quest                      | `RBAC_PERM_COMMAND_RELOAD_ALL_QUEST`                      | 196 (Administrator Commands)               |
| 621 | Command: reload all scripts                    | `RBAC_PERM_COMMAND_RELOAD_ALL_SCRIPTS`                    | 196 (Administrator Commands)               |
| 622 | Command: reload all spell                      | `RBAC_PERM_COMMAND_RELOAD_ALL_SPELL`                      | 196 (Administrator Commands)               |
| 623 | Command: reload areatrigger_involvedrelation   | `RBAC_PERM_COMMAND_RELOAD_AREATRIGGER_INVOLVEDRELATION`   | 196 (Administrator Commands)               |
| 624 | Command: reload areatrigger_tavern             | `RBAC_PERM_COMMAND_RELOAD_AREATRIGGER_TAVERN`             | 196 (Administrator Commands)               |
| 625 | Command: reload areatrigger_teleport           | `RBAC_PERM_COMMAND_RELOAD_AREATRIGGER_TELEPORT`           | 196 (Administrator Commands)               |
| 626 | Command: reload auctions                       | `RBAC_PERM_COMMAND_RELOAD_AUCTIONS`                       | 196 (Administrator Commands)               |
| 627 | Command: reload autobroadcast                  | `RBAC_PERM_COMMAND_RELOAD_AUTOBROADCAST`                  | 196 (Administrator Commands)               |
| 629 | Command: reload conditions                     | `RBAC_PERM_COMMAND_RELOAD_CONDITIONS`                     | 196 (Administrator Commands)               |
| 630 | Command: reload config                         | `RBAC_PERM_COMMAND_RELOAD_CONFIG`                         | 196 (Administrator Commands)               |
| 631 | Command: reload battleground_template          | `RBAC_PERM_COMMAND_RELOAD_BATTLEGROUND_TEMPLATE`          | 196 (Administrator Commands)               |
| 632 | Command: mutehistory                           | `RBAC_PERM_COMMAND_MUTEHISTORY`                           | 194 (Moderator), 198 (Moderator Commands)  |
| 633 | Command: reload creature_linked_respawn        | `RBAC_PERM_COMMAND_RELOAD_CREATURE_LINKED_RESPAWN`        | 196 (Administrator Commands)               |
| 634 | Command: reload creature_loot_template         | `RBAC_PERM_COMMAND_RELOAD_CREATURE_LOOT_TEMPLATE`         | 196 (Administrator Commands)               |
| 635 | Command: reload creature_onkill_reputation     | `RBAC_PERM_COMMAND_RELOAD_CREATURE_ONKILL_REPUTATION`     | 196 (Administrator Commands)               |
| 636 | Command: reload creature_questender            | `RBAC_PERM_COMMAND_RELOAD_CREATURE_QUESTENDER`            | 196 (Administrator Commands)               |
| 637 | Command: reload creature_queststarter          | `RBAC_PERM_COMMAND_RELOAD_CREATURE_QUESTSTARTER`          | 196 (Administrator Commands)               |
| 638 | Command: reload creature_summon_groups         | `RBAC_PERM_COMMAND_RELOAD_CREATURE_SUMMON_GROUPS`         | 196 (Administrator Commands)               |
| 639 | Command: reload creature_template              | `RBAC_PERM_COMMAND_RELOAD_CREATURE_TEMPLATE`              | 196 (Administrator Commands)               |
| 640 | Command: reload creature_text                  | `RBAC_PERM_COMMAND_RELOAD_CREATURE_TEXT`                  | 196 (Administrator Commands)               |
| 641 | Command: reload disables                       | `RBAC_PERM_COMMAND_RELOAD_DISABLES`                       | 196 (Administrator Commands)               |
| 642 | Command: reload disenchant_loot_template       | `RBAC_PERM_COMMAND_RELOAD_DISENCHANT_LOOT_TEMPLATE`       | 196 (Administrator Commands)               |
| 643 | Command: reload event_scripts                  | `RBAC_PERM_COMMAND_RELOAD_EVENT_SCRIPTS`                  | 196 (Administrator Commands)               |
| 644 | Command: reload fishing_loot_template          | `RBAC_PERM_COMMAND_RELOAD_FISHING_LOOT_TEMPLATE`          | 196 (Administrator Commands)               |
| 645 | Command: reload graveyard_zone                 | `RBAC_PERM_COMMAND_RELOAD_GRAVEYARD_ZONE`                 | 196 (Administrator Commands)               |
| 646 | Command: reload game_tele                      | `RBAC_PERM_COMMAND_RELOAD_GAME_TELE`                      | 196 (Administrator Commands)               |
| 647 | Command: reload gameobject_questender          | `RBAC_PERM_COMMAND_RELOAD_GAMEOBJECT_QUESTENDER`          | 196 (Administrator Commands)               |
| 648 | Command: reload gameobject_quest_loot_template | `RBAC_PERM_COMMAND_RELOAD_GAMEOBJECT_QUEST_LOOT_TEMPLATE` | 196 (Administrator Commands)               |
| 649 | Command: reload gameobject_queststarter        | `RBAC_PERM_COMMAND_RELOAD_GAMEOBJECT_QUESTSTARTER`        | 196 (Administrator Commands)               |
| 650 | Command: reload gm_tickets                     | `RBAC_PERM_COMMAND_RELOAD_GM_TICKETS`                     | 196 (Administrator Commands)               |
| 651 | Command: reload gossip_menu                    | `RBAC_PERM_COMMAND_RELOAD_GOSSIP_MENU`                    | 196 (Administrator Commands)               |
| 652 | Command: reload gossip_menu_option             | `RBAC_PERM_COMMAND_RELOAD_GOSSIP_MENU_OPTION`             | 196 (Administrator Commands)               |
| 653 | Command: reload item_enchantment_template      | `RBAC_PERM_COMMAND_RELOAD_ITEM_ENCHANTMENT_TEMPLATE`      | 196 (Administrator Commands)               |
| 654 | Command: reload item_loot_template             | `RBAC_PERM_COMMAND_RELOAD_ITEM_LOOT_TEMPLATE`             | 196 (Administrator Commands)               |
| 655 | Command: reload item_set_names                 | `RBAC_PERM_COMMAND_RELOAD_ITEM_SET_NAMES`                 | 196 (Administrator Commands)               |
| 656 | Command: reload lfg_dungeon_rewards            | `RBAC_PERM_COMMAND_RELOAD_LFG_DUNGEON_REWARDS`            | 196 (Administrator Commands)               |
| 657 | Command: reload achievement_reward_locale      | `RBAC_PERM_COMMAND_RELOAD_ACHIEVEMENT_REWARD_LOCALE`      | 196 (Administrator Commands)               |
| 658 | Command: reload creature_template_locale       | `RBAC_PERM_COMMAND_RELOAD_CREATURE_TEMPLATE_LOCALE`       | 196 (Administrator Commands)               |
| 659 | Command: reload creature_text_locale           | `RBAC_PERM_COMMAND_RELOAD_CREATURE_TEXT_LOCALE`           | 196 (Administrator Commands)               |
| 660 | Command: reload gameobject_template_locale     | `RBAC_PERM_COMMAND_RELOAD_GAMEOBJECT_TEMPLATE_LOCALE`     | 196 (Administrator Commands)               |
| 661 | Command: reload gossip_menu_option_locale      | `RBAC_PERM_COMMAND_RELOAD_GOSSIP_MENU_OPTION_LOCALE`      | 196 (Administrator Commands)               |
| 662 | Command: reload item_template_locale           | `RBAC_PERM_COMMAND_RELOAD_ITEM_TEMPLATE_LOCALE`           | 196 (Administrator Commands)               |
| 663 | Command: reload item_set_name_locale           | `RBAC_PERM_COMMAND_RELOAD_ITEM_SET_NAME_LOCALE`           | 196 (Administrator Commands)               |
| 664 | Command: reload npc_text_locale                | `RBAC_PERM_COMMAND_RELOAD_NPC_TEXT_LOCALE`                | 196 (Administrator Commands)               |
| 665 | Command: reload page_text_locale               | `RBAC_PERM_COMMAND_RELOAD_PAGE_TEXT_LOCALE`               | 196 (Administrator Commands)               |
| 666 | Command: reload points_of_interest_locale      | `RBAC_PERM_COMMAND_RELOAD_POINTS_OF_INTEREST_LOCALE`      | 196 (Administrator Commands)               |
| 667 | Command: reload quest_template_locale          | `RBAC_PERM_COMMAND_RELOAD_QUEST_TEMPLATE_LOCALE`          | 196 (Administrator Commands)               |
| 668 | Command: reload mail_level_reward              | `RBAC_PERM_COMMAND_RELOAD_MAIL_LEVEL_REWARD`              | 196 (Administrator Commands)               |
| 669 | Command: reload mail_loot_template             | `RBAC_PERM_COMMAND_RELOAD_MAIL_LOOT_TEMPLATE`             | 196 (Administrator Commands)               |
| 670 | Command: reload milling_loot_template          | `RBAC_PERM_COMMAND_RELOAD_MILLING_LOOT_TEMPLATE`          | 196 (Administrator Commands)               |
| 671 | Command: reload npc_spellclick_spells          | `RBAC_PERM_COMMAND_RELOAD_NPC_SPELLCLICK_SPELLS`          | 196 (Administrator Commands)               |
| 672 | Command: reload trainer                        | `RBAC_PERM_COMMAND_RELOAD_TRAINER`                        | 196 (Administrator Commands)               |
| 673 | Command: reload npc_vendor                     | `RBAC_PERM_COMMAND_RELOAD_NPC_VENDOR`                     | 196 (Administrator Commands)               |
| 674 | Command: reload page_text                      | `RBAC_PERM_COMMAND_RELOAD_PAGE_TEXT`                      | 196 (Administrator Commands)               |
| 675 | Command: reload pickpocketing_loot_template    | `RBAC_PERM_COMMAND_RELOAD_PICKPOCKETING_LOOT_TEMPLATE`    | 196 (Administrator Commands)               |
| 676 | Command: reload points_of_interest             | `RBAC_PERM_COMMAND_RELOAD_POINTS_OF_INTEREST`             | 196 (Administrator Commands)               |
| 677 | Command: reload prospecting_loot_template      | `RBAC_PERM_COMMAND_RELOAD_PROSPECTING_LOOT_TEMPLATE`      | 196 (Administrator Commands)               |
| 678 | Command: reload quest_poi                      | `RBAC_PERM_COMMAND_RELOAD_QUEST_POI`                      | 196 (Administrator Commands)               |
| 679 | Command: reload quest_template                 | `RBAC_PERM_COMMAND_RELOAD_QUEST_TEMPLATE`                 | 196 (Administrator Commands)               |
| 680 | Command: reload rbac                           | `RBAC_PERM_COMMAND_RELOAD_RBAC`                           | 196 (Administrator Commands)               |
| 681 | Command: reload reference_loot_template        | `RBAC_PERM_COMMAND_RELOAD_REFERENCE_LOOT_TEMPLATE`        | 196 (Administrator Commands)               |
| 682 | Command: reload reserved_name                  | `RBAC_PERM_COMMAND_RELOAD_RESERVED_NAME`                  | 196 (Administrator Commands)               |
| 683 | Command: reload reputation_reward_rate         | `RBAC_PERM_COMMAND_RELOAD_REPUTATION_REWARD_RATE`         | 196 (Administrator Commands)               |
| 684 | Command: reload reputation_spillover_template  | `RBAC_PERM_COMMAND_RELOAD_SPILLOVER_TEMPLATE`             | 196 (Administrator Commands)               |
| 685 | Command: reload skill_discovery_template       | `RBAC_PERM_COMMAND_RELOAD_SKILL_DISCOVERY_TEMPLATE`       | 196 (Administrator Commands)               |
| 686 | Command: reload skill_extra_item_template      | `RBAC_PERM_COMMAND_RELOAD_SKILL_EXTRA_ITEM_TEMPLATE`      | 196 (Administrator Commands)               |
| 687 | Command: reload skill_fishing_base_level       | `RBAC_PERM_COMMAND_RELOAD_SKILL_FISHING_BASE_LEVEL`       | 196 (Administrator Commands)               |
| 688 | Command: reload skinning_loot_template         | `RBAC_PERM_COMMAND_RELOAD_SKINNING_LOOT_TEMPLATE`         | 196 (Administrator Commands)               |
| 689 | Command: reload smart_scripts                  | `RBAC_PERM_COMMAND_RELOAD_SMART_SCRIPTS`                  | 196 (Administrator Commands)               |
| 690 | Command: reload spell_required                 | `RBAC_PERM_COMMAND_RELOAD_SPELL_REQUIRED`                 | 196 (Administrator Commands)               |
| 691 | Command: reload spell_area                     | `RBAC_PERM_COMMAND_RELOAD_SPELL_AREA`                     | 196 (Administrator Commands)               |
| 692 | Command: reload spell_bonus_data               | `RBAC_PERM_COMMAND_RELOAD_SPELL_BONUS_DATA`               | 196 (Administrator Commands)               |
| 693 | Command: reload spell_group                    | `RBAC_PERM_COMMAND_RELOAD_SPELL_GROUP`                    | 196 (Administrator Commands)               |
| 694 | Command: reload spell_learn_spell              | `RBAC_PERM_COMMAND_RELOAD_SPELL_LEARN_SPELL`              | 196 (Administrator Commands)               |
| 695 | Command: reload spell_loot_template            | `RBAC_PERM_COMMAND_RELOAD_SPELL_LOOT_TEMPLATE`            | 196 (Administrator Commands)               |
| 696 | Command: reload spell_linked_spell             | `RBAC_PERM_COMMAND_RELOAD_SPELL_LINKED_SPELL`             | 196 (Administrator Commands)               |
| 697 | Command: reload spell_pet_auras                | `RBAC_PERM_COMMAND_RELOAD_SPELL_PET_AURAS`                | 196 (Administrator Commands)               |
| 698 | Command: character changeaccount               | `RBAC_PERM_COMMAND_CHARACTER_CHANGEACCOUNT`               | 196 (Administrator Commands)               |
| 699 | Command: reload spell_proc                     | `RBAC_PERM_COMMAND_RELOAD_SPELL_PROC`                     | 196 (Administrator Commands)               |
| 701 | Command: reload spell_target_position          | `RBAC_PERM_COMMAND_RELOAD_SPELL_TARGET_POSITION`          | 196 (Administrator Commands)               |
| 702 | Command: reload spell_threats                  | `RBAC_PERM_COMMAND_RELOAD_SPELL_THREATS`                  | 196 (Administrator Commands)               |
| 703 | Command: reload spell_group_stack_rules        | `RBAC_PERM_COMMAND_RELOAD_SPELL_GROUP_STACK_RULES`        | 196 (Administrator Commands)               |
| 704 | Command: reload acore_string                   | `RBAC_PERM_COMMAND_RELOAD_ACORE_STRING`                   | 196 (Administrator Commands)               |
| 706 | Command: reload waypoint_scripts               | `RBAC_PERM_COMMAND_RELOAD_WAYPOINT_SCRIPTS`               | 196 (Administrator Commands)               |
| 707 | Command: reload waypoint_data                  | `RBAC_PERM_COMMAND_RELOAD_WAYPOINT_DATA`                  | 196 (Administrator Commands)               |
| 708 | Command: reload vehicle_accessory              | `RBAC_PERM_COMMAND_RELOAD_VEHICLE_ACCESSORY`              | 196 (Administrator Commands)               |
| 709 | Command: reload vehicle_template_accessory     | `RBAC_PERM_COMMAND_RELOAD_VEHICLE_TEMPLATE_ACCESSORY`     | 196 (Administrator Commands)               |
| 710 | Command: reset                                 | `RBAC_PERM_COMMAND_RESET`                                 | 196 (Administrator Commands)               |
| 711 | Command: reset achievements                    | `RBAC_PERM_COMMAND_RESET_ACHIEVEMENTS`                    | 196 (Administrator Commands)               |
| 712 | Command: reset honor                           | `RBAC_PERM_COMMAND_RESET_HONOR`                           | 196 (Administrator Commands)               |
| 713 | Command: reset level                           | `RBAC_PERM_COMMAND_RESET_LEVEL`                           | 196 (Administrator Commands)               |
| 714 | Command: reset spells                          | `RBAC_PERM_COMMAND_RESET_SPELLS`                          | 196 (Administrator Commands)               |
| 715 | Command: reset stats                           | `RBAC_PERM_COMMAND_RESET_STATS`                           | 196 (Administrator Commands)               |
| 716 | Command: reset talents                         | `RBAC_PERM_COMMAND_RESET_TALENTS`                         | 196 (Administrator Commands)               |
| 717 | Command: reset all                             | `RBAC_PERM_COMMAND_RESET_ALL`                             | 196 (Administrator Commands)               |
| 718 | Command: server                                | `RBAC_PERM_COMMAND_SERVER`                                | 196 (Administrator Commands)               |
| 719 | Command: server corpses                        | `RBAC_PERM_COMMAND_SERVER_CORPSES`                        | 196 (Administrator Commands)               |
| 720 | Command: server exit                           | `RBAC_PERM_COMMAND_SERVER_EXIT`                           | 196 (Administrator Commands)               |
| 721 | Command: server idlerestart                    | `RBAC_PERM_COMMAND_SERVER_IDLERESTART`                    | 196 (Administrator Commands)               |
| 722 | Command: server idlerestart cancel             | `RBAC_PERM_COMMAND_SERVER_IDLERESTART_CANCEL`             | 196 (Administrator Commands)               |
| 723 | Command: server idleshutdown                   | `RBAC_PERM_COMMAND_SERVER_IDLESHUTDOWN`                   | 196 (Administrator Commands)               |
| 724 | Command: server idleshutdown cancel            | `RBAC_PERM_COMMAND_SERVER_IDLESHUTDOWN_CANCEL`            | 196 (Administrator Commands)               |
| 725 | Command: server info                           | `RBAC_PERM_COMMAND_SERVER_INFO`                           | 199 (Player Commands)                      |
| 726 | Command: server plimit                         | `RBAC_PERM_COMMAND_SERVER_PLIMIT`                         | 196 (Administrator Commands)               |
| 727 | Command: server restart                        | `RBAC_PERM_COMMAND_SERVER_RESTART`                        | 196 (Administrator Commands)               |
| 728 | Command: server restart cancel                 | `RBAC_PERM_COMMAND_SERVER_RESTART_CANCEL`                 | 196 (Administrator Commands)               |
| 729 | Command: server set                            | `RBAC_PERM_COMMAND_SERVER_SET`                            | 196 (Administrator Commands)               |
| 730 | Command: server set closed                     | `RBAC_PERM_COMMAND_SERVER_SET_CLOSED`                     | 196 (Administrator Commands)               |
| 731 | Command: server set difftime                   | `RBAC_PERM_COMMAND_SERVER_SET_DIFFTIME`                   | 196 (Administrator Commands)               |
| 732 | Command: server set loglevel                   | `RBAC_PERM_COMMAND_SERVER_SET_LOGLEVEL`                   | 196 (Administrator Commands)               |
| 733 | Command: server set motd                       | `RBAC_PERM_COMMAND_SERVER_SET_MOTD`                       | 196 (Administrator Commands)               |
| 734 | Command: server shutdown                       | `RBAC_PERM_COMMAND_SERVER_SHUTDOWN`                       | 196 (Administrator Commands)               |
| 735 | Command: server shutdown cancel                | `RBAC_PERM_COMMAND_SERVER_SHUTDOWN_CANCEL`                | 196 (Administrator Commands)               |
| 736 | Command: server motd                           | `RBAC_PERM_COMMAND_SERVER_MOTD`                           | 196 (Administrator Commands)               |
| 737 | Command: tele                                  | `RBAC_PERM_COMMAND_TELE`                                  | 197 (Gamemaster Commands)                  |
| 738 | Command: tele add                              | `RBAC_PERM_COMMAND_TELE_ADD`                              | 197 (Gamemaster Commands)                  |
| 739 | Command: tele del                              | `RBAC_PERM_COMMAND_TELE_DEL`                              | 197 (Gamemaster Commands)                  |
| 740 | Command: tele name                             | `RBAC_PERM_COMMAND_TELE_NAME`                             | 197 (Gamemaster Commands)                  |
| 741 | Command: tele group                            | `RBAC_PERM_COMMAND_TELE_GROUP`                            | 197 (Gamemaster Commands)                  |
| 742 | Command: ticket                                | `RBAC_PERM_COMMAND_TICKET`                                | 198 (Moderator Commands)                   |
| 743 | Command: ticket assign                         | `RBAC_PERM_COMMAND_TICKET_ASSIGN`                         | 198 (Moderator Commands)                   |
| 744 | Command: ticket close                          | `RBAC_PERM_COMMAND_TICKET_CLOSE`                          | 198 (Moderator Commands)                   |
| 745 | Command: ticket closedlist                     | `RBAC_PERM_COMMAND_TICKET_CLOSEDLIST`                     | 198 (Moderator Commands)                   |
| 746 | Command: ticket comment                        | `RBAC_PERM_COMMAND_TICKET_COMMENT`                        | 198 (Moderator Commands)                   |
| 747 | Command: ticket complete                       | `RBAC_PERM_COMMAND_TICKET_COMPLETE`                       | 198 (Moderator Commands)                   |
| 748 | Command: ticket delete                         | `RBAC_PERM_COMMAND_TICKET_DELETE`                         | 196 (Administrator Commands)               |
| 749 | Command: ticket escalate                       | `RBAC_PERM_COMMAND_TICKET_ESCALATE`                       | 198 (Moderator Commands)                   |
| 750 | Command: ticket escalatedlist                  | `RBAC_PERM_COMMAND_TICKET_ESCALATEDLIST`                  | 198 (Moderator Commands)                   |
| 751 | Command: ticket list                           | `RBAC_PERM_COMMAND_TICKET_LIST`                           | 198 (Moderator Commands)                   |
| 752 | Command: ticket onlinelist                     | `RBAC_PERM_COMMAND_TICKET_ONLINELIST`                     | 198 (Moderator Commands)                   |
| 753 | Command: ticket reset                          | `RBAC_PERM_COMMAND_TICKET_RESET`                          | 196 (Administrator Commands)               |
| 754 | Command: ticket response                       | `RBAC_PERM_COMMAND_TICKET_RESPONSE`                       | 198 (Moderator Commands)                   |
| 755 | Command: ticket response append                | `RBAC_PERM_COMMAND_TICKET_RESPONSE_APPEND`                | 198 (Moderator Commands)                   |
| 756 | Command: ticket response appendln              | `RBAC_PERM_COMMAND_TICKET_RESPONSE_APPENDLN`              | 198 (Moderator Commands)                   |
| 757 | Command: ticket togglesystem                   | `RBAC_PERM_COMMAND_TICKET_TOGGLESYSTEM`                   | 196 (Administrator Commands)               |
| 758 | Command: ticket unassign                       | `RBAC_PERM_COMMAND_TICKET_UNASSIGN`                       | 198 (Moderator Commands)                   |
| 759 | Command: ticket viewid                         | `RBAC_PERM_COMMAND_TICKET_VIEWID`                         | 198 (Moderator Commands)                   |
| 760 | Command: ticket viewname                       | `RBAC_PERM_COMMAND_TICKET_VIEWNAME`                       | 198 (Moderator Commands)                   |
| 762 | Command: titles add                            | `RBAC_PERM_COMMAND_TITLES_ADD`                            | 197 (Gamemaster Commands)                  |
| 763 | Command: titles current                        | `RBAC_PERM_COMMAND_TITLES_CURRENT`                        | 197 (Gamemaster Commands)                  |
| 764 | Command: titles remove                         | `RBAC_PERM_COMMAND_TITLES_REMOVE`                         | 197 (Gamemaster Commands)                  |
| 766 | Command: titles set mask                       | `RBAC_PERM_COMMAND_TITLES_SET_MASK`                       | 197 (Gamemaster Commands)                  |
| 767 | Command: wp                                    | `RBAC_PERM_COMMAND_WP`                                    | 197 (Gamemaster Commands)                  |
| 768 | Command: wp add                                | `RBAC_PERM_COMMAND_WP_ADD`                                | 197 (Gamemaster Commands)                  |
| 769 | Command: wp event                              | `RBAC_PERM_COMMAND_WP_EVENT`                              | 197 (Gamemaster Commands)                  |
| 770 | Command: wp load                               | `RBAC_PERM_COMMAND_WP_LOAD`                               | 197 (Gamemaster Commands)                  |
| 771 | Command: wp modify                             | `RBAC_PERM_COMMAND_WP_MODIFY`                             | 197 (Gamemaster Commands)                  |
| 772 | Command: wp unload                             | `RBAC_PERM_COMMAND_WP_UNLOAD`                             | 197 (Gamemaster Commands)                  |
| 773 | Command: wp reload                             | `RBAC_PERM_COMMAND_WP_RELOAD`                             | 196 (Administrator Commands)               |
| 774 | Command: wp show                               | `RBAC_PERM_COMMAND_WP_SHOW`                               | 197 (Gamemaster Commands)                  |
| 777 | Command: mailbox                               | `RBAC_PERM_COMMAND_MAILBOX`                               | 196 (Administrator Commands)               |
| 779 | Command: ahbot items                           | `RBAC_PERM_COMMAND_AHBOT_ITEMS`                           | 196 (Administrator Commands)               |
| 780 | Command: ahbot items gray                      | `RBAC_PERM_COMMAND_AHBOT_ITEMS_GRAY`                      | 196 (Administrator Commands)               |
| 781 | Command: ahbot items white                     | `RBAC_PERM_COMMAND_AHBOT_ITEMS_WHITE`                     | 196 (Administrator Commands)               |
| 782 | Command: ahbot items green                     | `RBAC_PERM_COMMAND_AHBOT_ITEMS_GREEN`                     | 196 (Administrator Commands)               |
| 783 | Command: ahbot items blue                      | `RBAC_PERM_COMMAND_AHBOT_ITEMS_BLUE`                      | 196 (Administrator Commands)               |
| 784 | Command: ahbot items purple                    | `RBAC_PERM_COMMAND_AHBOT_ITEMS_PURPLE`                    | 196 (Administrator Commands)               |
| 785 | Command: ahbot items orange                    | `RBAC_PERM_COMMAND_AHBOT_ITEMS_ORANGE`                    | 196 (Administrator Commands)               |
| 786 | Command: ahbot items yellow                    | `RBAC_PERM_COMMAND_AHBOT_ITEMS_YELLOW`                    | 196 (Administrator Commands)               |
| 787 | Command: ahbot ratio                           | `RBAC_PERM_COMMAND_AHBOT_RATIO`                           | 196 (Administrator Commands)               |
| 788 | Command: ahbot ratio alliance                  | `RBAC_PERM_COMMAND_AHBOT_RATIO_ALLIANCE`                  | 196 (Administrator Commands)               |
| 789 | Command: ahbot ratio horde                     | `RBAC_PERM_COMMAND_AHBOT_RATIO_HORDE`                     | 196 (Administrator Commands)               |
| 790 | Command: ahbot ratio neutral                   | `RBAC_PERM_COMMAND_AHBOT_RATIO_NEUTRAL`                   | 196 (Administrator Commands)               |
| 791 | Command: ahbot rebuild                         | `RBAC_PERM_COMMAND_AHBOT_REBUILD`                         | 196 (Administrator Commands)               |
| 792 | Command: ahbot reload                          | `RBAC_PERM_COMMAND_AHBOT_RELOAD`                          | 196 (Administrator Commands)               |
| 793 | Command: ahbot status                          | `RBAC_PERM_COMMAND_AHBOT_STATUS`                          | 196 (Administrator Commands)               |
| 794 | Command: guild info                            | `RBAC_PERM_COMMAND_GUILD_INFO`                            | 197 (Gamemaster Commands)                  |
| 795 | Command: instance setbossstate                 | `RBAC_PERM_COMMAND_INSTANCE_SET_BOSS_STATE`               | 197 (Gamemaster Commands)                  |
| 796 | Command: instance getbossstate                 | `RBAC_PERM_COMMAND_INSTANCE_GET_BOSS_STATE`               | 197 (Gamemaster Commands)                  |
| 797 | Command: pvpstats                              | `RBAC_PERM_COMMAND_PVPSTATS`                              | 199 (Player Commands)                      |
| 798 | Command: modify xp                             | `RBAC_PERM_COMMAND_MODIFY_XP`                             | 194 (Moderator), 197 (Gamemaster Commands) |
| 837 | Command: npc evade                             | `RBAC_PERM_COMMAND_NPC_EVADE`                             | 197 (Gamemaster Commands)                  |
| 838 | Command: pet level                             | `RBAC_PERM_COMMAND_PET_LEVEL`                             | 197 (Gamemaster Commands)                  |
| 839 | Command: server shutdown force                 | `RBAC_PERM_COMMAND_SERVER_SHUTDOWN_FORCE`                 | 196 (Administrator Commands)               |
| 840 | Command: server restart force                  | `RBAC_PERM_COMMAND_SERVER_RESTART_FORCE`                  | 196 (Administrator Commands)               |
| 841 | Command: neargraveyard                         | `RBAC_PERM_COMMAND_NEARGRAVEYARD`                         | 197 (Gamemaster Commands)                  |
| 843 | Command: reload quest_greeting                 | `RBAC_PERM_COMMAND_RELOAD_QUEST_GREETING`                 | 196 (Administrator Commands)               |
| 856 | Command: npc spawngroup                        | `RBAC_PERM_COMMAND_NPC_SPAWNGROUP`                        | 197 (Gamemaster Commands)                  |
| 857 | Command: npc despawngroup                      | `RBAC_PERM_COMMAND_NPC_DESPAWNGROUP`                      | 197 (Gamemaster Commands)                  |
| 858 | Command: gobject spawngroup                    | `RBAC_PERM_COMMAND_GOBJECT_SPAWNGROUP`                    | 197 (Gamemaster Commands)                  |
| 859 | Command: gobject despawngroup                  | `RBAC_PERM_COMMAND_GOBJECT_DESPAWNGROUP`                  | 197 (Gamemaster Commands)                  |
| 860 | Command: list respawns                         | `RBAC_PERM_COMMAND_LIST_RESPAWNS`                         | 197 (Gamemaster Commands)                  |
| 861 | Command: group set                             | `RBAC_PERM_COMMAND_GROUP_SET`                             | 197 (Gamemaster Commands)                  |
| 862 | Command: group set assistant                   | `RBAC_PERM_COMMAND_GROUP_ASSISTANT`                       | 197 (Gamemaster Commands)                  |
| 863 | Command: group set maintank                    | `RBAC_PERM_COMMAND_GROUP_MAINTANK`                        | 197 (Gamemaster Commands)                  |
| 864 | Command: group set mainassist                  | `RBAC_PERM_COMMAND_GROUP_MAINASSIST`                      | 197 (Gamemaster Commands)                  |
| 865 | Command: npc showloot                          | `RBAC_PERM_COMMAND_NPC_SHOWLOOT`                          | 197 (Gamemaster Commands)                  |
| 866 | Command: list spawnpoints                      | `RBAC_PERM_COMMAND_LIST_SPAWNPOINTS`                      | 196 (Administrator Commands)               |
| 867 | Command: reload quest_greeting_locale          | `RBAC_PERM_COMMAND_RELOAD_QUEST_GREETING_LOCALE`          | 196 (Administrator Commands)               |
| 868 | Command: group revive                          | `RBAC_PERM_COMMAND_GROUP_REVIVE`                          | 197 (Gamemaster Commands)                  |
| 872 | Command: server debug                          | `RBAC_PERM_COMMAND_SERVER_DEBUG`                          | 196 (Administrator Commands)               |
| 873 | Command: reload creature_movement_override     | `RBAC_PERM_COMMAND_RELOAD_CREATURE_MOVEMENT_OVERRIDE`     | 196 (Administrator Commands)               |
| 874 | Command: settings announcer                    | `RBAC_PERM_COMMAND_SETTINGS_ANNOUNCER`                    | 197 (Gamemaster Commands)                  |
| 875 | Command: lookup map id                         | `RBAC_PERM_COMMAND_LOOKUP_MAP_ID`                         | 197 (Gamemaster Commands)                  |
| 876 | Command: lookup item id                        | `RBAC_PERM_COMMAND_LOOKUP_ITEM_ID`                        | 197 (Gamemaster Commands)                  |
| 877 | Command: lookup quest id                       | `RBAC_PERM_COMMAND_LOOKUP_QUEST_ID`                       | 197 (Gamemaster Commands)                  |
| 880 | Command: pdump copy                            | `RBAC_PERM_COMMAND_PDUMP_COPY`                            | 196 (Administrator Commands)               |
| 881 | Command: reload vehicle_template               | `RBAC_PERM_COMMAND_RELOAD_VEHICLE_TEMPLATE`               | 196 (Administrator Commands)               |
| 884 | Command: bg start                              | `RBAC_PERM_COMMAND_BG_START`                              | 197 (Gamemaster Commands)                  |
| 885 | Command: bg stop                               | `RBAC_PERM_COMMAND_BG_STOP`                               | 197 (Gamemaster Commands)                  |
| 886 | Command: item restore                          | `RBAC_PERM_COMMAND_ITEM_RESTORE`                          | 196 (Administrator Commands)               |
| 887 | Command: item restore list                     | `RBAC_PERM_COMMAND_ITEM_RESTORE_LIST`                     | 196 (Administrator Commands)               |
| 888 | Command: item refund                           | `RBAC_PERM_COMMAND_ITEM_REFUND`                           | 196 (Administrator Commands)               |
| 889 | Command: commentator                           | `RBAC_PERM_COMMAND_COMMENTATOR`                           | 197 (Gamemaster Commands)                  |
| 890 | Command: skirmish                              | `RBAC_PERM_COMMAND_SKIRMISH`                              | 197 (Gamemaster Commands)                  |
| 891 | Command: string                                | `RBAC_PERM_COMMAND_STRING`                                | 196 (Administrator Commands)               |
| 892 | Command: opendoor                              | `RBAC_PERM_COMMAND_OPENDOOR`                              | 197 (Gamemaster Commands)                  |
| 893 | Command: beastmaster                           | `RBAC_PERM_COMMAND_BEASTMASTER`                           | 197 (Gamemaster Commands)                  |
| 894 | Command: packetlog                             | `RBAC_PERM_COMMAND_PACKETLOG`                             | 196 (Administrator Commands)               |
| 895 | Command: aura stack                            | `RBAC_PERM_COMMAND_AURA_STACK`                            | 197 (Gamemaster Commands)                  |
| 896 | Command: respawn all                           | `RBAC_PERM_COMMAND_RESPAWN_ALL`                           | 196 (Administrator Commands)               |
| 897 | Command: gear repair                           | `RBAC_PERM_COMMAND_GEAR_REPAIR`                           | 197 (Gamemaster Commands)                  |
| 898 | Command: gear stats                            | `RBAC_PERM_COMMAND_GEAR_STATS`                            | 199 (Player Commands)                      |
| 899 | Command: spect                                 | `RBAC_PERM_COMMAND_SPECT`                                 | 199 (Player Commands)                      |
| 900 | Command: spect version                         | `RBAC_PERM_COMMAND_SPECT_VERSION`                         | 199 (Player Commands)                      |
| 901 | Command: spect reset                           | `RBAC_PERM_COMMAND_SPECT_RESET`                           | 199 (Player Commands)                      |
| 902 | Command: spect spectate                        | `RBAC_PERM_COMMAND_SPECT_SPECTATE`                        | 199 (Player Commands)                      |
| 903 | Command: spect watch                           | `RBAC_PERM_COMMAND_SPECT_WATCH`                           | 199 (Player Commands)                      |
| 904 | Command: spect leave                           | `RBAC_PERM_COMMAND_SPECT_LEAVE`                           | 199 (Player Commands)                      |
| 905 | Command: arena season state                    | `RBAC_PERM_COMMAND_ARENA_SEASON`                          | 196 (Administrator Commands)               |
| 906 | Command: arena season reward                   | `RBAC_PERM_COMMAND_ARENA_SEASON_REWARD`                   | 196 (Administrator Commands)               |
| 907 | Command: arena season deleteteams              | `RBAC_PERM_COMMAND_ARENA_SEASON_DELETETEAMS`              | 196 (Administrator Commands)               |
| 908 | Command: arena season start                    | `RBAC_PERM_COMMAND_ARENA_SEASON_START`                    | 196 (Administrator Commands)               |
| 909 | Command: character check bank                  | `RBAC_PERM_COMMAND_CHARACTER_CHECK_BANK`                  | 197 (Gamemaster Commands)                  |
| 910 | Command: character check bag                   | `RBAC_PERM_COMMAND_CHARACTER_CHECK_BAG`                   | 197 (Gamemaster Commands)                  |
| 911 | Command: character check profession            | `RBAC_PERM_COMMAND_CHARACTER_CHECK_PROFESSION`            | 197 (Gamemaster Commands)                  |
| 912 | Command: gobject load                          | `RBAC_PERM_COMMAND_GOBJECT_LOAD`                          | 196 (Administrator Commands)               |
| 913 | Command: bf queue                              | `RBAC_PERM_COMMAND_BF_QUEUE`                              | 197 (Gamemaster Commands)                  |
| 914 | Command: pet list                              | `RBAC_PERM_COMMAND_PET_LIST`                              | 198 (Moderator Commands)                   |
| 915 | Command: pet delete                            | `RBAC_PERM_COMMAND_PET_DELETE`                            | 196 (Administrator Commands)               |
| 916 | Command: respawn creature guid                 | `RBAC_PERM_COMMAND_RESPAWN_CREATURE_GUID`                 | 197 (Gamemaster Commands)                  |
| 917 | Command: respawn gameobject guid               | `RBAC_PERM_COMMAND_RESPAWN_GAMEOBJECT_GUID`               | 197 (Gamemaster Commands)                  |
| 918 | Command: respawn creature entry                | `RBAC_PERM_COMMAND_RESPAWN_CREATURE_ENTRY`                | 197 (Gamemaster Commands)                  |
| 919 | Command: respawn gameobject entry              | `RBAC_PERM_COMMAND_RESPAWN_GAMEOBJECT_ENTRY`              | 197 (Gamemaster Commands)                  |
| 920 | Command: debug info                            | `RBAC_PERM_COMMAND_DEBUG_INFO`                            | 300 (Command: debug)                       |
| 921 | Command: debug cosmetic                        | `RBAC_PERM_COMMAND_DEBUG_COSMETIC`                        | 300 (Command: debug)                       |
| 922 | Command: pet rename                            | `RBAC_PERM_COMMAND_PET_RENAME`                            | 196 (Administrator Commands)               |
| 923 | Command: chatfilter list                       | `RBAC_PERM_COMMAND_CHATFILTER_LIST`                       | 197 (Gamemaster Commands)                  |
| 924 | Command: chatfilter add                        | `RBAC_PERM_COMMAND_CHATFILTER_ADD`                        | 197 (Gamemaster Commands)                  |
| 925 | Command: chatfilter remove                     | `RBAC_PERM_COMMAND_CHATFILTER_REMOVE`                     | 197 (Gamemaster Commands)                  |
| 926 | Command: autobroadcast list                    | `RBAC_PERM_COMMAND_AUTOBROADCAST_LIST`                    | 197 (Gamemaster Commands)                  |
| 927 | Command: autobroadcast add                     | `RBAC_PERM_COMMAND_AUTOBROADCAST_ADD`                     | 196 (Administrator Commands)               |
| 928 | Command: autobroadcast locale                  | `RBAC_PERM_COMMAND_AUTOBROADCAST_LOCALE`                  | 196 (Administrator Commands)               |
| 929 | Command: autobroadcast remove                  | `RBAC_PERM_COMMAND_AUTOBROADCAST_REMOVE`                  | 196 (Administrator Commands)               |
| 930 | Command: mail list                             | `RBAC_PERM_COMMAND_MAIL_LIST`                             | 197 (Gamemaster Commands)                  |
| 931 | Command: mail return                           | `RBAC_PERM_COMMAND_MAIL_RETURN`                           | 197 (Gamemaster Commands)                  |
| 932 | Command: npc load                              | `RBAC_PERM_COMMAND_NPC_LOAD`                              | 196 (Administrator Commands)               |
| 933 | Command: pool info                             | `RBAC_PERM_COMMAND_POOL_INFO`                             | 197 (Gamemaster Commands)                  |
| 934 | Command: pool lookup                           | `RBAC_PERM_COMMAND_POOL_LOOKUP`                           | 197 (Gamemaster Commands)                  |
| 935 | Command: spellinfo attributes                  | `RBAC_PERM_COMMAND_SPELLINFO_ATTRIBUTES`                  | 197 (Gamemaster Commands)                  |
| 936 | Command: spellinfo effects                     | `RBAC_PERM_COMMAND_SPELLINFO_EFFECTS`                     | 197 (Gamemaster Commands)                  |
| 937 | Command: spellinfo targets                     | `RBAC_PERM_COMMAND_SPELLINFO_TARGETS`                     | 197 (Gamemaster Commands)                  |
| 938 | Command: spellinfo all                         | `RBAC_PERM_COMMAND_SPELLINFO_ALL`                         | 197 (Gamemaster Commands)                  |
| 939 | Command: server set security                   | `RBAC_PERM_COMMAND_SERVER_SET_SECURITY`                   | 196 (Administrator Commands)               |
| 940 | Command: group invites                         | `RBAC_PERM_COMMAND_GROUP_INVITES`                         | 197 (Gamemaster Commands)                  |
| 941 | Command: account flag                          | `RBAC_PERM_COMMAND_ACCOUNT_FLAG`                          | 197 (Gamemaster Commands)                  |
| 942 | Command: account flag list                     | `RBAC_PERM_COMMAND_ACCOUNT_FLAG_LIST`                     | 197 (Gamemaster Commands)                  |
| 943 | Command: account flag add                      | `RBAC_PERM_COMMAND_ACCOUNT_FLAG_ADD`                      | 196 (Administrator Commands)               |
| 944 | Command: account flag remove                   | `RBAC_PERM_COMMAND_ACCOUNT_FLAG_REMOVE`                   | 196 (Administrator Commands)               |
| 945 | Command: account info                          | `RBAC_PERM_COMMAND_ACCOUNT_INFO`                          | 197 (Gamemaster Commands)                  |

</details>

<!-- rbac-default-data:end -->
