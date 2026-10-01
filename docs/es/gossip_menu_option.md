# gossip\_menu\_option

**Tabla: gossip\_menu\_option**

Esta tabla contiene información sobre las opciones de menú que puede tener un NPC de gossip. Ejemplos de opciones: "¡Entréname!", "Quiero desaprender mis talentos"

## Estructura

| Field                      | Type      | Attributes | Key | Null | Default | Extra | Comment |
| -------------------------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID][1]                | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionID][2]              | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionIcon][3]            | SMALLINT  | UNSIGNED   | PRI | NO   |         |       |         |
| [OptionText][4]            | text      |            |     | YES  | NULL    |       |         |
| [OptionBroadcastTextID][5] | MEDIUMINT |            |     | NO   |         |       |         |
| [OptionType][6]            | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [OptionNpcFlag][7]         | INT       | UNSIGNED   |     | NO   |         |       |         |
| [ActionMenuID][8]          | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [ActionPoiID][9]           | MEDIUMINT | UNSIGNED   |     | NO   |         |       |         |
| [BoxCoded][10]             | TINYINT   | UNSIGNED   |     | NO   |         |       |         |
| [BoxMoney][11]             | INT       | UNSIGNED   |     | NO   |         |       |         |
| [BoxText][12]              | text      |            |     | YES  | NULL    |       |         |
| [BoxBroadcastTextID][13]   | MEDIUMINT |            |     | NO   |         |       |         |
| [VerifiedBuild][14]        | SMALLINT  |            |     | NO   |         |       |         |

[1]: #menuid
[2]: #optionid
[3]: #optionicon
[4]: #optiontext
[5]: #optionbroadcasttextid
[6]: #optiontype
[7]: #optionnpcflag
[8]: #actionmenuid
[9]: #actionpoiid
[10]: #boxcoded
[11]: #boxmoney
[12]: #boxtext
[13]: #boxbroadcasttextid
[14]: #verifiedbuild

## Descripción de los campos

### MenuID

