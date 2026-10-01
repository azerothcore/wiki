# quest\_poi\_points

[<-Volver a: World](database-world)

**Tabla \`quest\_poi\_points\`**

Proviene de sniffs. Visualmente hablando, esta tabla se usa para identificar las coordenadas X e Y en el mapa (no el minimapa, el mapa principal) donde debe aparecer el signo de interrogación de una misión. Usa el comando ".gps" donde estés parado para encontrar estas coordenadas. Para ver los cambios, usa ".reload quest\_poi", cierra Wow.exe y luego borra tu carpeta de caché.

**Estructura**

| Field              | Type     | Attributes | Key | Null | Default | Extra | Comment |
| ------------------ | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [questid][1]       | INT      | unasigned  | PRI | NO   | 0       |       |         |
| [idx2][2]          | INT      | unasigned  | PRI | NO   | 0       |       |         |
| [x][3]             | INT      | unasigned  |     | NO   | 0       |       |         |
| [y][4]             | INT      | unasigned  |     | NO   | 0       |       |         |
| [VerifiedBuild][5] | SMALLINT | unasigned  |     | YES  | NULL    |       |         |

[1]: #questid
[2]: #idx2
[3]: #x
[4]: #y
[5]: #verifiedbuild

**Descripción de los campos**

### questid

El ID de misión de [quest\_poi.questid](quest_poi#questid)

### idx1

Se usa para agrupar múltiples entradas de quest\_poi.id. Debes incrementar manualmente este valor en 1 por cada nueva fila en quest\_poi\_point con el mismo questId (0, 1, 2, 3...).

### idx2

Se usa para agrupar múltiples entradas en los quest poi points para dibujar el polígono de ese punto de interés. Los puntos reales son las esquinas de cada polígono.

Misión de ejemplo: Secreat Communication.

| QuestID | idx1 | idx2 | x     | y    | VerifiedBuild |
| ------- | ---- | ---- | ----- | ---- | ------------- |
| 8318    | 3    | 0    | -6231 | -51  | 0             |
| 8318    | 3    | 1    | -6236 | -19  | 0             |
| 8318    | 3    | 2    | -6241 | -52  | 0             |
| 8318    | 3    | 3    | -6316 | -282 | 0             |
| 8318    | 3    | 4    | -6413 | -282 | 0             |
| 8318    | 3    | 5    | -6483 | -250 | 0             |
| 8318    | 3    | 6    | -6483 | -217 | 0             |
| 8318    | 3    | 7    | -6326 | -7   | 0             |

**Estos puntos son todas las pequeñas esquinas de la caja azul. idx1 representa un área definida por los puntos de idx2 para dibujar la forma.**

![image](https://user-images.githubusercontent.com/1884642/119476187-bca11b00-bd45-11eb-95e5-876960f24457.png)

### x

La posición X del signo de interrogación en el mapa.

### y

La posición Y del signo de interrogación en el mapa.

### VerifiedBuild

VerifiedBuild
