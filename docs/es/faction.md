# Faction

**Faction.dbc**

[`Volver a:DBC`](dbc-index.md)

Éste archivo DBC alberga información acerca de todas las facciones existentes dentro del juego; las mismas son únicas y representan una facción con la cual un jugador cualquiera puede obtener reputación.

**IMPORTANTE:** Los valores a continuación son utilizados para casi todas las tablas, exceptuando [creature\_template](creature_template) y [gameobject_template\_addon](gameobject_template_addon).


## Estructura

| Columna | Campo               | Tipo                                                           | Notas                                                                                                                                                                                                                                                                                                                                                                              |
|---------|---------------------|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1       | ID                  | Integer                                                        | Identificador Único de la facción correspondiente.                                                                                                                                                                                                                                                                                                                                 |
| 2       | reputationIndex     | Integer                                                        | Cada facción en la cual es posible obtener reputación tiene un número único que iría en este campo. En caso contrario, aquellas facciones con las cuales no es posible obtener reputación tienen -1 como valor en este campo.                                                                                                                                                      |
| 3       | reputationRaceMask  | BitMask                                                        | Apunta a otro Identificador (ID) de Aliados/EnGuerra                                                                                                                                                                                                                                                                                                                               |
| 4       | reputationRaceMask  | BitMask                                                        | Por ejemplo, Bastión del Honor tiene 1101,690 y Thrallmar 690,1101.                                                                                                                                                                                                                                                                                                                |
| 5       | reputationRaceMask  | BitMask                                                        | Únicamente aquellas facciones de ciudades principales poseen un valor. Posible relación con algunos modificadores y 17 (Ventormenta = 1. Orgrimmar = 2. Clan Martillo Salvaje y Forjaz = 4. Darnassus = 8. Entrañas = 16. Exiliados de Gnomeregan = 64. Facciones de la Ciudad de Shattrath y Ciudad de Lunargenta = 512. Cima del Trueno y Trols Lanza Negra = 528. Exodar= 1024) |
| 6       | reputationRaceMask  | BitMask                                                        | Únicamente aquellas ciudades de la Horda tienen un valor de este tipo. Posible relación ccon algunos modificadores y 18 (Ciudad de Lunargenta = 16. Cima del Trueno = 32. Trols Lanza Negra = 128. Entrañas = 512. Orgrimmar = 528.)                                                                                                                                               |
| 7       | reputationClassMask | BitMask                                                        | (Círculo Cenarion = 479. Bajo Arrabal, "Amistoso, Oculto", Ala Abisal = 1503 . Guardia del cielo Sha'tari)                                                                                                                                                                                                                                                                         |
| 8       | reputationClassMask | BitMask                                                        | (1024 = Círculo Cenarion;)                                                                                                                                                                                                                                                                                                                                                         |
| 9       | reputationClassMask | BitMask                                                        | Nunca ha sido usado en parches pre 3.*.*, sin embargo 0x80 en "Kirin Tor".                                                                                                                                                                                                                                                                                                         |
| 10      | reputationClassMask | BitMask                                                        | Nunca ha sido usado en parches pre 3.*.*, sin embargo 0x80 en "Kirin Tor".                                                                                                                                                                                                                                                                                                         |
| 11      | reputationBase      | Integer\[4\]                                                   | Basado en: Neutral = 0.                                                                                                                                                                                                                                                                                                                                                            |
| 15      | reputationFlags     | Integer\[4\]                                                   |                                                                                                                                                                                                                                                                                                                                                                                    |
| 19      | **parentFactionID** | iRefID                                                         | Recursivo. Por ejemplo, Entrañas lista el Identificador (ID) número 67, por tanto es Horda.                                                                                                                                                                                                                                                                                        |
| 20      | parentFactionMod    | Float\[2\]                                                     |                                                                                                                                                                                                                                                                                                                                                                                    |
| 22      | parentFactionCap    | Integer\[2\]                                                   |                                                                                                                                                                                                                                                                                                                                                                                    |
| 24      | Name                | [Loc](Localization_lang)                                       | Muestra el nombre de la facción en cuestión.                                                                                                                                                                                                                                                                                                                                       |
| 41      | Description         | [Loc](https://wowdev.wiki/Localization "Loc")                  | Vista en la Interfaz de Reputación dentro del juego al hacer clic sobre ella.                                                                                                                                                                                                                                                                                                      |

## Flags

       FACTION_FLAG_NONE             = 0x00, // Sin marcador de facción
       FACTION_FLAG_VISIBLE          = 0x01, // Se hace visible en el cliente (establecido automáticamente o puede establecerse con la interacción de un objetivo perteneciente a la facción)
       FACTION_FLAG_AT_WAR           = 0x02, // Habilita el botón 'EnGuerra' dentro del cliente. Controlado por el jugador (exceptuando el bando contrario, siempre se encontrará 'EnGuerra'), el marcador únicamente es establecido en la creación inicial.
       FACTION_FLAG_HIDDEN           = 0x04, // Facción oculta dentro del Panel de Reputación del personaje (el jugador puede obtener reputación con la facción, pero este dato no será visto en el Cliente de Juego)
       FACTION_FLAG_INVISIBLE_FORCED = 0x08, // Siempre sobreescribe FACTION_FLAG_VISIBLE y oculta la facción en rep.list. Usado principalmente para ocultar las facciones del bando contrario.
       FACTION_FLAG_PEACE_FORCED     = 0x10, // Siempre sobreescribe FACTION_FLAG_AT_WAR. Usado principalmente para evitar la guerra con las facciones del propio bando.
       FACTION_FLAG_INACTIVE         = 0x20, // Controlado por el jugador, el estado se almacena en characters.data (CMSG_SET_FACTION_INACTIVE)
       FACTION_FLAG_RIVAL            = 0x40, // Marcador de ambas facciones en Terrallende que compiten entre sí.
       FACTION_FLAG_SPECIAL          = 0x80, // Las ciudades de origen de la horda y la alianza, y sus aliados de Rasganorte poseen este marcador.

## **Contenido**

| **Identificación (ID) de la Facción** | **Identificación (ID) de la Reputación** | **Nombre**                                         |
|---------------------------------------|------------------------------------------|----------------------------------------------------|
| 1                                     | -1                                       | JUGADOR, humano                                    |
| 2                                     | -1                                       | JUGADOR, orco                                      |
| 3                                     | -1                                       | JUGADOR, enano                                     |
| 4                                     | -1                                       | JUGADOR, elfo de la noche                          |
| 5                                     | -1                                       | JUGADOR, no-muerto                                 |
| 6                                     | -1                                       | JUGADOR, tauren                                    |
| 7                                     | -1                                       | Criatura                                           |
| 8                                     | -1                                       | JUGADOR, gnomo                                     |
| 9                                     | -1                                       | JUGADOR, trol                                      |
| 14                                    | -1                                       | Monstruo                                           |
| 15                                    | -1                                       | Hermandad Defias                                   |
| 16                                    | -1                                       | Gnoll: Zarparrío                                   |
| 17                                    | -1                                       | Gnoll: Crestagrana                                 |
| 18                                    | -1                                       | Gnoll: Pielsombra                                  |
| 19                                    | -1                                       | Múrloc                                             |
| 20                                    | -1                                       | No-muertos, Plaga                                  |
| 21                                    | 1                                        | Bahía del Botín                                    |
| 22                                    | -1                                       | Bestia: araña                                      |
| 23                                    | -1                                       | Bestia: jabalí                                     |
| 24                                    | -1                                       | Huargen                                            |
| 25                                    | -1                                       | Kóbold                                             |
| 26                                    | -1                                       | Trol, Sangrapellejo                                |
| 27                                    | -1                                       | Trol, Machacacráneos                               |
| 28                                    | -1                                       | Presa                                              |
| 29                                    | -1                                       | Bestia: lobo                                       |
| 30                                    | -1                                       | Traidor de la Hermandad Defias                     |
| 31                                    | -1                                       | Amistoso                                           |
| 32                                    | -1                                       | Trogg                                              |
| 33                                    | -1                                       | Trol, Peloescarcha                                 |
| 34                                    | -1                                       | Orco, Roca Negra                                   |
| 35                                    | -1                                       | Villian                                            |
| 36                                    | -1                                       | Víctima                                            |
| 37                                    | -1                                       | Bestia: oso                                        |
| 38                                    | -1                                       | Ogro                                               |
| 39                                    | -1                                       | Mercenarios de Kurzen                              |
| 40                                    | -1                                       | Acompañante                                        |
| 41                                    | -1                                       | Ventura y Cía.                                     |
| 42                                    | -1                                       | Bestia: raptor                                     |
| 43                                    | -1                                       | Basilisco                                          |
| 44                                    | -1                                       | Vuelo, Verde                                       |
| 45                                    | -1                                       | Los Perdidos                                       |
| 46                                    | 29                                       | Herrería: armaduras                                |
| 47                                    | 20                                       | Forjaz                                             |
| 48                                    | -1                                       | Enanos Hierro Negro                                |
| 49                                    | -1                                       | Humano, Guardia Nocturna                           |
| 50                                    | -1                                       | Vuelo, Rojo                                        |
| 51                                    | -1                                       | Gnoll: Pellejomusgo                                |
| 52                                    | -1                                       | Orco, Faucedraco                                   |
| 53                                    | -1                                       | Gnomo: paria                                       |
| 54                                    | 18                                       | Exiliados de Gnomeregan                            |
| 55                                    | -1                                       | Leopardo                                           |
| 56                                    | -1                                       | Cruzada Escarlata                                  |
| 57                                    | -1                                       | Gnoll: Putrepellejo                                |
| 58                                    | -1                                       | Bestia: gorila                                     |
| 59                                    | 4                                        | Hermandad del Torio                                |
| 60                                    | -1                                       | Naga                                               |
| 61                                    | -1                                       | Dalaran                                            |
| 62                                    | -1                                       | Espíritu Abandonado                                |
| 63                                    | -1                                       | Aullido Oscuro                                     |
| 64                                    | -1                                       | Grell                                              |
| 65                                    | -1                                       | Fúrbolg                                            |
| 66                                    | -1                                       | Genérico de la Horda                               |
| 67                                    | 12                                       | Horda                                              |
| 68                                    | 17                                       | Entrañas                                           |
| 69                                    | 21                                       | Darnassus                                          |
| 70                                    | 6                                        | La Hermandad                                       |
| 71                                    | -1                                       | Milicia de Trabalomas                              |
| 72                                    | 19                                       | Ventormenta                                        |
| 73                                    | -1                                       | Demonio                                            |
| 74                                    | -1                                       | Elemental                                          |
| 75                                    | -1                                       | Espíritu                                           |
| 76                                    | 14                                       | Orgrimmar                                          |
| 77                                    | -1                                       | Tesoro                                             |
| 78                                    | -1                                       | Gnoll: Morrobarro                                  |
| 79                                    | -1                                       | Trabalomas, Alcalde de Costasur                    |
| 80                                    | -1                                       | Vuelo, Negro                                       |
| 81                                    | 16                                       | Cima del Trueno                                    |
| 82                                    | -1                                       | Trol, Secacorteza                                  |
| 83                                    | 23                                       | Peletería: elemental                               |
| 84                                    | -1                                       | Jabaespín, Crines de Acero                         |
| 85                                    | -1                                       | Jabaespín, Erizapúas                               |
| 86                                    | 22                                       | Peletería: dragontina                              |
| 87                                    | 0                                        | Bucaneros Velasangre                               |
| 88                                    | -1                                       | Brazanegra                                         |
| 89                                    | -1                                       | Makrura                                            |
| 90                                    | -1                                       | Centauro, Kolkar                                   |
| 91                                    | -1                                       | Centauro, Galak                                    |
| 92                                    | 2                                        | Centauros del clan Gelkis                          |
| 93                                    | 3                                        | Centauros del clan Magram                          |
| 94                                    | -1                                       | Maraudine                                          |
| 108                                   | -1                                       | Theramore                                          |
| 109                                   | -1                                       | Jabaespín, Rajacieno                               |
| 110                                   | -1                                       | Jabaespín, Crines de Acero 2                       |
| 111                                   | -1                                       | Jabaespín, Galponmuerte                            |
| 128                                   | -1                                       | Enemigo                                            |
| 148                                   | -1                                       | Ambiente                                           |
| 168                                   | -1                                       | Caravana Nethergarde                               |
| 169                                   | 10                                       | Cártel Bonvapor                                    |
| 189                                   | -1                                       | Genérico de la Alianza                             |
| 209                                   | -1                                       | Nethergarde                                        |
| 229                                   | -1                                       | Cuevas de los Lamentos                             |
| 249                                   | -1                                       | Silítidos                                          |
| 269                                   | -1                                       | Lunargenta Despogiz                                |
| 270                                   | 51                                       | Tribu Zandalar                                     |
| 289                                   | 30                                       | Herrería: armas                                    |
| 309                                   | -1                                       | Escórpido                                          |
| 310                                   | -1                                       | Bestia: murciélago                                 |
| 311                                   | -1                                       | Titán                                              |
| 329                                   | -1                                       | Capataz Fizzule                                    |
| 349                                   | 5                                        | Ravenholdt                                         |
| 369                                   | 7                                        | Gadgetzan                                          |
| 389                                   | -1                                       | Bicho de Gnomeregan                                |
| 409                                   | -1                                       | Arpía                                              |
| 429                                   | -1                                       | Filo Ardiente                                      |
| 449                                   | -1                                       | Furtivo Sedaumbría                                 |
| 450                                   | -1                                       | Araña abrasadora                                   |
| 469                                   | 11                                       | Alianza                                            |
| 470                                   | 9                                        | Trinquete                                          |
| 471                                   | 8                                        | Clan Martillo Salvaje                              |
| 489                                   | -1                                       | Goblin, Dueño de bar Hierro Negro                  |
| 509                                   | 53                                       | Liga de Arathor                                    |
| 510                                   | 52                                       | Los Rapiñadores                                    |
| 511                                   | -1                                       | Gigante                                            |
| 529                                   | 13                                       | El Alba Argenta                                    |
| 530                                   | 15                                       | Trols Lanza Negra                                  |
| 531                                   | -1                                       | Vuelo, Bronce                                      |
| 532                                   | -1                                       | Vuelo, Azul                                        |
| 549                                   | 24                                       | Peletería: tribal                                  |
| 550                                   | 26                                       | Ingeniería: goblin                                 |
| 551                                   | 25                                       | Ingeniería: gnoma                                  |
| 569                                   | 33                                       | Herrería: martillos                                |
| 570                                   | 31                                       | Herrería: hachas                                   |
| 571                                   | 32                                       | Herrería: espadas                                  |
| 572                                   | -1                                       | Trol, Vilrama                                      |
| 573                                   | -1                                       | Filibusteros de los Mares del Sur                  |
| 574                                   | 34                                       | Castel Darrow                                      |
| 575                                   | -1                                       | Fúrbolg, incorrupto                                |
| 576                                   | 35                                       | Bastión Fauces de Madera                           |
| 577                                   | 28                                       | Vista Eterna                                       |
| 589                                   | 27                                       | Instructores de Sableinvernales                    |
| 609                                   | 36                                       | Círculo Cenarion                                   |
| 629                                   | -1                                       | Trols Rompelanzas                                  |
| 630                                   | -1                                       | Instructores de Ravasaurios                        |
| 649                                   | -1                                       | Mayordomo Executus                                 |
| 669                                   | -1                                       | Bestia: pájaro carroñero                           |
| 670                                   | -1                                       | Bestia: gato                                       |
| 671                                   | -1                                       | Bestia: cangrejo                                   |
| 672                                   | -1                                       | Bestia: crocolisco                                 |
| 673                                   | -1                                       | Bestia: hiena                                      |
| 674                                   | -1                                       | Bestia: búho                                       |
| 675                                   | -1                                       | Bestia: escórpido                                  |
| 676                                   | -1                                       | Bestia: zancaalta                                  |
| 677                                   | -1                                       | Bestia: tortuga                                    |
| 678                                   | -1                                       | Bestia: serpiente alada                            |
| 679                                   | -1                                       | Muñeco de entrenamiento                            |
| 689                                   | -1                                       | Vuelo, Negro: cebo                                 |
| 709                                   | -1                                       | Neutral en campo de batalla                        |
| 729                                   | 41                                       | Clan Lobo Gélido                                   |
| 730                                   | 40                                       | Guardia Pico Tormenta                              |
| 749                                   | 42                                       | Srs. del Agua de Hydraxis                          |
| 750                                   | -1                                       | Señores del Fuego de Sulfuron                      |
| 769                                   | -1                                       | Muñeco de Gizlock                                  |
| 770                                   | -1                                       | Talismán de Gizlock                                |
| 771                                   | -1                                       | Gizlock                                            |
| 789                                   | -1                                       | Moro\'gan                                          |
| 790                                   | -1                                       | Guía espiritual: Alianza                           |
| 809                                   | 44                                       | Shen\'dralar                                       |
| 829                                   | -1                                       | Ogro (capitán Kromcrush)                           |
| 849                                   | -1                                       | Guía espiritual: Horda                             |
| 869                                   | -1                                       | Jaedenar                                           |
| 889                                   | 46                                       | Escoltas Grito de Guerra                           |
| 890                                   | 45                                       | Centinelas Ala de Plata                            |
| 891                                   | 47                                       | Fuerzas de la Alianza                              |
| 892                                   | 48                                       | Fuerzas de la Horda                                |
| 893                                   | -1                                       | Trols Sañadiente                                   |
| 909                                   | 50                                       | Feria de la Luna Negra                             |
| 910                                   | 54                                       | Linaje de Nozdormu                                 |
| 911                                   | 55                                       | Ciudad de Lunargenta                               |
| 912                                   | -1                                       | Poder de Kalimdor                                  |
| 914                                   | -1                                       | JUGADOR, elfo de sangre                            |
| 915                                   | -1                                       | Ejércitos de C\'Thun                               |
| 916                                   | -1                                       | Atacantes silítidos                                |
| 917                                   | -1                                       | Brigada de Forjaz                                  |
| 918                                   | -1                                       | Enemigos CR                                        |
| 919                                   | -1                                       | Objetos CR                                         |
| 920                                   | -1                                       | Rojo                                               |
| 921                                   | -1                                       | Azul                                               |
| 922                                   | 56                                       | Tranquillien                                       |
| 923                                   | -1                                       | Los Errantes                                       |
| 924                                   | -1                                       | DEPRECATED                                         |
| 925                                   | -1                                       | Los Caminante del Sol                              |
| 926                                   | -1                                       | Hermandad de Magíster                              |
| 927                                   | -1                                       | JUGADOR, draenei                                   |
| 928                                   | -1                                       | Invasores de la Plaga                              |
| 929                                   | -1                                       | Clan Machacasangre                                 |
| 930                                   | 49                                       | El Exodar                                          |
| 931                                   | -1                                       | Facción de prueba (no es real)                     |
| 932                                   | 58                                       | Los Aldor                                          |
| 933                                   | 60                                       | El Consorcio                                       |
| 934                                   | 62                                       | Los Arúspices                                      |
| 935                                   | 39                                       | Los Sha\'tar                                       |
| 936                                   | 59                                       | Ciudad de Shattrath                                |
| 937                                   | -1                                       | Trol, bosque                                       |
| 938                                   | -1                                       | Los Omenai                                         |
| 939                                   | -1                                       | DEPRECATED                                         |
| 940                                   | -1                                       | Los Hijos de Lothar                                |
| 941                                   | 61                                       | Los Mag\'har                                       |
| 942                                   | 64                                       | Expedición Cenarion                                |
| 943                                   | -1                                       | Orco vil                                           |
| 944                                   | -1                                       | Fantasma de orco vil                               |
| 945                                   | -1                                       | Hijos de los Fantasmas de Lothar                   |
| 946                                   | 38                                       | Bastión del Honor                                  |
| 947                                   | 37                                       | Thrallmar                                          |
| 948                                   | 86                                       | Facción de prueba 2                                |
| 949                                   | 85                                       | Facción de prueba 1                                |
| 950                                   | -1                                       | ParaWoW - Bandera                                  |
| 951                                   | -1                                       | ParaWoW - Activador de bandera de la Alianza (DND) |
| 952                                   | 87                                       | Facción de prueba 3                                |
| 953                                   | -1                                       | Facción de prueba 4                                |
| 954                                   | -1                                       | ParaWoW - Activador de bandera de la Horda (DND)   |
| 955                                   | -1                                       | Tábidos                                            |
| 956                                   | -1                                       | El Etereum                                         |
| 957                                   | -1                                       | Elemental de tierra                                |
| 958                                   | -1                                       | Robots luchadores                                  |
| 959                                   | -1                                       | Actor bueno                                        |
| 960                                   | -1                                       | Actor malo                                         |
| 961                                   | -1                                       | Fúrbolg Semprepino                                 |
| 962                                   | -1                                       | Buhíco enloquecido                                 |
| 963                                   | -1                                       | Ajedrez Alianza                                    |
| 964                                   | -1                                       | Ajedrez Horda                                      |
| 965                                   | -1                                       | Monstruo de entrenamiento                          |
| 966                                   | -1                                       | Compañero de monstruo de entrenamiento             |
| 967                                   | 63                                       | El Ojo Violeta                                     |
| 968                                   | -1                                       | Halcones del Sol                                   |
| 969                                   | -1                                       | Mano de Argus                                      |
| 970                                   | 65                                       | Esporaggar                                         |
| 971                                   | -1                                       | Gigante Fungal                                     |
| 972                                   | -1                                       | Esporiélago                                        |
| 973                                   | -1                                       | Monstruo, predador                                 |
| 974                                   | -1                                       | Monstruo, presa                                    |
| 975                                   | -1                                       | Anomalía del vacío                                 |
| 976                                   | -1                                       | Defensores de Hyjal                                |
| 977                                   | -1                                       | Invasores de Hyjal                                 |
| 978                                   | 66                                       | Kurenai                                            |
| 979                                   | -1                                       | Anillo de la Tierra                                |
| 980                                   | 43                                       | The Burning Crusade                                |
| 981                                   | -1                                       | Arakkoa                                            |
| 982                                   | -1                                       | Estandarte de Marisma de Zangar (Alianza)          |
| 983                                   | -1                                       | Estandarte de Marisma de Zangar (Horda)            |
| 984                                   | -1                                       | Estandarte de Marisma de Zangar (Neutral)          |
| 985                                   | -1                                       | Cavernas del Tiempo - Thrall                       |
| 986                                   | -1                                       | Cavernas del Tiempo - Durnholde                    |
| 987                                   | -1                                       | Cavernas del Tiempo - Guardias de Costasur         |
| 988                                   | -1                                       | Secreto del Consejo de la Sombra                   |
| 989                                   | 67                                       | Vigilantes del Tiempo                              |
| 990                                   | 57                                       | La Escama de las Arenas                            |
| 991                                   | -1                                       | Defensor del Portal Oscuro, Alianza                |
| 992                                   | -1                                       | Defensor del Portal Oscuro, Horda                  |
| 993                                   | -1                                       | Agresor del Portal Oscuro, Legión                  |
| 994                                   | -1                                       | Activador de incitador                             |
| 995                                   | -1                                       | Activador de incitador 2                           |
| 996                                   | -1                                       | Activador de incitador 3                           |
| 997                                   | -1                                       | Activador de incitador 4                           |
| 998                                   | -1                                       | Activador de incitador 5                           |
| 999                                   | -1                                       | Criatura de maná                                   |
| 1000                                  | -1                                       | Sirviente de Khadgar                               |
| 1001                                  | -1                                       | Clan Aguja del Filo                                |
| 1002                                  | -1                                       | Compañero de entrenamiento de El Etereum           |
| 1003                                  | -1                                       | Protectorado                                       |
| 1004                                  | -1                                       | Aniquilador Arcano (DNR)                           |
| 1005                                  | 68                                       | Amistoso, oculto                                   |
| 1006                                  | -1                                       | Kirin\'Var - Dathric                               |
| 1007                                  | -1                                       | Kirin\'Var - Belmara                               |
| 1008                                  | -1                                       | Kirin\'Var - Luminrath                             |
| 1009                                  | -1                                       | Kirin\'Var - Cohlien                               |
| 1010                                  | -1                                       | Sirviente de Illidan                               |
| 1011                                  | 69                                       | Bajo Arrabal                                       |
| 1012                                  | 70                                       | Juramorte Lengua de ceniza                         |
| 1013                                  | -1                                       | Espíritus de Sombraluna 1                          |
| 1014                                  | -1                                       | Espíritus de Sombraluna 2                          |
| 1015                                  | 71                                       | Ala Abisal                                         |
| 1016                                  | -1                                       | Culto vermis                                       |
| 1017                                  | -1                                       | Antárboles                                         |
| 1018                                  | -1                                       | Demonio Leotheras I                                |
| 1019                                  | -1                                       | Demonio Leotheras II                               |
| 1020                                  | -1                                       | Demonio Leotheras III                              |
| 1021                                  | -1                                       | Demonio Leotheras IV                               |
| 1022                                  | -1                                       | Demonio Leotheras V                                |
| 1023                                  | -1                                       | Azaloth                                            |
| 1024                                  | -1                                       | Despellejador de roca                              |
| 1025                                  | -1                                       | Cazador despellejador                              |
| 1026                                  | -1                                       | Sombra de Sombraluna                               |
| 1027                                  | -1                                       | Comunicador de la Legión                           |
| 1028                                  | -1                                       | Ancianos del Bosque del Cuervo                     |
| 1029                                  | -1                                       | Ajedrez, amistoso con todo el tablero              |
| 1030                                  | -1                                       | Puertas del Templo Oscuro - Illidari               |
| 1031                                  | 72                                       | Guardia del cielo Sha\'tari                        |
| 1032                                  | -1                                       | Área 52                                            |
| 1033                                  | -1                                       | Maiev                                              |
| 1034                                  | -1                                       | Arakkoa oscuro Skettis                             |
| 1035                                  | -1                                       | Arakkoa Skettis                                    |
| 1036                                  | -1                                       | Enemigo Faucedraco                                 |
| 1037                                  | 88                                       | Vanguardia de la Alianza                           |
| 1038                                  | 73                                       | Ogri\'la                                           |
| 1039                                  | -1                                       | Devastador                                         |
| 1040                                  | -1                                       | REUSE                                              |
| 1041                                  | -1                                       | Furia                                              |
| 1042                                  | -1                                       | Enemigo de la Guardia del cielo                    |
| 1043                                  | -1                                       | Mofeta, Petunia                                    |
| 1044                                  | -1                                       | Desierto de Theramore                              |
| 1045                                  | -1                                       | Vrykul                                             |
| 1046                                  | -1                                       | Piratas del Mar del Norte                          |
| 1047                                  | -1                                       | Colmillarr                                         |
| 1048                                  | -1                                       | UNUSED                                             |
| 1049                                  | -1                                       | Trol, Amani                                        |
| 1050                                  | 74                                       | Expedición de Denuedo                              |
| 1051                                  | -1                                       | UNUSED                                             |
| 1052                                  | 75                                       | Expedición de la Horda                             |
| 1053                                  | -1                                       | Guardia Oeste                                      |
| 1054                                  | -1                                       | Grifo moteado                                      |
| 1055                                  | -1                                       | Can de peste domesticado                           |
| 1056                                  | -1                                       | Vrykul (espíritu antiguo 1)                        |
| 1057                                  | -1                                       | Vrykul (espíritu antiguo 2)                        |
| 1058                                  | -1                                       | Vrykul (espíritu antiguo 3)                        |
| 1059                                  | -1                                       | CLB - Bandera - Alianza                            |
| 1060                                  | -1                                       | Test                                               |
| 1061                                  | -1                                       | vrykul                                             |
| 1062                                  | -1                                       | Gladiador vrykul                                   |
| 1063                                  | -1                                       | Combatiente de Valgarde                            |
| 1064                                  | 76                                       | Los taunka                                         |
| 1065                                  | -1                                       | Monster, Reacción de fuerza de zona 1              |
| 1066                                  | -1                                       | Monster, Reacción de fuerza de zona 2              |
| 1067                                  | 77                                       | La Mano de la Venganza                             |
| 1068                                  | 78                                       | Liga de Expedicionarios                            |
| 1069                                  | -1                                       | Ram Racing Powerup DND                             |
| 1070                                  | -1                                       | Ram Racing Trap DND                                |
| 1071                                  | -1                                       | Ardillas de Craig                                  |
| 1072                                  | -1                                       | REUSE                                              |
| 1073                                  | 79                                       | Los Kalu\'ak                                       |
| 1074                                  | -1                                       | Fiesta - Barrica de agua                           |
| 1075                                  | -1                                       | Fiesta - Genérico                                  |
| 1076                                  | -1                                       | Enanos de Hierro                                   |
| 1077                                  | 80                                       | Ofensiva Sol Devastado                             |
| 1078                                  | -1                                       | Mascota de vanidad combativa                       |
| 1079                                  | -1                                       | Múrloc, Aleta Invernal                             |
| 1080                                  | -1                                       | Aliado, forzar reacción                            |
| 1081                                  | -1                                       | Objeto, Reacción de fuerza                         |
| 1082                                  | 82                                       | REUSE                                              |
| 1083                                  | -1                                       | REUSE                                              |
| 1084                                  | -1                                       | Vrykul, mar                                        |
| 1085                                  | 81                                       | Ofensiva Grito de Guerra                           |
| 1086                                  | -1                                       | Cazador furtivo                                    |
| 1087                                  | -1                                       | Monstruo de Fiesta                                 |
| 1088                                  | -1                                       | Fúrbolg, Colmillorrojo                             |
| 1089                                  | -1                                       | Fúrbolg, Pataescarcha                              |
| 1090                                  | 84                                       | Kirin Tor                                          |
| 1091                                  | 83                                       | El Acuerdo del Reposo del Dragón                   |
| 1092                                  | -1                                       | Azjol-Nerub                                        |
| 1093                                  | -1                                       | REUSE                                              |
| 1094                                  | 90                                       | El Pacto de Plata                                  |
| 1095                                  | -1                                       | Trampero de las Colinas Pardas                     |
| 1096                                  | -1                                       | REUSE                                              |
| 1097                                  | 89                                       | Wrath of the Lich King                             |
| 1098                                  | 91                                       | Caballeros de la Espada de Ébano                   |
| 1099                                  | -1                                       | Puerta de Cólera Plaga                             |
| 1100                                  | -1                                       | Puerta de Cólera Alianza                           |
| 1101                                  | -1                                       | Puerta de Cólera Horda                             |
| 1102                                  | -1                                       | CLB - Bandera - Horda                              |
| 1103                                  | -1                                       | CLB - Bandera - Neutral                            |
| 1104                                  | 92                                       | Tribu Corazón Frenético                            |
| 1105                                  | 93                                       | Los Oráculos                                       |
| 1106                                  | 94                                       | Cruzada Argenta                                    |
| 1107                                  | -1                                       | Trol, Drakkari                                     |
| 1108                                  | -1                                       | CdT Arthas                                         |
| 1109                                  | -1                                       | CdT Ciudadano de Stratholme                        |
| 1110                                  | -1                                       | CdT Plaga                                          |
| 1111                                  | -1                                       | Freya                                              |
| 1112                                  | -1                                       | Montura, taxi, Alianza                             |
| 1113                                  | -1                                       | Montura, taxi, Horda                               |
| 1114                                  | -1                                       | Montura, taxi, neutral                             |
| 1115                                  | -1                                       | Elemental, agua                                    |
| 1116                                  | -1                                       | Elemental, aire                                    |
| 1117                                  | 95                                       | Cuenca de Sholazar                                 |
| 1118                                  | 96                                       | Clásicas                                           |
| 1119                                  | 97                                       | Los Hijos de Hodir                                 |
| 1120                                  | -1                                       | Gigantes de Hierro                                 |
| 1121                                  | -1                                       | Vrykul de escarcha                                 |
| 1122                                  | -1                                       | Terráneo                                           |
| 1123                                  | -1                                       | Árbitro monstruo                                   |
| 1124                                  | 98                                       | Los Atracasol                                      |
| 1125                                  | -1                                       | Encuentro Hyldnir                                  |
| 1126                                  | 99                                       | Los Natoescarcha                                   |
| 1127                                  | -1                                       | Orgrimmar (Alex Test)                              |
| 1136                                  | 100                                      | Conversión de Tranquillien                         |
| 1137                                  | 101                                      | Conversión Sableinvernales                         |
| 1145                                  | -1                                       | Odia todo                                          |
| 1154                                  | 102                                      | Conversión Pacto de Plata                          |
| 1155                                  | 103                                      | Conversión Atracasol                               |
| 1156                                  | 104                                      | El Veredicto Cinéreo                               |
| 1159                                  | -1                                       | CLB - Bandera - Alianza 2                          |
| 1160                                  | -1                                       | CLB - Bandera - Horda 2                            |
