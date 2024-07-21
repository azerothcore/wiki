# item\_instance

[<-Volver a:Item Instance](item-instance)

**Tabla \`item\_instance\enchantments`**

Éste Campo también es una tabla como tal. Hay 36 números separados por un espacio y cada número hace parte de una [tupla](https://es.wikipedia.org/wiki/Tupla) de tres partes numéricas que representan un encantamiento aplicado al Item.

- Primer número de la tupla 

    Identificador (ID) extraído desde SpellItemEnchantment.dbc

- Segundo número de la tupla

    Duración del Encantamiento (opcional - Utilizado por algunos hechizos)

- Tercer número de la tupla

    Cargas (opcional - utilizado por algunos hechizos) 

Cada conjunto ordinal de 3 ID's es utilizado para un propósito distinto.

| Objetivo                      | Ordinal |
| ----------------------------- | ------- |
| PERM_ENCHANTMENT_SLOT         | 0       |
| TEMP_ENCHANTMENT_SLOT         | 1       |
| SOCK_ENCHANTMENT_SLOT         | 2       |
| SOCK_ENCHANTMENT_SLOT_2       | 3       |
| SOCK_ENCHANTMENT_SLOT_3       | 4       |
| BONUS_ENCHANTMENT_SLOT        | 5       |
| PRISMATIC_ENCHANTMENT_SLOT    | 6       |                   
| PROP_ENCHANTMENT_SLOT_0       | 7       |                   
| PROP_ENCHANTMENT_SLOT_1       | 8       |                   
| PROP_ENCHANTMENT_SLOT_2       | 9       |                   
| PROP_ENCHANTMENT_SLOT_3       | 10      |                   
| PROP_ENCHANTMENT_SLOT_4       | 11      |        

### PERM_ENCHANTMENT_SLOT

Este encantamiento ya hace parte del Item en cuestión.

### TEMP_ENCHANTMENT_SLOT
### SOCK_ENCHANTMENT_SLOT

Encantamiento aplicado al Item a través de una profesión (como herrería, sastrería o encantamiento por ejemplo).

### BONUS_ENCHANTMENT_SLOT        
### PRISMATIC_ENCHANTMENT_SLOT    
### PROP_ENCHANTMENT_SLOT       

Encantamientos aleatorios que reciben algunos Items al ser creados por el jugador. 

Las ranuras dependen de un sufijo aleatorio, o del campo RandomProperty dentro de [item_template](item_template#randomproperty).   

En caso de que hayamos aplicado un Sufijo Aleatorio cuando la instancia del Item fue creada, entonces ésta se basará en la tabla [item_enchantment_template](item_enchantment_template). La 'Item Enchantment template' o 'Tabla de Plantilla del Encantamiento' del Item otorga diferentes 'Encantamientos Aleatorios' que podrían ser aplicados al Item dado junto con su porcentaje de probabilidad.

Una vez seleccionado el encantamiento, son usados los valores de la tabla [ItemRandom_Suffix](ItemRandom_Suffix) para determinar qué tan fuerte en medida es el encantamiento en cuestión.  Sí el encantamiento es asignado en alguna de las 5 ranuras, pero y sin embargo no haya un AllocationPct (Porcentaje de asignación) que coincida en el .dbc ItemRandom_Suffix, entonces el encantamiento no tendrá ningún tipo deefecto sobre el Item. 
