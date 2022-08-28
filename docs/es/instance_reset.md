# instance\_reset

[<-Volver a:Characters](database-characters.md)

**Tabla \`instance\_reset\`**

Fecha y hora en la que se reiniciarán las instancias heroicas y Raids (es decir, las instancias que tienen un intervalo de reinicio fijo, que es independiente de la hora en la que algún jugador(es) entró en la(s) instancia(s)). Si Rate.InstanceResetTime se cambia en worldserver.conf o worldserver.conf.dist, borra todos los datos de esta tabla.

**Estructura**

| Field           | Type        | Attributes | Key | Null | Default | Extra | Comment |
|---------------- | ----------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [mapid][1]      | SMALLINT    | UNSIGNED   | PRI | NO   | 0       |       |         |
| [difficulty][2] | TINYINT     | UNSIGNED   | PRI | NO   | 0       |       |         |
| [resettime][3]  | INT         | UNSIGNED   |     | NO   | 0       |       |         |

[1]: #mapid
[2]: #difficulty
[3]: #resettime

**Descripción de los Campos**

### mapid

ID del mapa correspondiente en que se encuentra la instancia. Véase [Map.dbc](map).

### difficulty

Dificultad de Mazmorra o Raid.

### resettime

Fecha/Hora en que se reiniciará esta instancia (mapa), medido en tiempo Unix.
