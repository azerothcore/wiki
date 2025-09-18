# channels

[<-Volver a:Characters](database-characters)

**Tabla \`channels\`**

La tabla alberga información y configuración de aquellos canales de chat creados por los propios jugadores (no afecta a los canales por defecto del sistema).

**Estructura**

| Campo           | Tipo         | Atributos | Llave | Nulo | Por defecto | Extra          | Comentario |
| --------------- | ------------ | --------- | ----- | ---- | ----------- | -------------- | ---------- |
| [channelId][1]  | INT          | SIGNED    | PRI   | NO   |             | AUTO_INCREMENT |            |
| [name][2]       | VARCHAR(128) | SIGNED    |       | NO   |             |                |            |
| [team][3]       | INT          | UNSIGNED  |       | NO   |             |                |            |
| [announce][4]   | TINYINT      | UNSIGNED  |       | NO   | 1           |                |            |
| [ownership][5]  | TINYINT      | UNSIGNED  |       | NO   | 1           |                |            |
| [password][6]   | VARCHAR(32)  | SIGNED    |       | YES  |             |                |            |
| [lastUsed][7]   | INT          | UNSIGNED  |       | NO   |             |                |            |

[1]: #channelid
[2]: #name
[3]: #team
[4]: #announce
[5]: #ownership
[6]: #password
[7]: #lastused

**Descripción de los Campos**

### channelId

ID del canal en cuestión.

### name

Nombre del canal respectivo.

### team

Permite el acceso al canal desde una ID de la facción correspondiente del jugador especificado.

Para aquellos canales de razas variadas, deben existir dos (o más) entradas (entries) separadas con la misma configuración (EXACTA) para todos los campos excepto este (se necesitaría un `ID de equipo` distinto).

| Facción  | Valor |
| -------- | ----- |
| Horda    | 67    |
| Alianza  | 469   |

### announce

Anuncios del canal (0/1).

- 0 = Las acciones de unión/salida de jugadores dentro del canal no serán enviadas.
- 1 = Se enviarán aquellas acciones previamente mencionadas de unión/salida.

### ownership

Propiedad del canal.

- 0 = Nadie será propietario del mismo.
- 1 = El propietario es la primera persona dentro del canal.

### password

Contraseña del canal.

Ninguna, o una contraseña estándar basada en una cadena (no se permiten espacios entre sí).

### lastUsed

Campo usado para la limpieza automática de aquellos canales no utilizados en la base de datos. Esto medido en tiempo Unix.
