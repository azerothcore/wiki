# item\_instance

[<-Volver a: Item Instance](item_instance)

**El campo \`item\_instance\enchantments\`**

Este campo es en realidad una tabla en sí mismo.

Son 36 números separados por un espacio.

Cada número forma parte de una tupla de tres partes numéricas que representa un encantamiento aplicado al objeto.

- Primer número de la tupla

    Id en SpellItemEnchantment.dbc

- Segundo número de la tupla

    Duración del encantamiento (opcional - usado por algunos hechizos)

- Tercer número de la tupla

    Cargas (opcional - usado por algunos hechizos)

Cada conjunto ordinal de 3 Id se usa para un propósito distinto.

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
  Este encantamiento forma parte del diseño del objeto.

### TEMP_ENCHANTMENT_SLOT
### SOCK_ENCHANTMENT_SLOT
  Encantamientos aplicados al objeto mediante una profesión, como las ranuras (sockets) de herrería.

### BONUS_ENCHANTMENT_SLOT        
### PRISMATIC_ENCHANTMENT_SLOT    
### PROP_ENCHANTMENT_SLOT       
  Encantamientos aleatorios que algunos objetos reciben al ser creados.

  Estas ranuras dependen o bien de un sufijo aleatorio o del RandomProperty en [item_template](item_template).

  Si se aplicó un sufijo aleatorio cuando se creó la instancia, entonces se basa en la tabla [item_enchantment_template](item_enchantment_template). La tabla Item Enchantment template proporciona los distintos sufijos aleatorios que podrían aplicarse a un objeto dado junto con el porcentaje de probabilidad de que se apliquen.

  Una vez seleccionado un encantamiento, los valores de ItemRandomSuffix.dbc se usan para determinar cuán fuerte es el encantamiento en la ranura especificada.

  Si se coloca un encantamiento en una de estas 5 ranuras pero no hay un AllocationPct_# coincidente en el dbc ItemRandom_Suffix, entonces el encantamiento no tendrá efecto sobre el objeto.
