# account\_data

[<-Volver a: Characters](database-characters.md)

**La tabla \`account\_data\`**

Contiene información sobre las cuentas y configuraciones.

**Estructura**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment            |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------------------ |
| [accountId][1] | INT     | UNSIGNED   | PRI | NO   | 0       |       | Account Identifier |
| [type][2]      | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |                    |
| [time][3]      | INT     | UNSIGNED   |     | NO   | 0       |       |                    |
| [data][4]      | BLOB    | SIGNED     |     | NO   |         |       |                    |

[1]: #accountid
[2]: #type
[3]: #time
[4]: #data

**Descripción de los campos**

### accountId

El [account.id](account#id).

### type

| Value | Description                   |
| ----- | ----------------------------- |
| 0     | Global-account config cache   |
| 2     | Global-account bindings cache |
| 4     | Global-account macros cache   |

### time

Tiempo de la última modificación en Unixtime.

### data

No es posible escribir uan descripción. Usted simplemente tiene que enteder su información.
