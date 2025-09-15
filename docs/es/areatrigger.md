# areatrigger

[<-Voler a:World](database-world)

**La \`areatrigger\` tabla**

Esta tabla contiene puntos de activación de eventos en determinadas coordenadas de los mapas.

[Cómo importar datos DBC a mi base de datos](how-to-import-dbc-data-in-db)

**Table Structure**

| Campo       | Tipo  | Atributos | Llave | Nulo | Por defecto | Extra          | Comentario                                                              |
| ----------- | ----- | --------- | ----- | ---- | ----------- | -------------- | ----------------------------------------------------------------------- |
| entry       | INT   | UNSIGNED  | PRI   | NO   |             | AUTO_INCREMENT |                                                                         |
| map         | INT   | UNSIGNED  |       | NO   | 0           |                |                                                                         |
| x           | FLOAT |           |       | NO   | 0           |                |                                                                         |
| y           | FLOAT |           |       | NO   | 0           |                |                                                                         |
| z           | FLOAT |           |       | NO   | 0           |                |                                                                         |
| radius      | FLOAT |           |       | NO   | 0           |                | Parece ser una caja de tamaño yardas con centro en x,y,z                |
| length      | FLOAT |           |       | NO   | 0           |                | Se utiliza con mayor frecuencia cuando el tamaño es 0, pero no siempre. |
| width       | FLOAT |           |       | NO   | 0           |                | Se utiliza con mayor frecuencia cuando el tamaño es 0, pero no siempre. |
| height      | FLOAT |           |       | NO   | 0           |                | Se utiliza con mayor frecuencia cuando el tamaño es 0, pero no siempre. |
| orientation | FLOAT |           |       | NO   | 0           |                | Se utiliza con mayor frecuencia cuando el tamaño es 0, pero no siempre. |

**Descripción de los campos**

### Entry

Este es simplemente un contador automático que asigna un valor a cada disparador para enumerarlo.

### Map

Este campo recuerda un mapa determinado en función del ID (por ejemplo, el ID 30 recuerda Elwynn Forest)

### X, Y and Z

Contiene las coordenadas de las tres dimensiones 3D.

### Radius

Esto contiene el radio de activación del disparador.

### Length, Width, Height and Orientation

Estos campos contienen los valores de la física y el comportamiento de un disparador determinado.

### Ejemplo

| entry | map | x        | y        | z       | radius | length | width | height | orientation |
| ----- | --- | -------- | -------- | ------- | ------ | ------ | ----- | ------ | ----------- |
| 45    | 0   | 2924.38  | -798.429 | 161.611 | 8      | 0      | 0     | 0      | 0           |
| 71    | 0   | -10645.9 | 1179.06  | 48.1781 | 27     | 0      | 0     | 0      | 0           |
| 78    | 0   | -11208.5 | 1685.34  | 25.7612 | 7      | 0      | 0     | 0      | 0           |
| 84    | 0   | 16449.9  | 16393.2  | 69.4444 | 15     | 0      | 0     | 0      | 0           |
| 87    | 0   | -9077.34 | -552.925 | 60.3476 | 30     | 0      | 0     | 0      | 0           |
