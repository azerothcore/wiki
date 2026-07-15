# gossip\_menu

[<-Volver a:World](database-world)

**Tabla \`gossip\_menu\`**

Esta tabla se usa para mostrar gossip cuando un jugador habla con un NPC que tiene el [npcflag](creature_template#npcflag) establecido.

**Estructura**

| Field       | Type      | Attributes | Key | Null | Default | Extra | Comment |
| ----------- | --------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [MenuID][1] | SMALLINT  | UNSIGNED   | PRI | NO   | 0       |       |         |
| [TextID][2] | MEDIUMINT | UNSIGNED   | PRI | NO   | 0       |       |         |

[1]: #menuid
[2]: #textid

**Descripción de los campos**

### MenuID

Esto debe coincidir con el entry que añadiste a [creature\_template.gossip\_menu\_id](creature_template#gossip_menu_id). Esto también
agrupa las opciones de gossip\_menu\_option y muestra todas las opciones asociadas a este ID.

**Nota:** Si añades tus propias opciones de menú personalizadas, es práctica común empezar con un ID igual o superior a 90 000 para asegurarte de que no entre en conflicto con otros gossip menu id.

### TextID

Esto enlaza con el [npc\_text.ID](npc_text#id) del gossip que quieres que se muestre inicialmente. Esto también le dice al NPC qué decir en la parte superior del menú de opciones cuando se muestra.
