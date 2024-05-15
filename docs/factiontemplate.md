---
redirect_from: "/FactionTemplate"
---

# FactionTemplate

**FactionTemplate.dbc**

[`Back-to:DBC`](dbc-index.md)

This DBC contains information on all of the individual factions. A faction entry from this DBC contains all of the needed data to calculate hostility, friendliness, or neutrality to any other faction in this DBC.

**IMPORTANT: These values are only used for the [creature\_template](creature_template) and [gameobject\_template](gameobject\_template) tables.**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## **Structure**

| Field Nb | Name                                     | Type             |
|----------|------------------------------------------|------------------|
| 1        | ID                                       | Int              |
| 2        | Name (Ref to [Faction.dbc](Faction.dbc)) | Int              |
| 4        | ourMask                                  | Bitmask (4 bits) |
| 5        | friendlyMask                             | Bitmask (4 bits) |
| 6        | hostileMask                              | Bitmask (4 bits) |
| 7-10     | enemyFactions                            | Int              |
| 11-14    | friendFactions                           | Int              |

# **Explanations & Calculations**

Each different entry has different relations towards any other faction.

The easiest calculation when calculating hostility or friendliness is to look at the Friend factions and Enemy factions columns in the table below. If our faction has the other faction's ID in the Enemy factions list, then it is hostile to that faction (at least). The same thing applies for a friendliness check on the Friend factions column.

If our faction doesn't have the other faction's ID in the enemy or friend faction list, then we'll have to get more complicated in calculating hostility or friendliness.

First, let's define the four faction groups:

| ID | Bit | Name                              |
|----|-----|-----------------------------------|
| 0  | 1   | All players (and pets)            |
| 1  | 2   | Alliance players (and their pets) |
| 2  | 4   | Horde players (and their pets)    |
| 3  | 8   | Monster (Not a player nor a pet)  |

The first mask (ourMask) defines what type of faction we are dealing with. Eg, faction 1 (PLAYER, Human) has 3 as ourMask; that means that it has the first two bits set so it classifies as both 'All players' and 'Alliance players'.

The second mask (friendlyMask) defines what faction groups this faction is friendly with. That means that if this field contains the bit for a faction group, then it is friendly with that faction. Eg, faction 5 (PLAYER, Undead) has 4 as friendlyMask; that means that it has the third bit set so it is friendly with 'Horde players'.

The third mask (hostileMask) defines what faction groups this faction is hostile with. This faction will be hostile to any faction group whose bit is set in this field. For example, let's examine the first two Stormwind factions. The first one (faction 11) has hostileMask 12. The binary representation of this is 1100, with the third and fourth bits set. The second Stormwind faction (faction 12) has hostileMask 4. The binary representation of this is 0100, with the third bit set. Applying the formulas to these two values, we can see that faction 11 is hostile to Horde players and also anything that is not a player while faction 12 is only hostile to Horde players. Faction 12 will not aggro any creature that is part of the monster faction group.

For the mathematically inclined, the basic formula to test for friendliness is

``` cpp
(friendlyMask & other.ourMask) != 0 
```

...where other is another faction. The same thing applies for hostility:

``` cpp
(hostileMask & other.ourMask) != 0
```

For the not so mathematically inclined, we'll have to compare two binary numbers. 
First, you will need to convert all of the masks to binary form with four digits; so 1 becomes 0001, 2 becomes 0010, 3 becomes 0011, etc.

Second, line up the friendlyMask or hostileMask value with the ourMask value. For example:

``` cpp
     1100 //hostileMask of faction 11
     1000 //ourMask of faction 14
```

Next, perform a logical 'AND' on the two numbers, the bottom one with the one on top and follow these rules:

-   1 and 1 is 1
-   1 and 0 is 0
-   0 and 1 is 0
-   0 and 0 is 0
    So, continuing our example:

```
    1100
    1000
    ----
    1000
```

Finally, check the result that you get with the value 0. Only 0000 will equal 0, anything else will not equal 0. If the result **'does not**' equal 0, then the faction is hostile/friendly to the other faction. In our example, it is obvious that we do not have 0 (we have 8 in fact if you convert to base 10 again), so faction 11 is hostile to faction 14 and will aggro it.

From all of the above calculations, we notice that if ourMask for a faction is 0 (that means 0000), it will be neutral to everything (not necessarily friendly). If the friendlyMask for a faction is 0, then it will never be friendly to anything or anyone (unless it has other faction IDs in the Friend factions column in the table below). Finally, if the hostileMask for a faction is 0, it will never be hostile to anything or anyone (again there may be exceptions in the Enemy factions column in the table below).

To summarize, you should follow these steps to calculate if faction A is hostile to faction B:

1.  Look for faction B in the Enemy faction list of faction A in the table below
    -   If found, then faction A is hostile to faction B and you can stop
    -   If not found, then continue with the next steps
2.  Look up hostileMask for faction A in table below
3.  Look up ourMask for faction B in table below
4.  Do the and (&) operation on the two values
    -   If the result is 0, then faction A is not hostile to faction B (but not necessarily friendly either)
    -   If the result is not 0, then faction A IS hostile to faction B

And these steps to calculate if faction A is friendly to faction B:

1.  Look for faction B in the Friend faction list of faction A in the table below
    -   If found, then faction A is friendly to faction B and you can stop
    -   If not found, then continue with the next steps
2.  Look up friendlyMask for faction A in table below
3.  Look up ourMask for faction B in table below
4.  Do the and (&) operation on the two values
    -   If the result is 0, then faction A is not friendly to faction B (but not necessarily hostile either)
    -   If the result is not 0, then faction A IS friendly to faction B

# **Content**

**Version is : 3.3.5a**

