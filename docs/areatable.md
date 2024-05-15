---
redirect_from: "/AreaTable"
---

# AreaTable

[`Back-to:DBC`](dbc-index.md)

**AreaTable.dbc**

This DBC contains the zone and subzone lists. For the purposes of this wiki article, the zone IDs, names, mapID and AreaID will be included.

**Version is : 3.3.5a**

[How to Import DBC Data onto my Database](how-to-import-dbc-data-in-db.md)  

## Structure

| Column | Name             | Type   | Notes                                                         |
| ------ | ---------------- | ------ | ------------------------------------------------------------- |
| 1      | ID               | Int    | Zone Area                                                     |
| 2      | MapID            | Int    | Map or Continent                                              |
| 3      | AreaID           | Int    | SubArea of Map                                                |
| 4      | Explore Flag     | Int    |                                                               |
| 5      | Flags            | Int    |                                                               |
| 8      | SoundAmbienceID  | Int    | Reference to what Ambiance to use during day and night        |
| 9      | ZoneMusicID      | Int    | Reference to what zone music to play                          |
| 10     | ZoneIntroMusicID | Int    | Reference to what zone intro music to play when entering area |
| 11     | Area Level       | Int    |                                                               |
| 12-28  | Area Name        | String |                                                               |
| 29     | FactionGroupID   | Int    | Faction that owns area                                        |

**Description of the fields**

## Flags

| Value      | Name                     | Notes                                                                                                                                                                                          |
| ---------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00000001 | AREA_FLAG_SNOW           | snow (only Dun Morogh, Naxxramas, Razorfen Downs and Winterspring)                                                                                                                             |
| 0x00000002 | AREA_FLAG_UNK1           | may be necropolis?                                                                                                                                                                             |
| 0x00000004 | AREA_FLAG_UNK2           | Only used for areas on map 571 (development before)                                                                                                                                            |
| 0x00000008 | AREA_FLAG_SLAVE_CAPITAL  | city and city subzones                                                                                                                                                                         |
| 0x00000010 | AREA_FLAG_UNK3           | can't find common meaning                                                                                                                                                                      |
| 0x00000020 | AREA_FLAG_SLAVE_CAPITAL2 | slave capital city flag?                                                                                                                                                                       |
| 0x00000040 | AREA_FLAG_ALLOW_DUELS    | allow to duel here                                                                                                                                                                             |
| 0x00000080 | AREA_FLAG_ARENA          | arena, both instanced and world arenas                                                                                                                                                         |
| 0x00000100 | AREA_FLAG_CAPITAL        | main capital city flag                                                                                                                                                                         |
| 0x00000200 | AREA_FLAG_CITY           | only for one zone named "City" (where it located?)                                                                                                                                             |
| 0x00000400 | AREA_FLAG_OUTLAND        | expansion zones? (only Eye of the Storm not have this flag, but have 0x00004000 flag)                                                                                                          |
| 0x00000800 | AREA_FLAG_SANCTUARY      | sanctuary area (PvP disabled)                                                                                                                                                                  |
| 0x00001000 | AREA_FLAG_NEED_FLY       | only Netherwing Ledge, Socrethar's Seat, Tempest Keep, The Arcatraz, The Botanica, The Mechanar, Sorrow Wing Point, Dragonspine Ridge, Netherwing Mines, Dragonmaw Base Camp, Dragonmaw Skyway |
| 0x00002000 | AREA_FLAG_UNUSED1        | not used now (no area/zones with this flag set in 3.0.3)                                                                                                                                       |
| 0x00004000 | AREA_FLAG_OUTLAND2       | expansion zones? (only Circle of Blood Arena not have this flag, but have 0x00000400 flag)                                                                                                     |
| 0x00008000 | AREA_FLAG_OUTDOOR_PVP    | pvp objective area? (Death's Door also has this flag although it's no pvp object area)                                                                                                         |
| 0x00010000 | AREA_FLAG_ARENA_INSTANCE | used by instanced arenas only                                                                                                                                                                  |
| 0x00020000 | AREA_FLAG_UNUSED2        | not used now (no area/zones with this flag set in 3.0.3)                                                                                                                                       |
| 0x00040000 | AREA_FLAG_CONTESTED_AREA | On PvP servers these areas are considered contested, even though the zone it is contained in is a Horde/Alliance territory.                                                                    |
| 0x00080000 | AREA_FLAG_UNK6           | Valgarde and Acherus: The Ebon Hold                                                                                                                                                            |
| 0x00100000 | AREA_FLAG_LOWLEVEL       | used for some starting areas with area_level <=15                                                                                                                                              |
| 0x00200000 | AREA_FLAG_TOWN           | small towns with Inn                                                                                                                                                                           |
| 0x00400000 | AREA_FLAG_UNK7           | Warsong Hold, Acherus: The Ebon Hold, New Agamand Inn, Vengeance Landing Inn                                                                                                                   |
| 0x00800000 | AREA_FLAG_UNK8           | Westguard Inn, Acherus: The Ebon Hold, Valgarde                                                                                                                                                |
| 0x01000000 | AREA_FLAG_WINTERGRASP    | Wintergrasp and it's subzones                                                                                                                                                                  |
| 0x02000000 | AREA_FLAG_INSIDE         | used for determinating spell related inside/outside questions in Map::IsOutdoors                                                                                                               |
| 0x04000000 | AREA_FLAG_OUTSIDE        | used for determinating spell related inside/outside questions in Map::IsOutdoors                                                                                                               |
| 0x08000000 | AREA_FLAG_WINTERGRASP_2  | Wintergrasp and it's subzones                                                                                                                                                                  |
| 0x20000000 | AREA_FLAG_CANNOT_FLY     | not allowed to fly, only used in Dalaran areas (zone 4395)                                                                                                                                     |

**It's complete! 2307 records**

## Content

