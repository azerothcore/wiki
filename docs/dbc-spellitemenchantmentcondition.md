# SpellItemEnchantmentCondition.dbc

[`Back-to:DBC`](dbc-index)

**The \`SpellItemEnchantmentCondition.dbc\` file**

A client file of 3.3.5a (build 12340). AzerothCore loads it when the server starts. Its rows can be replaced or extended with the [spellitemenchantmentcondition_dbc](spellitemenchantmentcondition_dbc) table of the world database.

**Structure**

| Column | Field           | Type   | spellitemenchantmentcondition\_dbc column                           | Comment |
| :----: | :-------------- | :----- | :------------------------------------------------------------------ | :------ |
| 0      | ID              | uint32 | [ID](spellitemenchantmentcondition_dbc#id)                          |         |
| 1      | LtOperandType_0 | uint8  | [Lt_OperandType_1](spellitemenchantmentcondition_dbc#ltoperandtype) |         |
| 2      | LtOperandType_1 | uint8  | [Lt_OperandType_2](spellitemenchantmentcondition_dbc#ltoperandtype) |         |
| 3      | LtOperandType_2 | uint8  | [Lt_OperandType_3](spellitemenchantmentcondition_dbc#ltoperandtype) |         |
| 4      | LtOperandType_3 | uint8  | [Lt_OperandType_4](spellitemenchantmentcondition_dbc#ltoperandtype) |         |
| 5      | LtOperandType_4 | uint8  | [Lt_OperandType_5](spellitemenchantmentcondition_dbc#ltoperandtype) |         |
| 6      | LtOperand_0     | uint32 | [Lt_Operand_1](spellitemenchantmentcondition_dbc#ltoperand)         |         |
| 7      | LtOperand_1     | uint32 | [Lt_Operand_2](spellitemenchantmentcondition_dbc#ltoperand)         |         |
| 8      | LtOperand_2     | uint32 | [Lt_Operand_3](spellitemenchantmentcondition_dbc#ltoperand)         |         |
| 9      | LtOperand_3     | uint32 | [Lt_Operand_4](spellitemenchantmentcondition_dbc#ltoperand)         |         |
| 10     | LtOperand_4     | uint32 | [Lt_Operand_5](spellitemenchantmentcondition_dbc#ltoperand)         |         |
| 11     | Operator_0      | uint8  | [Operator_1](spellitemenchantmentcondition_dbc#operator)            |         |
| 12     | Operator_1      | uint8  | [Operator_2](spellitemenchantmentcondition_dbc#operator)            |         |
| 13     | Operator_2      | uint8  | [Operator_3](spellitemenchantmentcondition_dbc#operator)            |         |
| 14     | Operator_3      | uint8  | [Operator_4](spellitemenchantmentcondition_dbc#operator)            |         |
| 15     | Operator_4      | uint8  | [Operator_5](spellitemenchantmentcondition_dbc#operator)            |         |
| 16     | RtOperandType_0 | uint8  | [Rt_OperandType_1](spellitemenchantmentcondition_dbc#rtoperandtype) |         |
| 17     | RtOperandType_1 | uint8  | [Rt_OperandType_2](spellitemenchantmentcondition_dbc#rtoperandtype) |         |
| 18     | RtOperandType_2 | uint8  | [Rt_OperandType_3](spellitemenchantmentcondition_dbc#rtoperandtype) |         |
| 19     | RtOperandType_3 | uint8  | [Rt_OperandType_4](spellitemenchantmentcondition_dbc#rtoperandtype) |         |
| 20     | RtOperandType_4 | uint8  | [Rt_OperandType_5](spellitemenchantmentcondition_dbc#rtoperandtype) |         |
| 21     | RtOperand_0     | uint32 | [Rt_Operand_1](spellitemenchantmentcondition_dbc#rtoperand)         |         |
| 22     | RtOperand_1     | uint32 | [Rt_Operand_2](spellitemenchantmentcondition_dbc#rtoperand)         |         |
| 23     | RtOperand_2     | uint32 | [Rt_Operand_3](spellitemenchantmentcondition_dbc#rtoperand)         |         |
| 24     | RtOperand_3     | uint32 | [Rt_Operand_4](spellitemenchantmentcondition_dbc#rtoperand)         |         |
| 25     | RtOperand_4     | uint32 | [Rt_Operand_5](spellitemenchantmentcondition_dbc#rtoperand)         |         |
| 26     | Logic_0         | uint8  | [Logic_1](spellitemenchantmentcondition_dbc#logic)                  |         |
| 27     | Logic_1         | uint8  | [Logic_2](spellitemenchantmentcondition_dbc#logic)                  |         |
| 28     | Logic_2         | uint8  | [Logic_3](spellitemenchantmentcondition_dbc#logic)                  |         |
| 29     | Logic_3         | uint8  | [Logic_4](spellitemenchantmentcondition_dbc#logic)                  |         |
| 30     | Logic_4         | uint8  | [Logic_5](spellitemenchantmentcondition_dbc#logic)                  |         |

The layout of this file is also described on [wowdev.wiki](https://wowdev.wiki/DB/SpellItemEnchantmentCondition).
