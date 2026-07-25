# areatrigger

[<-Volver a:World](database-world)

**Tabla \`areatrigger\`**

Esta tabla contiene los puntos de activación (triggers) de eventos en ciertas coordenadas de los mapas.

[Cómo importar datos DBC a mi base de datos](how-to-import-dbc-data-in-db)

**Estructura**

| Field       | Type  | Attributes | Key | Null | Default | Extra          | Comment                                              |
| ----------- | ----- | ---------- | --- | ---- | ------- | -------------- | ---------------------------------------------------- |
| entry       | INT   | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT |                                                      |
| map         | INT   | UNSIGNED   |     | NO   | 0       |                |                                                      |
| x           | FLOAT |            |     | NO   | 0       |                |                                                      |
| y           | FLOAT |            |     | NO   | 0       |                |                                                      |
| z           | FLOAT |            |     | NO   | 0       |                |                                                      |
| radius      | FLOAT |            |     | NO   | 0       |                | Parece ser una caja de tamaño en yardas con centro en x,y,z |
| length      | FLOAT |            |     | NO   | 0       |                | Se usa más comúnmente cuando size es 0, pero no siempre |
| width       | FLOAT |            |     | NO   | 0       |                | Se usa más comúnmente cuando size es 0, pero no siempre |
| height      | FLOAT |            |     | NO   | 0       |                | Se usa más comúnmente cuando size es 0, pero no siempre |
| orientation | FLOAT |            |     | NO   | 0       |                | Se usa más comúnmente cuando size es 0, pero no siempre |

**Descripción de los campos**

### Entry

Este es simplemente un contador automático que asigna un valor a cada trigger para listarlo.

### Map

Este campo evoca un mapa concreto según el ID (por ejemplo, el ID 30 evoca Elwynn Forest)

### X, Y and Z

Contiene las coordenadas de las tres dimensiones 3d.

### Radius

Este contiene el radio de activación del trigger.

### Length, Width, Height and Orientation

estos campos contienen los valores de la física y el comportamiento de un trigger dado.

### Example

| entry | map | x        | y        | z       | radius | length | width | height | orientation |
| ----- | --- | -------- | -------- | ------- | ------ | ------ | ----- | ------ | ----------- |
| 45    | 0   | 2924.38  | -798.429 | 161.611 | 8      | 0      | 0     | 0      | 0           |
| 71    | 0   | -10645.9 | 1179.06  | 48.1781 | 27     | 0      | 0     | 0      | 0           |
| 78    | 0   | -11208.5 | 1685.34  | 25.7612 | 7      | 0      | 0     | 0      | 0           |
| 84    | 0   | 16449.9  | 16393.2  | 69.4444 | 15     | 0      | 0     | 0      | 0           |
| 87    | 0   | -9077.34 | -552.925 | 60.3476 | 30     | 0      | 0     | 0      | 0           |
