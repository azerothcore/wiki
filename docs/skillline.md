---
redirect_from: "/SkillLine"
---

# SkillLine

[`Back-to:DBC`](dbc-index.md)

**SkillLine.dbc**

This DBC contains all skills.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## Structure

| Column | Field                    | Type         | Notes              |
|--------|--------------------------|--------------|--------------------|
| 1      | ID                       | Integer      |                    |
| 2      | iRefID_SkillLineCategory | Integer      |                    |
| 3      | skillCostID              | Integer      |                    |
| 4      | sRefName                 | String + Loc |                    |
| 5      | description              | String + Loc |                    |
| 6      | iRefID_SpellIcon         | Integer      |                    |
| 7      | verb                     | String + Loc |                    |
| 8      | canLink                  | Integer      | prof. with recipes |

## **Content**

| ID  | CategoryId* | SkillCostId | Name                         | SpellIcon | AltVerb   | CanLink |
|-----|-------------|-------------|------------------------------|-----------|-----------|---------|
| 6   | 7           | 0           | Frost                        | 188       |           | 0       |
| 8   | 7           | 0           | Fire                         | 183       |           | 0       |
| 26  | 7           | 0           | Arms                         | 514       |           | 0       |
| 38  | 7           | 0           | Combat                       | 243       |           | 0       |
| 39  | 7           | 0           | Subtlety                     | 250       |           | 0       |
| 43  | 6           | 0           | Swords                       | 1         |           | 0       |
| 44  | 6           | 0           | Axes                         | 1         |           | 0       |
| 45  | 6           | 0           | Bows                         | 1         |           | 0       |
| 46  | 6           | 0           | Guns                         | 1         |           | 0       |
| 50  | 7           | 0           | Beast Mastery                | 255       |           | 0       |
| 51  | 7           | 0           | Survival                     | 257       |           | 0       |
| 54  | 6           | 0           | Maces                        | 1         |           | 0       |
| 55  | 6           | 0           | Two-Handed Swords            | 1         |           | 0       |
| 56  | 7           | 0           | Holy                         | 70        |           | 0       |
| 78  | 7           | 0           | Shadow Magic                 | 234       |           | 0       |
| 95  | 6           | 0           | Defense                      | 1         |           | 0       |
| 98  | 10          | 0           | Language: Common             | 1         |           | 0       |
| 101 | 9           | 0           | Dwarven Racial               | 1         |           | 0       |
| 109 | 10          | 0           | Language: Orcish             | 1         |           | 0       |
| 111 | 10          | 0           | Language: Dwarven            | 1         |           | 0       |
| 113 | 10          | 0           | Language: Darnassian         | 1         |           | 0       |
| 115 | 10          | 0           | Language: Taurahe            | 1         |           | 0       |
| 118 | 6           | 0           | Dual Wield                   | 1         |           | 0       |
| 124 | 9           | 0           | Tauren Racial                | 1         |           | 0       |
| 125 | 9           | 0           | Orc Racial                   | 1         |           | 0       |
| 126 | 9           | 0           | Night Elf Racial             | 1         |           | 0       |
| 129 | 9           | 0           | First Aid                    | 504       |           | 1       |
| 134 | 7           | 0           | Feral Combat                 | 107       |           | 0       |
| 136 | 6           | 0           | Staves                       | 1         |           | 0       |
| 137 | 10          | 0           | Language: Thalassian         | 1         |           | 0       |
| 138 | 10          | 0           | Language: Draconic           | 1         |           | 0       |
| 139 | 10          | 0           | Language: Demon Tongue       | 1         |           | 0       |
| 140 | 10          | 0           | Language: Titan              | 1         |           | 0       |
| 141 | 10          | 0           | Language: Old Tongue         | 1         |           | 0       |
| 142 | 9           | 0           | Survival                     | 1         |           | 0       |
| 148 | 9           | 0           | Horse Riding                 | 1         |           | 0       |
| 149 | 9           | 0           | Wolf Riding                  | 1         |           | 0       |
| 150 | 9           | 0           | Tiger Riding                 | 1         |           | 0       |
| 152 | 9           | 0           | Ram Riding                   | 1         |           | 0       |
| 155 | 9           | 0           | Swimming                     | 1         |           | 0       |
| 160 | 6           | 0           | Two-Handed Maces             | 1         |           | 0       |
| 162 | 6           | 0           | Unarmed                      | 1         |           | 0       |
| 163 | 7           | 0           | Marksmanship                 | 126       |           | 0       |
| 164 | 11          | 0           | Blacksmithing                | 335       | Modify    | 1       |
| 165 | 11          | 0           | Leatherworking               | 346       | Emboss    | 1       |
| 171 | 11          | 0           | Alchemy                      | 339       | Refill    | 1       |
| 172 | 6           | 0           | Two-Handed Axes              | 1         |           | 0       |
| 173 | 6           | 0           | Daggers                      | 1         |           | 0       |
| 176 | 6           | 0           | Thrown                       | 1         |           | 0       |
| 182 | 11          | 0           | Herbalism                    | 345       |           | 0       |
| 183 | 12          | 0           | GENERIC (DND)                | 1         |           | 0       |
| 184 | 7           | 0           | Retribution                  | 555       |           | 0       |
| 185 | 9           | 0           | Cooking                      | 1467      |           | 1       |
| 186 | 11          | 0           | Mining                       | 2418      |           | 0       |
| 188 | 7           | 0           | Pet - Imp                    | 1         |           | 0       |
| 189 | 7           | 0           | Pet - Felhunter              | 1         |           | 0       |
| 197 | 11          | 0           | Tailoring                    | 341       | Embroider | 1       |
| 202 | 11          | 0           | Engineering                  | 333       | Tinker    | 1       |
| 203 | 7           | 0           | Pet - Spider                 | 1         |           | 0       |
| 204 | 7           | 0           | Pet - Voidwalker             | 1         |           | 0       |
| 205 | 7           | 0           | Pet - Succubus               | 1         |           | 0       |
| 206 | 7           | 0           | Pet - Infernal               | 1         |           | 0       |
| 207 | 7           | 0           | Pet - Doomguard              | 1         |           | 0       |
| 208 | 7           | 0           | Pet - Wolf                   | 1         |           | 0       |
| 209 | 7           | 0           | Pet - Cat                    | 1         |           | 0       |
| 210 | 7           | 0           | Pet - Bear                   | 1         |           | 0       |
| 211 | 7           | 0           | Pet - Boar                   | 1         |           | 0       |
| 212 | 7           | 0           | Pet - Crocolisk              | 1         |           | 0       |
| 213 | 7           | 0           | Pet - Carrion Bird           | 1         |           | 0       |
| 214 | 7           | 0           | Pet - Crab                   | 1         |           | 0       |
| 215 | 7           | 0           | Pet - Gorilla                | 1         |           | 0       |
| 217 | 7           | 0           | Pet - Raptor                 | 1         |           | 0       |
| 218 | 7           | 0           | Pet - Tallstrider            | 1         |           | 0       |
| 220 | 9           | 0           | Racial - Undead              | 1         |           | 0       |
| 226 | 6           | 0           | Crossbows                    | 1         |           | 0       |
| 228 | 6           | 0           | Wands                        | 1         |           | 0       |
| 229 | 6           | 0           | Polearms                     | 1         |           | 0       |
| 236 | 7           | 0           | Pet - Scorpid                | 1         |           | 0       |
| 237 | 7           | 0           | Arcane                       | 125       |           | 0       |
| 251 | 7           | 0           | Pet - Turtle                 | 1         |           | 0       |
| 253 | 7           | 0           | Assassination                | 514       |           | 0       |
| 256 | 7           | 0           | Fury                         | 561       |           | 0       |
| 257 | 7           | 0           | Protection                   | 276       |           | 0       |
| 267 | 7           | 0           | Protection                   | 291       |           | 0       |
| 270 | 7           | 0           | Pet - Generic Hunter         | 1         |           | 0       |
| 293 | 8           | 0           | Plate Mail                   | 1         |           | 0       |
| 313 | 10          | 0           | Language: Gnomish            | 1         |           | 0       |
| 315 | 10          | 0           | Language: Troll              | 1         |           | 0       |
| 333 | 11          | 0           | Enchanting                   | 578       | Enchant   | 1       |
| 354 | 7           | 0           | Demonology                   | 90        |           | 0       |
| 355 | 7           | 0           | Affliction                   | 88        |           | 0       |
| 356 | 9           | 0           | Fishing                      | 580       |           | 0       |
| 373 | 7           | 0           | Enhancement                  | 19        |           | 0       |
| 374 | 7           | 0           | Restoration                  | 13        |           | 0       |
| 375 | 7           | 0           | Elemental Combat             | 62        |           | 0       |
| 393 | 11          | 0           | Skinning                     | 1         |           | 0       |
| 413 | 8           | 0           | Mail                         | 1         |           | 0       |
| 414 | 8           | 0           | Leather                      | 1         |           | 0       |
| 415 | 8           | 0           | Cloth                        | 1         |           | 0       |
| 433 | 8           | 0           | Shield                       | 1         |           | 0       |
| 473 | 6           | 0           | Fist Weapons                 | 1         |           | 0       |
| 533 | 9           | 0           | Raptor Riding                | 1         |           | 0       |
| 553 | 9           | 0           | Mechanostrider Piloting      | 1         |           | 0       |
| 554 | 9           | 0           | Undead Horsemanship          | 1         |           | 0       |
| 573 | 7           | 0           | Restoration                  | 962       |           | 0       |
| 574 | 7           | 0           | Balance                      | 225       |           | 0       |
| 593 | 7           | 0           | Destruction                  | 547       |           | 0       |
| 594 | 7           | 0           | Holy                         | 70        |           | 0       |
| 613 | 7           | 0           | Discipline                   | 685       |           | 0       |
| 633 | 7           | 0           | Lockpicking                  | 1         |           | 0       |
| 653 | 7           | 0           | Pet - Bat                    | 1         |           | 0       |
| 654 | 7           | 0           | Pet - Hyena                  | 1         |           | 0       |
| 655 | 7           | 0           | Pet - Bird of Prey           | 1         |           | 0       |
| 656 | 7           | 0           | Pet - Wind Serpent           | 1         |           | 0       |
| 673 | 10          | 0           | Language: Gutterspeak        | 1         |           | 0       |
| 713 | 9           | 0           | Kodo Riding                  | 317       |           | 0       |
| 733 | 9           | 0           | Racial - Troll               | 0         |           | 0       |
| 753 | 9           | 0           | Racial - Gnome               | 0         |           | 0       |
| 754 | 9           | 0           | Racial - Human               | 0         |           | 0       |
| 755 | 11          | 0           | Jewelcrafting                | 1768      | Modify    | 1       |
| 756 | 9           | 0           | Blood Elf Racial             | 0         |           | 0       |
| 758 | -1          | 0           | Pet - Event - Remote Control | 0         |           | 0       |
| 759 | 10          | 0           | Language: Draenei            | 0         |           | 0       |
| 760 | 9           | 0           | Draenei Racial               | 0         |           | 0       |
| 761 | 7           | 0           | Pet - Felguard               | 0         |           | 0       |
| 762 | 9           | 0           | Riding                       | 255       |           | 0       |
| 763 | 7           | 0           | Pet - Dragonhawk             | 1530      |           | 0       |
| 764 | 7           | 0           | Pet - Nether Ray             | 1577      |           | 0       |
| 765 | 7           | 0           | Pet - Sporebat               | 2033      |           | 0       |
| 766 | 7           | 0           | Pet - Warp Stalker           | 1952      |           | 0       |
| 767 | 7           | 0           | Pet - Ravager                | 1585      |           | 0       |
| 768 | 7           | 0           | Pet - Serpent                | 2167      |           | 0       |
| 769 | 7           | 22          | Internal                     | 1775      |           | 0       |
| 770 | 7           | 0           | Blood                        | 2636      |           | 0       |
| 771 | 7           | 0           | Frost                        | 2632      |           | 0       |
| 772 | 7           | 0           | Unholy                       | 2633      |           | 0       |
| 773 | 11          | 0           | Inscription                  | 3267      | Inscribe  | 1       |
| 775 | 7           | 0           | Pet - Moth                   | 0         |           | 0       |
| 776 | 7           | 0           | Runeforging                  | 2727      | Engrave   | 0       |
| 777 | 7           | 0           | Mounts                       | 2224      |           | 0       |
| 778 | 7           | 0           | Companions                   | 0         |           | 0       |
| 780 | 7           | 0           | Pet - Exotic Chimaera        | 0         |           | 0       |
| 781 | 7           | 0           | Pet - Exotic Devlisaur       | 0         |           | 0       |
| 782 | 7           | 0           | Pet - Ghoul                  | 221       |           | 0       |
| 783 | 7           | 0           | Pet - Exotic Silithid        | 0         |           | 0       |
| 784 | 7           | 0           | Pet - Exotic Worm            | 0         |           | 0       |
| 785 | 7           | 0           | Pet- Wasp                    | 0         |           | 0       |
| 786 | 7           | 0           | Pet - Exotic Rhino           | 0         |           | 0       |
| 787 | 7           | 0           | Pet - Exotic Core Hound      | 0         |           | 0       |
| 788 | 5           | 0           | Pet - Exotic Spirit Beast    | 0         |           | 0       |

## CategoryId

This field is from SkillLineCategory.dbc

This in the content of this small dbc

| Category Id | Name                |
|-------------|---------------------|
| 5           | Attributes          |
| 6           | Weapon Skills       |
| 7           | Class Skills        |
| 8           | Armor Proficiencies |
| 9           | Secondary Skills    |
| 10          | Languages           |
| 11          | Professions         |
| 12          | Not Displayed       |
