# vehicle\_accessory

[<-返回:World](database-world)

**\`vehicle\_accessory\` 表**

此表用于告知服务器在生成该载具时同时生成额外的 NPC。

**表结构**

| Field                | Type      | Attributes | Key | Null | Default | Extra | Comment                                          |
| -------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------------------------------------------------ |
| [guid][1]            | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |                                                  |
| [accessory_entry][2] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |                                                  |
| [seat_id][3]         | TINYINT   | SIGNED     | PRI | NO   | 0       |       |                                                  |
| [minion][4]          | TINYINT   | UNSIGNED   |     | NO   | 0       |       |                                                  |
| [description][5]     | text      | SIGNED     |     | NO   | "       |       |                                                  |
| [summontype][6]      | TINYINT   | UNSIGNED   |     | NO   | 6       |       | 参见枚举 TempSummonType                          |
| [summontimer][7]     | INT       | UNSIGNED   |     | NO   | 30000   |       | 计时器，仅对特定 summontype 有效                |

[1]: #guid
[2]: #accessoryentry
[3]: #seatid
[4]: #minion
[5]: #description
[6]: #summontype
[7]: #summontimer

**字段描述**

### guid

用作载具的生物的 Guid，可从 [creature](creature) 表中获取。

### accessory\_entry

用作主载具的骑乘者/炮塔/附加组件的 creature_template entry。取自 creature_template 的 ID。
飞行载具必须将 InhabitType 设置为（4 - Flying）。

### seat\_id

应在其中生成附加组件的载具座位。参见 [VehicleSeat.dbc](https://wowdev.wiki/DB/VehicleSeat)。

### minion

如果值为 0，当载具死亡时附加组件不会死亡。
如果值为 1，当载具死亡时附加组件也会死亡。

注意：制作可分离载具时，你通常应使用值 0，否则当主载具死亡时，分离出去的载具也会一同死亡。

### description

注释

### summontype

| Flag | Name                                   | Comments                                                      |
| ---- | -------------------------------------- | ------------------------------------------------------------- |
| 1    | TEMPSUMMON_TIMED_OR_DEAD_DESPAWN       | 在指定时间后或生物消失时消失                                  |
| 2    | TEMPSUMMON_TIMED_OR_CORPSE_DESPAWN     | 在指定时间后或生物死亡时消失                                  |
| 3    | TEMPSUMMON_TIMED_DESPAWN               | 在指定时间后消失                                              |
| 4    | TEMPSUMMON_TIMED_DESPAWN_OUT_OF_COMBAT | 在生物脱离战斗后的指定时间后消失                              |
| 5    | TEMPSUMMON_CORPSE_DESPAWN              | 死亡后立即消失                                                |
| 6    | TEMPSUMMON_CORPSE_TIMED_DESPAWN        | 死亡后的指定时间后消失                                        |
| 7    | TEMPSUMMON_DEAD_DESPAWN                | 当生物消失时消失                                              |
| 8    | TEMPSUMMON_MANUAL_DESPAWN              | 当调用 UnSummon() 时消失                                      |

### summontimer

与 summontype 关联的计时器