| ID   | Name                                | ourMask | friendlyMask | hostileMask | Enemy Factions      | Friend Factions   |
|------|-------------------------------------|---------|--------------|-------------|---------------------|-------------------|
| 1    | PLAYER, Human                       | 3       | 2            | 12          |                     |                   |
| 2    | PLAYER, Orc                         | 5       | 4            | 10          |                     |                   |
| 3    | PLAYER, Dwarf                       | 3       | 2            | 12          |                     |                   |
| 4    | PLAYER, Night Elf                   | 3       | 2            | 12          |                     |                   |
| 5    | PLAYER, Undead                      | 5       | 4            | 10          |                     |                   |
| 6    | PLAYER, Tauren                      | 5       | 4            | 10          |                     |                   |
| 7    | Creature                            | 0       | 0            | 0           |                     |                   |
| 10   | Escortee                            | 3       | 2            | 0           |                     |                   |
| 11   | Stormwind                           | 3       | 2            | 12          |                     |                   |
| 12   | Stormwind                           | 2       | 2            | 4           |                     | 72                |
| 14   | Monster                             | 8       | 0            | 1           |                     |                   |
| 15   | Creature                            | 0       | 0            | 0           |                     | 7                 |
| 16   | Monster                             | 8       | 0            | 1           |                     | 14                |
| 17   | Defias Brotherhood                  | 8       | 0            | 1           |                     | 15                |
| 18   | Murloc                              | 8       | 0            | 1           |                     | 19                |
| 19   | Gnoll - Redridge                    | 8       | 0            | 1           |                     | 17                |
| 20   | Gnoll - Riverpaw                    | 8       | 0            | 1           |                     | 16                |
| 21   | Undead, Scourge                     | 8       | 0            | 1           |                     | 20                |
| 22   | Beast - Spider                      | 8       | 0            | 1           |                     | 22                |
| 23   | Gnomeregan Exiles                   | 2       | 2            | 4           |                     |                   |
| 24   | Worgen                              | 8       | 0            | 1           |                     | 24                |
| 25   | Kobold                              | 8       | 0            | 0           |                     | 25                |
| 26   | Kobold                              | 8       | 0            | 1           |                     | 25                |
| 27   | Defias Brotherhood                  | 8       | 0            | 1           | 1                   | 15                |
| 28   | Troll, Bloodscalp                   | 8       | 0            | 1           |                     | 26                |
| 29   | Orgrimmar                           | 4       | 4            | 2           |                     |                   |
| 30   | Troll, Skullsplitter                | 8       | 0            | 1           |                     | 27                |
| 31   | Prey                                | 0       | 0            | 0           | 973                 | 148 28            |
| 32   | Beast - Wolf                        | 0       | 0            | 0           | 28                  |                   |
| 33   | Escortee                            | 5       | 4            | 0           |                     |                   |
| 34   | Defias Brotherhood                  | 8       | 0            | 0           |                     | 15                |
| 35   | Friendly                            | 0       | 1            | 0           |                     | 31                |
| 36   | Trogg                               | 0       | 0            | 0           |                     | 32                |
| 37   | Troll, Frostmane                    | 8       | 0            | 1           |                     | 33                |
| 38   | Beast - Wolf                        | 8       | 0            | 1           | 28                  | 29                |
| 39   | Gnoll - Shadowhide                  | 8       | 0            | 1           |                     | 18                |
| 40   | Orc, Blackrock                      | 8       | 0            | 1           |                     | 34                |
| 41   | Villian                             | 8       | 0            | 1           | 36                  | 35                |
| 42   | Victim                              | 1       | 1            | 0           |                     | 36                |
| 43   | Villian                             | 8       | 0            | 0           | 36                  | 35                |
| 44   | Beast - Bear                        | 8       | 0            | 1           |                     | 37                |
| 45   | Ogre                                | 8       | 0            | 1           |                     | 38                |
| 46   | Kurzen's Mercenaries                | 8       | 0            | 1           |                     | 39                |
| 47   | Venture Company                     | 8       | 0            | 1           |                     | 41                |
| 48   | Beast - Raptor                      | 8       | 0            | 1           |                     | 42                |
| 49   | Basilisk                            | 8       | 0            | 1           |                     | 43                |
| 50   | Dragonflight, Green                 | 8       | 0            | 1           |                     | 44                |
| 51   | Lost Ones                           | 8       | 0            | 1           | 46 40               | 45                |
| 52   | Gizlock's Dummy                     | 8       | 0            | 0           | 770                 |                   |
| 53   | Human, Night Watch                  | 2       | 2            | 12          |                     | 49                |
| 54   | Dark Iron Dwarves                   | 8       | 0            | 1           |                     | 48                |
| 55   | Ironforge                           | 2       | 2            | 4           |                     | 47                |
| 56   | Human, Night Watch                  | 2       | 2            | 12          |                     | 49                |
| 57   | Ironforge                           | 3       | 2            | 12          |                     |                   |
| 58   | Creature                            | 8       | 0            | 0           |                     |                   |
| 59   | Trogg                               | 8       | 0            | 1           |                     | 32                |
| 60   | Dragonflight, Red                   | 8       | 0            | 1           |                     | 50                |
| 61   | Gnoll - Mosshide                    | 8       | 0            | 1           |                     | 51                |
| 62   | Orc, Dragonmaw                      | 8       | 0            | 1           | 1015 932 934        | 52                |
| 63   | Gnome - Leper                       | 8       | 0            | 1           |                     | 53                |
| 64   | Gnomeregan Exiles                   | 2       | 2            | 4           |                     |                   |
| 65   | Orgrimmar                           | 0       | 0            | 0           | 45                  | 76                |
| 66   | Leopard                             | 8       | 0            | 1           | 28                  | 55                |
| 67   | Scarlet Crusade                     | 8       | 0            | 1           |                     | 56                |
| 68   | Undercity                           | 4       | 4            | 2           |                     |                   |
| 69   | Ratchet                             | 0       | 0            | 0           |                     | 470               |
| 70   | Gnoll - Rothide                     | 8       | 0            | 1           |                     | 57                |
| 71   | Undercity                           | 5       | 4            | 10          |                     |                   |
| 72   | Beast - Gorilla                     | 8       | 0            | 1           |                     | 58                |
| 73   | Beast - Carrion Bird                | 8       | 0            | 1           |                     | 669               |
| 74   | Naga                                | 8       | 0            | 1           | 289                 | 60                |
| 76   | Dalaran                             | 0       | 2            | 4           |                     | 61                |
| 77   | Forlorn Spirit                      | 8       | 0            | 0           |                     |                   |
| 78   | Darkhowl                            | 8       | 0            | 1           |                     |                   |
| 79   | Darnassus                           | 3       | 2            | 12          |                     |                   |
| 80   | Darnassus                           | 2       | 2            | 4           |                     | 69                |
| 81   | Grell                               | 8       | 0            | 1           |                     | 64                |
| 82   | Furbolg                             | 8       | 0            | 1           |                     | 65                |
| 83   | Horde Generic                       | 4       | 4            | 2           |                     |                   |
| 84   | Alliance Generic                    | 2       | 2            | 4           |                     |                   |
| 85   | Orgrimmar                           | 5       | 4            | 10          |                     |                   |
| 86   | Gizlock's Charm                     | 0       | 1            | 0           | 769                 | 771               |
| 87   | Syndicate                           | 8       | 0            | 1           |                     | 70                |
| 88   | Hillsbrad Militia                   | 2       | 2            | 4           |                     | 71                |
| 89   | Scarlet Crusade                     | 8       | 0            | 1           | 20                  | 56                |
| 90   | Demon                               | 8       | 0            | 1           |                     | 73                |
| 91   | Elemental                           | 8       | 0            | 1           |                     | 74                |
| 92   | Spirit                              | 8       | 0            | 1           |                     |                   |
| 93   | Monster                             | 8       | 0            | 1           |                     |                   |
| 94   | Treasure                            | 0       | 8            | 0           |                     |                   |
| 95   | Gnoll - Mudsnout                    | 8       | 0            | 1           |                     | 78                |
| 96   | HIllsbrad, Southshore Mayor         | 2       | 2            | 0           |                     |                   |
| 97   | Syndicate                           | 8       | 0            | 0           | 79                  | 70                |
| 98   | Undercity                           | 4       | 4            | 10          |                     |                   |
| 99   | Victim                              | 8       | 0            | 0           |                     |                   |
| 100  | Treasure                            | 0       | 0            | 9           |                     |                   |
| 101  | Treasure                            | 0       | 8            | 4           |                     |                   |
| 102  | Treasure                            | 0       | 8            | 2           |                     |                   |
| 103  | Dragonflight, Black                 | 8       | 0            | 1           | 689                 | 80                |
| 104  | Thunder Bluff                       | 4       | 4            | 2           |                     |                   |
| 105  | Thunder Bluff                       | 5       | 4            | 10          |                     |                   |
| 106  | Horde Generic                       | 4       | 4            | 10          |                     |                   |
| 107  | Troll, Frostmane                    | 8       | 0            | 1           |                     |                   |
| 108  | Syndicate                           | 0       | 0            | 0           | 79                  | 70                |
| 109  | Quilboar, Razormane 2               | 8       | 0            | 1           |                     | 110 111           |
| 110  | Quilboar, Razormane 2               | 8       | 0            | 1           | 85                  | 110               |
| 111  | Quilboar, Bristleback               | 8       | 0            | 1           |                     | 85 111            |
| 112  | Quilboar, Bristleback               | 8       | 0            | 1           | 110                 | 85 111            |
| 113  | Escortee                            | 1       | 1            | 0           |                     |                   |
| 114  | Treasure                            | 0       | 0            | 1           |                     |                   |
| 115  | PLAYER, Gnome                       | 3       | 2            | 12          |                     |                   |
| 116  | PLAYER, Troll                       | 5       | 4            | 10          |                     |                   |
| 118  | Undercity                           | 4       | 4            | 2           |                     |                   |
| 119  | Bloodsail Buccaneers                | 8       | 0            | 1           |                     | 87                |
| 120  | Booty Bay                           | 0       | 0            | 0           |                     | 21                |
| 121  | Booty Bay                           | 1       | 0            | 8           |                     | 21                |
| 122  | Ironforge                           | 2       | 2            | 4           |                     |                   |
| 123  | Stormwind                           | 2       | 2            | 4           |                     |                   |
| 124  | Darnassus                           | 2       | 2            | 4           |                     |                   |
| 125  | Orgrimmar                           | 4       | 4            | 2           |                     |                   |
| 126  | Darkspear Trolls                    | 4       | 4            | 2           |                     |                   |
| 127  | Villian                             | 0       | 0            | 1           |                     |                   |
| 128  | Blackfathom                         | 8       | 0            | 1           |                     | 88                |
| 129  | Makrura                             | 8       | 0            | 1           |                     | 89                |
| 130  | Centaur, Kolkar                     | 8       | 0            | 1           |                     | 90                |
| 131  | Centaur, Galak                      | 8       | 0            | 1           |                     | 91                |
| 132  | Gelkis Clan Centaur                 | 8       | 0            | 1           |                     | 92                |
| 133  | Magram Clan Centaur                 | 8       | 0            | 1           |                     | 93                |
| 134  | Maraudine                           | 8       | 0            | 1           |                     | 94                |
| 148  | Monster                             | 8       | 0            | 1           |                     |                   |
| 149  | Theramore                           | 2       | 2            | 0           |                     |                   |
| 150  | Theramore                           | 3       | 2            | 12          |                     |                   |
| 151  | Theramore                           | 2       | 0            | 4           |                     |                   |
| 152  | Quilboar, Razorfen                  | 8       | 0            | 1           |                     | 109 111           |
| 153  | Quilboar, Razorfen                  | 8       | 0            | 0           |                     | 109 111           |
| 154  | Quilboar, Deathshead                | 8       | 0            | 1           |                     | 109 85 111 110    |
| 168  | Enemy                               | 0       | 0            | 1           |                     |                   |
| 188  | Ambient                             | 0       | 0            | 0           |                     | 148 28            |
| 189  | Creature                            | 0       | 0            | 0           |                     |                   |
| 190  | Ambient                             | 0       | 0            | 0           |                     |                   |
| 208  | Nethergarde Caravan                 | 2       | 2            | 0           |                     | 168               |
| 209  | Nethergarde Caravan                 | 2       | 2            | 0           |                     | 168               |
| 210  | Alliance Generic                    | 2       | 2            | 12          |                     | 189               |
| 230  | Southsea Freebooters                | 8       | 0            | 1           |                     | 573               |
| 231  | Escortee                            | 3       | 2            | 8           |                     |                   |
| 232  | Escortee                            | 5       | 4            | 8           |                     |                   |
| 233  | Undead, Scourge                     | 8       | 0            | 1           | 68                  | 20                |
| 250  | Escortee                            | 1       | 1            | 8           |                     |                   |
| 270  | Wailing Caverns                     | 8       | 0            | 1           |                     | 229               |
| 290  | Escortee                            | 1       | 1            | 0           |                     |                   |
| 310  | Silithid                            | 8       | 0            | 1           |                     | 249               |
| 311  | Silithid                            | 8       | 0            | 0           |                     | 249               |
| 312  | Beast - Spider                      | 8       | 0            | 1           |                     | 22                |
| 330  | Wailing Caverns                     | 8       | 0            | 0           |                     | 229               |
| 350  | Blackfathom                         | 8       | 0            | 0           |                     | 88                |
| 370  | Armies of C'Thun                    | 8       | 8            | 1           | 912                 | 915               |
| 371  | Silvermoon Remnant                  | 2       | 2            | 4           |                     | 269               |
| 390  | Booty Bay                           | 0       | 0            | 0           | 60                  | 21                |
| 410  | Basilisk                            | 8       | 0            | 1           |                     | 43                |
| 411  | Beast - Bat                         | 8       | 0            | 1           |                     | 310               |
| 412  | The Defilers                        | 4       | 4            | 2           | 509                 | 510               |
| 413  | Scorpid                             | 8       | 0            | 1           |                     | 309               |
| 414  | Timbermaw Hold                      | 8       | 0            | 1           | 65                  | 576               |
| 415  | Titan                               | 8       | 0            | 1           |                     | 311               |
| 416  | Titan                               | 8       | 0            | 0           |                     |                   |
| 430  | Taskmaster Fizzule                  | 0       | 0            | 0           |                     |                   |
| 450  | Wailing Caverns                     | 8       | 0            | 1           | 40                  | 229               |
| 470  | Titan                               | 8       | 0            | 1           |                     |                   |
| 471  | Ravenholdt                          | 0       | 0            | 0           |                     | 349               |
| 472  | Syndicate                           | 8       | 0            | 1           | 349                 | 70                |
| 473  | Ravenholdt                          | 0       | 0            | 0           | 70                  | 349               |
| 474  | Gadgetzan                           | 0       | 0            | 0           |                     | 369               |
| 475  | Gadgetzan                           | 1       | 0            | 8           |                     | 369               |
| 494  | Gnomeregan Bug                      | 8       | 0            | 1           | 53                  | 389               |
| 495  | Escortee                            | 1       | 1            | 8           |                     | 40                |
| 514  | Harpy                               | 8       | 0            | 1           |                     | 409               |
| 534  | Alliance Generic                    | 2       | 2            | 0           |                     |                   |
| 554  | Burning Blade                       | 8       | 0            | 7           |                     | 429               |
| 574  | Shadowsilk Poacher                  | 8       | 0            | 1           | 450                 | 449               |
| 575  | Searing Spider                      | 8       | 0            | 1           |                     | 450               |
| 594  | Trogg                               | 8       | 0            | 0           |                     |                   |
| 614  | Victim                              | 0       | 1            | 0           |                     | 36                |
| 634  | Monster                             | 8       | 0            | 0           |                     |                   |
| 635  | Cenarion Circle                     | 0       | 0            | 0           |                     | 609               |
| 636  | Timbermaw Hold                      | 8       | 0            | 1           | 65                  | 576               |
| 637  | Ratchet                             | 1       | 0            | 8           |                     | 470               |
| 654  | Troll, Witherbark                   | 8       | 0            | 1           |                     | 82                |
| 655  | Centaur, Kolkar                     | 8       | 0            | 5           |                     | 90                |
| 674  | Dark Iron Dwarves                   | 0       | 0            | 0           |                     | 48                |
| 694  | Alliance Generic                    | 2       | 2            | 4           |                     | 189               |
| 695  | Hydraxian Waterlords                | 0       | 0            | 0           |                     | 749               |
| 714  | Horde Generic                       | 4       | 4            | 0           |                     |                   |
| 734  | Dark Iron Dwarves                   | 1       | 1            | 0           |                     | 48                |
| 735  | Goblin, Dark Iron Bar Patron        | 1       | 1            | 0           |                     | 489               |
| 736  | Goblin, Dark Iron Bar Patron        | 8       | 0            | 1           |                     | 489               |
| 754  | Dark Iron Dwarves                   | 8       | 0            | 1           | 34                  | 48                |
| 774  | Escortee                            | 3       | 2            | 0           |                     |                   |
| 775  | Escortee                            | 5       | 4            | 0           |                     |                   |
| 776  | Brood of Nozdormu                   | 0       | 0            | 0           | 249 80              | 910 531           |
| 777  | Might of Kalimdor                   | 1       | 1            | 0           | 915                 | 912               |
| 778  | Giant                               | 8       | 0            | 1           |                     | 511               |
| 794  | Argent Dawn                         | 1       | 0            | 0           |                     | 529               |
| 795  | Troll, Vilebranch                   | 8       | 0            | 1           |                     | 572               |
| 814  | Argent Dawn                         | 1       | 0            | 0           |                     | 529               |
| 834  | Elemental                           | 8       | 0            | 1           |                     | 74                |
| 854  | Everlook                            | 1       | 0            | 8           |                     | 577               |
| 855  | Everlook                            | 0       | 0            | 0           |                     | 577               |
| 874  | Wintersaber Trainers                | 2       | 2            | 4           |                     |                   |
| 875  | Gnomeregan Exiles                   | 2       | 2            | 4           |                     |                   |
| 876  | Darkspear Trolls                    | 4       | 4            | 2           |                     |                   |
| 877  | Darkspear Trolls                    | 5       | 4            | 10          |                     |                   |
| 894  | Theramore                           | 2       | 2            | 4           |                     | 108               |
| 914  | Training Dummy                      | 0       | 0            | 0           |                     |                   |
| 934  | Furbolg, Uncorrupted                | 8       | 0            | 1           |                     | 575               |
| 954  | Demon                               | 8       | 0            | 1           |                     | 73                |
| 974  | Undead, Scourge                     | 8       | 0            | 1           |                     | 20                |
| 994  | Cenarion Circle                     | 0       | 0            | 0           |                     | 609               |
| 995  | Thunder Bluff                       | 4       | 4            | 2           |                     |                   |
| 996  | Cenarion Circle                     | 1       | 0            | 8           | 249                 | 609               |
| 1014 | Shatterspear Trolls                 | 0       | 0            | 0           |                     | 629               |
| 1015 | Shatterspear Trolls                 | 0       | 0            | 0           |                     | 629               |
| 1034 | Horde Generic                       | 4       | 0            | 2           |                     |                   |
| 1054 | Alliance Generic                    | 3       | 2            | 12          |                     | 189               |
| 1055 | Alliance Generic                    | 2       | 2            | 4           |                     | 189               |
| 1074 | Orgrimmar                           | 4       | 4            | 2           |                     |                   |
| 1075 | Theramore                           | 2       | 2            | 4           |                     | 108               |
| 1076 | Darnassus                           | 2       | 2            | 4           |                     | 69                |
| 1077 | Theramore                           | 2       | 2            | 4           |                     | 108               |
| 1078 | Stormwind                           | 2       | 2            | 4           |                     | 72                |
| 1080 | Friendly                            | 0       | 1            | 0           | 74                  | 31 649            |
| 1081 | Elemental                           | 8       | 0            | 1           | 649                 | 74                |
| 1094 | Beast - Boar                        | 0       | 0            | 0           |                     |                   |
| 1095 | Training Dummy                      | 0       | 0            | 0           |                     |                   |
| 1096 | Theramore                           | 3       | 2            | 12          | 679                 |                   |
| 1097 | Darnassus                           | 2       | 2            | 4           |                     |                   |
| 1114 | Dragonflight, Black - Bait          | 8       | 0            | 1           | 80                  | 689               |
| 1134 | Undercity                           | 5       | 4            | 10          | 679                 |                   |
| 1154 | Undercity                           | 5       | 4            | 10          | 679                 |                   |
| 1174 | Orgrimmar                           | 4       | 4            | 2           |                     |                   |
| 1194 | Battleground Neutral                | 0       | 0            | 0           |                     |                   |
| 1214 | Frostwolf Clan                      | 5       | 4            | 10          | 730                 | 729               |
| 1215 | Frostwolf Clan                      | 4       | 4            | 2           | 730                 | 729               |
| 1216 | Stormpike Guard                     | 3       | 2            | 12          | 729                 | 730               |
| 1217 | Stormpike Guard                     | 2       | 2            | 4           | 729                 | 730               |
| 1234 | Sulfuron Firelords                  | 8       | 0            | 1           | 749                 | 750               |
| 1235 | Sulfuron Firelords                  | 8       | 0            | 1           | 749                 | 750               |
| 1236 | Sulfuron Firelords                  | 8       | 0            | 1           | 749                 | 750               |
| 1254 | Cenarion Circle                     | 1       | 0            | 8           |                     | 609               |
| 1274 | Creature                            | 0       | 0            | 4           |                     |                   |
| 1275 | Creature                            | 0       | 0            | 2           |                     |                   |
| 1294 | Gizlock                             | 8       | 0            | 1           | 770                 |                   |
| 1314 | Horde Generic                       | 4       | 4            | 2           |                     |                   |
| 1315 | Alliance Generic                    | 2       | 2            | 4           |                     |                   |
| 1334 | Stormpike Guard                     | 2       | 2            | 4           | 729                 | 730               |
| 1335 | Frostwolf Clan                      | 4       | 4            | 2           | 730                 | 729               |
| 1354 | Shen'dralar                         | 0       | 0            | 0           |                     | 809               |
| 1355 | Shen'dralar                         | 0       | 0            | 0           |                     | 809               |
| 1374 | Ogre (Captain Kromcrush)            | 8       | 0            | 1           |                     | 38                |
| 1375 | Treasure                            | 0       | 0            | 9           |                     |                   |
| 1394 | Dragonflight, Black                 | 8       | 0            | 1           | 689 47              | 80                |
| 1395 | Silithid Attackers                  | 8       | 0            | 1           |                     | 916               |
| 1414 | Spirit Guide - Alliance             | 0       | 0            | 4           |                     |                   |
| 1415 | Spirit Guide - Horde                | 0       | 0            | 2           |                     |                   |
| 1434 | Jaedenar                            | 8       | 0            | 1           |                     | 869               |
| 1454 | Victim                              | 0       | 1            | 0           | 35                  | 36                |
| 1474 | Thorium Brotherhood                 | 0       | 0            | 0           |                     | 59                |
| 1475 | Thorium Brotherhood                 | 0       | 0            | 0           |                     | 59                |
| 1494 | Horde Generic                       | 4       | 4            | 2           |                     | 66                |
| 1495 | Horde Generic                       | 5       | 4            | 10          |                     | 66                |
| 1496 | Horde Generic                       | 4       | 4            | 2           |                     | 66                |
| 1514 | Silverwing Sentinels                | 2       | 2            | 4           |                     |                   |
| 1515 | Warsong Outriders                   | 4       | 4            | 2           |                     |                   |
| 1534 | Stormpike Guard                     | 2       | 2            | 4           | 729                 | 730               |
| 1554 | Frostwolf Clan                      | 5       | 4            | 8           |                     |                   |
| 1555 | Darkmoon Faire                      | 0       | 0            | 0           |                     | 909               |
| 1574 | Zandalar Tribe                      | 0       | 0            | 0           |                     | 270               |
| 1575 | Stormwind                           | 3       | 2            | 12          |                     |                   |
| 1576 | Silvermoon Remnant                  | 2       | 2            | 4           |                     | 269               |
| 1577 | The League of Arathor               | 2       | 2            | 4           | 510                 | 509               |
| 1594 | Darnassus                           | 3       | 2            | 12          |                     |                   |
| 1595 | Orgrimmar                           | 5       | 4            | 10          |                     |                   |
| 1596 | Stormpike Guard                     | 3       | 2            | 12          | 729                 | 730               |
| 1597 | Frostwolf Clan                      | 5       | 4            | 10          | 730                 | 729               |
| 1598 | The Defilers                        | 4       | 4            | 2           | 509                 | 510               |
| 1599 | The League of Arathor               | 2       | 2            | 4           | 510                 | 509               |
| 1600 | Darnassus                           | 2       | 2            | 8           |                     |                   |
| 1601 | Brood of Nozdormu                   | 0       | 0            | 0           | 249 80              | 910 531           |
| 1602 | Silvermoon City                     | 4       | 4            | 2           |                     |                   |
| 1603 | Silvermoon City                     | 5       | 4            | 10          |                     |                   |
| 1604 | Silvermoon City                     | 4       | 4            | 2           |                     |                   |
| 1605 | Dragonflight, Bronze                | 0       | 0            | 1           |                     | 531               |
| 1606 | Creature                            | 0       | 4            | 2           | 7                   |                   |
| 1607 | Creature                            | 0       | 4            | 2           | 7                   |                   |
| 1608 | Cenarion Circle                     | 1       | 0            | 8           | 249                 | 609               |
| 1610 | PLAYER, Blood Elf                   | 5       | 4            | 10          |                     |                   |
| 1611 | Ironforge                           | 3       | 2            | 4           | 916                 |                   |
| 1612 | Orgrimmar                           | 5       | 4            | 2           | 916                 |                   |
| 1613 | Might of Kalimdor                   | 1       | 1            | 0           | 915                 | 912               |
| 1614 | Monster                             | 8       | 0            | 1           |                     | 14                |
| 1615 | Steamwheedle Cartel                 | 1       | 0            | 8           |                     | 21 577 369        |
| 1616 | RC Objects                          | 0       | 15           | 0           | 918                 | 919               |
| 1617 | RC Enemies                          | 0       | 0            | 1           | 919                 | 918               |
| 1618 | Ironforge                           | 2       | 2            | 12          |                     |                   |
| 1619 | Orgrimmar                           | 4       | 4            | 10          |                     |                   |
| 1620 | Enemy                               | 0       | 0            | 15          |                     |                   |
| 1621 | Blue                                | 2       | 0            | 4           | 920                 |                   |
| 1622 | Red                                 | 2       | 0            | 4           | 921                 |                   |
| 1623 | Tranquillien                        | 4       | 4            | 2           |                     |                   |
| 1624 | Argent Dawn                         | 1       | 0            | 8           |                     | 529               |
| 1625 | Argent Dawn                         | 1       | 0            | 8           |                     | 529               |
| 1626 | Undead, Scourge                     | 8       | 0            | 1           | 679                 | 20                |
| 1627 | Farstriders                         | 4       | 4            | 2           |                     |                   |
| 1628 | Tranquillien                        | 4       | 4            | 2           |                     |                   |
| 1629 | PLAYER, Draenei                     | 3       | 2            | 12          |                     |                   |
| 1630 | Scourge Invaders                    | 8       | 0            | 7           | 14 148              | 928 20            |
| 1634 | Scourge Invaders                    | 8       | 0            | 0           | 68 72               | 928 20            |
| 1635 | Steamwheedle Cartel                 | 0       | 0            | 0           | 891                 | 169 892           |
| 1636 | Farstriders                         | 4       | 4            | 2           |                     |                   |
| 1637 | Farstriders                         | 4       | 4            | 2           |                     |                   |
| 1638 | Exodar                              | 2       | 2            | 4           |                     |                   |
| 1639 | Exodar                              | 3       | 2            | 12          |                     |                   |
| 1640 | Exodar                              | 2       | 2            | 4           |                     |                   |
| 1641 | Warsong Outriders                   | 4       | 4            | 2           |                     |                   |
| 1642 | Silverwing Sentinels                | 2       | 2            | 4           |                     |                   |
| 1643 | Troll, Forest                       | 8       | 0            | 1           |                     | 937               |
| 1644 | The Sons of Lothar                  | 2       | 2            | 4           |                     |                   |
| 1645 | The Sons of Lothar                  | 3       | 2            | 12          |                     |                   |
| 1646 | Exodar                              | 2       | 2            | 4           |                     |                   |
| 1647 | Exodar                              | 3       | 2            | 12          |                     |                   |
| 1648 | The Sons of Lothar                  | 2       | 2            | 4           |                     | 72                |
| 1649 | The Sons of Lothar                  | 2       | 2            | 4           |                     | 72                |
| 1650 | The Mag'har                         | 5       | 4            | 10          |                     |                   |
| 1651 | The Mag'har                         | 4       | 4            | 2           | 28                  |                   |
| 1652 | The Mag'har                         | 4       | 4            | 2           |                     |                   |
| 1653 | The Mag'har                         | 4       | 4            | 2           |                     |                   |
| 1654 | Exodar                              | 2       | 2            | 4           |                     | 69                |
| 1655 | Exodar                              | 2       | 2            | 4           |                     | 69                |
| 1656 | Silvermoon City                     | 5       | 4            | 10          |                     |                   |
| 1657 | Silvermoon City                     | 4       | 4            | 2           |                     |                   |
| 1658 | Silvermoon City                     | 4       | 4            | 2           |                     |                   |
| 1659 | Cenarion Expedition                 | 1       | 0            | 8           | 60                  | 942               |
| 1660 | Cenarion Expedition                 | 1       | 0            | 8           |                     | 942               |
| 1661 | Cenarion Expedition                 | 1       | 0            | 8           |                     | 942               |
| 1662 | Fel Orc                             | 8       | 0            | 1           |                     | 943               |
| 1663 | Fel Orc Ghost                       | 8       | 0            | 1           | 945                 | 944               |
| 1664 | Sons of Lothar Ghosts               | 8       | 0            | 1           | 944                 | 945               |
| 1665 | None                                | 1       | 7            | 8           |                     |                   |
| 1666 | Honor Hold                          | 3       | 2            | 12          |                     |                   |
| 1667 | Honor Hold                          | 2       | 2            | 4           |                     | 72                |
| 1668 | Thrallmar                           | 5       | 4            | 10          |                     |                   |
| 1669 | Thrallmar                           | 4       | 4            | 2           |                     |                   |
| 1670 | Thrallmar                           | 4       | 4            | 2           |                     |                   |
| 1671 | Honor Hold                          | 2       | 2            | 4           |                     |                   |
| 1672 | Test Faction 1                      | 1       | 7            | 0           | 952                 | 949               |
| 1673 | ToWoW - Flag                        | 0       | 0            | 0           | 951                 | 950               |
| 1674 | Test Faction 4                      | 0       | 15           | 0           | 951                 | 950 953           |
| 1675 | Test Faction 3                      | 0       | 15           | 0           | 949                 | 952               |
| 1676 | ToWoW - Flag Trigger Horde (DND)    | 0       | 15           | 0           |                     | 954               |
| 1677 | ToWoW - Flag Trigger Alliance (DND) | 0       | 15           | 0           |                     | 954               |
| 1678 | Ethereum                            | 8       | 0            | 1           |                     | 956               |
| 1679 | Broken                              | 8       | 0            | 1           | 40                  | 955               |
| 1680 | Elemental                           | 0       | 1            | 0           | 957                 | 74                |
| 1681 | Earth Elemental                     | 8       | 0            | 1           | 74                  | 74                |
| 1682 | Fighting Robots                     | 0       | 0            | 0           | 958                 |                   |
| 1683 | Actor Good                          | 0       | 0            | 0           | 960                 | 959               |
| 1684 | Actor Evil                          | 0       | 0            | 0           | 959                 | 960               |
| 1685 | Stillpine Furbolg                   | 2       | 0            | 4           |                     | 961               |
| 1686 | Stillpine Furbolg                   | 2       | 2            | 4           | 962                 | 961               |
| 1687 | Crazed Owlkin                       | 8       | 0            | 1           | 961                 | 962               |
| 1688 | Chess Alliance                      | 0       | 1            | 0           | 964                 | 963               |
| 1689 | Chess Horde                         | 0       | 1            | 0           | 963                 | 964               |
| 1690 | Chess Alliance                      | 0       | 1            | 0           | 964                 | 963               |
| 1691 | Chess Horde                         | 0       | 1            | 0           | 963                 | 964               |
| 1692 | Monster Spar                        | 8       | 8            | 1           | 966                 | 965               |
| 1693 | Monster Spar Buddy                  | 8       | 8            | 1           | 965                 | 966               |
| 1694 | Exodar                              | 2       | 2            | 4           |                     |                   |
| 1695 | Silvermoon City                     | 4       | 4            | 2           |                     |                   |
| 1696 | The Violet Eye                      | 0       | 0            | 0           |                     | 967               |
| 1697 | Fel Orc                             | 8       | 0            | 1           | 946 947             | 943               |
| 1698 | Exodar                              | 2       | 2            | 4           | 968                 | 930               |
| 1699 | Exodar                              | 2       | 2            | 4           | 968                 | 930               |
| 1700 | Exodar                              | 2       | 2            | 4           | 968                 | 930               |
| 1701 | Sunhawks                            | 8       | 0            | 7           | 930                 | 968               |
| 1702 | Sunhawks                            | 8       | 0            | 7           | 930                 | 968               |
| 1703 | Training Dummy                      | 0       | 0            | 0           |                     |                   |
| 1704 | Fel Orc                             | 8       | 0            | 1           | 679                 | 943               |
| 1705 | Fel Orc                             | 8       | 0            | 1           |                     | 943 679           |
| 1706 | Fungal Giant                        | 8       | 0            | 1           | 970                 | 971               |
| 1707 | Sporeggar                           | 1       | 0            | 8           |                     | 970               |
| 1708 | Sporeggar                           | 1       | 0            | 8           |                     | 970               |
| 1709 | Sporeggar                           | 1       | 0            | 8           | 971                 | 970               |
| 1710 | Cenarion Expedition                 | 1       | 0            | 8           |                     | 942               |
| 1711 | Monster, Predator                   | 8       | 0            | 1           | 974                 | 973               |
| 1712 | Monster, Prey                       | 8       | 0            | 1           |                     | 974               |
| 1713 | Monster, Prey                       | 8       | 0            | 1           |                     | 974               |
| 1714 | Sunhawks                            | 8       | 0            | 7           | 930 975             | 968               |
| 1715 | Void Anomaly                        | 8       | 0            | 1           |                     | 975               |
| 1716 | Hyjal Defenders                     | 0       | 1            | 8           |                     | 976               |
| 1717 | Hyjal Defenders                     | 0       | 1            | 0           |                     | 976               |
| 1718 | Hyjal Defenders                     | 0       | 1            | 0           | 977                 | 976               |
| 1719 | Hyjal Defenders                     | 0       | 1            | 8           |                     | 976               |
| 1720 | Hyjal Invaders                      | 8       | 0            | 1           | 976                 | 977               |
| 1721 | Kurenai                             | 3       | 2            | 12          |                     | 978               |
| 1722 | Kurenai                             | 2       | 2            | 4           |                     | 978               |
| 1723 | Kurenai                             | 2       | 2            | 4           |                     | 978               |
| 1724 | Kurenai                             | 2       | 2            | 4           |                     | 978               |
| 1725 | Earthen Ring                        | 0       | 7            | 8           |                     | 469 67            |
| 1726 | Earthen Ring                        | 0       | 7            | 0           |                     | 469 67            |
| 1727 | Earthen Ring                        | 0       | 7            | 8           |                     | 469 67            |
| 1728 | Cenarion Expedition                 | 1       | 0            | 8           | 14                  | 942               |
| 1729 | Thrallmar                           | 4       | 4            | 2           |                     |                   |
| 1730 | The Consortium                      | 1       | 0            | 8           |                     | 933               |
| 1731 | The Consortium                      | 1       | 0            | 8           |                     | 933               |
| 1732 | Alliance Generic                    | 2       | 2            | 4           |                     |                   |
| 1733 | Alliance Generic                    | 2       | 2            | 4           |                     |                   |
| 1734 | Horde Generic                       | 4       | 4            | 2           |                     |                   |
| 1735 | Horde Generic                       | 4       | 4            | 2           |                     |                   |
| 1736 | Monster Spar Buddy                  | 8       | 8            | 0           | 965                 | 966               |
| 1737 | Honor Hold                          | 2       | 2            | 4           |                     | 72                |
| 1738 | Arakkoa                             | 8       | 0            | 1           |                     | 981               |
| 1739 | Zangarmarsh Banner (Alliance)       | 0       | 0            | 1           |                     | 982               |
| 1740 | Zangarmarsh Banner (Horde)          | 0       | 0            | 1           |                     | 982               |
| 1741 | The Sha'tar                         | 1       | 0            | 8           |                     | 935               |
| 1742 | Zangarmarsh Banner (Neutral)        | 0       | 0            | 1           |                     | 984               |
| 1743 | The Aldor                           | 0       | 0            | 0           |                     | 932               |
| 1744 | The Scryers                         | 0       | 0            | 0           |                     | 934               |
| 1745 | Silvermoon City                     | 4       | 4            | 2           | 679                 |                   |
| 1746 | The Scryers                         | 0       | 0            | 0           |                     | 934               |
| 1747 | Caverns of Time - Thrall            | 1       | 1            | 0           | 986 987             | 985               |
| 1748 | Caverns of Time - Durnholde         | 8       | 0            | 1           | 985                 | 986               |
| 1749 | Caverns of Time - Southshore Guards | 0       | 0            | 0           | 985                 | 987               |
| 1750 | Shadow Council Covert               | 8       | 0            | 1           |                     | 14                |
| 1751 | Monster                             | 8       | 0            | 1           | 932 935             |                   |
| 1752 | Dark Portal Attacker, Legion        | 8       | 0            | 7           | 991 992 943 529     | 993               |
| 1753 | Dark Portal Attacker, Legion        | 8       | 0            | 7           | 991 992 943 529     | 993               |
| 1754 | Dark Portal Attacker, Legion        | 8       | 0            | 7           | 991 992 943 529     | 993               |
| 1755 | Dark Portal Defender, Alliance      | 2       | 2            | 0           | 993                 | 991 992           |
| 1756 | Dark Portal Defender, Alliance      | 2       | 2            | 0           | 993                 | 991 992           |
| 1757 | Dark Portal Defender, Alliance      | 2       | 2            | 0           | 993                 | 991 992           |
| 1758 | Dark Portal Defender, Horde         | 4       | 4            | 0           | 993                 | 992 991           |
| 1759 | Dark Portal Defender, Horde         | 4       | 4            | 0           | 993                 | 992 991           |
| 1760 | Dark Portal Defender, Horde         | 4       | 4            | 0           | 993                 | 992 991           |
| 1761 | Inciter Trigger                     | 0       | 0            | 15          | 994                 |                   |
| 1762 | Inciter Trigger 2                   | 0       | 0            | 7           | 996 997 998 994     |                   |
| 1763 | Inciter Trigger 3                   | 0       | 0            | 7           | 997 998 994 995     |                   |
| 1764 | Inciter Trigger 4                   | 0       | 0            | 7           | 998 994 995 996     |                   |
| 1765 | Inciter Trigger 5                   | 0       | 0            | 7           | 994 995 996 997     |                   |
| 1766 | Argent Dawn                         | 0       | 0            | 0           | 993                 | 529               |
| 1767 | Argent Dawn                         | 0       | 0            | 0           | 993                 | 529               |
| 1768 | Demon                               | 0       | 0            | 15          | 14 529              | 73                |
| 1769 | Demon                               | 0       | 0            | 15          | 14 529              | 73                |
| 1770 | Actor Good                          | 0       | 1            | 0           | 960                 | 959               |
| 1771 | Actor Evil                          | 0       | 0            | 1           | 959                 | 960               |
| 1772 | Mana Creature                       | 8       | 0            | 1           | 968                 | 999               |
| 1773 | Khadgar's Servant                   | 0       | 1            | 0           |                     | 1000              |
| 1774 | Friendly                            | 0       | 1            | 0           | 1000                | 31                |
| 1775 | The Sha'tar                         | 1       | 0            | 8           |                     | 935               |
| 1776 | The Aldor                           | 0       | 0            | 0           | 1010                | 932               |
| 1777 | The Aldor                           | 0       | 0            | 0           |                     | 932               |
| 1778 | The Scale of the Sands              | 0       | 0            | 0           |                     | 990               |
| 1779 | Keepers of Time                     | 0       | 0            | 0           |                     | 989               |
| 1780 | Bladespire Clan                     | 8       | 0            | 1           | 929                 | 1001              |
| 1781 | Bloodmaul Clan                      | 8       | 0            | 1           | 1001                | 929               |
| 1782 | Bladespire Clan                     | 8       | 0            | 1           | 929                 | 1001              |
| 1783 | Bloodmaul Clan                      | 8       | 0            | 1           | 1001                | 929               |
| 1784 | Bladespire Clan                     | 8       | 0            | 1           | 929                 | 1001              |
| 1785 | Bloodmaul Clan                      | 8       | 0            | 1           | 1001                | 929               |
| 1786 | Demon                               | 8       | 0            | 1           |                     | 73                |
| 1787 | Monster                             | 8       | 0            | 1           | 994                 | 14                |
| 1788 | The Consortium                      | 1       | 0            | 8           | 968                 | 933               |
| 1789 | Sunhawks                            | 8       | 0            | 7           | 933                 | 968               |
| 1790 | Bladespire Clan                     | 8       | 0            | 1           | 929                 | 1001              |
| 1791 | Bloodmaul Clan                      | 8       | 0            | 1           | 1001                | 929               |
| 1792 | Fel Orc                             | 8       | 0            | 1           |                     | 943               |
| 1793 | Sunhawks                            | 8       | 0            | 7           | 930                 | 968               |
| 1794 | Protectorate                        | 0       | 1            | 0           |                     | 1003              |
| 1795 | Protectorate                        | 0       | 1            | 0           | 956                 | 1003              |
| 1796 | Ethereum                            | 8       | 0            | 1           | 1003                | 956               |
| 1797 | Protectorate                        | 0       | 1            | 0           |                     | 1003              |
| 1798 | Arcane Annihilator (DNR)            | 8       | 0            | 1           |                     | 968 1004          |
| 1799 | Ethereum Sparbuddy                  | 8       | 0            | 1           | 956                 | 1002              |
| 1800 | Ethereum                            | 8       | 0            | 1           | 1002                | 956               |
| 1801 | Horde                               | 5       | 4            | 10          |                     |                   |
| 1802 | Alliance                            | 3       | 2            | 12          |                     |                   |
| 1803 | Ambient                             | 0       | 0            | 4           |                     |                   |
| 1804 | Ambient                             | 0       | 0            | 2           |                     |                   |
| 1805 | The Aldor                           | 1       | 1            | 0           |                     | 932               |
| 1806 | Friendly                            | 0       | 1            | 8           |                     | 31                |
| 1807 | Protectorate                        | 1       | 1            | 8           |                     | 1003              |
| 1808 | Kirin'Var - Belmara                 | 8       | 0            | 1           |                     | 1007              |
| 1809 | Kirin'Var - Cohlien                 | 8       | 0            | 1           |                     | 1009              |
| 1810 | Kirin'Var - Dathric                 | 8       | 0            | 1           |                     | 1006              |
| 1811 | Kirin'Var - Luminrath               | 8       | 0            | 1           |                     | 1008              |
| 1812 | Friendly                            | 0       | 1            | 8           |                     | 31                |
| 1813 | Servant of Illidan                  | 8       | 0            | 1           | 1023                | 1010              |
| 1814 | Monster Spar Buddy                  | 8       | 8            | 1           | 965                 | 966               |
| 1815 | Beast - Wolf                        | 8       | 0            | 1           | 28                  | 29                |
| 1816 | Friendly                            | 0       | 1            | 0           |                     | 31                |
| 1818 | Lower City                          | 0       | 0            | 0           |                     | 1011              |
| 1819 | Alliance Generic                    | 2       | 2            | 12          | 73                  | 471               |
| 1820 | Ashtongue Deathsworn                | 0       | 0            | 0           |                     | 1012              |
| 1821 | Spirits of Shadowmoon 1             | 0       | 1            | 0           |                     | 1013              |
| 1822 | Spirits of Shadowmoon 2             | 0       | 1            | 0           |                     | 1013              |
| 1823 | Ethereum                            | 8       | 0            | 1           |                     | 956               |
| 1824 | Netherwing                          | 0       | 0            | 0           |                     | 1015              |
| 1825 | Demon                               | 0       | 0            | 15          | 14 529              | 73                |
| 1826 | Servant of Illidan                  | 8       | 0            | 1           | 73 1023             | 1010              |
| 1827 | Wyrmcult                            | 8       | 0            | 1           |                     | 1016              |
| 1828 | Treant                              | 0       | 0            | 0           | 1016                | 1017              |
| 1829 | Leotheras Demon I                   | 0       | 1            | 0           |                     | 1018 14           |
| 1830 | Leotheras Demon II                  | 0       | 1            | 0           |                     | 1019 14           |
| 1831 | Leotheras Demon III                 | 0       | 1            | 0           |                     | 1020 14           |
| 1832 | Leotheras Demon IV                  | 0       | 1            | 0           |                     | 1021 14           |
| 1833 | Leotheras Demon V                   | 0       | 1            | 0           |                     | 1022 14           |
| 1834 | Azaloth                             | 0       | 0            | 15          | 14 1010             | 1023              |
| 1835 | Horde Generic                       | 4       | 4            | 10          | 73                  | 471               |
| 1836 | The Consortium                      | 1       | 0            | 8           |                     | 933               |
| 1837 | Sporeggar                           | 1       | 0            | 8           | 971                 | 970               |
| 1838 | The Scryers                         | 0       | 0            | 0           | 1010                | 934               |
| 1839 | Rock Flayer                         | 8       | 0            | 1           | 1025                | 1024              |
| 1840 | Flayer Hunter                       | 1       | 7            | 0           | 1024                | 1025              |
| 1841 | Shadowmoon Shade                    | 0       | 1            | 0           |                     | 1026              |
| 1842 | Legion Communicator                 | 0       | 0            | 1           |                     |                   |
| 1843 | Servant of Illidan                  | 8       | 0            | 1           | 932 934 1033 1012   | 1010              |
| 1844 | The Aldor                           | 0       | 0            | 0           | 1010                | 932               |
| 1845 | The Scryers                         | 0       | 0            | 0           | 1010                | 934               |
| 1846 | Ravenswood Ancients                 | 8       | 0            | 1           |                     | 1028              |
| 1847 | Monster Spar                        | 8       | 8            | 1           | 966                 | 965               |
| 1848 | Monster Spar Buddy                  | 8       | 8            | 1           | 965                 | 966               |
| 1849 | Servant of Illidan                  | 8       | 0            | 1           | 1023                | 1010              |
| 1850 | Netherwing                          | 0       | 0            | 0           | 52                  | 1015              |
| 1851 | Lower City                          | 1       | 0            | 8           |                     | 1011              |
| 1852 | Chess, Friendly to All Chess        | 0       | 1            | 0           |                     | 963 964 1029      |
| 1853 | Servant of Illidan                  | 8       | 0            | 1           | 932 934             | 1010              |
| 1854 | The Aldor                           | 0       | 0            | 0           | 1030                | 932 934           |
| 1855 | The Scryers                         | 0       | 0            | 0           | 1030                | 934 932           |
| 1856 | Sha'tari Skyguard                   | 1       | 0            | 0           |                     | 1031              |
| 1857 | Friendly                            | 1       | 1            | 8           |                     | 1032              |
| 1858 | Ashtongue Deathsworn                | 0       | 1            | 0           | 1030                | 932 934 1012 1033 |
| 1859 | Maiev                               | 0       | 1            | 0           | 1030                | 932 934 1012 1033 |
| 1860 | Skettis Shadowy Arakkoa             | 0       | 1            | 0           |                     | 1034              |
| 1862 | Skettis Arakkoa                     | 8       | 0            | 1           |                     | 1035              |
| 1863 | Orc, Dragonmaw                      | 8       | 0            | 1           | 1015 1036 932 934   | 52                |
| 1864 | Dragonmaw Enemy                     | 8       | 0            | 1           | 52                  | 14                |
| 1865 | Orc, Dragonmaw                      | 8       | 0            | 1           |                     | 52                |
| 1866 | Ashtongue Deathsworn                | 1       | 0            | 0           | 1010                | 1012              |
| 1867 | Maiev                               | 0       | 1            | 0           | 1010                | 932 934 1012 1033 |
| 1868 | Monster Spar Buddy                  | 0       | 1            | 0           | 965                 | 966               |
| 1869 | Arakkoa                             | 8       | 0            | 0           |                     | 1035              |
| 1870 | Sha'tari Skyguard                   | 1       | 0            | 0           |                     | 1031              |
| 1871 | Skettis Arakkoa                     | 8       | 0            | 1           |                     | 1035              |
| 1872 | Ogri'la                             | 1       | 0            | 0           |                     | 1038              |
| 1873 | Rock Flayer                         | 8       | 0            | 1           |                     | 1024              |
| 1874 | Ogri'la                             | 1       | 0            | 0           |                     | 1038              |
| 1875 | The Aldor                           | 0       | 0            | 0           | 52                  | 932               |
| 1876 | The Scryers                         | 0       | 0            | 0           | 52                  | 934               |
| 1877 | Orc, Dragonmaw                      | 8       | 0            | 1           | 1015 932 934        | 52                |
| 1878 | Frenzy                              | 8       | 0            | 1           |                     | 1041              |
| 1879 | Skyguard Enemy                      | 8       | 0            | 1           | 1031                | 1042              |
| 1880 | Orc, Dragonmaw                      | 8       | 0            | 1           |                     | 52                |
| 1881 | Skettis Arakkoa                     | 8       | 0            | 1           |                     | 1035              |
| 1882 | Servant of Illidan                  | 8       | 0            | 1           | 1023                | 1010              |
| 1883 | Theramore Deserter                  | 8       | 0            | 7           |                     | 1044              |
| 1884 | Tuskarr                             | 8       | 8            | 1           |                     |                   |
| 1885 | Vrykul                              | 8       | 0            | 1           |                     | 1045              |
| 1886 | Creature                            | 8       | 0            | 1           |                     | 7                 |
| 1887 | Creature                            | 8       | 0            | 0           |                     | 7 7               |
| 1888 | Northsea Pirates                    | 8       | 8            | 1           |                     | 1046              |
| 1889 | UNUSED                              | 8       | 0            | 1           |                     | 1048              |
| 1890 | Troll, Amani                        | 8       | 0            | 1           |                     | 1049              |
| 1891 | Valiance Expedition                 | 3       | 2            | 4           |                     | 1050              |
| 1892 | Valiance Expedition                 | 2       | 2            | 4           |                     | 1050              |
| 1893 | Valiance Expedition                 | 3       | 2            | 4           | 1045                | 1050              |
| 1894 | Vrykul                              | 8       | 0            | 1           |                     | 1045              |
| 1895 | Vrykul                              | 8       | 0            | 1           | 1050                | 1045              |
| 1896 | Darkmoon Faire                      | 1       | 1            | 8           |                     | 909               |
| 1897 | The Hand of Vengeance               | 4       | 4            | 2           | 1045 1050           | 1052 1067         |
| 1898 | Valiance Expedition                 | 2       | 2            | 4           | 1067                | 1050              |
| 1899 | Valiance Expedition                 | 2       | 2            | 4           | 1067                | 1050              |
| 1900 | The Hand of Vengeance               | 4       | 4            | 2           | 1053                | 1052 1067         |
| 1901 | Horde Expedition                    | 4       | 4            | 2           |                     | 1052              |
| 1902 | Actor Evil                          | 8       | 0            | 1           |                     |                   |
| 1904 | Actor Evil                          | 8       | 0            | 1           |                     |                   |
| 1905 | Tamed Plaguehound                   | 0       | 0            | 0           | 1054                | 1055              |
| 1906 | Spotted Gryphon                     | 8       | 0            | 1           | 1055                | 1054              |
| 1907 | Test Faction 1                      | 1       | 0            | 8           | 949                 | 948               |
| 1908 | Test Faction 1                      | 1       | 0            | 0           | 949                 | 948               |
| 1909 | Beast - Raptor                      | 0       | 0            | 9           | 14                  | 42                |
| 1910 | Vrykul (Ancient Spirit 1)           | 0       | 1            | 0           |                     | 1056              |
| 1911 | Vrykul (Ancient Siprit 2)           | 0       | 1            | 0           |                     | 1057              |
| 1912 | Vrykul (Ancient Siprit 3)           | 1       | 1            | 0           |                     | 1058              |
| 1913 | CTF - Flag - Alliance               | 0       | 7            | 0           |                     | 1059              |
| 1914 | Vrykul                              | 8       | 0            | 1           | 1067 1085           | 1045              |
| 1915 | Test                                | 0       | 0            | 0           |                     | 1060              |
| 1916 | Maiev                               | 0       | 1            | 0           | 1010                | 932 934 1012 1033 |
| 1917 | Creature                            | 0       | 0            | 1           |                     | 7                 |
| 1918 | Horde Expedition                    | 4       | 4            | 2           | 679                 | 1052              |
| 1919 | Vrykul Gladiator                    | 8       | 0            | 1           | 1063                | 1062              |
| 1920 | Valgarde Combatant                  | 3       | 0            | 4           | 1062                | 1063              |
| 1921 | The Taunka                          | 0       | 4            | 2           |                     | 1064              |
| 1922 | The Taunka                          | 0       | 4            | 2           |                     | 1064              |
| 1923 | The Taunka                          | 0       | 4            | 2           |                     | 1064              |
| 1924 | Monster, Zone Force Reaction 1      | 8       | 0            | 1           |                     | 1065              |
| 1925 | Monster                             | 8       | 0            | 9           | 14                  |                   |
| 1926 | Explorers' League                   | 2       | 0            | 4           |                     | 1068              |
| 1927 | Explorers' League                   | 2       | 0            | 4           |                     | 1068              |
| 1928 | The Hand of Vengeance               | 4       | 0            | 2           |                     | 1067 1052         |
| 1929 | The Hand of Vengeance               | 4       | 0            | 2           |                     | 1067 1052         |
| 1930 | Ram Racing Powerup DND              | 0       | 0            | 0           |                     | 1069              |
| 1931 | Ram Racing Trap DND                 | 0       | 0            | 0           |                     | 1070              |
| 1932 | Elemental                           | 0       | 0            | 15          | 14                  | 74                |
| 1933 | Friendly                            | 0       | 4            | 0           |                     | 31                |
| 1934 | Actor Good                          | 2       | 2            | 4           | 960                 | 959               |
| 1935 | Actor Good                          | 4       | 4            | 2           | 960                 | 959               |
| 1936 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1937 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1938 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1939 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1940 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1941 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1942 | Craig's Squirrels                   | 0       | 0            | 0           |                     | 960               |
| 1943 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1944 | Craig's Squirrels                   | 0       | 0            | 0           |                     |                   |
| 1945 | Craig's Squirrels                   | 15      | 15           | 15          |                     | 1071 551 189      |
| 1947 | Craig's Squirrels                   | 15      | 15           | 15          |                     | 1071 551 189      |
| 1948 | Blue                                | 1       | 2            | 1           | 469                 | 921               |
| 1949 | The Kalu'ak                         | 0       | 0            | 0           | 1046                | 1073              |
| 1950 | The Kalu'ak                         | 0       | 0            | 0           |                     | 1073              |
| 1951 | Darnassus                           | 2       | 2            | 12          | 22 29               | 69                |
| 1952 | Holiday - Water Barrel              | 0       | 1            | 0           |                     | 1074              |
| 1953 | Monster, Predator                   | 8       | 0            | 1           | 974                 | 973               |
| 1954 | Iron Dwarves                        | 8       | 0            | 1           |                     | 1076              |
| 1955 | Iron Dwarves                        | 8       | 0            | 1           |                     | 1076              |
| 1956 | Shattered Sun Offensive             | 1       | 0            | 0           |                     | 1077              |
| 1957 | Shattered Sun Offensive             | 1       | 0            | 0           |                     | 1077              |
| 1958 | Actor Evil                          | 8       | 0            | 1           | 959                 | 960               |
| 1959 | Actor Evil                          | 0       | 1            | 0           | 959                 | 960               |
| 1960 | Shattered Sun Offensive             | 1       | 0            | 0           |                     | 1077              |
| 1961 | Fighting Vanity Pet                 | 0       | 15           | 0           | 1078                |                   |
| 1962 | Undead, Scourge                     | 8       | 0            | 1           | 73                  | 20                |
| 1963 | Demon                               | 8       | 0            | 1           | 20                  | 73                |
| 1964 | Undead, Scourge                     | 8       | 0            | 1           | 73                  | 20                |
| 1965 | Monster Spar                        | 8       | 8            | 1           | 966                 | 965               |
| 1966 | Murloc                              | 8       | 0            | 0           | 60                  | 19                |
| 1967 | Shattered Sun Offensive             | 1       | 0            | 0           | 1077                |                   |
| 1968 | Murloc, Winterfin                   | 0       | 0            | 8           | 19                  | 1079              |
| 1969 | Murloc                              | 8       | 0            | 1           | 1079                | 19                |
| 1970 | Monster                             | 8       | 0            | 1           | 1079                | 14                |
| 1971 | Friendly, Force Reaction            | 0       | 1            | 0           |                     | 1080              |
| 1972 | Object, Force Reaction              | 0       | 0            | 0           |                     |                   |
| 1973 | Valiance Expedition                 | 3       | 2            | 4           |                     | 1050              |
| 1974 | Valiance Expedition                 | 2       | 2            | 4           | 1084 20             | 1050              |
| 1975 | Undead, Scourge                     | 8       | 0            | 7           | 1050                | 20                |
| 1976 | Valiance Expedition                 | 3       | 2            | 4           | 679                 | 1050              |
| 1977 | Valiance Expedition                 | 3       | 2            | 4           | 1050                |                   |
| 1978 | Warsong Offensive                   | 4       | 0            | 2           |                     | 1085              |
| 1979 | Warsong Offensive                   | 4       | 0            | 2           |                     | 1085              |
| 1980 | Warsong Offensive                   | 4       | 0            | 2           | 20                  | 1085              |
| 1981 | Warsong Offensive                   | 4       | 0            | 2           |                     | 1085              |
| 1982 | Undead, Scourge                     | 8       | 0            | 1           | 1085                | 20                |
| 1983 | Monster Spar                        | 8       | 8            | 1           | 966                 | 965               |
| 1984 | Monster Spar Buddy                  | 8       | 8            | 1           | 965                 | 966               |
| 1985 | Monster                             | 8       | 0            | 1           | 20                  | 14                |
| 1986 | Escortee                            | 1       | 1            | 8           | 1057 1058 1056      | 40                |
| 1987 | Cenarion Expedition                 | 1       | 0            | 0           | 1086                | 942 148           |
| 1988 | Undead, Scourge                     | 8       | 0            | 7           | 1050                | 20                |
| 1989 | Poacher                             | 8       | 0            | 1           | 148 942             | 1086              |
| 1990 | Ambient                             | 8       | 0            | 1           |                     | 148 942           |
| 1991 | Undead, Scourge                     | 0       | 0            | 7           | 14 148              | 928 20            |
| 1992 | Monster                             | 0       | 0            | 9           | 14                  |                   |
| 1993 | Monster Spar                        | 2       | 2            | 4           | 966                 | 965               |
| 1994 | Monster Spar Buddy                  | 2       | 2            | 4           | 965                 | 966               |
| 1995 | CTF - Flag - Alliance               | 0       | 5            | 2           |                     | 1059              |
| 1997 | CTF - Flag - Alliance               | 0       | 3            | 4           |                     | 1059              |
| 1998 | Holiday Monster                     | 8       | 0            | 1           |                     | 1087              |
| 1999 | Monster, Prey                       | 8       | 0            | 0           |                     | 974               |
| 2000 | Monster, Prey                       | 8       | 0            | 0           |                     | 974               |
| 2001 | Furbolg, Redfang                    | 8       | 8            | 1           | 1089                | 1088              |
| 2003 | Furbolg, Frostpaw                   | 8       | 8            | 1           | 1088                | 1089              |
| 2004 | Valiance Expedition                 | 3       | 2            | 4           | 20                  | 1050              |
| 2005 | Undead, Scourge                     | 8       | 0            | 7           | 1050                | 20                |
| 2006 | Kirin Tor                           | 0       | 0            | 0           |                     | 1090              |
| 2007 | Kirin Tor                           | 0       | 0            | 0           |                     | 1090              |
| 2008 | Kirin Tor                           | 0       | 0            | 0           |                     | 1090              |
| 2009 | Kirin Tor                           | 1       | 0            | 0           |                     | 1090              |
| 2010 | The Wyrmrest Accord                 | 0       | 0            | 0           |                     | 1091              |
| 2011 | The Wyrmrest Accord                 | 0       | 0            | 0           |                     | 1091              |
| 2012 | The Wyrmrest Accord                 | 0       | 0            | 0           |                     | 1091              |
| 2013 | The Wyrmrest Accord                 | 0       | 0            | 0           |                     | 1091              |
| 2014 | Azjol-Nerub                         | 0       | 0            | 0           |                     | 1092              |
| 2016 | Azjol-Nerub                         | 0       | 0            | 0           | 20                  | 1092              |
| 2017 | Azjol-Nerub                         | 0       | 0            | 0           |                     | 1092              |
| 2018 | Undead, Scourge                     | 8       | 0            | 7           | 1092                | 20                |
| 2019 | The Taunka                          | 0       | 4            | 2           | 20                  | 1064              |
| 2020 | Warsong Offensive                   | 4       | 4            | 2           |                     | 1085              |
| 2021 | REUSE                               | 3       | 2            | 4           |                     | 1082              |
| 2022 | Monster                             | 8       | 0            | 1           |                     | 14                |
| 2023 | Scourge Invaders                    | 9       | 0            | 6           | 14 148              | 928 20            |
| 2024 | The Hand of Vengeance               | 5       | 0            | 2           |                     | 1067              |
| 2025 | The Silver Covenant                 | 3       | 2            | 4           | 67                  | 1094              |
| 2026 | The Silver Covenant                 | 3       | 2            | 4           | 67                  | 1094              |
| 2027 | The Silver Covenant                 | 3       | 2            | 4           | 67                  | 1094              |
| 2028 | Ambient                             | 0       | 1            | 0           |                     |                   |
| 2029 | Monster, Predator                   | 8       | 0            | 1           | 974 28              | 973               |
| 2030 | Monster, Predator                   | 8       | 0            | 1           | 974 28              | 973               |
| 2031 | Horde Generic                       | 4       | 4            | 0           |                     | 148               |
| 2032 | Grizzly Hills Trapper               | 0       | 2            | 4           |                     | 1095              |
| 2033 | Monster                             | 8       | 0            | 1           | 56                  |                   |
| 2034 | Warsong Offensive                   | 4       | 0            | 2           | 1095                | 1085              |
| 2035 | Undead, Scourge                     | 8       | 0            | 7           | 31                  | 20                |
| 2036 | Friendly                            | 0       | 1            | 8           | 20                  | 31                |
| 2037 | Valiance Expedition                 | 2       | 2            | 4           | 148                 | 1050              |
| 2038 | Ambient                             | 8       | 0            | 0           | 1050                | 148               |
| 2039 | Monster                             | 8       | 0            | 1           | 1050                | 14                |
| 2040 | Valiance Expedition                 | 3       | 2            | 4           | 14                  | 1050              |
| 2041 | The Wyrmrest Accord                 | 0       | 0            | 0           | 20                  | 1091              |
| 2042 | Undead, Scourge                     | 8       | 0            | 7           | 1091                | 20                |
| 2043 | Undead, Scourge                     | 8       | 0            | 7           | 1050 1085           | 20                |
| 2044 | Valiance Expedition                 | 1       | 2            | 4           | 20                  | 1050              |
| 2045 | Warsong Offensive                   | 0       | 4            | 2           | 20                  | 1085              |
| 2046 | Escortee                            | 5       | 4            | 8           |                     |                   |
| 2047 | The Kalu'ak                         | 0       | 0            | 0           | 965                 |                   |
| 2048 | Scourge Invaders                    | 8       | 0            | 0           |                     | 928 20            |
| 2049 | Scourge Invaders                    | 0       | 0            | 0           |                     | 928 20            |
| 2050 | Knights of the Ebon Blade           | 1       | 0            | 0           |                     | 1098              |
| 2051 | Knights of the Ebon Blade           | 1       | 0            | 0           |                     | 1098              |
| 2052 | Wrathgate Scourge                   | 8       | 1            | 0           | 1050 1085 1101 1100 | 1099              |
| 2053 | Wrathgate Alliance                  | 1       | 6            | 0           | 20 1099             | 1100              |
| 2054 | Wrathgate Horde                     | 0       | 6            | 0           | 20 1099             | 1101              |
| 2055 | Monster Spar                        | 4       | 4            | 2           | 966                 | 965               |
| 2056 | Monster Spar Buddy                  | 4       | 4            | 2           | 965                 | 966               |
| 2057 | Monster, Zone Force Reaction 2      | 8       | 0            | 1           |                     | 1066              |
| 2058 | CTF - Flag - Horde                  | 0       | 7            | 0           |                     | 1102              |
| 2059 | CTF - Flag - Neutral                | 0       | 7            | 0           |                     | 1103              |
| 2060 | Frenzyheart Tribe                   | 0       | 0            | 0           |                     | 1104              |
| 2061 | Frenzyheart Tribe                   | 0       | 0            | 0           | 1105                | 1104              |
| 2062 | Frenzyheart Tribe                   | 0       | 0            | 0           | 1105                | 1104              |
| 2063 | The Oracles                         | 0       | 0            | 0           |                     | 1105              |
| 2064 | The Oracles                         | 0       | 0            | 0           | 1104                | 1105              |
| 2065 | The Oracles                         | 0       | 0            | 0           | 14                  | 1105              |
| 2066 | The Oracles                         | 0       | 0            | 0           | 1104                | 1105              |
| 2067 | The Wyrmrest Accord                 | 0       | 0            | 8           | 14                  | 1091              |
| 2068 | Undead, Scourge                     | 8       | 0            | 7           | 1107 1106 959       | 20                |
| 2069 | Troll, Drakkari                     | 8       | 0            | 7           | 1106 20             | 1107              |
| 2070 | Argent Crusade                      | 0       | 0            | 0           |                     | 1106              |
| 2071 | Argent Crusade                      | 0       | 0            | 0           |                     | 1106              |
| 2072 | Argent Crusade                      | 0       | 0            | 0           |                     | 1106              |
| 2073 | Argent Crusade                      | 0       | 0            | 0           | 1107 20             | 1106              |
| 2074 | Caverns of Time - Durnholde         | 8       | 0            | 0           |                     | 986 987           |
| 2075 | CoT Scourge                         | 8       | 0            | 1           | 1108                | 1110              |
| 2076 | CoT Arthas                          | 0       | 1            | 0           | 1110 1109           | 1108              |
| 2077 | CoT Arthas                          | 0       | 1            | 0           | 1110 1109           | 1108              |
| 2078 | CoT Stratholme Citizen              | 0       | 0            | 0           |                     | 1109              |
| 2079 | CoT Arthas                          | 0       | 1            | 0           | 1110 1109           | 1108              |
| 2080 | Undead, Scourge                     | 8       | 0            | 7           | 1111                | 20                |
| 2081 | Freya                               | 0       | 1            | 0           | 20                  | 1111              |
| 2082 | Undead, Scourge                     | 0       | 1            | 0           |                     | 20                |
| 2083 | Undead, Scourge                     | 0       | 1            | 0           |                     | 20                |
| 2084 | Undead, Scourge                     | 0       | 1            | 0           | 529 56              | 20                |
| 2085 | Undead, Scourge                     | 0       | 1            | 0           | 529 56              | 20                |
| 2086 | Argent Dawn                         | 8       | 0            | 1           |                     | 529               |
| 2087 | Argent Dawn                         | 8       | 0            | 1           |                     | 529               |
| 2088 | Actor Evil                          | 0       | 0            | 1           | 20 56               | 960               |
| 2089 | Scarlet Crusade                     | 8       | 0            | 1           | 20 529              | 56                |
| 2090 | Mount - Taxi - Alliance             | 2       | 0            | 0           |                     | 1112              |
| 2091 | Mount - Taxi - Horde                | 4       | 0            | 0           |                     | 1113              |
| 2092 | Mount - Taxi - Neutral              | 0       | 1            | 0           |                     | 1114              |
| 2093 | Undead, Scourge                     | 0       | 1            | 0           | 959                 | 20                |
| 2094 | Undead, Scourge                     | 0       | 1            | 0           |                     | 20                |
| 2095 | Scarlet Crusade                     | 8       | 0            | 1           | 20 529              | 56                |
| 2096 | Scarlet Crusade                     | 0       | 0            | 0           | 20 529              | 56                |
| 2097 | Undead, Scourge                     | 8       | 0            | 1           |                     | 20                |
| 2098 | Elemental, Air                      | 8       | 0            | 1           | 1115                | 1116              |
| 2099 | Elemental, Water                    | 8       | 0            | 1           | 1116                | 1115              |
| 2100 | Undead, Scourge                     | 0       | 1            | 8           | 529 56              | 20                |
| 2101 | Actor Evil                          | 0       | 1            | 0           | 959                 | 960               |
| 2102 | Actor Evil                          | 0       | 0            | 1           | 959                 | 960               |
| 2103 | Scarlet Crusade                     | 8       | 0            | 1           | 20 529              | 56                |
| 2104 | Monster Spar                        | 1       | 1            | 0           | 966                 | 965               |
| 2105 | Monster Spar Buddy                  | 1       | 1            | 0           | 965                 | 966               |
| 2106 | Ambient                             | 8       | 0            | 1           | 28                  | 148               |
| 2107 | The Sons of Hodir                   | 8       | 0            | 0           | 1120 1121           | 1119              |
| 2108 | Iron Giants                         | 8       | 0            | 1           | 1119                | 1120              |
| 2109 | Frost Vrykul                        | 8       | 0            | 1           |                     | 1121              |
| 2110 | Friendly                            | 0       | 1            | 8           |                     | 31                |
| 2111 | Monster                             | 8       | 0            | 1           | 31                  | 14                |
| 2112 | The Sons of Hodir                   | 8       | 0            | 0           | 1121                | 1119              |
| 2113 | Frost Vrykul                        | 8       | 0            | 1           | 1119                | 1121              |
| 2114 | Vrykul                              | 8       | 0            | 1           |                     | 1045 20           |
| 2115 | Actor Good                          | 0       | 1            | 8           | 1107 20             | 959               |
| 2116 | Vrykul                              | 8       | 0            | 1           |                     | 1045              |
| 2117 | Actor Good                          | 0       | 1            | 8           | 1107 20             | 959               |
| 2118 | Earthen                             | 0       | 1            | 0           | 1120                | 1122              |
| 2119 | Monster Referee                     | 8       | 0            | 1           |                     | 965 966 1123      |
| 2120 | Monster Referee                     | 8       | 0            | 1           |                     | 965 966 1123      |
| 2121 | The Sunreavers                      | 4       | 4            | 2           |                     | 1124              |
| 2122 | The Sunreavers                      | 4       | 4            | 2           |                     | 1124              |
| 2123 | The Sunreavers                      | 4       | 4            | 2           |                     | 1124              |
| 2124 | Monster                             | 8       | 0            | 1           | 1119                | 14                |
| 2125 | Frost Vrykul                        | 8       | 0            | 1           | 148                 | 1121              |
| 2126 | Frost Vrykul                        | 8       | 0            | 1           | 148                 | 1121              |
| 2127 | Ambient                             | 0       | 0            | 0           | 1121                | 148               |
| 2128 | Hyldsmeet                           | 0       | 1            | 0           | 1125                | 1125              |
| 2129 | The Sunreavers                      | 4       | 4            | 10          |                     | 1124              |
| 2130 | The Silver Covenant                 | 3       | 2            | 12          | 67                  | 1094              |
| 2131 | Argent Crusade                      | 0       | 0            | 0           | 1107 20             | 1106              |
| 2132 | Warsong Offensive                   | 5       | 4            | 2           |                     | 1085              |
| 2133 | Frost Vrykul                        | 8       | 0            | 1           | 1119                | 1121              |
| 2134 | Argent Crusade                      | 0       | 0            | 0           | 20                  | 1106              |
| 2135 | Friendly                            | 0       | 1            | 0           |                     | 31                |
| 2136 | Ambient                             | 0       | 0            | 0           |                     | 148               |
| 2137 | Friendly                            | 0       | 1            | 0           | 148                 | 31                |
| 2138 | Argent Crusade                      | 0       | 0            | 0           | 1107 20             | 1106              |
| 2139 | Scourge Invaders                    | 8       | 0            | 1           | 68 72               | 928 20            |
| 2140 | Friendly                            | 0       | 1            | 0           | 20                  | 31                |
| 2141 | Friendly                            | 0       | 1            | 8           |                     | 31                |
| 2142 | Alliance                            | 3       | 2            | 12          |                     |                   |
| 2143 | Valiance Expedition                 | 2       | 2            | 4           | 1085                | 1050              |
| 2144 | Knights of the Ebon Blade           | 1       | 0            | 0           | 20                  | 1098              |
| 2145 | Scourge Invaders                    | 8       | 0            | 7           | 14 148              | 928 20            |
| 2148 | The Kalu'ak                         | 0       | 0            | 0           |                     | 1073              |
| 2150 | Monster Spar Buddy                  | 8       | 8            | 1           | 965                 |                   |
| 2155 | Ironforge                           | 2       | 2            | 4           |                     | 47                |
| 2156 | Monster, Predator                   | 0       | 0            | 0           |                     | 973               |
| 2176 | Actor Good                          | 4       | 4            | 2           | 960                 | 959               |
| 2178 | Actor Good                          | 2       | 2            | 4           | 960                 | 959               |
| 2189 | Hates Everything                    | 8       | 0            | 15          |                     | 1145              |
| 2190 | Hates Everything                    | 8       | 0            | 15          |                     | 1145              |
| 2191 | Hates Everything                    | 8       | 0            | 15          |                     | 1145              |
| 2209 | Undead, Scourge                     | 8       | 0            | 7           | 1098 1106           | 20                |
| 2210 | Silvermoon City                     | 4       | 7            | 0           |                     |                   |
| 2212 | Undead, Scourge                     | 8       | 0            | 7           | 1098 1106           | 20                |
| 2214 | Knights of the Ebon Blade           | 1       | 6            | 0           | 20                  | 1098 529          |
| 2216 | The Ashen Verdict                   | 0       | 0            | 0           |                     | 1106 1156 1098    |
| 2217 | The Ashen Verdict                   | 0       | 0            | 0           |                     | 1106 1156 1098    |
| 2218 | The Ashen Verdict                   | 0       | 0            | 0           | 20                  | 1106 1156 1098    |
| 2219 | The Ashen Verdict                   | 0       | 0            | 0           | 20                  | 1106 1156 1098    |
| 2226 | Knights of the Ebon Blade           | 1       | 6            | 0           | 20                  | 1098 529          |
| 2230 | Argent Crusade                      | 0       | 0            | 0           | 1107 20             | 1106              |
| 2235 | CTF - Flag - Horde 2                | 0       | 5            | 2           |                     |                   |
| 2236 | CTF - Flag - Alliance 2             | 0       | 3            | 4           |                     |                   |
