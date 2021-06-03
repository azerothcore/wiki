# gossip\_menu\_option\_action

# **Table: gossip\_menu\_option\_action**

This table holds information about what a gossip menu option is doing, redirect to gossip or showing poi on mnap.

## Structure

| Field             | Type    | Attributes | Key | Null | Default | Extra | Comment |
|-------------------|---------|------------|-----|------|---------|-------|---------|
| [MenuId][1]       | INT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [OptionIndex][2]  | INT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [ActionMenuId][3] | INT | UNSIGNED   |     | NO   | 0       |       |         |
| [ActionPoiId][4]  | INT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #menuid
[2]: #optionindex
[3]: #actionmenuid
[4]: #actionpoiid

## Description of the fields

### MenuId

Gossip entry from Gossip\_menu.MenuId this option is associated with.

### OptionIndex

The OptionIndex associated with this gossip\_menu\_option. Must be unique for a given  [gossip\_menu\_option.OptionIndex](https://trinitycore.atlassian.net/wiki/spaces/tc/pages/2130188/gossip+menu+option#gossip_menu_option-OptionIndex) starting from 0 (zero).

### ActionMenuId

Gossip entry from Gossip\_menu.MenuId this option will link to. Opens Gossip with id specified here.

### ActionPoiId

Poi id from [points\_of\_interest.ID](https://trinitycore.atlassian.net/wiki/spaces/tc/pages/2130272/points+of+interest#points_of_interest-ID) this option is associated with.
If not 0 will show POI on Map.
