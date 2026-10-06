# ScalingStatValues.dbc

[`Back-to:DBC`](dbc-index)

**The \`ScalingStatValues.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [scalingstatvalues_dbc](scalingstatvalues_dbc) table of the world database.

**Structure**

| Column | Field                | Type   | scalingstatvalues\_dbc column                                      | Comment |
| :----: | :------------------- | :----- | :----------------------------------------------------------------- | :------ |
| 0      | ID                   | uint32 | [ID](scalingstatvalues_dbc#id)                                     |         |
| 1      | Charlevel            | uint32 | [Charlevel](scalingstatvalues_dbc#charlevel)                       |         |
| 2      | ShoulderBudget       | uint32 | [ShoulderBudget](scalingstatvalues_dbc#shoulderbudget)             |         |
| 3      | TrinketBudget        | uint32 | [TrinketBudget](scalingstatvalues_dbc#trinketbudget)               |         |
| 4      | WeaponBudget1H       | uint32 | [WeaponBudget1H](scalingstatvalues_dbc#weaponbudget1h)             |         |
| 5      | RangedBudget         | uint32 | [RangedBudget](scalingstatvalues_dbc#rangedbudget)                 |         |
| 6      | ClothShoulderArmor   | uint32 | [ClothShoulderArmor](scalingstatvalues_dbc#clothshoulderarmor)     |         |
| 7      | LeatherShoulderArmor | uint32 | [LeatherShoulderArmor](scalingstatvalues_dbc#leathershoulderarmor) |         |
| 8      | MailShoulderArmor    | uint32 | [MailShoulderArmor](scalingstatvalues_dbc#mailshoulderarmor)       |         |
| 9      | PlateShoulderArmor   | uint32 | [PlateShoulderArmor](scalingstatvalues_dbc#plateshoulderarmor)     |         |
| 10     | WeaponDPS1H          | uint32 | [WeaponDPS1H](scalingstatvalues_dbc#weapondps1h)                   |         |
| 11     | WeaponDPS2H          | uint32 | [WeaponDPS2H](scalingstatvalues_dbc#weapondps2h)                   |         |
| 12     | SpellcasterDPS1H     | uint32 | [SpellcasterDPS1H](scalingstatvalues_dbc#spellcasterdps1h)         |         |
| 13     | SpellcasterDPS2H     | uint32 | [SpellcasterDPS2H](scalingstatvalues_dbc#spellcasterdps2h)         |         |
| 14     | RangedDPS            | uint32 | [RangedDPS](scalingstatvalues_dbc#rangeddps)                       |         |
| 15     | WandDPS              | uint32 | [WandDPS](scalingstatvalues_dbc#wanddps)                           |         |
| 16     | SpellPower           | uint32 | [SpellPower](scalingstatvalues_dbc#spellpower)                     |         |
| 17     | PrimaryBudget        | uint32 | [PrimaryBudget](scalingstatvalues_dbc#primarybudget)               |         |
| 18     | TertiaryBudget       | uint32 | [TertiaryBudget](scalingstatvalues_dbc#tertiarybudget)             |         |
| 19     | ClothCloakArmor      | uint32 | [ClothCloakArmor](scalingstatvalues_dbc#clothcloakarmor)           |         |
| 20     | ClothChestArmor      | uint32 | [ClothChestArmor](scalingstatvalues_dbc#clothchestarmor)           |         |
| 21     | LeatherChestArmor    | uint32 | [LeatherChestArmor](scalingstatvalues_dbc#leatherchestarmor)       |         |
| 22     | MailChestArmor       | uint32 | [MailChestArmor](scalingstatvalues_dbc#mailchestarmor)             |         |
| 23     | PlateChestArmor      | uint32 | [PlateChestArmor](scalingstatvalues_dbc#platechestarmor)           |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/ScalingStatValues).
