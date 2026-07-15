# gameobject\_template\_addon

Esta tabla contiene información adicional sobre los gameobjects.

## Estructura

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

## Descripción de los campos

### entry

ID del objeto de juego, de [gameobject\_template.entry](gameobject_template#entry).

### faction

La facción del objeto, si tiene. Ver [FactionTemplate](factiontemplate)

### flags

| Flag       | Bit  | Name                        | Comment                                                                                                                  |
| ---------- | ---- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| 0x00000001 | 1    | GO\_FLAG\_IN\_USE           | Gameobject en uso - Deshabilita la interacción mientras se está animando                                                 |
| 0x00000002 | 2    | GO\_FLAG\_LOCKED            | Hace que el gameobject esté bloqueado. Requiere una llave, hechizo o evento para abrirse. Aparece "Locked" en el tooltip |
| 0x00000004 | 4    | GO\_FLAG\_INTERACT\_COND    | No seleccionable, no se puede interactuar (condición para interactuar - requiere GO_DYNFLAG_LO_ACTIVATE para habilitar la interacción del lado del cliente) |
| 0x00000008 | 8    | GO\_FLAG\_TRANSPORT         | El gameobject puede transportar (barco, ascensor, coche)                                                                 |
| 0x00000010 | 16   | GO\_FLAG\_NOT\_SELECTABLE   | No seleccionable (ni siquiera en modo GM)                                                                                |
| 0x00000020 | 32   | GO\_FLAG\_NODESPAWN         | Nunca desaparece. Típico de gameobjects con estado on/off (puertas por ejemplo)                                         |
| 0x00000040 | 64   | GO\_FLAG\_TRIGGERED         | (GO_FLAG_AI_OBSTACLE) hace que el cliente registre el objeto en algo llamado AIObstacleMgr, se desconoce qué hace       |
| 0x00000080 | 128  | GO\_FLAG\_FREEZE\_ANIMATION | sin usar en AzerothCore                                                                                                  |
| 0x00000200 | 512  | GO\_FLAG\_DAMAGED           | El gameobject ha sido dañado por asedio                                                                                  |
| 0x00000400 | 1024 | GO\_FLAG\_DESTROYED         | El gameobject ha sido destruido                                                                                          |

### mingold

Dinero mínimo, en cobre, que el gameobject puede soltar al accederse / usarse.

### maxgold

Dinero máximo, en cobre, que el gameobject puede soltar al accederse / usarse.

### artkit

ID de GameObjectArtKit.dbc

Actualiza la visualización si el objeto se activa mediante SPELL_EFFCT_ACTIVATE_OBJECT con MiscValue 19 - 22.
