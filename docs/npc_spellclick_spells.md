# npc\_spellclick\_spells

[<-Back-to:World](database-world)

**The \`npc\_spellclick\_spells\` table**

This table holds information about spells to be cast upon receiving CMSG\_SPELLCLICK.

That opcode is sent for quests in which you have to loot creatures, who are already dead at spawning. Examples are [Planning for the Future](http://www.wowhead.com/quest=11960) and [Rifle the bodies](http://www.wowhead.com/quest=11999).

**Table: npc\_spellclick\_spells's Structure**

| Field                    | Type     |          | Null | Key | Default | Extra | Comment                                                                                               |
| :----------------------- | :------- | :------- | :--: | :-: | :-----: | :---: | :---------------------------------------------------------------------------------------------------- |
| [npc_entry](#npcentry)   | INT      | UNSIGNED | NO   | PRI |         |       | reference to creature_template                                                                        |
| [spell_id](#spellid)     | INT      | UNSIGNED | NO   | PRI |         |       | spell which should be casted                                                                          |
| [cast_flags](#castflags) | TINYINT  | UNSIGNED | NO   |     |         |       | first bit defines caster: 1=player, 0=creature; second bit defines target, same mapping as caster bit |
| [user_type](#usertype)   | SMALLINT | UNSIGNED | NO   |     | 0       |       | relation with summoner: 0-no 1-friendly 2-raid 3-party player can click                               |

**Description of the table's fields**

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
