# rbac\_linked\_permissions

[<-Back-to:Auth](database-auth)

**The \`rbac\_linked\_permissions\` table**

This table defines the parent-child relationships between permissions. When a permission (typically a role) is granted, all of its linked permissions are also granted. This is how role inheritance works in the [RBAC](rbac) system.

**Table: rbac\_linked\_permissions's Structure**

| Field                 | Type |          | Null | Key | Default | Extra | Comment              |
| :-------------------- | :--- | :------- | :--: | :-: | :-----: | :---: | :------------------- |
| [id](#id)             | INT  | UNSIGNED | NO   | PRI |         |       | Permission id        |
| [linkedId](#linkedid) | INT  | UNSIGNED | NO   | PRI |         |       | Linked Permission id |

Both fields have a foreign key to [rbac_permissions.id](rbac_permissions#id) with `ON DELETE CASCADE`.

**Description of the table's fields**

### id

The parent permission (role) that contains other permissions. Typically one of the role IDs:

| ID | Role |
| -- | ---- |
| 192 | Administrator |
| 193 | Gamemaster |
| 194 | Moderator |
| 195 | Player |
| 196 | Admin Commands |
| 197 | GM Commands |
| 198 | Mod Commands |
| 199 | Player Commands |

### linkedId

The child permission that is granted when the parent (`id`) is granted. Can be any permission from [rbac_permissions](rbac_permissions), including another role — this is how the hierarchy chains together (e.g. Administrator 192 links to Gamemaster 193, which links to Moderator 194, and so on).

Linked permissions are expanded recursively during [permission resolution](rbac#permission-resolution).

<!-- rbac-default-data:start -->

**Default links**

These are the links a clean AzerothCore database comes with, grouped by the parent permission. *Comment* is the name of the linked permission in [rbac_permissions](rbac_permissions).

<button type="button" class="details-toggle" onclick="var d=document.querySelectorAll('#git-wiki-content details'),o=!Array.prototype.every.call(d,function(e){return e.open});d.forEach(function(e){e.open=o});this.textContent=o?'Collapse all':'Expand all'">Expand all</button>

<details>
<summary id="role-192">192 - Role: Sec Level Administrator</summary>

| id  | linkedId | Comment                                              |
| :-- | :------- | :--------------------------------------------------- |
| 192 | 7        | Skip idle connection check                           |
| 192 | 21       | Skip reset talents when used more than allowed check |
| 192 | 42       | Allows to use CMSG_WORLD_TELEPORT opcode             |
| 192 | 43       | Allows to use CMSG_WHOIS opcode                      |
| 192 | 193      | Role: Sec Level Gamemaster                           |
| 192 | 196      | Role: Administrator Commands                         |

</details>

<details>
<summary id="role-193">193 - Role: Sec Level Gamemaster</summary>

| id  | linkedId | Comment                                         |
| :-- | :------- | :---------------------------------------------- |
| 193 | 45       | Join channels without announce                  |
| 193 | 48       | Enable IP, Last Login and EMail output in pinfo |
| 193 | 52       | No battleground deserter debuff                 |
| 193 | 53       | Can be AFK on the battleground                  |
| 193 | 194      | Role: Sec Level Moderator                       |
| 193 | 197      | Role: Gamemaster Commands                       |

</details>

<details>
<summary id="role-194">194 - Role: Sec Level Moderator</summary>

| id  | linkedId | Comment                                                        |
| :-- | :------- | :------------------------------------------------------------- |
| 194 | 1        | Instant logout                                                 |
| 194 | 2        | Skip Queue                                                     |
| 194 | 9        | Cannot earn realm first achievements                           |
| 194 | 11       | Log GM trades                                                  |
| 194 | 13       | Skip Instance required bosses check                            |
| 194 | 14       | Skip character creation team mask check                        |
| 194 | 15       | Skip character creation class mask check                       |
| 194 | 16       | Skip character creation race mask check                        |
| 194 | 17       | Skip character creation reserved name check                    |
| 194 | 18       | Skip character creation death knight min level check           |
| 194 | 19       | Skip needed requirements to use channel check                  |
| 194 | 20       | Skip disable map check                                         |
| 194 | 22       | Skip spam chat check                                           |
| 194 | 23       | Skip over-speed ping check                                     |
| 194 | 25       | Allow say chat between factions                                |
| 194 | 26       | Allow channel chat between factions                            |
| 194 | 27       | Two side mail interaction                                      |
| 194 | 28       | See two side who list                                          |
| 194 | 29       | Add friends of other faction                                   |
| 194 | 30       | Save character without delay with .save command                |
| 194 | 31       | Use params with .unstuck command                               |
| 194 | 32       | Can be assigned tickets with .assign ticket command            |
| 194 | 33       | Notify if a command was not found                              |
| 194 | 34       | Check if should appear in list using .gm ingame command        |
| 194 | 35       | See all security levels with who command                       |
| 194 | 36       | Filter whispers                                                |
| 194 | 37       | Use staff badge in chat                                        |
| 194 | 38       | Resurrect with full Health Points                              |
| 194 | 39       | Restore saved gm setting states                                |
| 194 | 40       | Allows to add a gm to friend list                              |
| 194 | 41       | Use Config option START_GM_LEVEL to assign new character level |
| 194 | 44       | Receive global GM messages/texts                               |
| 194 | 46       | Change channel settings without being channel moderator        |
| 194 | 47       | Can ignore lower security checks                               |
| 194 | 51       | Allow trading between factions                                 |
| 194 | 195      | Role: Sec Level Player                                         |
| 194 | 198      | Role: Moderator Commands                                       |
| 194 | 632      | Command: mutehistory                                           |
| 194 | 798      | Command: modify xp                                             |

</details>

<details>
<summary id="role-195">195 - Role: Sec Level Player</summary>

| id  | linkedId | Comment                                                       |
| :-- | :------- | :------------------------------------------------------------ |
| 195 | 3        | Join Normal Battleground                                      |
| 195 | 4        | Join Random Battleground                                      |
| 195 | 5        | Join Arenas                                                   |
| 195 | 6        | Join Dungeon Finder                                           |
| 195 | 24       | Two side faction characters on the same account               |
| 195 | 49       | Forces to enter the email for confirmation on password change |
| 195 | 199      | Role: Player Commands                                         |

</details>

<details>
<summary id="role-196">196 - Role: Administrator Commands</summary>

| id  | linkedId | Comment                                        |
| :-- | :------- | :--------------------------------------------- |
| 196 | 200      | Command: rbac                                  |
| 196 | 201      | Command: rbac account                          |
| 196 | 202      | Command: rbac account list                     |
| 196 | 203      | Command: rbac account grant                    |
| 196 | 204      | Command: rbac account deny                     |
| 196 | 205      | Command: rbac account revoke                   |
| 196 | 206      | Command: rbac list                             |
| 196 | 219      | Command: account create                        |
| 196 | 220      | Command: account delete                        |
| 196 | 224      | Command: account onlinelist                    |
| 196 | 226      | Command: account set                           |
| 196 | 227      | Command: account set addon                     |
| 196 | 228      | Command: account set gmlevel                   |
| 196 | 229      | Command: account set password                  |
| 196 | 258      | Command: bf start                              |
| 196 | 259      | Command: bf stop                               |
| 196 | 260      | Command: bf switch                             |
| 196 | 261      | Command: bf timer                              |
| 196 | 262      | Command: bf enable                             |
| 196 | 265      | Command: account set sec email                 |
| 196 | 266      | Command: account set sec regmail               |
| 196 | 278      | Command: character deleted delete              |
| 196 | 281      | Command: character deleted old                 |
| 196 | 282      | Command: character erase                       |
| 196 | 289      | Command: pdump load                            |
| 196 | 290      | Command: pdump write                           |
| 196 | 350      | Command: disable add achievement_criteria      |
| 196 | 351      | Command: disable add battleground              |
| 196 | 352      | Command: disable add map                       |
| 196 | 353      | Command: disable add mmap                      |
| 196 | 354      | Command: disable add outdoorpvp                |
| 196 | 355      | Command: disable add quest                     |
| 196 | 356      | Command: disable add spell                     |
| 196 | 357      | Command: disable add vmap                      |
| 196 | 359      | Command: disable remove achievement_criteria   |
| 196 | 360      | Command: disable remove battleground           |
| 196 | 361      | Command: disable remove map                    |
| 196 | 362      | Command: disable remove mmap                   |
| 196 | 363      | Command: disable remove outdoorpvp             |
| 196 | 364      | Command: disable remove quest                  |
| 196 | 365      | Command: disable remove spell                  |
| 196 | 366      | Command: disable remove vmap                   |
| 196 | 463      | Command: channel                               |
| 196 | 464      | Command: channel set                           |
| 196 | 465      | Command: channel set ownership                 |
| 196 | 503      | Command: flusharenapoints                      |
| 196 | 511      | Command: linkgrave                             |
| 196 | 524      | Command: saveall                               |
| 196 | 607      | Command: reload                                |
| 196 | 608      | Command: reload access_requirement             |
| 196 | 609      | Command: reload achievement_criteria_data      |
| 196 | 610      | Command: reload achievement_reward             |
| 196 | 611      | Command: reload all                            |
| 196 | 612      | Command: reload all achievement                |
| 196 | 613      | Command: reload all area                       |
| 196 | 614      | Command: reload broadcast_text                 |
| 196 | 615      | Command: reload all gossips                    |
| 196 | 616      | Command: reload all item                       |
| 196 | 617      | Command: reload all locales                    |
| 196 | 618      | Command: reload all loot                       |
| 196 | 619      | Command: reload all npc                        |
| 196 | 620      | Command: reload all quest                      |
| 196 | 621      | Command: reload all scripts                    |
| 196 | 622      | Command: reload all spell                      |
| 196 | 623      | Command: reload areatrigger_involvedrelation   |
| 196 | 624      | Command: reload areatrigger_tavern             |
| 196 | 625      | Command: reload areatrigger_teleport           |
| 196 | 626      | Command: reload auctions                       |
| 196 | 627      | Command: reload autobroadcast                  |
| 196 | 629      | Command: reload conditions                     |
| 196 | 630      | Command: reload config                         |
| 196 | 631      | Command: reload battleground_template          |
| 196 | 633      | Command: reload creature_linked_respawn        |
| 196 | 634      | Command: reload creature_loot_template         |
| 196 | 635      | Command: reload creature_onkill_reputation     |
| 196 | 636      | Command: reload creature_questender            |
| 196 | 637      | Command: reload creature_queststarter          |
| 196 | 638      | Command: reload creature_summon_groups         |
| 196 | 639      | Command: reload creature_template              |
| 196 | 640      | Command: reload creature_text                  |
| 196 | 641      | Command: reload disables                       |
| 196 | 642      | Command: reload disenchant_loot_template       |
| 196 | 643      | Command: reload event_scripts                  |
| 196 | 644      | Command: reload fishing_loot_template          |
| 196 | 645      | Command: reload graveyard_zone                 |
| 196 | 646      | Command: reload game_tele                      |
| 196 | 647      | Command: reload gameobject_questender          |
| 196 | 648      | Command: reload gameobject_quest_loot_template |
| 196 | 649      | Command: reload gameobject_queststarter        |
| 196 | 650      | Command: reload gm_tickets                     |
| 196 | 651      | Command: reload gossip_menu                    |
| 196 | 652      | Command: reload gossip_menu_option             |
| 196 | 653      | Command: reload item_enchantment_template      |
| 196 | 654      | Command: reload item_loot_template             |
| 196 | 655      | Command: reload item_set_names                 |
| 196 | 656      | Command: reload lfg_dungeon_rewards            |
| 196 | 657      | Command: reload achievement_reward_locale      |
| 196 | 658      | Command: reload creature_template_locale       |
| 196 | 659      | Command: reload creature_text_locale           |
| 196 | 660      | Command: reload gameobject_template_locale     |
| 196 | 661      | Command: reload gossip_menu_option_locale      |
| 196 | 662      | Command: reload item_template_locale           |
| 196 | 663      | Command: reload item_set_name_locale           |
| 196 | 664      | Command: reload npc_text_locale                |
| 196 | 665      | Command: reload page_text_locale               |
| 196 | 666      | Command: reload points_of_interest_locale      |
| 196 | 667      | Command: reload quest_template_locale          |
| 196 | 668      | Command: reload mail_level_reward              |
| 196 | 669      | Command: reload mail_loot_template             |
| 196 | 670      | Command: reload milling_loot_template          |
| 196 | 671      | Command: reload npc_spellclick_spells          |
| 196 | 672      | Command: reload trainer                        |
| 196 | 673      | Command: reload npc_vendor                     |
| 196 | 674      | Command: reload page_text                      |
| 196 | 675      | Command: reload pickpocketing_loot_template    |
| 196 | 676      | Command: reload points_of_interest             |
| 196 | 677      | Command: reload prospecting_loot_template      |
| 196 | 678      | Command: reload quest_poi                      |
| 196 | 679      | Command: reload quest_template                 |
| 196 | 680      | Command: reload rbac                           |
| 196 | 681      | Command: reload reference_loot_template        |
| 196 | 682      | Command: reload reserved_name                  |
| 196 | 683      | Command: reload reputation_reward_rate         |
| 196 | 684      | Command: reload reputation_spillover_template  |
| 196 | 685      | Command: reload skill_discovery_template       |
| 196 | 686      | Command: reload skill_extra_item_template      |
| 196 | 687      | Command: reload skill_fishing_base_level       |
| 196 | 688      | Command: reload skinning_loot_template         |
| 196 | 689      | Command: reload smart_scripts                  |
| 196 | 690      | Command: reload spell_required                 |
| 196 | 691      | Command: reload spell_area                     |
| 196 | 692      | Command: reload spell_bonus_data               |
| 196 | 693      | Command: reload spell_group                    |
| 196 | 694      | Command: reload spell_learn_spell              |
| 196 | 695      | Command: reload spell_loot_template            |
| 196 | 696      | Command: reload spell_linked_spell             |
| 196 | 697      | Command: reload spell_pet_auras                |
| 196 | 698      | Command: character changeaccount               |
| 196 | 699      | Command: reload spell_proc                     |
| 196 | 701      | Command: reload spell_target_position          |
| 196 | 702      | Command: reload spell_threats                  |
| 196 | 703      | Command: reload spell_group_stack_rules        |
| 196 | 704      | Command: reload acore_string                   |
| 196 | 706      | Command: reload waypoint_scripts               |
| 196 | 707      | Command: reload waypoint_data                  |
| 196 | 708      | Command: reload vehicle_accessory              |
| 196 | 709      | Command: reload vehicle_template_accessory     |
| 196 | 710      | Command: reset                                 |
| 196 | 711      | Command: reset achievements                    |
| 196 | 712      | Command: reset honor                           |
| 196 | 713      | Command: reset level                           |
| 196 | 714      | Command: reset spells                          |
| 196 | 715      | Command: reset stats                           |
| 196 | 716      | Command: reset talents                         |
| 196 | 717      | Command: reset all                             |
| 196 | 718      | Command: server                                |
| 196 | 719      | Command: server corpses                        |
| 196 | 720      | Command: server exit                           |
| 196 | 721      | Command: server idlerestart                    |
| 196 | 722      | Command: server idlerestart cancel             |
| 196 | 723      | Command: server idleshutdown                   |
| 196 | 724      | Command: server idleshutdown cancel            |
| 196 | 726      | Command: server plimit                         |
| 196 | 727      | Command: server restart                        |
| 196 | 728      | Command: server restart cancel                 |
| 196 | 729      | Command: server set                            |
| 196 | 730      | Command: server set closed                     |
| 196 | 731      | Command: server set difftime                   |
| 196 | 732      | Command: server set loglevel                   |
| 196 | 733      | Command: server set motd                       |
| 196 | 734      | Command: server shutdown                       |
| 196 | 735      | Command: server shutdown cancel                |
| 196 | 736      | Command: server motd                           |
| 196 | 748      | Command: ticket delete                         |
| 196 | 753      | Command: ticket reset                          |
| 196 | 757      | Command: ticket togglesystem                   |
| 196 | 773      | Command: wp reload                             |
| 196 | 777      | Command: mailbox                               |
| 196 | 779      | Command: ahbot items                           |
| 196 | 780      | Command: ahbot items gray                      |
| 196 | 781      | Command: ahbot items white                     |
| 196 | 782      | Command: ahbot items green                     |
| 196 | 783      | Command: ahbot items blue                      |
| 196 | 784      | Command: ahbot items purple                    |
| 196 | 785      | Command: ahbot items orange                    |
| 196 | 786      | Command: ahbot items yellow                    |
| 196 | 787      | Command: ahbot ratio                           |
| 196 | 788      | Command: ahbot ratio alliance                  |
| 196 | 789      | Command: ahbot ratio horde                     |
| 196 | 790      | Command: ahbot ratio neutral                   |
| 196 | 791      | Command: ahbot rebuild                         |
| 196 | 792      | Command: ahbot reload                          |
| 196 | 793      | Command: ahbot status                          |
| 196 | 839      | Command: server shutdown force                 |
| 196 | 840      | Command: server restart force                  |
| 196 | 843      | Command: reload quest_greeting                 |
| 196 | 866      | Command: list spawnpoints                      |
| 196 | 867      | Command: reload quest_greeting_locale          |
| 196 | 872      | Command: server debug                          |
| 196 | 873      | Command: reload creature_movement_override     |
| 196 | 880      | Command: pdump copy                            |
| 196 | 881      | Command: reload vehicle_template               |
| 196 | 886      | Command: item restore                          |
| 196 | 887      | Command: item restore list                     |
| 196 | 888      | Command: item refund                           |
| 196 | 891      | Command: string                                |
| 196 | 894      | Command: packetlog                             |
| 196 | 896      | Command: respawn all                           |
| 196 | 905      | Command: arena season state                    |
| 196 | 906      | Command: arena season reward                   |
| 196 | 907      | Command: arena season deleteteams              |
| 196 | 908      | Command: arena season start                    |
| 196 | 912      | Command: gobject load                          |
| 196 | 915      | Command: pet delete                            |
| 196 | 922      | Command: pet rename                            |
| 196 | 927      | Command: autobroadcast add                     |
| 196 | 928      | Command: autobroadcast locale                  |
| 196 | 929      | Command: autobroadcast remove                  |
| 196 | 932      | Command: npc load                              |
| 196 | 939      | Command: server set security                   |
| 196 | 943      | Command: account flag add                      |
| 196 | 944      | Command: account flag remove                   |

</details>

<details>
<summary id="role-197">197 - Role: Gamemaster Commands</summary>

| id  | linkedId | Comment                             |
| :-- | :------- | :---------------------------------- |
| 197 | 231      | Command: achievement add            |
| 197 | 232      | Command: achievement checkall       |
| 197 | 233      | Command: arena captain              |
| 197 | 234      | Command: arena create               |
| 197 | 235      | Command: arena disband              |
| 197 | 236      | Command: arena info                 |
| 197 | 237      | Command: arena lookup               |
| 197 | 238      | Command: arena rename               |
| 197 | 267      | Command: cast                       |
| 197 | 268      | Command: cast back                  |
| 197 | 269      | Command: cast dist                  |
| 197 | 270      | Command: cast self                  |
| 197 | 271      | Command: cast target                |
| 197 | 272      | Command: cast dest                  |
| 197 | 274      | Command: character customize        |
| 197 | 275      | Command: character changefaction    |
| 197 | 276      | Command: character changerace       |
| 197 | 279      | Command: character deleted list     |
| 197 | 280      | Command: character deleted restore  |
| 197 | 283      | Command: character level            |
| 197 | 284      | Command: character rename           |
| 197 | 285      | Command: character reputation       |
| 197 | 286      | Command: character titles           |
| 197 | 287      | Command: levelup                    |
| 197 | 292      | Command: cheat casttime             |
| 197 | 293      | Command: cheat cooldown             |
| 197 | 294      | Command: cheat explore              |
| 197 | 295      | Command: cheat god                  |
| 197 | 296      | Command: cheat power                |
| 197 | 297      | Command: cheat status               |
| 197 | 298      | Command: cheat taxi                 |
| 197 | 299      | Command: cheat waterwalk            |
| 197 | 300      | Command: debug                      |
| 197 | 343      | Command: deserter bg add            |
| 197 | 344      | Command: deserter bg remove         |
| 197 | 346      | Command: deserter instance add      |
| 197 | 347      | Command: deserter instance remove   |
| 197 | 367      | Command: event info                 |
| 197 | 368      | Command: event activelist           |
| 197 | 369      | Command: event start                |
| 197 | 370      | Command: event stop                 |
| 197 | 371      | Command: gm                         |
| 197 | 372      | Command: gm chat                    |
| 197 | 373      | Command: gm fly                     |
| 197 | 376      | Command: gm visible                 |
| 197 | 377      | Command: go                         |
| 197 | 388      | Command: gobject activate           |
| 197 | 389      | Command: gobject add                |
| 197 | 390      | Command: gobject add temp           |
| 197 | 391      | Command: gobject delete             |
| 197 | 392      | Command: gobject info               |
| 197 | 393      | Command: gobject move               |
| 197 | 394      | Command: gobject near               |
| 197 | 396      | Command: gobject set phase          |
| 197 | 397      | Command: gobject set state          |
| 197 | 398      | Command: gobject target             |
| 197 | 399      | Command: gobject turn               |
| 197 | 401      | Command: guild                      |
| 197 | 402      | Command: guild create               |
| 197 | 403      | Command: guild delete               |
| 197 | 404      | Command: guild invite               |
| 197 | 405      | Command: guild uninvite             |
| 197 | 406      | Command: guild rank                 |
| 197 | 407      | Command: guild rename               |
| 197 | 409      | Command: honor add                  |
| 197 | 410      | Command: honor add kill             |
| 197 | 411      | Command: honor update               |
| 197 | 413      | Command: instance listbinds         |
| 197 | 414      | Command: instance unbind            |
| 197 | 415      | Command: instance stats             |
| 197 | 416      | Command: instance savedata          |
| 197 | 417      | Command: learn                      |
| 197 | 419      | Command: learn all my               |
| 197 | 420      | Command: learn all my class         |
| 197 | 421      | Command: learn my pettalents        |
| 197 | 422      | Command: learn all my spells        |
| 197 | 423      | Command: learn all talents          |
| 197 | 424      | Command: learn all gm               |
| 197 | 425      | Command: learn all crafts           |
| 197 | 426      | Command: learn all default          |
| 197 | 427      | Command: learn all lang             |
| 197 | 428      | Command: learn all recipes          |
| 197 | 429      | Command: unlearn                    |
| 197 | 431      | Command: lfg player                 |
| 197 | 432      | Command: lfg group                  |
| 197 | 433      | Command: lfg queue                  |
| 197 | 434      | Command: lfg clean                  |
| 197 | 435      | Command: lfg options                |
| 197 | 436      | Command: lfg cooldown               |
| 197 | 437      | Command: list creature              |
| 197 | 438      | Command: list item                  |
| 197 | 439      | Command: list object                |
| 197 | 440      | Command: list auras                 |
| 197 | 441      | Command: list mail                  |
| 197 | 445      | Command: lookup event               |
| 197 | 448      | Command: lookup itemset             |
| 197 | 449      | Command: lookup object              |
| 197 | 451      | Command: lookup player              |
| 197 | 452      | Command: lookup player ip           |
| 197 | 453      | Command: lookup player account      |
| 197 | 454      | Command: lookup player email        |
| 197 | 457      | Command: lookup spell id            |
| 197 | 458      | Command: lookup taxinode            |
| 197 | 460      | Command: lookup title               |
| 197 | 461      | Command: lookup map                 |
| 197 | 472      | Command: group                      |
| 197 | 473      | Command: group leader               |
| 197 | 474      | Command: group disband              |
| 197 | 475      | Command: group remove               |
| 197 | 476      | Command: group join                 |
| 197 | 477      | Command: group list                 |
| 197 | 478      | Command: group summon               |
| 197 | 479      | Command: pet                        |
| 197 | 480      | Command: pet create                 |
| 197 | 481      | Command: pet learn                  |
| 197 | 482      | Command: pet unlearn                |
| 197 | 483      | Command: send                       |
| 197 | 484      | Command: send items                 |
| 197 | 485      | Command: send mail                  |
| 197 | 486      | Command: send message               |
| 197 | 487      | Command: send money                 |
| 197 | 488      | Command: additem                    |
| 197 | 489      | Command: additemset                 |
| 197 | 490      | Command: appear                     |
| 197 | 491      | Command: aura                       |
| 197 | 492      | Command: bank                       |
| 197 | 493      | Command: bindsight                  |
| 197 | 494      | Command: combatstop                 |
| 197 | 495      | Command: cometome                   |
| 197 | 497      | Command: cooldown                   |
| 197 | 498      | Command: damage                     |
| 197 | 499      | Command: dev                        |
| 197 | 500      | Command: die                        |
| 197 | 502      | Command: distance                   |
| 197 | 504      | Command: freeze                     |
| 197 | 506      | Command: guid                       |
| 197 | 508      | Command: hidearea                   |
| 197 | 509      | Command: itemmove                   |
| 197 | 512      | Command: listfreeze                 |
| 197 | 513      | Command: maxskill                   |
| 197 | 514      | Command: movegens                   |
| 197 | 516      | Command: neargrave                  |
| 197 | 518      | Command: playall                    |
| 197 | 519      | Command: possess                    |
| 197 | 520      | Command: recall                     |
| 197 | 521      | Command: repairitems                |
| 197 | 522      | Command: respawn                    |
| 197 | 523      | Command: revive                     |
| 197 | 526      | Command: setskill                   |
| 197 | 527      | Command: showarea                   |
| 197 | 528      | Command: summon                     |
| 197 | 529      | Command: unaura                     |
| 197 | 530      | Command: unbindsight                |
| 197 | 531      | Command: unfreeze                   |
| 197 | 533      | Command: unpossess                  |
| 197 | 535      | Command: wchange                    |
| 197 | 536      | Command: mmap                       |
| 197 | 537      | Command: mmap loadedtiles           |
| 197 | 538      | Command: mmap loc                   |
| 197 | 539      | Command: mmap path                  |
| 197 | 540      | Command: mmap stats                 |
| 197 | 541      | Command: mmap testarea              |
| 197 | 542      | Command: morph                      |
| 197 | 543      | Command: demorph                    |
| 197 | 544      | Command: modify                     |
| 197 | 545      | Command: modify arenapoints         |
| 197 | 546      | Command: modify bit                 |
| 197 | 547      | Command: modify drunk               |
| 197 | 548      | Command: modify energy              |
| 197 | 549      | Command: modify faction             |
| 197 | 550      | Command: modify gender              |
| 197 | 551      | Command: modify honor               |
| 197 | 552      | Command: modify hp                  |
| 197 | 553      | Command: modify mana                |
| 197 | 554      | Command: modify money               |
| 197 | 555      | Command: modify mount               |
| 197 | 556      | Command: modify phase               |
| 197 | 557      | Command: modify rage                |
| 197 | 558      | Command: modify reputation          |
| 197 | 559      | Command: modify runicpower          |
| 197 | 560      | Command: modify scale               |
| 197 | 561      | Command: modify speed               |
| 197 | 562      | Command: modify speed all           |
| 197 | 563      | Command: modify speed backwalk      |
| 197 | 564      | Command: modify speed fly           |
| 197 | 565      | Command: modify speed walk          |
| 197 | 566      | Command: modify speed swim          |
| 197 | 567      | Command: modify spell               |
| 197 | 568      | Command: modify standstate          |
| 197 | 569      | Command: modify talentpoints        |
| 197 | 571      | Command: npc add                    |
| 197 | 572      | Command: npc add formation          |
| 197 | 573      | Command: npc add item               |
| 197 | 574      | Command: npc add move               |
| 197 | 575      | Command: npc add temp               |
| 197 | 576      | Command: npc delete                 |
| 197 | 577      | Command: npc delete item            |
| 197 | 578      | Command: npc follow                 |
| 197 | 579      | Command: npc follow stop            |
| 197 | 580      | Command: npc set                    |
| 197 | 581      | Command: npc set allowmove          |
| 197 | 582      | Command: npc set entry              |
| 197 | 583      | Command: npc set factionid          |
| 197 | 584      | Command: npc set flag               |
| 197 | 585      | Command: npc set level              |
| 197 | 586      | Command: npc set link               |
| 197 | 587      | Command: npc set model              |
| 197 | 588      | Command: npc set movetype           |
| 197 | 589      | Command: npc set phase              |
| 197 | 590      | Command: npc set spawndist          |
| 197 | 591      | Command: npc set spawntime          |
| 197 | 592      | Command: npc set data               |
| 197 | 593      | Command: npc info                   |
| 197 | 594      | Command: npc near                   |
| 197 | 595      | Command: npc move                   |
| 197 | 596      | Command: npc playemote              |
| 197 | 597      | Command: npc say                    |
| 197 | 598      | Command: npc textemote              |
| 197 | 599      | Command: npc whisper                |
| 197 | 600      | Command: npc yell                   |
| 197 | 601      | Command: npc tame                   |
| 197 | 602      | Command: quest                      |
| 197 | 603      | Command: quest add                  |
| 197 | 604      | Command: quest complete             |
| 197 | 605      | Command: quest remove               |
| 197 | 606      | Command: quest reward               |
| 197 | 737      | Command: tele                       |
| 197 | 738      | Command: tele add                   |
| 197 | 739      | Command: tele del                   |
| 197 | 740      | Command: tele name                  |
| 197 | 741      | Command: tele group                 |
| 197 | 762      | Command: titles add                 |
| 197 | 763      | Command: titles current             |
| 197 | 764      | Command: titles remove              |
| 197 | 766      | Command: titles set mask            |
| 197 | 767      | Command: wp                         |
| 197 | 768      | Command: wp add                     |
| 197 | 769      | Command: wp event                   |
| 197 | 770      | Command: wp load                    |
| 197 | 771      | Command: wp modify                  |
| 197 | 772      | Command: wp unload                  |
| 197 | 774      | Command: wp show                    |
| 197 | 794      | Command: guild info                 |
| 197 | 795      | Command: instance setbossstate      |
| 197 | 796      | Command: instance getbossstate      |
| 197 | 798      | Command: modify xp                  |
| 197 | 837      | Command: npc evade                  |
| 197 | 838      | Command: pet level                  |
| 197 | 841      | Command: neargraveyard              |
| 197 | 856      | Command: npc spawngroup             |
| 197 | 857      | Command: npc despawngroup           |
| 197 | 858      | Command: gobject spawngroup         |
| 197 | 859      | Command: gobject despawngroup       |
| 197 | 860      | Command: list respawns              |
| 197 | 861      | Command: group set                  |
| 197 | 862      | Command: group set assistant        |
| 197 | 863      | Command: group set maintank         |
| 197 | 864      | Command: group set mainassist       |
| 197 | 865      | Command: npc showloot               |
| 197 | 868      | Command: group revive               |
| 197 | 874      | Command: settings announcer         |
| 197 | 875      | Command: lookup map id              |
| 197 | 876      | Command: lookup item id             |
| 197 | 877      | Command: lookup quest id            |
| 197 | 884      | Command: bg start                   |
| 197 | 885      | Command: bg stop                    |
| 197 | 889      | Command: commentator                |
| 197 | 890      | Command: skirmish                   |
| 197 | 892      | Command: opendoor                   |
| 197 | 893      | Command: beastmaster                |
| 197 | 895      | Command: aura stack                 |
| 197 | 897      | Command: gear repair                |
| 197 | 909      | Command: character check bank       |
| 197 | 910      | Command: character check bag        |
| 197 | 911      | Command: character check profession |
| 197 | 913      | Command: bf queue                   |
| 197 | 916      | Command: respawn creature guid      |
| 197 | 917      | Command: respawn gameobject guid    |
| 197 | 918      | Command: respawn creature entry     |
| 197 | 919      | Command: respawn gameobject entry   |
| 197 | 923      | Command: chatfilter list            |
| 197 | 924      | Command: chatfilter add             |
| 197 | 925      | Command: chatfilter remove          |
| 197 | 926      | Command: autobroadcast list         |
| 197 | 930      | Command: mail list                  |
| 197 | 931      | Command: mail return                |
| 197 | 933      | Command: pool info                  |
| 197 | 934      | Command: pool lookup                |
| 197 | 935      | Command: spellinfo attributes       |
| 197 | 936      | Command: spellinfo effects          |
| 197 | 937      | Command: spellinfo targets          |
| 197 | 938      | Command: spellinfo all              |
| 197 | 940      | Command: group invites              |
| 197 | 941      | Command: account flag               |
| 197 | 942      | Command: account flag list          |
| 197 | 945      | Command: account info               |

</details>

<details>
<summary id="role-198">198 - Role: Moderator Commands</summary>

| id  | linkedId | Comment                           |
| :-- | :------- | :-------------------------------- |
| 198 | 240      | Command: ban account              |
| 198 | 241      | Command: ban character            |
| 198 | 242      | Command: ban ip                   |
| 198 | 243      | Command: ban playeraccount        |
| 198 | 245      | Command: baninfo account          |
| 198 | 246      | Command: baninfo character        |
| 198 | 247      | Command: baninfo ip               |
| 198 | 249      | Command: banlist account          |
| 198 | 250      | Command: banlist character        |
| 198 | 251      | Command: banlist ip               |
| 198 | 253      | Command: unban account            |
| 198 | 254      | Command: unban character          |
| 198 | 255      | Command: unban ip                 |
| 198 | 256      | Command: unban playeraccount      |
| 198 | 462      | Command: announce                 |
| 198 | 466      | Command: gmannounce               |
| 198 | 467      | Command: gmnameannounce           |
| 198 | 468      | Command: gmnotify                 |
| 198 | 469      | Command: nameannounce             |
| 198 | 470      | Command: notify                   |
| 198 | 510      | Command: kick                     |
| 198 | 515      | Command: mute                     |
| 198 | 517      | Command: pinfo                    |
| 198 | 532      | Command: unmute                   |
| 198 | 632      | Command: mutehistory              |
| 198 | 742      | Command: ticket                   |
| 198 | 743      | Command: ticket assign            |
| 198 | 744      | Command: ticket close             |
| 198 | 745      | Command: ticket closedlist        |
| 198 | 746      | Command: ticket comment           |
| 198 | 747      | Command: ticket complete          |
| 198 | 749      | Command: ticket escalate          |
| 198 | 750      | Command: ticket escalatedlist     |
| 198 | 751      | Command: ticket list              |
| 198 | 752      | Command: ticket onlinelist        |
| 198 | 754      | Command: ticket response          |
| 198 | 755      | Command: ticket response append   |
| 198 | 756      | Command: ticket response appendln |
| 198 | 758      | Command: ticket unassign          |
| 198 | 759      | Command: ticket viewid            |
| 198 | 760      | Command: ticket viewname          |
| 198 | 914      | Command: pet list                 |

</details>

<details>
<summary id="role-199">199 - Role: Player Commands</summary>

| id  | linkedId | Comment                       |
| :-- | :------- | :---------------------------- |
| 199 | 217      | Command: account              |
| 199 | 218      | Command: account addon        |
| 199 | 221      | Command: account lock         |
| 199 | 222      | Command: account lock country |
| 199 | 223      | Command: account lock ip      |
| 199 | 225      | Command: account password     |
| 199 | 263      | Command: account email        |
| 199 | 374      | Command: gm ingame            |
| 199 | 375      | Command: gm list              |
| 199 | 442      | Command: lookup               |
| 199 | 443      | Command: lookup area          |
| 199 | 444      | Command: lookup creature      |
| 199 | 446      | Command: lookup faction       |
| 199 | 447      | Command: lookup item          |
| 199 | 450      | Command: lookup quest         |
| 199 | 455      | Command: lookup skill         |
| 199 | 456      | Command: lookup spell         |
| 199 | 459      | Command: lookup tele          |
| 199 | 496      | Command: commands             |
| 199 | 501      | Command: dismount             |
| 199 | 505      | Command: gps                  |
| 199 | 507      | Command: help                 |
| 199 | 525      | Command: save                 |
| 199 | 534      | Command: unstuck              |
| 199 | 725      | Command: server info          |
| 199 | 797      | Command: pvpstats             |
| 199 | 898      | Command: gear stats           |
| 199 | 899      | Command: spect                |
| 199 | 900      | Command: spect version        |
| 199 | 901      | Command: spect reset          |
| 199 | 902      | Command: spect spectate       |
| 199 | 903      | Command: spect watch          |
| 199 | 904      | Command: spect leave          |

</details>

<details>
<summary id="role-300">300 - Command: debug</summary>

| id  | linkedId | Comment                 |
| :-- | :------- | :---------------------- |
| 300 | 920      | Command: debug info     |
| 300 | 921      | Command: debug cosmetic |

</details>

<!-- rbac-default-data:end -->
