# guild\_bank\_item

[<-Volver a:Characters](database-characters.md)

**Tabla \`guild\_bank\_item\`**

La tabla alberga toda la información de aquellos Items que se almacenan en el banco de la hermandad.

**Estructura**

| Field          | Type    | Attributes | Key | Null | Default | Extra | Comment |
| -------------- | ------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [guildid][1]   | INT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TabId][2]     | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [SlotId][3]    | TINYINT | UNSIGNED   | PRI | NO   | 0       |       |         |
| [item_guid][4] | INT     | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #guildid
[2]: #tabid
[3]: #slotid
[4]: #itemguid

**Descripción de los Campos**

### guildid

ID de la hermandad que posee el banco. Véase [guild.guildid](guild#guildid).

### TabId

ID de la pestaña en la que actualmente se encuentra el Item. Véase [guild\_bank\_tab.TabId](guild_bank_tab#tabid).

### SlotId

ID de la ranura en la que el Item correspondiente se halla almacenado en la pestaña.

### item\_guid

GUID o Identificador Global Único del Item correspondiente. Véase [item\_instance.guid](item_instance#guid).
