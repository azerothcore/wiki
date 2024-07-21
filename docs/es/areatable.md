
# AreaTable

[`Volver a:DBC`](dbc-index)

**AreaTable.dbc**

El DBC contiene en su interior las listas de zonas y subzonas existentes dentro del juego. Para fines de este artículo en la wiki, se incluirá la ID de cada zona, junto con sus respectivos nombres, mapID y AreaID de la zona en cuestión.

**Versión 3.3.5a**

## Estructura

| Columna | Nombre             | Tipo   | Notas                                                                                                        |
| ------- | ------------------ | ------ | ------------------------------------------------------------------------------------------------------------ |
| 1       | ID                 | Int    | Área de la zona                                                                                              |
| 2       | MapID              | Int    | Mapa o Continente                                                                                            |
| 3       | AreaID             | Int    | SubÁrea o Mapa.                                                                                              |
| 4       | Explore Flag       | Int    |                                                                                                              |
| 5       | Flags              | Int    |                                                                                                              |
| 8       | SoundAmbienceID    | Int    | Identificador del tipo de Sonido de Ambiente utilizado durante el día y la noche                             |
| 9       | ZoneMusicID        | Int    | Identificador del tipo de Música utilizada en la zona                                                        |
| 10      | ZoneIntroMusicID   | Int    | Identificador del tipo de 'Música de Introducción de la zona' (ZoneIntro) que debe sonar al ingresar en ella |
| 11      | Area Level         | Int    |                                                                                                              |
| 12-28   | Area Name          | String |                                                                                                              |
| 29      | FactionGroupID     | Int    | Facción de la zona en cuestión                                                                               |

**Descripción de los Campos**

## Flags

Marcadores o 'Flags'.

| Valor      | Nombre                   | Notas                                                                                                                                                                                                                                          |
| ---------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x00000001 | AREA_FLAG_SNOW           | Nieve (sólo Dun Morogh, Naxxramas, Zahúrda Rojocieno y Cuna del Invierno)                                                                                                                                                                      |
| 0x00000002 | AREA_FLAG_UNK1           | ¿Podría ser para alguna necrópolis?                                                                                                                                                                                                            |
| 0x00000004 | AREA_FLAG_UNK2           | Solía ser usado en zonas del mapa 571 (antes llamada Zona de Desarrollo)                                                                                                                                                                       |
| 0x00000008 | AREA_FLAG_SLAVE_CAPITAL  | Zonas y subzonas de la ciudad en cuestión                                                                                                                                                                                                      |
| 0x00000010 | AREA_FLAG_UNK3           | No pudo encontrarse un significado para esta columna                                                                                                                                                                                           |
| 0x00000020 | AREA_FLAG_SLAVE_CAPITAL2 | ¿Marcador de una capital esclava?                                                                                                                                                                                                              |
| 0x00000040 | AREA_FLAG_ALLOW_DUELS    | Permite hacer un duelo aquí                                                                                                                                                                                                                    |
| 0x00000080 | AREA_FLAG_ARENA          | Arena, tanto en instancias como en Arenas de Mundo                                                                                                                                                                                             |
| 0x00000100 | AREA_FLAG_CAPITAL        | Marcador de la capital principal                                                                                                                                                                                                               |
| 0x00000200 | AREA_FLAG_CITY           | Usado únicamente para una zona llamada "Ciudad" (¿Dónde se encuentra? Sólo Dios sabe)                                                                                                                                                          |
| 0x00000400 | AREA_FLAG_OUTLAND        | ¿Zonas de expansión? (únicamente el Ojo de la Tormenta no tiene este marcador, sin embargo posée 0x00004000)                                                                                                                                   |
| 0x00000800 | AREA_FLAG_SANCTUARY      | Zona de santuario (PvP desactivado)                                                                                                                                                                                                            |
| 0x00001000 | AREA_FLAG_NEED_FLY       | Únicamente para Arrecife del Ala Abisal, Trono de Socrethar, Castillo de la Tempestad, El Arcatraz, El Invernáculo, El Mechanar, Punta Alapenas, Cresta Espinazo de Dragón, Minas del Ala Abisal, Campamento Faucedraco, Ruta Aérea Faucedraco |
| 0x00002000 | AREA_FLAG_UNUSED1        | No es usado (no hay áreas/zonas con este marcador establecido en el parche 3.0.3)                                                                                                                                                              |
| 0x00004000 | AREA_FLAG_OUTLAND2       | ¿Zonas de expansión? (únicamente la arena del Círculo de Sangre no tiene el marcador, sino 0x00000400)                                                                                                                                         |
| 0x00008000 | AREA_FLAG_OUTDOOR_PVP    | ¿Área de objetivo pvp? (La Puerta de la Muerte también posée el marcador, aunque no sea un área para objetivos pvp)                                                                                                                            |
| 0x00010000 | AREA_FLAG_ARENA_INSTANCE | Utilizado sólo para arenas que se encuentren en una instanciada, no aplica para arenas de mundo.                                                                                                                                               |
| 0x00020000 | AREA_FLAG_UNUSED2        | No es usado (no hay áreas/zonas con este marcador establecido en el parche 3.0.3)                                                                                                                                                              |
| 0x00040000 | AREA_FLAG_CONTESTED_AREA | En servidores PvP, las áreas que posean este marcador se consideran 'En Disputa', ya sea un territorio perteneciente a la Horda/Alianza.                                                                                                       |
| 0x00080000 | AREA_FLAG_UNK6           | Valgarde y Acherus: El Bastión de Ébano                                                                                                                                                                                                        |
| 0x00100000 | AREA_FLAG_LOWLEVEL       | Usado para algunas zonas de inicio con area_level (nivel de área) <=15 (menor o igual a 15)                                                                                                                                                    |
| 0x00200000 | AREA_FLAG_TOWN           | Pueblos pequeños con posada                                                                                                                                                                                                                    |
| 0x00400000 | AREA_FLAG_UNK7           | Bastión Grito de Guerra, Acherus: El Bastión de Ébano, Fortaleza de Nuevo Agamand, Fortaleza de Campo Venganza                                                                                                                                 |
| 0x00800000 | AREA_FLAG_UNK8           | Fortaleza de la Guardia del Oeste, Acherus: El Bastión de Ébano, Valgarde                                                                                                                                                                      |
| 0x01000000 | AREA_FLAG_WINTERGRASP    | Cuna del Invierno y sus subzonas                                                                                                                                                                                                               |
| 0x02000000 | AREA_FLAG_INSIDE         | Usado para determinar las misiones del interior/exterior relacionadas con el hechizo en Map::IsOutdoors                                                                                                                                        |
| 0x04000000 | AREA_FLAG_OUTSIDE        | Usado para determinar las misiones del interior/exterior relacionadas con el hechizo en Map::IsOutdoors                                                                                                                                        |
| 0x08000000 | AREA_FLAG_WINTERGRASP_2  | Cuna del Invierno y sus subzonas                                                                                                                                                                                                               |
| 0x20000000 | AREA_FLAG_CANNOT_FLY     | No se permite volar, únicamente es usado en las áreas aledañas de Dalaran (zona 4395)                                                                                                                                                          |

## Contenido

