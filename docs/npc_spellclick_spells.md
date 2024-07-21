# npc\_spellclick\_spells

[<-Back-to:World](database-world)

**The \`npc\_spellclick\_spells\` table**

This table holds information about spells to be cast upon receiving CMSG\_SPELLCLICK.

That opcode is sent for quests in which you have to loot creatures, who are already dead at spawning. Examples are [Planning for the Future](http://www.wowhead.com/quest=11960) and [Rifle the bodies](http://www.wowhead.com/quest=11999).

**Table Structure**

| Field           | Type     | Attributes | Key | Null | Default | Extra | Comment                                                                 |
| --------------- | -------- | ---------- | --- | ---- | ------- | ----- | ----------------------------------------------------------------------- |
| [npc_entry][1]  | INT      | UNSIGNED   | PRI | NO   | NULL    |       | Reference to the creature_template table                                |
| [spell_id][2]   | INT      | UNSIGNED   | PRI | NO   | NULL    |       | The ID of the spell to be cast                                          |
| [cast_flags][3] | TINYINT  | UNSIGNED   |     | NO   | NULL    |       | Who casts the spell on who, creature <=> player (values: 0-3)           |
| [user_type][4]  | SMALLINT | UNSIGNED   |     | NO   | 0       |       | Relation with summoner: 0-no 1-friendly 2-raid 3-party player can click |

[1]: #npc_entry
[2]: #spell_id
[3]: #cast_flags
[4]: #user_type

**Description of the fields**

### npc\_entry

Reference to creature\_template.entry

### spell\_id

The spell which should be cast.

Note that for several quests there are more than one spell per click.

[Planing for the Future](http://www.wowhead.com/quest=11960) for example has [Planning for the Future: Create Snowfall Glade Pup](http://www.wowhead.com/spell=46773) which will create the item in the player’s inventory
and [Planning for the Future: Create Snowfall Glade Pup Cover](http://www.wowhead.com/spell=46167) which despawns the creature.

This creates the illusion that the creature has been looted.

### cast\_flags

On every spellclick event, a player and a creature "participate". This field defines who casts the spell on who.
Lower bit defines caster: 1=Clicker, 0=Clickee; higher bit defines target, same mapping as caster bit.
You can use that table for the actual value:

| Caster   | Target  | cast\_flags value |
| -------- | ------- | ----------------- |
| Creature | Clickee | 0                 |
| Clicker  | Clickee | 1                 |
| Clickee  | Clicker | 2                 |
| Clicker  | Clicker | 3                 |

### user\_type

Relation with summoner: defines who is able to use this spellclick.

| Value | Description |
| ----- | ----------- |
| 0     | Only self   |
| 1     | Friendly    |
| 2     | Raid        |
| 3     | Party       |
