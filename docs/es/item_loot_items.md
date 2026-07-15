# item\_loot\_items

[<-Volver a: Characters](database-characters)

**Tabla \`item\_loot\_items\`**

Contiene los objetos asociados a un objeto de inventario saqueable como un "watertight trunk" o una "Bulging Sack of Gems".

Esta tabla se rellena la primera vez que el jugador hace click derecho para abrir un objeto. Las filas se eliminan cuando
el jugador retira un objeto o destruye el objeto contenedor.

**Estructura**

| Field                | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [container_id][1]    | INT     | UNSIGNED   |     | NO   |         |       |         |
| [item_id][2]         | INT     | UNSIGNED   |     | NO   |         |       |         |
| [item_count][3]      | INT     |            |     | NO   |         |       |         |
| [follow_rules][4]    | TINYINT |            |     | NO   |         |       |         |
| [ffa][5]             | TINYINT |            |     | NO   |         |       |         |
| [blocked][6]         | TINYINT |            |     | NO   |         |       |         |
| [counted][7]         | TINYINT |            |     | NO   |         |       |         |
| [under_threshold][8] | TINYINT |            |     | NO   |         |       |         |
| [needs_quest][9]     | TINYINT |            |     | NO   |         |       |         |
| [rnd_prop][10]       | INT     |            |     | NO   |         |       |         |
| [rnd_suffix][11]     | INT     |            |     | NO   |         |       |         |

[1]: #container_id
[2]: #item_id
[3]: #item_count
[4]: #follow_rules
[5]: #ffa
[6]: #blocked
[7]: #counted
[8]: #under_threshold
[9]: #needs_quest
[10]: #rnd_prop
[11]: #rnd_suffix

**Descripción de los campos**

### container\_id

El GUID del objeto contenedor que aloja el/los objeto(s) de botín. Ver item\_instance.guid

Nota: Un [container\_id](#item_loot_items-container_id) puede tener más de un [item\_id](#item_loot_items-item_id) asociado.

### item\_id

El entry del objeto de botín. Ver item\_instance.itemEntry

Nota: Es posible que haya más de una unidad del mismo objeto en un contenedor.

### item\_count

El tamaño de pila (stack) del objeto. Solo los objetos apilables pueden ser &gt; 1.

### follow\_rules

Flag para determinar si el core debe aplicar reglas de botín adicionales cuando el objeto
se retira del contenedor.

### ffa

Flag para determinar si se aplica el saqueo libre para todos (free-for-all). Normalmente esto debería ser 0 porque los objetos están dentro de

un objeto en el inventario del personaje.

### blocked

`campo-sin-descripción|6`

### counted

`campo-sin-descripción|6`

### under\_threshold

`campo-sin-descripción|6`

### needs\_quest

Flag para determinar si el objeto es un objeto de misión que debe contarse como "quest drop".

### rnd\_prop

El encantamiento aleatorio (si lo hay) que se lanzó y se añadió al objeto cuando el contenedor de botín se
abrió originalmente.

Por ejemplo: "Ebon Scimitar" (en contraposición a un simple "Scimitar").

### rnd\_suffix

El sufijo aleatorio (si lo hay) que se lanzó y se añadió al objeto cuando el contenedor de botín se
abrió originalmente.

Por ejemplo: "of the Monkey"
