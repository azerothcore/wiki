# spellitemenchantmentcondition\_dbc

[<-Back-to:World](database-world)

**The \`spellitemenchantmentcondition\_dbc\` table**

This table has the same columns as the client file `SpellItemEnchantmentCondition.dbc`. At startup the core loads the file and then this table: a row here replaces the row with the same `ID` from the file, and a row with a new `ID` is added. When a row is replaced, a text column that is left empty keeps the text from the file.

See [How to import DBC data inside the AC database](how-to-import-dbc-data-in-db) for how to fill this table.

**Table: spellitemenchantmentcondition\_dbc's Structure**

| Field                              | Type    |          | Null | Key | Default | Extra | Comment |
| :--------------------------------- | :------ | :------- | :--: | :-: | :-----: | :---: | :------ |
| [ID](#id)                          | INT     |          | NO   | PRI | 0       |       |         |
| [Lt_OperandType_1](#ltoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Lt_OperandType_2](#ltoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Lt_OperandType_3](#ltoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Lt_OperandType_4](#ltoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Lt_OperandType_5](#ltoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Lt_Operand_1](#ltoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Lt_Operand_2](#ltoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Lt_Operand_3](#ltoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Lt_Operand_4](#ltoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Lt_Operand_5](#ltoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Operator_1](#operator)            | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Operator_2](#operator)            | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Operator_3](#operator)            | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Operator_4](#operator)            | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Operator_5](#operator)            | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Rt_OperandType_1](#rtoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Rt_OperandType_2](#rtoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Rt_OperandType_3](#rtoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Rt_OperandType_4](#rtoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Rt_OperandType_5](#rtoperandtype) | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Rt_Operand_1](#rtoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Rt_Operand_2](#rtoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Rt_Operand_3](#rtoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Rt_Operand_4](#rtoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Rt_Operand_5](#rtoperand)         | INT     |          | NO   |     | 0       |       |         |
| [Logic_1](#logic)                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Logic_2](#logic)                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Logic_3](#logic)                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Logic_4](#logic)                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |
| [Logic_5](#logic)                  | TINYINT | UNSIGNED | NO   |     | 0       |       |         |

**Description of the table's fields**

### ID

The row ID. The core uses it as the index of the rows and stores it in `SpellItemEnchantmentConditionEntry::ID`.

### Lt\_OperandType

The core reads these columns into `SpellItemEnchantmentConditionEntry::Color`.

### Lt\_Operand

Not used by the core.

### Operator

The core reads these columns.

### Rt\_OperandType

The core reads these columns into `SpellItemEnchantmentConditionEntry::CompareColor`.

### Rt\_Operand

The core reads these columns into `SpellItemEnchantmentConditionEntry::Value`.

### Logic

Not used by the core.
