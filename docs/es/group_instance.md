# group\_instance

[<-Volver a: Characters](database-characters)

**Tabla \`group\_instance\`**

`tabla-sin-descripción`

**Estructura**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guid][1]      | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [instance][2]  | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [permanent][3] | TINYINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guid
[2]: #instance
[3]: #permanent

**Descripción de los campos**

### guid

Guid del grupo.

### instance

ID de la sesión de instancia a la que ha entrado el grupo.

### permanent

Flag booleano que indica si el grupo está ligado a la instancia o no.
