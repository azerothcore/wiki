# character\_reputation

[<-Volver a:Characters](database-characters)

**Tabla \`character\_reputation\`**

La tabla contiene información acerca de la reputación para cada personaje.

**Estructura**

| Campo         | Tipo        | Atributos | Llave | Nulo | Por defecto | Extra | Comentario                 |
| ------------- | ----------- | --------- | ----- | ---- | ----------- | ----- | -------------------------- |
| [guid][1]     | INT         | UNSIGNED  | PRI   | NO   | 0           |       | Identificador único global |
| [faction][2]  | SMALLINT    | UNSIGNED  | PRI   | NO   | 0           |       |                            |
| [standing][3] | INT         | SIGNED    |       | NO   | 0           |       |                            |
| [flags][4]    | SMALLINT    | UNSIGNED  |       | NO   | 0           |       |                            |

[1]: #guid
[2]: #faction
[3]: #standing
[4]: #flags

**Descripción de los Campos**

### guid

Globally Unique Identifier o Identificador Global único del personaje. Ver [characters.guid](characters#guid).

### faction

ID de la facción respectiva en la cual el personaje tiene la reputación asignada. Ver [Faction.dbc](facción).

### standing

Valor en la reputación actual que tiene el personaje.

### flags

Este campo es una 'Máscara de Bits' o BitMask que almacena 'Flags' o Marcadores que son asignados a la facción correspondiente del jugador, con lo cual se altera el cómo éstas son percibidas por el jugador. Al igual que cualquier campo de flags o marcadores, puedes combinarlos sumándolos entre sí. En tal caso de que este campo tuviese asignado el valor 0, significará que la reputación correspondiente no sería vista en la lista de reputación del jugador.

| Bandera | Nombre                        | Comentario                                                                                                      |
|-------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------- |
| 1       | FACTION_FLAG_VISIBLE          | Aparece en la pestaña de reputación                                                                             |
| 2       | FACTION_FLAG_AT_WAR           | Es activada cuando el jugador activa la casilla 'en guerra' en la pestaña de reputación                         |
| 4       | FACTION_FLAG_HIDDEN           | Facción oculta en el panel de reputación del cliente, pero no del lado del servidor                             |
| 8       | FACTION_FLAG_INVISIBLE_FORCED | Sobrescribe siempre FACTION_FLAG_VISIBLE y oculta la facción en rep.list                                        |
| 16      | FACTION_FLAG_PEACE_FORCED     | Sobrescribe siempre FACTION_FLAG_AT_WAR                                                                         |
| 32      | FACTION_FLAG_INACTIVE         |                                                                                                                 |
| 64      | FACTION_FLAG_RIVAL            | Marcador de las dos facciones que compiten en Terrallende                                                       |
| 128     | FACTION_FLAG_SPECIAL          | Las ciudades de origen de la Horda y la Alianza y sus aliados de Rasganorte tienen este marcador                |
