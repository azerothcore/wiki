# spell\_enchant\_proc\_data

[<-Back-to:World](database-world)

**The \`spell\_enchant\_proc\_data\` table**

Changes how often and when weapon enchantments proc their spell.

**Table: spell\_enchant\_proc\_data's Structure**

| Field              | Type  | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | ----- | ---------- | --- | ---- | ------- | ----- | ------- |
| [entry][1]         | INT   | UNSIGNED   | PRI | NO   |         |       |         |
| [customChance][2]  | INT   | UNSIGNED   |     | NO   | 0       |       |         |
| [PPMChance][3]     | FLOAT | SIGNED     |     | NO   | 0       |       |         |
| [procEx][4]        | INT   | UNSIGNED   |     | NO   | 0       |       |         |
| [attributeMask][5] | INT   | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #entry
[2]: #customchance
[3]: #ppmchance
[4]: #procex
[5]: #attributemask

**Description of the table's fields**

### entry

Enchantment ID from SpellItemEnchantment.dbc

### customChance

Proc chance in percent. Overrides the chance from the enchantment. 0 to not change it.

### PPMChance

Value must be >=0. If the value does not meet the condition the SQL will fail on `spell_enchant_proc_data_chk_1`.

### procEx

If set, the enchantment only procs on hits that match one of these hit results (`PROC_EX_*` flags, for example a normal hit or a critical hit). If 0, it procs on any hit that does damage.

### attributeMask

| Flag | Name                        | Description                                                     |
| ---- | --------------------------- | --------------------------------------------------------------- |
| 1    | ENCHANT_PROC_ATTR_EXCLUSIVE | Does not proc while the target already has the aura from the caster. |
| 2    | ENCHANT_PROC_ATTR_WHITE_HIT | Only procs from white hits, not from abilities.                 |