| ID   | Nombre                                                | MapID | AreaID |
|------|-------------------------------------------------------|-------|--------|
| 1    | Dun Morogh                                            | 0     | 0      |
| 2    | Playa Larga                                           | 0     | 40     |
| 3    | Tierras Inhóspitas                                    | 0     | 0      |
| 4    | Las Tierras Devastadas                                | 0     | 0      |
| 7    | Cala Aguasnegras                                      | 0     | 33     |
| 8    | Pantano de las Penas                                  | 0     | 0      |
| 9    | Valle de Villanorte                                   | 0     | 12     |
| 10   | Bosque del Ocaso                                      | 0     | 0      |
| 11   | Los Humedales                                         | 0     | 0      |
| 12   | Bosque de Elwynn                                      | 0     | 0      |
| 13   | Árbol del Mundo                                       | 0     | 10     |
| 14   | Durotar                                               | 1     | 0      |
| 15   | Marjal Revolcafango                                   | 1     | 0      |
| 16   | Azshara                                               | 1     | 0      |
| 17   | Los Baldíos                                           | 1     | 0      |
| 18   | Lago de Cristal                                       | 0     | 12     |
| 19   | Zul'Gurub                                             | 0     | 33     |
| 20   | Arroyo de la Luna                                     | 0     | 40     |
| 21   | Kul Tiras                                             | 0     | 0      |
| 22   | Isla del Programador                                  | 451   | 0      |
| 23   | Río de Villanorte                                     | 0     | 12     |
| 24   | Abadía de Villanorte                                  | 0     | 12     |
| 25   | Montaña Roca Negra                                    | 0     | 0      |
| 26   | Faro                                                  | 0     | 40     |
| 28   | Tierras de la Peste del Oeste                         | 0     | 0      |
| 30   | Nine                                                  | 0     | 0      |
| 32   | El Cementerio                                         | 0     | 10     |
| 33   | Vega de Tuercespina                                   | 0     | 0      |
| 34   | Mina del Eco                                          | 0     | 12     |
| 35   | Bahía del Botín                                       | 0     | 33     |
| 36   | Montañas de Alterac                                   | 0     | 0      |
| 37   | Lago Nazferiti                                        | 0     | 33     |
| 38   | Loch Modan                                            | 0     | 0      |
| 40   | Páramos de Poniente                                   | 0     | 0      |
| 41   | Paso de la Muerte                                     | 0     | 0      |
| 42   | Villa Oscura                                          | 0     | 10     |
| 43   | Orilla Salvaje                                        | 0     | 33     |
| 44   | Montañas Crestagrana                                  | 0     | 0      |
| 45   | Tierras Altas de Arathi                               | 0     | 0      |
| 46   | Las Estepas Ardientes                                 | 0     | 0      |
| 47   | Tierras del Interior                                  | 0     | 0      |
| 49   | El Agujero del Muerto                                 | 451   | 22     |
| 51   | La Garganta de Fuego                                  | 0     | 0      |
| 53   | Campamento de Ladrones                                | 0     | 12     |
| 54   | Cantera de Jaspe                                      | 0     | 12     |
| 55   | Valley of Heroes UNUSED                               | 0     | 12     |
| 56   | Vigilia de los Héroes                                 | 0     | 12     |
| 57   | Mina Abisal                                           | 0     | 12     |
| 59   | Viñedos de Villanorte                                 | 0     | 12     |
| 60   | Linde del bosque                                      | 0     | 12     |
| 61   | Cataratas del Trueno                                  | 0     | 12     |
| 62   | Plantación de Calabazas de Brackwell                  | 0     | 12     |
| 63   | La Granja Pedregosa                                   | 0     | 12     |
| 64   | Los Viñedos de Maclure                                | 0     | 12     |
| 65   | Cementerio de Dragones                                | 571   | 0      |
| 66   | Zul'Drak                                              | 571   | 0      |
| 67   | Las Cumbres Tormentosas                               | 571   | 0      |
| 68   | Lago Sempiterno                                       | 0     | 44     |
| 69   | Villa del Lago                                        | 0     | 44     |
| 70   | Petravista                                            | 0     | 44     |
| 71   | Cascadas Petravista                                   | 0     | 44     |
| 72   | El Portal Oscuro                                      | 0     | 4      |
| 73   | Escara Impía                                          | 0     | 4      |
| 74   | Charca de Lágrimas                                    | 0     | 8      |
| 75   | Rocal                                                 | 0     | 8      |
| 76   | Retiro Fangoso                                        | 0     | 8      |
| 77   | Yunquemar                                             | 0     | 1      |
| 80   | Montañas de Ventormenta                               | 0     | 12     |
| 81   | Jeff NE Quadrant Changed                              | 451   | 22     |
| 82   | Jeff NW Quadrant                                      | 451   | 22     |
| 83   | Jeff SE Quadrant                                      | 451   | 22     |
| 84   | Jeff SW Quadrant                                      | 451   | 22     |
| 85   | Claros de Tirisfal                                    | 0     | 0      |
| 86   | Lago del Hito                                         | 0     | 12     |
| 87   | Villadorada                                           | 0     | 12     |
| 88   | Aserradero de la Vega del Este                        | 0     | 12     |
| 89   | Vergel del Lago Espejo                                | 0     | 12     |
| 91   | Torre de Azora                                        | 0     | 12     |
| 92   | Lago Espejo                                           | 0     | 12     |
| 93   | Túmulo de Vul'Gol                                     | 0     | 10     |
| 94   | Cerro del Cuervo                                      | 0     | 10     |
| 95   | Cañones de Crestagrana                                | 0     | 44     |
| 96   | Torre de Ilgalar                                      | 0     | 44     |
| 97   | Molino de Alther                                      | 0     | 44     |
| 98   | Cavernas de Rethban                                   | 0     | 44     |
| 99   | Asentamiento Rebelde                                  | 0     | 33     |
| 100  | Expedición de Nesingwary                              | 0     | 33     |
| 101  | Base de Kurzen                                        | 0     | 33     |
| 102  | Ruinas de Zul'Kunda                                   | 0     | 33     |
| 103  | Ruinas de Zul'Mamwe                                   | 0     | 33     |
| 104  | El Arrecife Mortal                                    | 0     | 33     |
| 105  | Túmulo Ogro Mosh'Ogg                                  | 0     | 33     |
| 106  | Las Reservas                                          | 0     | 33     |
| 107  | Finca de Saldean                                      | 0     | 40     |
| 108  | Colina del Centinela                                  | 0     | 40     |
| 109  | Plantación de Calabazas de Cejade                     | 0     | 40     |
| 111  | Mina de Jango                                         | 0     | 40     |
| 113  | Mina de la Costa del Oro                              | 0     | 40     |
| 115  | Faro de Poniente                                      | 0     | 40     |
| 116  | Valle Brumoso                                         | 0     | 8      |
| 117  | Campamento Grom'gol                                   | 0     | 33     |
| 118  | Excavación de Whelgar                                 | 0     | 11     |
| 120  | Cuartel de Arroyoeste                                 | 0     | 12     |
| 121  | Cementerio del Jardín Sereno                          | 0     | 10     |
| 122  | Ruinas Zuuldaia                                       | 0     | 33     |
| 123  | Ruinas de Bal'lal                                     | 0     | 33     |
| 125  | Ruinas de Kal'ai                                      | 0     | 33     |
| 126  | Ruinas de Tkashi                                      | 0     | 33     |
| 127  | Ruinas de Balia'mah                                   | 0     | 33     |
| 128  | Ruinas de Ziata'jai                                   | 0     | 33     |
| 129  | Ruinas de Mizjah                                      | 0     | 33     |
| 130  | Bosque de Argénteos                                   | 0     | 0      |
| 131  | Kharanos                                              | 0     | 1      |
| 132  | Valle de Crestanevada                                 | 0     | 1      |
| 133  | Gnomeregan                                            | 0     | 1      |
| 134  | Cantera de Gol'Bolar                                  | 0     | 1      |
| 135  | Poblado Peloescarcha                                  | 0     | 1      |
| 136  | El Cubil Pardo                                        | 0     | 1      |
| 137  | Las Birras                                            | 0     | 1      |
| 138  | Refugio Pinobruma                                     | 0     | 1      |
| 139  | Tierras de la Peste del Este                          | 0     | 0      |
| 141  | Teldrassil                                            | 1     | 0      |
| 142  | Excavación de Vetaferro                               | 0     | 38     |
| 143  | Fortaleza de Mo'grosh                                 | 0     | 38     |
| 144  | Thelsamar                                             | 0     | 38     |
| 145  | Puerta de Algaz                                       | 0     | 38     |
| 146  | Presa de las Tres Cabezas                             | 0     | 38     |
| 147  | Cabaña del Errante                                    | 0     | 38     |
| 148  | Costa Oscura                                          | 1     | 0      |
| 149  | Mina de Fuenteplata                                   | 0     | 38     |
| 150  | Puerto de Menethil                                    | 0     | 11     |
| 151  | Isla del Diseñador                                    | 451   | 0      |
| 152  | El Baluarte                                           | 0     | 85     |
| 153  | Ruinas de Lordaeron                                   | 0     | 85     |
| 154  | Camposanto                                            | 0     | 85     |
| 155  | Hoya Nocturácnidas                                    | 0     | 85     |
| 156  | Hacienda Solliden                                     | 0     | 85     |
| 157  | Molinos de Agamand                                    | 0     | 85     |
| 158  | Cripta de la Familia Agamand                          | 0     | 85     |
| 159  | Rémol                                                 | 0     | 85     |
| 160  | Jardines de los Susurros                              | 0     | 85     |
| 161  | Bancal del Reposo                                     | 0     | 85     |
| 162  | Lago Aguasclaras                                      | 0     | 85     |
| 163  | Refugio de Gunther                                    | 0     | 85     |
| 164  | Granja de Garren                                      | 0     | 85     |
| 165  | Hacienda Balnir                                       | 0     | 85     |
| 166  | Mansión Fríogar                                       | 0     | 85     |
| 167  | Avanzada de los Cruzados                              | 0     | 85     |
| 168  | La Costa Norte                                        | 0     | 85     |
| 169  | Costa Murmurante                                      | 0     | 85     |
| 170  | Lago Lordamere                                        | 0     | 0      |
| 172  | Isla de Fenris                                        | 0     | 130    |
| 173  | Tumba de Faol                                         | 0     | 85     |
| 186  | Dolanaar                                              | 1     | 141    |
| 187  | Darnassus UNUSED                                      | 1     | 141    |
| 188  | Cañada Umbría                                         | 1     | 141    |
| 189  | Almacén de Brasacerada                                | 0     | 1      |
| 190  | Vega del Amparo                                       | 0     | 28     |
| 192  | Aserradero Crestanorte                                | 0     | 28     |
| 193  | Ruinas de Andorhal                                    | 0     | 28     |
| 195  | Escuela de Nigromancia                                | 0     | 28     |
| 196  | Tumba de Uther                                        | 0     | 28     |
| 197  | Colina de las Penas                                   | 0     | 28     |
| 198  | La Cueva del Llanto                                   | 0     | 28     |
| 199  | Campo de Piedramácula                                 | 0     | 28     |
| 200  | Llanto de Dalson                                      | 0     | 28     |
| 201  | Gangrena de Gahrron                                   | 0     | 28     |
| 202  | El Tormento                                           | 0     | 28     |
| 203  | Fortaleza de Mardenholde                              | 0     | 28     |
| 204  | Aldea Piroleña                                        | 0     | 130    |
| 205  | Dun Modr                                              | 0     | 11     |
| 206  | Fortaleza de Utgarde                                  | 574   | 0      |
| 207  | Mare Magnum                                           | 36    | 0      |
| 208  | Unused Cala del Acorazado                             | 36    | 0      |
| 209  | Castillo de Colmillo Oscuro                           | 33    | 0      |
| 210  | Corona de Hielo                                       | 571   | 0      |
| 211  | Lago Glacial                                          | 0     | 1      |
| 212  | Lago de Helm                                          | 0     | 1      |
| 213  | Mina de Elem                                          | 0     | 130    |
| 214  | Mare Magnum                                           | 0     | 0      |
| 215  | Mulgore                                               | 1     | 0      |
| 219  | Hacienda de Alexston                                  | 0     | 40     |
| 220  | Mesa de la Nube Roja                                  | 1     | 215    |
| 221  | Campamento Narache                                    | 1     | 215    |
| 222  | Poblado Pezuña de Sangre                              | 1     | 215    |
| 223  | Lago Toro de Piedra                                   | 1     | 215    |
| 224  | Caravana Devastada                                    | 1     | 215    |
| 225  | Roca Roja                                             | 1     | 215    |
| 226  | Penumbra de las Celerácnidas                          | 0     | 130    |
| 227  | Campo de Valgan                                       | 0     | 130    |
| 228  | El Sepulcro                                           | 0     | 130    |
| 229  | Finca de Olsen                                        | 0     | 130    |
| 230  | La Muralla de Cringris                                | 0     | 130    |
| 231  | El Desafío de Beren                                   | 0     | 130    |
| 232  | Islas del Alba                                        | 0     | 130    |
| 233  | Molino Ámbar                                          | 0     | 130    |
| 235  | Castillo de Fenris                                    | 0     | 130    |
| 236  | Castillo de Colmillo Oscuro                           | 0     | 130    |
| 237  | El Viejo Embarcadero                                  | 0     | 130    |
| 238  | Huerta de Malden                                      | 0     | 130    |
| 239  | Los Dominios de Ivar                                  | 0     | 130    |
| 240  | El Campo Muerto                                       | 0     | 130    |
| 241  | El Vergel Pútrido                                     | 0     | 10     |
| 242  | Arboleda del Destello                                 | 0     | 10     |
| 243  | Loma Inhóspita                                        | 0     | 10     |
| 244  | El Raquitismo                                         | 0     | 10     |
| 245  | La Hacienda Yorgen                                    | 0     | 10     |
| 246  | La Caldera                                            | 0     | 51     |
| 247  | Excavación de Grimesilt                               | 0     | 51     |
| 249  | Roca Machacamiedo                                     | 0     | 46     |
| 250  | Ruinas de Thaurissan                                  | 0     | 46     |
| 251  | Peñasco Llamarada                                     | 0     | 46     |
| 252  | Bastión de Roca Negra                                 | 0     | 46     |
| 253  | El Pilar de Ceniza                                    | 0     | 46     |
| 254  | Montaña Roca Negra                                    | 0     | 46     |
| 255  | Altar de la Tempestad                                 | 0     | 46     |
| 256  | Aldrassil                                             | 1     | 141    |
| 257  | Gruta Narácnida                                       | 1     | 141    |
| 258  | Roca Mácula                                           | 1     | 141    |
| 259  | Lago Al'Ameth                                         | 1     | 141    |
| 260  | Aldea Brisa Estelar                                   | 1     | 141    |
| 261  | Tierras de los Tuercepinos                            | 1     | 141    |
| 262  | Túmulo de Ban'ethil                                   | 1     | 141    |
| 263  | La Grieta                                             | 1     | 141    |
| 264  | El Claro del Oráculo                                  | 1     | 141    |
| 265  | Río Primigenio                                        | 1     | 141    |
| 266  | Lago Primigenio                                       | 1     | 141    |
| 267  | Laderas de Trabalomas                                 | 0     | 0      |
| 268  | Cráter de Azshara                                     | 37    | 0      |
| 269  | Dun Algaz                                             | 0     | 0      |
| 271  | Costasur                                              | 0     | 267    |
| 272  | Molino Tarren                                         | 0     | 267    |
| 275  | Castillo de Durnholde                                 | 0     | 267    |
| 276  | UNUSED Stonewrought Pass                              | 0     | 0      |
| 277  | Cuevas de la Ladera                                   | 0     | 36     |
| 278  | Campo de Reclusión de Lordamere                       | 0     | 36     |
| 279  | Cráter de Dalaran                                     | 0     | 36     |
| 280  | Strahnbrad                                            | 0     | 36     |
| 281  | Ruinas de Alterac                                     | 0     | 36     |
| 282  | Dominios de los Aplastacresta                         | 0     | 36     |
| 283  | Cuenca de la Matanza                                  | 0     | 36     |
| 284  | Las Tierras Altas                                     | 0     | 36     |
| 285  | Torre Austral                                         | 0     | 267    |
| 286  | Campos de Trabalomas                                  | 0     | 267    |
| 287  | Trabalomas                                            | 0     | 267    |
| 288  | Mina Azur                                             | 0     | 267    |
| 289  | Granja Nethander                                      | 0     | 267    |
| 290  | Dun Garok                                             | 0     | 267    |
| 293  | Muralla de Thoradin                                   | 0     | 0      |
| 294  | Playa del Este                                        | 0     | 267    |
| 295  | Playa del Oeste                                       | 0     | 267    |
| 296  | South Seas UNUSED                                     | 0     | 0      |
| 297  | Isla Jaguero                                          | 0     | 33     |
| 298  | Bahía de Baradin                                      | 0     | 11     |
| 299  | Bahía de Menethil                                     | 0     | 11     |
| 300  | Playa Juncobruma                                      | 0     | 8      |
| 301  | La Costa Salvaje                                      | 0     | 33     |
| 302  | La Costa de Cristal                                   | 0     | 33     |
| 303  | Playa del Molusco                                     | 0     | 33     |
| 305  | Cala Mareanorte                                       | 0     | 130    |
| 306  | Cala Mareasur                                         | 0     | 130    |
| 307  | Los Acantilados Dominantes                            | 0     | 47     |
| 308  | Mar Adusto                                            | 0     | 0      |
| 309  | Tumba de Barbaférrea                                  | 0     | 11     |
| 310  | Mina de Cristal                                       | 0     | 33     |
| 311  | Ruinas de Aboraz                                      | 0     | 33     |
| 312  | Cayo de Janeiro                                       | 0     | 33     |
| 313  | Mansión Redilnorte                                    | 0     | 45     |
| 314  | Granja Go'shek                                        | 0     | 45     |
| 315  | Granja de Dabyrie                                     | 0     | 45     |
| 316  | Sala Puño de Roca                                     | 0     | 45     |
| 317  | Poblado Secacorteza                                   | 0     | 45     |
| 318  | Cañón Mostacho Seco                                   | 0     | 45     |
| 320  | Refugio de la Zaga                                    | 0     | 45     |
| 321  | Sentencia                                             | 0     | 45     |
| 322  | Naufragios de Aguasnegras                             | 0     | 45     |
| 323  | Campamento de O'Breen                                 | 0     | 45     |
| 324  | Castillo de Stromgarde                                | 0     | 45     |
| 325  | Torre de Arathor                                      | 0     | 45     |
| 326  | El Sagrario                                           | 0     | 45     |
| 327  | Cala de Faldir                                        | 0     | 45     |
| 328  | El Arrecife Hundido                                   | 0     | 45     |
| 330  | Puente Thandol                                        | 0     | 0      |
| 331  | Vallefresno                                           | 1     | 0      |
| 332  | Mare Magnum                                           | 1     | 0      |
| 333  | Círculo de Vínculo Este                               | 0     | 45     |
| 334  | Círculo de Vínculo Oeste                              | 0     | 45     |
| 335  | Círculo de Vínculo Interior                           | 0     | 45     |
| 336  | Círculo de Vínculo Exterior                           | 0     | 45     |
| 337  | Descanso de Apócrifo                                  | 0     | 3      |
| 338  | Fortaleza de Angor                                    | 0     | 3      |
| 339  | Barranco Lethlor                                      | 0     | 3      |
| 340  | Kargath                                               | 0     | 3      |
| 341  | Asentamiento Kosh                                     | 0     | 3      |
| 342  | Asentamiento Boff                                     | 0     | 3      |
| 343  | Asentamiento Wurg                                     | 0     | 3      |
| 344  | Asentamiento Cagg                                     | 0     | 3      |
| 345  | El Final de Agmond                                    | 0     | 3      |
| 346  | Excavación de Piemartillo                             | 0     | 3      |
| 347  | Gruta Rotapolvo                                       | 0     | 3      |
| 348  | Pico Nidal                                            | 0     | 47     |
| 349  | Fortaleza de los Martillo Salvaje                     | 0     | 47     |
| 350  | Avanzada Quel'Danil                                   | 0     | 47     |
| 351  | Roca Oculta                                           | 0     | 47     |
| 352  | Zun'watha                                             | 0     | 47     |
| 353  | Shadra'Alor                                           | 0     | 47     |
| 354  | Jintha'Alor                                           | 0     | 47     |
| 355  | El Altar de Zul                                       | 0     | 47     |
| 356  | Seradane                                              | 0     | 47     |
| 357  | Feralas                                               | 1     | 0      |
| 358  | Barranco Cortazarza                                   | 1     | 215    |
| 359  | Bael Modan                                            | 1     | 17     |
| 360  | Mina Ventura y Cía.                                   | 1     | 215    |
| 361  | Frondavil                                             | 1     | 0      |
| 362  | Cerrotajo                                             | 1     | 14     |
| 363  | Valle de los Retos                                    | 1     | 14     |
| 364  | El Cubil                                              | 1     | 14     |
| 365  | Aquelarre del Filo Ardiente                           | 1     | 14     |
| 366  | Risco Kolkar                                          | 1     | 14     |
| 367  | Poblado Sen'jin                                       | 1     | 14     |
| 368  | Islas del Eco                                         | 1     | 14     |
| 369  | Monte del Trueno                                      | 1     | 14     |
| 370  | Barranco Árido                                        | 1     | 14     |
| 371  | Cueva Viento Seco                                     | 1     | 14     |
| 372  | Fuerte de Tiragarde                                   | 1     | 14     |
| 373  | Costa de la Huida                                     | 1     | 14     |
| 374  | Bahía de Garrafilada                                  | 1     | 14     |
| 375  | Costa de Mortojo                                      | 1     | 14     |
| 377  | Río Furia del Sur                                     | 1     | 0      |
| 378  | Campamento Taurajo                                    | 1     | 17     |
| 379  | Avanzada del Puente                                   | 1     | 17     |
| 380  | El Cruce                                              | 1     | 17     |
| 381  | Mina Pedrusco                                         | 1     | 17     |
| 382  | El Fangal                                             | 1     | 17     |
| 383  | Las Colinas Áridas                                    | 1     | 17     |
| 384  | Cima Calígine                                         | 1     | 17     |
| 385  | Fuerte del Norte                                      | 1     | 17     |
| 386  | Las Charcas del Olvido                                | 1     | 17     |
| 387  | Oasis Aguaverde                                       | 1     | 17     |
| 388  | El Oasis Estancado                                    | 1     | 17     |
| 390  | Tierra de Gigantes                                    | 1     | 17     |
| 391  | La Costa Mercante                                     | 1     | 17     |
| 392  | Trinquete                                             | 1     | 17     |
| 393  | Playa Lanza Negra                                     | 1     | 14     |
| 394  | Colinas Pardas                                        | 571   | 0      |
| 395  | Fauceparda                                            | 571   | 394    |
| 396  | Pozo Pezuña Invernal                                  | 1     | 215    |
| 397  | Pozo Tronacuerno                                      | 1     | 215    |
| 398  | Pozo Ferocrín                                         | 1     | 215    |
| 399  | Cresta Horizonte                                      | 1     | 215    |
| 400  | Las Mil Agujas                                        | 1     | 0      |
| 401  | El Escalón de la Marea                                | 1     | 17     |
| 403  | Posada Reposo Umbrío                                  | 1     | 15     |
| 404  | Excavación de Bael'dun                                | 1     | 215    |
| 405  | Desolace                                              | 1     | 0      |
| 406  | Sierra Espolón                                        | 1     | 0      |
| 407  | Orgrimmar UNUSED                                      | 1     | 14     |
| 408  | Isla de Gillijim                                      | 0     | 0      |
| 409  | Isla del Doctor Lapidis                               | 0     | 0      |
| 410  | Cañón del Ventajo                                     | 1     | 14     |
| 411  | Ruinas de Bathran                                     | 1     | 331    |
| 412  | Las Ruinas de Ordil'Aran                              | 1     | 331    |
| 413  | Atalaya de Maestra                                    | 1     | 331    |
| 414  | La Ensenada de Zoram                                  | 1     | 331    |
| 415  | Astranaar                                             | 1     | 331    |
| 416  | El Santuario de Aessina                               | 1     | 331    |
| 417  | Santuario de la Escara                                | 1     | 331    |
| 418  | Las Ruinas del Polvo Estelar                          | 1     | 331    |
| 419  | Vega del Aullido                                      | 1     | 331    |
| 420  | Refugio Brisa de Plata                                | 1     | 331    |
| 421  | Lago Mystral                                          | 1     | 331    |
| 422  | Lago Cielo Estrellado                                 | 1     | 331    |
| 424  | Lago Iris                                             | 1     | 331    |
| 425  | Poza de la Luna                                       | 1     | 331    |
| 426  | Refugio de la Algaba                                  | 1     | 331    |
| 427  | El Rincón Lóbrego                                     | 1     | 331    |
| 428  | Senda de la Noche                                     | 1     | 331    |
| 429  | Xavian                                                | 1     | 331    |
| 430  | Satyrnaar                                             | 1     | 331    |
| 431  | Puesto del Hachazo                                    | 1     | 331    |
| 432  | El Túmulo de Dor'danil                                | 1     | 331    |
| 433  | Río Falfarren                                         | 1     | 331    |
| 434  | Cerro Lumbrevil                                       | 1     | 331    |
| 435  | Barranco del Demonio                                  | 1     | 331    |
| 436  | Cresta del Demonio                                    | 1     | 331    |
| 437  | Aserradero Grito de Guerra                            | 1     | 331    |
| 438  | Talloumbrío                                           | 1     | 331    |
| 439  | El Desierto de Sal                                    | 1     | 400    |
| 440  | Tanaris                                               | 1     | 0      |
| 441  | Lago Falathim                                         | 1     | 331    |
| 442  | Auberdine                                             | 1     | 148    |
| 443  | Ruinas de Mathystra                                   | 1     | 148    |
| 444  | Torre de Althalaxx                                    | 1     | 148    |
| 445  | Salto de Fonroca                                      | 1     | 148    |
| 446  | Bashal'Aran                                           | 1     | 148    |
| 447  | Ameth'Aran                                            | 1     | 148    |
| 448  | Páramo de los Ancianos                                | 1     | 148    |
| 449  | La Espada del Maestro                                 | 1     | 148    |
| 450  | Excavación de Tripirrem                               | 1     | 148    |
| 452  | Cabo de la Niebla                                     | 1     | 148    |
| 453  | Playa del Oleaje                                      | 1     | 148    |
| 454  | Río Culebra                                           | 1     | 148    |
| 455  | Cubil del Bosque Negro                                | 1     | 148    |
| 456  | Río Fonroca                                           | 1     | 148    |
| 457  | Mar de la Bruma                                       | 1     | 0      |
| 458  | Camino del Oro                                        | 1     | 17     |
| 459  | Atalaya Escarlata                                     | 0     | 85     |
| 460  | Refugio Roca del Sol                                  | 1     | 406    |
| 461  | Risco Cortaviento                                     | 1     | 406    |
| 463  | Lago del Peñasco                                      | 1     | 406    |
| 464  | Lago Mirkfallon                                       | 1     | 406    |
| 465  | La Vega Carbonizada                                   | 1     | 406    |
| 466  | Valle Furia Sangrienta                                | 1     | 406    |
| 467  | Cima del Espolón                                      | 1     | 406    |
| 468  | El Cubil del Espolón                                  | 1     | 406    |
| 469  | Vega del Gran Bosque                                  | 1     | 406    |
| 470  | Cima del Trueno UNUSED                                | 1     | 215    |
| 471  | Mesa de Viento Bravo                                  | 1     | 215    |
| 472  | Mesa de La Piedra de Fuego                            | 1     | 215    |
| 473  | Rocamanto                                             | 1     | 215    |
| 474  | Hunter Rise UNUSED                                    | 1     | 215    |
| 475  | Spirit RiseUNUSED                                     | 1     | 215    |
| 476  | Elder RiseUNUSED                                      | 1     | 215    |
| 477  | Ruinas de Jubuwal                                     | 0     | 33     |
| 478  | Estanques de Arlithrien                               | 1     | 141    |
| 479  | Excavación Oximelena                                  | 1     | 400    |
| 480  | Campamento E'thok                                     | 1     | 400    |
| 481  | Risco Pezuña Quebrada                                 | 1     | 400    |
| 482  | Nido Alto                                             | 1     | 400    |
| 483  | Cañón del Chirrido                                    | 1     | 400    |
| 484  | Poblado Viento Libre                                  | 1     | 400    |
| 485  | El Gran Elevador                                      | 1     | 400    |
| 486  | Dominios Galak                                        | 1     | 400    |
| 487  | Guarida Malapluma                                     | 1     | 400    |
| 488  | El Hueco Perdido                                      | 1     | 400    |
| 489  | Thalanaar                                             | 1     | 357    |
| 490  | Cráter de Un'Goro                                     | 1     | 0      |
| 491  | Horado Rajacieno                                      | 47    | 0      |
| 492  | Cementerio del Cerro del Cuervo                       | 0     | 10     |
| 493  | Claro de la Luna                                      | 1     | 0      |
| 495  | Fiordo Aquilonal                                      | 571   | 0      |
| 496  | Poblado Murohelecho                                   | 1     | 15     |
| 497  | Mansión Cienaluz                                      | 1     | 15     |
| 498  | Madriguera de los Cienorrojo                          | 1     | 15     |
| 499  | Cueva Niebla Negra                                    | 1     | 15     |
| 500  | Cabo Moggle                                           | 1     | 15     |
| 501  | Siniestro de Beezil                                   | 1     | 15     |
| 502  | Colina de las Brujas                                  | 1     | 15     |
| 503  | Alto del Centinela                                    | 1     | 15     |
| 504  | Torre de la Punta Norte                               | 1     | 15     |
| 505  | Torre de la Punta Oeste                               | 1     | 15     |
| 506  | Punta Perdida                                         | 1     | 15     |
| 507  | Ciénaga Azul                                          | 1     | 15     |
| 508  | Ruinas Quebrantarrocas                                | 1     | 15     |
| 509  | Cubil de la Llama                                     | 1     | 15     |
| 510  | El Pantano del Dragón                                 | 1     | 15     |
| 511  | Ciénaga de Fuego                                      | 1     | 15     |
| 512  | Poblado Pezuñanegra                                   | 1     | 15     |
| 513  | Isla Theramore                                        | 1     | 15     |
| 514  | Ciudadela Garrida                                     | 1     | 15     |
| 515  | Prisión del Acorazado                                 | 1     | 15     |
| 516  | Bahía Revolcafango                                    | 1     | 15     |
| 517  | Cala Furiamarea                                       | 1     | 15     |
| 518  | Playa Tenebruma                                       | 1     | 15     |
| 536  | Granja de Addle                                       | 0     | 10     |
| 537  | Cresta del Penacho en Llamas                          | 1     | 490    |
| 538  | Fosas de Alquitrán Lakkari                            | 1     | 490    |
| 539  | Camino del Terror                                     | 1     | 490    |
| 540  | La Cicatriz del Desliz                                | 1     | 490    |
| 541  | Refugio de Marshal                                    | 1     | 490    |
| 542  | Roca Fungal                                           | 1     | 490    |
| 543  | Baños de Golakka                                      | 1     | 490    |
| 556  | Loch Modan                                            | 0     | 38     |
| 576  | Refugio de los Mendigos                               | 0     | 10     |
| 596  | Cementerio de Kodos                                   | 1     | 405    |
| 597  | Campamento del Espíritu Errante                       | 1     | 405    |
| 598  | Playa de Sar'theris                                   | 1     | 405    |
| 599  | Fortaleza del Hacha de Trueno                         | 1     | 405    |
| 600  | Cuenca de Bolgan                                      | 1     | 405    |
| 602  | Aquelarre Mannoroc                                    | 1     | 405    |
| 603  | Sargeron                                              | 1     | 405    |
| 604  | Poblado Magram                                        | 1     | 405    |
| 606  | Poblado Gelkis                                        | 1     | 405    |
| 607  | Valle de las Lanzas                                   | 1     | 405    |
| 608  | Punta de Nijel                                        | 1     | 405    |
| 609  | Poblado Kolkar                                        | 1     | 405    |
| 616  | Hyjal                                                 | 1     | 0      |
| 618  | Cuna del Invierno                                     | 1     | 0      |
| 636  | Río Lobonegro                                         | 1     | 406    |
| 637  | Roca de los Kodos                                     | 1     | 215    |
| 638  | Sendero Oculto                                        | 1     | 14     |
| 639  | Roca de los Espíritus                                 | 1     | 14     |
| 640  | Santuario de la Llama Latente                         | 1     | 14     |
| 656  | Lago Elune'ara                                        | 1     | 493    |
| 657  | El Puerto                                             | 0     | 8      |
| 676  | Terrallende                                           | 150   | 0      |
| 696  | Craftsmen's Terrace UNUSED                            | 1     | 141    |
| 697  | Tradesmen's Terrace UNUSED                            | 1     | 141    |
| 698  | The Temple Gardens UNUSED                             | 1     | 141    |
| 699  | Templo de Elune UNUSED                                | 1     | 141    |
| 700  | Cenarion Enclave UNUSED                               | 1     | 141    |
| 701  | Warrior's Terrace UNUSED                              | 1     | 141    |
| 702  | Aldea Rut'theran                                      | 1     | 141    |
| 716  | Complejo Vetaferro                                    | 0     | 1      |
| 717  | Las Mazmorras                                         | 34    | 0      |
| 718  | Cuevas de los Lamentos                                | 43    | 0      |
| 719  | Cavernas de Brazanegra                                | 48    | 0      |
| 720  | Isla de Batalla                                       | 1     | 17     |
| 721  | Gnomeregan                                            | 90    | 0      |
| 722  | Zahúrda Rajacieno                                     | 129   | 0      |
| 736  | Hondonada Ban'ethil                                   | 1     | 141    |
| 796  | Monasterio Escarlata                                  | 189   | 0      |
| 797  | Embarcadero de Jerod                                  | 0     | 12     |
| 798  | Torre de la Peña                                      | 0     | 12     |
| 799  | La Ribera Lóbrega                                     | 0     | 10     |
| 800  | Desfiladero de Crestanevada                           | 0     | 1      |
| 801  | Valle Escalofrío                                      | 0     | 1      |
| 802  | Monte Luz                                             | 0     | 1      |
| 803  | Granja de Semperámbar                                 | 0     | 1      |
| 804  | Las Colinas Tundra                                    | 0     | 1      |
| 805  | Paso de la Puerta Sur                                 | 0     | 1      |
| 806  | Avanzada de la Puerta Sur                             | 0     | 1      |
| 807  | Paso de la Puerta Norte                               | 0     | 1      |
| 808  | Avanzada de la Puerta Norte                           | 0     | 1      |
| 809  | Puertas de Forjaz                                     | 0     | 1      |
| 810  | Charca Aguaserena                                     | 0     | 85     |
| 811  | Vega Pesadilla                                        | 0     | 85     |
| 812  | Vega Venerácnidas                                     | 0     | 85     |
| 813  | El Baluarte                                           | 0     | 28     |
| 814  | Río Furia del Sur                                     | 1     | 14     |
| 815  | Río Furia del Sur                                     | 1     | 17     |
| 816  | Tierras Crines de Acero                               | 1     | 14     |
| 817  | Roca del Cráneo                                       | 1     | 14     |
| 818  | Roca Crines Pálidas                                   | 1     | 215    |
| 819  | Cresta Viento Furioso                                 | 1     | 215    |
| 820  | Las Llanuras Doradas                                  | 1     | 215    |
| 821  | Las Llanuras Onduladas                                | 1     | 215    |
| 836  | Dun Algaz                                             | 0     | 11     |
| 837  | Dun Algaz                                             | 0     | 38     |
| 838  | Paso de la Puerta Norte                               | 0     | 38     |
| 839  | Paso de la Puerta Sur                                 | 0     | 38     |
| 856  | Arboleda del Crepúsculo                               | 0     | 10     |
| 876  | Isla de los MJ                                        | 1     | 0      |
| 877  | Delete ME                                             | 1     | 17     |
| 878  | Río Furia del Sur                                     | 1     | 16     |
| 879  | Río Furia del Sur                                     | 1     | 331    |
| 880  | Puente Thandol                                        | 0     | 45     |
| 881  | Puente Thandol                                        | 0     | 11     |
| 896  | Isla del Purgatorio                                   | 0     | 267    |
| 916  | La Finca de Jansen                                    | 0     | 40     |
| 917  | El Campo Funesto                                      | 0     | 40     |
| 918  | La Granja de Molsen                                   | 0     | 40     |
| 919  | Estanque de Stendel                                   | 0     | 40     |
| 920  | Las Colinas Afiladas                                  | 0     | 40     |
| 921  | Paraje de Demont                                      | 0     | 40     |
| 922  | Los Yermos Polvorientos                               | 0     | 40     |
| 923  | Valle Rompecantos                                     | 0     | 38     |
| 924  | Valle de los Reyes                                    | 0     | 38     |
| 925  | Estación de Algaz                                     | 0     | 38     |
| 926  | La granja de Bucklebree                               | 0     | 130    |
| 927  | La Playa Plateada                                     | 0     | 130    |
| 928  | Hoya de la Marea                                      | 0     | 130    |
| 936  | Fuerte Zarpagris                                      | 0     | 38     |
| 956  | Los Verdegales                                        | 169   | 0      |
| 976  | Gadgetzan                                             | 1     | 440    |
| 977  | Puerto Bonvapor                                       | 1     | 440    |
| 978  | Zul'Farrak                                            | 1     | 440    |
| 979  | Vigía Penas de Arena                                  | 1     | 440    |
| 980  | Valle Cardizal                                        | 1     | 440    |
| 981  | Sima Abierta                                          | 1     | 440    |
| 982  | La Guarida Ponzoñosa                                  | 1     | 440    |
| 983  | Base Machacaduna                                      | 1     | 440    |
| 984  | Ruinas de Lunaeste                                    | 1     | 440    |
| 985  | Campo del Manantial                                   | 1     | 440    |
| 986  | Guarida de Zalashji                                   | 1     | 440    |
| 987  | Playa Finisterrae                                     | 1     | 440    |
| 988  | Playa Baile de las Olas                               | 1     | 440    |
| 989  | Uldum                                                 | 1     | 440    |
| 990  | Valle de los Vigías                                   | 1     | 440    |
| 991  | Puesto de Gunstan                                     | 1     | 440    |
| 992  | Ruinas de Lunasur                                     | 1     | 440    |
| 996  | Campamento de Render                                  | 0     | 44     |
| 997  | Valle de Render                                       | 0     | 44     |
| 998  | Roca de Render                                        | 0     | 44     |
| 999  | Torre de Petravista                                   | 0     | 44     |
| 1000 | Valle de Galardell                                    | 0     | 44     |
| 1001 | Camino del Lago                                       | 0     | 44     |
| 1002 | Tres Caminos                                          | 0     | 44     |
| 1016 | Cerro Fraguaferoz                                     | 0     | 11     |
| 1017 | Colina del Raptor                                     | 0     | 11     |
| 1018 | Pantano del Canal Negro                               | 0     | 11     |
| 1019 | La Franja Verde                                       | 0     | 139    |
| 1020 | Pantano Pellejomusgo                                  | 0     | 11     |
| 1021 | Roca Thelgen                                          | 0     | 11     |
| 1022 | Pantano Branquiazul                                   | 0     | 11     |
| 1023 | Cañada Salobre                                        | 0     | 11     |
| 1024 | Pantano del Ocaso                                     | 0     | 11     |
| 1025 | La Franja Verde                                       | 0     | 11     |
| 1036 | Campamento Dentellada                                 | 0     | 11     |
| 1037 | Grim Batol                                            | 0     | 11     |
| 1038 | Puertas Faucedraco                                    | 0     | 11     |
| 1039 | La Flota Perdida                                      | 0     | 11     |
| 1056 | Colinas de Darrow                                     | 0     | 267    |
| 1057 | Muralla de Thoradin                                   | 0     | 267    |
| 1076 | Senda de las Tejedoras                                | 1     | 406    |
| 1097 | La Ribera Silente                                     | 0     | 10     |
| 1098 | Mansión Mantoniebla                                   | 0     | 10     |
| 1099 | Campamento Mojache                                    | 1     | 357    |
| 1100 | Dominios Tótem Siniestro                              | 1     | 357    |
| 1101 | Las Galerías Retorcidas                               | 1     | 357    |
| 1102 | Lago Ventosalvaje                                     | 1     | 357    |
| 1103 | Avanzada Gordunni                                     | 1     | 357    |
| 1104 | Mok'Gordun                                            | 1     | 357    |
| 1105 | Vega Cicatriz Feral                                   | 1     | 357    |
| 1106 | Tierras Altas de Plumavieja                           | 1     | 357    |
| 1107 | Lago Soplo                                            | 1     | 357    |
| 1108 | La Costa Olvidada                                     | 1     | 357    |
| 1109 | Pilar Este                                            | 1     | 357    |
| 1110 | Pilar Oeste                                           | 1     | 357    |
| 1111 | Rama Oniria                                           | 1     | 357    |
| 1112 | Lago Jademir                                          | 1     | 357    |
| 1113 | Oneiros                                               | 1     | 357    |
| 1114 | Ruinas de Viento Azabache                             | 1     | 357    |
| 1115 | Dominios de los Cicatriz de Rabia                     | 1     | 357    |
| 1116 | Bastión Plumaluna                                     | 1     | 357    |
| 1117 | Ruinas de Solarsal                                    | 1     | 357    |
| 1118 | Lower Wilds UNUSED                                    | 1     | 357    |
| 1119 | Los Dos Colosos                                       | 1     | 357    |
| 1120 | Isla de Sardor                                        | 1     | 357    |
| 1121 | Isla del Terror                                       | 1     | 357    |
| 1136 | Altas Tierras Salvajes                                | 1     | 357    |
| 1137 | Bajas Tierras Salvajes                                | 1     | 357    |
| 1156 | Baldíos del Sur                                       | 1     | 17     |
| 1157 | Camino del Oro Sur                                    | 1     | 17     |
| 1176 | Zul'Farrak                                            | 209   | 0      |
| 1196 | Pináculo de Utgarde                                   | 575   | 0      |
| 1216 | Bastión Fauces de Madera                              | 1     | 16     |
| 1217 | Campamento Vanndir                                    | 1     | 16     |
| 1218 | TESTAzshara                                           | 1     | 16     |
| 1219 | Campamento Legashi                                    | 1     | 16     |
| 1220 | Campamento base thalassiano                           | 1     | 16     |
| 1221 | Ruinas de Eldarath                                    | 1     | 16     |
| 1222 | Guarida de Hetaera                                    | 1     | 16     |
| 1223 | Templo de Zin-Malor                                   | 1     | 16     |
| 1224 | Cabeza de Oso                                         | 1     | 16     |
| 1225 | Ursolan                                               | 1     | 16     |
| 1226 | Templo de Arkkoran                                    | 1     | 16     |
| 1227 | Bahía de la Tempestad                                 | 1     | 16     |
| 1228 | La Playa Arrasada                                     | 1     | 16     |
| 1229 | Torre de Eldara                                       | 1     | 16     |
| 1230 | Arrecife Dentado                                      | 1     | 16     |
| 1231 | Playa del Arrecife Sur                                | 1     | 16     |
| 1232 | Monumento Cresta Cuervo                               | 1     | 16     |
| 1233 | Loma Desolada                                         | 1     | 16     |
| 1234 | Lago Mennar                                           | 1     | 16     |
| 1235 | Santuario Cantosombrío                                | 1     | 16     |
| 1236 | Campamento Haldarr                                    | 1     | 16     |
| 1237 | Valormok                                              | 1     | 16     |
| 1256 | Las Ruinas                                            | 1     | 16     |
| 1276 | El Paso del Espolón                                   | 1     | 331    |
| 1277 | El Paso del Espolón                                   | 1     | 406    |
| 1296 | Granja Rocamuela                                      | 1     | 14     |
| 1297 | La Pocilga                                            | 1     | 14     |
| 1316 | Zahúrda Rajacieno                                     | 1     | 17     |
| 1336 | Cala del Aparejo Perdido                              | 1     | 440    |
| 1337 | Uldaman                                               | 70    | 0      |
| 1338 | Lago Lordamere                                        | 0     | 130    |
| 1339 | Lago Lordamere                                        | 0     | 36     |
| 1357 | Camino de la Horca                                    | 0     | 36     |
| 1377 | Silithus                                              | 1     | 0      |
| 1397 | Bosque Esmeralda                                      | 169   | 0      |
| 1417 | Templo Sumergido                                      | 109   | 0      |
| 1437 | Bastión Machacamiedo                                  | 0     | 4      |
| 1438 | Castillo de Nethergarde                               | 0     | 4      |
| 1439 | Puesto Machacamiedo                                   | 0     | 4      |
| 1440 | Serpiente Enroscada                                   | 0     | 4      |
| 1441 | Altar de la Tempestad                                 | 0     | 4      |
| 1442 | Cresta Vigía                                          | 0     | 51     |
| 1443 | La Fosa de la Escoria                                 | 0     | 51     |
| 1444 | El Mar de las Cenizas                                 | 0     | 51     |
| 1445 | Montaña Roca Negra                                    | 0     | 51     |
| 1446 | Puesto del Torio                                      | 0     | 51     |
| 1457 | Arsenal del Cuartel                                   | 0     | 4      |
| 1477 | El Templo de Atal'Hakkar                              | 109   | 0      |
| 1497 | Entrañas                                              | 0     | 0      |
| 1517 | Uldaman                                               | 0     | 3      |
| 1518 | Not Used Deadmines                                    | 0     | 40     |
| 1519 | Ciudad de Ventormenta                                 | 0     | 0      |
| 1537 | Forjaz                                                | 0     | 0      |
| 1557 | Campamento Pezuña Quebrada                            | 1     | 400    |
| 1577 | El Cabo de Tuercespina                                | 0     | 33     |
| 1578 | Costa Salvaje del Sur                                 | 0     | 33     |
| 1579 | Unused The Deadmines 002                              | 0     | 0      |
| 1580 | Unused Ironclad Cove 003                              | 0     | 1579   |
| 1581 | Las Minas de la Muerte                                | 36    | 0      |
| 1582 | Cala del Acorazado                                    | 36    | 1581   |
| 1583 | Cumbre de Roca Negra                                  | 229   | 0      |
| 1584 | Profundidades de Roca Negra                           | 230   | 0      |
| 1597 | Raptor Grounds UNUSED                                 | 1     | 17     |
| 1598 | Grol'dom Farm UNUSED                                  | 1     | 17     |
| 1599 | Campamento de Mor'shan                                | 1     | 17     |
| 1600 | Honor's Stand UNUSED                                  | 1     | 17     |
| 1601 | Blackthorn Ridge UNUSED                               | 1     | 17     |
| 1602 | Bramblescar UNUSED                                    | 1     | 17     |
| 1603 | Agama'gor UNUSED                                      | 1     | 17     |
| 1617 | Valle de los Héroes                                   | 0     | 1519   |
| 1637 | Orgrimmar                                             | 1     | 0      |
| 1638 | Cima del Trueno                                       | 1     | 0      |
| 1639 | Alto de los Ancestros                                 | 1     | 1638   |
| 1640 | Alto de los Espíritus                                 | 1     | 1638   |
| 1641 | Alto de los Cazadores                                 | 1     | 1638   |
| 1657 | Darnassus                                             | 1     | 0      |
| 1658 | Enclave Cenarion                                      | 1     | 1657   |
| 1659 | Bancal del Artesano                                   | 1     | 1657   |
| 1660 | Bancal del Guerrero                                   | 1     | 1657   |
| 1661 | Los Jardines del Templo                               | 1     | 1657   |
| 1662 | Bancal de los Mercaderes                              | 1     | 1657   |
| 1677 | Saliente de Gavin                                     | 0     | 36     |
| 1678 | Saliente de Sofera                                    | 0     | 36     |
| 1679 | Daga de Corrahn                                       | 0     | 36     |
| 1680 | La Punta                                              | 0     | 36     |
| 1681 | Costa de la Neblina                                   | 0     | 36     |
| 1682 | Redil de Dandred                                      | 0     | 36     |
| 1683 | Caverna Estrecha                                      | 0     | 36     |
| 1684 | Alto del Orvallo                                      | 0     | 36     |
| 1697 | Tierras de los Raptores                               | 1     | 17     |
| 1698 | Rajazarza                                             | 1     | 17     |
| 1699 | Colina Espinosa                                       | 1     | 17     |
| 1700 | Agama'gor                                             | 1     | 17     |
| 1701 | Loma Espina Negra                                     | 1     | 17     |
| 1702 | El Alto del Honor                                     | 1     | 17     |
| 1703 | La Empalizada de Mor'shan                             | 1     | 17     |
| 1704 | Granja de Grol'dom                                    | 1     | 17     |
| 1717 | Horado Rajacieno                                      | 1     | 17     |
| 1718 | El Gran Elevador                                      | 1     | 17     |
| 1737 | Valle del Velo de Bruma                               | 0     | 33     |
| 1738 | Manantial Nek'mani                                    | 0     | 33     |
| 1739 | Dominios Velasangre                                   | 0     | 33     |
| 1740 | Base de Ventura y Cía.                                | 0     | 33     |
| 1741 | Arena Gurubashi                                       | 0     | 33     |
| 1742 | Cubil del Espíritu                                    | 0     | 33     |
| 1757 | El Velo Carmesí                                       | 0     | 33     |
| 1758 | Las Mareas Vivas                                      | 0     | 33     |
| 1759 | La Damisela Afortunada                                | 0     | 33     |
| 1760 | Centro de Operaciones de Ventura y Cía.               | 0     | 33     |
| 1761 | Aldea Muertobosque                                    | 1     | 361    |
| 1762 | Poblado Zarpavil                                      | 1     | 361    |
| 1763 | Jaedenar                                              | 1     | 361    |
| 1764 | Río del Veneno                                        | 1     | 361    |
| 1765 | Cascadas del Veneno                                   | 1     | 361    |
| 1766 | Cañada Gran Cicatriz                                  | 1     | 361    |
| 1767 | Bosque de Troncoferro                                 | 1     | 361    |
| 1768 | Caverna de Troncoferro                                | 1     | 361    |
| 1769 | Bastión Fauces de Madera                              | 1     | 361    |
| 1770 | Guarida Sombría                                       | 1     | 361    |
| 1771 | Santuario del Impostor                                | 1     | 361    |
| 1777 | Cueva de Itharius                                     | 0     | 8      |
| 1778 | Tinieblas de las Penas                                | 0     | 8      |
| 1779 | Aldea Draenil'dur                                     | 0     | 8      |
| 1780 | Cruce Lanzarrota                                      | 0     | 8      |
| 1797 | Stagalbog                                             | 0     | 8      |
| 1798 | Lodo Traicionero                                      | 0     | 8      |
| 1817 | Cueva Stagalbog                                       | 0     | 8      |
| 1837 | Cuevas Secacorteza                                    | 0     | 45     |
| 1857 | Muralla de Thoradin                                   | 0     | 45     |
| 1858 | Boulder'gor                                           | 0     | 45     |
| 1877 | Valle de los Colmillos                                | 0     | 3      |
| 1878 | Terraseca                                             | 0     | 3      |
| 1879 | Explanada del Espejismo                               | 0     | 3      |
| 1880 | Cobertizo de Barbapluma                               | 0     | 47     |
| 1881 | Campamento Machacacanillas                            | 0     | 47     |
| 1882 | Barranco Bruma Enferma                                | 0     | 47     |
| 1883 | Lago Ventobravo                                       | 0     | 47     |
| 1884 | Agol'watha                                            | 0     | 47     |
| 1885 | Hiri'watha                                            | 0     | 47     |
| 1886 | Las Ruinas Abyectas                                   | 0     | 47     |
| 1887 | Arrecife de Bogen                                     | 0     | 47     |
| 1897 | Bancal del Hacedor                                    | 0     | 3      |
| 1898 | Barranco Viento Seco                                  | 0     | 3      |
| 1917 | Shaol'watha                                           | 0     | 47     |
| 1937 | Ruinas Sombrasol                                      | 1     | 440    |
| 1938 | Pilar Partido                                         | 1     | 440    |
| 1939 | Arenas Abisales                                       | 1     | 440    |
| 1940 | Tierras del Sur                                       | 1     | 440    |
| 1941 | Cavernas del Tiempo                                   | 1     | 0      |
| 1942 | Los Pantanales                                        | 1     | 490    |
| 1943 | Meseta Roca de Hierro                                 | 1     | 490    |
| 1957 | Cueva Tizonegro                                       | 0     | 51     |
| 1958 | Base de Peleteros                                     | 0     | 51     |
| 1959 | Valle Polvofuego                                      | 0     | 51     |
| 1977 | Zul'Gurub                                             | 309   | 0      |
| 1978 | Puesto Juncobruma                                     | 0     | 8      |
| 1997 | Puesto del Veneno                                     | 1     | 361    |
| 1998 | Claro Ramaespolón                                     | 1     | 361    |
| 2017 | Stratholme                                            | 329   | 0      |
| 2037 | Quel'thalas                                           | 0     | 0      |
| 2057 | Scholomance                                           | 289   | 0      |
| 2077 | Vega Crepuscular                                      | 1     | 148    |
| 2078 | Orilla Crepuscular                                    | 1     | 148    |
| 2079 | Isla de Alcaz                                         | 1     | 15     |
| 2097 | Cumbre de la Nube Negra                               | 1     | 400    |
| 2098 | Catacumbas del Bosque Aurora                          | 0     | 10     |
| 2099 | Fuerte de Petravista                                  | 0     | 44     |
| 2100 | Maraudon                                              | 349   | 0      |
| 2101 | Pensión La Cebada                                     | 0     | 38     |
| 2102 | Destilería Cebatruenos                                | 0     | 1      |
| 2103 | Castillo de Menethil                                  | 0     | 11     |
| 2104 | Mesón Aguahonda                                       | 0     | 11     |
| 2117 | Sepulcro Sombrío                                      | 0     | 85     |
| 2118 | Concejo de Rémol                                      | 0     | 85     |
| 2119 | Mesón La Horca                                        | 0     | 85     |
| 2137 | The Pools of VisionUNUSED                             | 1     | 215    |
| 2138 | Cubil Calígine                                        | 1     | 17     |
| 2157 | Fortaleza de Bael'dun                                 | 1     | 17     |
| 2158 | Cubil de Brasaliza                                    | 1     | 15     |
| 2159 | Guarida de Onyxia                                     | 1     | 0      |
| 2160 | Mina Cortaviento                                      | 1     | 406    |
| 2161 | Condena de Roland                                     | 0     | 10     |
| 2177 | Liza                                                  | 0     | 33     |
| 2197 | Pozas de las Visiones                                 | 1     | 1638   |
| 2198 | Barranco Rompesombras                                 | 1     | 405    |
| 2217 | Aldea Lanza Partida                                   | 1     | 405    |
| 2237 | Campamento del Tramo Blanco                           | 1     | 400    |
| 2238 | Gornia                                                | 1     | 400    |
| 2239 | Cráter del Ojo de Zane                                | 1     | 400    |
| 2240 | Circuito del Espejismo                                | 1     | 400    |
| 2241 | Roca Sable de Hielo                                   | 1     | 618    |
| 2242 | La Arboleda Oculta                                    | 1     | 618    |
| 2243 | Puesto de los Fauces de Madera                        | 1     | 618    |
| 2244 | Poblado Nevada                                        | 1     | 618    |
| 2245 | Mazthoril                                             | 1     | 618    |
| 2246 | Baños de Fuego de Escarcha                            | 1     | 618    |
| 2247 | Colinas Cardo Nevado                                  | 1     | 618    |
| 2248 | Dun Mandarr                                           | 1     | 618    |
| 2249 | Cañón Levescarcha                                     | 1     | 618    |
| 2250 | Matorral del Ala del Búho                             | 1     | 618    |
| 2251 | Lago Kel'Theril                                       | 1     | 618    |
| 2252 | Las Ruinas de Kel'Theril                              | 1     | 618    |
| 2253 | Aldea Estrella Fugaz                                  | 1     | 618    |
| 2254 | Túmulo de Ban'Thallow                                 | 1     | 618    |
| 2255 | Vista Eterna                                          | 1     | 618    |
| 2256 | Garganta Negro Rumor                                  | 1     | 618    |
| 2257 | Tranvía Subterráneo                                   | 369   | 0      |
| 2258 | Cuenca Fungal                                         | 0     | 139    |
| 2259 | UNUSEDThe Marris Stead                                | 0     | 139    |
| 2260 | Hacienda de Marris                                    | 0     | 139    |
| 2261 | La Subgranja                                          | 0     | 139    |
| 2262 | Villa Darrow                                          | 0     | 139    |
| 2263 | Torre de la Corona                                    | 0     | 139    |
| 2264 | Cruce de Corin                                        | 0     | 139    |
| 2265 | Base Escarlata                                        | 0     | 139    |
| 2266 | Mano de Tyr                                           | 0     | 139    |
| 2267 | La Basílica Escarlata                                 | 0     | 139    |
| 2268 | Capilla de la Esperanza de la Luz                     | 0     | 139    |
| 2269 | Molino Cejifrente                                     | 0     | 139    |
| 2270 | El Claro Ponzoñoso                                    | 0     | 139    |
| 2271 | Torre de la Muralla del Este                          | 0     | 139    |
| 2272 | Vallenorte                                            | 0     | 139    |
| 2273 | Zul'Mashar                                            | 0     | 139    |
| 2274 | Mazra'Alor                                            | 0     | 139    |
| 2275 | Torre del Paso Norte                                  | 0     | 139    |
| 2276 | Refugio Quel'Lithien                                  | 0     | 139    |
| 2277 | Bosque de la Peste                                    | 0     | 139    |
| 2278 | Fuerte de la Plaga                                    | 0     | 139    |
| 2279 | Stratholme                                            | 0     | 139    |
| 2280 | DO NOT USE                                            | 0     | 0      |
| 2297 | Lago Darrowmere                                       | 0     | 28     |
| 2298 | Castel Darrow                                         | 0     | 28     |
| 2299 | Lago Darrowmere                                       | 0     | 139    |
| 2300 | Cavernas del Tiempo                                   | 1     | 440    |
| 2301 | Poblado Piel de Cardo                                 | 1     | 331    |
| 2302 | El Lodazal                                            | 1     | 15     |
| 2303 | Cañón Rompevientos                                    | 1     | 400    |
| 2317 | Mares del Sur                                         | 1     | 440    |
| 2318 | Mare Magnum                                           | 1     | 15     |
| 2319 | Mare Magnum                                           | 1     | 17     |
| 2320 | Mare Magnum                                           | 1     | 14     |
| 2321 | Mare Magnum                                           | 1     | 16     |
| 2322 | Mar de la Bruma                                       | 1     | 141    |
| 2323 | Mar de la Bruma                                       | 1     | 357    |
| 2324 | Mar de la Bruma                                       | 1     | 405    |
| 2325 | Mar de la Bruma                                       | 1     | 331    |
| 2326 | Mar de la Bruma                                       | 1     | 148    |
| 2337 | Cuartel de Cerrotajo                                  | 1     | 14     |
| 2338 | Mares del Sur                                         | 0     | 33     |
| 2339 | Mare Magnum                                           | 0     | 33     |
| 2357 | Asentamiento Sangradientes                            | 1     | 331    |
| 2358 | Canción del Bosque                                    | 1     | 331    |
| 2359 | Poblado Zarpaverde                                    | 1     | 331    |
| 2360 | Avanzada Ala de Plata                                 | 1     | 331    |
| 2361 | Amparo de la Noche                                    | 1     | 493    |
| 2362 | Santuario de Remulos                                  | 1     | 493    |
| 2363 | Túmulo de Tempestira                                  | 1     | 493    |
| 2364 | Mare Magnum                                           | 0     | 40     |
| 2365 | Mare Magnum                                           | 0     | 11     |
| 2366 | La Ciénaga Negra                                      | 269   | 0      |
| 2367 | Antiguas Laderas de Trabalomas                        | 560   | 0      |
| 2368 | Molino Tarren                                         | 560   | 2367   |
| 2369 | Costasur                                              | 560   | 2367   |
| 2370 | Castillo de Durnholde                                 | 560   | 2367   |
| 2371 | Dun Garok                                             | 560   | 2367   |
| 2372 | Campos de Trabalomas                                  | 560   | 2367   |
| 2373 | Playa del Este                                        | 560   | 2367   |
| 2374 | Granja Nethander                                      | 560   | 2367   |
| 2375 | Colinas de Darrow                                     | 560   | 2367   |
| 2376 | Torre Austral                                         | 560   | 2367   |
| 2377 | Muralla de Thoradin                                   | 560   | 2367   |
| 2378 | Playa del Oeste                                       | 560   | 2367   |
| 2379 | Mina Azur                                             | 560   | 2367   |
| 2397 | Mare Magnum                                           | 0     | 267    |
| 2398 | Mare Magnum                                           | 0     | 130    |
| 2399 | Mare Magnum                                           | 0     | 85     |
| 2400 | Mar Adusto                                            | 0     | 47     |
| 2401 | Mar Adusto                                            | 0     | 45     |
| 2402 | Mar Adusto                                            | 0     | 11     |
| 2403 | Mar Adusto                                            | 0     | 8      |
| 2404 | Tethris Aran                                          | 1     | 405    |
| 2405 | Ethel Rethor                                          | 1     | 405    |
| 2406 | Isla Ranazjar                                         | 1     | 405    |
| 2407 | Cabaña de Kormek                                      | 1     | 405    |
| 2408 | Aldea Cazasombras                                     | 1     | 405    |
| 2417 | Desfiladero de Roca Negra                             | 0     | 46     |
| 2418 | Vigilia de Morgan                                     | 0     | 46     |
| 2419 | Roca Desliz                                           | 0     | 46     |
| 2420 | Senda del Ala del Terror                              | 0     | 46     |
| 2421 | Draco'dar                                             | 0     | 46     |
| 2437 | Sima Ígnea                                            | 389   | 0      |
| 2457 | Bosque Arrullanoche                                   | 1     | 331    |
| 2477 | Mar de la Bruma                                       | 1     | 1377   |
| 2478 | Morlos'Aran                                           | 1     | 361    |
| 2479 | Santuario Esmeralda                                   | 1     | 361    |
| 2480 | Cañada Fuego de Jade                                  | 1     | 361    |
| 2481 | Ruinas de Constellas                                  | 1     | 361    |
| 2497 | Costa Amarga                                          | 1     | 16     |
| 2517 | Alto de los Rapiñadores                               | 0     | 4      |
| 2518 | Pabellón de Lariss                                    | 1     | 357    |
| 2519 | Colinas Zarpaleña                                     | 1     | 357    |
| 2520 | Guarida de los Zarpaleña                              | 1     | 357    |
| 2521 | Río Verdantis                                         | 1     | 357    |
| 2522 | Ruinas de Isildien                                    | 1     | 357    |
| 2537 | Poblado Tótem Siniestro                               | 1     | 406    |
| 2538 | Campamento Aparaje                                    | 1     | 406    |
| 2539 | Malaka'jin                                            | 1     | 406    |
| 2540 | Barranco del Alud                                     | 1     | 406    |
| 2541 | Cañón Sishir                                          | 1     | 406    |
| 2557 | La Masacre                                            | 429   | 0      |
| 2558 | Barranco de la Muerte                                 | 0     | 41     |
| 2559 | Río Diamante                                          | 0     | 41     |
| 2560 | Campamento de Ariden                                  | 0     | 41     |
| 2561 | El Vicio                                              | 0     | 41     |
| 2562 | Karazhan                                              | 0     | 41     |
| 2563 | Terreno de Morgan                                     | 0     | 41     |
| 2577 | La Masacre                                            | 1     | 357    |
| 2597 | Valle de Alterac                                      | 30    | 0      |
| 2617 | Campamento de los Mezclatornillos                     | 1     | 405    |
| 2618 | Camino Fuego de Jade                                  | 1     | 361    |
| 2619 | Río Thondroril                                        | 0     | 139    |
| 2620 | Río Thondroril                                        | 0     | 28     |
| 2621 | Lago Mereldar                                         | 0     | 139    |
| 2622 | Cicatriz Pestilente                                   | 0     | 139    |
| 2623 | La Cicatriz Purulenta                                 | 0     | 139    |
| 2624 | Lago del Bosque Negro                                 | 0     | 139    |
| 2625 | Puerta de la Muralla del Este                         | 0     | 139    |
| 2626 | Túnel Terroarácnido                                   | 0     | 139    |
| 2627 | Valle del Terror                                      | 0     | 139    |
| 2637 | Fuerte de Kargathia                                   | 1     | 331    |
| 2657 | Valle de los Huesos                                   | 1     | 405    |
| 2677 | Guarida de Alanegra                                   | 469   | 0      |
| 2697 | Cruce de la Muerte                                    | 0     | 41     |
| 2717 | Núcleo de Magma                                       | 409   | 0      |
| 2737 | El Muro del Escarabajo                                | 1     | 1377   |
| 2738 | Aldea del Viento del Sur                              | 1     | 1377   |
| 2739 | Campamento Crepúsculo                                 | 1     | 1377   |
| 2740 | La Vega de Cristal                                    | 1     | 1377   |
| 2741 | Estrado del Escarabajo                                | 1     | 1377   |
| 2742 | Colmen'Ashi                                           | 1     | 1377   |
| 2743 | Colmen'Zora                                           | 1     | 1377   |
| 2744 | Colmen'Regal                                          | 1     | 1377   |
| 2757 | Santuario del Guerrero Caído                          | 1     | 17     |
| 2777 | UNUSED Alterac Valley                                 | 0     | 267    |
| 2797 | Cavernas de Brazanegra                                | 1     | 331    |
| 2817 | Bosque Canto de Cristal                               | 571   | 0      |
| 2837 | El Sótano del Maestro                                 | 0     | 41     |
| 2838 | Paso de Fraguapiedra                                  | 0     | 51     |
| 2839 | Valle de Alterac                                      | 0     | 36     |
| 2857 | La Jaula del Rugido                                   | 1     | 440    |
| 2877 | Chunk Test                                            | 451   | 22     |
| 2897 | Avanzada de Zoram'gar                                 | 1     | 331    |
| 2917 | Sala de las Leyendas                                  | 1     | 0      |
| 2918 | Sala de los Campeones                                 | 449   | 0      |
| 2937 | Dominios Grosh'gok                                    | 0     | 41     |
| 2938 | Desfiladero del Letargo                               | 0     | 41     |
| 2957 | Mina Ferrohondo                                       | 30    | 2597   |
| 2958 | Avanzada Piedrahogar                                  | 30    | 2597   |
| 2959 | Dun Baldar                                            | 30    | 2597   |
| 2960 | Paso de Ala Gélida                                    | 30    | 2597   |
| 2961 | Aldea Lobo Gélido                                     | 30    | 2597   |
| 2962 | Torre de la Punta                                     | 30    | 2597   |
| 2963 | Mina Dentefrío                                        | 30    | 2597   |
| 2964 | Fuerte Hacha Invernal                                 | 30    | 2597   |
| 2977 | Baluarte Sangrehielo                                  | 30    | 2597   |
| 2978 | Bastión Lobo Gélido                                   | 30    | 2597   |
| 2979 | Granja Tor'kren                                       | 1     | 14     |
| 3017 | Paso de la Daga Escarcha                              | 30    | 2597   |
| 3037 | Campamento Roca de Hierro                             | 1     | 400    |
| 3038 | Cráter de la Comadreja                                | 1     | 400    |
| 3039 | Ruinas de Tahonda                                     | 1     | 400    |
| 3057 | Tierra de Disputa                                     | 30    | 2597   |
| 3058 | Cueva Ala Gélida                                      | 30    | 2597   |
| 3077 | Sosiego del Valor                                     | 1     | 1377   |
| 3097 | El Pilar de la Ascensión                              | 1     | 1377   |
| 3098 | Puesto Crepúsculo                                     | 1     | 1377   |
| 3099 | Avanzada Crepúsculo                                   | 1     | 1377   |
| 3100 | Campamento Crepúsculo Devastado                       | 1     | 1377   |
| 3117 | Guarida de Shalzaru                                   | 1     | 357    |
| 3137 | Punta Talrendis                                       | 1     | 16     |
| 3138 | Sagrario de Rethress                                  | 1     | 16     |
| 3139 | Cubil del Horror de la Luna                           | 1     | 618    |
| 3140 | Cueva de Barbaescamas                                 | 1     | 16     |
| 3157 | Cueva del Alud                                        | 1     | 406    |
| 3177 | Campo de trabajos forzados Grito de Guerra            | 1     | 331    |
| 3197 | Campamento del Orvallo                                | 0     | 28     |
| 3217 | La Marra                                              | 429   | 2557   |
| 3237 | The Maul UNUSED                                       | 429   | 2557   |
| 3257 | Huesos de Grakkarond                                  | 1     | 1377   |
| 3277 | Garganta Grito de Guerra                              | 489   | 0      |
| 3297 | Cementerio Lobo Gélido                                | 30    | 2597   |
| 3298 | Paso Lobo Gélido                                      | 30    | 2597   |
| 3299 | Paso de Dun Baldar                                    | 30    | 2597   |
| 3300 | Cementerio Sangrehielo                                | 30    | 2597   |
| 3301 | Cementerio Avalancha                                  | 30    | 2597   |
| 3302 | Cementerio Piedrahogar                                | 30    | 2597   |
| 3303 | Cementerio Pico Tormenta                              | 30    | 2597   |
| 3304 | Búnker Ala Gélida                                     | 30    | 2597   |
| 3305 | Búnker Piedrahogar                                    | 30    | 2597   |
| 3306 | Risco Zarpa Salvaje                                   | 30    | 2597   |
| 3317 | Poblado Sañadiente                                    | 0     | 47     |
| 3318 | Roca de Durotan                                       | 30    | 2597   |
| 3319 | Claro Ala de Plata                                    | 1     | 331    |
| 3320 | Serrería Grito de Guerra                              | 489   | 3277   |
| 3321 | Bastión Ala de Plata                                  | 489   | 3277   |
| 3337 | Caverna Zarpa Salvaje                                 | 30    | 2597   |
| 3338 | La Grieta Velada                                      | 30    | 2597   |
| 3357 | Isla Yojamba                                          | 0     | 33     |
| 3358 | Cuenca de Arathi                                      | 529   | 0      |
| 3377 | El Serpenteo                                          | 309   | 1977   |
| 3378 | Altar de Hir'eek                                      | 309   | 1977   |
| 3379 | Shadra'zaar                                           | 309   | 1977   |
| 3380 | Dominios Hakkari                                      | 309   | 1977   |
| 3381 | Saliente de Shirvallah                                | 309   | 1977   |
| 3382 | Templo de Bethekk                                     | 309   | 1977   |
| 3383 | Foso de las Llamas de Sangre                          | 309   | 1977   |
| 3384 | Altar del Dios de la Sangre                           | 309   | 1977   |
| 3397 | Alto de Zanza                                         | 309   | 1977   |
| 3398 | Extremo de la Locura                                  | 309   | 1977   |
| 3417 | Bastión de Aterratrols                                | 529   | 3358   |
| 3418 | Guarida de los Rapiñadores                            | 529   | 3358   |
| 3419 | Punta de Pagle                                        | 309   | 1977   |
| 3420 | Granja                                                | 529   | 3358   |
| 3421 | Herrería                                              | 529   | 3358   |
| 3422 | Aserradero                                            | 529   | 3358   |
| 3423 | Mina de oro                                           | 529   | 3358   |
| 3424 | Establos                                              | 529   | 3358   |
| 3425 | Fuerte Cenarion                                       | 1     | 1377   |
| 3426 | Punta de Corzocelada                                  | 1     | 1377   |
| 3427 | Campamento Barbabronce                                | 1     | 1377   |
| 3428 | Ahn'Qiraj                                             | 531   | 0      |
| 3429 | Ruinas de Ahn'Qiraj                                   | 509   | 0      |
| 3430 | Bosque Canción Eterna                                 | 530   | 0      |
| 3431 | Isla del Caminante del Sol                            | 530   | 3430   |
| 3432 | Santuario de Dath'Remar                               | 530   | 3430   |
| 3433 | Tierras Fantasma                                      | 530   | 0      |
| 3434 | Bancal del Escarabajo                                 | 531   | 3428   |
| 3435 | Bancal del General                                    | 531   | 3428   |
| 3436 | La Presa                                              | 531   | 3428   |
| 3437 | El Criadero                                           | 531   | 3428   |
| 3438 | El Panal                                              | 531   | 3428   |
| 3439 | Bancal de los Oteadores                               | 531   | 3428   |
| 3440 | Bancal del Escarabajo                                 | 509   | 3429   |
| 3441 | Bancal del General                                    | 509   | 3429   |
| 3442 | La Presa                                              | 509   | 3429   |
| 3443 | El Criadero                                           | 509   | 3429   |
| 3444 | El Panal                                              | 509   | 3429   |
| 3445 | Bancal de los Oteadores                               | 509   | 3429   |
| 3446 | Paseo Crepúsculo                                      | 1     | 1377   |
| 3447 | Guarida de Ortell                                     | 1     | 1377   |
| 3448 | Bancal del Escarabajo                                 | 509   | 3429   |
| 3449 | Bancal del General                                    | 509   | 3429   |
| 3450 | La Presa                                              | 509   | 3429   |
| 3451 | El Criadero                                           | 509   | 3429   |
| 3452 | El Panal                                              | 509   | 3429   |
| 3453 | Bancal de los Oteadores                               | 509   | 3429   |
| 3454 | Ruinas de Ahn'Qiraj                                   | 1     | 1377   |
| 3455 | El Mar del Norte                                      | 530   | 0      |
| 3456 | Naxxramas                                             | 533   | 0      |
| 3457 | Karazhan                                              | 532   | 0      |
| 3459 | Ciudad                                                | 0     | 0      |
| 3460 | La Ensenada Dorada                                    | 530   | 3430   |
| 3461 | Fondeadero Vela del Sol                               | 530   | 3430   |
| 3462 | Aldea Brisa Pura                                      | 530   | 3430   |
| 3463 | Puerta Magister                                       | 530   | 3430   |
| 3464 | El Retiro del Errante                                 | 530   | 3430   |
| 3465 | Sagrario del Norte                                    | 530   | 3430   |
| 3466 | Sagrario del Oeste                                    | 530   | 3430   |
| 3467 | Sagrario del Este                                     | 530   | 3430   |
| 3468 | Refugio de Saltheril                                  | 530   | 3430   |
| 3469 | Caballería de Thuron                                  | 530   | 3430   |
| 3470 | Charca Plácido Susurro                                | 530   | 3430   |
| 3471 | El Bosque Viviente                                    | 530   | 3430   |
| 3472 | Costa Bris Azur                                       | 530   | 3430   |
| 3473 | Lago Elrendar                                         | 530   | 3430   |
| 3474 | La Arboleda Agostada                                  | 530   | 3430   |
| 3475 | Zeb'Watha                                             | 530   | 3430   |
| 3476 | Tor'Watha                                             | 530   | 3430   |
| 3477 | Azjol-Nerub                                           | 571   | 0      |
| 3478 | Puerta de Ahn'Qiraj                                   | 1     | 0      |
| 3479 | Mar de la Bruma                                       | 530   | 0      |
| 3480 | Tierras Ocaso Marchito                                | 530   | 3430   |
| 3481 | Aguja Ocaso Marchito                                  | 530   | 3430   |
| 3482 | La Cicatriz Muerta                                    | 530   | 3430   |
| 3483 | Península del Fuego Infernal                          | 530   | 0      |
| 3484 | La Aguja del Sol                                      | 530   | 3430   |
| 3485 | Academia Falthrien                                    | 530   | 3430   |
| 3486 | Mansión Ravenholdt                                    | 0     | 36     |
| 3487 | Ciudad de Lunargenta                                  | 530   | 0      |
| 3488 | Tranquillien                                          | 530   | 3433   |
| 3489 | Aldea Corona del Sol                                  | 530   | 3433   |
| 3490 | Aldea Bruma Dorada                                    | 530   | 3433   |
| 3491 | Aldea Brisaveloz                                      | 530   | 3433   |
| 3492 | Aguja Brisaveloz                                      | 530   | 3433   |
| 3493 | Sagrario del Sol                                      | 530   | 3433   |
| 3494 | Sagrario de la Luna                                   | 530   | 3433   |
| 3495 | Aguja de la Estrella del Alba                         | 530   | 3433   |
| 3496 | Enclave del Errante                                   | 530   | 3433   |
| 3497 | An'daroth                                             | 530   | 3433   |
| 3498 | An'telas                                              | 530   | 3433   |
| 3499 | An'owyn                                               | 530   | 3433   |
| 3500 | Ciudad de la Muerte                                   | 530   | 3433   |
| 3501 | Zigurat Sangrante                                     | 530   | 3433   |
| 3502 | Zigurat Aullante                                      | 530   | 3433   |
| 3503 | Isla Shalandis                                        | 530   | 3433   |
| 3504 | Los Dominios Toryl                                    | 530   | 3433   |
| 3505 | Minas Sondaluz                                        | 530   | 3433   |
| 3506 | Dominios Andilien                                     | 530   | 3433   |
| 3507 | Colinas Hacha                                         | 530   | 3433   |
| 3508 | Paso de Amani                                         | 530   | 3433   |
| 3509 | Cima Rasguño de Sol                                   | 530   | 3433   |
| 3510 | Catacumbas Amani                                      | 530   | 3433   |
| 3511 | Torre de los Condenados                               | 530   | 3433   |
| 3512 | Zeb'Sora                                              | 530   | 3433   |
| 3513 | Lago Elrendar                                         | 530   | 3433   |
| 3514 | La Cicatriz Muerta                                    | 530   | 3433   |
| 3515 | Río Elrendar                                          | 530   | 3433   |
| 3516 | Zeb'Tela                                              | 530   | 3433   |
| 3517 | Zeb'Nowa                                              | 530   | 3433   |
| 3518 | Nagrand                                               | 530   | 0      |
| 3519 | Bosque de Terokkar                                    | 530   | 0      |
| 3520 | Valle Sombraluna                                      | 530   | 0      |
| 3521 | Marisma de Zangar                                     | 530   | 0      |
| 3522 | Montañas Filospada                                    | 530   | 0      |
| 3523 | Tormenta Abisal                                       | 530   | 0      |
| 3524 | Isla Bruma Azur                                       | 530   | 0      |
| 3525 | Isla Bruma de Sangre                                  | 530   | 0      |
| 3526 | Valle Ammen                                           | 530   | 3524   |
| 3527 | Lugar del Accidente                                   | 530   | 3524   |
| 3528 | Lago Lineargenta                                      | 530   | 3524   |
| 3529 | Matorral Cubrebosque                                  | 530   | 3524   |
| 3530 | Cresta de las Sombras                                 | 530   | 3524   |
| 3531 | El Frontal de la Muerte                               | 530   | 3430   |
| 3532 | Calle del Alba                                        | 530   | 3430   |
| 3533 | Ruinas de Lunargenta                                  | 530   | 3430   |
| 3534 | Camino de Feth                                        | 530   | 3430   |
| 3535 | Ciudadela del Fuego Infernal                          | 540   | 0      |
| 3536 | Thrallmar                                             | 530   | 3483   |
| 3537 | Tundra Boreal                                         | 571   | 0      |
| 3538 | Bastión del Honor                                     | 530   | 3483   |
| 3539 | Los Peldaños del Destino                              | 530   | 3483   |
| 3540 | El Vacío Abisal                                       | 530   | 0      |
| 3541 | Campamento Forja: Mageddon                            | 530   | 3483   |
| 3542 | El Camino a la Gloria                                 | 530   | 3483   |
| 3543 | La Gran Fisura                                        | 530   | 3483   |
| 3544 | Llanura de los Fragmentos                             | 530   | 3483   |
| 3545 | Ciudadela del Fuego Infernal                          | 530   | 3483   |
| 3546 | Armería de Expedición                                 | 530   | 3483   |
| 3547 | Trono de Kil'Jaeden                                   | 530   | 3483   |
| 3548 | Campamento Forja: Ira                                 | 530   | 3483   |
| 3549 | Punto de invasión: Aniquilador                        | 530   | 3483   |
| 3550 | Ruinas Borune                                         | 530   | 3483   |
| 3551 | Ruinas de Sha'naar                                    | 530   | 3483   |
| 3552 | Templo de Telhamat                                    | 530   | 3483   |
| 3553 | Pozas de Aggonar                                      | 530   | 3483   |
| 3554 | Avanzada del Halcón                                   | 530   | 3483   |
| 3555 | Puesto Mag'har                                        | 530   | 3483   |
| 3556 | Cubil de Haal'esh                                     | 530   | 3483   |
| 3557 | El Exodar                                             | 530   | 0      |
| 3558 | Cascadas Elrendar                                     | 530   | 3430   |
| 3559 | Colinas Cubrebosque                                   | 530   | 3524   |
| 3560 | Campos Ammen                                          | 530   | 3524   |
| 3561 | La Arboleda Sagrada                                   | 530   | 3524   |
| 3562 | Murallas del Fuego Infernal                           | 543   | 0      |
| 3563 | Ciudadela del Fuego Infernal                          | 543   | 3562   |
| 3564 | El Claro de Ascuas                                    | 530   | 3524   |
| 3565 | Refugio Cenarion                                      | 530   | 3521   |
| 3566 | Túmulo Lunala                                         | 530   | 3524   |
| 3567 | La Maraña de Cápsulas                                 | 530   | 3524   |
| 3568 | El Cementerio de Cápsulas                             | 530   | 3524   |
| 3569 | Hoya Mareanorte                                       | 530   | 3524   |
| 3570 | Punto Escama de Cólera                                | 530   | 3524   |
| 3571 | Aldea Brazolanudo                                     | 530   | 3524   |
| 3572 | Bastión Semprepino                                    | 530   | 3524   |
| 3573 | Desembarco de Odesyus                                 | 530   | 3524   |
| 3574 | Atracadero de Valaar                                  | 530   | 3524   |
| 3575 | La Costa de Cieno                                     | 530   | 3524   |
| 3576 | Avanzada Azur                                         | 530   | 3524   |
| 3577 | Campamento de Geezle                                  | 530   | 3524   |
| 3578 | Restos del Arca                                       | 530   | 3524   |
| 3579 | Cala del Traidor                                      | 530   | 3524   |
| 3580 | Cima Ventosalvaje                                     | 530   | 3524   |
| 3581 | Senda Ventosalvaje                                    | 530   | 3524   |
| 3582 | Zeth'Gor                                              | 530   | 3483   |
| 3583 | Costa de Berilo                                       | 530   | 3525   |
| 3584 | Avanzada de Sangre                                    | 530   | 3525   |
| 3585 | Bosquespada                                           | 530   | 3525   |
| 3586 | La Espiral Vectorial                                  | 530   | 3525   |
| 3587 | El Pistón de Distorsión                               | 530   | 3525   |
| 3588 | El Crionúcleo                                         | 530   | 3525   |
| 3589 | El Tramo Carmesí                                      | 530   | 3525   |
| 3590 | Guarida Escama de Cólera                              | 530   | 3525   |
| 3591 | Ruinas de Loreth'Aran                                 | 530   | 3525   |
| 3592 | Nazzivian                                             | 530   | 3525   |
| 3593 | Axxarien                                              | 530   | 3525   |
| 3594 | Costa Cienonegro                                      | 530   | 3525   |
| 3595 | La Poza del Hediondo                                  | 530   | 3525   |
| 3596 | El Arrecife Oculto                                    | 530   | 3525   |
| 3597 | Paso de Redámbar                                      | 530   | 3525   |
| 3598 | Isla Cicatriz de Vermis                               | 530   | 3525   |
| 3599 | Alto de la Garra                                      | 530   | 3525   |
| 3600 | Enclave Brazolanudo                                   | 530   | 3525   |
| 3601 | Loma Plumira                                          | 530   | 3525   |
| 3602 | Encrucijada de Kessel                                 | 530   | 3525   |
| 3603 | Campamento de Tel'athion                              | 530   | 3525   |
| 3604 | El Arrecife Sangre Maldita                            | 530   | 3525   |
| 3605 | El Pasado Hyjal                                       | 560   | 0      |
| 3606 | La Cima Hyjal                                         | 534   | 0      |
| 3607 | Caverna Santuario Serpiente                           | 548   | 0      |
| 3608 | El Reposo del Vindicador                              | 530   | 3525   |
| 3609 | Unused3                                               | 530   | 3518   |
| 3610 | Ruinas Filo Ardiente                                  | 530   | 3518   |
| 3611 | Avanzada del Clan                                     | 530   | 3518   |
| 3612 | Isla Sangre Maldita                                   | 530   | 3525   |
| 3613 | Garadar                                               | 530   | 3518   |
| 3614 | Lago Son Celeste                                      | 530   | 3518   |
| 3615 | El Trono de los Elementos                             | 530   | 3518   |
| 3616 | Ruinas Riecráneos                                     | 530   | 3518   |
| 3617 | Colina Mazo de Guerra                                 | 530   | 3518   |
| 3618 | Guarida de Gruul                                      | 530   | 3518   |
| 3619 | Cresta Auren                                          | 530   | 3518   |
| 3620 | Cascadas Auren                                        | 530   | 3518   |
| 3621 | Lago Primasol                                         | 530   | 3518   |
| 3622 | Puesto Primasol                                       | 530   | 3518   |
| 3623 | Desembarco Aeris                                      | 530   | 3518   |
| 3624 | Campamento Forja: Miedo                               | 530   | 3518   |
| 3625 | Campamento Forja: Odio                                | 530   | 3518   |
| 3626 | Telaar                                                | 530   | 3518   |
| 3627 | Grieta del Viento Norte                               | 530   | 3518   |
| 3628 | Halaa                                                 | 530   | 3518   |
| 3629 | Grieta del Viento Sur                                 | 530   | 3518   |
| 3630 | Oshu'gun                                              | 530   | 3518   |
| 3631 | Campos de Espíritus                                   | 530   | 3518   |
| 3632 | Shamanar                                              | 530   | 3518   |
| 3633 | Tierras Ancestrales                                   | 530   | 3518   |
| 3634 | Aldea Junco Alabeado                                  | 530   | 3518   |
| 3635 | Unused2                                               | 530   | 3518   |
| 3636 | Meseta Elemental                                      | 530   | 3518   |
| 3637 | Fortaleza Mata'penas                                  | 530   | 3518   |
| 3638 | El Círculo de los Retos                               | 530   | 3518   |
| 3639 | Isla Bruma de Plata                                   | 530   | 3524   |
| 3640 | Aldea Dagapantano                                     | 530   | 3521   |
| 3641 | Aldea Umbropantano                                    | 530   | 3521   |
| 3642 | Aldea Feropantano                                     | 530   | 3521   |
| 3643 | Enclave Escamas de Sangre                             | 530   | 3521   |
| 3644 | Telredor                                              | 530   | 3521   |
| 3645 | Zabra'jin                                             | 530   | 3521   |
| 3646 | Cresta Quagg                                          | 530   | 3521   |
| 3647 | La Cañada Emergente                                   | 530   | 3521   |
| 3648 | El Lodo Muerto                                        | 530   | 3521   |
| 3649 | Esporaggar                                            | 530   | 3521   |
| 3650 | Dominios Ango'rosh                                    | 530   | 3521   |
| 3651 | Bastión Ango'rosh                                     | 530   | 3521   |
| 3652 | Caverna Funggor                                       | 530   | 3521   |
| 3653 | Lago Serpiente                                        | 530   | 3521   |
| 3654 | El Vaciado                                            | 530   | 3521   |
| 3655 | Lago Umbropantano                                     | 530   | 3521   |
| 3656 | Lago Luz Pantanosa                                    | 530   | 3521   |
| 3657 | Portal del Claro                                      | 530   | 3521   |
| 3658 | Lago Espora Volante                                   | 530   | 3521   |
| 3659 | La Laguna                                             | 530   | 3521   |
| 3660 | Camino de las Espadas                                 | 530   | 3521   |
| 3661 | Cañón Dientespada                                     | 530   | 3521   |
| 3662 | Cámara del Pueblo                                     | 530   | 3430   |
| 3663 | Mansión Derelicta                                     | 530   | 3430   |
| 3664 | Cazadora del Sol                                      | 530   | 3430   |
| 3665 | Plaza Alalcón                                         | 530   | 3430   |
| 3666 | Cuenca Halaani                                        | 530   | 3518   |
| 3667 | Ciénaga Talada                                        | 530   | 3521   |
| 3668 | Ruinas Boha'mu                                        | 530   | 3521   |
| 3669 | El Estadium                                           | 530   | 3483   |
| 3670 | La Dominancia                                         | 530   | 3483   |
| 3671 | Cerro Tábido                                          | 530   | 3483   |
| 3672 | Procesión Mag'hari                                    | 530   | 3518   |
| 3673 | Safari Nesingwary                                     | 530   | 3518   |
| 3674 | Matorral Cenarion                                     | 530   | 3519   |
| 3675 | Tuurem                                                | 530   | 3519   |
| 3676 | Velo Shienor                                          | 530   | 3519   |
| 3677 | Velo Skith                                            | 530   | 3519   |
| 3678 | Velo Shalas                                           | 530   | 3519   |
| 3679 | Skettis                                               | 530   | 3519   |
| 3680 | Valle Vientonegro                                     | 530   | 3519   |
| 3681 | Alto Ala de Fuego                                     | 530   | 3519   |
| 3682 | Poblado Grangol'var                                   | 530   | 3519   |
| 3683 | Bastión Rompepedras                                   | 530   | 3519   |
| 3684 | Bastión Allerian                                      | 530   | 3519   |
| 3685 | Ruinas Mascahuesos                                    | 530   | 3519   |
| 3686 | Velo Lítico                                           | 530   | 3519   |
| 3687 | Olembas                                               | 530   | 3519   |
| 3688 | Auchindoun                                            | 530   | 3519   |
| 3689 | Velo Reskk                                            | 530   | 3519   |
| 3690 | Lago Vientonegro                                      | 530   | 3519   |
| 3691 | Lago Ere'Noru                                         | 530   | 3519   |
| 3692 | Lago Jorune                                           | 530   | 3519   |
| 3693 | Montañas Skethyl                                      | 530   | 3519   |
| 3694 | Cresta Brumosa                                        | 530   | 3519   |
| 3695 | Las Colinas Quebradas                                 | 530   | 3519   |
| 3696 | Las Colinas Barrera                                   | 530   | 3519   |
| 3697 | El Vertedero de Huesos                                | 530   | 3519   |
| 3698 | Arena de Nagrand                                      | 559   | 0      |
| 3699 | Patio Riecráneos                                      | 530   | 3518   |
| 3700 | El Círculo de Sangre                                  | 530   | 3518   |
| 3701 | El Suelo de la Arena                                  | 530   | 3518   |
| 3702 | Arena Filospada                                       | 562   | 0      |
| 3703 | Ciudad de Shattrath                                   | 530   | 0      |
| 3704 | La Puerta del Pastor                                  | 530   | 3487   |
| 3705 | Cuenca Telaari                                        | 530   | 3518   |
| 3706 | El Portal Oscuro                                      | 269   | 2366   |
| 3707 | Base de la Alianza                                    | 534   | 3606   |
| 3708 | Campamento de la Horda                                | 534   | 3606   |
| 3709 | Villa Elfo de la Noche                                | 534   | 3606   |
| 3710 | Nordrassil                                            | 534   | 3606   |
| 3711 | Cuenca de Sholazar                                    | 571   | 0      |
| 3712 | Área 52                                               | 530   | 3523   |
| 3713 | El Horno de Sangre                                    | 542   | 0      |
| 3714 | Las Salas Arrasadas                                   | 540   | 0      |
| 3715 | La Cámara de Vapor                                    | 545   | 0      |
| 3716 | La Sotiénaga                                          | 546   | 0      |
| 3717 | Recinto de los Esclavos                               | 547   | 0      |
| 3718 | Avanzada Rata del Pantano                             | 530   | 3521   |
| 3719 | Ruinas Foso Sangrante                                 | 530   | 3519   |
| 3720 | Ruinas de las Agujas Gemelas                          | 530   | 3521   |
| 3721 | Las Ruinas Desmoronadas                               | 530   | 3523   |
| 3722 | Forja de Maná Ara                                     | 530   | 3523   |
| 3723 | Ruinas Arklon                                         | 530   | 3523   |
| 3724 | Cosmotirón                                            | 530   | 3523   |
| 3725 | Ruinas de Enkaat                                      | 530   | 3523   |
| 3726 | Forja de Maná B'naar                                  | 530   | 3523   |
| 3727 | El Campo de Sobras                                    | 530   | 3523   |
| 3728 | Los Campos del Vórtice                                | 530   | 3523   |
| 3729 | La Pila                                               | 530   | 3523   |
| 3730 | Forja de Maná Coruu                                   | 530   | 3523   |
| 3731 | La Falla de la Tempestad                              | 530   | 3523   |
| 3732 | Poblado Kirin'Var                                     | 530   | 3523   |
| 3733 | Torre Violeta                                         | 530   | 3523   |
| 3734 | Forja de Maná Duro                                    | 530   | 3523   |
| 3735 | Meseta del Viento del Vacío                           | 530   | 3523   |
| 3736 | Forja de Maná Ultris                                  | 530   | 3523   |
| 3737 | Cresta Celestial                                      | 530   | 3523   |
| 3738 | La Flecha de la Tormenta                              | 530   | 3523   |
| 3739 | Base Forja: Olvido                                    | 530   | 3523   |
| 3740 | Base Forja: Gehenna                                   | 530   | 3523   |
| 3741 | Ruinas de Farahlon                                    | 530   | 3523   |
| 3742 | Trono de Socrethar                                    | 530   | 3523   |
| 3743 | Bastión de la Legión                                  | 530   | 3520   |
| 3744 | Aldea Sombraluna                                      | 530   | 3520   |
| 3745 | Bastión Martillo Salvaje                              | 530   | 3520   |
| 3746 | La Mano de Gul'dan                                    | 530   | 3520   |
| 3747 | Las Fosas Viles                                       | 530   | 3520   |
| 3748 | La Forja Muerta                                       | 530   | 3520   |
| 3749 | Cisterna Cicatriz Espiral                             | 530   | 3520   |
| 3750 | Alto Cicatriz Espiral                                 | 530   | 3520   |
| 3751 | Punta del Fuego Solar                                 | 530   | 3520   |
| 3752 | Alto Illidari                                         | 530   | 3520   |
| 3753 | Ruinas de Baa'ri                                      | 530   | 3520   |
| 3754 | Altar de Sha'tar                                      | 530   | 3520   |
| 3755 | La Escalera Maldita                                   | 530   | 3520   |
| 3756 | Ruinas de Karabor                                     | 530   | 3520   |
| 3757 | Bancal de Ata'mal                                     | 530   | 3520   |
| 3758 | Campos del Ala Abisal                                 | 530   | 3520   |
| 3759 | Arrecife del Ala Abisal                               | 530   | 3520   |
| 3760 | Las Colinas Barrera                                   | 530   | 3518   |
| 3761 | El Paso Elevado                                       | 530   | 3518   |
| 3762 | Paso Junco Alabeado                                   | 530   | 3518   |
| 3763 | Loma de Zangar                                        | 530   | 3518   |
| 3764 | La Cresta del Crepúsculo                              | 530   | 3518   |
| 3765 | Senda Rajaespina                                      | 530   | 3483   |
| 3766 | Puerto Orebor                                         | 530   | 3521   |
| 3767 | Camino de las Espadas                                 | 530   | 3522   |
| 3768 | Cresta Dentada                                        | 530   | 3522   |
| 3769 | Bastión Señor del Trueno                              | 530   | 3522   |
| 3770 | Cañón Dientespada                                     | 530   | 3522   |
| 3771 | La Arboleda Viviente                                  | 530   | 3522   |
| 3772 | Sylvanaar                                             | 530   | 3522   |
| 3773 | Bastión Aguja del Filo                                | 530   | 3522   |
| 3774 | Guarida de Gruul                                      | 530   | 3522   |
| 3775 | Anillo de Sangre                                      | 530   | 3522   |
| 3776 | Avanzada Machacasangre                                | 530   | 3522   |
| 3777 | Campamento Machacasangre                              | 530   | 3522   |
| 3778 | Mina Draenetista                                      | 530   | 3522   |
| 3779 | La Llamada de Trogma                                  | 530   | 3522   |
| 3780 | Aquelarre Alanegra                                    | 530   | 3522   |
| 3781 | Grishnath                                             | 530   | 3522   |
| 3782 | Velo Lashh                                            | 530   | 3522   |
| 3783 | Velo Vekh                                             | 530   | 3522   |
| 3784 | Campamento Forja: Terror                              | 530   | 3522   |
| 3785 | Campamento Forja: Cólera                              | 530   | 3522   |
| 3786 | Ogri'la                                               | 530   | 3522   |
| 3787 | Campamento Forja: Inquina                             | 530   | 3522   |
| 3788 | El Paso Bajo                                          | 530   | 3518   |
| 3789 | Laberinto de las Sombras                              | 555   | 0      |
| 3790 | Criptas Auchenai                                      | 558   | 0      |
| 3791 | Salas Sethekk                                         | 556   | 0      |
| 3792 | Tumbas de Maná                                        | 557   | 0      |
| 3793 | Barranco Burbujas Viles                               | 530   | 3483   |
| 3794 | Valle de los Huesos                                   | 530   | 3483   |
| 3795 | Ruinas Sha'naari                                      | 530   | 3483   |
| 3796 | Los Campos Alabeados                                  | 530   | 3483   |
| 3797 | Cresta Cielo Estrellado                               | 530   | 3483   |
| 3798 | Garganta Haal'eshi                                    | 530   | 3483   |
| 3799 | Cañón de la Muralla                                   | 530   | 3483   |
| 3800 | Colina Colmillespinado                                | 530   | 3483   |
| 3801 | Dominios Mag'har                                      | 530   | 3483   |
| 3802 | Cresta del Vacío                                      | 530   | 3483   |
| 3803 | La Plataforma Abisal                                  | 530   | 3483   |
| 3804 | La Avanzadilla de la Legión                           | 530   | 3483   |
| 3805 | Zul'Aman                                              | 568   | 0      |
| 3806 | Caravana de Provisiones                               | 530   | 3483   |
| 3807 | Caída del Atracador Vil                               | 530   | 3483   |
| 3808 | Puesto Cenarion                                       | 530   | 3483   |
| 3809 | Muralla Sur                                           | 530   | 3483   |
| 3810 | Muralla Norte                                         | 530   | 3483   |
| 3811 | Avanzada Gor'gaz                                      | 530   | 3483   |
| 3812 | Avanzada Rompeloma                                    | 530   | 3483   |
| 3813 | El Camino del Tormento                                | 530   | 3483   |
| 3814 | Caravana de Provisiones del Este                      | 530   | 3483   |
| 3815 | Punta de Expedición                                   | 530   | 3483   |
| 3816 | Zepelín Caído                                         | 530   | 3483   |
| 3817 | Testeo                                                | 13    | 0      |
| 3818 | Tierras Escamas de Sangre                             | 530   | 3521   |
| 3819 | Enclave Cresta Oscura                                 | 530   | 3521   |
| 3820 | Ojo de la Tormenta                                    | 566   | 0      |
| 3821 | Jaula de la Guardiana                                 | 530   | 3520   |
| 3822 | Punta Eclipse                                         | 530   | 3520   |
| 3823 | Isla de las Tribulaciones                             | 530   | 3433   |
| 3824 | Barranco Machacasangre                                | 530   | 3522   |
| 3825 | Cabo del Dragón                                       | 530   | 3522   |
| 3826 | Cañón Faucedaga                                       | 530   | 3522   |
| 3827 | Alto Vekhaar                                          | 530   | 3522   |
| 3828 | Foresta Ruuan                                         | 530   | 3522   |
| 3829 | Velo Ruuan                                            | 530   | 3522   |
| 3830 | Bosque del Cuervo                                     | 530   | 3522   |
| 3831 | Puerta de la Muerte                                   | 530   | 3522   |
| 3832 | Cumbre del Vórtice                                    | 530   | 3522   |
| 3833 | Loma Tajo                                             | 530   | 3522   |
| 3834 | Cresta de la Locura                                   | 530   | 3522   |
| 3835 | Barranco Pluma Polvorienta                            | 530   | 3483   |
| 3836 | Guarida de Magtheridon                                | 544   | 0      |
| 3837 | Bastión Furia del Sol                                 | 530   | 3523   |
| 3838 | Montañas Rompeloma                                    | 530   | 3483   |
| 3839 | Armería Abandonada                                    | 530   | 3518   |
| 3840 | El Templo Oscuro                                      | 530   | 3520   |
| 3841 | Playa Crestanegra                                     | 530   | 3521   |
| 3842 | El Castillo de la Tempestad                           | 530   | 3523   |
| 3844 | Aldea Mok'Nathal                                      | 530   | 3522   |
| 3845 | El Castillo de la Tempestad                           | 550   | 0      |
| 3846 | El Arcatraz                                           | 530   | 3525   |
| 3847 | El Invernáculo                                        | 553   | 0      |
| 3848 | El Arcatraz                                           | 552   | 0      |
| 3849 | El Mechanar                                           | 554   | 0      |
| 3850 | Piedra Abisal                                         | 530   | 3523   |
| 3851 | Puesto de la Tierra Media                             | 530   | 3523   |
| 3852 | Alto de Tuluman                                       | 530   | 3523   |
| 3854 | Avanzada del Protectorado                             | 530   | 3523   |
| 3855 | Arena del Anillo de Sangre                            | 530   | 3522   |
| 3856 | Cruce Elrendar                                        | 530   | 3433   |
| 3857 | Vado Ammen                                            | 530   | 3524   |
| 3858 | Saliente Rajaespina                                   | 530   | 3519   |
| 3859 | Lago Silmyr                                           | 530   | 3519   |
| 3860 | Claro Raastok                                         | 530   | 3519   |
| 3861 | Desfiladero Thalassiano                               | 530   | 3433   |
| 3862 | Garganta Bulliciosa                                   | 530   | 3522   |
| 3863 | Landas Tábidas                                        | 530   | 3522   |
| 3864 | Alto Bash'ir                                          | 530   | 3522   |
| 3865 | Espina de Cristal                                     | 530   | 3522   |
| 3866 | Skald                                                 | 530   | 3522   |
| 3867 | Barranco del Filo                                     | 530   | 3522   |
| 3868 | Puente Girolámina                                     | 530   | 3523   |
| 3869 | Torre de los Magos                                    | 566   | 3820   |
| 3870 | Torre de los Elfos de Sangre                          | 566   | 3820   |
| 3871 | Ruinas Draenei                                        | 566   | 3820   |
| 3872 | Ruinas del Atracador Vil                              | 566   | 3820   |
| 3873 | Terreno de Pruebas                                    | 530   | 3523   |
| 3874 | Ecodomo Campolejano                                   | 530   | 3523   |
| 3875 | Ecodomo Altocielo                                     | 530   | 3523   |
| 3876 | Ecodomo Sutheron                                      | 530   | 3523   |
| 3877 | Ecodomo de la Tierra Media                            | 530   | 3523   |
| 3878 | Punto de Escala de El Etereum                         | 530   | 3523   |
| 3879 | Patio de la Capilla                                   | 530   | 3523   |
| 3880 | Eje de Acceso Zeon                                    | 530   | 3523   |
| 3881 | Mina Trelleum                                         | 530   | 3523   |
| 3882 | Punto de Invasión: Destructor                         | 530   | 3523   |
| 3883 | Campamento de Bum                                     | 530   | 3523   |
| 3884 | Desfiladero Rompeloma                                 | 530   | 3483   |
| 3885 | Cresta Red Abisal                                     | 530   | 3519   |
| 3886 | Caravana Derelicta                                    | 530   | 3519   |
| 3887 | Caravana de Refugiados                                | 530   | 3519   |
| 3888 | Tumba Umbría                                          | 530   | 3519   |
| 3889 | Velo Rhaze                                            | 530   | 3519   |
| 3890 | Tumba de las Luces                                    | 530   | 3519   |
| 3891 | Colina Carroña                                        | 530   | 3519   |
| 3892 | Alcor Tortuoso                                        | 530   | 3519   |
| 3893 | Círculo de la Observancia                             | 530   | 3519   |
| 3894 | Tierras Auchenai                                      | 530   | 3519   |
| 3895 | Puesto de Vigilancia Cenarion                         | 530   | 3521   |
| 3896 | Alto Aldor                                            | 530   | 3703   |
| 3897 | Bancal de la Luz                                      | 530   | 3703   |
| 3898 | Grada del Arúspice                                    | 530   | 3703   |
| 3899 | Bajo Arrabal                                          | 530   | 3703   |
| 3900 | Punto de Invasión: Señor Supremo                      | 530   | 3523   |
| 3901 | Puesto Allerian                                       | 530   | 3519   |
| 3902 | Campamento Rompepedras                                | 530   | 3519   |
| 3903 | Peña'mok                                              | 530   | 3522   |
| 3904 | Hoya Maldita                                          | 530   | 3522   |
| 3905 | Reserva Colmillo Torcido                              | 530   | 3521   |
| 3906 | La Playa de Sangre                                    | 530   | 3525   |
| 3907 | Punta Veridiana                                       | 530   | 3525   |
| 3908 | Mediavega                                             | 530   | 3525   |
| 3909 | El Aprisco Perdido                                    | 530   | 3525   |
| 3910 | Bosque Bruma                                          | 530   | 3525   |
| 3911 | Orilla Tranquila                                      | 530   | 3430   |
| 3912 | Desfiladero Ramadorada                                | 530   | 3430   |
| 3913 | Piedra Rúnica Falithas                                | 530   | 3430   |
| 3914 | Piedra Rúnica Shan'dor                                | 530   | 3430   |
| 3915 | Playa Puentegrato                                     | 530   | 3524   |
| 3916 | Bosque Pasto Lunar                                    | 530   | 3524   |
| 3917 | Auchindoun                                            | 530   | 0      |
| 3918 | Estación de Toshley                                   | 530   | 3522   |
| 3919 | Cresta Canto                                          | 530   | 3522   |
| 3920 | Puesto Devastación                                    | 530   | 3483   |
| 3921 | Cresta Arklonis                                       | 530   | 3523   |
| 3922 | Avanzada Aguja del Filo                               | 530   | 3522   |
| 3923 | Guarida de Gruul                                      | 565   | 0      |
| 3924 | Torre Quiebranorte                                    | 530   | 3522   |
| 3925 | Torre Quiebrasur                                      | 530   | 3522   |
| 3926 | Llanuras Devastadas                                   | 530   | 3520   |
| 3927 | Granja de Oronok                                      | 530   | 3520   |
| 3928 | El Altar de Condenación                               | 530   | 3520   |
| 3929 | El Sendero de la Conquista                            | 530   | 3520   |
| 3930 | Campos Eclipsianos                                    | 530   | 3520   |
| 3931 | Dominios Aguja del Filo                               | 530   | 3522   |
| 3932 | Campamento Sketh'lon                                  | 530   | 3520   |
| 3933 | Ruinas de Sketh'lon                                   | 530   | 3520   |
| 3934 | Plaza de la Ciudad                                    | 530   | 3523   |
| 3935 | Pasaje del Zahorí                                     | 530   | 3523   |
| 3936 | Torre de la Forja Muerta                              | 530   | 3520   |
| 3937 | Vigía de la Escoria                                   | 530   | 3520   |
| 3938 | Sagrario de las Estrellas                             | 530   | 3520   |
| 3939 | Fortaleza Faucedraco                                  | 530   | 3520   |
| 3940 | La Poza Fétida                                        | 530   | 3520   |
| 3941 | Test                                                  | 530   | 3520   |
| 3942 | Zona de Aterrizaje Razaan                             | 530   | 3522   |
| 3943 | Punto de Invasión: Cataclismo                         | 530   | 3520   |
| 3944 | El Altar de las Sombras                               | 530   | 3520   |
| 3945 | Desfiladero del Ala Abisal                            | 530   | 3520   |
| 3946 | Refugio de Wayne                                      | 530   | 3519   |
| 3947 | Las Pozas Escaldantes                                 | 530   | 3520   |
| 3948 | Brian and Pat Test                                    | 451   | 0      |
| 3949 | Campos de Magma                                       | 530   | 3520   |
| 3950 | Atalaya Carmesí                                       | 530   | 3520   |
| 3951 | Soto Eterno                                           | 530   | 3522   |
| 3952 | Puente Calavermis                                     | 530   | 3522   |
| 3953 | Plataforma Alaescama                                  | 530   | 3522   |
| 3954 | Túnel Calavermis                                      | 530   | 3522   |
| 3955 | Cuenca del Fuego Infernal                             | 530   | 3483   |
| 3956 | La Escalera Umbría                                    | 530   | 3519   |
| 3957 | Avanzada Sha'tari                                     | 530   | 3519   |
| 3958 | Campamento Sha'tari                                   | 530   | 3519   |
| 3959 | Templo Oscuro                                         | 564   | 0      |
| 3960 | Túmulo de Moledor de Almas                            | 530   | 3522   |
| 3961 | Punta Alapenas                                        | 530   | 3519   |
| 3962 | Anillo de Vim'gol                                     | 530   | 3522   |
| 3963 | Cresta Espinazo de Dragón                             | 530   | 3522   |
| 3964 | Avanzada de la Guardia del Cielo                      | 530   | 3522   |
| 3965 | Minas del Ala Abisal                                  | 530   | 3520   |
| 3966 | Campamento Faucedraco                                 | 530   | 3520   |
| 3967 | Ruta Aérea Faucedraco                                 | 530   | 3520   |
| 3968 | Ruinas de Lordaeron                                   | 572   | 0      |
| 3969 | Nido de Desgarro Oscuro                               | 530   | 3522   |
| 3970 | Nido de Obsidia                                       | 530   | 3522   |
| 3971 | Nido de Insidion                                      | 530   | 3522   |
| 3972 | Nido de Alafuria                                      | 530   | 3522   |
| 3973 | Alto de los Vientonegro                               | 530   | 3519   |
| 3974 | Velo Harr'ik                                          | 530   | 3519   |
| 3975 | Sosiego de Terokk                                     | 530   | 3519   |
| 3976 | Velo Ala'rak                                          | 530   | 3519   |
| 3977 | Velo Shil'ak Alto                                     | 530   | 3519   |
| 3978 | Velo Shil'ak Bajo                                     | 530   | 3519   |
| 3979 | El Mar Gélido                                         | 571   | 0      |
| 3980 | Bahía Cubredaga                                       | 571   | 495    |
| 3981 | Valgarde                                              | 571   | 495    |
| 3982 | Poblado Calavermis                                    | 571   | 495    |
| 3983 | Fortaleza de Utgarde                                  | 571   | 495    |
| 3984 | Nafsavar                                              | 571   | 495    |
| 3985 | Cataratas de Ymiron                                   | 571   | 495    |
| 3986 | Risco del Eco                                         | 571   | 495    |
| 3987 | La Isla de las Lanzas                                 | 571   | 495    |
| 3988 | Komawa                                                | 571   | 495    |
| 3989 | Arrecife de Garvan                                    | 571   | 495    |
| 3990 | Cabo Pillastre                                        | 571   | 495    |
| 3991 | Nuevo Agamand                                         | 571   | 495    |
| 3992 | El Antiguo Elevador                                   | 571   | 495    |
| 3993 | Torreta de la Guardia Oeste                           | 571   | 495    |
| 3994 | Haltorboll                                            | 571   | 495    |
| 3995 | La Playa Rompeolas                                    | 571   | 495    |
| 3996 | Excavación de Baelgun                                 | 571   | 495    |
| 3997 | Avanzada de la Liga de Expedicionarios                | 571   | 495    |
| 3998 | Fortaleza de la Guardia Oeste                         | 571   | 495    |
| 3999 | Las Puertas de Acero                                  | 571   | 495    |
| 4000 | Campo Venganza                                        | 571   | 495    |
| 4001 | Baleheim                                              | 571   | 495    |
| 4002 | Skorn                                                 | 571   | 495    |
| 4003 | Fuerte Vildervar                                      | 571   | 495    |
| 4004 | Poblado Presavil                                      | 571   | 495    |
| 4005 | Ruinas de Ivald                                       | 571   | 495    |
| 4006 | Gjalerbron                                            | 571   | 495    |
| 4007 | Tumba de los Reyes Perdidos                           | 571   | 495    |
| 4008 | Transportador de Shartuul                             | 530   | 3522   |
| 4009 | Campo de entrenamiento Illidari                       | 564   | 3959   |
| 4010 | Piñón de Barro                                        | 1     | 15     |
| 4018 | Campamento Pezuña Invernal                            | 571   | 495    |
| 4019 | Tierra de Desarrollo                                  | 451   | 0      |
| 4020 | Cantera de Piedra de Poderío                          | 571   | 3537   |
| 4021 | Llanuras Sanguiespora                                 | 571   | 3537   |
| 4022 | Gammoth                                               | 571   | 3537   |
| 4023 | El Saliente Ámbar                                     | 571   | 3537   |
| 4024 | Gelidar                                               | 571   | 3537   |
| 4025 | La Falla Oeste                                        | 571   | 3537   |
| 4026 | La Escalera de Tránsito                               | 571   | 3537   |
| 4027 | Costa de los Ecos                                     | 571   | 3537   |
| 4028 | Litoral Tralladón                                     | 571   | 3537   |
| 4029 | Ruinas Tralladón                                      | 571   | 3537   |
| 4030 | Costa de los Ídolos                                   | 571   | 3537   |
| 4031 | Pal'ea                                                | 571   | 3537   |
| 4032 | Fortaleza Denuedo                                     | 571   | 3537   |
| 4033 | Poblado Aleta Invernal                                | 571   | 3537   |
| 4034 | La Muralla Boreal                                     | 571   | 3537   |
| 4035 | Los Campos de Géiseres                                | 571   | 3537   |
| 4036 | Estación de Bombeo de Palanqueta                      | 571   | 3537   |
| 4037 | Poblado Taunka'le                                     | 571   | 3537   |
| 4038 | Cavernas Magnamoth                                    | 571   | 3537   |
| 4039 | Cantera Frioescollo                                   | 571   | 3537   |
| 4040 | Bahía Aliento de Njord                                | 571   | 3537   |
| 4041 | Kashala                                               | 571   | 3537   |
| 4042 | Transborea                                            | 571   | 3537   |
| 4043 | Llanuras Anegadas                                     | 571   | 3537   |
| 4046 | Puesto Cuernoatroz                                    | 1     | 15     |
| 4047 | Embarcadero de Nat                                    | 1     | 15     |
| 4048 | Encierro Ámbar                                        | 571   | 495    |
| 4049 | Granja de Tabetha                                     | 1     | 15     |
| 4050 | Playa Derelicta                                       | 571   | 495    |
| 4051 | El Claro Helado                                       | 571   | 495    |
| 4052 | El Claro Vibrante                                     | 571   | 495    |
| 4053 | El Claro Retorcido                                    | 571   | 495    |
| 4054 | El Bosque Hendido                                     | 571   | 495    |
| 4055 | Lago Caldemere                                        | 571   | 495    |
| 4056 | Catacumbas de Utgarde                                 | 571   | 495    |
| 4057 | Colina Escudo                                         | 571   | 495    |
| 4058 | Lago Caldros                                          | 571   | 495    |
| 4059 | Isla Caldros                                          | 571   | 495    |
| 4060 | Vega Sangrante                                        | 571   | 495    |
| 4061 | El Paso del Gigante                                   | 571   | 495    |
| 4062 | Campamento de los Boticarios                          | 571   | 495    |
| 4063 | Torre Lanza Ámbar                                     | 571   | 495    |
| 4064 | Estrecho Devastado                                    | 571   | 495    |
| 4065 | Gjalercorn                                            | 571   | 495    |
| 4066 | Pico Filoescarcha                                     | 571   | 495    |
| 4067 | Torre del Bosque de la Peste                          | 0     | 139    |
| 4068 | Torre Lanza del Oeste                                 | 571   | 495    |
| 4069 | Torre Lanza del Norte                                 | 571   | 495    |
| 4070 | Costafría                                             | 571   | 495    |
| 4071 | Garganta Susurro                                      | 571   | 495    |
| 4072 | Subzona                                               | 451   | 151    |
| 4073 | Bancal del Invierno                                   | 571   | 495    |
| 4074 | Las Salas del Despertar                               | 571   | 495    |
| 4075 | Meseta de La Fuente del Sol                           | 580   | 0      |
| 4076 | Reuse Me 7                                            | 598   | 0      |
| 4077 | Playa de Sorlof                                       | 571   | 495    |
| 4078 | Alto Rajaespina                                       | 530   | 3519   |
| 4079 | Paso Filoescarcha                                     | 571   | 495    |
| 4080 | Isla de Quel'Danas                                    | 530   | 0      |
| 4081 | El Cazador del Albor                                  | 530   | 4080   |
| 4082 | El Sin'loren                                          | 530   | 4080   |
| 4083 | Orgullo de Lunargenta                                 | 530   | 4080   |
| 4084 | El Juramento de Sangre                                | 530   | 4080   |
| 4085 | Zona de escala de Sol Devastado                       | 530   | 4080   |
| 4086 | Sagrario de Tramo del Sol                             | 530   | 4080   |
| 4087 | Puerto de Tramo del Sol                               | 530   | 4080   |
| 4088 | Arsenal de Tramo del Sol                              | 530   | 4080   |
| 4089 | Poblado Estrella del Alba                             | 530   | 4080   |
| 4090 | La Plaza Crepuscular                                  | 530   | 4080   |
| 4091 | Costa Branquia Verde                                  | 530   | 4080   |
| 4092 | La Cicatriz Muerta                                    | 530   | 4080   |
| 4093 | La Forja del Sol                                      | 530   | 4080   |
| 4094 | Meseta de La Fuente del Sol                           | 530   | 4080   |
| 4095 | Bancal del Magister                                   | 530   | 4080   |
| 4096 | Claytön's WoWEdit Land                                | 451   | 4019   |
| 4097 | Cavernas Aleta Invernal                               | 571   | 3537   |
| 4098 | Bahía Titileo                                         | 571   | 3537   |
| 4099 | Refugio Aleta Invernal                                | 571   | 3537   |
| 4100 | La Matanza de Stratholme                              | 595   | 0      |
| 4101 | Arenas de Nasam                                       | 571   | 3537   |
| 4102 | Puerto de Krom                                        | 571   | 3537   |
| 4103 | Garfa de Nasam                                        | 571   | 3537   |
| 4104 | Cala del Eco                                          | 571   | 3537   |
| 4105 | Alto de Berilo                                        | 571   | 3537   |
| 4106 | Desembarco de Garrosh                                 | 571   | 3537   |
| 4107 | Malecón Grito de Guerra                               | 571   | 3537   |
| 4108 | Pista de Aterrizaje de Palanqueta                     | 571   | 3537   |
| 4109 | Lago Kum'uya                                          | 571   | 3537   |
| 4110 | Campos de Lindeallá                                   | 571   | 3537   |
| 4111 | Lindeallá                                             | 571   | 3537   |
| 4112 | Faro de Lindeallá                                     | 571   | 3537   |
| 4113 | Unu'pe                                                | 571   | 3537   |
| 4114 | Confín de la Muerte                                   | 571   | 3537   |
| 4115 | El Tramo Abandonado                                   | 571   | 3537   |
| 4116 | Pozas Escaldantes                                     | 571   | 3537   |
| 4117 | Manantiales de Vapor                                  | 571   | 3537   |
| 4118 | Talramas                                              | 571   | 3537   |
| 4119 | Pozas Purulentas                                      | 571   | 3537   |
| 4120 | El Nexo                                               | 571   | 3537   |
| 4121 | Escudo de Tránsito                                    | 571   | 3537   |
| 4122 | Avanzada Bor'gorok                                    | 571   | 3537   |
| 4123 | Magmoth                                               | 571   | 3537   |
| 4124 | Los Cubiles de los Moribundos                         | 571   | 3537   |
| 4125 | Ciudad Templo de En'kilah                             | 571   | 3537   |
| 4126 | El Zigurat de los Lamentos                            | 571   | 3537   |
| 4127 | Caravana de Quijacero                                 | 571   | 3537   |
| 4128 | Naxxanar                                              | 571   | 3537   |
| 4129 | Bastión Grito de Guerra                               | 571   | 3537   |
| 4130 | Llanuras de Nasam                                     | 571   | 3537   |
| 4131 | Bancal del Magister                                   | 585   | 0      |
| 4132 | Ruinas de Eldra'nath                                  | 571   | 3537   |
| 4133 | Alto Carbonizado                                      | 571   | 3537   |
| 4134 | Poza Virulenta                                        | 571   | 3537   |
| 4135 | Aguja de Sangre                                       | 571   | 3537   |
| 4136 | Aguja de Putrefacción                                 | 571   | 3537   |
| 4137 | Aguja de Dolor                                        | 571   | 3537   |
| 4138 | Tramo Helado                                          | 571   | 3537   |
| 4139 | Plaza del Parhelio                                    | 580   | 4075   |
| 4140 | La Cicatriz Muerta                                    | 580   | 4075   |
| 4141 | Granja de Torp                                        | 571   | 3537   |
| 4142 | Granero Grito de Guerra                               | 571   | 3537   |
| 4143 | Matadero Grito de Guerra                              | 571   | 3537   |
| 4144 | Avanzada de las Granjas Grito de Guerra               | 571   | 3537   |
| 4145 | Estación de la Punta Oeste                            | 571   | 3537   |
| 4146 | Estación de la Punta Norte                            | 571   | 3537   |
| 4147 | Estación de la Punta Central                          | 571   | 3537   |
| 4148 | Estación de la Punta Sur                              | 571   | 3537   |
| 4149 | Campamento D.E.H.T.A.                                 | 571   | 3537   |
| 4150 | Percha de Kaw                                         | 571   | 3537   |
| 4151 | Campo de Refugiados de Viento Oeste                   | 571   | 65     |
| 4152 | Puerto Moa'ki                                         | 571   | 65     |
| 4153 | Poblado Indu'le                                       | 571   | 65     |
| 4154 | Claro Avalancha                                       | 571   | 65     |
| 4155 | La Media Concha                                       | 571   | 65     |
| 4156 | Aguja de Flujo                                        | 571   | 65     |
| 4157 | Jardines Reposo Lunar                                 | 571   | 65     |
| 4158 | Reposo Estelar                                        | 571   | 65     |
| 4159 | Campamento de la Brigada de los Páramos de Poniente   | 571   | 394    |
| 4160 | Bosque Lothalor                                       | 571   | 65     |
| 4161 | Templo del Reposo del Dragón                          | 571   | 65     |
| 4162 | Cataratas Bruma de Hielo                              | 571   | 65     |
| 4163 | Poblado Bruma de Hielo                                | 571   | 65     |
| 4164 | El Foso de Narjun                                     | 571   | 65     |
| 4165 | Martillo de Agmar                                     | 571   | 65     |
| 4166 | Lago Indu'le                                          | 571   | 65     |
| 4167 | Santuario de Dragones Obsidiana                       | 571   | 65     |
| 4168 | Santuario de Dragones Rubí                            | 571   | 65     |
| 4169 | Bastión de Fordragón                                  | 571   | 65     |
| 4170 | Vanguardia Kor'kron                                   | 571   | 65     |
| 4171 | La Corte de las Calaveras                             | 571   | 65     |
| 4172 | Angrathar la Puerta de Cólera                         | 571   | 65     |
| 4173 | Reposo de Galakrond                                   | 571   | 65     |
| 4174 | La Espiral Maldita                                    | 571   | 65     |
| 4175 | Santuario de Dragones Bronce                          | 571   | 65     |
| 4176 | El Espejo del Alba                                    | 571   | 65     |
| 4177 | Fortaleza de Hibergarde                               | 571   | 65     |
| 4178 | Mina de Hibergarde                                    | 571   | 65     |
| 4179 | Santuario de Dragones Esmeralda                       | 571   | 65     |
| 4180 | Nueva Vega del Amparo                                 | 571   | 65     |
| 4181 | El Tramo del Cruzado                                  | 571   | 65     |
| 4182 | Locura del Pecador                                    | 571   | 65     |
| 4183 | Santuario de Dragones Azur                            | 571   | 65     |
| 4184 | Senda de los Titanes                                  | 571   | 65     |
| 4185 | La Orilla Olvidada                                    | 571   | 65     |
| 4186 | Rencor Venenoso                                       | 571   | 65     |
| 4187 | Vicio de Cristal                                      | 571   | 65     |
| 4188 | Los Campos de Carroña                                 | 571   | 65     |
| 4189 | Campamento del Embate                                 | 571   | 65     |
| 4190 | Puesto de Thorson                                     | 571   | 65     |
| 4191 | Confianza de la Luz                                   | 571   | 65     |
| 4192 | Caverna Agonía de Escarcha                            | 571   | 65     |
| 4193 | Punta Escarlata                                       | 571   | 65     |
| 4194 | Jintha'kalar                                          | 571   | 65     |
| 4195 | Caverna Corazón de Hielo                              | 571   | 65     |
| 4196 | Fortaleza de Drak'Tharon                              | 600   | 0      |
| 4197 | Conquista del Invierno                                | 571   | 0      |
| 4198 | Atolón de Kili'ua                                     | 571   | 65     |
| 4199 | Arroyoplata                                           | 571   | 394    |
| 4200 | Corazón de Vordrassil                                 | 571   | 394    |
| 4201 | Lágrimas de Vordrassil                                | 571   | 0      |
| 4202 | Lágrimas de Vordrassil                                | 571   | 394    |
| 4203 | Extremidad de Vordrassil                              | 571   | 394    |
| 4204 | Refugio Pino Ámbar                                    | 571   | 394    |
| 4205 | Poblado Solsticio                                     | 571   | 394    |
| 4206 | Bastión de la Conquista                               | 571   | 394    |
| 4207 | Runavold                                              | 571   | 394    |
| 4208 | Manantial de Granito                                  | 571   | 394    |
| 4209 | Zeb'Halak                                             | 571   | 394    |
| 4210 | Fortaleza de Drak'Tharon                              | 571   | 394    |
| 4211 | Campamento Oneqwah                                    | 571   | 394    |
| 4212 | Playa Viento Este                                     | 571   | 394    |
| 4213 | Riscos Quebrados                                      | 571   | 394    |
| 4214 | Colinas Pedrusco                                      | 571   | 394    |
| 4215 | Santuario Colmillo Iracundo                           | 571   | 394    |
| 4216 | Ruinas de Drakil'jin                                  | 571   | 394    |
| 4217 | Aserradero Río Negro                                  | 571   | 394    |
| 4218 | Santuario Sangre de Corazón                           | 571   | 394    |
| 4219 | Mina Piedrahueca                                      | 571   | 394    |
| 4220 | Dun Argol                                             | 571   | 394    |
| 4221 | Thor Modan                                            | 571   | 394    |
| 4222 | Aserradero Cielo Azul                                 | 571   | 394    |
| 4223 | Fauces de Neltharion                                  | 571   | 65     |
| 4224 | El Pináculo Salobre                                   | 571   | 65     |
| 4225 | Orilla Resplandeciente                                | 571   | 65     |
| 4226 | Iskaal                                                | 571   | 495    |
| 4227 | Caída del Dragón                                      | 571   | 65     |
| 4228 | El Oculus                                             | 578   | 0      |
| 4229 | Altozano del Prospector                               | 571   | 394    |
| 4230 | Altos Viento Helado                                   | 571   | 65     |
| 4231 | Puesto de Venta de Madera Roja                        | 571   | 394    |
| 4232 | Paso Venganza                                         | 571   | 65     |
| 4233 | Tramo del Alba                                        | 571   | 65     |
| 4234 | Naxxramas                                             | 571   | 65     |
| 4235 | Puesto de Venta de Duramen                            | 571   | 394    |
| 4236 | Puesto de Venta de Siempreverde                       | 571   | 394    |
| 4237 | Puesto del Altozano de Píceas                         | 571   | 394    |
| 4238 | Puesto de Venta de Pino Blanco                        | 571   | 394    |
| 4239 | Puesto de la Alameda                                  | 571   | 394    |
| 4240 | Puesto Fronterizo del Bosque                          | 571   | 394    |
| 4241 | Cumbres de Eldritch                                   | 571   | 65     |
| 4242 | Bahía Ventura                                         | 571   | 394    |
| 4243 | Cripta de Hibergarde                                  | 571   | 65     |
| 4244 | Isla Luna de Sangre                                   | 571   | 394    |
| 4245 | Torre de Colmillo Oscuro                              | 571   | 394    |
| 4246 | Mausoleo de Hibergarde                                | 571   | 65     |
| 4247 | Cubil Aúllaocaso                                      | 571   | 394    |
| 4248 | El Foso de la Conquista                               | 571   | 394    |
| 4249 | La Senda de Hierro                                    | 571   | 394    |
| 4250 | Ruinas de Tethys                                      | 571   | 394    |
| 4251 | Colinas de Arroyoplata                                | 571   | 394    |
| 4252 | Riscos Quebrados                                      | 571   | 495    |
| 4253 | Frente de la Séptima Legión                           | 571   | 65     |
| 4254 | Baldío del Dragón                                     | 571   | 65     |
| 4255 | Ruinas de Drak'Zin                                    | 571   | 394    |
| 4256 | Lago Drak'Mar                                         | 571   | 65     |
| 4257 | Afluente del Espinazo del Dragón                      | 571   | 65     |
| 4258 | El Mar del Norte                                      | 571   | 0      |
| 4259 | Drak'ural                                             | 571   | 394    |
| 4260 | Campamento de Thorvald                                | 571   | 495    |
| 4261 | Puesto del Filo Fantasmal                             | 571   | 495    |
| 4262 | Puesto Fresno                                         | 571   | 394    |
| 4263 | Emboscada de Lydell                                   | 571   | 495    |
| 4264 | Cámaras de Piedra                                     | 599   | 0      |
| 4265 | El Nexo                                               | 576   | 0      |
| 4266 | Campamento de Harkor                                  | 571   | 394    |
| 4267 | Paso de Vordrassil                                    | 571   | 394    |
| 4268 | Campamento de Ruuna                                   | 571   | 394    |
| 4269 | Santuario de Escamas                                  | 571   | 3537   |
| 4270 | Pasaje de Drak'atal                                   | 571   | 394    |
| 4271 | Pináculo de Utgarde                                   | 571   | 495    |
| 4272 | Cámaras de Relámpagos                                 | 602   | 0      |
| 4273 | Ulduar                                                | 603   | 0      |
| 4275 | El Confín Argenta                                     | 571   | 66     |
| 4276 | Altar de Sseratus                                     | 571   | 66     |
| 4277 | Azjol-Nerub                                           | 601   | 0      |
| 4278 | Campos Drak'Sotra                                     | 571   | 66     |
| 4279 | Drak'Sotra                                            | 571   | 66     |
| 4280 | Drak'Agal                                             | 571   | 66     |
| 4281 | Acherus: El Bastión de Ébano                          | 0     | 139    |
| 4282 | La Avalancha                                          | 571   | 3711   |
| 4283 | Las Tierras Perdidas                                  | 571   | 3711   |
| 4284 | Campamento Base de Nesingwary                         | 571   | 3711   |
| 4285 | El Flujo de la Brecha del Mar                         | 571   | 3711   |
| 4286 | Los Huesos de Nozronn                                 | 571   | 3711   |
| 4287 | Bastión de Kartak                                     | 571   | 3711   |
| 4288 | Retiro Pavesa                                         | 571   | 3711   |
| 4289 | La Senda del Guardián de Vida                         | 571   | 3711   |
| 4290 | Corazón del Río                                       | 571   | 3711   |
| 4291 | Espesura Hablalluvia                                  | 571   | 3711   |
| 4292 | Colina Corazón Frenético                              | 571   | 3711   |
| 4293 | Manglar Silvestre                                     | 571   | 3711   |
| 4294 | Heb'Valok                                             | 571   | 66     |
| 4295 | El Fragmento Hendido                                  | 571   | 3711   |
| 4296 | El Pilar Sangrevida                                   | 571   | 3711   |
| 4297 | Poblado Caminamoho                                    | 571   | 3711   |
| 4298 | Tierras de la Peste: El Enclave Escarlata             | 609   | 0      |
| 4299 | Kolramas                                              | 571   | 66     |
| 4300 | Puerta                                                | 571   | 3711   |
| 4302 | El Pilar del Trecho Celestial                         | 571   | 3711   |
| 4303 | Claro Callonudillo                                    | 571   | 3711   |
| 4304 | Enjambre Zafiro                                       | 571   | 3711   |
| 4306 | Refugio Susurraneblina                                | 571   | 3711   |
| 4307 | El Pilar Iluminado                                    | 571   | 3711   |
| 4308 | Campamento Lanzonato                                  | 571   | 3711   |
| 4309 | Fortaleza de Drak'Tharon                              | 571   | 66     |
| 4310 | Zeramas                                               | 571   | 66     |
| 4311 | Relicario de Agonía                                   | 571   | 66     |
| 4312 | Puesto de Vigilancia de Ébano                         | 571   | 66     |
| 4313 | Fin de Thrym                                          | 571   | 66     |
| 4314 | Voltarus                                              | 571   | 66     |
| 4315 | Relicario de Dolor                                    | 571   | 66     |
| 4316 | Guarida de Garrafuria                                 | 571   | 66     |
| 4317 | Brecha de la Luz                                      | 571   | 66     |
| 4318 | Pozas de Zha'Jin                                      | 571   | 66     |
| 4319 | Zim'Abwa                                              | 571   | 66     |
| 4320 | Anfiteatro de la Angustia                             | 571   | 66     |
| 4321 | Altar de Rhunok                                       | 571   | 66     |
| 4322 | Altar de Har'koa                                      | 571   | 66     |
| 4323 | Zim'Torga                                             | 571   | 66     |
| 4324 | Pozas de Jin'Alai                                     | 571   | 66     |
| 4325 | Altar de Quetz'lun                                    | 571   | 66     |
| 4326 | Heb'Drakkar                                           | 571   | 66     |
| 4327 | Drak'Mabwa                                            | 571   | 66     |
| 4328 | Zim'Rhuk                                              | 571   | 66     |
| 4329 | Altar de Mam'toth                                     | 571   | 66     |
| 4342 | Acherus: El Bastión de Ébano                          | 609   | 4298   |
| 4343 | Nuevo Avalon                                          | 609   | 4298   |
| 4344 | Campos de Nuevo Avalon                                | 609   | 4298   |
| 4345 | Huerto de Nuevo Avalon                                | 609   | 4298   |
| 4346 | Concejo de Nuevo Avalon                               | 609   | 4298   |
| 4347 | Villa Refugio                                         | 609   | 4298   |
| 4348 | Granjas de Villa Refugio                              | 609   | 4298   |
| 4349 | Serrería de Villa Refugio                             | 609   | 4298   |
| 4350 | Establos de Villa Refugio                             | 609   | 4298   |
| 4351 | El Bastión Escarlata                                  | 609   | 4298   |
| 4352 | Capilla de la Llama Carmesí                           | 609   | 4298   |
| 4353 | Torre de la Punta de la Luz                           | 609   | 4298   |
| 4354 | Punta de la Luz                                       | 609   | 4298   |
| 4355 | Cripta de los Recuerdos                               | 609   | 4298   |
| 4356 | Brecha de la Muerte                                   | 609   | 4298   |
| 4357 | El Claro Ponzoñoso                                    | 609   | 4298   |
| 4358 | Mano de Tyr                                           | 609   | 4298   |
| 4359 | Puerto del Rey                                        | 609   | 4298   |
| 4360 | Mirador Escarlata                                     | 609   | 4298   |
| 4361 | Capilla de la Esperanza de la Luz                     | 609   | 4298   |
| 4362 | Locura del Pecador                                    | 609   | 4298   |
| 4363 | Cicatriz Pestilente                                   | 609   | 4298   |
| 4364 | Molino Cejifrente                                     | 609   | 4298   |
| 4365 | Mina de Villa Refugio                                 | 609   | 4298   |
| 4366 | El Cubil de Ursoc                                     | 571   | 394    |
| 4367 | La Línea de Añublo                                    | 571   | 3711   |
| 4368 | Los Campos de Huesos                                  | 571   | 3711   |
| 4369 | Avanzada de Dorian                                    | 571   | 3711   |
| 4371 | Cráter de Mam'toth                                    | 571   | 66     |
| 4372 | Bastión de Zol'Maz                                    | 571   | 66     |
| 4373 | Zol'Heb                                               | 571   | 66     |
| 4374 | Lago de Garrafuria                                    | 571   | 66     |
| 4375 | Gundrak                                               | 571   | 66     |
| 4376 | El Matorral Silvestre                                 | 571   | 3711   |
| 4377 | Forja de Nuevo Avalon                                 | 609   | 4298   |
| 4378 | Arena de Dalaran                                      | 617   | 0      |
| 4379 | Valgarde                                              | 571   | 495    |
| 4380 | Taberna de Guardia Oeste                              | 571   | 495    |
| 4381 | Puerta                                                | 1     | 490    |
| 4382 | El Bancal del Creador                                 | 1     | 490    |
| 4383 | Pista del Lago                                        | 571   | 3711   |
| 4384 | Playa de los Ancestros                                | 607   | 0      |
| 4385 | Lago Olamarga                                         | 571   | 3711   |
| 4386 | Rápidos de Hablalluvia                                | 571   | 3711   |
| 4387 | Río Corazón Frenético                                 | 571   | 3711   |
| 4388 | Río Conquista del Invierno                            | 571   | 3711   |
| 4389 | El Pilar Toquesol                                     | 571   | 3711   |
| 4390 | Brecha Gélida                                         | 571   | 66     |
| 4391 | Excavación de Timomueca                               | 571   | 3711   |
| 4392 | La Plataforma del Tormentoso                          | 571   | 3711   |
| 4393 | Campamento Mano de la Muerte                          | 571   | 3711   |
| 4394 | Taberna Escarlata                                     | 609   | 4298   |
| 4395 | Dalaran                                               | 571   | 0      |
| 4396 | Puesto Boquilla Oxidada                               | 571   | 65     |
| 4399 | Mina de Lindeallá                                     | 571   | 3537   |
| 4400 | El Pilar Musgoluz                                     | 571   | 3711   |
| 4401 | Alto de Saragosa                                      | 571   | 3537   |
| 4402 | Elevador de Venganza                                  | 571   | 495    |
| 4403 | Avanzada Balejar                                      | 571   | 495    |
| 4404 | Posada de Nuevo Agamand                               | 571   | 495    |
| 4405 | Pasaje de los Malignos Perdidos                       | 601   | 4277   |
| 4406 | El Círculo del Valor                                  | 618   | 0      |
| 4407 | Cámara de los Lobo Gélido                             | 30    | 2597   |
| 4408 | Cámara de los Pico Tormenta                           | 30    | 2597   |
| 4411 | Puerto de Ventormenta                                 | 0     | 1519   |
| 4412 | El Mirador de los Creadores                           | 571   | 3711   |
| 4413 | El Pedestal de los Creadores                          | 571   | 3711   |
| 4414 | Torre Escarlata                                       | 571   | 65     |
| 4415 | El Bastión Violeta                                    | 608   | 0      |
| 4416 | Gundrak                                               | 604   | 0      |
| 4417 | Puerto del Embate                                     | 571   | 210    |
| 4418 | K3                                                    | 571   | 67     |
| 4419 | Colinas Veloneve                                      | 571   | 67     |
| 4420 | Bancal Veloneve                                       | 571   | 67     |
| 4421 | Garm                                                  | 571   | 67     |
| 4422 | Poblado Brunnhildar                                   | 571   | 67     |
| 4423 | Poblado Sifreldar                                     | 571   | 67     |
| 4424 | Valkyrion                                             | 571   | 67     |
| 4425 | La Mina Desolada                                      | 571   | 67     |
| 4426 | Río del Aliento de Bor                                | 571   | 67     |
| 4427 | Vanguardia Argenta                                    | 571   | 67     |
| 4428 | Fuerte Escarcha                                       | 571   | 67     |
| 4429 | Lugar del accidente de Grom'arsh                      | 571   | 67     |
| 4430 | Templo de las Tormentas                               | 571   | 67     |
| 4431 | Motor de los Creadores                                | 571   | 67     |
| 4432 | Las Estepas Inferiores                                | 571   | 67     |
| 4433 | Cumbres Espinazo de Dragón                            | 571   | 67     |
| 4434 | Nidavelir                                             | 571   | 67     |
| 4435 | Cuna de Narvir                                        | 571   | 67     |
| 4436 | Llanuras Ventisquero                                  | 571   | 67     |
| 4437 | Valle de los Viejos Inviernos                         | 571   | 67     |
| 4438 | Dun Niffelem                                          | 571   | 67     |
| 4439 | Lago Campo de Escarcha                                | 571   | 67     |
| 4440 | Truenotoño                                            | 571   | 67     |
| 4441 | Campamento Tunka'lo                                   | 571   | 67     |
| 4442 | Campamento base de Brann                              | 571   | 67     |
| 4443 | Puerta de los Ecos                                    | 571   | 67     |
| 4444 | Llanura de los Ecos                                   | 571   | 67     |
| 4445 | Ulduar                                                | 571   | 67     |
| 4446 | Bancal de los Creadores                               | 571   | 67     |
| 4447 | Puerta de los Rayos                                   | 571   | 67     |
| 4448 | Senda de los Titanes                                  | 571   | 67     |
| 4449 | Uldis                                                 | 571   | 67     |
| 4450 | Acuerdo de Loken                                      | 571   | 67     |
| 4451 | Caída de Bor                                          | 571   | 67     |
| 4452 | Aliento de Bor                                        | 571   | 67     |
| 4453 | Paso de Rohemdal                                      | 571   | 67     |
| 4454 | La Fundición de la Tormenta                           | 571   | 67     |
| 4455 | Caverna Hibernal                                      | 571   | 67     |
| 4456 | Morada Runavold                                       | 571   | 394    |
| 4457 | Reposo de Torseg                                      | 571   | 67     |
| 4458 | Campo de Minas Encajebujía                            | 571   | 67     |
| 4459 | Locura de Ricket                                      | 571   | 67     |
| 4460 | Pesadilla de Garm                                     | 571   | 67     |
| 4461 | Alto de Garm                                          | 571   | 67     |
| 4462 | Caverna Red de Cristal                                | 571   | 67     |
| 4463 | Templo de la Vida                                     | 571   | 67     |
| 4464 | Templo del Orden                                      | 571   | 67     |
| 4465 | Templo del Invierno                                   | 571   | 67     |
| 4466 | Templo de la Invención                                | 571   | 67     |
| 4467 | Ascenso de la Muerte                                  | 571   | 210    |
| 4468 | Los Campos Muertos                                    | 571   | 66     |
| 4469 | Óbito de Dargath                                      | 571   | 66     |
| 4470 | La Hondonada Oculta                                   | 571   | 210    |
| 4471 | El Maravilloso Mundo de Bernau                        | 451   | 4019   |
| 4472 | Hondonada Puño Helado                                 | 571   | 67     |
| 4473 | La Tumba Gélida                                       | 571   | 67     |
| 4474 | Las Playas Gemelas                                    | 571   | 495    |
| 4475 | Guarida de Zim'bo                                     | 571   | 394    |
| 4476 | Campamento Abandonado                                 | 571   | 67     |
| 4477 | La Cámara de las Sombras                              | 571   | 210    |
| 4478 | Pasaje Viento Helado                                  | 571   | 65     |
| 4479 | Lago Aliento Invernal                                 | 571   | 495    |
| 4480 | El Mirador Olvidado                                   | 571   | 394    |
| 4481 | Pasaje de Jintha'kalar                                | 571   | 66     |
| 4482 | Pasarela de Arriga                                    | 571   | 394    |
| 4483 | El Pasaje Perdido                                     | 571   | 3711   |
| 4484 | Refugio de Pedruscón                                  | 571   | 67     |
| 4485 | La Biblioteca del Inventor                            | 571   | 67     |
| 4486 | La Mina Gélida                                        | 571   | 67     |
| 4487 | Hondonada Témpano Gélido                              | 571   | 67     |
| 4488 | La Hondonada Aullante                                 | 571   | 67     |
| 4489 | Puesto de Avanzada de los Cruzados                    | 571   | 66     |
| 4490 | Crestormenta                                          | 571   | 67     |
| 4491 | Campamento Cascahueso                                 | 571   | 394    |
| 4492 | Sala de Ufrang                                        | 571   | 210    |
| 4493 | El Sagrario Obsidiana                                 | 615   | 0      |
| 4494 | Ahn'kahet: El Antiguo Reino                           | 619   | 0      |
| 4495 | Yunque de Fjorn                                       | 571   | 67     |
| 4496 | Jotunheim                                             | 571   | 210    |
| 4497 | Cornisa Salvaje                                       | 571   | 210    |
| 4498 | Salas de los Ancestros                                | 571   | 210    |
| 4499 | La Poza Contagiada                                    | 571   | 67     |
| 4500 | El Ojo de la Eternidad                                | 616   | 0      |
| 4501 | La Vanguardia Argenta                                 | 571   | 210    |
| 4502 | Taller de Mimir                                       | 571   | 67     |
| 4503 | Presa del Muro de Hierro                              | 571   | 210    |
| 4504 | Valle de los Ecos                                     | 571   | 210    |
| 4505 | La Brecha                                             | 571   | 210    |
| 4506 | Ciudad de la Plaga                                    | 571   | 210    |
| 4507 | El Frente Roto                                        | 571   | 210    |
| 4508 | Mord'rethar: La Puerta de la Muerte                   | 571   | 210    |
| 4509 | El Bombardeo                                          | 571   | 210    |
| 4510 | Aldur'thar: La Puerta de la Desolación                | 571   | 210    |
| 4511 | El Rompecielos                                        | 571   | 210    |
| 4512 | Martillo de Orgrim                                    | 571   | 210    |
| 4513 | Ymirheim                                              | 571   | 210    |
| 4514 | Minas de Saronita                                     | 571   | 210    |
| 4515 | La Conflagración                                      | 571   | 210    |
| 4516 | Fortificación del Muro de Hierro                      | 571   | 210    |
| 4517 | Cantera Llorosa                                       | 571   | 210    |
| 4518 | Corp'rethar: La Puerta del Horror                     | 571   | 210    |
| 4519 | El Patio de los Huesos                                | 571   | 210    |
| 4520 | Malykriss: El Bastión Inmundo                         | 571   | 210    |
| 4521 | Catedral de la Oscuridad                              | 571   | 210    |
| 4522 | Ciudadela de la Corona de Hielo                       | 571   | 210    |
| 4523 | Glaciar Corona de Hielo                               | 571   | 210    |
| 4524 | Valhalas                                              | 571   | 210    |
| 4525 | Las Cámaras Subterráneas                              | 571   | 210    |
| 4526 | Poblado Njorndar                                      | 571   | 210    |
| 4527 | Fortaleza de Balargarde                               | 571   | 210    |
| 4528 | Fortaleza de Kul'galar                                | 571   | 210    |
| 4529 | La Catedral Carmesí                                   | 571   | 210    |
| 4530 | Sagrario de Reanimación                               | 571   | 210    |
| 4531 | La Factoría de Carne                                  | 571   | 210    |
| 4532 | Taberna de Campo Venganza                             | 571   | 495    |
| 4533 | La Caída de Sindragosa                                | 571   | 210    |
| 4534 | Mina de Vildervar                                     | 571   | 495    |
| 4535 | El Foso del Colmillo                                  | 571   | 67     |
| 4536 | Caverna Aúllaescarcha                                 | 571   | 67     |
| 4537 | El Valle de la Esperanza Perdida                      | 571   | 210    |
| 4538 | El Anillo Sumergido                                   | 571   | 4197   |
| 4539 | El Templo Quebrado                                    | 571   | 4197   |
| 4540 | El Valle de los Héroes Caídos                         | 571   | 210    |
| 4541 | Enfermería de la Vanguardia                           | 571   | 210    |
| 4542 | Sala del Creador                                      | 571   | 67     |
| 4543 | Templo de Sabiduría                                   | 571   | 67     |
| 4544 | Brecha de la Muerte                                   | 0     | 139    |
| 4545 | Mina Abandonada                                       | 0     | 139    |
| 4546 | Ruinas de El Enclave Escarlata                        | 0     | 139    |
| 4547 | Cámaras de Piedra                                     | 571   | 67     |
| 4548 | Cámaras de Relámpagos                                 | 571   | 67     |
| 4549 | El Gran Árbol                                         | 571   | 2817   |
| 4550 | El Espejo del Crepúsculo                              | 571   | 2817   |
| 4551 | El Riachuelo Crepuscular                              | 571   | 2817   |
| 4552 | La Corriente Decrépita                                | 571   | 2817   |
| 4553 | El Bosque Desolado                                    | 571   | 2817   |
| 4554 | Ruinas de Shandaral                                   | 571   | 2817   |
| 4555 | El Frente Azur                                        | 571   | 2817   |
| 4556 | El Confín Violeta                                     | 571   | 2817   |
| 4557 | El Matorral Desatado                                  | 571   | 2817   |
| 4558 | Dominio de los Atracasol                              | 571   | 2817   |
| 4559 | Mirador Brisaveloz                                    | 571   | 2817   |
| 4560 | Los Bajos Fondos                                      | 571   | 4395   |
| 4564 | Alto de Krasus                                        | 571   | 4395   |
| 4567 | El Bastión Violeta                                    | 571   | 4395   |
| 4568 | El Manto de la Noche                                  | 571   | 4395   |
| 4569 | Tubería de salida de las cloacas                      | 571   | 4395   |
| 4570 | Círculo de Voluntades                                 | 571   | 4395   |
| 4571 | Sala de la Bandera de Brisa de Plata                  | 489   | 3277   |
| 4572 | Sala de la Bandera Grito de Guerra                    | 489   | 3277   |
| 4575 | Fortaleza de Conquista del Invierno                   | 571   | 4197   |
| 4576 | Puente Central                                        | 571   | 4197   |
| 4577 | Puente Oriental                                       | 571   | 4197   |
| 4578 | Puente Occidental                                     | 571   | 4197   |
| 4579 | Dubra'Jin                                             | 571   | 66     |
| 4580 | Pináculo de los Cruzados                              | 571   | 210    |
| 4581 | Torre de la Guardia en Llamas                         | 571   | 4197   |
| 4582 | Torre Filoinvierno                                    | 571   | 4197   |
| 4583 | Torre de la Vista de las Sombras                      | 571   | 4197   |
| 4584 | El Caldero de Llamas                                  | 571   | 4197   |
| 4585 | Cascadas Glaciales                                    | 571   | 4197   |
| 4586 | Riscos Ventosos                                       | 571   | 4197   |
| 4587 | El Bosque de las Sombras                              | 571   | 4197   |
| 4588 | La Guardia Negra                                      | 571   | 210    |
| 4589 | El Cenagal Escalofrío                                 | 571   | 4197   |
| 4590 | Las Estepas de la Vida                                | 571   | 4197   |
| 4591 | Vigía Silencioso                                      | 571   | 210    |
| 4592 | Guarida de Gimorak                                    | 571   | 67     |
| 4593 | El Foso de los Mefistos                               | 571   | 210    |
| 4594 | Cumbre Marca de Guerra                                | 571   | 210    |
| 4595 | Cámara de los Horrores                                | 571   | 210    |
| 4596 | El Círculo de Sufrimiento                             | 571   | 210    |
| 4597 | Alto del Sufrimiento                                  | 571   | 210    |
| 4598 | Alto de Krasus                                        | 571   | 4395   |
| 4599 | Tubería de salida de las cloacas                      | 571   | 4395   |
| 4601 | Isla de Dalaran                                       | 571   | 4395   |
| 4602 | Fuerza Interior                                       | 571   | 0      |
| 4603 | La Cámara de Archavon                                 | 624   | 0      |
| 4604 | Puerta del Sol Rojo                                   | 607   | 4384   |
| 4605 | Puerta del Zafiro Azul                                | 607   | 4384   |
| 4606 | Puerta de la Esmeralda Verde                          | 607   | 4384   |
| 4607 | Puerta de la Amatista Púrpura                         | 607   | 4384   |
| 4608 | Puerta de la Luna Amarilla                            | 607   | 4384   |
| 4609 | Patio de los Ancestros                                | 607   | 4384   |
| 4610 | Playa de Desembarco                                   | 607   | 4384   |
| 4611 | Taller Chispa Occidental                              | 571   | 4197   |
| 4612 | Taller Chispa Oriental                                | 571   | 4197   |
| 4613 | Ciudad de Dalaran                                     | 571   | 4395   |
| 4614 | Aguja de La Ciudadela Violeta                         | 571   | 4395   |
| 4615 | Naz'anak: Las Profundidades Olvidadas                 | 571   | 210    |
| 4616 | Santuario Atracasol                                   | 571   | 4395   |
| 4617 | Elevador                                              | 0     | 1497   |
| 4618 | Monumento de Antonidas                                | 571   | 4395   |
| 4619 | La Ciudadela Violeta                                  | 571   | 4395   |
| 4620 | Mercado de Magos                                      | 571   | 4395   |
| 4621 | UNUSED                                                | 571   | 67     |
| 4622 | Puesto de Avanzada de la Primera Legión               | 571   | 210    |
| 4623 | Cámara de los Reyes Conquistados                      | 619   | 4494   |
| 4624 | Bancal Infecto                                        | 619   | 4494   |
| 4625 | El Altar Profanado                                    | 619   | 4494   |
| 4626 | Ciénaga Bruñida                                       | 619   | 4494   |
| 4627 | Templo Caído de Ahn'kahet                             | 619   | 4494   |
| 4628 | Sala de Vínculos                                      | 229   | 1583   |
| 4629 | Corazón del Invierno                                  | 571   | 67     |
| 4630 | El Mar del Norte                                      | 571   | 0      |
| 4631 | El Nido de la Madre de Linaje                         | 571   | 67     |
| 4632 | Rocas Flotantes de Dalaran                            | 571   | 4395   |
| 4633 | Cercado de Raptores                                   | 600   | 4196   |
| 4635 | Fortaleza de Drak'Tharon                              | 571   | 66     |
| 4636 | El Paso Ponzoñoso                                     | 609   | 4298   |
| 4637 | Reposo de Vargoth                                     | 571   | 4395   |
| 4638 | Balcón de la Ciudadela Violeta                        | 571   | 4395   |
| 4639 | Anillo de Discrepancia                                | 571   | 3537   |
| 4640 | Anillo de Aceleración                                 | 571   | 3537   |
| 4641 | Anillo de Transmutación                               | 571   | 3537   |
| 4642 | Anillo de Alineación                                  | 571   | 3537   |
| 4646 | Lago Fresno                                           | 571   | 394    |
| 4650 | Explanada de Hierro                                   | 603   | 4273   |
| 4652 | Campo de Formación                                    | 603   | 4273   |
| 4653 | Nidal de Tajoescama                                   | 603   | 4273   |
| 4654 | La Forja Colosal                                      | 603   | 4273   |
| 4655 | La Chatarrería                                        | 603   | 4273   |
| 4656 | El Invernadero de Vida                                | 603   | 4273   |
| 4657 | El Archivum                                           | 603   | 4273   |
| 4658 | Campos del Torneo Argenta                             | 571   | 210    |
| 4665 | Campamento Base de la Expedición                      | 603   | 4273   |
| 4666 | Pabellón Atracasol                                    | 571   | 210    |
| 4667 | Pabellón de El Pacto de Plata                         | 571   | 210    |
| 4668 | La Residencia Cooper                                  | 0     | 40     |
| 4669 | La Liza de los Campeones                              | 571   | 210    |
| 4670 | La Liza de los Aspirantes                             | 571   | 210    |
| 4671 | La Liza de los Valerosos Argenta                      | 571   | 210    |
| 4672 | La Liza de los Valerosos de la Alianza                | 571   | 210    |
| 4673 | La Liza de los Valerosos de la Horda                  | 571   | 210    |
| 4674 | Pabellón Argenta                                      | 571   | 210    |
| 4676 | Pabellón Atracasol                                    | 571   | 210    |
| 4677 | Pabellón de El Pacto de Plata                         | 571   | 210    |
| 4679 | La Caverna Abandonada                                 | 0     | 1537   |
| 4688 | claytonio test area                                   | 451   | 151    |
| 4692 | Reposo de Quel'Delar                                  | 571   | 210    |
| 4710 | Isla de la Conquista                                  | 628   | 0      |
| 4722 | Prueba del Cruzado                                    | 649   | 0      |
| 4723 | Prueba del Campeón                                    | 650   | 0      |
| 4739 | Plaza Tejerruna                                       | 571   | 4395   |
| 4740 | El Enclave de Plata                                   | 571   | 4395   |
| 4741 | Tierra de Nadie de Isla de la Conquista               | 628   | 4710   |
| 4742 | Desembarco de Hrothgar                                | 571   | 0      |
| 4743 | Avanzada del Portavoz de la Muerte                    | 571   | 210    |
| 4747 | Taller                                                | 628   | 4710   |
| 4748 | Cantera                                               | 628   | 4710   |
| 4749 | Muelles                                               | 628   | 4710   |
| 4750 | Hangar                                                | 628   | 4710   |
| 4751 | Refinería                                             | 628   | 4710   |
| 4752 | Fortaleza de la Horda                                 | 628   | 4710   |
| 4753 | Fortaleza de la Alianza                               | 628   | 4710   |
| 4760 | La Travesía del Atracamar                             | 571   | 4742   |
| 4763 | Transporte: Nave de Guerra de la Alianza              | 641   | 0      |
| 4764 | Transporte: Nave de Guerra de la Horda                | 642   | 0      |
| 4769 | Desembarco de Hrothgar                                | 571   | 4742   |
| 4809 | La Forja de Almas                                     | 632   | 0      |
| 4812 | Ciudadela de la Corona de Hielo                       | 631   | 0      |
| 4813 | Foso de Saron                                         | 658   | 0      |
| 4820 | Cámaras de Reflexión                                  | 668   | 0      |
| 4832 | Transporte: Nave de Guerra de la Alianza              | 672   | 0      |
| 4833 | Transporte: Nave de Guerra de la Horda                | 673   | 0      |
| 4859 | El Trono Helado                                       | 631   | 4812   |
| 4862 | Las Cámaras Heladas                                   | 571   | 210    |
| 4889 | La Guarida de la Reina de Escarcha                    | 631   | 4812   |
| 4890 | Laboratorio Horrores y Risas Alquímicas de Putricidio | 631   | 4812   |
| 4891 | El Sagrario de Sangre                                 | 631   | 4812   |
| 4892 | La Sala Carmesí                                       | 631   | 4812   |
| 4893 | La Guarida de la Reina de Escarcha                    | 631   | 0      |
| 4894 | Laboratorio Horrores y Risas Alquímicas de Putricidio | 631   | 0      |
| 4895 | La Sala Carmesí                                       | 631   | 0      |
| 4896 | El Trono Helado                                       | 631   | 0      |
| 4897 | El Sagrario de Sangre                                 | 631   | 0      |
| 4898 | Agonía de Escarcha                                    | 631   | 4896   |
| 4904 | El Trayecto Oscuro                                    | 658   | 4813   |
| 4905 | Dominio del Señor de la Plaga                         | 658   | 4813   |
| 4906 | El Trono de las Sombras                               | 668   | 4820   |
| 4908 | El Pasaje Oculto                                      | 668   | 4820   |
| 4910 | Agonía de Escarcha                                    | 631   | 4812   |
| 4987 | El Sagrario Rubí                                      | 724   | 0      |