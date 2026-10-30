# HitInfo Reference

[`Back-to:Documentation Index`](documentation-index)

This page lists the hit info flags of a melee swing. They are not stored in the database: the core builds them for each swing and sends them to the client in the `SMSG_ATTACKERSTATEUPDATE` packet, where they decide what the client shows (critical hit, block, absorb and so on).

The flags come from the enumeration `HitInfo` in [Unit.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Entities/Unit/Unit.h). The names and notes follow what was seen in sniffs ([pull request 27612](https://github.com/azerothcore/azerothcore-wotlk/pull/27612)).

**Version is : 3.3.5a**

## Flags

| Value    | Hex          | Flag                     | Comment                                                                                                                                                                                    |
| :------- | :----------: | :----------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0        | `0x00000000` | HITINFO_NORMALSWING      | Normal swing, no flag                                                                                                                                                                      |
| 1        | `0x00000001` | HITINFO_DEBUG            | The packet has extra debug data, such as the chance to crit, miss or dodge                                                                                                                 |
| 2        | `0x00000002` | HITINFO_AFFECTS_VICTIM   |                                                                                                                                                                                            |
| 4        | `0x00000004` | HITINFO_OFFHAND          | The swing is made with the off-hand weapon                                                                                                                                                 |
| 8        | `0x00000008` | HITINFO_UNK2             | Not seen in sniffs                                                                                                                                                                         |
| 16       | `0x00000010` | HITINFO_MISS             | The swing missed                                                                                                                                                                           |
| 32       | `0x00000020` | HITINFO_FULL_ABSORB      | All the damage was absorbed                                                                                                                                                                |
| 64       | `0x00000040` | HITINFO_PARTIAL_ABSORB   | Part of the damage was absorbed                                                                                                                                                            |
| 128      | `0x00000080` | HITINFO_FULL_RESIST      | All the damage was resisted                                                                                                                                                                |
| 256      | `0x00000100` | HITINFO_PARTIAL_RESIST   | Part of the damage was resisted                                                                                                                                                            |
| 512      | `0x00000200` | HITINFO_CRITICALHIT      | Critical hit                                                                                                                                                                               |
| 1024     | `0x00000400` | HITINFO_ROLLED_DODGE     | The victim is able to dodge and the chance was rolled                                                                                                                                      |
| 2048     | `0x00000800` | HITINFO_ROLLED_PARRY     | The victim is able to parry and the chance was rolled                                                                                                                                      |
| 4096     | `0x00001000` | HITINFO_ROLLED_BLOCK     | The victim is able to block and the chance was rolled                                                                                                                                      |
| 8192     | `0x00002000` | HITINFO_BLOCK            | Damage was blocked. Always comes with HITINFO_ROLLED_BLOCK                                                                                                                                 |
| 16384    | `0x00004000` | HITINFO_NO_FLOATING_TEXT | No text is shown in the world when the victim is hit for 0 damage. Set only when the swing has a melee spell ID                                                                            |
| 32768    | `0x00008000` | HITINFO_BLOOD_SPURT      | Sprays extra blood. Set on hits where the damage, with the absorbed, resisted and blocked part, is between 20% and 100% of the maximum health of the victim. Only seen with player victims |
| 65536    | `0x00010000` | HITINFO_GLANCING         | Glancing blow                                                                                                                                                                              |
| 131072   | `0x00020000` | HITINFO_CRUSHING         | Crushing blow                                                                                                                                                                              |
| 262144   | `0x00040000` | HITINFO_NO_ANIMATION     | No swing animation. Always set when the swing has a melee spell ID                                                                                                                         |
| 524288   | `0x00080000` | HITINFO_PVP              | Set only when the attacker and the victim are both controlled by a player (UNIT_FLAG_PLAYER_CONTROLLED)                                                                                    |
| 1048576  | `0x00100000` | HITINFO_DUEL             | Always comes with HITINFO_PVP. Never seen in battlegrounds or arenas, often seen in sanctuary areas                                                                                        |
| 2097152  | `0x00200000` | HITINFO_SWINGNOHITSOUND  | Not seen in sniffs                                                                                                                                                                         |
| 4194304  | `0x00400000` | HITINFO_CRITICAL_BLOCK   | Always comes with HITINFO_BLOCK. The victim is always a warrior with the Critical Block talent, and the blocked amount is doubled                                                          |
| 8388608  | `0x00800000` | HITINFO_RAGE_GAIN        |                                                                                                                                                                                            |
| 16777216 | `0x01000000` | HITINFO_FAKE_DAMAGE      | Plays the damage animation although no damage was done. Set only when there is no damage                                                                                                   |
