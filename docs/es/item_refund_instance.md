# item\_refund\_instance

[<-Volver a:Characters](database-characters)

**Tabla \`item\_refund\_instance\`**

La tabla tiene la función de ser un "recibo de las compras" para Items reembolsables durante un intervalo de tiempo de aproximadamente 2 horas dentro del juego. También alberga información acerca de la moneda que se usó para la compra del Item.

**Estructura**

| Field                 | Type     | Attributes | Key | Null | Default | Extra  | Comment     |
| --------------------- | -------- | ---------- | --- | ---- | ------- | ------ | ----------- |
| [item_guid][1]        | INT      | UNSIGNED   | PRI | NO   |         |        | Item GUID   |
| [player_guid][2]      | INT      | UNSIGNED   | PRI | NO   |         |        | Player GUID |
| [paidMoney][3]        | INT      | UNSIGNED   |     | NO   | 0       |        |             |
| [paidExtendedCost][4] | SMALLINT | UNSIGNED   |     | NO   | 0       |        |             |

[1]: #itemguid
[2]: #playerguid
[3]: #paidmoney
[4]: #paidextendedcost

**Descripción de los Campos**

### item\_guid

GUID o Identificador Global Único del Item comprado. Véase [item\_instance.guid](item_instance#guid).

### player\_guid

GUID o Identificador Global Único del jugador con derecho a reembolso. Véase [characters.guid](characters#guid).

### paidMoney

La cantidad de dinero (medido en monedas de cobre) gastados por el jugador.

### paidExtendedCost

ID del ItemExtendedCost.dbc que se pagó por el artículo (si es que se usó alguno para la compra)
