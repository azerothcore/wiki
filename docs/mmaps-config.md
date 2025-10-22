# MMap Configuration File

## skipLiquid
Usage: `true` or `false`

Default: `false`

This is what responsible for creature or player's without control movement in liquids, water, lava or liquid areas.


## skipContinents
Usage: `true` or `false`

Default: `false`

This is what responsible for creature or player's without control movement for the open-world, which excludes instances like Dungeons, Raids or specific un-used or test maps which are not considered "junk" maps.


## skipJunkMaps
Usage: `true` or `false`

Default: `true`

This is what responsible for creature or player's without control movement for what the core and extractors refer as "junk" maps which are files that do not contain full data to be considered a proper map.


## skipBattlegrounds
Usage: `true` or `false`

Default: `false`

This is what responsible for creature or player's without control movement for Battkegrounds Instances.


## dataDir
Usage: Directory / Path

Default: `./`

Path to the directory containing navigation data files. This directory should contain the "maps" and "vmaps" folders, and is also where the "mmaps" folder will be created or located.


### walkableSlopeAngle
Usage: Integer / whole  Number in degrees

Default: `60`

Maximum slope angle (in degrees) NPCs can walk on. Surfaces steeper than this will be considered unwalkable.

**TECHNICAL PART [Cell Size Calculation] Can be skipped for normal users** 

Many parameters below are defined in "cell units". In RecastDemo, you often work with world units instead of cell units. By default, these cell units are converted to world units using the formula:

```
cellSize = MMAP::GRID_SIZE / (verticesPerMapEdge - 1)
```

**WHERE:**

```
MMAP::GRID_SIZE = 533.3333f (the size of one map tile in world units)
verticesPerMapEdge = number of vertices along one edge of the full map grid
```

**EXAMPLE:**

```   
If verticesPerMapEdge = 2000, then: cellSize ≈ 533.3333 / (2000 - 1) ≈ 0.2667 world units per cell

To convert a value from cell units to world units (e.g., walkableClimb), multiply by cellSize. For example, a walkableClimb of 6 corresponds to: 6 * 0.2667 ≈ 1.6 world units

```


### walkableHeight
Usage: Integer / whole  Number

Default: `6`

Minimum ceiling height (in cell units) NPCs need to pass under an obstacle. Controls how much vertical clearance is required. To convert to world units, multiply by cellSize (see "Cell Size Calculation").


### walkableClimb
Usage: Integer / whole  Number

Default: `6`



### walkableRadius
Usage: Integer / whole  Number

Default: `2`



### verticesPerMapEdge
Usage: Integer / whole  Number

Default: `2000`



### verticesPerTileEdge
Usage: Integer / whole  Number

Default: `80`



### maxSimplificationError
Usage: Float / Number with decimal values

Default: `1.8`



### mapsOverrides
Usage: [MapID](map)

Default:
```
562 | Blade's Edge Arena
walkableRadius: 0
This allows walking on the ropes to the pillars

48 | Blackfathom Deeps
cellSizeVertical: 0.5334 # ch*2 = 0.2667 * 2 ≈ 0.5334. 
Reduce the chance to have underground levels.

529 | Arathi Basin
tilesOverrides: 30,29: 
walkableSlopeAngle: 45
Make sure that Fear will not drop players rom cliff in Lumber Mill
https://github.com/azerothcore/azerothcore-wotlk/pull/22462#issuecomment-3067024680
```

### debugOutput