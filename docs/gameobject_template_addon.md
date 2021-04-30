# gameobject\_template\_addon

Table created and content moved from gameobject\_template in commit bd4bf0a

## Structure

|                                               |              |                |         |          |             |           |             |
|-----------------------------------------------|--------------|----------------|---------|----------|-------------|-----------|-------------|
| **Field**                                     | **Type**     | **Attributes** | **Key** | **Null** | **Default** | **Extra** | **Comment** |
| [entry](#gameobject_template_addon-entry)     | MEDIUMINT | UNSIGNED       | PRI     | NO       | 0           |           |             |
| [faction](#gameobject_template_addon-faction) | SMALLINT  | UNSIGNED       |         | NO       | 0           |           |             |
| [flags](#gameobject_template_addon-flags)     | INT      | UNSIGNED       |         | NO       | 0           |           |             |
| mingold                                       | MEDIUMINT | UNSIGNED       |         | NO       | 0           |           |             |
| maxgold                                       | MEDIUMINT | UNSIGNED       |         | NO       | 0           |           |             |

## Description of the fields

### entry

ID of the game object, from [gameobject\_template.entry](https://trinitycore.atlassian.net/wiki/display/tc/gameobject_template#gameobject_template-entry). (`WDB fields)`

### faction

Object's faction, if any. See [FactionTemplate](FactionTemplate) (`Sniff fields)`

### flags

| Flag | Name       | Comments                  |
|------|------------|---------------------------|
| 1    | 0x00000001 | GO\_FLAG\_IN\_USE         |
| 2    | 0x00000002 | GO\_FLAG\_LOCKED          |
| 4    | 0x00000004 | GO\_FLAG\_INTERACT\_COND  |
| 8    | 0x00000008 | GO\_FLAG\_TRANSPORT       |
| 16   | 0x00000010 | GO\_FLAG\_NOT\_SELECTABLE |
| 32   | 0x00000020 | GO\_FLAG\_NODESPAWN       |
| 64   | 0x00000040 | GO\_FLAG\_TRIGGERED       |
| 512  | 0x00000200 | GO\_FLAG\_DAMAGED         |
| 1024 | 0x00000400 | GO\_FLAG\_DESTROYED       |

`Sniff fields`

### mingold

Minimum money, in copper, that the gameobject can drop when accessed / used.

### maxgold

Maximum money, in copper, that the gameobject can drop when accessed / used.
