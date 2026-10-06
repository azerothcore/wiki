# points\_of\_interest

[<-Back-to:World](database-world)

**The \`points\_of\_interest\` table**

Points of interest that gossip options can mark on the player's minimap, for example when a city guard gives directions. See [gossip\_menu\_option.ActionPoiID](gossip_menu_option#actionpoiid).

**Table: points\_of\_interest's Structure**

| Field                     | Type  |          | Null | Key | Default | Extra | Comment |
| :------------------------ | :---- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                 | INT   | UNSIGNED | NO   | PRI | 0       |       |         |
| [PositionX](#positionx)   | FLOAT |          | NO   |     | 0       |       |         |
| [PositionY](#positiony)   | FLOAT |          | NO   |     | 0       |       |         |
| [Icon](#icon)             | INT   | UNSIGNED | NO   |     | 0       |       |         |
| [Flags](#flags)           | INT   | UNSIGNED | NO   |     | 0       |       |         |
| [Importance](#importance) | INT   | UNSIGNED | NO   |     | 0       |       |         |
| [Name](#name)             | TEXT  |          | NO   |     |         |       |         |

**Description of the table's fields**

### ID

The unique ID of the point of interest.

### PositionX

X position of the point on the map.

### PositionY

Y position of the point on the map.

### icon

| Icon                      | Value | Description               |
| ------------------------- | ----- | ------------------------- |
| ICON\_POI\_BLANK          | 0     | Blank (not visible)       |
| ICON\_POI\_GREY\_AV\_MINE | 1     | Grey mine lorry           |
| ICON\_POI\_RED\_AV\_MINE  | 2     | Red mine lorry            |
| ICON\_POI\_BLUE\_AV\_MINE | 3     | Blue mine lorry           |
| ICON\_POI\_BWTOMB         | 4     | Blue and White Tomb Stone |
| ICON\_POI\_SMALL\_HOUSE   | 5     | Small house               |
| ICON\_POI\_GREYTOWER      | 6     | Grey Tower                |
| ICON\_POI\_REDFLAG        | 7     | Red Flag w/Yellow !       |
| ICON\_POI\_TOMBSTONE      | 8     | Normal tomb stone (brown) |
| ICON\_POI\_BWTOWER        | 9     | Blue and White Tower      |
| ICON\_POI\_REDTOWER       | 10    | Red Tower                 |
| ICON\_POI\_BLUETOWER      | 11    | Blue Tower                |
| ICON\_POI\_RWTOWER        | 12    | Red and White Tower       |
| ICON\_POI\_REDTOMB        | 13    | Red Tomb Stone            |
| ICON\_POI\_RWTOMB         | 14    | Red and White Tomb Stone  |
| ICON\_POI\_BLUETOMB       | 15    | Blue Tomb Stone           |
| ICON\_POI\_16             | 16    | Grey ?                    |
| ICON\_POI\_17             | 17    | Blue/White ?              |
| ICON\_POI\_18             | 18    | Blue ?                    |
| ICON\_POI\_19             | 19    | Red and White ?           |
| ICON\_POI\_20             | 20    | Red ?                     |
| ICON\_POI\_GREYLOGS       | 21    | Grey Wood Logs            |
| ICON\_POI\_BWLOGS         | 22    | Blue and White Wood Logs  |
| ICON\_POI\_BLUELOGS       | 23    | Blue Wood Logs            |
| ICON\_POI\_RWLOGS         | 24    | Red and White Wood Logs   |
| ICON\_POI\_REDLOGS        | 25    | Red Wood Logs             |
| ICON\_POI\_26             | 26    | Grey ?                    |
| ICON\_POI\_27             | 27    | Blue and White ?          |
| ICON\_POI\_28             | 28    | Blue ?                    |
| ICON\_POI\_29             | 29    | Red and White ?           |
| ICON\_POI\_30             | 30    | Red ?                     |
| ICON\_POI\_GREYHOUSE      | 31    | Grey House                |
| ICON\_POI\_BWHOUSE        | 32    | Blue and White House      |
| ICON\_POI\_BLUEHOUSE      | 33    | Blue House                |
| ICON\_POI\_RWHOUSE        | 34    | Red and White House       |
| ICON\_POI\_REDHOUSE       | 35    | Red House                 |
| ICON\_POI\_GREYHORSE      | 36    | Grey Horse                |
| ICON\_POI\_BWHORSE        | 37    | Blue and White Horse      |
| ICON\_POI\_BLUEHORSE      | 38    | Blue Horse                |
| ICON\_POI\_RWHORSE        | 39    | Red and White Horse       |
| ICON\_POI\_REDHORSE       | 40    | Red Horse                 |

### Flags

Sent to the client with the point. Its exact effect is not known, most points use 99.

### Importance

Sent to the client with the point. Its exact effect is not known.

### Name

The name of the point of interest shown to the player.
