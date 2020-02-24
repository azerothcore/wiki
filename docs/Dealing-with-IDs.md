# Dealing with IDs

If dealing with IDs it has to be ensured that the same ID is not used twice. Please use these ranges for new IDs and always check if the ID you chose is not already used by the core or one of the modules (see below for already existing IDs).

| ID type           | Table               | Field      | Reserved IDs for the core | Reserved IDs for modules | Reserved IDs for custom use | Max value  |
|-------------------|---------------------|------------|---------------------------|--------------------------|-----------------------------|------------|
| Creature ID       | creature_template   | entry      | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 16777215   |
| Creature GUID     | creature            | guid       | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 4294967295 |
| Gameobject ID     | gameobject_template | entry      | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 16777215   |
| Gameobject GUID   | gameobject          | guid       | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 4294967295 |
| NPC Text ID       | npc_text            | ID         | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 16777215   |
| Gossip Menu ID    | gossip_menu         | MenuID     | < 57000                   | >= 57000 < 60000         | >= 60000                    | 65535      |
| Broadcast Text ID | broadcast_text      | ID         | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 16777215   |
| Creature Text ID  | creature_text       | CreatureID | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 16777215   |
| ACore String ID   | acore_string        | entry      | < 4000000                 | >= 4000000 < 5000000     | >= 5000000                  | 16777215   |


# IDs already in use by modules

**The following IDs may not be used by the core or other modules!**


## Creature IDs

- Guild House Ver. 1: 70101
- Guild House Ver. 2: 55005

- NPC All Mounts: 601014
- NPC Enchanther: 601015
- NPC Buffer: 601016
- NPC Gambler: 601020
- NPC Codebox: 601021
- NPC Beastmaster: 601026
- NPC Morphsummon: 601072


- NPC Emblem Transfer: 100000
- NPC Transmog: 190010
- NPC Free Professions: 199999
- NPC Instance Reset: 300000

- NPC Services: 55002 (You can't have Services and Talent NPC at once)
- NPC Talent Template: 55002
- NPC Weapon Visual: 55003
- NPC Morph: 55004
- NPC Reward Shop: 92000


- Battleground: Slavery Valley 129999, 130000, 130001


To do:

* Different creature ID have to be used for NPC Services or Talent template.


## NPC Text IDs

- MorphSummon: 601072, 601073, 601074


## Gossip Menu IDs

- MorphSummon: 61072, 61073, 61074
