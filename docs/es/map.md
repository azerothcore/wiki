# Map

**Map.dbc**

[`Volver a:DBC`](dbc-index.md)

Éste archivo DBC contiene la lista de mapas dentro del juego.

**Versión 3.3.5a**

## Estructura

| Columna | Campo                                                                                                                                                        | Type    | Notes                                                                                                                        |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|------------------------------------------------------------------------------------------------------------------------------|
| 1       | ID                                                                                                                                                           | Integer |                                                                                                                              |
| 2       | InternalName                                                                                                                                                 | String  | Referencia al nombre interno del mundo en World\\Map\\ \[...\] \\                                                            |
| 3       | Flags                                                                                                                                                        | Integer | 0x100 - CAN\_CHANGE\_PLAYER\_DIFFICULTY  (El Jugador Puede Cambiar la Dificultad)                                            |
| 4       | Type                                                                                                                                                         | Integer | 0: nada, 1: grupo, 2: banda, 3: pvp, 4: arena, &gt;=5: nada (oficial desde "IsInInstance()")                                 |
| 5       | IsBattleground                                                                                                                                               | Integer | Booleano (1 = True (Cierto), 0 = False (Falso))                                                                              |
| 6-22    | Name                                                                                                                                                         | String  | [Localization](https://wowdev.wiki/Localization); Mostrado en el mapa del mundo por ejemplo.                                 |
| 23      | [AreaTableID](https://wowdev.wiki/DB/AreaTable)                                                                                                              | Integer | ID del area en cuestión.                                                                                                     |
| 24-40   | MapDescriptionA                                                                                                                                              | String  | [Localization](https://wowdev.wiki/Localization)                                                                             |
| 41-57   | MapDescriptionH                                                                                                                                              | String  | [Localization](https://wowdev.wiki/Localization)                                                                             |
| 58      | [LoadingScreen](https://wowdev.wiki/DB/LoadingScreens)                                                                                                       | Integer | Referencia a la ID de la pantalla de carga que se muestra                                                                    |
| 59      | BGMapIconScale                                                                                                                                               | Float   |                                                                                                                              |
| 60      | GhostEntranceMap                                                                                                                                             | Integer | Referencia a la ID; Apunta a la columna 1, -1 es nada.                                                                       |
| 61      | GhostEntranceX                                                                                                                                               | Float   | Coordenada en X del ingreso a la instancia                                                                                   |
| 62      | GhostEntranceY                                                                                                                                               | Float   | Coordenada en Y del ingreso a la instancia                                                                                   |
| 63      | TimeOfDayOverride                                                                                                                                            | Integer | Poner -1 para todo excepto para la arena de Orgrimmar y Dalaran. Para éstos, la hora del día cambiará a la que se configure. |
| 64      | Expansion                                                                                                                                                    | Integer | Classic: 0; TBC: 1; WotLK: 2                                                                                                 |
| 65      | RaidOffset                                                                                                                                                   | Integer | Reinicio de instancia?                                                                                                       |
| 66      | MaxPlayers                                                                                                                                                   | Integer |                                                                                                                              |

## Contenido

| ID  | Tipo | Nombre                                             | AreaTablaID | Expansión | MaxJugadores |
|-----|------|----------------------------------------------------|-------------|-----------|--------------|
|0|0|Reinos del Este|0|0|0|
|1|0|Kalimdor|0|0|0|
|13|0|Testing|3817|0|0|
|25|0|Scott Test|0|0|0|
|30|3|Valle de Alterac|0|0|0|
|33|1|Castillo de Colmillo Oscuro|0|0|10|
|34|1|Mazmorras de Ventormenta|717|0|10|
|35|0|<unused>VentormentaPrison|717|0|0|
|36|1|Minas de la Muerte|0|0|10|
|37|0|Cráter de Azshara|0|0|0|
|42|0|Collin\'s Test|0|0|0|
|43|1|Cuevas de los Lamentos|718|0|10|
|44|1|<unused> Monastery|0|0|10|
|47|1|Horado Rajacieno|0|0|10|
|48|1|Cavernas de Brazanegra|719|0|10|
|70|1|Uldaman|1337|0|10|
|90|1|Gnomeregan|721|0|10|
|109|1|Templo Sumergido|1477|0|10|
|129|1|Zahúrda Rajacieno|0|0|10|
|169|2|Sueño Esmeralda|0|0|40|
|189|1|Monasterio Escarlata|0|0|10|
|209|1|Zul\'Farrak|0|0|10|
|229|1|Cumbre de Roca Negra|1583|0|10|
|230|1|Profundidades de Roca Negra|1584|0|5|
|249|2|Guarida de Onyxia|2159|0|40|
|269|1|Apertura de El Portal Oscuro|0|1|5|
|289|1|Scholomance|0|0|5|
|309|2|Zul\'Gurub|1977|0|20|
|329|1|Stratholme|0|0|5|
|349|1|Maraudon|2100|0|10|
|369|0|Tranvía Subterráneo|2257|0|0|
|389|1|Sima Ígnea|2437|0|10|
|409|2|Núcleo de Magma|2717|0|40|
|429|1|La Masacre|2557|0|5|
|449|0|Cuartel JcJ de la Alianza|2918|0|0|
|450|0|Cuartel JcJ de la Horda|2917|0|0|
|451|0|Territorio en desarrollo|0|2|0|
|469|2|Guarida de Alanegra|2677|0|40|
|489|3|Garganta Grito de Guerra|3277|0|0|
|509|2|Ruinas de Ahn\'Qiraj|3429|0|20|
|529|3|Cuenca de Arathi|3358|0|0|
|530|0|Terrallende|0|1|0|
|531|2|Templo de Ahn\'Qiraj|3428|0|40|
|532|2|Karazhan|3457|1|10|
|533|2|Naxxramas|3456|2|25|
|534|2|Batalla del Monte Hyjal|616|1|25|
|540|1|Ciudadela del Fuego Infernal: Salas Arrasadas|3714|1|5|
|542|1|Ciudadela del Fuego Infernal: Horno de Sangre|3713|1|5|
|543|1|Ciudadela del Fuego Infernal: Murallas|3562|1|5|
|544|2|Guarida de Magtheridon|3836|1|25|
|545|1|Colmillo Torcido: Cámara de Vapor|3715|1|5|
|546|1|Colmillo Torcido: La Sotiénaga|3716|1|5|
|547|1|Colmillo Torcido: Recinto de los Esclavos|3717|1|5|
|548|2|Reserva Colmillo Torcido: Caverna Santuario Serpiente|3607|1|25|
|550|2|El Castillo de la Tempestad|3845|1|25|
|552|1|El Castillo de la Tempestad: El Arcatraz|3848|1|5|
|553|1|El Castillo de la Tempestad: El Invernáculo|3847|1|5|
|554|1|El Castillo de la Tempestad: El Mechanar|3849|1|5|
|555|1|Auchindoun: Laberinto de las Sombras|3789|1|5|
|556|1|Auchindoun: Salas Sethekk|3791|1|5|
|557|1|Auchindoun: Tumbas de Maná|3792|1|5|
|558|1|Auchindoun: Criptas Auchenai|3790|1|5|
|559|4|Arena de Nagrand|0|0|0|
|560|1|La Fuga de Durnholde|267|1|5|
|562|4|Arena Filospada|3702|0|0|
|564|2|El Templo Oscuro|0|1|25|
|565|2|Guarida de Gruul|3923|1|25|
|566|3|Ojo de la Tormenta|0|1|0|
|568|2|Zul\'Aman|0|1|10|
|571|0|Rasganorte|0|2|0|
|572|4|Ruinas de Lordaeron|0|0|0|
|573|0|ExteriorTest|0|2|0|
|574|1|Fortaleza de Utgarde|0|2|5|
|575|1|Pináculo de Utgarde|0|2|5|
|576|1|El Nexo|4265|2|5|
|578|1|El Oculus|0|2|5|
|580|2|La Fuente del Sol|0|1|25|
|582|0|Transporte - de Rut\'theran a Auberdine|0|0|0|
|584|0|Transporte - de Menethil a Theramore|0|0|0|
|585|1|Bancal del Magister|0|1|5|
|586|0|Transporte - de El Exodar a Auberdine|0|0|0|
|587|0|Transporte - Transbordador de Plumaluna|0|0|0|
|588|0|Transporte - de Menethil a Auberdine|0|0|0|
|589|0|Transporte - de Orgrimmar a Grom\'Gol|0|0|0|
|590|0|Transporte - de Grom\'Gol a Entrañas|0|0|0|
|591|0|Transporte - de Entrañas a Orgrimmar|0|0|0|
|592|0|Transporte - Tundra Boreal prueba|0|0|0|
|593|0|Transporte: Bahía del Botín a Trinquete|0|0|0|
|594|0|Transporte: Fiordo Aquilonal Hermana Misericordia (misión)|0|2|0|
|595|1|La Matanza de Stratholme|0|2|5|
|596|0|Transporte: Naglfar|0|2|0|
|597|0|Craig Test|0|0|0|
|598|1|Sunwell Fix (Unused)|0|1|5|
|599|1|Cámaras de Piedra|0|2|5|
|600|1|Fortaleza de Drak\'Tharon|0|2|5|
|601|1|Azjol-Nerub|0|2|5|
|602|1|Cámaras de Relámpagos|0|2|5|
|603|2|Ulduar|0|2|5|
|604|1|Gundrak|0|2|5|
|605|0|Development Land (non-weighted textures)|0|0|0|
|606|0|QA and DVD|0|2|0|
|607|3|Playa de los Ancestros|0|2|0|
|608|1|Bastión Violeta|0|2|5|
|609|0|El Bastión de Ébano|0|2|0|
|610|0|Transporte: Tirisfal al Campo Venganza|0|0|0|
|612|0|Transporte: Menethil a Valgarde|0|0|0|
|613|0|Transporte: Orgrimmar al Bastión Grito de Guerra|0|0|0|
|614|0|Transporte: Ventormenta a la Fortaleza Denuedo|0|0|0|
|615|2|El Sagrario Obsidiana|0|2|0|
|616|2|El Ojo de la Eternidad|0|2|5|
|617|4|Cloacas de Dalaran|0|0|0|
|618|4|El Círculo del Valor|0|0|0|
|619|1|Ahn\'kahet: El Antiguo Reino|0|2|0|
|620|0|Transporte: Moa\'ki a Unu\'pe|0|2|0|
|621|0|Transporte: Moa\'ki a Komawa|0|2|0|
|622|0|Transporte: Martillo de Orgrim|0|2|0|
|623|0|Transporte: El Rompecielos|0|2|0|
|624|2|Cámara de Archavon|0|2|0|
|628|3|Isla de la Conquista|0|2|0|
|631|2|Ciudadela de la Corona de Hielo|0|2|0|
|632|1|La Forja de Almas|0|2|0|
|641|0|Transport: Alliance Airship BG|0|2|0|
|642|0|Transport: HordeAirshipBG|0|2|0|
|647|0|Transporte: Orgrimmar a Cima del Trueno|0|2|0|
|649|2|Prueba del Cruzado|0|2|0|
|650|1|Prueba del Campeón|0|2|0|
|658|1|Foso de Saron|0|2|0|
|668|1|Cámaras de Reflexión|0|2|0|
|672|0|Transporte: El Rompecielos (Banda de Ciudadela de la Corona de Hielo)|0|2|0|
|673|0|Transporte: Martillo de Orgrim (Banda de Ciudadela de la Corona de Hielo)|0|2|0|
|712|0|Transporte: El Rompecielos (Mazmorra de Ciudadela de la Corona de Hielo)|0|2|0|
|713|0|Transporte: Martillo de Orgrim (Mazmorra de Ciudadela de la Corona de Hielo)|0|2|0|
|718|0|Transporte: El Viento Poderoso (Banda de Ciudadela de la Corona de Hielo)|0|2|0|
|723|0|Ventormenta|0|0|0|
|724|2|El Sagrario Rubí|0|2|0|


