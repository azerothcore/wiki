# item\_instance

[<-Back-to:Item Instance](item_instance)

**The \`item\_instance\enchantments` field**

This Field is really a table of its own. 

There are 36 numerics seperated by a space

Each Numeric is part of a three part Tuple of Numerics represents an enchantment as applied to the item.

- First Number in Tuple 
  
    Id in the SpellItemEnchantment.dbc
 
- Second Number in Tuple
    
    Duration of the Enchantment (optional - Used by some spells)
  
- Third Number in Tuple

    Charges (optional - used by some spells) 

Each ordinal set of 3 Id is used for a different purpose.

| Purpose                    | Ordinal |
| -------------------------- | ------- |
| PERM_ENCHANTMENT_SLOT      | 0       |
| TEMP_ENCHANTMENT_SLOT      | 1       |
| SOCK_ENCHANTMENT_SLOT      | 2       |
| SOCK_ENCHANTMENT_SLOT_2    | 3       |
| SOCK_ENCHANTMENT_SLOT_3    | 4       |
| BONUS_ENCHANTMENT_SLOT     | 5       |
| PRISMATIC_ENCHANTMENT_SLOT | 6       |
| PROP_ENCHANTMENT_SLOT_0    | 7       |
| PROP_ENCHANTMENT_SLOT_1    | 8       |
| PROP_ENCHANTMENT_SLOT_2    | 9       |
| PROP_ENCHANTMENT_SLOT_3    | 10      |
| PROP_ENCHANTMENT_SLOT_4    | 11      |

### PERM_ENCHANTMENT_SLOT
  This Enchantment is part of the Items design.
  
### TEMP_ENCHANTMENT_SLOT
### SOCK_ENCHANTMENT_SLOT
  Enchantments applied to the Item via a profession like blacksmithing sockets.
  
### BONUS_ENCHANTMENT_SLOT        
### PRISMATIC_ENCHANTMENT_SLOT    
### PROP_ENCHANTMENT_SLOT       
  Random Enchatments Some Items receive on creation. 
  
  These Slots are dependent on either a Random Suffix or the RandomProperty in [item_template](item_template).   
  
  If a Random Suffix was applied when the instance we created then that is based off of the [item_enchantment_template](item_enchantment_template) table. The Item Enchantment template table gives the different Random Suffixs that might be applied to a given item along with the percent chance that they will be applied.
  
  Once an Enchant is selected then the Values in ItemRandomSuffix.dbc are used to determine how strong the enchantment is in the specified slot. 
  
  If an enchantment is placed in one of these 5 slots but there is no matching AllocationPct_# in the ItemRandom_Suffix dbc then the enchantment will have no effect on the Item.
