# gameobject\_template\_addon

This table holds additional information on gameobjects.

## Structure

| Field               | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry](#entry)     | INT      | UNSIGNED   | PRI | NO   | 0       |       |         |
| [faction](#faction) | SMALLINT | UNSIGNED   |     | NO   | 0       |       |         |
| [flags](#flags)     | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [mingold](#mingold) | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [maxgold](#maxgold) | INT      | UNSIGNED   |     | NO   | 0       |       |         |
| [artkit0](#artkit)  | INT      |            |     |      | 0       |       |         |
| [artkit1](#artkit)  | INT      |            |     |      | 0       |       |         |
| [artkit2](#artkit)  | INT      |            |     |      | 0       |       |         |
| [artkit3](#artkit)  | INT      |            |     |      | 0       |       |         |

## Description of the fields

### entry

ID of the game object, from [gameobject\_template.entry](gameobject_template#entry).

### faction

Object's faction, if any. See [FactionTemplate](factiontemplate)

### flags

| Flag       | Bit  | Name                        | Comment                                                                                                                  |
| ---------- | ---- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 0x00000001 | 1    | GO\_FLAG\_IN\_USE           | Gameobject in use - Disables interaction while being animated                                                            |
| 0x00000002 | 2    | GO\_FLAG\_LOCKED            | Makes the Gameobject Locked. Requires a key, spell, or event to be opened. "Locked" appears in tooltip                   |
| 0x00000004 | 4    | GO\_FLAG\_INTERACT\_COND    | Untargetable, cannot interact (condition to interact - requires GO_DYNFLAG_LO_ACTIVATE to enable interaction clientside) |
| 0x00000008 | 8    | GO\_FLAG\_TRANSPORT         | Gameobject can transport (boat, elevator, car)                                                                           |
| 0x00000010 | 16   | GO\_FLAG\_NOT\_SELECTABLE   | Not selectable (Not even in GM-mode)                                                                                     |
| 0x00000020 | 32   | GO\_FLAG\_NODESPAWN         | Never despawns. Typical for gameobjects with on/off state (doors for example)                                            |
| 0x00000040 | 64   | GO\_FLAG\_TRIGGERED         | (GO_FLAG_AI_OBSTACLE) makes the client register the object in something called AIObstacleMgr, unknown what it does       |
| 0x00000080 | 128  | GO\_FLAG\_FREEZE\_ANIMATION | unused from AzerothCore                                                                                                  |
| 0x00000200 | 512  | GO\_FLAG\_DAMAGED           | Gameobject has been siege damaged                                                                                        |
| 0x00000400 | 1024 | GO\_FLAG\_DESTROYED         | Gameobject has been destroyed                                                                                            |

### mingold

Minimum money, in copper, that the gameobject can drop when accessed / used.

### maxgold

Maximum money, in copper, that the gameobject can drop when accessed / used.

### artkit

GameObjectArtKit.dbc ID

Updates display if object is activated by SPELL_EFFCT_ACTIVATE_OBJECT with MiscValue 19 - 22.
