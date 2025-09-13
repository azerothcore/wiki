# account\_tutorial

[<-Volver a: Characters](database-characters)

**La tabla \`account\_tutorial\`**

Esta tabla es usada para almacenar el estado de los tutoriales de todas las cuentas.

**Estructura**

| Campo          | Tipo | Atributos | Llave | Nulo | Por defecto | Extra  | Comentario              |
| -------------- | ---- | --------- | ----- | ---- | ----------- | ------ | ----------------------- |
| [accountId][1] | INT  | UNSIGNED  | PRI   | NO   | 0           | Unique | Identificador de cuenta |
| [tut0][2]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut1][3]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut2][4]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut3][5]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut4][6]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut5][7]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut6][8]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |
| [tut7][9]      | INT  | UNSIGNED  |       | NO   | 0           |        |                         |

[1]: #accountid
[2]: #tut0
[3]: #tut1
[4]: #tut2
[5]: #tut3
[6]: #tut4
[7]: #tut5
[8]: #tut6
[9]: #tut7

**Descripción de los campos**

### guid

Cuenta del jugador. Véase [account.id](account#id).

### tut0

`field-no-description|2`

### tut1

`field-no-description|3`

### tut2

`field-no-description|4`

### tut3

`field-no-description|5`

### tut4

`field-no-description|6`

### tut5

`field-no-description|7`

### tut6

`field-no-description|8`

### tut7

Sin valores de 32bits flags. Entonces, 8 x valores de 32bits da como resultado 256 bits disponibles para almacenar 256 mensajes de estado de los tutoriales.

Cada bit significa:

- 0 - Sin mostrar aún
- 1 - Mostrado

Esto es usado para mostrar solo tutoriales que el personaje no ha visto ya.

Desmarcar la opción "Mostrar tutoriales" dentro del juego hace que todos los bits se conviertan en Mostrado. Así, todas las columnas van a contener 11111111111111111111111111111111 binario = 4294967295 en decimal después de que esta opción haya sido cambiada.
