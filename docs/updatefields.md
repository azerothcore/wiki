### UpdateFields

### General

**Block Value 2:** OBJECT_FIELD_TYPE:

| Value | Description           |
|-------|-----------------------|
| 3     | Item                  |
| 7     | Bag                   |
| 9     | Unit (creature)       |
| 25    | Player                |
| 33    | GameObject            |
| 65    | DynamicObject(spells) |
| 129   | Corpse                |

**Block Value 3:** OBJECT_FIELD_ENTRY: creature_template.entry, gameobject_template.entry
**Block Value 4:** OBJECT_FIELD_SCALE_X: creature_template.size, gameobject_template.size

### Creatures

| Name                                             | Index    | DB Field Name                                               |
|--------------------------------------------------|----------|-------------------------------------------------------------|
| UNIT_FIELD_CHARM                                 | 6-7      |                                                             |
| UNIT_FIELD_SUMMON                                | 8-9      |                                                             |
| UNIT_FIELD_CRITTER                               | 10-11    |                                                             |
| UNIT_FIELD_CHARMEDBY                             | 12-13    |                                                             |
| UNIT_FIELD_SUMMONEDBY                            | 14-15    |                                                             |
| UNIT_FIELD_CREATEDBY                             | 16-17    |                                                             |
| UNIT_FIELD_TARGET                                | 18-19    |                                                             |
| UNIT_FIELD_CHANNEL_OBJECT                        | 20-21    |                                                             |
| UNIT_CHANNEL_SPELL                               | 22       |                                                             |
| UNIT_FIELD_BYTES_0                               | 23       |                                                             |
| UNIT_FIELD_HEALTH                                | 24       |                                                             |
| UNIT_FIELD_POWER1                                | 25       |                                                             |
| UNIT_FIELD_POWER2                                | 26       |                                                             |
| UNIT_FIELD_POWER3                                | 27       |                                                             |
| UNIT_FIELD_POWER4                                | 28       |                                                             |
| UNIT_FIELD_POWER5                                | 29       |                                                             |
| UNIT_FIELD_POWER6                                | 30       |                                                             |
| UNIT_FIELD_POWER7                                | 31       |                                                             |
| UNIT_FIELD_MAXHEALTH                             | 32       |                                                             |
| UNIT_FIELD_MAXPOWER1                             | 33       |                                                             |
| UNIT_FIELD_MAXPOWER2                             | 34       |                                                             |
| UNIT_FIELD_MAXPOWER3                             | 35       |                                                             |
| UNIT_FIELD_MAXPOWER4                             | 36       |                                                             |
| UNIT_FIELD_MAXPOWER5                             | 37       |                                                             |
| UNIT_FIELD_MAXPOWER6                             | 38       |                                                             |
| UNIT_FIELD_MAXPOWER7                             | 39       |                                                             |
| UNIT_FIELD_POWER_REGEN_FLAT_MODIFIER             | 40-46    |                                                             |
| UNIT_FIELD_POWER_REGEN_INTERRUPTED_FLAT_MODIFIER | 47-53    |                                                             |
| UNIT_FIELD_LEVEL                                 | 54       | creature_template.minlevel OR maxlevel                      |
| UNIT_FIELD_FACTIONTEMPLATE                       | 55       | creature_template.faction_X                                 |
| UNIT_VIRTUAL_ITEM_SLOT_ID                        | 56,57,58 | creature_equip_template.equipentry1,equipentry2,equipentry3 |
| UNIT_FIELD_FLAGS                                 | 59       | creature_template.unit_flags                                |
| UNIT_FIELD_FLAGS_2                               | 60       |                                                             |
| UNIT_FIELD_AURASTATE                             | 61       |                                                             |
| UNIT_FIELD_BASEATTACKTIME                        | 62-63    | creature_template.baseattacktime                            |
| UNIT_FIELD_RANGEDATTACKTIME                      | 64       | creature_template.rangedattacktime                          |
| UNIT_FIELD_BOUNDINGRADIUS                        | 65       |                                                             |
| UNIT_FIELD_COMBATREACH                           | 66       |                                                             |
| UNIT_FIELD_DISPLAYID                             | 67       | creature_template.modelidX                                  |
| UNIT_FIELD_NATIVEDISPLAYID                       | 68       | creature_template.modelidX                                  |
| UNIT_FIELD_MOUNTDISPLAYID                        | 69       |                                                             |
| UNIT_FIELD_MINDAMAGE                             | 70       | creature_template.mindmg                                    |
| UNIT_FIELD_MAXDAMAGE                             | 71       | creature_template.maxdmg                                    |
| UNIT_FIELD_MINOFFHANDDAMAGE                      | 72       |                                                             |
| UNIT_FIELD_MAXOFFHANDDAMAGE                      | 73       |                                                             |
| UNIT_FIELD_BYTES_1                               | 74       | creature_addon.bytes1                                       |
| UNIT_FIELD_PETNUMBER                             | 75       |                                                             |
| UNIT_FIELD_PET_NAME_TIMESTAMP                    | 76       |                                                             |
| UNIT_FIELD_PETEXPERIENCE                         | 77       |                                                             |
| UNIT_FIELD_PETNEXTLEVELEXP                       | 78       |                                                             |
| UNIT_DYNAMIC_FLAGS                               | 79       | creature_template.dynamicflags                              |
| UNIT_MOD_CAST_SPEED                              | 80       |                                                             |
| UNIT_CREATED_BY_SPELL                            | 81       |                                                             |
| UNIT_NPC_FLAGS                                   | 82       | creature_template.npcflags                                  |
| UNIT_NPC_EMOTESTATE                              | 83       | creature_addon.emote                                        |
| UNIT_FIELD_STAT0                                 | 84       |                                                             |
| UNIT_FIELD_STAT1                                 | 85       |                                                             |
| UNIT_FIELD_STAT2                                 | 86       |                                                             |
| UNIT_FIELD_STAT3                                 | 87       |                                                             |
| UNIT_FIELD_STAT4                                 | 88       |                                                             |
| UNIT_FIELD_POSSTAT0                              | 89       |                                                             |
| UNIT_FIELD_POSSTAT1                              | 90       |                                                             |
| UNIT_FIELD_POSSTAT2                              | 91       |                                                             |
| UNIT_FIELD_POSSTAT3                              | 92       |                                                             |
| UNIT_FIELD_POSSTAT4                              | 93       |                                                             |
| UNIT_FIELD_NEGSTAT0                              | 94       |                                                             |
| UNIT_FIELD_NEGSTAT1                              | 95       |                                                             |
| UNIT_FIELD_NEGSTAT2                              | 96       |                                                             |
| UNIT_FIELD_NEGSTAT3                              | 97       |                                                             |
| UNIT_FIELD_NEGSTAT4                              | 98       |                                                             |
| UNIT_FIELD_RESISTANCES                           | 99-105   | creature_template.resistance1,resistance2,(...)resistance6  |
| UNIT_FIELD_RESISTANCEBUFFMODSPOSITIVE            | 106      |                                                             |
| UNIT_FIELD_RESISTANCEBUFFMODSNEGATIVE            | 113      |                                                             |
| UNIT_FIELD_BASE_MANA                             | 120      |                                                             |
| UNIT_FIELD_BASE_HEALTH                           | 121      |                                                             |
| UNIT_FIELD_BYTES_2                               | 122      | creature_addon.bytes2                                       |
| UNIT_FIELD_ATTACK_POWER                          | 123      | creature_template.attackpower                               |
| UNIT_FIELD_ATTACK_POWER_MODS                     | 124      |                                                             |
| UNIT_FIELD_ATTACK_POWER_MULTIPLIER               | 125      | creature_template.dmg_multiplier                            |
| UNIT_FIELD_RANGED_ATTACK_POWER                   | 126      | creature_template.rangedattackpower                         |
| UNIT_FIELD_RANGED_ATTACK_POWER_MODS              | 127      |                                                             |
| UNIT_FIELD_RANGED_ATTACK_POWER_MULTIPLIER        | 128      |                                                             |
| UNIT_FIELD_MINRANGEDDAMAGE                       | 129      | creature_template.minrangedmg                               |
| UNIT_FIELD_MAXRANGEDDAMAGE                       | 130      | creature_template.maxrangedmg                               |
| UNIT_FIELD_POWER_COST_MODIFIER                   | 131      |                                                             |
| UNIT_FIELD_POWER_COST_MULTIPLIER                 | 138-144  |                                                             |
| UNIT_FIELD_MAXHEALTHMODIFIER                     | 145      |                                                             |
| UNIT_FIELD_HOVERHEIGHT                           | 146      | creature_template.HoverHeight                               |
| UNIT_FIELD_PADDING                               | 147      |                                                             |

### Gameobjects

| Name                      | Index | DB Field Name                             |
|---------------------------|-------|-------------------------------------------|
| GAMEOBJECT_DISPLAYID      | 8     | gameobject_template.displayid             |
| GAMEOBJECT_FLAGS          | 9     | gameobject_template.flags                 |
| GAMEOBJECT_PARENTROTATION | 10-13 | gameobject.rotation1,rotation2,rotation3, |
| GAMEOBJECT_DYNAMIC        | 14    |                                           |
| GAMEOBJECT_FACTION        | 15    | gameobject_template.faction               |
| GAMEOBJECT_LEVEL          | 16    |                                           |
| GAMEOBJECT_BYTES_1        | 17    |                                           |

Source: https://trinitycore.atlassian.net/wiki/spaces/tc/pages/2129942/UpdateFields
