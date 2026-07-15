# creature\_addon

[<-Volver a: World](database-world)

**Tabla \`creature\_addon\`**

Las tablas creature\_addon y creature\_template\_addon definen distintas cosas que se aplican a las criaturas cuando se cargan. Estas "distintas cosas" pueden ser, por ejemplo, hacer que la criatura vaya montada, que haga un emote, que muestre un efecto de aura, etc. Mediante el uso de los campos de esta tabla se pueden cambiar muchas cosas sobre la apariencia visual externa de la criatura. La tabla creature\_template\_addon afecta a todas las criaturas con ese ID de plantilla de criatura, mientras que la tabla creature\_addon afecta a criaturas generadas individualmente (de modo que dos criaturas que usan la misma plantilla puedan verse diferentes).

NOTA: un registro de creature\_addon sobrescribirá a un registro de creature\_template\_addon si se solapan en la misma criatura.

AVISO: los datos de esta tabla están en gran parte incompletos y son en su mayoría una simple repetición de lo que el cliente recibe del servidor. Este artículo es un WIP en cuanto a cuáles son todos los valores posibles.

**Estructura**

| Field                        | Type          | Attributes | Key | Null | Default | Extra | Comment |
| ---------------------------- | ------------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid/entry][1]              | INT/MEDIUMINT | UNSIGNED   | PRI | NO   |         |       |         |
| [path_id][2]                 | INT           | UNSIGNED   |     | NO   |         |       |         |
| [mount][3]                   | MEDIUMINT     | UNSIGNED   |     | NO   |         |       |         |
| [bytes1][4]                  | INT           | UNSIGNED   |     | NO   |         |       |         |
| [bytes2][5]                  | INT           | UNSIGNED   |     | NO   |         |       |         |
| [emote][6]                   | INT           | UNSIGNED   |     | NO   |         |       |         |
| [aiAnimKit][7]               | SMALLINT      | SIGNED     |     | NO   |         |       |         |
| [movementAnimKit][8]         | SMALLINT      | SIGNED     |     | NO   |         |       |         |
| [meleeAnimKit][9]            | SMALLINT      | SIGNED     |     | NO   |         |       |         |
| [visibilityDistanceType][10] | TINYINT       | UNSIGNED   |     | NO   |         |       |         |
| [auras][11]                  | text          |            |     | YES  |         |       |         |

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

Para creature\_addon, este campo indica un guid de criatura único. Afectará solo a la criatura cuyo GUID coincida con el especificado aquí.
Para creature\_template\_addon, este campo indica el [creature\_template.entry](creature_template#entry). Afectará a todas las criaturas generadas que usen ese entry de plantilla.

### path\_id

Si una criatura tiene movimiento por waypoints, este campo contiene el waypoint\_data.id de la ruta que la criatura debe seguir.

### mount

El ID de modelo de la montura que se usará para que la criatura aparezca montada. El valor de aquí sobrescribe el valor del campo de unidad UNIT\_FIELD\_MOUNTDISPLAYID de la criatura.

### bytes1

El valor de aquí sobrescribe el valor del campo de unidad UNIT\_FIELD\_BYTES\_1 de la criatura.

Lista de valores conocidos y sus efectos visuales en la criatura:

- 1 = Sentado
- 2 = Sentado en silla
- 3 = Dormido
- 4 = Sentado en silla baja
- 5 = Sentado en silla media
- 6 = Sentado en silla alta
- 7 = Muestra la barra de vida vacía (combínalo con el emote de estado muerto para que una criatura parezca muerta)
- 8 = Hace que el mob se arrodille
- 9 = Sumerge a la criatura bajo el suelo
- 54432 = Modo flotación (Hover)
- 50331648 = Modo flotación 2

### bytes2

El valor de aquí sobrescribe el valor del campo de unidad UNIT\_FIELD\_BYTES\_2 de la criatura.

NOTA: //las criaturas siempre tienen el arma cuerpo a cuerpo lista, si tienen alguna, salvo que se especifique lo contrario

Lista de algunos valores conocidos y sus efectos visuales en la criatura:

- 0 = STATE\_UNARMED (arma no preparada, armas a los lados/espalda)
- 1 = STATE\_MELEE (arma cuerpo a cuerpo preparada en las manos)
- 2 = STATE\_RANGED (arma a distancia preparada en las manos, armas cuerpo a cuerpo a los lados)

### emote

ID de emote que la criatura debería realizar de forma continua.

La lista de IDs de emote más usados y lo que hacen se puede encontrar [aquí](emotes).

### aiAnimKit / movementAnimKit / meleeAnimKit

ID de AnimKit de AnimKit.db2 que se aplica a la criatura al generarse.

### visibilityDistanceType

Este campo controla la distancia de visibilidad de las criaturas:

- Normal = 0,  100.0f  // distancia visible por defecto, 100 yardas en continentes
- Tiny = 1,  25.0f
- Small = 2,  50.0f
- Large = 3, 200.0f
- Gigantic = 4, 400.0f
- Infinite = 5, SIZE_OF_GRIDS // distancia máxima para objetos visibles)

### auras

Este campo controla cualquier aura que se aplique a la criatura (tanto en efecto como visualmente). Para aplicar varias auras, puedes añadir más entradas de aura, separando cada entrada con un espacio. Recuerda que si un hechizo aplica varias auras.

Lista de entradas de aura útiles (ejemplos):

- '16380' - Hace invisible a la criatura.
- '18950' - Hace que la criatura detecte a otras unidades invisibles (jugadores o criaturas).
- '16380 18950' - Ambas auras de arriba