| Field Nb | Name                                                 | MapID | AreaID |
| -------- | ---------------------------------------------------- | ----- | ------ |
| 1        | Dun Morogh                                           | 0     | 0      |
| 2        | Longshore                                            | 0     | 40     |
| 3        | Badlands                                             | 0     | 0      |
| 4        | Blasted Lands                                        | 0     | 0      |
| 7        | Blackwater Cove                                      | 0     | 33     |
| 8        | Swamp of Sorrows                                     | 0     | 0      |
| 9        | Northshire Valley                                    | 0     | 12     |
| 10       | Duskwood                                             | 0     | 0      |
| 11       | Wetlands                                             | 0     | 0      |
| 12       | Elwynn Forest                                        | 0     | 0      |
| 13       | The World Tree                                       | 0     | 10     |
| 14       | Durotar                                              | 1     | 0      |
| 15       | Dustwallow Marsh                                     | 1     | 0      |
| 16       | Azshara                                              | 1     | 0      |
| 17       | The Barrens                                          | 1     | 0      |
| 18       | Crystal Lake                                         | 0     | 12     |
| 19       | Zul'Gurub                                            | 0     | 33     |
| 20       | Moonbrook                                            | 0     | 40     |
| 21       | Kul Tiras                                            | 0     | 0      |
| 22       | Programmer Isle                                      | 451   | 0      |
| 23       | Northshire River                                     | 0     | 12     |
| 24       | Northshire Abbey                                     | 0     | 12     |
| 25       | Blackrock Mountain                                   | 0     | 0      |
| 26       | Lighthouse                                           | 0     | 40     |
| 28       | Western Plaguelands                                  | 0     | 0      |
| 30       | Nine                                                 | 0     | 0      |
| 32       | The Cemetary                                         | 0     | 10     |
| 33       | Stranglethorn Vale                                   | 0     | 0      |
| 34       | Echo Ridge Mine                                      | 0     | 12     |
| 35       | Booty Bay                                            | 0     | 33     |
| 36       | Alterac Mountains                                    | 0     | 0      |
| 37       | Lake Nazferiti                                       | 0     | 33     |
| 38       | Loch Modan                                           | 0     | 0      |
| 40       | Westfall                                             | 0     | 0      |
| 41       | Deadwind Pass                                        | 0     | 0      |
| 42       | Darkshire                                            | 0     | 10     |
| 43       | Wild Shore                                           | 0     | 33     |
| 44       | Redridge Mountains                                   | 0     | 0      |
| 45       | Arathi Highlands                                     | 0     | 0      |
| 46       | Burning Steppes                                      | 0     | 0      |
| 47       | The Hinterlands                                      | 0     | 0      |
| 49       | Dead Man's Hole                                      | 451   | 22     |
| 51       | Searing Gorge                                        | 0     | 0      |
| 53       | Thieves Camp                                         | 0     | 12     |
| 54       | Jasperlode Mine                                      | 0     | 12     |
| 55       | Valley of Heroes UNUSED                              | 0     | 12     |
| 56       | Heroes' Vigil                                        | 0     | 12     |
| 57       | Fargodeep Mine                                       | 0     | 12     |
| 59       | Northshire Vineyards                                 | 0     | 12     |
| 60       | Forest's Edge                                        | 0     | 12     |
| 61       | Thunder Falls                                        | 0     | 12     |
| 62       | Brackwell Pumpkin Patch                              | 0     | 12     |
| 63       | The Stonefield Farm                                  | 0     | 12     |
| 64       | The Maclure Vineyards                                | 0     | 12     |
| 65       | Dragonblight                                         | 571   | 0      |
| 66       | Zul'Drak                                             | 571   | 0      |
| 67       | The Storm Peaks                                      | 571   | 0      |
| 68       | Lake Everstill                                       | 0     | 44     |
| 69       | Lakeshire                                            | 0     | 44     |
| 70       | Stonewatch                                           | 0     | 44     |
| 71       | Stonewatch Falls                                     | 0     | 44     |
| 72       | The Dark Portal                                      | 0     | 4      |
| 73       | The Tainted Scar                                     | 0     | 4      |
| 74       | Pool of Tears                                        | 0     | 8      |
| 75       | Stonard                                              | 0     | 8      |
| 76       | Fallow Sanctuary                                     | 0     | 8      |
| 77       | Anvilmar                                             | 0     | 1      |
| 80       | Stormwind Mountains                                  | 0     | 12     |
| 81       | Jeff NE Quadrant Changed                             | 451   | 22     |
| 82       | Jeff NW Quadrant                                     | 451   | 22     |
| 83       | Jeff SE Quadrant                                     | 451   | 22     |
| 84       | Jeff SW Quadrant                                     | 451   | 22     |
| 85       | Tirisfal Glades                                      | 0     | 0      |
| 86       | Stone Cairn Lake                                     | 0     | 12     |
| 87       | Goldshire                                            | 0     | 12     |
| 88       | Eastvale Logging Camp                                | 0     | 12     |
| 89       | Mirror Lake Orchard                                  | 0     | 12     |
| 91       | Tower of Azora                                       | 0     | 12     |
| 92       | Mirror Lake                                          | 0     | 12     |
| 93       | Vul'Gol Ogre Mound                                   | 0     | 10     |
| 94       | Raven Hill                                           | 0     | 10     |
| 95       | Redridge Canyons                                     | 0     | 44     |
| 96       | Tower of Ilgalar                                     | 0     | 44     |
| 97       | Alther's Mill                                        | 0     | 44     |
| 98       | Rethban Caverns                                      | 0     | 44     |
| 99       | Rebel Camp                                           | 0     | 33     |
| 100      | Nesingwary's Expedition                              | 0     | 33     |
| 101      | Kurzen's Compound                                    | 0     | 33     |
| 102      | Ruins of Zul'Kunda                                   | 0     | 33     |
| 103      | Ruins of Zul'Mamwe                                   | 0     | 33     |
| 104      | The Vile Reef                                        | 0     | 33     |
| 105      | Mosh'Ogg Ogre Mound                                  | 0     | 33     |
| 106      | The Stockpile                                        | 0     | 33     |
| 107      | Saldean's Farm                                       | 0     | 40     |
| 108      | Sentinel Hill                                        | 0     | 40     |
| 109      | Furlbrow's Pumpkin Farm                              | 0     | 40     |
| 111      | Jangolode Mine                                       | 0     | 40     |
| 113      | Gold Coast Quarry                                    | 0     | 40     |
| 115      | Westfall Lighthouse                                  | 0     | 40     |
| 116      | Misty Valley                                         | 0     | 8      |
| 117      | Grom'gol Base Camp                                   | 0     | 33     |
| 118      | Whelgar's Excavation Site                            | 0     | 11     |
| 120      | Westbrook Garrison                                   | 0     | 12     |
| 121      | Tranquil Gardens Cemetery                            | 0     | 10     |
| 122      | Zuuldaia Ruins                                       | 0     | 33     |
| 123      | Bal'lal Ruins                                        | 0     | 33     |
| 125      | Kal'ai Ruins                                         | 0     | 33     |
| 126      | Tkashi Ruins                                         | 0     | 33     |
| 127      | Balia'mah Ruins                                      | 0     | 33     |
| 128      | Ziata'jai Ruins                                      | 0     | 33     |
| 129      | Mizjah Ruins                                         | 0     | 33     |
| 130      | Silverpine Forest                                    | 0     | 0      |
| 131      | Kharanos                                             | 0     | 1      |
| 132      | Coldridge Valley                                     | 0     | 1      |
| 133      | Gnomeregan                                           | 0     | 1      |
| 134      | Gol'Bolar Quarry                                     | 0     | 1      |
| 135      | Frostmane Hold                                       | 0     | 1      |
| 136      | The Grizzled Den                                     | 0     | 1      |
| 137      | Brewnall Village                                     | 0     | 1      |
| 138      | Misty Pine Refuge                                    | 0     | 1      |
| 139      | Eastern Plaguelands                                  | 0     | 0      |
| 141      | Teldrassil                                           | 1     | 0      |
| 142      | Ironband's Excavation Site                           | 0     | 38     |
| 143      | Mo'grosh Stronghold                                  | 0     | 38     |
| 144      | Thelsamar                                            | 0     | 38     |
| 145      | Algaz Gate                                           | 0     | 38     |
| 146      | Stonewrought Dam                                     | 0     | 38     |
| 147      | The Farstrider Lodge                                 | 0     | 38     |
| 148      | Darkshore                                            | 1     | 0      |
| 149      | Silver Stream Mine                                   | 0     | 38     |
| 150      | Menethil Harbor                                      | 0     | 11     |
| 151      | Designer Island                                      | 451   | 0      |
| 152      | The Bulwark                                          | 0     | 85     |
| 153      | Ruins of Lordaeron                                   | 0     | 85     |
| 154      | Deathknell                                           | 0     | 85     |
| 155      | Night Web's Hollow                                   | 0     | 85     |
| 156      | Solliden Farmstead                                   | 0     | 85     |
| 157      | Agamand Mills                                        | 0     | 85     |
| 158      | Agamand Family Crypt                                 | 0     | 85     |
| 159      | Brill                                                | 0     | 85     |
| 160      | Whispering Gardens                                   | 0     | 85     |
| 161      | Terrace of Repose                                    | 0     | 85     |
| 162      | Brightwater Lake                                     | 0     | 85     |
| 163      | Gunther's Retreat                                    | 0     | 85     |
| 164      | Garren's Haunt                                       | 0     | 85     |
| 165      | Balnir Farmstead                                     | 0     | 85     |
| 166      | Cold Hearth Manor                                    | 0     | 85     |
| 167      | Crusader Outpost                                     | 0     | 85     |
| 168      | The North Coast                                      | 0     | 85     |
| 169      | Whispering Shore                                     | 0     | 85     |
| 170      | Lordamere Lake                                       | 0     | 0      |
| 172      | Fenris Isle                                          | 0     | 130    |
| 173      | Faol's Rest                                          | 0     | 85     |
| 186      | Dolanaar                                             | 1     | 141    |
| 187      | Darnassus UNUSED                                     | 1     | 141    |
| 188      | Shadowglen                                           | 1     | 141    |
| 189      | Steelgrill's Depot                                   | 0     | 1      |
| 190      | Hearthglen                                           | 0     | 28     |
| 192      | Northridge Lumber Camp                               | 0     | 28     |
| 193      | Ruins of Andorhal                                    | 0     | 28     |
| 195      | School of Necromancy                                 | 0     | 28     |
| 196      | Uther's Tomb                                         | 0     | 28     |
| 197      | Sorrow Hill                                          | 0     | 28     |
| 198      | The Weeping Cave                                     | 0     | 28     |
| 199      | Felstone Field                                       | 0     | 28     |
| 200      | Dalson's Tears                                       | 0     | 28     |
| 201      | Gahrron's Withering                                  | 0     | 28     |
| 202      | The Writhing Haunt                                   | 0     | 28     |
| 203      | Mardenholde Keep                                     | 0     | 28     |
| 204      | Pyrewood Village                                     | 0     | 130    |
| 205      | Dun Modr                                             | 0     | 11     |
| 206      | Utgarde Keep                                         | 574   | 0      |
| 207      | The Great Sea                                        | 36    | 0      |
| 208      | Unused Ironcladcove                                  | 36    | 0      |
| 209      | Shadowfang Keep                                      | 33    | 0      |
| 210      | Icecrown                                             | 571   | 0      |
| 211      | Iceflow Lake                                         | 0     | 1      |
| 212      | Helm's Bed Lake                                      | 0     | 1      |
| 213      | Deep Elem Mine                                       | 0     | 130    |
| 214      | The Great Sea                                        | 0     | 0      |
| 215      | Mulgore                                              | 1     | 0      |
| 219      | Alexston Farmstead                                   | 0     | 40     |
| 220      | Red Cloud Mesa                                       | 1     | 215    |
| 221      | Camp Narache                                         | 1     | 215    |
| 222      | Bloodhoof Village                                    | 1     | 215    |
| 223      | Stonebull Lake                                       | 1     | 215    |
| 224      | Ravaged Caravan                                      | 1     | 215    |
| 225      | Red Rocks                                            | 1     | 215    |
| 226      | The Skittering Dark                                  | 0     | 130    |
| 227      | Valgan's Field                                       | 0     | 130    |
| 228      | The Sepulcher                                        | 0     | 130    |
| 229      | Olsen's Farthing                                     | 0     | 130    |
| 230      | The Greymane Wall                                    | 0     | 130    |
| 231      | Beren's Peril                                        | 0     | 130    |
| 232      | The Dawning Isles                                    | 0     | 130    |
| 233      | Ambermill                                            | 0     | 130    |
| 235      | Fenris Keep                                          | 0     | 130    |
| 236      | Shadowfang Keep                                      | 0     | 130    |
| 237      | The Decrepit Ferry                                   | 0     | 130    |
| 238      | Malden's Orchard                                     | 0     | 130    |
| 239      | The Ivar Patch                                       | 0     | 130    |
| 240      | The Dead Field                                       | 0     | 130    |
| 241      | The Rotting Orchard                                  | 0     | 10     |
| 242      | Brightwood Grove                                     | 0     | 10     |
| 243      | Forlorn Rowe                                         | 0     | 10     |
| 244      | The Whipple Estate                                   | 0     | 10     |
| 245      | The Yorgen Farmstead                                 | 0     | 10     |
| 246      | The Cauldron                                         | 0     | 51     |
| 247      | Grimesilt Dig Site                                   | 0     | 51     |
| 249      | Dreadmaul Rock                                       | 0     | 46     |
| 250      | Ruins of Thaurissan                                  | 0     | 46     |
| 251      | Flame Crest                                          | 0     | 46     |
| 252      | Blackrock Stronghold                                 | 0     | 46     |
| 253      | The Pillar of Ash                                    | 0     | 46     |
| 254      | Blackrock Mountain                                   | 0     | 46     |
| 255      | Altar of Storms                                      | 0     | 46     |
| 256      | Aldrassil                                            | 1     | 141    |
| 257      | Shadowthread Cave                                    | 1     | 141    |
| 258      | Fel Rock                                             | 1     | 141    |
| 259      | Lake Al'Ameth                                        | 1     | 141    |
| 260      | Starbreeze Village                                   | 1     | 141    |
| 261      | Gnarlpine Hold                                       | 1     | 141    |
| 262      | Ban'ethil Barrow Den                                 | 1     | 141    |
| 263      | The Cleft                                            | 1     | 141    |
| 264      | The Oracle Glade                                     | 1     | 141    |
| 265      | Wellspring River                                     | 1     | 141    |
| 266      | Wellspring Lake                                      | 1     | 141    |
| 267      | Hillsbrad Foothills                                  | 0     | 0      |
| 268      | Azshara Crater                                       | 37    | 0      |
| 269      | Dun Algaz                                            | 0     | 0      |
| 271      | Southshore                                           | 0     | 267    |
| 272      | Tarren Mill                                          | 0     | 267    |
| 275      | Durnholde Keep                                       | 0     | 267    |
| 276      | UNUSED Stonewrought Pass                             | 0     | 0      |
| 277      | The Foothill Caverns                                 | 0     | 36     |
| 278      | Lordamere Internment Camp                            | 0     | 36     |
| 279      | Dalaran Crater                                       | 0     | 36     |
| 280      | Strahnbrad                                           | 0     | 36     |
| 281      | Ruins of Alterac                                     | 0     | 36     |
| 282      | Crushridge Hold                                      | 0     | 36     |
| 283      | Slaughter Hollow                                     | 0     | 36     |
| 284      | The Uplands                                          | 0     | 36     |
| 285      | Southpoint Tower                                     | 0     | 267    |
| 286      | Hillsbrad Fields                                     | 0     | 267    |
| 287      | Hillsbrad                                            | 0     | 267    |
| 288      | Azurelode Mine                                       | 0     | 267    |
| 289      | Nethander Stead                                      | 0     | 267    |
| 290      | Dun Garok                                            | 0     | 267    |
| 293      | Thoradin's Wall                                      | 0     | 0      |
| 294      | Eastern Strand                                       | 0     | 267    |
| 295      | Western Strand                                       | 0     | 267    |
| 296      | South Seas UNUSED                                    | 0     | 0      |
| 297      | Jaguero Isle                                         | 0     | 33     |
| 298      | Baradin Bay                                          | 0     | 11     |
| 299      | Menethil Bay                                         | 0     | 11     |
| 300      | Misty Reed Strand                                    | 0     | 8      |
| 301      | The Savage Coast                                     | 0     | 33     |
| 302      | The Crystal Shore                                    | 0     | 33     |
| 303      | Shell Beach                                          | 0     | 33     |
| 305      | North Tide's Run                                     | 0     | 130    |
| 306      | South Tide's Run                                     | 0     | 130    |
| 307      | The Overlook Cliffs                                  | 0     | 47     |
| 308      | The Forbidding Sea                                   | 0     | 0      |
| 309      | Ironbeard's Tomb                                     | 0     | 11     |
| 310      | Crystalvein Mine                                     | 0     | 33     |
| 311      | Ruins of Aboraz                                      | 0     | 33     |
| 312      | Janeiro's Point                                      | 0     | 33     |
| 313      | Northfold Manor                                      | 0     | 45     |
| 314      | Go'Shek Farm                                         | 0     | 45     |
| 315      | Dabyrie's Farmstead                                  | 0     | 45     |
| 316      | Boulderfist Hall                                     | 0     | 45     |
| 317      | Witherbark Village                                   | 0     | 45     |
| 318      | Drywhisker Gorge                                     | 0     | 45     |
| 320      | Refuge Pointe                                        | 0     | 45     |
| 321      | Hammerfall                                           | 0     | 45     |
| 322      | Blackwater Shipwrecks                                | 0     | 45     |
| 323      | O'Breen's Camp                                       | 0     | 45     |
| 324      | Stromgarde Keep                                      | 0     | 45     |
| 325      | The Tower of Arathor                                 | 0     | 45     |
| 326      | The Sanctum                                          | 0     | 45     |
| 327      | Faldir's Cove                                        | 0     | 45     |
| 328      | The Drowned Reef                                     | 0     | 45     |
| 330      | Thandol Span                                         | 0     | 0      |
| 331      | Ashenvale                                            | 1     | 0      |
| 332      | The Great Sea                                        | 1     | 0      |
| 333      | Circle of East Binding                               | 0     | 45     |
| 334      | Circle of West Binding                               | 0     | 45     |
| 335      | Circle of Inner Binding                              | 0     | 45     |
| 336      | Circle of Outer Binding                              | 0     | 45     |
| 337      | Apocryphan's Rest                                    | 0     | 3      |
| 338      | Angor Fortress                                       | 0     | 3      |
| 339      | Lethlor Ravine                                       | 0     | 3      |
| 340      | Kargath                                              | 0     | 3      |
| 341      | Camp Kosh                                            | 0     | 3      |
| 342      | Camp Boff                                            | 0     | 3      |
| 343      | Camp Wurg                                            | 0     | 3      |
| 344      | Camp Cagg                                            | 0     | 3      |
| 345      | Agmond's End                                         | 0     | 3      |
| 346      | Hammertoe's Digsite                                  | 0     | 3      |
| 347      | Dustbelch Grotto                                     | 0     | 3      |
| 348      | Aerie Peak                                           | 0     | 47     |
| 349      | Wildhammer Keep                                      | 0     | 47     |
| 350      | Quel'Danil Lodge                                     | 0     | 47     |
| 351      | Skulk Rock                                           | 0     | 47     |
| 352      | Zun'watha                                            | 0     | 47     |
| 353      | Shadra'Alor                                          | 0     | 47     |
| 354      | Jintha'Alor                                          | 0     | 47     |
| 355      | The Altar of Zul                                     | 0     | 47     |
| 356      | Seradane                                             | 0     | 47     |
| 357      | Feralas                                              | 1     | 0      |
| 358      | Brambleblade Ravine                                  | 1     | 215    |
| 359      | Bael Modan                                           | 1     | 17     |
| 360      | The Venture Co. Mine                                 | 1     | 215    |
| 361      | Felwood                                              | 1     | 0      |
| 362      | Razor Hill                                           | 1     | 14     |
| 363      | Valley of Trials                                     | 1     | 14     |
| 364      | The Den                                              | 1     | 14     |
| 365      | Burning Blade Coven                                  | 1     | 14     |
| 366      | Kolkar Crag                                          | 1     | 14     |
| 367      | Sen'jin Village                                      | 1     | 14     |
| 368      | Echo Isles                                           | 1     | 14     |
| 369      | Thunder Ridge                                        | 1     | 14     |
| 370      | Drygulch Ravine                                      | 1     | 14     |
| 371      | Dustwind Cave                                        | 1     | 14     |
| 372      | Tiragarde Keep                                       | 1     | 14     |
| 373      | Scuttle Coast                                        | 1     | 14     |
| 374      | Bladefist Bay                                        | 1     | 14     |
| 375      | Deadeye Shore                                        | 1     | 14     |
| 377      | Southfury River                                      | 1     | 0      |
| 378      | Camp Taurajo                                         | 1     | 17     |
| 379      | Far Watch Post                                       | 1     | 17     |
| 380      | The Crossroads                                       | 1     | 17     |
| 381      | Boulder Lode Mine                                    | 1     | 17     |
| 382      | The Sludge Fen                                       | 1     | 17     |
| 383      | The Dry Hills                                        | 1     | 17     |
| 384      | Dreadmist Peak                                       | 1     | 17     |
| 385      | Northwatch Hold                                      | 1     | 17     |
| 386      | The Forgotten Pools                                  | 1     | 17     |
| 387      | Lushwater Oasis                                      | 1     | 17     |
| 388      | The Stagnant Oasis                                   | 1     | 17     |
| 390      | Field of Giants                                      | 1     | 17     |
| 391      | The Merchant Coast                                   | 1     | 17     |
| 392      | Ratchet                                              | 1     | 17     |
| 393      | Darkspear Strand                                     | 1     | 14     |
| 394      | Grizzly Hills                                        | 571   | 0      |
| 395      | Grizzlemaw                                           | 571   | 394    |
| 396      | Winterhoof Water Well                                | 1     | 215    |
| 397      | Thunderhorn Water Well                               | 1     | 215    |
| 398      | Wildmane Water Well                                  | 1     | 215    |
| 399      | Skyline Ridge                                        | 1     | 215    |
| 400      | Thousand Needles                                     | 1     | 0      |
| 401      | The Tidus Stair                                      | 1     | 17     |
| 403      | Shady Rest Inn                                       | 1     | 15     |
| 404      | Bael'dun Digsite                                     | 1     | 215    |
| 405      | Desolace                                             | 1     | 0      |
| 406      | Stonetalon Mountains                                 | 1     | 0      |
| 407      | Orgrimmar UNUSED                                     | 1     | 14     |
| 408      | Gillijim's Isle                                      | 0     | 0      |
| 409      | Island of Doctor Lapidis                             | 0     | 0      |
| 410      | Razorwind Canyon                                     | 1     | 14     |
| 411      | Bathran's Haunt                                      | 1     | 331    |
| 412      | The Ruins of Ordil'Aran                              | 1     | 331    |
| 413      | Maestra's Post                                       | 1     | 331    |
| 414      | The Zoram Strand                                     | 1     | 331    |
| 415      | Astranaar                                            | 1     | 331    |
| 416      | The Shrine of Aessina                                | 1     | 331    |
| 417      | Fire Scar Shrine                                     | 1     | 331    |
| 418      | The Ruins of Stardust                                | 1     | 331    |
| 419      | The Howling Vale                                     | 1     | 331    |
| 420      | Silverwind Refuge                                    | 1     | 331    |
| 421      | Mystral Lake                                         | 1     | 331    |
| 422      | Fallen Sky Lake                                      | 1     | 331    |
| 424      | Iris Lake                                            | 1     | 331    |
| 425      | Moonwell                                             | 1     | 331    |
| 426      | Raynewood Retreat                                    | 1     | 331    |
| 427      | The Shady Nook                                       | 1     | 331    |
| 428      | Night Run                                            | 1     | 331    |
| 429      | Xavian                                               | 1     | 331    |
| 430      | Satyrnaar                                            | 1     | 331    |
| 431      | Splintertree Post                                    | 1     | 331    |
| 432      | The Dor'Danil Barrow Den                             | 1     | 331    |
| 433      | Falfarren River                                      | 1     | 331    |
| 434      | Felfire Hill                                         | 1     | 331    |
| 435      | Demon Fall Canyon                                    | 1     | 331    |
| 436      | Demon Fall Ridge                                     | 1     | 331    |
| 437      | Warsong Lumber Camp                                  | 1     | 331    |
| 438      | Bough Shadow                                         | 1     | 331    |
| 439      | The Shimmering Flats                                 | 1     | 400    |
| 440      | Tanaris                                              | 1     | 0      |
| 441      | Lake Falathim                                        | 1     | 331    |
| 442      | Auberdine                                            | 1     | 148    |
| 443      | Ruins of Mathystra                                   | 1     | 148    |
| 444      | Tower of Althalaxx                                   | 1     | 148    |
| 445      | Cliffspring Falls                                    | 1     | 148    |
| 446      | Bashal'Aran                                          | 1     | 148    |
| 447      | Ameth'Aran                                           | 1     | 148    |
| 448      | Grove of the Ancients                                | 1     | 148    |
| 449      | The Master's Glaive                                  | 1     | 148    |
| 450      | Remtravel's Excavation                               | 1     | 148    |
| 452      | Mist's Edge                                          | 1     | 148    |
| 453      | The Long Wash                                        | 1     | 148    |
| 454      | Wildbend River                                       | 1     | 148    |
| 455      | Blackwood Den                                        | 1     | 148    |
| 456      | Cliffspring River                                    | 1     | 148    |
| 457      | The Veiled Sea                                       | 1     | 0      |
| 458      | Gold Road                                            | 1     | 17     |
| 459      | Scarlet Watch Post                                   | 0     | 85     |
| 460      | Sun Rock Retreat                                     | 1     | 406    |
| 461      | Windshear Crag                                       | 1     | 406    |
| 463      | Cragpool Lake                                        | 1     | 406    |
| 464      | Mirkfallon Lake                                      | 1     | 406    |
| 465      | The Charred Vale                                     | 1     | 406    |
| 466      | Valley of the Bloodfuries                            | 1     | 406    |
| 467      | Stonetalon Peak                                      | 1     | 406    |
| 468      | The Talon Den                                        | 1     | 406    |
| 469      | Greatwood Vale                                       | 1     | 406    |
| 470      | Thunder Bluff UNUSED                                 | 1     | 215    |
| 471      | Brave Wind Mesa                                      | 1     | 215    |
| 472      | Fire Stone Mesa                                      | 1     | 215    |
| 473      | Mantle Rock                                          | 1     | 215    |
| 474      | Hunter Rise UNUSED                                   | 1     | 215    |
| 475      | Spirit RiseUNUSED                                    | 1     | 215    |
| 476      | Elder RiseUNUSED                                     | 1     | 215    |
| 477      | Ruins of Jubuwal                                     | 0     | 33     |
| 478      | Pools of Arlithrien                                  | 1     | 141    |
| 479      | The Rustmaul Dig Site                                | 1     | 400    |
| 480      | Camp E'thok                                          | 1     | 400    |
| 481      | Splithoof Crag                                       | 1     | 400    |
| 482      | Highperch                                            | 1     | 400    |
| 483      | The Screeching Canyon                                | 1     | 400    |
| 484      | Freewind Post                                        | 1     | 400    |
| 485      | The Great Lift                                       | 1     | 400    |
| 486      | Galak Hold                                           | 1     | 400    |
| 487      | Roguefeather Den                                     | 1     | 400    |
| 488      | The Weathered Nook                                   | 1     | 400    |
| 489      | Thalanaar                                            | 1     | 357    |
| 490      | Un'Goro Crater                                       | 1     | 0      |
| 491      | Razorfen Kraul                                       | 47    | 0      |
| 492      | Raven Hill Cemetery                                  | 0     | 10     |
| 493      | Moonglade                                            | 1     | 0      |
| 495      | Howling Fjord                                        | 571   | 0      |
| 496      | Brackenwall Village                                  | 1     | 15     |
| 497      | Swamplight Manor                                     | 1     | 15     |
| 498      | Bloodfen Burrow                                      | 1     | 15     |
| 499      | Darkmist Cavern                                      | 1     | 15     |
| 500      | Moggle Point                                         | 1     | 15     |
| 501      | Beezil's Wreck                                       | 1     | 15     |
| 502      | Witch Hill                                           | 1     | 15     |
| 503      | Sentry Point                                         | 1     | 15     |
| 504      | North Point Tower                                    | 1     | 15     |
| 505      | West Point Tower                                     | 1     | 15     |
| 506      | Lost Point                                           | 1     | 15     |
| 507      | Bluefen                                              | 1     | 15     |
| 508      | Stonemaul Ruins                                      | 1     | 15     |
| 509      | The Den of Flame                                     | 1     | 15     |
| 510      | The Dragonmurk                                       | 1     | 15     |
| 511      | Wyrmbog                                              | 1     | 15     |
| 512      | Blackhoof Village                                    | 1     | 15     |
| 513      | Theramore Isle                                       | 1     | 15     |
| 514      | Foothold Citadel                                     | 1     | 15     |
| 515      | Ironclad Prison                                      | 1     | 15     |
| 516      | Dustwallow Bay                                       | 1     | 15     |
| 517      | Tidefury Cove                                        | 1     | 15     |
| 518      | Dreadmurk Shore                                      | 1     | 15     |
| 536      | Addle's Stead                                        | 0     | 10     |
| 537      | Fire Plume Ridge                                     | 1     | 490    |
| 538      | Lakkari Tar Pits                                     | 1     | 490    |
| 539      | Terror Run                                           | 1     | 490    |
| 540      | The Slithering Scar                                  | 1     | 490    |
| 541      | Marshal's Refuge                                     | 1     | 490    |
| 542      | Fungal Rock                                          | 1     | 490    |
| 543      | Golakka Hot Springs                                  | 1     | 490    |
| 556      | The Loch                                             | 0     | 38     |
| 576      | Beggar's Haunt                                       | 0     | 10     |
| 596      | Kodo Graveyard                                       | 1     | 405    |
| 597      | Ghost Walker Post                                    | 1     | 405    |
| 598      | Sar'theris Strand                                    | 1     | 405    |
| 599      | Thunder Axe Fortress                                 | 1     | 405    |
| 600      | Bolgan's Hole                                        | 1     | 405    |
| 602      | Mannoroc Coven                                       | 1     | 405    |
| 603      | Sargeron                                             | 1     | 405    |
| 604      | Magram Village                                       | 1     | 405    |
| 606      | Gelkis Village                                       | 1     | 405    |
| 607      | Valley of Spears                                     | 1     | 405    |
| 608      | Nijel's Point                                        | 1     | 405    |
| 609      | Kolkar Village                                       | 1     | 405    |
| 616      | Hyjal                                                | 1     | 0      |
| 618      | Winterspring                                         | 1     | 0      |
| 636      | Blackwolf River                                      | 1     | 406    |
| 637      | Kodo Rock                                            | 1     | 215    |
| 638      | Hidden Path                                          | 1     | 14     |
| 639      | Spirit Rock                                          | 1     | 14     |
| 640      | Shrine of the Dormant Flame                          | 1     | 14     |
| 656      | Lake Elune'ara                                       | 1     | 493    |
| 657      | The Harborage                                        | 0     | 8      |
| 676      | Outland                                              | 150   | 0      |
| 696      | Craftsmen's Terrace UNUSED                           | 1     | 141    |
| 697      | Tradesmen's Terrace UNUSED                           | 1     | 141    |
| 698      | The Temple Gardens UNUSED                            | 1     | 141    |
| 699      | Temple of Elune UNUSED                               | 1     | 141    |
| 700      | Cenarion Enclave UNUSED                              | 1     | 141    |
| 701      | Warrior's Terrace UNUSED                             | 1     | 141    |
| 702      | Rut'theran Village                                   | 1     | 141    |
| 716      | Ironband's Compound                                  | 0     | 1      |
| 717      | The Stockade                                         | 34    | 0      |
| 718      | Wailing Caverns                                      | 43    | 0      |
| 719      | Blackfathom Deeps                                    | 48    | 0      |
| 720      | Fray Island                                          | 1     | 17     |
| 721      | Gnomeregan                                           | 90    | 0      |
| 722      | Razorfen Downs                                       | 129   | 0      |
| 736      | Ban'ethil Hollow                                     | 1     | 141    |
| 796      | Scarlet Monastery                                    | 189   | 0      |
| 797      | Jerod's Landing                                      | 0     | 12     |
| 798      | Ridgepoint Tower                                     | 0     | 12     |
| 799      | The Darkened Bank                                    | 0     | 10     |
| 800      | Coldridge Pass                                       | 0     | 1      |
| 801      | Chill Breeze Valley                                  | 0     | 1      |
| 802      | Shimmer Ridge                                        | 0     | 1      |
| 803      | Amberstill Ranch                                     | 0     | 1      |
| 804      | The Tundrid Hills                                    | 0     | 1      |
| 805      | South Gate Pass                                      | 0     | 1      |
| 806      | South Gate Outpost                                   | 0     | 1      |
| 807      | North Gate Pass                                      | 0     | 1      |
| 808      | North Gate Outpost                                   | 0     | 1      |
| 809      | Gates of Ironforge                                   | 0     | 1      |
| 810      | Stillwater Pond                                      | 0     | 85     |
| 811      | Nightmare Vale                                       | 0     | 85     |
| 812      | Venomweb Vale                                        | 0     | 85     |
| 813      | The Bulwark                                          | 0     | 28     |
| 814      | Southfury River                                      | 1     | 14     |
| 815      | Southfury River                                      | 1     | 17     |
| 816      | Razormane Grounds                                    | 1     | 14     |
| 817      | Skull Rock                                           | 1     | 14     |
| 818      | Palemane Rock                                        | 1     | 215    |
| 819      | Windfury Ridge                                       | 1     | 215    |
| 820      | The Golden Plains                                    | 1     | 215    |
| 821      | The Rolling Plains                                   | 1     | 215    |
| 836      | Dun Algaz                                            | 0     | 11     |
| 837      | Dun Algaz                                            | 0     | 38     |
| 838      | North Gate Pass                                      | 0     | 38     |
| 839      | South Gate Pass                                      | 0     | 38     |
| 856      | Twilight Grove                                       | 0     | 10     |
| 876      | GM Island                                            | 1     | 0      |
| 877      | Delete ME                                            | 1     | 17     |
| 878      | Southfury River                                      | 1     | 16     |
| 879      | Southfury River                                      | 1     | 331    |
| 880      | Thandol Span                                         | 0     | 45     |
| 881      | Thandol Span                                         | 0     | 11     |
| 896      | Purgation Isle                                       | 0     | 267    |
| 916      | The Jansen Stead                                     | 0     | 40     |
| 917      | The Dead Acre                                        | 0     | 40     |
| 918      | The Molsen Farm                                      | 0     | 40     |
| 919      | Stendel's Pond                                       | 0     | 40     |
| 920      | The Dagger Hills                                     | 0     | 40     |
| 921      | Demont's Place                                       | 0     | 40     |
| 922      | The Dust Plains                                      | 0     | 40     |
| 923      | Stonesplinter Valley                                 | 0     | 38     |
| 924      | Valley of Kings                                      | 0     | 38     |
| 925      | Algaz Station                                        | 0     | 38     |
| 926      | Bucklebree Farm                                      | 0     | 130    |
| 927      | The Shining Strand                                   | 0     | 130    |
| 928      | North Tide's Hollow                                  | 0     | 130    |
| 936      | Grizzlepaw Ridge                                     | 0     | 38     |
| 956      | The Verdant Fields                                   | 169   | 0      |
| 976      | Gadgetzan                                            | 1     | 440    |
| 977      | Steamwheedle Port                                    | 1     | 440    |
| 978      | Zul'Farrak                                           | 1     | 440    |
| 979      | Sandsorrow Watch                                     | 1     | 440    |
| 980      | Thistleshrub Valley                                  | 1     | 440    |
| 981      | The Gaping Chasm                                     | 1     | 440    |
| 982      | The Noxious Lair                                     | 1     | 440    |
| 983      | Dunemaul Compound                                    | 1     | 440    |
| 984      | Eastmoon Ruins                                       | 1     | 440    |
| 985      | Waterspring Field                                    | 1     | 440    |
| 986      | Zalashji's Den                                       | 1     | 440    |
| 987      | Land's End Beach                                     | 1     | 440    |
| 988      | Wavestrider Beach                                    | 1     | 440    |
| 989      | Uldum                                                | 1     | 440    |
| 990      | Valley of the Watchers                               | 1     | 440    |
| 991      | Gunstan's Post                                       | 1     | 440    |
| 992      | Southmoon Ruins                                      | 1     | 440    |
| 996      | Render's Camp                                        | 0     | 44     |
| 997      | Render's Valley                                      | 0     | 44     |
| 998      | Render's Rock                                        | 0     | 44     |
| 999      | Stonewatch Tower                                     | 0     | 44     |
| 1000     | Galardell Valley                                     | 0     | 44     |
| 1001     | Lakeridge Highway                                    | 0     | 44     |
| 1002     | Three Corners                                        | 0     | 44     |
| 1016     | Direforge Hill                                       | 0     | 11     |
| 1017     | Raptor Ridge                                         | 0     | 11     |
| 1018     | Black Channel Marsh                                  | 0     | 11     |
| 1019     | The Green Belt                                       | 0     | 139    |
| 1020     | Mosshide Fen                                         | 0     | 11     |
| 1021     | Thelgen Rock                                         | 0     | 11     |
| 1022     | Bluegill Marsh                                       | 0     | 11     |
| 1023     | Saltspray Glen                                       | 0     | 11     |
| 1024     | Sundown Marsh                                        | 0     | 11     |
| 1025     | The Green Belt                                       | 0     | 11     |
| 1036     | Angerfang Encampment                                 | 0     | 11     |
| 1037     | Grim Batol                                           | 0     | 11     |
| 1038     | Dragonmaw Gates                                      | 0     | 11     |
| 1039     | The Lost Fleet                                       | 0     | 11     |
| 1056     | Darrow Hill                                          | 0     | 267    |
| 1057     | Thoradin's Wall                                      | 0     | 267    |
| 1076     | Webwinder Path                                       | 1     | 406    |
| 1097     | The Hushed Bank                                      | 0     | 10     |
| 1098     | Manor Mistmantle                                     | 0     | 10     |
| 1099     | Camp Mojache                                         | 1     | 357    |
| 1100     | Grimtotem Compound                                   | 1     | 357    |
| 1101     | The Writhing Deep                                    | 1     | 357    |
| 1102     | Wildwind Lake                                        | 1     | 357    |
| 1103     | Gordunni Outpost                                     | 1     | 357    |
| 1104     | Mok'Gordun                                           | 1     | 357    |
| 1105     | Feral Scar Vale                                      | 1     | 357    |
| 1106     | Frayfeather Highlands                                | 1     | 357    |
| 1107     | Idlewind Lake                                        | 1     | 357    |
| 1108     | The Forgotten Coast                                  | 1     | 357    |
| 1109     | East Pillar                                          | 1     | 357    |
| 1110     | West Pillar                                          | 1     | 357    |
| 1111     | Dream Bough                                          | 1     | 357    |
| 1112     | Jademir Lake                                         | 1     | 357    |
| 1113     | Oneiros                                              | 1     | 357    |
| 1114     | Ruins of Ravenwind                                   | 1     | 357    |
| 1115     | Rage Scar Hold                                       | 1     | 357    |
| 1116     | Feathermoon Stronghold                               | 1     | 357    |
| 1117     | Ruins of Solarsal                                    | 1     | 357    |
| 1118     | Lower Wilds UNUSED                                   | 1     | 357    |
| 1119     | The Twin Colossals                                   | 1     | 357    |
| 1120     | Sardor Isle                                          | 1     | 357    |
| 1121     | Isle of Dread                                        | 1     | 357    |
| 1136     | High Wilderness                                      | 1     | 357    |
| 1137     | Lower Wilds                                          | 1     | 357    |
| 1156     | Southern Barrens                                     | 1     | 17     |
| 1157     | Southern Gold Road                                   | 1     | 17     |
| 1176     | Zul'Farrak                                           | 209   | 0      |
| 1196     | Utgarde Pinnacle                                     | 575   | 0      |
| 1216     | Timbermaw Hold                                       | 1     | 16     |
| 1217     | Vanndir Encampment                                   | 1     | 16     |
| 1218     | TESTAzshara                                          | 1     | 16     |
| 1219     | Legash Encampment                                    | 1     | 16     |
| 1220     | Thalassian Base Camp                                 | 1     | 16     |
| 1221     | Ruins of Eldarath                                    | 1     | 16     |
| 1222     | Hetaera's Clutch                                     | 1     | 16     |
| 1223     | Temple of Zin-Malor                                  | 1     | 16     |
| 1224     | Bear's Head                                          | 1     | 16     |
| 1225     | Ursolan                                              | 1     | 16     |
| 1226     | Temple of Arkkoran                                   | 1     | 16     |
| 1227     | Bay of Storms                                        | 1     | 16     |
| 1228     | The Shattered Strand                                 | 1     | 16     |
| 1229     | Tower of Eldara                                      | 1     | 16     |
| 1230     | Jagged Reef                                          | 1     | 16     |
| 1231     | Southridge Beach                                     | 1     | 16     |
| 1232     | Ravencrest Monument                                  | 1     | 16     |
| 1233     | Forlorn Ridge                                        | 1     | 16     |
| 1234     | Lake Mennar                                          | 1     | 16     |
| 1235     | Shadowsong Shrine                                    | 1     | 16     |
| 1236     | Haldarr Encampment                                   | 1     | 16     |
| 1237     | Valormok                                             | 1     | 16     |
| 1256     | The Ruined Reaches                                   | 1     | 16     |
| 1276     | The Talondeep Path                                   | 1     | 331    |
| 1277     | The Talondeep Path                                   | 1     | 406    |
| 1296     | Rocktusk Farm                                        | 1     | 14     |
| 1297     | Jaggedswine Farm                                     | 1     | 14     |
| 1316     | Razorfen Downs                                       | 1     | 17     |
| 1336     | Lost Rigger Cove                                     | 1     | 440    |
| 1337     | Uldaman                                              | 70    | 0      |
| 1338     | Lordamere Lake                                       | 0     | 130    |
| 1339     | Lordamere Lake                                       | 0     | 36     |
| 1357     | Gallows' Corner                                      | 0     | 36     |
| 1377     | Silithus                                             | 1     | 0      |
| 1397     | Emerald Forest                                       | 169   | 0      |
| 1417     | Sunken Temple                                        | 109   | 0      |
| 1437     | Dreadmaul Hold                                       | 0     | 4      |
| 1438     | Nethergarde Keep                                     | 0     | 4      |
| 1439     | Dreadmaul Post                                       | 0     | 4      |
| 1440     | Serpent's Coil                                       | 0     | 4      |
| 1441     | Altar of Storms                                      | 0     | 4      |
| 1442     | Firewatch Ridge                                      | 0     | 51     |
| 1443     | The Slag Pit                                         | 0     | 51     |
| 1444     | The Sea of Cinders                                   | 0     | 51     |
| 1445     | Blackrock Mountain                                   | 0     | 51     |
| 1446     | Thorium Point                                        | 0     | 51     |
| 1457     | Garrison Armory                                      | 0     | 4      |
| 1477     | The Temple of Atal'Hakkar                            | 109   | 0      |
| 1497     | Undercity                                            | 0     | 0      |
| 1517     | Uldaman                                              | 0     | 3      |
| 1518     | Not Used Deadmines                                   | 0     | 40     |
| 1519     | Stormwind City                                       | 0     | 0      |
| 1537     | Ironforge                                            | 0     | 0      |
| 1557     | Splithoof Hold                                       | 1     | 400    |
| 1577     | The Cape of Stranglethorn                            | 0     | 33     |
| 1578     | Southern Savage Coast                                | 0     | 33     |
| 1579     | Unused The Deadmines 002                             | 0     | 0      |
| 1580     | Unused Ironclad Cove 003                             | 0     | 1579   |
| 1581     | The Deadmines                                        | 36    | 0      |
| 1582     | Ironclad Cove                                        | 36    | 1581   |
| 1583     | Blackrock Spire                                      | 229   | 0      |
| 1584     | Blackrock Depths                                     | 230   | 0      |
| 1597     | Raptor Grounds UNUSED                                | 1     | 17     |
| 1598     | Grol'dom Farm UNUSED                                 | 1     | 17     |
| 1599     | Mor'shan Base Camp                                   | 1     | 17     |
| 1600     | Honor's Stand UNUSED                                 | 1     | 17     |
| 1601     | Blackthorn Ridge UNUSED                              | 1     | 17     |
| 1602     | Bramblescar UNUSED                                   | 1     | 17     |
| 1603     | Agama'gor UNUSED                                     | 1     | 17     |
| 1617     | Valley of Heroes                                     | 0     | 1519   |
| 1637     | Orgrimmar                                            | 1     | 0      |
| 1638     | Thunder Bluff                                        | 1     | 0      |
| 1639     | Elder Rise                                           | 1     | 1638   |
| 1640     | Spirit Rise                                          | 1     | 1638   |
| 1641     | Hunter Rise                                          | 1     | 1638   |
| 1657     | Darnassus                                            | 1     | 0      |
| 1658     | Cenarion Enclave                                     | 1     | 1657   |
| 1659     | Craftsmen's Terrace                                  | 1     | 1657   |
| 1660     | Warrior's Terrace                                    | 1     | 1657   |
| 1661     | The Temple Gardens                                   | 1     | 1657   |
| 1662     | Tradesmen's Terrace                                  | 1     | 1657   |
| 1677     | Gavin's Naze                                         | 0     | 36     |
| 1678     | Sofera's Naze                                        | 0     | 36     |
| 1679     | Corrahn's Dagger                                     | 0     | 36     |
| 1680     | The Headland                                         | 0     | 36     |
| 1681     | Misty Shore                                          | 0     | 36     |
| 1682     | Dandred's Fold                                       | 0     | 36     |
| 1683     | Growless Cave                                        | 0     | 36     |
| 1684     | Chillwind Point                                      | 0     | 36     |
| 1697     | Raptor Grounds                                       | 1     | 17     |
| 1698     | Bramblescar                                          | 1     | 17     |
| 1699     | Thorn Hill                                           | 1     | 17     |
| 1700     | Agama'gor                                            | 1     | 17     |
| 1701     | Blackthorn Ridge                                     | 1     | 17     |
| 1702     | Honor's Stand                                        | 1     | 17     |
| 1703     | The Mor'shan Rampart                                 | 1     | 17     |
| 1704     | Grol'dom Farm                                        | 1     | 17     |
| 1717     | Razorfen Kraul                                       | 1     | 17     |
| 1718     | The Great Lift                                       | 1     | 17     |
| 1737     | Mistvale Valley                                      | 0     | 33     |
| 1738     | Nek'mani Wellspring                                  | 0     | 33     |
| 1739     | Bloodsail Compound                                   | 0     | 33     |
| 1740     | Venture Co. Base Camp                                | 0     | 33     |
| 1741     | Gurubashi Arena                                      | 0     | 33     |
| 1742     | Spirit Den                                           | 0     | 33     |
| 1757     | The Crimson Veil                                     | 0     | 33     |
| 1758     | The Riptide                                          | 0     | 33     |
| 1759     | The Damsel's Luck                                    | 0     | 33     |
| 1760     | Venture Co. Operations Center                        | 0     | 33     |
| 1761     | Deadwood Village                                     | 1     | 361    |
| 1762     | Felpaw Village                                       | 1     | 361    |
| 1763     | Jaedenar                                             | 1     | 361    |
| 1764     | Bloodvenom River                                     | 1     | 361    |
| 1765     | Bloodvenom Falls                                     | 1     | 361    |
| 1766     | Shatter Scar Vale                                    | 1     | 361    |
| 1767     | Irontree Woods                                       | 1     | 361    |
| 1768     | Irontree Cavern                                      | 1     | 361    |
| 1769     | Timbermaw Hold                                       | 1     | 361    |
| 1770     | Shadow Hold                                          | 1     | 361    |
| 1771     | Shrine of the Deceiver                               | 1     | 361    |
| 1777     | Itharius's Cave                                      | 0     | 8      |
| 1778     | Sorrowmurk                                           | 0     | 8      |
| 1779     | Draenil'dur Village                                  | 0     | 8      |
| 1780     | Splinterspear Junction                               | 0     | 8      |
| 1797     | Stagalbog                                            | 0     | 8      |
| 1798     | The Shifting Mire                                    | 0     | 8      |
| 1817     | Stagalbog Cave                                       | 0     | 8      |
| 1837     | Witherbark Caverns                                   | 0     | 45     |
| 1857     | Thoradin's Wall                                      | 0     | 45     |
| 1858     | Boulder'gor                                          | 0     | 45     |
| 1877     | Valley of Fangs                                      | 0     | 3      |
| 1878     | The Dustbowl                                         | 0     | 3      |
| 1879     | Mirage Flats                                         | 0     | 3      |
| 1880     | Featherbeard's Hovel                                 | 0     | 47     |
| 1881     | Shindigger's Camp                                    | 0     | 47     |
| 1882     | Plaguemist Ravine                                    | 0     | 47     |
| 1883     | Valorwind Lake                                       | 0     | 47     |
| 1884     | Agol'watha                                           | 0     | 47     |
| 1885     | Hiri'watha                                           | 0     | 47     |
| 1886     | The Creeping Ruin                                    | 0     | 47     |
| 1887     | Bogen's Ledge                                        | 0     | 47     |
| 1897     | The Maker's Terrace                                  | 0     | 3      |
| 1898     | Dustwind Gulch                                       | 0     | 3      |
| 1917     | Shaol'watha                                          | 0     | 47     |
| 1937     | Noonshade Ruins                                      | 1     | 440    |
| 1938     | Broken Pillar                                        | 1     | 440    |
| 1939     | Abyssal Sands                                        | 1     | 440    |
| 1940     | Southbreak Shore                                     | 1     | 440    |
| 1941     | Caverns of Time                                      | 1     | 0      |
| 1942     | The Marshlands                                       | 1     | 490    |
| 1943     | Ironstone Plateau                                    | 1     | 490    |
| 1957     | Blackchar Cave                                       | 0     | 51     |
| 1958     | Tanner Camp                                          | 0     | 51     |
| 1959     | Dustfire Valley                                      | 0     | 51     |
| 1977     | Zul'Gurub                                            | 309   | 0      |
| 1978     | Misty Reed Post                                      | 0     | 8      |
| 1997     | Bloodvenom Post                                      | 1     | 361    |
| 1998     | Talonbranch Glade                                    | 1     | 361    |
| 2017     | Stratholme                                           | 329   | 0      |
| 2037     | Quel'thalas                                          | 0     | 0      |
| 2057     | Scholomance                                          | 289   | 0      |
| 2077     | Twilight Vale                                        | 1     | 148    |
| 2078     | Twilight Shore                                       | 1     | 148    |
| 2079     | Alcaz Island                                         | 1     | 15     |
| 2097     | Darkcloud Pinnacle                                   | 1     | 400    |
| 2098     | Dawning Wood Catacombs                               | 0     | 10     |
| 2099     | Stonewatch Keep                                      | 0     | 44     |
| 2100     | Maraudon                                             | 349   | 0      |
| 2101     | Stoutlager Inn                                       | 0     | 38     |
| 2102     | Thunderbrew Distillery                               | 0     | 1      |
| 2103     | Menethil Keep                                        | 0     | 11     |
| 2104     | Deepwater Tavern                                     | 0     | 11     |
| 2117     | Shadow Grave                                         | 0     | 85     |
| 2118     | Brill Town Hall                                      | 0     | 85     |
| 2119     | Gallows' End Tavern                                  | 0     | 85     |
| 2137     | The Pools of VisionUNUSED                            | 1     | 215    |
| 2138     | Dreadmist Den                                        | 1     | 17     |
| 2157     | Bael'dun Keep                                        | 1     | 17     |
| 2158     | Emberstrife's Den                                    | 1     | 15     |
| 2159     | Onyxia's Lair                                        | 1     | 0      |
| 2160     | Windshear Mine                                       | 1     | 406    |
| 2161     | Roland's Doom                                        | 0     | 10     |
| 2177     | Battle Ring                                          | 0     | 33     |
| 2197     | The Pools of Vision                                  | 1     | 1638   |
| 2198     | Shadowbreak Ravine                                   | 1     | 405    |
| 2217     | Broken Spear Village                                 | 1     | 405    |
| 2237     | Whitereach Post                                      | 1     | 400    |
| 2238     | Gornia                                               | 1     | 400    |
| 2239     | Zane's Eye Crater                                    | 1     | 400    |
| 2240     | Mirage Raceway                                       | 1     | 400    |
| 2241     | Frostsaber Rock                                      | 1     | 618    |
| 2242     | The Hidden Grove                                     | 1     | 618    |
| 2243     | Timbermaw Post                                       | 1     | 618    |
| 2244     | Winterfall Village                                   | 1     | 618    |
| 2245     | Mazthoril                                            | 1     | 618    |
| 2246     | Frostfire Hot Springs                                | 1     | 618    |
| 2247     | Ice Thistle Hills                                    | 1     | 618    |
| 2248     | Dun Mandarr                                          | 1     | 618    |
| 2249     | Frostwhisper Gorge                                   | 1     | 618    |
| 2250     | Owl Wing Thicket                                     | 1     | 618    |
| 2251     | Lake Kel'Theril                                      | 1     | 618    |
| 2252     | The Ruins of Kel'Theril                              | 1     | 618    |
| 2253     | Starfall Village                                     | 1     | 618    |
| 2254     | Ban'Thallow Barrow Den                               | 1     | 618    |
| 2255     | Everlook                                             | 1     | 618    |
| 2256     | Darkwhisper Gorge                                    | 1     | 618    |
| 2257     | Deeprun Tram                                         | 369   | 0      |
| 2258     | The Fungal Vale                                      | 0     | 139    |
| 2259     | UNUSEDThe Marris Stead                               | 0     | 139    |
| 2260     | The Marris Stead                                     | 0     | 139    |
| 2261     | The Undercroft                                       | 0     | 139    |
| 2262     | Darrowshire                                          | 0     | 139    |
| 2263     | Crown Guard Tower                                    | 0     | 139    |
| 2264     | Corin's Crossing                                     | 0     | 139    |
| 2265     | Scarlet Base Camp                                    | 0     | 139    |
| 2266     | Tyr's Hand                                           | 0     | 139    |
| 2267     | The Scarlet Basilica                                 | 0     | 139    |
| 2268     | Light's Hope Chapel                                  | 0     | 139    |
| 2269     | Browman Mill                                         | 0     | 139    |
| 2270     | The Noxious Glade                                    | 0     | 139    |
| 2271     | Eastwall Tower                                       | 0     | 139    |
| 2272     | Northdale                                            | 0     | 139    |
| 2273     | Zul'Mashar                                           | 0     | 139    |
| 2274     | Mazra'Alor                                           | 0     | 139    |
| 2275     | Northpass Tower                                      | 0     | 139    |
| 2276     | Quel'Lithien Lodge                                   | 0     | 139    |
| 2277     | Plaguewood                                           | 0     | 139    |
| 2278     | Scourgehold                                          | 0     | 139    |
| 2279     | Stratholme                                           | 0     | 139    |
| 2280     | DO NOT USE                                           | 0     | 0      |
| 2297     | Darrowmere Lake                                      | 0     | 28     |
| 2298     | Caer Darrow                                          | 0     | 28     |
| 2299     | Darrowmere Lake                                      | 0     | 139    |
| 2300     | Caverns of Time                                      | 1     | 440    |
| 2301     | Thistlefur Village                                   | 1     | 331    |
| 2302     | The Quagmire                                         | 1     | 15     |
| 2303     | Windbreak Canyon                                     | 1     | 400    |
| 2317     | South Seas                                           | 1     | 440    |
| 2318     | The Great Sea                                        | 1     | 15     |
| 2319     | The Great Sea                                        | 1     | 17     |
| 2320     | The Great Sea                                        | 1     | 14     |
| 2321     | The Great Sea                                        | 1     | 16     |
| 2322     | The Veiled Sea                                       | 1     | 141    |
| 2323     | The Veiled Sea                                       | 1     | 357    |
| 2324     | The Veiled Sea                                       | 1     | 405    |
| 2325     | The Veiled Sea                                       | 1     | 331    |
| 2326     | The Veiled Sea                                       | 1     | 148    |
| 2337     | Razor Hill Barracks                                  | 1     | 14     |
| 2338     | South Seas                                           | 0     | 33     |
| 2339     | The Great Sea                                        | 0     | 33     |
| 2357     | Bloodtooth Camp                                      | 1     | 331    |
| 2358     | Forest Song                                          | 1     | 331    |
| 2359     | Greenpaw Village                                     | 1     | 331    |
| 2360     | Silverwing Outpost                                   | 1     | 331    |
| 2361     | Nighthaven                                           | 1     | 493    |
| 2362     | Shrine of Remulos                                    | 1     | 493    |
| 2363     | Stormrage Barrow Dens                                | 1     | 493    |
| 2364     | The Great Sea                                        | 0     | 40     |
| 2365     | The Great Sea                                        | 0     | 11     |
| 2366     | The Black Morass                                     | 269   | 0      |
| 2367     | Old Hillsbrad Foothills                              | 560   | 0      |
| 2368     | Tarren Mill                                          | 560   | 2367   |
| 2369     | Southshore                                           | 560   | 2367   |
| 2370     | Durnholde Keep                                       | 560   | 2367   |
| 2371     | Dun Garok                                            | 560   | 2367   |
| 2372     | Hillsbrad Fields                                     | 560   | 2367   |
| 2373     | Eastern Strand                                       | 560   | 2367   |
| 2374     | Nethander Stead                                      | 560   | 2367   |
| 2375     | Darrow Hill                                          | 560   | 2367   |
| 2376     | Southpoint Tower                                     | 560   | 2367   |
| 2377     | Thoradin's Wall                                      | 560   | 2367   |
| 2378     | Western Strand                                       | 560   | 2367   |
| 2379     | Azurelode Mine                                       | 560   | 2367   |
| 2397     | The Great Sea                                        | 0     | 267    |
| 2398     | The Great Sea                                        | 0     | 130    |
| 2399     | The Great Sea                                        | 0     | 85     |
| 2400     | The Forbidding Sea                                   | 0     | 47     |
| 2401     | The Forbidding Sea                                   | 0     | 45     |
| 2402     | The Forbidding Sea                                   | 0     | 11     |
| 2403     | The Forbidding Sea                                   | 0     | 8      |
| 2404     | Tethris Aran                                         | 1     | 405    |
| 2405     | Ethel Rethor                                         | 1     | 405    |
| 2406     | Ranazjar Isle                                        | 1     | 405    |
| 2407     | Kormek's Hut                                         | 1     | 405    |
| 2408     | Shadowprey Village                                   | 1     | 405    |
| 2417     | Blackrock Pass                                       | 0     | 46     |
| 2418     | Morgan's Vigil                                       | 0     | 46     |
| 2419     | Slither Rock                                         | 0     | 46     |
| 2420     | Terror Wing Path                                     | 0     | 46     |
| 2421     | Draco'dar                                            | 0     | 46     |
| 2437     | Ragefire Chasm                                       | 389   | 0      |
| 2457     | Nightsong Woods                                      | 1     | 331    |
| 2477     | The Veiled Sea                                       | 1     | 1377   |
| 2478     | Morlos'Aran                                          | 1     | 361    |
| 2479     | Emerald Sanctuary                                    | 1     | 361    |
| 2480     | Jadefire Glen                                        | 1     | 361    |
| 2481     | Ruins of Constellas                                  | 1     | 361    |
| 2497     | Bitter Reaches                                       | 1     | 16     |
| 2517     | Rise of the Defiler                                  | 0     | 4      |
| 2518     | Lariss Pavilion                                      | 1     | 357    |
| 2519     | Woodpaw Hills                                        | 1     | 357    |
| 2520     | Woodpaw Den                                          | 1     | 357    |
| 2521     | Verdantis River                                      | 1     | 357    |
| 2522     | Ruins of Isildien                                    | 1     | 357    |
| 2537     | Grimtotem Post                                       | 1     | 406    |
| 2538     | Camp Aparaje                                         | 1     | 406    |
| 2539     | Malaka'jin                                           | 1     | 406    |
| 2540     | Boulderslide Ravine                                  | 1     | 406    |
| 2541     | Sishir Canyon                                        | 1     | 406    |
| 2557     | Dire Maul                                            | 429   | 0      |
| 2558     | Deadwind Ravine                                      | 0     | 41     |
| 2559     | Diamondhead River                                    | 0     | 41     |
| 2560     | Ariden's Camp                                        | 0     | 41     |
| 2561     | The Vice                                             | 0     | 41     |
| 2562     | Karazhan                                             | 0     | 41     |
| 2563     | Morgan's Plot                                        | 0     | 41     |
| 2577     | Dire Maul                                            | 1     | 357    |
| 2597     | Alterac Valley                                       | 30    | 0      |
| 2617     | Scrabblescrew's Camp                                 | 1     | 405    |
| 2618     | Jadefire Run                                         | 1     | 361    |
| 2619     | Thondroril River                                     | 0     | 139    |
| 2620     | Thondroril River                                     | 0     | 28     |
| 2621     | Lake Mereldar                                        | 0     | 139    |
| 2622     | Pestilent Scar                                       | 0     | 139    |
| 2623     | The Infectis Scar                                    | 0     | 139    |
| 2624     | Blackwood Lake                                       | 0     | 139    |
| 2625     | Eastwall Gate                                        | 0     | 139    |
| 2626     | Terrorweb Tunnel                                     | 0     | 139    |
| 2627     | Terrordale                                           | 0     | 139    |
| 2637     | Kargathia Keep                                       | 1     | 331    |
| 2657     | Valley of Bones                                      | 1     | 405    |
| 2677     | Blackwing Lair                                       | 469   | 0      |
| 2697     | Deadman's Crossing                                   | 0     | 41     |
| 2717     | Molten Core                                          | 409   | 0      |
| 2737     | The Scarab Wall                                      | 1     | 1377   |
| 2738     | Southwind Village                                    | 1     | 1377   |
| 2739     | Twilight Base Camp                                   | 1     | 1377   |
| 2740     | The Crystal Vale                                     | 1     | 1377   |
| 2741     | The Scarab Dais                                      | 1     | 1377   |
| 2742     | Hive'Ashi                                            | 1     | 1377   |
| 2743     | Hive'Zora                                            | 1     | 1377   |
| 2744     | Hive'Regal                                           | 1     | 1377   |
| 2757     | Shrine of the Fallen Warrior                         | 1     | 17     |
| 2777     | UNUSED Alterac Valley                                | 0     | 267    |
| 2797     | Blackfathom Deeps                                    | 1     | 331    |
| 2817     | Crystalsong Forest                                   | 571   | 0      |
| 2837     | The Master's Cellar                                  | 0     | 41     |
| 2838     | Stonewrought Pass                                    | 0     | 51     |
| 2839     | Alterac Valley                                       | 0     | 36     |
| 2857     | The Rumble Cage                                      | 1     | 440    |
| 2877     | Chunk Test                                           | 451   | 22     |
| 2897     | Zoram'gar Outpost                                    | 1     | 331    |
| 2917     | Hall of Legends                                      | 1     | 0      |
| 2918     | Champions' Hall                                      | 449   | 0      |
| 2937     | Grosh'gok Compound                                   | 0     | 41     |
| 2938     | Sleeping Gorge                                       | 0     | 41     |
| 2957     | Irondeep Mine                                        | 30    | 2597   |
| 2958     | Stonehearth Outpost                                  | 30    | 2597   |
| 2959     | Dun Baldar                                           | 30    | 2597   |
| 2960     | Icewing Pass                                         | 30    | 2597   |
| 2961     | Frostwolf Village                                    | 30    | 2597   |
| 2962     | Tower Point                                          | 30    | 2597   |
| 2963     | Coldtooth Mine                                       | 30    | 2597   |
| 2964     | Winterax Hold                                        | 30    | 2597   |
| 2977     | Iceblood Garrison                                    | 30    | 2597   |
| 2978     | Frostwolf Keep                                       | 30    | 2597   |
| 2979     | Tor'kren Farm                                        | 1     | 14     |
| 3017     | Frost Dagger Pass                                    | 30    | 2597   |
| 3037     | Ironstone Camp                                       | 1     | 400    |
| 3038     | Weazel's Crater                                      | 1     | 400    |
| 3039     | Tahonda Ruins                                        | 1     | 400    |
| 3057     | Field of Strife                                      | 30    | 2597   |
| 3058     | Icewing Cavern                                       | 30    | 2597   |
| 3077     | Valor's Rest                                         | 1     | 1377   |
| 3097     | The Swarming Pillar                                  | 1     | 1377   |
| 3098     | Twilight Post                                        | 1     | 1377   |
| 3099     | Twilight Outpost                                     | 1     | 1377   |
| 3100     | Ravaged Twilight Camp                                | 1     | 1377   |
| 3117     | Shalzaru's Lair                                      | 1     | 357    |
| 3137     | Talrendis Point                                      | 1     | 16     |
| 3138     | Rethress Sanctum                                     | 1     | 16     |
| 3139     | Moon Horror Den                                      | 1     | 618    |
| 3140     | Scalebeard's Cave                                    | 1     | 16     |
| 3157     | Boulderslide Cavern                                  | 1     | 406    |
| 3177     | Warsong Labor Camp                                   | 1     | 331    |
| 3197     | Chillwind Camp                                       | 0     | 28     |
| 3217     | The Maul                                             | 429   | 2557   |
| 3237     | The Maul UNUSED                                      | 429   | 2557   |
| 3257     | Bones of Grakkarond                                  | 1     | 1377   |
| 3277     | Warsong Gulch                                        | 489   | 0      |
| 3297     | Frostwolf Graveyard                                  | 30    | 2597   |
| 3298     | Frostwolf Pass                                       | 30    | 2597   |
| 3299     | Dun Baldar Pass                                      | 30    | 2597   |
| 3300     | Iceblood Graveyard                                   | 30    | 2597   |
| 3301     | Snowfall Graveyard                                   | 30    | 2597   |
| 3302     | Stonehearth Graveyard                                | 30    | 2597   |
| 3303     | Stormpike Graveyard                                  | 30    | 2597   |
| 3304     | Icewing Bunker                                       | 30    | 2597   |
| 3305     | Stonehearth Bunker                                   | 30    | 2597   |
| 3306     | Wildpaw Ridge                                        | 30    | 2597   |
| 3317     | Revantusk Village                                    | 0     | 47     |
| 3318     | Rock of Durotan                                      | 30    | 2597   |
| 3319     | Silverwing Grove                                     | 1     | 331    |
| 3320     | Warsong Lumber Mill                                  | 489   | 3277   |
| 3321     | Silverwing Hold                                      | 489   | 3277   |
| 3337     | Wildpaw Cavern                                       | 30    | 2597   |
| 3338     | The Veiled Cleft                                     | 30    | 2597   |
| 3357     | Yojamba Isle                                         | 0     | 33     |
| 3358     | Arathi Basin                                         | 529   | 0      |
| 3377     | The Coil                                             | 309   | 1977   |
| 3378     | Altar of Hir'eek                                     | 309   | 1977   |
| 3379     | Shadra'zaar                                          | 309   | 1977   |
| 3380     | Hakkari Grounds                                      | 309   | 1977   |
| 3381     | Naze of Shirvallah                                   | 309   | 1977   |
| 3382     | Temple of Bethekk                                    | 309   | 1977   |
| 3383     | The Bloodfire Pit                                    | 309   | 1977   |
| 3384     | Altar of the Blood God                               | 309   | 1977   |
| 3397     | Zanza's Rise                                         | 309   | 1977   |
| 3398     | Edge of Madness                                      | 309   | 1977   |
| 3417     | Trollbane Hall                                       | 529   | 3358   |
| 3418     | Defiler's Den                                        | 529   | 3358   |
| 3419     | Pagle's Pointe                                       | 309   | 1977   |
| 3420     | Farm                                                 | 529   | 3358   |
| 3421     | Blacksmith                                           | 529   | 3358   |
| 3422     | Lumber Mill                                          | 529   | 3358   |
| 3423     | Gold Mine                                            | 529   | 3358   |
| 3424     | Stables                                              | 529   | 3358   |
| 3425     | Cenarion Hold                                        | 1     | 1377   |
| 3426     | Staghelm Point                                       | 1     | 1377   |
| 3427     | Bronzebeard Encampment                               | 1     | 1377   |
| 3428     | Ahn'Qiraj                                            | 531   | 0      |
| 3429     | Ruins of Ahn'Qiraj                                   | 509   | 0      |
| 3430     | Eversong Woods                                       | 530   | 0      |
| 3431     | Sunstrider Isle                                      | 530   | 3430   |
| 3432     | Shrine of Dath'Remar                                 | 530   | 3430   |
| 3433     | Ghostlands                                           | 530   | 0      |
| 3434     | Scarab Terrace                                       | 531   | 3428   |
| 3435     | General's Terrace                                    | 531   | 3428   |
| 3436     | The Reservoir                                        | 531   | 3428   |
| 3437     | The Hatchery                                         | 531   | 3428   |
| 3438     | The Comb                                             | 531   | 3428   |
| 3439     | Watchers' Terrace                                    | 531   | 3428   |
| 3440     | Scarab Terrace                                       | 509   | 3429   |
| 3441     | General's Terrace                                    | 509   | 3429   |
| 3442     | The Reservoir                                        | 509   | 3429   |
| 3443     | The Hatchery                                         | 509   | 3429   |
| 3444     | The Comb                                             | 509   | 3429   |
| 3445     | Watchers' Terrace                                    | 509   | 3429   |
| 3446     | Twilight's Run                                       | 1     | 1377   |
| 3447     | Ortell's Hideout                                     | 1     | 1377   |
| 3448     | Scarab Terrace                                       | 509   | 3429   |
| 3449     | General's Terrace                                    | 509   | 3429   |
| 3450     | The Reservoir                                        | 509   | 3429   |
| 3451     | The Hatchery                                         | 509   | 3429   |
| 3452     | The Comb                                             | 509   | 3429   |
| 3453     | Watchers' Terrace                                    | 509   | 3429   |
| 3454     | Ruins of Ahn'Qiraj                                   | 1     | 1377   |
| 3455     | The North Sea                                        | 530   | 0      |
| 3456     | Naxxramas                                            | 533   | 0      |
| 3457     | Karazhan                                             | 532   | 0      |
| 3459     | City                                                 | 0     | 0      |
| 3460     | Golden Strand                                        | 530   | 3430   |
| 3461     | Sunsail Anchorage                                    | 530   | 3430   |
| 3462     | Fairbreeze Village                                   | 530   | 3430   |
| 3463     | Magisters Gate                                       | 530   | 3430   |
| 3464     | Farstrider Retreat                                   | 530   | 3430   |
| 3465     | North Sanctum                                        | 530   | 3430   |
| 3466     | West Sanctum                                         | 530   | 3430   |
| 3467     | East Sanctum                                         | 530   | 3430   |
| 3468     | Saltheril's Haven                                    | 530   | 3430   |
| 3469     | Thuron's Livery                                      | 530   | 3430   |
| 3470     | Stillwhisper Pond                                    | 530   | 3430   |
| 3471     | The Living Wood                                      | 530   | 3430   |
| 3472     | Azurebreeze Coast                                    | 530   | 3430   |
| 3473     | Lake Elrendar                                        | 530   | 3430   |
| 3474     | The Scorched Grove                                   | 530   | 3430   |
| 3475     | Zeb'Watha                                            | 530   | 3430   |
| 3476     | Tor'Watha                                            | 530   | 3430   |
| 3477     | Azjol-Nerub                                          | 571   | 0      |
| 3478     | Gates of Ahn'Qiraj                                   | 1     | 0      |
| 3479     | The Veiled Sea                                       | 530   | 0      |
| 3480     | Duskwither Grounds                                   | 530   | 3430   |
| 3481     | Duskwither Spire                                     | 530   | 3430   |
| 3482     | The Dead Scar                                        | 530   | 3430   |
| 3483     | Hellfire Peninsula                                   | 530   | 0      |
| 3484     | The Sunspire                                         | 530   | 3430   |
| 3485     | Falthrien Academy                                    | 530   | 3430   |
| 3486     | Ravenholdt Manor                                     | 0     | 36     |
| 3487     | Silvermoon City                                      | 530   | 0      |
| 3488     | Tranquillien                                         | 530   | 3433   |
| 3489     | Suncrown Village                                     | 530   | 3433   |
| 3490     | Goldenmist Village                                   | 530   | 3433   |
| 3491     | Windrunner Village                                   | 530   | 3433   |
| 3492     | Windrunner Spire                                     | 530   | 3433   |
| 3493     | Sanctum of the Sun                                   | 530   | 3433   |
| 3494     | Sanctum of the Moon                                  | 530   | 3433   |
| 3495     | Dawnstar Spire                                       | 530   | 3433   |
| 3496     | Farstrider Enclave                                   | 530   | 3433   |
| 3497     | An'daroth                                            | 530   | 3433   |
| 3498     | An'telas                                             | 530   | 3433   |
| 3499     | An'owyn                                              | 530   | 3433   |
| 3500     | Deatholme                                            | 530   | 3433   |
| 3501     | Bleeding Ziggurat                                    | 530   | 3433   |
| 3502     | Howling Ziggurat                                     | 530   | 3433   |
| 3503     | Shalandis Isle                                       | 530   | 3433   |
| 3504     | Toryl Estate                                         | 530   | 3433   |
| 3505     | Underlight Mines                                     | 530   | 3433   |
| 3506     | Andilien Estate                                      | 530   | 3433   |
| 3507     | Hatchet Hills                                        | 530   | 3433   |
| 3508     | Amani Pass                                           | 530   | 3433   |
| 3509     | Sungraze Peak                                        | 530   | 3433   |
| 3510     | Amani Catacombs                                      | 530   | 3433   |
| 3511     | Tower of the Damned                                  | 530   | 3433   |
| 3512     | Zeb'Sora                                             | 530   | 3433   |
| 3513     | Lake Elrendar                                        | 530   | 3433   |
| 3514     | The Dead Scar                                        | 530   | 3433   |
| 3515     | Elrendar River                                       | 530   | 3433   |
| 3516     | Zeb'Tela                                             | 530   | 3433   |
| 3517     | Zeb'Nowa                                             | 530   | 3433   |
| 3518     | Nagrand                                              | 530   | 0      |
| 3519     | Terokkar Forest                                      | 530   | 0      |
| 3520     | Shadowmoon Valley                                    | 530   | 0      |
| 3521     | Zangarmarsh                                          | 530   | 0      |
| 3522     | Blade's Edge Mountains                               | 530   | 0      |
| 3523     | Netherstorm                                          | 530   | 0      |
| 3524     | Azuremyst Isle                                       | 530   | 0      |
| 3525     | Bloodmyst Isle                                       | 530   | 0      |
| 3526     | Ammen Vale                                           | 530   | 3524   |
| 3527     | Crash Site                                           | 530   | 3524   |
| 3528     | Silverline Lake                                      | 530   | 3524   |
| 3529     | Nestlewood Thicket                                   | 530   | 3524   |
| 3530     | Shadow Ridge                                         | 530   | 3524   |
| 3531     | Skulking Row                                         | 530   | 3430   |
| 3532     | Dawning Lane                                         | 530   | 3430   |
| 3533     | Ruins of Silvermoon                                  | 530   | 3430   |
| 3534     | Feth's Way                                           | 530   | 3430   |
| 3535     | Hellfire Citadel                                     | 540   | 0      |
| 3536     | Thrallmar                                            | 530   | 3483   |
| 3537     | Borean Tundra                                        | 571   | 0      |
| 3538     | Honor Hold                                           | 530   | 3483   |
| 3539     | The Stair of Destiny                                 | 530   | 3483   |
| 3540     | Twisting Nether                                      | 530   | 0      |
| 3541     | Forge Camp: Mageddon                                 | 530   | 3483   |
| 3542     | The Path of Glory                                    | 530   | 3483   |
| 3543     | The Great Fissure                                    | 530   | 3483   |
| 3544     | Plain of Shards                                      | 530   | 3483   |
| 3545     | Hellfire Citadel                                     | 530   | 3483   |
| 3546     | Expedition Armory                                    | 530   | 3483   |
| 3547     | Throne of Kil'jaeden                                 | 530   | 3483   |
| 3548     | Forge Camp: Rage                                     | 530   | 3483   |
| 3549     | Invasion Point: Annihilator                          | 530   | 3483   |
| 3550     | Borune Ruins                                         | 530   | 3483   |
| 3551     | Ruins of Sha'naar                                    | 530   | 3483   |
| 3552     | Temple of Telhamat                                   | 530   | 3483   |
| 3553     | Pools of Aggonar                                     | 530   | 3483   |
| 3554     | Falcon Watch                                         | 530   | 3483   |
| 3555     | Mag'har Post                                         | 530   | 3483   |
| 3556     | Den of Haal'esh                                      | 530   | 3483   |
| 3557     | The Exodar                                           | 530   | 0      |
| 3558     | Elrendar Falls                                       | 530   | 3430   |
| 3559     | Nestlewood Hills                                     | 530   | 3524   |
| 3560     | Ammen Fields                                         | 530   | 3524   |
| 3561     | The Sacred Grove                                     | 530   | 3524   |
| 3562     | Hellfire Ramparts                                    | 543   | 0      |
| 3563     | Hellfire Citadel                                     | 543   | 3562   |
| 3564     | Emberglade                                           | 530   | 3524   |
| 3565     | Cenarion Refuge                                      | 530   | 3521   |
| 3566     | Moonwing Den                                         | 530   | 3524   |
| 3567     | Pod Cluster                                          | 530   | 3524   |
| 3568     | Pod Wreckage                                         | 530   | 3524   |
| 3569     | Tides' Hollow                                        | 530   | 3524   |
| 3570     | Wrathscale Point                                     | 530   | 3524   |
| 3571     | Bristlelimb Village                                  | 530   | 3524   |
| 3572     | Stillpine Hold                                       | 530   | 3524   |
| 3573     | Odesyus' Landing                                     | 530   | 3524   |
| 3574     | Valaar's Berth                                       | 530   | 3524   |
| 3575     | Silting Shore                                        | 530   | 3524   |
| 3576     | Azure Watch                                          | 530   | 3524   |
| 3577     | Geezle's Camp                                        | 530   | 3524   |
| 3578     | Menagerie Wreckage                                   | 530   | 3524   |
| 3579     | Traitor's Cove                                       | 530   | 3524   |
| 3580     | Wildwind Peak                                        | 530   | 3524   |
| 3581     | Wildwind Path                                        | 530   | 3524   |
| 3582     | Zeth'Gor                                             | 530   | 3483   |
| 3583     | Beryl Coast                                          | 530   | 3525   |
| 3584     | Blood Watch                                          | 530   | 3525   |
| 3585     | Bladewood                                            | 530   | 3525   |
| 3586     | The Vector Coil                                      | 530   | 3525   |
| 3587     | The Warp Piston                                      | 530   | 3525   |
| 3588     | The Cryo-Core                                        | 530   | 3525   |
| 3589     | The Crimson Reach                                    | 530   | 3525   |
| 3590     | Wrathscale Lair                                      | 530   | 3525   |
| 3591     | Ruins of Loreth'Aran                                 | 530   | 3525   |
| 3592     | Nazzivian                                            | 530   | 3525   |
| 3593     | Axxarien                                             | 530   | 3525   |
| 3594     | Blacksilt Shore                                      | 530   | 3525   |
| 3595     | The Foul Pool                                        | 530   | 3525   |
| 3596     | The Hidden Reef                                      | 530   | 3525   |
| 3597     | Amberweb Pass                                        | 530   | 3525   |
| 3598     | Wyrmscar Island                                      | 530   | 3525   |
| 3599     | Talon Stand                                          | 530   | 3525   |
| 3600     | Bristlelimb Enclave                                  | 530   | 3525   |
| 3601     | Ragefeather Ridge                                    | 530   | 3525   |
| 3602     | Kessel's Crossing                                    | 530   | 3525   |
| 3603     | Tel'athion's Camp                                    | 530   | 3525   |
| 3604     | The Bloodcursed Reef                                 | 530   | 3525   |
| 3605     | Hyjal Past                                           | 560   | 0      |
| 3606     | Hyjal Summit                                         | 534   | 0      |
| 3607     | Serpentshrine Cavern                                 | 548   | 0      |
| 3608     | Vindicator's Rest                                    | 530   | 3525   |
| 3609     | Unused3                                              | 530   | 3518   |
| 3610     | Burning Blade Ruins                                  | 530   | 3518   |
| 3611     | Clan Watch                                           | 530   | 3518   |
| 3612     | Bloodcurse Isle                                      | 530   | 3525   |
| 3613     | Garadar                                              | 530   | 3518   |
| 3614     | Skysong Lake                                         | 530   | 3518   |
| 3615     | Throne of the Elements                               | 530   | 3518   |
| 3616     | Laughing Skull Ruins                                 | 530   | 3518   |
| 3617     | Warmaul Hill                                         | 530   | 3518   |
| 3618     | Gruul's Lair                                         | 530   | 3518   |
| 3619     | Auren Ridge                                          | 530   | 3518   |
| 3620     | Auren Falls                                          | 530   | 3518   |
| 3621     | Lake Sunspring                                       | 530   | 3518   |
| 3622     | Sunspring Post                                       | 530   | 3518   |
| 3623     | Aeris Landing                                        | 530   | 3518   |
| 3624     | Forge Camp: Fear                                     | 530   | 3518   |
| 3625     | Forge Camp: Hate                                     | 530   | 3518   |
| 3626     | Telaar                                               | 530   | 3518   |
| 3627     | Northwind Cleft                                      | 530   | 3518   |
| 3628     | Halaa                                                | 530   | 3518   |
| 3629     | Southwind Cleft                                      | 530   | 3518   |
| 3630     | Oshu'gun                                             | 530   | 3518   |
| 3631     | Spirit Fields                                        | 530   | 3518   |
| 3632     | Shamanar                                             | 530   | 3518   |
| 3633     | Ancestral Grounds                                    | 530   | 3518   |
| 3634     | Windyreed Village                                    | 530   | 3518   |
| 3635     | Unused2                                              | 530   | 3518   |
| 3636     | Elemental Plateau                                    | 530   | 3518   |
| 3637     | Kil'sorrow Fortress                                  | 530   | 3518   |
| 3638     | The Ring of Trials                                   | 530   | 3518   |
| 3639     | Silvermyst Isle                                      | 530   | 3524   |
| 3640     | Daggerfen Village                                    | 530   | 3521   |
| 3641     | Umbrafen Village                                     | 530   | 3521   |
| 3642     | Feralfen Village                                     | 530   | 3521   |
| 3643     | Bloodscale Enclave                                   | 530   | 3521   |
| 3644     | Telredor                                             | 530   | 3521   |
| 3645     | Zabra'jin                                            | 530   | 3521   |
| 3646     | Quagg Ridge                                          | 530   | 3521   |
| 3647     | The Spawning Glen                                    | 530   | 3521   |
| 3648     | The Dead Mire                                        | 530   | 3521   |
| 3649     | Sporeggar                                            | 530   | 3521   |
| 3650     | Ango'rosh Grounds                                    | 530   | 3521   |
| 3651     | Ango'rosh Stronghold                                 | 530   | 3521   |
| 3652     | Funggor Cavern                                       | 530   | 3521   |
| 3653     | Serpent Lake                                         | 530   | 3521   |
| 3654     | The Drain                                            | 530   | 3521   |
| 3655     | Umbrafen Lake                                        | 530   | 3521   |
| 3656     | Marshlight Lake                                      | 530   | 3521   |
| 3657     | Portal Clearing                                      | 530   | 3521   |
| 3658     | Sporewind Lake                                       | 530   | 3521   |
| 3659     | The Lagoon                                           | 530   | 3521   |
| 3660     | Blades' Run                                          | 530   | 3521   |
| 3661     | Blade Tooth Canyon                                   | 530   | 3521   |
| 3662     | Commons Hall                                         | 530   | 3430   |
| 3663     | Derelict Manor                                       | 530   | 3430   |
| 3664     | Huntress of the Sun                                  | 530   | 3430   |
| 3665     | Falconwing Square                                    | 530   | 3430   |
| 3666     | Halaani Basin                                        | 530   | 3518   |
| 3667     | Hewn Bog                                             | 530   | 3521   |
| 3668     | Boha'mu Ruins                                        | 530   | 3521   |
| 3669     | The Stadium                                          | 530   | 3483   |
| 3670     | The Overlook                                         | 530   | 3483   |
| 3671     | Broken Hill                                          | 530   | 3483   |
| 3672     | Mag'hari Procession                                  | 530   | 3518   |
| 3673     | Nesingwary Safari                                    | 530   | 3518   |
| 3674     | Cenarion Thicket                                     | 530   | 3519   |
| 3675     | Tuurem                                               | 530   | 3519   |
| 3676     | Veil Shienor                                         | 530   | 3519   |
| 3677     | Veil Skith                                           | 530   | 3519   |
| 3678     | Veil Shalas                                          | 530   | 3519   |
| 3679     | Skettis                                              | 530   | 3519   |
| 3680     | Blackwind Valley                                     | 530   | 3519   |
| 3681     | Firewing Point                                       | 530   | 3519   |
| 3682     | Grangol'var Village                                  | 530   | 3519   |
| 3683     | Stonebreaker Hold                                    | 530   | 3519   |
| 3684     | Allerian Stronghold                                  | 530   | 3519   |
| 3685     | Bonechewer Ruins                                     | 530   | 3519   |
| 3686     | Veil Lithic                                          | 530   | 3519   |
| 3687     | Olembas                                              | 530   | 3519   |
| 3688     | Auchindoun                                           | 530   | 3519   |
| 3689     | Veil Reskk                                           | 530   | 3519   |
| 3690     | Blackwind Lake                                       | 530   | 3519   |
| 3691     | Lake Ere'Noru                                        | 530   | 3519   |
| 3692     | Lake Jorune                                          | 530   | 3519   |
| 3693     | Skethyl Mountains                                    | 530   | 3519   |
| 3694     | Misty Ridge                                          | 530   | 3519   |
| 3695     | The Broken Hills                                     | 530   | 3519   |
| 3696     | The Barrier Hills                                    | 530   | 3519   |
| 3697     | The Bone Wastes                                      | 530   | 3519   |
| 3698     | Nagrand Arena                                        | 559   | 0      |
| 3699     | Laughing Skull Courtyard                             | 530   | 3518   |
| 3700     | The Ring of Blood                                    | 530   | 3518   |
| 3701     | Arena Floor                                          | 530   | 3518   |
| 3702     | Blade's Edge Arena                                   | 562   | 0      |
| 3703     | Shattrath City                                       | 530   | 0      |
| 3704     | The Shepherd's Gate                                  | 530   | 3487   |
| 3705     | Telaari Basin                                        | 530   | 3518   |
| 3706     | The Dark Portal                                      | 269   | 2366   |
| 3707     | Alliance Base                                        | 534   | 3606   |
| 3708     | Horde Encampment                                     | 534   | 3606   |
| 3709     | Night Elf Village                                    | 534   | 3606   |
| 3710     | Nordrassil                                           | 534   | 3606   |
| 3711     | Sholazar Basin                                       | 571   | 0      |
| 3712     | Area 52                                              | 530   | 3523   |
| 3713     | The Blood Furnace                                    | 542   | 0      |
| 3714     | The Shattered Halls                                  | 540   | 0      |
| 3715     | The Steamvault                                       | 545   | 0      |
| 3716     | The Underbog                                         | 546   | 0      |
| 3717     | The Slave Pens                                       | 547   | 0      |
| 3718     | Swamprat Post                                        | 530   | 3521   |
| 3719     | Bleeding Hollow Ruins                                | 530   | 3519   |
| 3720     | Twin Spire Ruins                                     | 530   | 3521   |
| 3721     | The Crumbling Waste                                  | 530   | 3523   |
| 3722     | Manaforge Ara                                        | 530   | 3523   |
| 3723     | Arklon Ruins                                         | 530   | 3523   |
| 3724     | Cosmowrench                                          | 530   | 3523   |
| 3725     | Ruins of Enkaat                                      | 530   | 3523   |
| 3726     | Manaforge B'naar                                     | 530   | 3523   |
| 3727     | The Scrap Field                                      | 530   | 3523   |
| 3728     | The Vortex Fields                                    | 530   | 3523   |
| 3729     | The Heap                                             | 530   | 3523   |
| 3730     | Manaforge Coruu                                      | 530   | 3523   |
| 3731     | The Tempest Rift                                     | 530   | 3523   |
| 3732     | Kirin'Var Village                                    | 530   | 3523   |
| 3733     | The Violet Tower                                     | 530   | 3523   |
| 3734     | Manaforge Duro                                       | 530   | 3523   |
| 3735     | Voidwind Plateau                                     | 530   | 3523   |
| 3736     | Manaforge Ultris                                     | 530   | 3523   |
| 3737     | Celestial Ridge                                      | 530   | 3523   |
| 3738     | The Stormspire                                       | 530   | 3523   |
| 3739     | Forge Base: Oblivion                                 | 530   | 3523   |
| 3740     | Forge Base: Gehenna                                  | 530   | 3523   |
| 3741     | Ruins of Farahlon                                    | 530   | 3523   |
| 3742     | Socrethar's Seat                                     | 530   | 3523   |
| 3743     | Legion Hold                                          | 530   | 3520   |
| 3744     | Shadowmoon Village                                   | 530   | 3520   |
| 3745     | Wildhammer Stronghold                                | 530   | 3520   |
| 3746     | The Hand of Gul'dan                                  | 530   | 3520   |
| 3747     | The Fel Pits                                         | 530   | 3520   |
| 3748     | The Deathforge                                       | 530   | 3520   |
| 3749     | Coilskar Cistern                                     | 530   | 3520   |
| 3750     | Coilskar Point                                       | 530   | 3520   |
| 3751     | Sunfire Point                                        | 530   | 3520   |
| 3752     | Illidari Point                                       | 530   | 3520   |
| 3753     | Ruins of Baa'ri                                      | 530   | 3520   |
| 3754     | Altar of Sha'tar                                     | 530   | 3520   |
| 3755     | The Stair of Doom                                    | 530   | 3520   |
| 3756     | Ruins of Karabor                                     | 530   | 3520   |
| 3757     | Ata'mal Terrace                                      | 530   | 3520   |
| 3758     | Netherwing Fields                                    | 530   | 3520   |
| 3759     | Netherwing Ledge                                     | 530   | 3520   |
| 3760     | The Barrier Hills                                    | 530   | 3518   |
| 3761     | The High Path                                        | 530   | 3518   |
| 3762     | Windyreed Pass                                       | 530   | 3518   |
| 3763     | Zangar Ridge                                         | 530   | 3518   |
| 3764     | The Twilight Ridge                                   | 530   | 3518   |
| 3765     | Razorthorn Trail                                     | 530   | 3483   |
| 3766     | Orebor Harborage                                     | 530   | 3521   |
| 3767     | Blades' Run                                          | 530   | 3522   |
| 3768     | Jagged Ridge                                         | 530   | 3522   |
| 3769     | Thunderlord Stronghold                               | 530   | 3522   |
| 3770     | Blade Tooth Canyon                                   | 530   | 3522   |
| 3771     | The Living Grove                                     | 530   | 3522   |
| 3772     | Sylvanaar                                            | 530   | 3522   |
| 3773     | Bladespire Hold                                      | 530   | 3522   |
| 3774     | Gruul's Lair                                         | 530   | 3522   |
| 3775     | Circle of Blood                                      | 530   | 3522   |
| 3776     | Bloodmaul Outpost                                    | 530   | 3522   |
| 3777     | Bloodmaul Camp                                       | 530   | 3522   |
| 3778     | Draenethyst Mine                                     | 530   | 3522   |
| 3779     | Trogma's Claim                                       | 530   | 3522   |
| 3780     | Blackwing Coven                                      | 530   | 3522   |
| 3781     | Grishnath                                            | 530   | 3522   |
| 3782     | Veil Lashh                                           | 530   | 3522   |
| 3783     | Veil Vekh                                            | 530   | 3522   |
| 3784     | Forge Camp: Terror                                   | 530   | 3522   |
| 3785     | Forge Camp: Wrath                                    | 530   | 3522   |
| 3786     | Ogri'la                                              | 530   | 3522   |
| 3787     | Forge Camp: Anger                                    | 530   | 3522   |
| 3788     | The Low Path                                         | 530   | 3518   |
| 3789     | Shadow Labyrinth                                     | 555   | 0      |
| 3790     | Auchenai Crypts                                      | 558   | 0      |
| 3791     | Sethekk Halls                                        | 556   | 0      |
| 3792     | Mana-Tombs                                           | 557   | 0      |
| 3793     | Felspark Ravine                                      | 530   | 3483   |
| 3794     | Valley of Bones                                      | 530   | 3483   |
| 3795     | Sha'naari Wastes                                     | 530   | 3483   |
| 3796     | The Warp Fields                                      | 530   | 3483   |
| 3797     | Fallen Sky Ridge                                     | 530   | 3483   |
| 3798     | Haal'eshi Gorge                                      | 530   | 3483   |
| 3799     | Stonewall Canyon                                     | 530   | 3483   |
| 3800     | Thornfang Hill                                       | 530   | 3483   |
| 3801     | Mag'har Grounds                                      | 530   | 3483   |
| 3802     | Void Ridge                                           | 530   | 3483   |
| 3803     | The Abyssal Shelf                                    | 530   | 3483   |
| 3804     | The Legion Front                                     | 530   | 3483   |
| 3805     | Zul'Aman                                             | 568   | 0      |
| 3806     | Supply Caravan                                       | 530   | 3483   |
| 3807     | Reaver's Fall                                        | 530   | 3483   |
| 3808     | Cenarion Post                                        | 530   | 3483   |
| 3809     | Southern Rampart                                     | 530   | 3483   |
| 3810     | Northern Rampart                                     | 530   | 3483   |
| 3811     | Gor'gaz Outpost                                      | 530   | 3483   |
| 3812     | Spinebreaker Post                                    | 530   | 3483   |
| 3813     | The Path of Anguish                                  | 530   | 3483   |
| 3814     | East Supply Caravan                                  | 530   | 3483   |
| 3815     | Expedition Point                                     | 530   | 3483   |
| 3816     | Zeppelin Crash                                       | 530   | 3483   |
| 3817     | Testing                                              | 13    | 0      |
| 3818     | Bloodscale Grounds                                   | 530   | 3521   |
| 3819     | Darkcrest Enclave                                    | 530   | 3521   |
| 3820     | Eye of the Storm                                     | 566   | 0      |
| 3821     | Warden's Cage                                        | 530   | 3520   |
| 3822     | Eclipse Point                                        | 530   | 3520   |
| 3823     | Isle of Tribulations                                 | 530   | 3433   |
| 3824     | Bloodmaul Ravine                                     | 530   | 3522   |
| 3825     | Dragons' End                                         | 530   | 3522   |
| 3826     | Daggermaw Canyon                                     | 530   | 3522   |
| 3827     | Vekhaar Stand                                        | 530   | 3522   |
| 3828     | Ruuan Weald                                          | 530   | 3522   |
| 3829     | Veil Ruuan                                           | 530   | 3522   |
| 3830     | Raven's Wood                                         | 530   | 3522   |
| 3831     | Death's Door                                         | 530   | 3522   |
| 3832     | Vortex Pinnacle                                      | 530   | 3522   |
| 3833     | Razor Ridge                                          | 530   | 3522   |
| 3834     | Ridge of Madness                                     | 530   | 3522   |
| 3835     | Dustquill Ravine                                     | 530   | 3483   |
| 3836     | Magtheridon's Lair                                   | 544   | 0      |
| 3837     | Sunfury Hold                                         | 530   | 3523   |
| 3838     | Spinebreaker Mountains                               | 530   | 3483   |
| 3839     | Abandoned Armory                                     | 530   | 3518   |
| 3840     | The Black Temple                                     | 530   | 3520   |
| 3841     | Darkcrest Shore                                      | 530   | 3521   |
| 3842     | Tempest Keep                                         | 530   | 3523   |
| 3844     | Mok'Nathal Village                                   | 530   | 3522   |
| 3845     | Tempest Keep                                         | 550   | 0      |
| 3846     | The Arcatraz                                         | 530   | 3525   |
| 3847     | The Botanica                                         | 553   | 0      |
| 3848     | The Arcatraz                                         | 552   | 0      |
| 3849     | The Mechanar                                         | 554   | 0      |
| 3850     | Netherstone                                          | 530   | 3523   |
| 3851     | Midrealm Post                                        | 530   | 3523   |
| 3852     | Tuluman's Landing                                    | 530   | 3523   |
| 3854     | Protectorate Watch Post                              | 530   | 3523   |
| 3855     | Circle of Blood Arena                                | 530   | 3522   |
| 3856     | Elrendar Crossing                                    | 530   | 3433   |
| 3857     | Ammen Ford                                           | 530   | 3524   |
| 3858     | Razorthorn Shelf                                     | 530   | 3519   |
| 3859     | Silmyr Lake                                          | 530   | 3519   |
| 3860     | Raastok Glade                                        | 530   | 3519   |
| 3861     | Thalassian Pass                                      | 530   | 3433   |
| 3862     | Churning Gulch                                       | 530   | 3522   |
| 3863     | Broken Wilds                                         | 530   | 3522   |
| 3864     | Bash'ir Landing                                      | 530   | 3522   |
| 3865     | Crystal Spine                                        | 530   | 3522   |
| 3866     | Skald                                                | 530   | 3522   |
| 3867     | Bladed Gulch                                         | 530   | 3522   |
| 3868     | Gyro-Plank Bridge                                    | 530   | 3523   |
| 3869     | Mage Tower                                           | 566   | 3820   |
| 3870     | Blood Elf Tower                                      | 566   | 3820   |
| 3871     | Draenei Ruins                                        | 566   | 3820   |
| 3872     | Fel Reaver Ruins                                     | 566   | 3820   |
| 3873     | The Proving Grounds                                  | 530   | 3523   |
| 3874     | Eco-Dome Farfield                                    | 530   | 3523   |
| 3875     | Eco-Dome Skyperch                                    | 530   | 3523   |
| 3876     | Eco-Dome Sutheron                                    | 530   | 3523   |
| 3877     | Eco-Dome Midrealm                                    | 530   | 3523   |
| 3878     | Ethereum Staging Grounds                             | 530   | 3523   |
| 3879     | Chapel Yard                                          | 530   | 3523   |
| 3880     | Access Shaft Zeon                                    | 530   | 3523   |
| 3881     | Trelleum Mine                                        | 530   | 3523   |
| 3882     | Invasion Point: Destroyer                            | 530   | 3523   |
| 3883     | Camp of Boom                                         | 530   | 3523   |
| 3884     | Spinebreaker Pass                                    | 530   | 3483   |
| 3885     | Netherweb Ridge                                      | 530   | 3519   |
| 3886     | Derelict Caravan                                     | 530   | 3519   |
| 3887     | Refugee Caravan                                      | 530   | 3519   |
| 3888     | Shadow Tomb                                          | 530   | 3519   |
| 3889     | Veil Rhaze                                           | 530   | 3519   |
| 3890     | Tomb of Lights                                       | 530   | 3519   |
| 3891     | Carrion Hill                                         | 530   | 3519   |
| 3892     | Writhing Mound                                       | 530   | 3519   |
| 3893     | Ring of Observance                                   | 530   | 3519   |
| 3894     | Auchenai Grounds                                     | 530   | 3519   |
| 3895     | Cenarion Watchpost                                   | 530   | 3521   |
| 3896     | Aldor Rise                                           | 530   | 3703   |
| 3897     | Terrace of Light                                     | 530   | 3703   |
| 3898     | Scryer's Tier                                        | 530   | 3703   |
| 3899     | Lower City                                           | 530   | 3703   |
| 3900     | Invasion Point: Overlord                             | 530   | 3523   |
| 3901     | Allerian Post                                        | 530   | 3519   |
| 3902     | Stonebreaker Camp                                    | 530   | 3519   |
| 3903     | Boulder'mok                                          | 530   | 3522   |
| 3904     | Cursed Hollow                                        | 530   | 3522   |
| 3905     | Coilfang Reservoir                                   | 530   | 3521   |
| 3906     | The Bloodwash                                        | 530   | 3525   |
| 3907     | Veridian Point                                       | 530   | 3525   |
| 3908     | Middenvale                                           | 530   | 3525   |
| 3909     | The Lost Fold                                        | 530   | 3525   |
| 3910     | Mystwood                                             | 530   | 3525   |
| 3911     | Tranquil Shore                                       | 530   | 3430   |
| 3912     | Goldenbough Pass                                     | 530   | 3430   |
| 3913     | Runestone Falithas                                   | 530   | 3430   |
| 3914     | Runestone Shan'dor                                   | 530   | 3430   |
| 3915     | Fairbridge Strand                                    | 530   | 3524   |
| 3916     | Moongraze Woods                                      | 530   | 3524   |
| 3917     | Auchindoun                                           | 530   | 0      |
| 3918     | Toshley's Station                                    | 530   | 3522   |
| 3919     | Singing Ridge                                        | 530   | 3522   |
| 3920     | Shatter Point                                        | 530   | 3483   |
| 3921     | Arklonis Ridge                                       | 530   | 3523   |
| 3922     | Bladespire Outpost                                   | 530   | 3522   |
| 3923     | Gruul's Lair                                         | 565   | 0      |
| 3924     | Northmaul Tower                                      | 530   | 3522   |
| 3925     | Southmaul Tower                                      | 530   | 3522   |
| 3926     | Shattered Plains                                     | 530   | 3520   |
| 3927     | Oronok's Farm                                        | 530   | 3520   |
| 3928     | The Altar of Damnation                               | 530   | 3520   |
| 3929     | The Path of Conquest                                 | 530   | 3520   |
| 3930     | Eclipsion Fields                                     | 530   | 3520   |
| 3931     | Bladespire Grounds                                   | 530   | 3522   |
| 3932     | Sketh'lon Base Camp                                  | 530   | 3520   |
| 3933     | Sketh'lon Wreckage                                   | 530   | 3520   |
| 3934     | Town Square                                          | 530   | 3523   |
| 3935     | Wizard Row                                           | 530   | 3523   |
| 3936     | Deathforge Tower                                     | 530   | 3520   |
| 3937     | Slag Watch                                           | 530   | 3520   |
| 3938     | Sanctum of the Stars                                 | 530   | 3520   |
| 3939     | Dragonmaw Fortress                                   | 530   | 3520   |
| 3940     | The Fetid Pool                                       | 530   | 3520   |
| 3941     | Test                                                 | 530   | 3520   |
| 3942     | Razaan's Landing                                     | 530   | 3522   |
| 3943     | Invasion Point: Cataclysm                            | 530   | 3520   |
| 3944     | The Altar of Shadows                                 | 530   | 3520   |
| 3945     | Netherwing Pass                                      | 530   | 3520   |
| 3946     | Wayne's Refuge                                       | 530   | 3519   |
| 3947     | The Scalding Pools                                   | 530   | 3520   |
| 3948     | Brian and Pat Test                                   | 451   | 0      |
| 3949     | Magma Fields                                         | 530   | 3520   |
| 3950     | Crimson Watch                                        | 530   | 3520   |
| 3951     | Evergrove                                            | 530   | 3522   |
| 3952     | Wyrmskull Bridge                                     | 530   | 3522   |
| 3953     | Scalewing Shelf                                      | 530   | 3522   |
| 3954     | Wyrmskull Tunnel                                     | 530   | 3522   |
| 3955     | Hellfire Basin                                       | 530   | 3483   |
| 3956     | The Shadow Stair                                     | 530   | 3519   |
| 3957     | Sha'tari Outpost                                     | 530   | 3519   |
| 3958     | Sha'tari Base Camp                                   | 530   | 3519   |
| 3959     | Black Temple                                         | 564   | 0      |
| 3960     | Soulgrinder's Barrow                                 | 530   | 3522   |
| 3961     | Sorrow Wing Point                                    | 530   | 3519   |
| 3962     | Vim'gol's Circle                                     | 530   | 3522   |
| 3963     | Dragonspine Ridge                                    | 530   | 3522   |
| 3964     | Skyguard Outpost                                     | 530   | 3522   |
| 3965     | Netherwing Mines                                     | 530   | 3520   |
| 3966     | Dragonmaw Base Camp                                  | 530   | 3520   |
| 3967     | Dragonmaw Skyway                                     | 530   | 3520   |
| 3968     | Ruins of Lordaeron                                   | 572   | 0      |
| 3969     | Rivendark's Perch                                    | 530   | 3522   |
| 3970     | Obsidia's Perch                                      | 530   | 3522   |
| 3971     | Insidion's Perch                                     | 530   | 3522   |
| 3972     | Furywing's Perch                                     | 530   | 3522   |
| 3973     | Blackwind Landing                                    | 530   | 3519   |
| 3974     | Veil Harr'ik                                         | 530   | 3519   |
| 3975     | Terokk's Rest                                        | 530   | 3519   |
| 3976     | Veil Ala'rak                                         | 530   | 3519   |
| 3977     | Upper Veil Shil'ak                                   | 530   | 3519   |
| 3978     | Lower Veil Shil'ak                                   | 530   | 3519   |
| 3979     | The Frozen Sea                                       | 571   | 0      |
| 3980     | Daggercap Bay                                        | 571   | 495    |
| 3981     | Valgarde                                             | 571   | 495    |
| 3982     | Wyrmskull Village                                    | 571   | 495    |
| 3983     | Utgarde Keep                                         | 571   | 495    |
| 3984     | Nifflevar                                            | 571   | 495    |
| 3985     | Falls of Ymiron                                      | 571   | 495    |
| 3986     | Echo Reach                                           | 571   | 495    |
| 3987     | The Isle of Spears                                   | 571   | 495    |
| 3988     | Kamagua                                              | 571   | 495    |
| 3989     | Garvan's Reef                                        | 571   | 495    |
| 3990     | Scalawag Point                                       | 571   | 495    |
| 3991     | New Agamand                                          | 571   | 495    |
| 3992     | The Ancient Lift                                     | 571   | 495    |
| 3993     | Westguard Turret                                     | 571   | 495    |
| 3994     | Halgrind                                             | 571   | 495    |
| 3995     | The Laughing Stand                                   | 571   | 495    |
| 3996     | Baelgun's Excavation Site                            | 571   | 495    |
| 3997     | Explorers' League Outpost                            | 571   | 495    |
| 3998     | Westguard Keep                                       | 571   | 495    |
| 3999     | Steel Gate                                           | 571   | 495    |
| 4000     | Vengeance Landing                                    | 571   | 495    |
| 4001     | Baleheim                                             | 571   | 495    |
| 4002     | Skorn                                                | 571   | 495    |
| 4003     | Fort Wildervar                                       | 571   | 495    |
| 4004     | Vileprey Village                                     | 571   | 495    |
| 4005     | Ivald's Ruin                                         | 571   | 495    |
| 4006     | Gjalerbron                                           | 571   | 495    |
| 4007     | Tomb of the Lost Kings                               | 571   | 495    |
| 4008     | Shartuul's Transporter                               | 530   | 3522   |
| 4009     | Illidari Training Grounds                            | 564   | 3959   |
| 4010     | Mudsprocket                                          | 1     | 15     |
| 4018     | Camp Winterhoof                                      | 571   | 495    |
| 4019     | Development Land                                     | 451   | 0      |
| 4020     | Mightstone Quarry                                    | 571   | 3537   |
| 4021     | Bloodspore Plains                                    | 571   | 3537   |
| 4022     | Gammoth                                              | 571   | 3537   |
| 4023     | Amber Ledge                                          | 571   | 3537   |
| 4024     | Coldarra                                             | 571   | 3537   |
| 4025     | The Westrift                                         | 571   | 3537   |
| 4026     | The Transitus Stair                                  | 571   | 3537   |
| 4027     | Coast of Echoes                                      | 571   | 3537   |
| 4028     | Riplash Strand                                       | 571   | 3537   |
| 4029     | Riplash Ruins                                        | 571   | 3537   |
| 4030     | Coast of Idols                                       | 571   | 3537   |
| 4031     | Pal'ea                                               | 571   | 3537   |
| 4032     | Valiance Keep                                        | 571   | 3537   |
| 4033     | Winterfin Village                                    | 571   | 3537   |
| 4034     | The Borean Wall                                      | 571   | 3537   |
| 4035     | The Geyser Fields                                    | 571   | 3537   |
| 4036     | Fizzcrank Pumping Station                            | 571   | 3537   |
| 4037     | Taunka'le Village                                    | 571   | 3537   |
| 4038     | Magnamoth Caverns                                    | 571   | 3537   |
| 4039     | Coldrock Quarry                                      | 571   | 3537   |
| 4040     | Njord's Breath Bay                                   | 571   | 3537   |
| 4041     | Kaskala                                              | 571   | 3537   |
| 4042     | Transborea                                           | 571   | 3537   |
| 4043     | The Flood Plains                                     | 571   | 3537   |
| 4046     | Direhorn Post                                        | 1     | 15     |
| 4047     | Nat's Landing                                        | 1     | 15     |
| 4048     | Ember Clutch                                         | 571   | 495    |
| 4049     | Tabetha's Farm                                       | 1     | 15     |
| 4050     | Derelict Strand                                      | 571   | 495    |
| 4051     | The Frozen Glade                                     | 571   | 495    |
| 4052     | The Vibrant Glade                                    | 571   | 495    |
| 4053     | The Twisted Glade                                    | 571   | 495    |
| 4054     | Rivenwood                                            | 571   | 495    |
| 4055     | Caldemere Lake                                       | 571   | 495    |
| 4056     | Utgarde Catacombs                                    | 571   | 495    |
| 4057     | Shield Hill                                          | 571   | 495    |
| 4058     | Lake Cauldros                                        | 571   | 495    |
| 4059     | Cauldros Isle                                        | 571   | 495    |
| 4060     | Bleeding Vale                                        | 571   | 495    |
| 4061     | Giants' Run                                          | 571   | 495    |
| 4062     | Apothecary Camp                                      | 571   | 495    |
| 4063     | Ember Spear Tower                                    | 571   | 495    |
| 4064     | Shattered Straits                                    | 571   | 495    |
| 4065     | Gjalerhorn                                           | 571   | 495    |
| 4066     | Frostblade Peak                                      | 571   | 495    |
| 4067     | Plaguewood Tower                                     | 0     | 139    |
| 4068     | West Spear Tower                                     | 571   | 495    |
| 4069     | North Spear Tower                                    | 571   | 495    |
| 4070     | Chillmere Coast                                      | 571   | 495    |
| 4071     | Whisper Gulch                                        | 571   | 495    |
| 4072     | Sub zone                                             | 451   | 151    |
| 4073     | Winter's Terrace                                     | 571   | 495    |
| 4074     | The Waking Halls                                     | 571   | 495    |
| 4075     | Sunwell Plateau                                      | 580   | 0      |
| 4076     | Reuse Me 7                                           | 598   | 0      |
| 4077     | Sorlof's Strand                                      | 571   | 495    |
| 4078     | Razorthorn Rise                                      | 530   | 3519   |
| 4079     | Frostblade Pass                                      | 571   | 495    |
| 4080     | Isle of Quel'Danas                                   | 530   | 0      |
| 4081     | The Dawnchaser                                       | 530   | 4080   |
| 4082     | The Sin'loren                                        | 530   | 4080   |
| 4083     | Silvermoon's Pride                                   | 530   | 4080   |
| 4084     | The Bloodoath                                        | 530   | 4080   |
| 4085     | Shattered Sun Staging Area                           | 530   | 4080   |
| 4086     | Sun's Reach Sanctum                                  | 530   | 4080   |
| 4087     | Sun's Reach Harbor                                   | 530   | 4080   |
| 4088     | Sun's Reach Armory                                   | 530   | 4080   |
| 4089     | Dawnstar Village                                     | 530   | 4080   |
| 4090     | The Dawning Square                                   | 530   | 4080   |
| 4091     | Greengill Coast                                      | 530   | 4080   |
| 4092     | The Dead Scar                                        | 530   | 4080   |
| 4093     | The Sun Forge                                        | 530   | 4080   |
| 4094     | Sunwell Plateau                                      | 530   | 4080   |
| 4095     | Magisters' Terrace                                   | 530   | 4080   |
| 4096     | Clayt?Ân's WoWEdit Land                              | 451   | 4019   |
| 4097     | Winterfin Caverns                                    | 571   | 3537   |
| 4098     | Glimmer Bay                                          | 571   | 3537   |
| 4099     | Winterfin Retreat                                    | 571   | 3537   |
| 4100     | The Culling of Stratholme                            | 595   | 0      |
| 4101     | Sands of Nasam                                       | 571   | 3537   |
| 4102     | Krom's Landing                                       | 571   | 3537   |
| 4103     | Nasam's Talon                                        | 571   | 3537   |
| 4104     | Echo Cove                                            | 571   | 3537   |
| 4105     | Beryl Point                                          | 571   | 3537   |
| 4106     | Garrosh's Landing                                    | 571   | 3537   |
| 4107     | Warsong Jetty                                        | 571   | 3537   |
| 4108     | Fizzcrank Airstrip                                   | 571   | 3537   |
| 4109     | Lake Kum'uya                                         | 571   | 3537   |
| 4110     | Farshire Fields                                      | 571   | 3537   |
| 4111     | Farshire                                             | 571   | 3537   |
| 4112     | Farshire Lighthouse                                  | 571   | 3537   |
| 4113     | Unu'pe                                               | 571   | 3537   |
| 4114     | Death's Stand                                        | 571   | 3537   |
| 4115     | The Abandoned Reach                                  | 571   | 3537   |
| 4116     | Scalding Pools                                       | 571   | 3537   |
| 4117     | Steam Springs                                        | 571   | 3537   |
| 4118     | Talramas                                             | 571   | 3537   |
| 4119     | Festering Pools                                      | 571   | 3537   |
| 4120     | The Nexus                                            | 571   | 3537   |
| 4121     | Transitus Shield                                     | 571   | 3537   |
| 4122     | Bor'gorok Outpost                                    | 571   | 3537   |
| 4123     | Magmoth                                              | 571   | 3537   |
| 4124     | The Dens of Dying                                    | 571   | 3537   |
| 4125     | Temple City of En'kilah                              | 571   | 3537   |
| 4126     | The Wailing Ziggurat                                 | 571   | 3537   |
| 4127     | Steeljaw's Caravan                                   | 571   | 3537   |
| 4128     | Naxxanar                                             | 571   | 3537   |
| 4129     | Warsong Hold                                         | 571   | 3537   |
| 4130     | Plains of Nasam                                      | 571   | 3537   |
| 4131     | Magisters' Terrace                                   | 585   | 0      |
| 4132     | Ruins of Eldra'nath                                  | 571   | 3537   |
| 4133     | Charred Rise                                         | 571   | 3537   |
| 4134     | Blistering Pool                                      | 571   | 3537   |
| 4135     | Spire of Blood                                       | 571   | 3537   |
| 4136     | Spire of Decay                                       | 571   | 3537   |
| 4137     | Spire of Pain                                        | 571   | 3537   |
| 4138     | Frozen Reach                                         | 571   | 3537   |
| 4139     | Parhelion Plaza                                      | 580   | 4075   |
| 4140     | The Dead Scar                                        | 580   | 4075   |
| 4141     | Torp's Farm                                          | 571   | 3537   |
| 4142     | Warsong Granary                                      | 571   | 3537   |
| 4143     | Warsong Slaughterhouse                               | 571   | 3537   |
| 4144     | Warsong Farms Outpost                                | 571   | 3537   |
| 4145     | West Point Station                                   | 571   | 3537   |
| 4146     | North Point Station                                  | 571   | 3537   |
| 4147     | Mid Point Station                                    | 571   | 3537   |
| 4148     | South Point Station                                  | 571   | 3537   |
| 4149     | D.E.H.T.A. Encampment                                | 571   | 3537   |
| 4150     | Kaw's Roost                                          | 571   | 3537   |
| 4151     | Westwind Refugee Camp                                | 571   | 65     |
| 4152     | Moa'ki Harbor                                        | 571   | 65     |
| 4153     | Indu'le Village                                      | 571   | 65     |
| 4154     | Snowfall Glade                                       | 571   | 65     |
| 4155     | The Half Shell                                       | 571   | 65     |
| 4156     | Surge Needle                                         | 571   | 65     |
| 4157     | Moonrest Gardens                                     | 571   | 65     |
| 4158     | Stars' Rest                                          | 571   | 65     |
| 4159     | Westfall Brigade Encampment                          | 571   | 394    |
| 4160     | Lothalor Woodlands                                   | 571   | 65     |
| 4161     | Wyrmrest Temple                                      | 571   | 65     |
| 4162     | Icemist Falls                                        | 571   | 65     |
| 4163     | Icemist Village                                      | 571   | 65     |
| 4164     | The Pit of Narjun                                    | 571   | 65     |
| 4165     | Agmar's Hammer                                       | 571   | 65     |
| 4166     | Lake Indu'le                                         | 571   | 65     |
| 4167     | Obsidian Dragonshrine                                | 571   | 65     |
| 4168     | Ruby Dragonshrine                                    | 571   | 65     |
| 4169     | Fordragon Hold                                       | 571   | 65     |
| 4170     | Kor'kron Vanguard                                    | 571   | 65     |
| 4171     | The Court of Skulls                                  | 571   | 65     |
| 4172     | Angrathar the Wrathgate                              | 571   | 65     |
| 4173     | Galakrond's Rest                                     | 571   | 65     |
| 4174     | The Wicked Coil                                      | 571   | 65     |
| 4175     | Bronze Dragonshrine                                  | 571   | 65     |
| 4176     | The Mirror of Dawn                                   | 571   | 65     |
| 4177     | Wintergarde Keep                                     | 571   | 65     |
| 4178     | Wintergarde Mine                                     | 571   | 65     |
| 4179     | Emerald Dragonshrine                                 | 571   | 65     |
| 4180     | New Hearthglen                                       | 571   | 65     |
| 4181     | Crusader's Landing                                   | 571   | 65     |
| 4182     | Sinner's Folly                                       | 571   | 65     |
| 4183     | Azure Dragonshrine                                   | 571   | 65     |
| 4184     | Path of the Titans                                   | 571   | 65     |
| 4185     | The Forgotten Shore                                  | 571   | 65     |
| 4186     | Venomspite                                           | 571   | 65     |
| 4187     | The Crystal Vice                                     | 571   | 65     |
| 4188     | The Carrion Fields                                   | 571   | 65     |
| 4189     | Onslaught Base Camp                                  | 571   | 65     |
| 4190     | Thorson's Post                                       | 571   | 65     |
| 4191     | Light's Trust                                        | 571   | 65     |
| 4192     | Frostmourne Cavern                                   | 571   | 65     |
| 4193     | Scarlet Point                                        | 571   | 65     |
| 4194     | Jintha'kalar                                         | 571   | 65     |
| 4195     | Ice Heart Cavern                                     | 571   | 65     |
| 4196     | Drak'Tharon Keep                                     | 600   | 0      |
| 4197     | Wintergrasp                                          | 571   | 0      |
| 4198     | Kili'ua's Atoll                                      | 571   | 65     |
| 4199     | Silverbrook                                          | 571   | 394    |
| 4200     | Vordrassil's Heart                                   | 571   | 394    |
| 4201     | Vordrassil's Tears                                   | 571   | 0      |
| 4202     | Vordrassil's Tears                                   | 571   | 394    |
| 4203     | Vordrassil's Limb                                    | 571   | 394    |
| 4204     | Amberpine Lodge                                      | 571   | 394    |
| 4205     | Solstice Village                                     | 571   | 394    |
| 4206     | Conquest Hold                                        | 571   | 394    |
| 4207     | Voldrune                                             | 571   | 394    |
| 4208     | Granite Springs                                      | 571   | 394    |
| 4209     | Zeb'Halak                                            | 571   | 394    |
| 4210     | Drak'Tharon Keep                                     | 571   | 394    |
| 4211     | Camp Oneqwah                                         | 571   | 394    |
| 4212     | Eastwind Shore                                       | 571   | 394    |
| 4213     | The Broken Bluffs                                    | 571   | 394    |
| 4214     | Boulder Hills                                        | 571   | 394    |
| 4215     | Rage Fang Shrine                                     | 571   | 394    |
| 4216     | Drakil'jin Ruins                                     | 571   | 394    |
| 4217     | Blackriver Logging Camp                              | 571   | 394    |
| 4218     | Heart's Blood Shrine                                 | 571   | 394    |
| 4219     | Hollowstone Mine                                     | 571   | 394    |
| 4220     | Dun Argol                                            | 571   | 394    |
| 4221     | Thor Modan                                           | 571   | 394    |
| 4222     | Blue Sky Logging Grounds                             | 571   | 394    |
| 4223     | Maw of Neltharion                                    | 571   | 65     |
| 4224     | The Briny Pinnacle                                   | 571   | 65     |
| 4225     | Glittering Strand                                    | 571   | 65     |
| 4226     | Iskaal                                               | 571   | 495    |
| 4227     | Dragon's Fall                                        | 571   | 65     |
| 4228     | The Oculus                                           | 578   | 0      |
| 4229     | Prospector's Point                                   | 571   | 394    |
| 4230     | Coldwind Heights                                     | 571   | 65     |
| 4231     | Redwood Trading Post                                 | 571   | 394    |
| 4232     | Vengeance Pass                                       | 571   | 65     |
| 4233     | Dawn's Reach                                         | 571   | 65     |
| 4234     | Naxxramas                                            | 571   | 65     |
| 4235     | Heartwood Trading Post                               | 571   | 394    |
| 4236     | Evergreen Trading Post                               | 571   | 394    |
| 4237     | Spruce Point Post                                    | 571   | 394    |
| 4238     | White Pine Trading Post                              | 571   | 394    |
| 4239     | Aspen Grove Post                                     | 571   | 394    |
| 4240     | Forest's Edge Post                                   | 571   | 394    |
| 4241     | Eldritch Heights                                     | 571   | 65     |
| 4242     | Venture Bay                                          | 571   | 394    |
| 4243     | Wintergarde Crypt                                    | 571   | 65     |
| 4244     | Bloodmoon Isle                                       | 571   | 394    |
| 4245     | Shadowfang Tower                                     | 571   | 394    |
| 4246     | Wintergarde Mausoleum                                | 571   | 65     |
| 4247     | Duskhowl Den                                         | 571   | 394    |
| 4248     | The Conquest Pit                                     | 571   | 394    |
| 4249     | The Path of Iron                                     | 571   | 394    |
| 4250     | Ruins of Tethys                                      | 571   | 394    |
| 4251     | Silverbrook Hills                                    | 571   | 394    |
| 4252     | The Broken Bluffs                                    | 571   | 495    |
| 4253     | 7th Legion Front                                     | 571   | 65     |
| 4254     | The Dragon Wastes                                    | 571   | 65     |
| 4255     | Ruins of Drak'Zin                                    | 571   | 394    |
| 4256     | Drak'Mar Lake                                        | 571   | 65     |
| 4257     | Dragonspine Tributary                                | 571   | 65     |
| 4258     | The North Sea                                        | 571   | 0      |
| 4259     | Drak'ural                                            | 571   | 394    |
| 4260     | Thorvald's Camp                                      | 571   | 495    |
| 4261     | Ghostblade Post                                      | 571   | 495    |
| 4262     | Ashwood Post                                         | 571   | 394    |
| 4263     | Lydell's Ambush                                      | 571   | 495    |
| 4264     | Halls of Stone                                       | 599   | 0      |
| 4265     | The Nexus                                            | 576   | 0      |
| 4266     | Harkor's Camp                                        | 571   | 394    |
| 4267     | Vordrassil Pass                                      | 571   | 394    |
| 4268     | Ruuna's Camp                                         | 571   | 394    |
| 4269     | Shrine of Scales                                     | 571   | 3537   |
| 4270     | Drak'atal Passage                                    | 571   | 394    |
| 4271     | Utgarde Pinnacle                                     | 571   | 495    |
| 4272     | Halls of Lightning                                   | 602   | 0      |
| 4273     | Ulduar                                               | 603   | 0      |
| 4275     | The Argent Stand                                     | 571   | 66     |
| 4276     | Altar of Sseratus                                    | 571   | 66     |
| 4277     | Azjol-Nerub                                          | 601   | 0      |
| 4278     | Drak'Sotra Fields                                    | 571   | 66     |
| 4279     | Drak'Sotra                                           | 571   | 66     |
| 4280     | Drak'Agal                                            | 571   | 66     |
| 4281     | Acherus: The Ebon Hold                               | 0     | 139    |
| 4282     | The Avalanche                                        | 571   | 3711   |
| 4283     | The Lost Lands                                       | 571   | 3711   |
| 4284     | Nesingwary Base Camp                                 | 571   | 3711   |
| 4285     | The Seabreach Flow                                   | 571   | 3711   |
| 4286     | The Bones of Nozronn                                 | 571   | 3711   |
| 4287     | Kartak's Hold                                        | 571   | 3711   |
| 4288     | Sparktouched Haven                                   | 571   | 3711   |
| 4289     | The Path of the Lifewarden                           | 571   | 3711   |
| 4290     | River's Heart                                        | 571   | 3711   |
| 4291     | Rainspeaker Canopy                                   | 571   | 3711   |
| 4292     | Frenzyheart Hill                                     | 571   | 3711   |
| 4293     | Wildgrowth Mangal                                    | 571   | 3711   |
| 4294     | Heb'Valok                                            | 571   | 66     |
| 4295     | The Sundered Shard                                   | 571   | 3711   |
| 4296     | The Lifeblood Pillar                                 | 571   | 3711   |
| 4297     | Mosswalker Village                                   | 571   | 3711   |
| 4298     | Plaguelands: The Scarlet Enclave                     | 609   | 0      |
| 4299     | Kolramas                                             | 571   | 66     |
| 4300     | Waygate                                              | 571   | 3711   |
| 4302     | The Skyreach Pillar                                  | 571   | 3711   |
| 4303     | Hardknuckle Clearing                                 | 571   | 3711   |
| 4304     | Sapphire Hive                                        | 571   | 3711   |
| 4306     | Mistwhisper Refuge                                   | 571   | 3711   |
| 4307     | The Glimmering Pillar                                | 571   | 3711   |
| 4308     | Spearborn Encampment                                 | 571   | 3711   |
| 4309     | Drak'Tharon Keep                                     | 571   | 66     |
| 4310     | Zeramas                                              | 571   | 66     |
| 4311     | Reliquary of Agony                                   | 571   | 66     |
| 4312     | Ebon Watch                                           | 571   | 66     |
| 4313     | Thrym's End                                          | 571   | 66     |
| 4314     | Voltarus                                             | 571   | 66     |
| 4315     | Reliquary of Pain                                    | 571   | 66     |
| 4316     | Rageclaw Den                                         | 571   | 66     |
| 4317     | Light's Breach                                       | 571   | 66     |
| 4318     | Pools of Zha'Jin                                     | 571   | 66     |
| 4319     | Zim'Abwa                                             | 571   | 66     |
| 4320     | Amphitheater of Anguish                              | 571   | 66     |
| 4321     | Altar of Rhunok                                      | 571   | 66     |
| 4322     | Altar of Har'koa                                     | 571   | 66     |
| 4323     | Zim'Torga                                            | 571   | 66     |
| 4324     | Pools of Jin'Alai                                    | 571   | 66     |
| 4325     | Altar of Quetz'lun                                   | 571   | 66     |
| 4326     | Heb'Drakkar                                          | 571   | 66     |
| 4327     | Drak'Mabwa                                           | 571   | 66     |
| 4328     | Zim'Rhuk                                             | 571   | 66     |
| 4329     | Altar of Mam'toth                                    | 571   | 66     |
| 4342     | Acherus: The Ebon Hold                               | 609   | 4298   |
| 4343     | New Avalon                                           | 609   | 4298   |
| 4344     | New Avalon Fields                                    | 609   | 4298   |
| 4345     | New Avalon Orchard                                   | 609   | 4298   |
| 4346     | New Avalon Town Hall                                 | 609   | 4298   |
| 4347     | Havenshire                                           | 609   | 4298   |
| 4348     | Havenshire Farms                                     | 609   | 4298   |
| 4349     | Havenshire Lumber Mill                               | 609   | 4298   |
| 4350     | Havenshire Stables                                   | 609   | 4298   |
| 4351     | Scarlet Hold                                         | 609   | 4298   |
| 4352     | Chapel of the Crimson Flame                          | 609   | 4298   |
| 4353     | Light's Point Tower                                  | 609   | 4298   |
| 4354     | Light's Point                                        | 609   | 4298   |
| 4355     | Crypt of Remembrance                                 | 609   | 4298   |
| 4356     | Death's Breach                                       | 609   | 4298   |
| 4357     | The Noxious Glade                                    | 609   | 4298   |
| 4358     | Tyr's Hand                                           | 609   | 4298   |
| 4359     | King's Harbor                                        | 609   | 4298   |
| 4360     | Scarlet Overlook                                     | 609   | 4298   |
| 4361     | Light's Hope Chapel                                  | 609   | 4298   |
| 4362     | Sinner's Folly                                       | 609   | 4298   |
| 4363     | Pestilent Scar                                       | 609   | 4298   |
| 4364     | Browman Mill                                         | 609   | 4298   |
| 4365     | Havenshire Mine                                      | 609   | 4298   |
| 4366     | Ursoc's Den                                          | 571   | 394    |
| 4367     | The Blight Line                                      | 571   | 3711   |
| 4368     | The Bonefields                                       | 571   | 3711   |
| 4369     | Dorian's Outpost                                     | 571   | 3711   |
| 4371     | Mam'toth Crater                                      | 571   | 66     |
| 4372     | Zol'Maz Stronghold                                   | 571   | 66     |
| 4373     | Zol'Heb                                              | 571   | 66     |
| 4374     | Rageclaw Lake                                        | 571   | 66     |
| 4375     | Gundrak                                              | 571   | 66     |
| 4376     | The Savage Thicket                                   | 571   | 3711   |
| 4377     | New Avalon Forge                                     | 609   | 4298   |
| 4378     | Dalaran Arena                                        | 617   | 0      |
| 4379     | Valgarde                                             | 571   | 495    |
| 4380     | Westguard Inn                                        | 571   | 495    |
| 4381     | Waygate                                              | 1     | 490    |
| 4382     | The Shaper's Terrace                                 | 1     | 490    |
| 4383     | Lakeside Landing                                     | 571   | 3711   |
| 4384     | Strand of the Ancients                               | 607   | 0      |
| 4385     | Bittertide Lake                                      | 571   | 3711   |
| 4386     | Rainspeaker Rapids                                   | 571   | 3711   |
| 4387     | Frenzyheart River                                    | 571   | 3711   |
| 4388     | Wintergrasp River                                    | 571   | 3711   |
| 4389     | The Suntouched Pillar                                | 571   | 3711   |
| 4390     | Frigid Breach                                        | 571   | 66     |
| 4391     | Swindlegrin's Dig                                    | 571   | 3711   |
| 4392     | The Stormwright's Shelf                              | 571   | 3711   |
| 4393     | Death's Hand Encampment                              | 571   | 3711   |
| 4394     | Scarlet Tavern                                       | 609   | 4298   |
| 4395     | Dalaran                                              | 571   | 0      |
| 4396     | Nozzlerust Post                                      | 571   | 65     |
| 4399     | Farshire Mine                                        | 571   | 3537   |
| 4400     | The Mosslight Pillar                                 | 571   | 3711   |
| 4401     | Saragosa's Landing                                   | 571   | 3537   |
| 4402     | Vengeance Lift                                       | 571   | 495    |
| 4403     | Balejar Watch                                        | 571   | 495    |
| 4404     | New Agamand Inn                                      | 571   | 495    |
| 4405     | Passage of Lost Fiends                               | 601   | 4277   |
| 4406     | The Ring of Valor                                    | 618   | 0      |
| 4407     | Hall of the Frostwolf                                | 30    | 2597   |
| 4408     | Hall of the Stormpike                                | 30    | 2597   |
| 4411     | Stormwind Harbor                                     | 0     | 1519   |
| 4412     | The Makers' Overlook                                 | 571   | 3711   |
| 4413     | The Makers' Perch                                    | 571   | 3711   |
| 4414     | Scarlet Tower                                        | 571   | 65     |
| 4415     | The Violet Hold                                      | 608   | 0      |
| 4416     | Gundrak                                              | 604   | 0      |
| 4417     | Onslaught Harbor                                     | 571   | 210    |
| 4418     | K3                                                   | 571   | 67     |
| 4419     | Snowblind Hills                                      | 571   | 67     |
| 4420     | Snowblind Terrace                                    | 571   | 67     |
| 4421     | Garm                                                 | 571   | 67     |
| 4422     | Brunnhildar Village                                  | 571   | 67     |
| 4423     | Sifreldar Village                                    | 571   | 67     |
| 4424     | Valkyrion                                            | 571   | 67     |
| 4425     | The Forlorn Mine                                     | 571   | 67     |
| 4426     | Bor's Breath River                                   | 571   | 67     |
| 4427     | Argent Vanguard                                      | 571   | 67     |
| 4428     | Frosthold                                            | 571   | 67     |
| 4429     | Grom'arsh Crash-Site                                 | 571   | 67     |
| 4430     | Temple of Storms                                     | 571   | 67     |
| 4431     | Engine of the Makers                                 | 571   | 67     |
| 4432     | The Foot Steppes                                     | 571   | 67     |
| 4433     | Dragonspine Peaks                                    | 571   | 67     |
| 4434     | Nidavelir                                            | 571   | 67     |
| 4435     | Narvir's Cradle                                      | 571   | 67     |
| 4436     | Snowdrift Plains                                     | 571   | 67     |
| 4437     | Valley of Ancient Winters                            | 571   | 67     |
| 4438     | Dun Niffelem                                         | 571   | 67     |
| 4439     | Frostfield Lake                                      | 571   | 67     |
| 4440     | Thunderfall                                          | 571   | 67     |
| 4441     | Camp Tunka'lo                                        | 571   | 67     |
| 4442     | Brann's Base-Camp                                    | 571   | 67     |
| 4443     | Gate of Echoes                                       | 571   | 67     |
| 4444     | Plain of Echoes                                      | 571   | 67     |
| 4445     | Ulduar                                               | 571   | 67     |
| 4446     | Terrace of the Makers                                | 571   | 67     |
| 4447     | Gate of Lightning                                    | 571   | 67     |
| 4448     | Path of the Titans                                   | 571   | 67     |
| 4449     | Uldis                                                | 571   | 67     |
| 4450     | Loken's Bargain                                      | 571   | 67     |
| 4451     | Bor's Fall                                           | 571   | 67     |
| 4452     | Bor's Breath                                         | 571   | 67     |
| 4453     | Rohemdal Pass                                        | 571   | 67     |
| 4454     | The Storm Foundry                                    | 571   | 67     |
| 4455     | Hibernal Cavern                                      | 571   | 67     |
| 4456     | Voldrune Dwelling                                    | 571   | 394    |
| 4457     | Torseg's Rest                                        | 571   | 67     |
| 4458     | Sparksocket Minefield                                | 571   | 67     |
| 4459     | Ricket's Folly                                       | 571   | 67     |
| 4460     | Garm's Bane                                          | 571   | 67     |
| 4461     | Garm's Rise                                          | 571   | 67     |
| 4462     | Crystalweb Cavern                                    | 571   | 67     |
| 4463     | Temple of Life                                       | 571   | 67     |
| 4464     | Temple of Order                                      | 571   | 67     |
| 4465     | Temple of Winter                                     | 571   | 67     |
| 4466     | Temple of Invention                                  | 571   | 67     |
| 4467     | Death's Rise                                         | 571   | 210    |
| 4468     | The Dead Fields                                      | 571   | 66     |
| 4469     | Dargath's Demise                                     | 571   | 66     |
| 4470     | The Hidden Hollow                                    | 571   | 210    |
| 4471     | Bernau's Happy Fun Land                              | 451   | 4019   |
| 4472     | Frostgrip's Hollow                                   | 571   | 67     |
| 4473     | The Frigid Tomb                                      | 571   | 67     |
| 4474     | Twin Shores                                          | 571   | 495    |
| 4475     | Zim'bo's Hideout                                     | 571   | 394    |
| 4476     | Abandoned Camp                                       | 571   | 67     |
| 4477     | The Shadow Vault                                     | 571   | 210    |
| 4478     | Coldwind Pass                                        | 571   | 65     |
| 4479     | Winter's Breath Lake                                 | 571   | 495    |
| 4480     | The Forgotten Overlook                               | 571   | 394    |
| 4481     | Jintha'kalar Passage                                 | 571   | 66     |
| 4482     | Arriga Footbridge                                    | 571   | 394    |
| 4483     | The Lost Passage                                     | 571   | 3711   |
| 4484     | Bouldercrag's Refuge                                 | 571   | 67     |
| 4485     | The Inventor's Library                               | 571   | 67     |
| 4486     | The Frozen Mine                                      | 571   | 67     |
| 4487     | Frostfloe Deep                                       | 571   | 67     |
| 4488     | The Howling Hollow                                   | 571   | 67     |
| 4489     | Crusader Forward Camp                                | 571   | 66     |
| 4490     | Stormcrest                                           | 571   | 67     |
| 4491     | Bonesnap's Camp                                      | 571   | 394    |
| 4492     | Ufrang's Hall                                        | 571   | 210    |
| 4493     | The Obsidian Sanctum                                 | 615   | 0      |
| 4494     | Ahn'kahet: The Old Kingdom                           | 619   | 0      |
| 4495     | Fjorn's Anvil                                        | 571   | 67     |
| 4496     | Jotunheim                                            | 571   | 210    |
| 4497     | Savage Ledge                                         | 571   | 210    |
| 4498     | Halls of the Ancestors                               | 571   | 210    |
| 4499     | The Blighted Pool                                    | 571   | 67     |
| 4500     | The Eye of Eternity                                  | 616   | 0      |
| 4501     | The Argent Vanguard                                  | 571   | 210    |
| 4502     | Mimir's Workshop                                     | 571   | 67     |
| 4503     | Ironwall Dam                                         | 571   | 210    |
| 4504     | Valley of Echoes                                     | 571   | 210    |
| 4505     | The Breach                                           | 571   | 210    |
| 4506     | Scourgeholme                                         | 571   | 210    |
| 4507     | The Broken Front                                     | 571   | 210    |
| 4508     | Mord'rethar: The Death Gate                          | 571   | 210    |
| 4509     | The Bombardment                                      | 571   | 210    |
| 4510     | Aldur'thar: The Desolation Gate                      | 571   | 210    |
| 4511     | The Skybreaker                                       | 571   | 210    |
| 4512     | Orgrim's Hammer                                      | 571   | 210    |
| 4513     | Ymirheim                                             | 571   | 210    |
| 4514     | Saronite Mines                                       | 571   | 210    |
| 4515     | The Conflagration                                    | 571   | 210    |
| 4516     | Ironwall Rampart                                     | 571   | 210    |
| 4517     | Weeping Quarry                                       | 571   | 210    |
| 4518     | Corp'rethar: The Horror Gate                         | 571   | 210    |
| 4519     | The Court of Bones                                   | 571   | 210    |
| 4520     | Malykriss: The Vile Hold                             | 571   | 210    |
| 4521     | Cathedral of Darkness                                | 571   | 210    |
| 4522     | Icecrown Citadel                                     | 571   | 210    |
| 4523     | Icecrown Glacier                                     | 571   | 210    |
| 4524     | Valhalas                                             | 571   | 210    |
| 4525     | The Underhalls                                       | 571   | 210    |
| 4526     | Njorndar Village                                     | 571   | 210    |
| 4527     | Balargarde Fortress                                  | 571   | 210    |
| 4528     | Kul'galar Keep                                       | 571   | 210    |
| 4529     | The Crimson Cathedral                                | 571   | 210    |
| 4530     | Sanctum of Reanimation                               | 571   | 210    |
| 4531     | The Fleshwerks                                       | 571   | 210    |
| 4532     | Vengeance Landing Inn                                | 571   | 495    |
| 4533     | Sindragosa's Fall                                    | 571   | 210    |
| 4534     | Wildervar Mine                                       | 571   | 495    |
| 4535     | The Pit of the Fang                                  | 571   | 67     |
| 4536     | Frosthowl Cavern                                     | 571   | 67     |
| 4537     | The Valley of Lost Hope                              | 571   | 210    |
| 4538     | The Sunken Ring                                      | 571   | 4197   |
| 4539     | The Broken Temple                                    | 571   | 4197   |
| 4540     | The Valley of Fallen Heroes                          | 571   | 210    |
| 4541     | Vanguard Infirmary                                   | 571   | 210    |
| 4542     | Hall of the Shaper                                   | 571   | 67     |
| 4543     | Temple of Wisdom                                     | 571   | 67     |
| 4544     | Death's Breach                                       | 0     | 139    |
| 4545     | Abandoned Mine                                       | 0     | 139    |
| 4546     | Ruins of the Scarlet Enclave                         | 0     | 139    |
| 4547     | Halls of Stone                                       | 571   | 67     |
| 4548     | Halls of Lightning                                   | 571   | 67     |
| 4549     | The Great Tree                                       | 571   | 2817   |
| 4550     | The Mirror of Twilight                               | 571   | 2817   |
| 4551     | The Twilight Rivulet                                 | 571   | 2817   |
| 4552     | The Decrepit Flow                                    | 571   | 2817   |
| 4553     | Forlorn Woods                                        | 571   | 2817   |
| 4554     | Ruins of Shandaral                                   | 571   | 2817   |
| 4555     | The Azure Front                                      | 571   | 2817   |
| 4556     | Violet Stand                                         | 571   | 2817   |
| 4557     | The Unbound Thicket                                  | 571   | 2817   |
| 4558     | Sunreaver's Command                                  | 571   | 2817   |
| 4559     | Windrunner's Overlook                                | 571   | 2817   |
| 4560     | The Underbelly                                       | 571   | 4395   |
| 4564     | Krasus' Landing                                      | 571   | 4395   |
| 4567     | The Violet Hold                                      | 571   | 4395   |
| 4568     | The Eventide                                         | 571   | 4395   |
| 4569     | Sewer Exit Pipe                                      | 571   | 4395   |
| 4570     | Circle of Wills                                      | 571   | 4395   |
| 4571     | Silverwing Flag Room                                 | 489   | 3277   |
| 4572     | Warsong Flag Room                                    | 489   | 3277   |
| 4575     | Wintergrasp Fortress                                 | 571   | 4197   |
| 4576     | Central Bridge                                       | 571   | 4197   |
| 4577     | Eastern Bridge                                       | 571   | 4197   |
| 4578     | Western Bridge                                       | 571   | 4197   |
| 4579     | Dubra'Jin                                            | 571   | 66     |
| 4580     | Crusaders' Pinnacle                                  | 571   | 210    |
| 4581     | Flamewatch Tower                                     | 571   | 4197   |
| 4582     | Winter's Edge Tower                                  | 571   | 4197   |
| 4583     | Shadowsight Tower                                    | 571   | 4197   |
| 4584     | The Cauldron of Flames                               | 571   | 4197   |
| 4585     | Glacial Falls                                        | 571   | 4197   |
| 4586     | Windy Bluffs                                         | 571   | 4197   |
| 4587     | The Forest of Shadows                                | 571   | 4197   |
| 4588     | Blackwatch                                           | 571   | 210    |
| 4589     | The Chilled Quagmire                                 | 571   | 4197   |
| 4590     | The Steppe of Life                                   | 571   | 4197   |
| 4591     | Silent Vigil                                         | 571   | 210    |
| 4592     | Gimorak's Den                                        | 571   | 67     |
| 4593     | The Pit of Fiends                                    | 571   | 210    |
| 4594     | Battlescar Spire                                     | 571   | 210    |
| 4595     | Hall of Horrors                                      | 571   | 210    |
| 4596     | The Circle of Suffering                              | 571   | 210    |
| 4597     | Rise of Suffering                                    | 571   | 210    |
| 4598     | Krasus' Landing                                      | 571   | 4395   |
| 4599     | Sewer Exit Pipe                                      | 571   | 4395   |
| 4601     | Dalaran Island                                       | 571   | 4395   |
| 4602     | Force Interior                                       | 571   | 0      |
| 4603     | Vault of Archavon                                    | 624   | 0      |
| 4604     | Gate of the Red Sun                                  | 607   | 4384   |
| 4605     | Gate of the Blue Sapphire                            | 607   | 4384   |
| 4606     | Gate of the Green Emerald                            | 607   | 4384   |
| 4607     | Gate of the Purple Amethyst                          | 607   | 4384   |
| 4608     | Gate of the Yellow Moon                              | 607   | 4384   |
| 4609     | Courtyard of the Ancients                            | 607   | 4384   |
| 4610     | Landing Beach                                        | 607   | 4384   |
| 4611     | Westspark Workshop                                   | 571   | 4197   |
| 4612     | Eastspark Workshop                                   | 571   | 4197   |
| 4613     | Dalaran City                                         | 571   | 4395   |
| 4614     | The Violet Citadel Spire                             | 571   | 4395   |
| 4615     | Naz'anak: The Forgotten Depths                       | 571   | 210    |
| 4616     | Sunreaver's Sanctuary                                | 571   | 4395   |
| 4617     | Elevator                                             | 0     | 1497   |
| 4618     | Antonidas Memorial                                   | 571   | 4395   |
| 4619     | The Violet Citadel                                   | 571   | 4395   |
| 4620     | Magus Commerce Exchange                              | 571   | 4395   |
| 4621     | UNUSED                                               | 571   | 67     |
| 4622     | First Legion Forward Camp                            | 571   | 210    |
| 4623     | Hall of the Conquered Kings                          | 619   | 4494   |
| 4624     | Befouled Terrace                                     | 619   | 4494   |
| 4625     | The Desecrated Altar                                 | 619   | 4494   |
| 4626     | Shimmering Bog                                       | 619   | 4494   |
| 4627     | Fallen Temple of Ahn'kahet                           | 619   | 4494   |
| 4628     | Halls of Binding                                     | 229   | 1583   |
| 4629     | Winter's Heart                                       | 571   | 67     |
| 4630     | The North Sea                                        | 571   | 0      |
| 4631     | The Broodmother's Nest                               | 571   | 67     |
| 4632     | Dalaran Floating Rocks                               | 571   | 4395   |
| 4633     | Raptor Pens                                          | 600   | 4196   |
| 4635     | Drak'Tharon Keep                                     | 571   | 66     |
| 4636     | The Noxious Pass                                     | 609   | 4298   |
| 4637     | Vargoth's Retreat                                    | 571   | 4395   |
| 4638     | Violet Citadel Balcony                               | 571   | 4395   |
| 4639     | Band of Variance                                     | 571   | 3537   |
| 4640     | Band of Acceleration                                 | 571   | 3537   |
| 4641     | Band of Transmutation                                | 571   | 3537   |
| 4642     | Band of Alignment                                    | 571   | 3537   |
| 4646     | Ashwood Lake                                         | 571   | 394    |
| 4650     | Iron Concourse                                       | 603   | 4273   |
| 4652     | Formation Grounds                                    | 603   | 4273   |
| 4653     | Razorscale's Aerie                                   | 603   | 4273   |
| 4654     | The Colossal Forge                                   | 603   | 4273   |
| 4655     | The Scrapyard                                        | 603   | 4273   |
| 4656     | The Conservatory of Life                             | 603   | 4273   |
| 4657     | The Archivum                                         | 603   | 4273   |
| 4658     | Argent Tournament Grounds                            | 571   | 210    |
| 4665     | Expedition Base Camp                                 | 603   | 4273   |
| 4666     | Sunreaver Pavilion                                   | 571   | 210    |
| 4667     | Silver Covenant Pavilion                             | 571   | 210    |
| 4668     | The Cooper Residence                                 | 0     | 40     |
| 4669     | The Ring of Champions                                | 571   | 210    |
| 4670     | The Aspirants' Ring                                  | 571   | 210    |
| 4671     | The Argent Valiants' Ring                            | 571   | 210    |
| 4672     | The Alliance Valiants' Ring                          | 571   | 210    |
| 4673     | The Horde Valiants' Ring                             | 571   | 210    |
| 4674     | Argent Pavilion                                      | 571   | 210    |
| 4676     | Sunreaver Pavilion                                   | 571   | 210    |
| 4677     | Silver Covenant Pavilion                             | 571   | 210    |
| 4679     | The Forlorn Cavern                                   | 0     | 1537   |
| 4688     | claytonio test area                                  | 451   | 151    |
| 4692     | Quel'Delar's Rest                                    | 571   | 210    |
| 4710     | Isle of Conquest                                     | 628   | 0      |
| 4722     | Trial of the Crusader                                | 649   | 0      |
| 4723     | Trial of the Champion                                | 650   | 0      |
| 4739     | Runeweaver Square                                    | 571   | 4395   |
| 4740     | The Silver Enclave                                   | 571   | 4395   |
| 4741     | Isle of Conquest No Man's Land                       | 628   | 4710   |
| 4742     | Hrothgar's Landing                                   | 571   | 0      |
| 4743     | Deathspeaker's Watch                                 | 571   | 210    |
| 4747     | Workshop                                             | 628   | 4710   |
| 4748     | Quarry                                               | 628   | 4710   |
| 4749     | Docks                                                | 628   | 4710   |
| 4750     | Hangar                                               | 628   | 4710   |
| 4751     | Refinery                                             | 628   | 4710   |
| 4752     | Horde Keep                                           | 628   | 4710   |
| 4753     | Alliance Keep                                        | 628   | 4710   |
| 4760     | The Sea Reaver's Run                                 | 571   | 4742   |
| 4763     | Transport: Alliance Gunship                          | 641   | 0      |
| 4764     | Transport: Horde Gunship                             | 642   | 0      |
| 4769     | Hrothgar's Landing                                   | 571   | 4742   |
| 4809     | The Forge of Souls                                   | 632   | 0      |
| 4812     | Icecrown Citadel                                     | 631   | 0      |
| 4813     | Pit of Saron                                         | 658   | 0      |
| 4820     | Halls of Reflection                                  | 668   | 0      |
| 4832     | Transport: Alliance Gunship (IGB)                    | 672   | 0      |
| 4833     | Transport: Horde Gunship (IGB)                       | 673   | 0      |
| 4859     | The Frozen Throne                                    | 631   | 4812   |
| 4862     | The Frozen Halls                                     | 571   | 210    |
| 4889     | The Frost Queen's Lair                               | 631   | 4812   |
| 4890     | Putricide's Laboratory of Alchemical Horrors and Fun | 631   | 4812   |
| 4891     | The Sanctum of Blood                                 | 631   | 4812   |
| 4892     | The Crimson Hall                                     | 631   | 4812   |
| 4893     | The Frost Queen's Lair                               | 631   | 0      |
| 4894     | Putricide's Laboratory of Alchemical Horrors and Fun | 631   | 0      |
| 4895     | The Crimson Hall                                     | 631   | 0      |
| 4896     | The Frozen Throne                                    | 631   | 0      |
| 4897     | The Sanctum of Blood                                 | 631   | 0      |
| 4898     | Frostmourne                                          | 631   | 4896   |
| 4904     | The Dark Approach                                    | 658   | 4813   |
| 4905     | Scourgelord's Command                                | 658   | 4813   |
| 4906     | The Shadow Throne                                    | 668   | 4820   |
| 4908     | The Hidden Passage                                   | 668   | 4820   |
| 4910     | Frostmourne                                          | 631   | 4812   |
| 4987     | The Ruby Sanctum                                     | 724   | 0      |
