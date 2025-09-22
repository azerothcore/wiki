# creature\_addon

[<-Volver a:World](database-world)

**Tabla \`creature\_addon\`**

Las tablas creature\_addon y creature\_template\_addon definen diferentes funciones que se aplican a las criaturas al cargarlas. Estas funciones pueden ser, por ejemplo, que la criatura esté montada, que muestre algún gesto, que muestre un efecto de aura, etc. Mediante el uso de los campos de esta tabla, se pueden modificar muchos aspectos de la apariencia visual de la criatura. La tabla creature\_template\_addon afecta a todas las criaturas con ese ID de plantilla, mientras que la tabla creature\_addon afecta a las criaturas generadas individualmente (de modo que dos criaturas que usan la misma plantilla pueden tener un aspecto diferente).

NOTA: Un registro de creature\_complemento anulará un registro de creature\_template\_complemento si se superponen en la misma criatura.

AVISO: Los datos de esta tabla están en gran parte incompletos y son, en su mayoría, una simple repetición de lo que el cliente recibe del servidor. Este artículo es un trabajo en curso sobre cuáles son todos los valores posibles.

**Estructura**

| Campo                        | Tipo          | Atributos | Llave | Nulo | Por defecto | Extra | Comentario |
| ---------------------------- | ------------- | --------- | ----- | ---- | ----------- | ----- | ---------- |
| [guid/entry][1]              | INT/MEDIUMINT | UNSIGNED  | PRI   | NO   |             |       |            |
| [path_id][2]                 | INT           | UNSIGNED  |       | NO   |             |       |            |
| [mount][3]                   | MEDIUMINT     | UNSIGNED  |       | NO   |             |       |            |
| [bytes1][4]                  | INT           | UNSIGNED  |       | NO   |             |       |            |
| [bytes2][5]                  | INT           | UNSIGNED  |       | NO   |             |       |            |
| [emote][6]                   | INT           | UNSIGNED  |       | NO   |             |       |            |
| [aiAnimKit][7]               | SMALLINT      | SIGNED    |       | NO   |             |       |            |
| [movementAnimKit][8]         | SMALLINT      | SIGNED    |       | NO   |             |       |            |
| [meleeAnimKit][9]            | SMALLINT      | SIGNED    |       | NO   |             |       |            |
| [visibilityDistanceType][10] | TINYINT       | UNSIGNED  |       | NO   |             |       |            |
| [auras][11]                  | text          |           |       | YES  |             |       |            |

[1]: #guid/entry
[2]: #path_id
[3]: #mount
[4]: #bytes1
[5]: #bytes2
[6]: #emote
[7]: #aianimkit
[8]: #movementanimkit
[9]: #meleeanimkit
[10]: #visibilityDistanceType
[11]: #auras

**Descripción de los campos**

### guid/entry

Para creature\_addon, este campo indica un GUID de criatura único. Afectará únicamente a la criatura cuyo GUID coincida con el especificado aquí.
Para creature\_template\_complemento, este campo representa la [creature\_template.entry](creature_template#creature_template-entry). Afectará a todas las criaturas generadas que usen esa entrada de plantilla.

### path\_id

Si una criatura tiene un punto de ruta de movimiento, este campo contiene el waypoint\_data.id para la ruta que debe seguir la criatura.

### mount

El ID del modelo de la montura que se usará para que la criatura parezca montada. Este valor anula el valor del campo de unidad de la criatura: UNIT\_FIELD\_MOUNTDISPLAYID.

### bytes1

El valor aquí anula el valor del campo de unidad de la criatura UNIT\_FIELD\_BYTES\_1.

Lista de valores conocidos y cuáles son sus efectos visuales en la criatura.

- 1 = Sentado
- 2 = Sentado en silla
- 3 = Dormido
- 4 = Sentado en silla baja
- 5 = Sentado en silla mediana
- 6 = Sentado en silla alta
- 7 = Muestra la barra de salud vacía (combina con el gesto de estado muerto para que la criatura parezca muerta)
- 8 = Hace que el monstruo se arrodille
- 9 = Sumerge a la criatura bajo tierra
- 54432 = Modo flotante
- 50331648 = Modo flotante 2

### bytes2

El valor aquí anula el valor del campo de unidad de la criatura UNIT\_FIELD\_BYTES\_2.

NOTA: //las criaturas siempre tienen un arma cuerpo a cuerpo lista, si la tienen, a menos que se especifique lo contrario

Lista de algunos valores conocidos y cuáles son sus efectos visuales en la criatura.

- 0 = STATE\_UNARMED (arma no preparada, armas a los lados/atrás)
- 1 = STATE\_MELEE A CUERPO (arma cuerpo a cuerpo preparada en las manos)
- 2 = STATE\_RANGED (arma a distancia preparada en las manos, armas cuerpo a cuerpo a los lados)

### emote

Identificación del gesto que la criatura debe realizar continuamente.

La lista de identificaciones de emoticonos frecuentemente usados ​​y lo que hacen se puede encontrar [aquí] (Emotes).

### aiAnimKit / movementAnimKit / meleeAnimKit

ID de AnimKit de AnimKit.db2 que se aplica a la criatura cuando se genera.

### visibilityDistanceType

Este campo controla la distancia de visibilidad de las criaturas:

- Normal = 0, 100.0f // distancia visible predeterminada, 100 yardas en continentes
- Diminuto = 1, 25.0f
- Pequeño = 2, 50.0f
- Grande = 3, 200.0f
- Gigantesco = 4, 400.0f
- Infinito = 5, SIZE_OF_GRIDS // distancia máxima para objetos visibles)

### auras

Este campo controla las auras que se aplicarán a la criatura (tanto en efecto como visualmente). Para aplicar varias auras, puedes añadir más entradas, separándolas con un espacio. Recuerda que si un hechizo aplica varias auras...

Lista de entradas de aura útiles (ejemplos):

- '16380' - Hace que la criatura sea invisible.
- '18950' - Hace que la criatura detecte otras unidades invisibles (jugadores o criaturas).
- '16380 18950' - Ambas auras anteriores
