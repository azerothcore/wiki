# creature\_template

[<-Back-to:World](database-world)

**The \`creature\_template\` table**

This table contains the description of creatures. Each spawned creature is an instance of a template present in this table, this means every creature MUST be defined in this table.

**Table: creature\_template's Structure**

| Field                                         | Type      |          | Null | Key | Default | Extra | Comment                                |
| :-------------------------------------------- | :-------- | :------- | :--: | :-: | :-----: | :---: | :------------------------------------- |
| [entry](#entry)                               | INT       | UNSIGNED | NO   | PRI | 0       |       |                                        |
| [difficulty_entry_1](#difficultyentryx)       | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [difficulty_entry_2](#difficultyentryx)       | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [difficulty_entry_3](#difficultyentryx)       | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [KillCredit1](#killcredit1)                   | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [KillCredit2](#killcredit2)                   | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [name](#name)                                 | CHAR(100) |          | NO   | MUL | 0       |       |                                        |
| [subname](#subname)                           | CHAR(100) |          | YES  |     | NULL    |       |                                        |
| [IconName](#iconname)                         | CHAR(100) |          | YES  |     | NULL    |       |                                        |
| [gossip_menu_id](#gossipmenuid)               | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [minlevel](#minlevel)                         | TINYINT   | UNSIGNED | NO   |     | 1       |       |                                        |
| [maxlevel](#maxlevel)                         | TINYINT   | UNSIGNED | NO   |     | 1       |       |                                        |
| [exp](#exp)                                   | SMALLINT  |          | NO   |     | 0       |       |                                        |
| [faction](#faction)                           | SMALLINT  | UNSIGNED | NO   |     | 0       |       |                                        |
| [npcflag](#npcflag)                           | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [speed_walk](#speedwalk)                      | FLOAT     |          | NO   |     | 1       |       | Result of 2.5/2.5, most common value   |
| [speed_run](#speedrun)                        | FLOAT     |          | NO   |     | 1.14286 |       | Result of 8.0/7.0, most common value   |
| [speed_swim](#speedswim)                      | FLOAT     |          | NO   |     | 1       |       |                                        |
| [speed_flight](#speedflight)                  | FLOAT     |          | NO   |     | 1       |       |                                        |
| [detection_range](#detectionrange)            | FLOAT     |          | NO   |     | 20      |       |                                        |
| [rank](#rank)                                 | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                        |
| [dmgschool](#dmgschool)                       | TINYINT   |          | NO   |     | 0       |       |                                        |
| [DamageModifier](#damagemodifier)             | FLOAT     |          | NO   |     | 1       |       |                                        |
| [BaseAttackTime](#baseattacktime)             | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [RangeAttackTime](#rangeattacktime)           | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [BaseVariance](#basevariance)                 | FLOAT     |          | NO   |     | 1       |       |                                        |
| [RangeVariance](#rangevariance)               | FLOAT     |          | NO   |     | 1       |       |                                        |
| [unit_class](#unitclass)                      | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                        |
| [unit_flags](#unitflags)                      | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [unit_flags2](#unitflags2)                    | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [dynamicflags](#dynamicflags)                 | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [family](#family)                             | TINYINT   |          | NO   |     | 0       |       |                                        |
| [type](#type)                                 | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                        |
| [type_flags](#typeflags)                      | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [lootid](#lootid)                             | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [pickpocketloot](#pickpocketloot)             | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [skinloot](#skinloot)                         | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [PetSpellDataId](#petspelldataid)             | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [VehicleId](#vehicleid)                       | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [mingold](#mingold)                           | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [maxgold](#maxgold)                           | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [AIName](#ainame)                             | CHAR(64)  |          | NO   |     | ''      |       |                                        |
| [MovementType](#movementtype)                 | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                        |
| [HoverHeight](#hoverheight)                   | FLOAT     |          | NO   |     | 1       |       |                                        |
| [HealthModifier](#healthmodifier)             | FLOAT     |          | NO   |     | 1       |       |                                        |
| [ManaModifier](#manamodifier)                 | FLOAT     |          | NO   |     | 1       |       |                                        |
| [ArmorModifier](#armormodifier)               | FLOAT     |          | NO   |     | 1       |       |                                        |
| [ExperienceModifier](#experiencemodifier)     | FLOAT     |          | NO   |     | 1       |       |                                        |
| [RacialLeader](#racialleader)                 | TINYINT   | UNSIGNED | NO   |     | 0       |       |                                        |
| [movementId](#movementid)                     | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [RegenHealth](#regenhealth)                   | TINYINT   | UNSIGNED | NO   |     | 1       |       |                                        |
| [CreatureImmunitiesId](#creatureimmunitiesid) | INT       |          | NO   |     | 0       |       | Reference to creature_immunities table |
| [flags_extra](#flagsextra)                    | INT       | UNSIGNED | NO   |     | 0       |       |                                        |
| [ScriptName](#scriptname)                     | CHAR(64)  |          | NO   |     | ''      |       |                                        |
| [VerifiedBuild](#verifiedbuild)               | INT       |          | YES  |     | NULL    |       |                                        |

---

**Description of the table's fields**

### entry

Creature's unique id.

### difficulty_entry_x

| name                                                      | entry | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| --------------------------------------------------------- | ----- | ------------------ | ------------------ | ------------------ |
| [Anomalus](http://www.wowhead.com/npc=26763/anomalus)     | 26763 | 30529              | 0                  | 0                  |
| [Sindragosa](http://www.wowhead.com/npc=36853/sindragosa) | 36853 | 38265              | 38266              | 38267              |

Anomalus is a 5 man boss located in The Nexus. You can fight him on two types of difficulties (normal dungeon and heroic dungeon). Depending on the type of difficulty, bosses have different statistics like health and damage. In case of Anomalus information from entry 26763 is used when you fight him at normal difficulty and entry 30529 is used when you fight him at heroic difficulty.

Sindragosa, a raid boss encounter located in the Icecrown Citadel can be fought on 4 different difficulties due to the introduction of heroic raid modes in Patch 3.2 (10man normal/heroic, 25man normal/heroic). Depending on the type of difficulty, she must have different statistics. So if you see her in 10man normal raid she will use information from entry 36853, in a 25man normal raid entry 38265 will be used and so on.  This is in stark contrast to raid bosses such as Patchwerk and XT-002 Deconstructor, located in Naxxramas and Ulduar respectively, who only have two different raid modes (10-man 'normal'/25-man 'normal').  Hardmodes within the Ulduar raid do not have their own template, due to game mechanics engaging the harder difficulty during the encounter itself.

Here is a special case with the Alterac Valley battleground. There are 4 level brackets where the NPCs are made easier or harder, depending on your level bracket (Added in WoW patch 3.2.2 when level 80 characters received their own bracket for this battleground and all brackets below level 80 received their own level of difficulty).  The same concept applies to the Isle of Conquest battleground, with only two brackets.  

If you look at the database you will notice a very characteristic pattern which is summarized in table below:

| name             | entry             | difficulty_entry_1 | difficulty_entry_2 | difficulty_entry_3 |
| ---------------- | ----------------- | ------------------ | ------------------ | ------------------ |
| Normal Creature  | Different than 0  | 0                  | 0                  | 0                  |
| Dungeon Creature | Normal Dungeon    | Heroic Dungeon     | 0                  | 0                  |
| Raid Creature    | 10man Normal Raid | 25man Normal Raid  | 10man Heroic Raid  | 25man Heroic Raid  |
| Battleground     | 51- 59            | 60-69              | 70-79              | 80                 |

### KillCredit1

If this is a kill credit template -- one that is a dummy template that is used when more than one creature can count as a kill in a quest, then this is a link to the first [entry](#entry) of the creature that could be killed to give quest credit.

### KillCredit2

If this is a kill credit template -- one that is a dummy template that is used when more than one creature can count as a kill in a quest, then this is a link to the second [entry](#entry) of the creature that could be killed to give quest credit. If more than two creatures can be killed and count toward a single objective, an smart or C++ script will be required.

### name

Base name of the creature.

### subname

The subname of the creature that appears in &lt;&gt; below the creature's name.

### IconName

Used to tell the player what kind of NPC this creature is.

| IconName           | description                                                                        |
| ------------------ | ---------------------------------------------------------------------------------- |
| **Directions**     | Used for guards and teleporter NPC's.                                              |
| **Gunner**         | Indicator of a turret NPC/Player Controlled.                                       |
| **vehichleCursor** | Indicator that this is a PCV (Player Controlled Vehicle)                           |
| **Driver**         | Shows a steering wheel icon when mouse over.                                       |
| **Attack**         | Shows a sword icon indicating you can attack this target.                          |
| **Buy**            | Shows a brown bag icon usually if the NPC only sells things.                       |
| **Speak**          | Shows a chat bubble icon if this NPC has quest/gossip options.                     |
| **Pickup**         | Shows a hand grasping icon if this NPC can be picked up for quest/items.           |
| **Interact**       | Shows cog icon commonly used for quest/transport.                                  |
| **Trainer**        | Shows a book icon, identifying this NPC as a trainer.                              |
| **Taxi**           | Shows a boot with wings icon identifying this NPC as a taxi.                       |
| **Repair**         | Shows a anvil icon identifying that this NPC can repair.                           |
| **LootAll**        | Shows a multiple brown bag icon (same as holding shift before looting a creature). |
| **Quest**          | Unused or unknown (see entry 32870 "The Real Ronakada").                           |
| **PVP**            | Unused or Unknown (see entry 29387 "Arena Master: Dalaran Arena").                 |

**Attention!** This is not required to make the NPC function unless you are using scripts or gossip options. Names are case sensitive, If in doubt use an example above.

### gossip_menu_id

The gossip ID of this creature. This field is obtained from sniff (update fields). If you can not sniff this value, and need to make one up, it must be &gt; 50000. This field is the link to [gossip_menu.MenuID](gossip_menu#menuid).

### minlevel

The minimum level of the creature if the creature has a level range.

### maxlevel

The maximum level of the creature if the creature has a level range. When added to world, a level in chosen in the specified level range.

### exp

The expansion table the creatures health value is taken from. Values are from 0 to 2. See creature_classlevelstats.

| exp | name                   |
| --- | ---------------------- |
| 0   | Classic                |
| 1   | The Burning Crusade    |
| 2   | Wrath of The Lich King |

### faction

The faction of the creature. See [FactionTemplate](factiontemplate). Just because more than one faction has the same name, the inter-faction relationships can be different.

Note: This field also controls the creature family assistance mechanic. Only creatures with the same faction will assist each other.

### npcflag

A bitmask that represents what NPC flags the creature has. Each bit controls a different flag and to combine flags, you can add each flag that you want, in effect activating the respective bits.

| Value    | Hex          | Flag               | Comment                                                                                 |
| :------- | :----------: | :----------------- | :-------------------------------------------------------------------------------------- |
| 1        | `0x00000001` | Gossip             | If creature has more gossip options, add this flag to bring up a menu.                  |
| 2        | `0x00000002` | Quest Giver        | Any creature giving or taking quests needs to have this flag.                           |
| 4        | `0x00000004` | Unknown 1          | UNIT_NPC_FLAG_UNK1 in the core. It has no description in TrinityCore, cmangos or mangos |
| 8        | `0x00000008` | Unknown 2          | UNIT_NPC_FLAG_UNK2 in the core. It has no description in TrinityCore, cmangos or mangos |
| 16       | `0x00000010` | Trainer            | Allows the creature to have a trainer list to teach spells                              |
| 32       | `0x00000020` | Class Trainer      | Is class trainer                                                                        |
| 64       | `0x00000040` | Profession Trainer | Is profession trainer                                                                   |
| 128      | `0x00000080` | Vendor             | Is vendor (generic) Any creature selling items needs to have this flag.                 |
| 256      | `0x00000100` | Vendor Ammo        | Is vendor (ammo)                                                                        |
| 512      | `0x00000200` | Vendor Food        | Is vendor (food)                                                                        |
| 1024     | `0x00000400` | Vendor Poison      | Is vendor (poison)                                                                      |
| 2048     | `0x00000800` | Vendor Reagent     | Is vendor (Reagent)                                                                     |
| 4096     | `0x00001000` | Repairer           | Creatures with this flag can repair items.                                              |
| 8192     | `0x00002000` | Flight Master      | Any creature serving as flight master has this.                                         |
| 16384    | `0x00004000` | Spirit Healer      | Makes the creature invisible to alive characters and has the resurrect function.        |
| 32768    | `0x00008000` | Spirit Guide       | Is spirit guide                                                                         |
| 65536    | `0x00010000` | Innkeeper          | Creatures with this flag can set hearthstone locations.                                 |
| 131072   | `0x00020000` | Banker             | Creatures with this flag can show the bank                                              |
| 262144   | `0x00040000` | Petitioner         | Handles guild/arena petitions                                                           |
| 524288   | `0x00080000` | Tabard Designer    | Allows the designing of guild tabards.                                                  |
| 1048576  | `0x00100000` | Battlemaster       | Creatures with this flag port players to battlegrounds.                                 |
| 2097152  | `0x00200000` | Auctioneer         | Allows creature to display auction list.                                                |
| 4194304  | `0x00400000` | Stable Master      | Has the option to stable pets for hunters.                                              |
| 8388608  | `0x00800000` | Guild Banker       | Is guild banker                                                                         |
| 16777216 | `0x01000000` | Spellclick         | Needs data on npc_spellclick_spells table                                               |
| 67108864 | `0x04000000` | Mailbox            | NPC will act like a mailbox (opens mailbox with right-click)                            |

So if you want a NPC that is a quest giver(2), a vendor(128) and can repair(4096) you just add specific flags together: 2+128+4096=4226

### speed_walk

Controls how fast the creature can walk. For vehicles: increases fly speed.

### speed_run

Controls how fast the creature can run. For vehicles: increases ground movement speed.

### speed_swim

Controls how fast the creature can swim.

### speed_flight

Controls how fast the creature can fly.

### detection_range

Controls the range at which creatures detect and see players.

### rank

The rank of the creature:

| Rank | Name       | Default Respawn Time Creature.spawntimesecs | Corpse Decay Time Worldserver.conf (Corpse.Decay) | Total Default Respawn spawntimesecs + Corpse.Decay |
| ---- | ---------- | ------------------------------------------- | ------------------------------------------------- | -------------------------------------------------- |
| 0    | Normal     | 5 min                                       | 60 sec                                            | 6 min                                              |
| 1    | Elite      | 5 min                                       | 5 min                                             | 10 min                                             |
| 2    | Rare Elite | 5 min                                       | 5 min                                             | 10 min                                             |
| 3    | Boss       | 5 min                                       | 1 hour                                            | 1 hour, 5 min                                      |
| 4    | Rare       | 5 min                                       | 5 min                                             | 10 min                                             |

**Note 1:** An NPC's rank is mostly visual (which also requires your Cache to be cleared to see changes). Changing this value will not change its health, damage, or loot. However, it will change the respawn time of the creature.

**Note 2:** Respawn times can be modified in two other places: [Creature.spawntimesecs](creature#spawntimesecs) (only for that single GUID of the creature) and in the worldserver.conf file under the "Corpse.Decay" settings (for ALL creatures of the same rank). The default \`spawntimesecs\` for all spawned creatures is 300 seconds (5 minutes). For example, using the ".npc add" command to spawn a "Normal" NPC will give it a default respawn time of 6 minutes (spawntimesecs + Corpse.Decay time). Also, the creature must decay first before it can respawn. For this reason, the Corpse Decay Time of the creature is also it's minimum respawn time, since setting the creature's Creature.spawntimesecs = 0 will remove the Default Respawn Time. In the example above, setting our Normal NPC's spawntimesecs = 0 will mean the creature's respawn time decreases from 6 minutes to 60 seconds.

**Note 3:** If you want the creature to show a skull or "??" in the portrait (often with Bosses), set the [type_flags](#typeflags) to 4.

### dmgschool

Creature's melee damage school.

| ID  | Name                |
| --- | ------------------- |
| 0   | SPELL_SCHOOL_NORMAL |
| 1   | SPELL_SCHOOL_HOLY   |
| 2   | SPELL_SCHOOL_FIRE   |
| 3   | SPELL_SCHOOL_NATURE |
| 4   | SPELL_SCHOOL_FROST  |
| 5   | SPELL_SCHOOL_SHADOW |
| 6   | SPELL_SCHOOL_ARCANE |

### DamageModifier

Used to modify the Minimum/Maximum damage of a creature.

The formulas to calculate the damage output are:

MINDAMAGE = ((([damage_base](creature_classlevelstats#damagebase) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))  
MAXDAMAGE = (((([damage_base](creature_classlevelstats#damagebase) * 1.5) + ([attackpower](creature_classlevelstats#attackpower) / 14) * [BaseVariance](creature_template#basevariance)) * DamageModifier) * ([BaseAttackTime](#baseattacktime) / 1000))

damage_base comes from the creature_classlevelstats table and takes its value either from [damage_base](creature_classlevelstats#damagebase), [damage_exp1](creature_classlevelstats#damageexp1) or [damage_exp2](creature_classlevelstats#damageexp2) according to the creature's value in [exp](#exp) (0 = base_damage, 1 = damage_exp1, 2 = damage_exp2).

BaseAttackTime is either [BaseAttackTime](#baseattacktime) or [RangeAttackTime](#rangeattacktime) depending on the type of attack.

attackpower is either [attackpower](creature_classlevelstats#attackpower) or [rangedattackpower](creature_classlevelstats#rangedattackpower) depending on the type of attack.

BaseVariance is either [BaseVariance](#basevariance) or [RangeVariance](#rangevariance) depending on the type of attack.

### BaseAttackTime

This is the base time that determines how long a creature must wait between melee attacks. This time is in milliseconds.

### RangeAttackTime

This is the base time that determines how long a creature must wait between ranged attacks. This time is in milliseconds.

### BaseVariance

Value to customize the creature's damage output. See [DamageModifier](#damagemodifier).

Non-custom creatures should always leave this at 1.

### RangeVariance

Value to customize the creature's damage output. See [DamageModifier](#damagemodifier).

Non-custom creatures should always leave this at 1.

### unit_class

This is the creature's class, and it dictates levels of health and mana. Also note that health and mana will change according to [exp](#exp), [HealthModifier](#healthmodifier), and [ManaModifier](#manamodifier). Not setting this value will report a minor warning in the "DB_Errors.log".

| Value | Name          | Comment                                                |
| ----- | ------------- | ------------------------------------------------------ |
| 1     | CLASS_WARRIOR | health only (equal to rogue)                           |
| 2     | CLASS_PALADIN | health & mana (more health than mage but less mana)    |
| 4     | CLASS_ROGUE   | Health only (equal to warrior)                         |
| 8     | CLASS_MAGE    | health & mana (less health than paladin but more mana) |

### unit_flags

Allows the manual application of unit flags to creatures. Again this is a bitmask field and to apply more than one flag, just add the different numbers. Some possible flags are:

| Value      | Hex          | Flag                                    | Comment                                                                                                                                                                                                                                                                                                                                             |
| :--------- | :----------: | :-------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | `0x00000001` | UNIT_FLAG_SERVER_CONTROLLED             | set only when unit movement is controlled by server - by SPLINE/MONSTER_MOVE packets, together with UNIT_FLAG_STUNNED; only set to units controlled by client; client function CGUnit_C::IsClientControlled returns false when set for owner                                                                                                        |
| 2          | `0x00000002` | UNIT_FLAG_NON_ATTACKABLE                | Not attackable                                                                                                                                                                                                                                                                                                                                      |
| 4          | `0x00000004` | UNIT_FLAG_DISABLE_MOVE                  | The unit cannot be moved by its player. The core sets it on a player that controls another unit and rejects movement while it is set. [TrinityCore](https://github.com/TrinityCore/TrinityCore/blob/master/src/server/game/Entities/Unit/UnitDefines.h) calls it a legacy flag, renamed to UNIT_FLAG_REMOVE_CLIENT_CONTROL                          |
| 8          | `0x00000008` | UNIT_FLAG_PLAYER_CONTROLLED             | Controlled by player, use _IMMUNE_TO_PC instead of _IMMUNE_TO_NPC                                                                                                                                                                                                                                                                                   |
| 16         | `0x00000010` | UNIT_FLAG_RENAME                        | The core reads it to decide if the unit can swim. [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Unit.h) and [WowPacketParser](https://github.com/TrinityCore/WowPacketParser/blob/master/WowPacketParser/Enums/UnitFlags.cs) name it EVADING_HOME, and cmangos notes the client uses it in its check for swimming |
| 32         | `0x00000020` | UNIT_FLAG_PREPARATION                   | Don't take reagents for spells with SPELL_ATTR5_NO_REAGENT_COST_WITH_AURA                                                                                                                                                                                                                                                                           |
| 64         | `0x00000040` | UNIT_FLAG_UNK_6                         | not sure what it does, but it is needed to cast nontriggered spells in smart_scripts                                                                                                                                                                                                                                                                |
| 128        | `0x00000080` | UNIT_FLAG_NOT_ATTACKABLE_1              | ?? (UNIT_FLAG_PLAYER_CONTROLLED                                                                                                                                                                                                                                                                                                                     |
| 256        | `0x00000100` | UNIT_FLAG_IMMUNE_TO_PC                  | Disables combat/assistance with PlayerCharacters (PC)                                                                                                                                                                                                                                                                                               |
| 512        | `0x00000200` | UNIT_FLAG_IMMUNE_TO_NPC                 | Disables combat/assistance with NonPlayerCharacters (NPC)                                                                                                                                                                                                                                                                                           |
| 1024       | `0x00000400` | UNIT_FLAG_LOOTING                       | Loot animation                                                                                                                                                                                                                                                                                                                                      |
| 2048       | `0x00000800` | UNIT_FLAG_PET_IN_COMBAT                 | In combat? 2.0.8                                                                                                                                                                                                                                                                                                                                    |
| 4096       | `0x00001000` | UNIT_FLAG_PVP                           | Changed in 3.0.3                                                                                                                                                                                                                                                                                                                                    |
| 8192       | `0x00002000` | UNIT_FLAG_SILENCED                      | Can't cast spells                                                                                                                                                                                                                                                                                                                                   |
| 16384      | `0x00004000` | UNIT_FLAG_CANNOT_SWIM                   | 2.0.8                                                                                                                                                                                                                                                                                                                                               |
| 32768      | `0x00008000` | UNIT_FLAG_SWIMMING                      | Shows swim animation in water                                                                                                                                                                                                                                                                                                                       |
| 65536      | `0x00010000` | UNIT_FLAG_NON_ATTACKABLE_2              | Removes attackable icon, if on yourself, cannot assist self but can cast TARGET_SELF spells - added by SPELL_AURA_MOD_UNATTACKABLE                                                                                                                                                                                                                  |
| 131072     | `0x00020000` | UNIT_FLAG_PACIFIED                      | Creature will not attack                                                                                                                                                                                                                                                                                                                            |
| 262144     | `0x00040000` | UNIT_FLAG_STUNNED                       | 3.0.3 ok                                                                                                                                                                                                                                                                                                                                            |
| 524288     | `0x00080000` | UNIT_FLAG_IN_COMBAT                     | ('AffectingCombat' from UnitFlags.cs in WPP)                                                                                                                                                                                                                                                                                                        |
| 1048576    | `0x00100000` | UNIT_FLAG_TAXI_FLIGHT                   | Disable casting at client side spell not allowed by taxi flight (mounted?), probably used with 0x4 flag                                                                                                                                                                                                                                             |
| 2097152    | `0x00200000` | UNIT_FLAG_DISARMED                      | 3.0.3, disable melee spells casting..., "Required melee weapon" added to melee spells tooltip.                                                                                                                                                                                                                                                      |
| 4194304    | `0x00400000` | UNIT_FLAG_CONFUSED                      | Confused.                                                                                                                                                                                                                                                                                                                                           |
| 8388608    | `0x00800000` | UNIT_FLAG_FLEEING                       | ('Feared' from UnitFlags.cs in WPP)                                                                                                                                                                                                                                                                                                                 |
| 16777216   | `0x01000000` | UNIT_FLAG_POSSESSED                     | Under direct client control by a player (possess or vehicle)                                                                                                                                                                                                                                                                                        |
| 33554432   | `0x02000000` | UNIT_FLAG_NOT_SELECTABLE                | Can't be selected by mouse or with /target {name} command.                                                                                                                                                                                                                                                                                          |
| 67108864   | `0x04000000` | UNIT_FLAG_SKINNABLE                     | Skinnable                                                                                                                                                                                                                                                                                                                                           |
| 134217728  | `0x08000000` | UNIT_FLAG_MOUNT                         | The client seems to handle it perfectly. Also used when making custom mounts.                                                                                                                                                                                                                                                                       |
| 268435456  | `0x10000000` | UNIT_FLAG_UNK_28                        | (PreventKneelingWhenLooting from UnitFlags.cs in WPP)                                                                                                                                                                                                                                                                                               |
| 536870912  | `0x20000000` | UNIT_FLAG_PREVENT_EMOTES_FROM_CHAT_TEXT | Prevent automatically playing emotes from parsing chat text, for example "lol" in /say, ending message with ? or !, or using /yell                                                                                                                                                                                                                  |
| 1073741824 | `0x40000000` | UNIT_FLAG_SHEATHE                       | Not used by the core. It has no description in TrinityCore, cmangos or mangos                                                                                                                                                                                                                                                                       |
| 2147483648 | `0x80000000` | UNIT_FLAG_IMMUNE                        | Immune to damage                                                                                                                                                                                                                                                                                                                                    |

### unit_flags2

Allows additional application of unit flags to creatures. Again, this is a bitmask field and to apply more than one flag, just add the different numbers. Some possible flags are:


| Value  | Hex          | Flag                                  | Comment                                                                                                                                                                                                                                                                                              |
| :----- | :----------: | :------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1      | `0x00000001` | UNIT_FLAG2_FEIGN_DEATH                | The unit is feigning death                                                                                                                                                                                                                                                                           |
| 2      | `0x00000002` | UNIT_FLAG2_HIDE_BODY                  | Hide unit model (show only player equip)                                                                                                                                                                                                                                                             |
| 4      | `0x00000004` | UNIT_FLAG2_IGNORE_REPUTATION          | Reputation is ignored when the core works out if the unit is friendly or hostile                                                                                                                                                                                                                     |
| 8      | `0x00000008` | UNIT_FLAG2_COMPREHEND_LANG            | The unit understands every language                                                                                                                                                                                                                                                                  |
| 16     | `0x00000010` | UNIT_FLAG2_MIRROR_IMAGE               | The unit is a copy of another unit, used by the mirror image aura ([cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Unit.h) names it UNIT_FLAG2_CLONED)                                                                                                               |
| 32     | `0x00000020` | UNIT_FLAG2_DO_NOT_FADE_IN             | Unit model instantly appears when summoned (does not fade in)                                                                                                                                                                                                                                        |
| 64     | `0x00000040` | UNIT_FLAG2_FORCE_MOVEMENT             | The unit is forced to move. The core removes it from a player on login                                                                                                                                                                                                                               |
| 128    | `0x00000080` | UNIT_FLAG2_DISARM_OFFHAND             | The off-hand weapon or shield is disarmed                                                                                                                                                                                                                                                            |
| 256    | `0x00000100` | UNIT_FLAG2_DISABLE_PRED_STATS         | Player has disabled predicted stats (Used by raid frames)                                                                                                                                                                                                                                            |
| 512    | `0x00000200` | UNIT_FLAG2_ALLOW_CHANGING_TALENTS     | Not in the core. [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Entities/Unit.h) names it and marks it as not implemented; [TrinityCore 3.3.5](https://github.com/TrinityCore/TrinityCore/blob/3.3.5/src/server/game/Entities/Unit/UnitDefines.h) has it as UNIT_FLAG2_UNK_1 |
| 1024   | `0x00000400` | UNIT_FLAG2_DISARM_RANGED              | this does not disable ranged weapon display (maybe additional flag needed?)                                                                                                                                                                                                                          |
| 2048   | `0x00000800` | UNIT_FLAG2_REGENERATE_POWER           | The unit regenerates its power. Creatures with the extra flag NO_AUTOMATIC_REGEN do not get it                                                                                                                                                                                                       |
| 4096   | `0x00001000` | UNIT_FLAG2_RESTRICT_PARTY_INTERACTION | Restrict interaction to party or raid                                                                                                                                                                                                                                                                |
| 8192   | `0x00002000` | UNIT_FLAG2_PREVENT_SPELL_CLICK        | Prevent spellclick                                                                                                                                                                                                                                                                                   |
| 16384  | `0x00004000` | UNIT_FLAG2_ALLOW_ENEMY_INTERACT       | The unit can be interacted with while it is hostile ([TrinityCore](https://github.com/TrinityCore/TrinityCore/blob/master/src/server/game/Entities/Unit/UnitDefines.h) names it UNIT_FLAG2_INTERACT_WHILE_HOSTILE)                                                                                   |
| 32768  | `0x00008000` | UNIT_FLAG2_CANNOT_TURN                | The unit cannot turn                                                                                                                                                                                                                                                                                 |
| 65536  | `0x00010000` | UNIT_FLAG2_UNK2                       | Unknown. It has no description in AzerothCore, TrinityCore, cmangos or mangos                                                                                                                                                                                                                        |
| 131072 | `0x00020000` | UNIT_FLAG2_PLAY_DEATH_ANIM            | Plays special death animation upon death                                                                                                                                                                                                                                                             |
| 262144 | `0x00040000` | UNIT_FLAG2_ALLOW_CHEAT_SPELLS         | allows casting spells with AttributesEx7 & SPELL_ATTR7_DEBUG_SPELL                                                                                                                                                                                                                                   |

### dynamicflags

Flags that control visual appearance of the creature.

A few known flags and their use are:


| Value | Hex    | Flag                                   | Comment                                                                                                            |
| :---- | :----: | :------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| 0     | `0x00` | UNIT_DYNFLAG_NONE                      | No flag                                                                                                            |
| 1     | `0x01` | UNIT_DYNFLAG_LOOTABLE                  | The unit can be looted                                                                                             |
| 2     | `0x02` | UNIT_DYNFLAG_TRACK_UNIT                | Creature's location will be seen as a small dot in the minimap                                                     |
| 4     | `0x04` | UNIT_DYNFLAG_TAPPED                    | Makes creatures name appear grey (Lua_UnitIsTapped)                                                                |
| 8     | `0x08` | UNIT_DYNFLAG_TAPPED_BY_PLAYER          | Lua_UnitIsTappedByPlayer usually used by PCVs (Player Controlled Vehicles)                                         |
| 16    | `0x10` | UNIT_DYNFLAG_SPECIALINFO               | Extra information such as health is shown to a player that has an empathy aura on the unit, for example Beast Lore |
| 32    | `0x20` | UNIT_DYNFLAG_DEAD                      | Makes the creature appear dead (this DOES NOT make the creature's name grey or not attack players).                |
| 64    | `0x40` | UNIT_DYNFLAG_REFER_A_FRIEND            | Set by the core on a player linked through Refer-A-Friend                                                          |
| 128   | `0x80` | UNIT_DYNFLAG_TAPPED_BY_ALL_THREAT_LIST | Lua_UnitIsTappedByAllThreatList                                                                                    |

### family

The family this creature belongs to.

| ID  | Family       | ID  | Family         |
| --- | ------------ | --- | -------------- |
| 1.  | Wolf         | 26. | Owl            |
| 2.  | Cat          | 27. | Wind Serpent   |
| 3.  | Spider       | 28. | Remote Control |
| 4.  | Bear         | 29. | Felguard       |
| 5.  | Boar         | 30. | Dragonhawk     |
| 6.  | Crocolisk    | 31. | Ravager        |
| 7.  | Carrion Bird | 32. | Warp Stalker   |
| 8.  | Crab         | 33. | Sporebat       |
| 9.  | Gorilla      | 34. | Nether Ray     |
| 11. | Raptor       | 35. | Serpent        |
| 12. | Tallstrider  | 37. | Moth           |
| 15. | Felhunter    | 38. | Chimaera       |
| 16. | Voidwalker   | 39. | Devilsaur      |
| 17. | Succubus     | 40. | Ghoul          |
| 19. | Doomguard    | 41. | Silithid       |
| 20. | Scorpid      | 42. | Worm           |
| 21. | Turtle       | 43. | Rhino          |
| 23. | Imp          | 44. | Wasp           |
| 24. | Bat          | 45. | Core Hound     |
| 25. | Hyena        | 46. | Spirit Beast   |

### type

The type of the creature.

| ID  | Type           |
| --- | -------------- |
| 0   | None           |
| 1   | Beast          |
| 2   | Dragonkin      |
| 3   | Demon          |
| 4   | Elemental      |
| 5   | Giant          |
| 6   | Undead         |
| 7   | Humanoid       |
| 8   | Critter        |
| 9   | Mechanical     |
| 10  | Not specified  |
| 11  | Totem          |
| 12  | Non-Combat Pet |
| 13  | Gas Cloud      |

### type_flags

This field can control whether a mob is minable or herbable or lootable by engineer. If it is either of those three, then the loot given when it is skinned/mined will be stored in the [skinning_loot_template](loot_template) table. It also controls, whether this mob can be tamed by a hunter. Other fields have no special meaning on the serverside. The entire field will be send to the client in SMSG_CREATURE_QUERY_RESPONSE

| Value      | Hex          | Flag                                                 | Comment                                                                                                                                                |
| :--------- | :----------: | :--------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | `0x00000001` | CREATURE_TYPE_FLAG_TAMEABLE                          | Makes the mob tameable (must also be a beast and have family set)                                                                                      |
| 2          | `0x00000002` | CREATURE_TYPE_FLAG_VISIBLE_TO_GHOSTS                 | Creature are also visible for not alive player. Allow gossip interaction if npcflag allow?                                                             |
| 4          | `0x00000004` | CREATURE_TYPE_FLAG_BOSS_MOB                          | Changes creature's visible level to "??" in the creature's portrait - Immune to Knockback.                                                             |
| 8          | `0x00000008` | CREATURE_TYPE_FLAG_DO_NOT_PLAY_WOUND_ANIM            | Does not play wound animation on parry.                                                                                                                |
| 16         | `0x00000010` | CREATURE_TYPE_FLAG_NO_FACTION_TOOLTIP                | Hides tooltip faction.                                                                                                                                 |
| 32         | `0x00000020` | CREATURE_TYPE_FLAG_MORE_AUDIBLE                      | Related to sound                                                                                                                                       |
| 64         | `0x00000040` | CREATURE_TYPE_FLAG_SPELL_ATTACKABLE                  | Spell attackable.                                                                                                                                      |
| 128        | `0x00000080` | CREATURE_TYPE_FLAG_INTERACT_WHILE_DEAD               | Player can interact with the creature if its dead (not player dead)                                                                                    |
| 256        | `0x00000100` | CREATURE_TYPE_FLAG_SKIN_WITH_HERBALISM               | Makes mob herbable                                                                                                                                     |
| 512        | `0x00000200` | CREATURE_TYPE_FLAG_SKIN_WITH_MINING                  | Makes mob minable                                                                                                                                      |
| 1024       | `0x00000400` | CREATURE_TYPE_FLAG_NO_DEATH_MESSAGE                  | Does not combatlog death.                                                                                                                              |
| 2048       | `0x00000800` | CREATURE_TYPE_FLAG_ALLOW_MOUNTED_COMBAT              | Creature can remain mounted when entering combat                                                                                                       |
| 4096       | `0x00001000` | CREATURE_TYPE_FLAG_CAN_ASSIST                        | Can aid any player in combat if in range?                                                                                                              |
| 8192       | `0x00002000` | CREATURE_TYPE_FLAG_NO_PET_BAR                        | Is using pet bar.                                                                                                                                      |
| 16384      | `0x00004000` | CREATURE_TYPE_FLAG_MASK_UID                          | Not unique in the combat log                                                                                                                           |
| 32768      | `0x00008000` | CREATURE_TYPE_FLAG_SKIN_WITH_ENGINEERING             | Makes mob lootable by engineer                                                                                                                         |
| 65536      | `0x00010000` | CREATURE_TYPE_FLAG_TAMEABLE_EXOTIC                   | Tamable as an exotic pet. Normal tamable flag must also be set.                                                                                        |
| 131072     | `0x00020000` | CREATURE_TYPE_FLAG_USE_MODEL_COLLISION_SIZE          | Collision related. (always using default collision box?)                                                                                               |
| 262144     | `0x00040000` | CREATURE_TYPE_FLAG_ALLOW_INTERACTION_WHILE_IN_COMBAT | Is siege weapon.                                                                                                                                       |
| 524288     | `0x00080000` | CREATURE_TYPE_FLAG_COLLIDE_WITH_MISSILES             | Projectiles can collide with this creature - interacts with TARGET_DEST_TRAJ                                                                           |
| 1048576    | `0x00100000` | CREATURE_TYPE_FLAG_NO_NAME_PLATE                     | Hides nameplate.                                                                                                                                       |
| 2097152    | `0x00200000` | CREATURE_TYPE_FLAG_DO_NOT_PLAY_MOUNTED_ANIMATIONS    | Does not play mounted animations.                                                                                                                      |
| 4194304    | `0x00400000` | CREATURE_TYPE_FLAG_LINK_ALL                          | Unknown. It has no description in AzerothCore, TrinityCore, cmangos or mangos                                                                          |
| 8388608    | `0x00800000` | CREATURE_TYPE_FLAG_INTERACT_ONLY_WITH_CREATOR        | Can only interact with its creator.                                                                                                                    |
| 16777216   | `0x01000000` | CREATURE_TYPE_FLAG_DO_NOT_PLAY_UNIT_EVENT_SOUNDS     | No death scream                                                                                                                                        |
| 33554432   | `0x02000000` | CREATURE_TYPE_FLAG_HAS_NO_SHADOW_BLOB                | By its name, no shadow is drawn under the model. The core notes an older description, "can be healed by enemies", that may be linked to the wrong flag |
| 67108864   | `0x04000000` | CREATURE_TYPE_FLAG_TREAT_AS_RAID_UNIT                | Creature can be targeted by spells that require target to be in caster's party/raid                                                                    |
| 134217728  | `0x08000000` | CREATURE_TYPE_FLAG_FORCE_GOSSIP                      | Allows the creature to display a single gossip option.                                                                                                 |
| 268435456  | `0x10000000` | CREATURE_TYPE_FLAG_DO_NOT_SHEATHE                    | Sheathing of weapons is controlled by hand                                                                                                             |
| 536870912  | `0x20000000` | CREATURE_TYPE_FLAG_DO_NOT_TARGET_ON_INTERACTION      | A right click on the creature does not change the target of the player                                                                                 |
| 1073741824 | `0x40000000` | CREATURE_TYPE_FLAG_DO_NOT_RENDER_OBJECT_NAME         | The name is hidden in the world                                                                                                                        |
| 2147483648 | `0x80000000` | CREATURE_TYPE_FLAG_QUEST_BOSS                        | Not verified                                                                                                                                           |

### lootid

The ID of the loot template ID that this creature should use to generate loots. See [creature_loot_template.entry](loot_template#entry)

### pickpocketloot

The ID of the pickpocketing loot template that this creature should use to generate pickpocketing loots. See [pickpocketing_loot_template.entry](loot_template#entry)

### skinloot

The ID of the skinning loot template that this creature should use to generate skinning loots. See [skinning_loot_template.entry](loot_template#entry)

### PetSpellDataId

ID, found in CreatureSpellData.dbc, that displays what spells the pet has in the client.

### VehicleId

Entry of vehicle if creature is/has a vehicle entry. This field determines how the player appears on the vehicle, how the vehicle moves, and whether or not the vehicle action bar is shown. For example, a vehicleID of 292 will make the player invisible, prevent the vehicle from strafing left/right (but will allow forwards/backwards), and will show the vehicle action bar spells (which are defined in [spell1-8](http://trinitycore.atlassian.net#spell)). An npc_spellclick_spells entry must be made for this creature entry in order for this to work.

### mingold

Minimum money that the creature drops when killed, in copper.

### maxgold

Maximum money that the creature drops when killed, in copper.

### AIName

This field is overridden by ScriptName field if both are set.

| Name           | Description                                                                                         |
| -------------- | --------------------------------------------------------------------------------------------------- |
| NullCreatureAI | Empty AI, creature does nothing; cannot be charmed.                                                 |
| TriggerAI      | Same as "NullCreatureAI", except that the creature casts the spell from field spell1 when summoned. |
| AggressorAI    | Creature attacks when entering aggro radius; uses only melee attacks.                               |
| ReactorAI      | Creature attacks only if aggroed; uses only melee attacks.                                          |
| PassiveAI      | Creature behaves passive, cannot attack.                                                            |
| CritterAI      | Critter which flees if attacked.                                                                    |
| GuardAI        | Creature is a zone guard.                                                                           |
| PetAI          | Creature is a pet.                                                                                  |
| TotemAI        | Creature casts spell from field spell1; does not move.                                              |
| CombatAI       | Creature attacks as soon as something is in aggro range; uses also spells.                          |
| ArcherAI       | Creature casts spell from field spell1; chases the victim.                                          |
| TurretAI       | Creature attacks using spell from field spell1; does not move.                                      |
| VehicleAI      | Creature acts as player vehicle.                                                                    |
| SmartAI        | Creature uses the "[smart_scripts](smart_scripts)" table to specify it's behaviour.                 |

### MovementType

The creature's default movement type.

| ID  | Type                                              |
| --- | ------------------------------------------------- |
| 0   | Idle; stay in one place                           |
| 1   | Random movement inside the wander_distance radius |
| 2   | Waypoint movement                                 |

### HoverHeight

Distance above the ground that the creature will hover if it has MOVEMENTFLAG_DISABLE_GRAVITY enabled. Value taken from sniffs.

### HealthModifier

Used to modify the base Level/Class health of a creature. This field comes from WDB.

### ManaModifier

Used to modify the base Level/Class mana of a creature. This field comes from WDB.

### ArmorModifier

Used to modify the base Level/Class armor of a creature.

### ExperienceModifier

Used to modify the experience a player gets for killing the creature. The base experience is multiplied by this value, for example 2 gives double experience and 0 gives none.

Elite creatures already give double experience before this modifier is applied. Use the `CREATURE_FLAG_EXTRA_NO_XP` flag in [flags\_extra](#flagsextra) to make a creature give no experience at all.

### RacialLeader

A flag with two possible values: '1' or '0' indicating whether the creature is a racial leader or not. Killing racial leaders grants 100 honor.

| entry | name                     |
| ----- | ------------------------ |
| 2784  | King Magni Bronzebeard   |
| 3057  | Cairne Bloodhoof         |
| 4949  | Thrall                   |
| 7999  | Tyrande Whisperwind      |
| 10181 | Lady Sylvanas Windrunner |
| 16802 | Lor'themar Theron        |
| 17468 | Prophet Velen            |
| 29611 | King Varian Wrynn        |
| 36648 | Baine Bloodhoof (Leader) |
| 37764 | Lor'themar Theron        |

### movementId

We have no idea what this field does. It is passed directly to the client.

### RegenHealth

Boolean '1' or '0' controlling whether the creature should regenerate it's health or not.

### CreatureImmunitiesId

Reference to the `creature_immunities` table which centralises spell- and mechanic-based immunities.

For the detailed list of mechanics and spell-school bits, see [creature_immunities](creature_immunities).

### flags_extra

These flags control certain creature specific attributes. Flags can be added together to apply more than one.

**Example:** 32+64=96

| Value      | Hex          | Flag                                                | Comment                                                                                                                                |
| :--------- | :----------: | :-------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | `0x00000001` | CREATURE_FLAG_EXTRA_INSTANCE_BIND                   | creature kill binds instance to killer and killer's group                                                                              |
| 2          | `0x00000002` | CREATURE_FLAG_EXTRA_CIVILIAN                        | creature does not aggro (ignore faction/reputation hostility)                                                                          |
| 4          | `0x00000004` | CREATURE_FLAG_EXTRA_NO_PARRY                        | creature does not parry                                                                                                                |
| 8          | `0x00000008` | CREATURE_FLAG_EXTRA_NO_PARRY_HASTEN                 | creature does not counter-attack at parry                                                                                              |
| 16         | `0x00000010` | CREATURE_FLAG_EXTRA_NO_BLOCK                        | creature does not block                                                                                                                |
| 32         | `0x00000020` | CREATURE_FLAG_EXTRA_NO_CRUSHING_BLOWS               | creature does not do crush-attacks                                                                                                     |
| 64         | `0x00000040` | CREATURE_FLAG_EXTRA_NO_XP                           | creature kill does not give XP                                                                                                         |
| 128        | `0x00000080` | CREATURE_FLAG_EXTRA_TRIGGER                         | creature is trigger-NPC (invisible to players only)                                                                                    |
| 256        | `0x00000100` | CREATURE_FLAG_EXTRA_NO_TAUNT                        | creature is immune to taunt-auras and "attack me"-effects                                                                              |
| 512        | `0x00000200` | CREATURE_FLAG_EXTRA_NO_MOVE_FLAGS_UPDATE            | Creature won't update movement flags                                                                                                   |
| 1024       | `0x00000400` | CREATURE_FLAG_EXTRA_GHOST_VISIBILITY                | creature will be only visible for dead players                                                                                         |
| 2048       | `0x00000800` | CREATURE_FLAG_EXTRA_USE_OFFHAND_ATTACK              | creature will use offhand attacks                                                                                                      |
| 4096       | `0x00001000` | CREATURE_FLAG_EXTRA_NO_SELL_VENDOR                  | players can't sell items to this vendor                                                                                                |
| 8192       | `0x00002000` | CREATURE_FLAG_EXTRA_CANNOT_ENTER_COMBAT             | creature cannot enter combat (will not attack or be attacked)                                                                          |
| 16384      | `0x00004000` | CREATURE_FLAG_EXTRA_WORLDEVENT                      | custom flag for world events (left room for merging)                                                                                   |
| 32768      | `0x00008000` | CREATURE_FLAG_EXTRA_GUARD                           | creature is a guard (Will ignore feign death and vanish)                                                                               |
| 65536      | `0x00010000` | CREATURE_FLAG_EXTRA_IGNORE_FEIGN_DEATH              | creature ignores feign death                                                                                                           |
| 131072     | `0x00020000` | CREATURE_FLAG_EXTRA_NO_CRIT                         | creature does not do critical strikes                                                                                                  |
| 262144     | `0x00040000` | CREATURE_FLAG_EXTRA_NO_SKILL_GAINS                  | creature won't increase weapon skills                                                                                                  |
| 524288     | `0x00080000` | CREATURE_FLAG_EXTRA_OBEYS_TAUNT_DIMINISHING_RETURNS | creature taunt is subject to diminishing returns                                                                                       |
| 1048576    | `0x00100000` | CREATURE_FLAG_EXTRA_ALL_DIMINISH                    | Creature is subject to all diminishing returns                                                                                         |
| 2097152    | `0x00200000` | CREATURE_FLAG_EXTRA_NO_PLAYER_DAMAGE_REQ            | creature does not need to take player damage for kill credit                                                                           |
| 4194304    | `0x00400000` | CREATURE_FLAG_EXTRA_AVOID_AOE                       | ignored by aoe attacks (for icc blood prince council npc - Dark Nucleus)                                                               |
| 8388608    | `0x00800000` | CREATURE_FLAG_EXTRA_NO_DODGE                        | target cannot dodge                                                                                                                    |
| 16777216   | `0x01000000` | CREATURE_FLAG_EXTRA_MODULE                          | Used by module creatures to avoid blizzlike checks.                                                                                    |
| 33554432   | `0x02000000` | CREATURE_FLAG_EXTRA_DONT_CALL_ASSISTANCE            | Prevents creatures from calling for assistance on initial aggro                                                                        |
| 67108864   | `0x04000000` | CREATURE_FLAG_EXTRA_IGNORE_ALL_ASSISTANCE_CALLS     | Prevents creature from responding to assistance calls                                                                                  |
| 134217728  | `0x08000000` | CREATURE_FLAG_EXTRA_DONT_OVERRIDE_ENTRY_SAI         | Allows creatures to use both GUID and ENTRY specific SAI without one overwriting the other                                             |
| 268435456  | `0x10000000` | CREATURE_FLAG_EXTRA_DUNGEON_BOSS                    | Creature is a dungeon boss. This flag is generically set by core during runtime. Setting this in database will give you startup error. |
| 536870912  | `0x20000000` | CREATURE_FLAG_EXTRA_IGNORE_PATHFINDING              | Creature will ignore pathfinding. This is like disabling Mmaps, only for one creature.                                                 |
| 1073741824 | `0x40000000` | CREATURE_FLAG_EXTRA_IMMUNITY_KNOCKBACK              | creature will immune all knockback effects                                                                                             |
| 2147483648 | `0x80000000` | CREATURE_FLAG_EXTRA_HARD_RESET                      | Creature will despawn on evade                                                                                                         |

### ScriptName

The name of the script that this creature uses, if any. This ties a script from a scripting engine to this creature.

### VerifiedBuild

This field was used to determine whether a template has been verified from WDB files.

If value is 0 then it has not been parsed yet.

If value is above 0 then it has been parsed with WDB files from that specific client build.

If value is -1 then it is just a place holder until proper data are found on WDBs.

If value is -Client Build then it was parsed with WDB files from that specific [client build](http://archive.trinitycore.info/DB:Auth:realmlist#gamebuild "DB:Auth:realmlist") and manually edited later for some special necessity.
