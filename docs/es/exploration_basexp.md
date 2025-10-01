# exploration_basexp

[<-Volver a:World](database-world)

Esta tabla contiene la información de puntos de experiencia base necesarios cuando un jugador explora una nueva zona.

| Campo       | Tipo      | Atributos | Llave | Nulo | Por defecto |
| ----------- | --------- | --------- | ----- | ---- | ----------- |
| [level][1]  | TINYINT   | UNSIGNED  | PRI   | NO   | 0           |
| [basexp][2] | MEDIUMINT | SIGNED    |       | NO   | 0           |

[1]: #level
[2]: #basexp

**Descripción de los campos**

### level
El nivel del jugador.

### basexp
La experiencia base que recibirá el jugador cuando descubra una nueva zona en el nivel especificado en el campo de nivel.