Entry de gossip de Gossip\_menu.entry con el que está asociada esta opción.
Si esta es la opción de gossip por defecto para el NPC seleccionado, verifica que el NPC tenga este valor en su [creature\_template.gossip\_menu\_id](creature_template#gossipmenuid) .

### OptionID

El id asociado a este gossip\_menu\_option. Debe ser único para un menu\_id dado empezando desde 0 (cero).
El valor se incrementa en 1 si hay varias opciones en el mismo gossip\_menu.

### OptionIcon

| Name                      | ID  | Description                                     |
| ------------------------- | --- | ----------------------------------------------- |
| GOSSIP\_ICON\_CHAT        | 0   | Burbuja de chat blanca                          |
| GOSSIP\_ICON\_VENDOR      | 1   | Bolsa marrón                                    |
| GOSSIP\_ICON\_TAXI        | 2   | Vuelo                                           |
| GOSSIP\_ICON\_TRAINER     | 3   | Libro                                           |
| GOSSIP\_ICON\_INTERACT\_1 | 4   | Rueda de interacción                            |
| GOSSIP\_ICON\_INTERACT\_2 | 5   | Rueda de interacción                            |
| GOSSIP\_ICON\_MONEY\_BAG  | 6   | Bolsa marrón con punto amarillo (oro)           |
| GOSSIP\_ICON\_TALK        | 7   | Burbuja de chat blanca con puntos negros (**...**) |
| GOSSIP\_ICON\_TABARD      | 8   | Tabardo                                         |
| GOSSIP\_ICON\_BATTLE      | 9   | Dos espadas                                     |
| GOSSIP\_ICON\_DOT         | 10  | Punto amarillo                                  |

### OptionText

Este es el texto que quieres que se muestre en la opción seleccionable por el jugador. Ejemplos serían: "Por favor, entréname.", "Me gustaría ver tus productos.", "Aprender doble especialización".
Si OptionBroadcastTextID contiene un broadcast\_text.ID válido, enlaza con broadcast\_text de modo que se muestra directamente el contenido de broadcast\_text en lugar del contenido del campo option\_text.

### OptionBroadcastTextID

El ID del mismo texto en broadcast\_text.ID.

### OptionType

| option_id Name                  | Value | npcflag Name (& comentario)                                                    | npcflag value |
| ------------------------------- | ----- | --------------------------------------------------------------------------- | ------------- |
| GOSSIP_OPTION_NONE              | 0     | UNIT_NPC_FLAG_NONE                                                          | 0             |
| GOSSIP_OPTION_GOSSIP            | 1     | UNIT_NPC_FLAG_GOSSIP                                                        | 1             |
| GOSSIP_OPTION_QUESTGIVER        | 2     | UNIT_NPC_FLAG_QUESTGIVER                                                    | 2             |
| GOSSIP_OPTION_VENDOR            | 3     | UNIT_NPC_FLAG_VENDOR (Asegúrate de que haya datos de npc_vendor para esta creature) | 128           |
| GOSSIP_OPTION_TAXIVENDOR        | 4     | UNIT_NPC_FLAG_TAXIVENDOR                                                    | 8192          |
| GOSSIP_OPTION_TRAINER           | 5     | UNIT_NPC_FLAG_TRAINER (Recuerda establecer un (TrainerId, CreatureId) en creature_default_trainer)  | 16            |
| GOSSIP_OPTION_SPIRITHEALER      | 6     | UNIT_NPC_FLAG_SPIRITHEALER                                                  | 16384         |
| GOSSIP_OPTION_SPIRITGUIDE       | 7     | UNIT_NPC_FLAG_SPIRITGUIDE                                                   | 32768         |
| GOSSIP_OPTION_INNKEEPER         | 8     | UNIT_NPC_FLAG_INNKEEPER                                                     | 65536         |
| GOSSIP_OPTION_BANKER            | 9     | UNIT_NPC_FLAG_BANKER                                                        | 131072        |
| GOSSIP_OPTION_PETITIONER        | 10    | UNIT_NPC_FLAG_PETITIONER                                                    | 262144        |
| GOSSIP_OPTION_TABARDDESIGNER    | 11    | UNIT_NPC_FLAG_TABARDDESIGNER                                                | 524288        |
| GOSSIP_OPTION_BATTLEFIELD       | 12    | UNIT_NPC_FLAG_BATTLEFIELDPERSON                                             | 1048576       |
| GOSSIP_OPTION_AUCTIONEER        | 13    | UNIT_NPC_FLAG_AUCTIONEER                                                    | 2097152       |
| GOSSIP_OPTION_STABLEPET         | 14    | UNIT_NPC_FLAG_STABLE                                                        | 4194304       |
| GOSSIP_OPTION_ARMORER           | 15    | UNIT_NPC_FLAG_ARMORER (no usado)                                           | 4096          |
| GOSSIP_OPTION_UNLEARNTALENTS    | 16    | UNIT_NPC_FLAG_TRAINER (opción extra para GOSSIP_OPTION_TRAINER)             | 16            |
| GOSSIP_OPTION_UNLEARNPETTALENTS | 17    | UNIT_NPC_FLAG_TRAINER (opción extra para GOSSIP_OPTION_TRAINER)             | 16            |
| GOSSIP_OPTION_LEARNDUALSPEC     | 18    | UNIT_NPC_FLAG_TRAINER (opción extra para GOSSIP_OPTION_TRAINER)             | 16            |
| GOSSIP_OPTION_OUTDOORPVP        | 19    | Añadido por código (opción para creatures de PvP al aire libre)             |               |
| GOSSIP_OPTION_MAX               |       |                                                                             |               |


### OptionNpcFlag

Este es el npcflag ([Creature\_template.npcflag](creature_template#npcflag) que el NPC debe tener para que se muestre esta opción. Ver los comentarios (después de //) en la tabla anterior)

### ActionMenuID

Si quieres crear un submenú, este es el ID ([gossip\_menu.entry](gossip_menu#entry) / [gossip\_menu\_option.menu\_id](gossip_menu_option#menuid)) con el que enlazar para crear ese submenú.

### ActionPoiID

Si quieres que se muestre un POI (punto de interés) en el minimapa (como cuando un guardia de la ciudad coloca un marcador al pedirle indicaciones), este es el \`entry\` de [Points\_of\_interest.entry](points_of_interest#entry)

### BoxCoded

Si quieres que se muestre una caja donde tengas que introducir un código, este es el campo que usas.

### BoxMoney

La cantidad de dinero que el jugador tiene que pagar por la opción seleccionada, aparece en la caja de confirmación como cantidad de oro, plata, cobre.
El valor de BD que introduces aquí debe darse en número de cobre, así que 10 de oro se introduce como 100000 (10o 00p 00c).

### BoxText

Este es el texto de la ventana que aparece con "Sí" o "No" como botones clicables. Esto es útil si quieres una ventana de confirmación Sí/No antes de que el script se ejecute. Por ejemplo: "¿Seguro que quieres teletransportarte a Dalaran?".
Si BoxBroadCastTextID contiene un broadcast\_text.ID válido, enlaza con broadcast\_text de modo que se muestra directamente el contenido de broadcast\_text en lugar del contenido del campo box\_text.

### BoxBroadcastTextID

El ID del mismo texto en [broadcast\_text.ID](broadcast_text#id).

### VerifiedBuild

Este campo se usaba para determinar si una plantilla ha sido verificada a partir de archivos WDB.

Si el valor es 0 entonces aún no se ha parseado.

Si el valor es mayor que 0 entonces se ha parseado con archivos WDB de esa build de cliente concreta.

Si el valor es -1 entonces es solo un marcador de posición hasta que se encuentren los datos correctos en los WDB.

Si el valor es [client Build](realmlist#gamebuild) entonces se parseó con archivos WDB de esa build de cliente concreta y se editó manualmente después por alguna necesidad especial.
