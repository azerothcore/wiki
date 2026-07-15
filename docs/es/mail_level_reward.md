# mail\_level\_reward

[<-Volver a:World](database-world)

**Tabla \`mail\_level\_reward\`**

En ciertos niveles, recibes un correo con algo de texto.

**Estructura**

| Field               | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [level][1]          | TINYINT   | UNSIGNED   | PRI | NO   | 0       |       |         |
| [raceMask][2]       | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [mailTemplateId][3] | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |
| [senderEntry][4]    | MEDIUMINT | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #level
[2]: #racemask
[3]: #mailtemplateid
[4]: #senderentry

**Descripción de los campos**

### level

Nivel requerido para recibir un correo concreto

### raceMask

Máscara requerida para recibir el correo.
`:ChrRaces.dbc`

### mailTemplateId

ID del correo a enviar. Ver [MailTemplate.dbc](mailtemplate)

### senderEntry

El ID de entry de la creature del NPC que envía el correo de recompensa. Ver [creature_template.entry](creature_template#entry).
