# gameobject\_template\_addon

[<-Back-to:World](database-world)

This table holds additional information on gameobjects.

**Table: gameobject\_template\_addon's Structure**

| Field               | Type     |          | Null | Key | Default | Extra | Comment |
| :------------------ | :------- | :------- | :--: | :-: | :-----: | :---: | :------ |
| [entry](#entry)     | INT      | UNSIGNED | NO   | PRI | 0       |       |         |
| [faction](#faction) | SMALLINT | UNSIGNED | NO   |     | 0       |       |         |
| [flags](#flags)     | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [mingold](#mingold) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [maxgold](#maxgold) | INT      | UNSIGNED | NO   |     | 0       |       |         |
| [artkit0](#artkit)  | INT      |          | NO   |     | 0       |       |         |
| [artkit1](#artkit)  | INT      |          | NO   |     | 0       |       |         |
| [artkit2](#artkit)  | INT      |          | NO   |     | 0       |       |         |
| [artkit3](#artkit)  | INT      |          | NO   |     | 0       |       |         |

**Description of the table's fields**

### entry

ID of the game object, from [gameobject\_template.entry](gameobject_template#entry).

### faction

Object's faction, if any. See [FactionTemplate](factiontemplate)

### flags

| Value | Hex      | Flag                      | Comment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| :---- | :------: | :------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1     | `0x0001` | GO\_FLAG\_IN\_USE         | Gameobject in use - Disables interaction while being animated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2     | `0x0002` | GO\_FLAG\_LOCKED          | Makes the Gameobject Locked. Requires a key, spell, or event to be opened. "Locked" appears in tooltip                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 4     | `0x0004` | GO\_FLAG\_INTERACT\_COND  | Untargetable, cannot interact (condition to interact - requires GO_DYNFLAG_LO_ACTIVATE to enable interaction clientside)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 8     | `0x0008` | GO\_FLAG\_TRANSPORT       | Gameobject can transport (boat, elevator, car)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 16    | `0x0010` | GO\_FLAG\_NOT\_SELECTABLE | Not selectable (Not even in GM-mode)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 32    | `0x0020` | GO\_FLAG\_NODESPAWN       | Never despawns. Typical for gameobjects with on/off state (doors for example)                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 64    | `0x0040` | GO\_FLAG\_TRIGGERED       | Typically a summoned object, triggered by a spell or another event. This is the meaning in the core, [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Globals/SharedDefines.h) and [mangos](https://github.com/mangostwo/server/blob/master/src/game/Server/SharedDefines.h). [TrinityCore](https://github.com/TrinityCore/TrinityCore/blob/3.3.5/src/server/shared/SharedDefines.h) names this bit GO\_FLAG\_AI\_OBSTACLE instead: the client registers the object in something called AIObstacleMgr                  |
| 128   | `0x0080` | *Not in the core*         | The emulators disagree. [TrinityCore](https://github.com/TrinityCore/TrinityCore/blob/3.3.5/src/server/shared/SharedDefines.h) names it GO\_FLAG\_FREEZE\_ANIMATION, [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Globals/SharedDefines.h) names it GO\_FLAG\_AI\_OBSTACLE, [mangos](https://github.com/mangostwo/server/blob/master/src/game/Server/SharedDefines.h) and [WowPacketParser](https://github.com/TrinityCore/WowPacketParser/blob/master/WowPacketParser/Enums/GameObjectFlag.cs) have it as unknown |
| 256   | `0x0100` | *Not in the core*         | [cmangos](https://github.com/cmangos/mangos-wotlk/blob/master/src/game/Globals/SharedDefines.h) names it GO\_FLAG\_FREEZE\_ANIMATION. [mangos](https://github.com/mangostwo/server/blob/master/src/game/Server/SharedDefines.h) has it as unknown and notes it was seen on destructible buildings (type 33). [WowPacketParser](https://github.com/TrinityCore/WowPacketParser/blob/master/WowPacketParser/Enums/GameObjectFlag.cs) has it as unknown, and TrinityCore does not define it                                                     |
| 512   | `0x0200` | GO\_FLAG\_DAMAGED         | Gameobject has been siege damaged                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 1024  | `0x0400` | GO\_FLAG\_DESTROYED       | Gameobject has been destroyed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### mingold

Minimum money, in copper, that the gameobject can drop when accessed / used.

### maxgold

Maximum money, in copper, that the gameobject can drop when accessed / used.

### artkit

GameObjectArtKit.dbc ID

Updates display if object is activated by SPELL_EFFECT_ACTIVATE_OBJECT with MiscValue 19 - 22.
