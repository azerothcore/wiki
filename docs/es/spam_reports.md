# spam\_reports

[<-Volver a:Characters](database-characters)

**Tabla `spam_reports`**

Esta tabla almacena los reportes de spam enviados por los jugadores dentro del juego (p. ej. reportar spam en el chat, el correo o el calendario). El registro (logging) de los reportes de spam se puede activar mediante la opción `LogSpamReports` de `worldserver.conf`.

**Estructura**

| Field                                           | Type     | Attributes | Key | Null | Default | Extra          | Comment                              |
| ----------------------------------------------- | -------- | ---------- | --- | ---- | ------- | -------------- | ------------------------------------ |
| [ID](#id)                                       | INT      | UNSIGNED   | PRI | NO   |         | AUTO_INCREMENT | Unique identifier                    |
| [SpamType](#spamtype)                           | TINYINT  | UNSIGNED   |     | NO   |         |                | 0 = mail, 1 = chat, 2 = calendar     |
| [SpammerGuid](#spammerguid)                     | INT      | UNSIGNED   |     | NO   | 0       |                | GUID of the reported player          |
| [Unk1](#unk1)                                   | INT      | UNSIGNED   |     | YES  | 0       |                |                                      |
| [MailIdOrMessageType](#mailidormessagetype)     | INT      | UNSIGNED   |     | YES  | 0       |                | Mail ID or message type              |
| [ChannelId](#channelid)                         | INT      | UNSIGNED   |     | YES  | NULL    |                | Only used if SpamType = 1 (chat)     |
| [SecondsSinceMessage](#secondssincemessage)     | INT      | UNSIGNED   |     | YES  | NULL    |                | Only used if SpamType = 1 (chat)     |
| [Description](#description)                    | LONGTEXT |            |     | YES  | NULL    |                | Description or context of the report |
| [Time](#time)                                   | INT      | SIGNED     |     | YES  | NULL    |                | Time of report as Unix timestamp     |

**Descripción de los campos**

### ID

El identificador único del reporte de spam. Este número se incrementa automáticamente.

### SpamType

El tipo de spam que se reporta:

- 0 = Correo
- 1 = Chat
- 2 = Calendario

### SpammerGuid

El GUID del jugador reportado por spam. Ver [characters.guid](characters#guid).

### Unk1

Campo desconocido. Reservado para uso futuro.

### MailIdOrMessageType

Para los reportes de correo (SpamType = 0): el ID del correo infractor.
Para los reportes de chat (SpamType = 1): el tipo de mensaje.

### ChannelId

El ID del canal de chat en el que ocurrió el spam. Solo se usa cuando SpamType = 1 (chat).

### SecondsSinceMessage

El número de segundos transcurridos desde que se envió el mensaje reportado. Solo se usa cuando SpamType = 1 (chat).

### Description

Una descripción o contexto adicional proporcionado por el reporte (p. ej. el ID del evento para los reportes de calendario).

### Time

El timestamp Unix de cuándo se envió el reporte de spam.
