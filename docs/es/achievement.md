
# Logros

[`Volver a:DBC`](dbc-index.md)

**Achievement.dbc**

La tabla DBC contiene todos los logros disponibles dentro del juego.

 **Versión: 3.3.5a**

## Estructura

|Columna |  Campo               | Tipo         | Notas                                                                                                                                                                                                                                                  |
| ------ | -------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1      | ID                   | Integer      | Identificador (ID) del logro.                                                                                                                                                                                                                          |
| 2      | Faction              | Integer      | Valor -1 para ambas facciones. Valor 0 para la Horda y 1 para la Alianza.                                                                                                                                                                              |
| 3      | Map                  | Integer      | Establecerse siempre y cuando el logro esté relacionado con una zona en específico, de lo contrario se asigna el valor -1.                                                                                                                             |
| 4      | Previous             | Integer      | En caso de que el logro pertenezca a una serie de otros logros, este campo vendría a ser inmediatamente la ID del anterior. En caso contrario se asigna el valor 0.                                                                                    |
| 5-20   | Name                 | String + Loc |                                                                                                                                                                                                                                                        |
| 21     | ?                    |              | Aparentemente suele ser siempre el valor hexadecimal 0xFF01FE                                                                                                                                                                                          |
| 22-37  | Description          | String + Loc | Si la descripción de este campo se encuentra vacía, no es un logro sino parte de las Estadísticas del Jugador.                                                                                                                                         |
| 38     | ?                    |              | Aparentemente suele ser siempre el valor 16712190, en raras ocasiones 16712188 (¿Instancias quizá?)                                                                                                                                                    |
| 39     | Category             | Integer      | ID de la categoría del logro.                                                                                                                                                                                                                          |
| 40     | Points               | Integer      | 0,5,10,15,20,25,30,50 (Puntos por completar el logro)                                                                                                                                                                                                  |
| 41     | OrderInGroup         | Integer      | Valor mínimo: 1.                                                                                                                                                                                                                                       |
| 42     | Flags                | Integer      | Comunmente desde el 0 hasta 768, si el valor es 256 quiere decir que sólo una persona por reino puede obtener el logro, y en caso de que sea 768 sólo es obtenible para una banda (Raid) por reino. ¿Quizá una segunda categoría?                      |
| 43     | SpellIcon            | Integer      | Ícono a mostrarse.                                                                                                                                                                                                                                     |
| 44-59  | Reward               | String+ Loc  |                                                                                                                                                                                                                                                        |
| 47     | Bonus                |              | Texto adicional acerca de la recompensa al recibir el logro.                                                                                                                                                                                           |
| 60     | ?                    |              | ¿Número flotante?                                                                                                                                                                                                                                      |
| 61     | Demands              | Integer      | Número de cosas que debes de obtener/cumplir para obtener este logro. Por ejemplo, si debes de conseguir 25 tabardos, hay un número 25 en este campo. TrinityCore: "Necesita un número de Criterios de Logros Completados (propios o referenciados)"   |
| 62     | ReferencedAchievemnt | Integer      | TrinityCore: "Logro referenciado (número de todos los Criterios de Logros completados)"                                                                                                                                                                |

## Contenido

| ID   | Nombre                                                                         |
|------|--------------------------------------------------------------------------------|
| 6    | Nivel 10                                                                       |
| 7    | Nivel 20                                                                       |
| 8    | Nivel 30                                                                       |
| 9    | Nivel 40                                                                       |
| 10   | Nivel 50                                                                       |
| 11   | Nivel 60                                                                       |
| 12   | Nivel 70                                                                       |
| 13   | Nivel 80                                                                       |
| 15   | Muchas mascotas                                                                |
| 16   | ¿Alguien ha pedido un bocadillo de nudillos?                                   |
| 31   | Una re-misión sencilla                                                         |
| 32   | 2000 misiones completadas                                                      |
| 33   | La Tundra no tiene nada de aburrida                                            |
| 34   | He paseado por el Fiordo                                                       |
| 35   | El poder del Cementerio de Dragones                                            |
| 36   | El imperio de Zul\'Drak                                                        |
| 37   | Mi furia por las pardas                                                        |
| 38   | La cima de Las Cumbres Tormentosas                                             |
| 39   | Dentro de la Cuenca                                                            |
| 40   | Corona de Hielo: la meta final                                                 |
| 41   | Maestro cultural de Rasganorte                                                 |
| 42   | Explora los Reinos del Este                                                    |
| 43   | Explora Kalimdor                                                               |
| 44   | Explora Terrallende                                                            |
| 45   | Explora Rasganorte                                                             |
| 46   | Explorador del mundo                                                           |
| 49   | Victorias en el Valle de Alterac                                               |
| 50   | Victorias en el Ojo de la Tormenta                                             |
| 51   | Victorias en la Cuenca de Arathi                                               |
| 52   | Batallas en la Garganta Grito de Guerra                                        |
| 53   | Batallas en el Valle de Alterac                                                |
| 54   | Batallas en el Ojo de la Tormenta                                              |
| 55   | Batallas en la Cuenca de Arathi                                                |
| 56   | Muertes en la Garganta Grito de Guerra                                         |
| 57   | Muertes en el Valle de Alterac                                                 |
| 58   | Muertes contra Drek\'Thar                                                      |
| 59   | Muertes en la Cuenca de Arathi                                                 |
| 60   | Muertes propias                                                                |
| 73   | Deshonrar la Cuenca                                                            |
| 94   | Misiones abandonadas                                                           |
| 95   | Cantidad media de misiones completadas cada día                                |
| 97   | Misiones diarias completadas                                                   |
| 98   | Misiones completadas                                                           |
| 99   | Encuentros en las Ruinas de Lordaeron                                          |
| 100  | Victorias en El Círculo de los Retos                                           |
| 101  | Encuentros en El Círculo de los Retos                                          |
| 102  | Victorias en las Ruinas de Lordaeron                                           |
| 103  | Encuentros en el Anillo de Sangre                                              |
| 104  | Victorias en el Anillo de Sangre                                               |
| 105  | Victorias en la Garganta Grito de Guerra                                       |
| 107  | Criaturas muertas                                                              |
| 108  | Alimañas muertas                                                               |
| 110  | Lich King: Jefe asesinado más veces (5 j.)                                     |
| 112  | Muertes por ahogamiento                                                        |
| 113  | Muertes por fatiga                                                             |
| 114  | Muertes por caída                                                              |
| 115  | Muertes por fuego y lava                                                       |
| 116  | Oficial profesional                                                            |
| 121  | Oficial cocinero                                                               |
| 122  | Cocinero experto                                                               |
| 123  | Cocinero artesano                                                              |
| 124  | Maestro cocinero                                                               |
| 125  | Gran maestro cocinero                                                          |
| 126  | Oficial pescador                                                               |
| 127  | Pescador experto                                                               |
| 128  | Pescador artesano                                                              |
| 129  | Maestro pescador                                                               |
| 130  | Gran maestro pescador                                                          |
| 131  | Oficial en primeros auxilios                                                   |
| 132  | Experto en primeros auxilios                                                   |
| 133  | Artesano en primeros auxilios                                                  |
| 134  | Maestro en primeros auxilios                                                   |
| 135  | Gran maestro en primeros auxilios                                              |
| 137  | Abastecerse                                                                    |
| 141  | Elección final                                                                 |
| 144  | El Rondador de arriba                                                          |
| 150  | El diplomático pescador                                                        |
| 153  | El viejo gnomo y el mar                                                        |
| 154  | Victoria en la Cuenca de Arathi                                                |
| 155  | Veterano de la Cuenca de Arathi                                                |
| 156  | Dominio territorial                                                            |
| 157  | ¡Al rescate!                                                                   |
| 158  | El Capitán y yo lo conseguimos                                                 |
| 159  | Hagámoslo                                                                      |
| 161  | Victoria elástica                                                              |
| 162  | La victoria estaba clara *ejem*                                                |
| 165  | Perfección en la Cuenca de Arathi                                              |
| 166  | Victoria en la Garganta Grito de Guerra                                        |
| 167  | Veterano de la Garganta Grito de Guerra                                        |
| 168  | Perfección en la Garganta Grito de Guerra                                      |
| 178  | Fórmulas de encantamiento conocidas                                            |
| 181  | Objetos desencantados                                                          |
| 183  | Materiales producidos al desencantar                                           |
| 189  | Mayor sanación realizada                                                       |
| 193  | Mayor golpe asestado                                                           |
| 197  | Daño total infligido                                                           |
| 198  | Sanación total realizada                                                       |
| 199  | Captura la bandera                                                             |
| 200  | Defensor persistente                                                           |
| 201  | Conveniencia Grito de Guerra                                                   |
| 202  | Captura rápida                                                                 |
| 203  | En mi casa no                                                                  |
| 204  | Hombre de hierro                                                               |
| 206  | Defensor supremo                                                               |
| 207  | Eres mi héroe                                                                  |
| 208  | Victoria en el Ojo de la Tormenta                                              |
| 209  | Veterano del Ojo de la Tormenta                                                |
| 211  | Gloria de la tormenta                                                          |
| 212  | Rematar la tormenta                                                            |
| 213  | Soldado de asalto                                                              |
| 214  | Aluvión                                                                        |
| 216  | Destinado a la gloria                                                          |
| 218  | Victoria en el Valle de Alterac                                                |
| 219  | Veterano del Valle de Alterac                                                  |
| 220  | Perfección Pico Tormenta                                                       |
| 221  | Ladrón de tumbas de Alterac                                                    |
| 222  | Defensa de torres                                                              |
| 223  | La gacela enfermiza                                                            |
| 224  | Leal defensor                                                                  |
| 225  | Todo cuenta                                                                    |
| 226  | El rayo de Alterac                                                             |
| 227  | Control de daños                                                               |
| 229  | La parca                                                                       |
| 230  | Maestro de batalla                                                             |
| 231  | Bola de demolición                                                             |
| 233  | Rabioso sediento de sangre                                                     |
| 238  | Una muerte con honor                                                           |
| 239  | 25000 muertes con honor                                                        |
| 245  | Hace falta clase                                                               |
| 246  | Conoce a tu enemigo                                                            |
| 247  | Haz el amor, no Warcraft                                                       |
| 248  | El traje de domingo                                                            |
| 249  | Vestido para la ocasión                                                        |
| 252  | Con un poco de ayuda de mis amigos                                             |
| 255  | Tráeme la cabeza de... esto, vaya                                              |
| 259  | Avaricioso                                                                     |
| 260  | Encantador                                                                     |
| 263  | Hiela al Señor de la Escarcha                                                  |
| 271  | Baile ardiente en el poste caliente                                            |
| 272  | Malabarista                                                                    |
| 273  | ¡Vamos, Metzen!                                                                |
| 275  | Niñera veterana                                                                |
| 277  | Es la temporada                                                                |
| 279  | Simplemente abominable                                                         |
| 281  | Habilidad en primeros auxilios                                                 |
| 283  | La Mascarada                                                                   |
| 284  | Una máscara para todas las ocasiones                                           |
| 288  | Sácalo                                                                         |
| 289  | El salvador de Halloween                                                       |
| 291  | Búscate la cabeza                                                              |
| 292  | Llamada siniestra                                                              |
| 293  | Perturbar la paz                                                               |
| 295  | Fiesta de la Cerveza Temible                                                   |
| 303  | Viajará gracias al barril                                                      |
| 306  | Maestro pescador de Azeroth                                                    |
| 318  | Veces que te ha matado la facción contraria                                    |
| 319  | Duelos ganados                                                                 |
| 320  | Duelos perdidos                                                                |
| 321  | Muertes en mazmorra y banda                                                    |
| 322  | Lich King: Muertes contra jefes (5 j.)                                         |
| 323  | Lich King: Muertes contra jefes (10 j.)                                        |
| 324  | Lich King: Muertes contra jefes (25 j.)                                        |
| 326  | Oro obtenido como recompensa de misiones                                       |
| 328  | Oro total adquirido                                                            |
| 329  | Cantidad de subastas creadas                                                   |
| 330  | Compras realizadas en la casa de subastas                                      |
| 331  | La puja más alta realizada en una subasta                                      |
| 332  | Venta más cara realizada en una subasta                                        |
| 333  | Cantidad de oro despojado                                                      |
| 334  | Mayor cantidad de oro jamás poseída                                            |
| 336  | Objetos legendarios adquiridos                                                 |
| 338  | Mascotas de vanidad poseídas                                                   |
| 339  | Monturas poseídas                                                              |
| 341  | Objetos épicos despojados                                                      |
| 342  | Objetos épicos adquiridos                                                      |
| 344  | Vendas usadas                                                                  |
| 345  | Pociones de salud consumidas                                                   |
| 346  | Bebidas consumidas                                                             |
| 347  | Comida consumida                                                               |
| 349  | Rutas de vuelo tomadas                                                         |
| 350  | Portales de mago atravesados                                                   |
| 353  | Veces que has usado la piedra de hogar                                         |
| 362  | Victorias 5c5                                                                  |
| 363  | Encuentros 5c5                                                                 |
| 364  | Victorias 3c3                                                                  |
| 365  | Encuentros 3c3                                                                 |
| 366  | Victorias 2c2                                                                  |
| 367  | Encuentros 2c2                                                                 |
| 370  | Mayor índice personal en grupos de 2 personas                                  |
| 374  | Mayor índice de equipo en grupos de 2 personas                                 |
| 377  | Mayoría de facciones a nivel Exaltado                                          |
| 378  | Mayoría de facciones en Venerado o superior                                    |
| 381  | Muertes con honor en el mundo                                                  |
| 382  | Muertes con honor en campos de batalla                                         |
| 383  | Muertes con honor en la arena                                                  |
| 388  | Defensor de la ciudad                                                          |
| 389  | Maestro de la Arena Gurubashi                                                  |
| 393  | Torres defendidas en el Valle de Alterac                                       |
| 394  | Torres capturadas en el Valle de Alterac                                       |
| 395  | Banderas capturadas en la Garganta Grito de Guerra                             |
| 396  | Gran Maestro de la Arena Gurubashi                                             |
| 397  | Entra en la arena                                                              |
| 398  | Despiadadamente entregado                                                      |
| 399  | Entre tú y yo: 1550                                                            |
| 400  | Entre tú y yo: 1750                                                            |
| 401  | Entre tú y yo: 2000                                                            |
| 402  | Tres son multitud: 1550                                                        |
| 403  | Tres son multitud: 1750                                                        |
| 404  | Choca esos cinco: 2000                                                         |
| 405  | Tres son multitud: 2000                                                        |
| 406  | Choca esos cinco: 1550                                                         |
| 407  | Choca esos cinco: 1750                                                         |
| 408  | Una buena racha                                                                |
| 409  | El último hombre en pie                                                        |
| 411  | Murky                                                                          |
| 412  | Traje de múrloc                                                                |
| 414  | Empuñadura de Tyrael                                                           |
| 415  | Gran oso de Blizzard                                                           |
| 416  | Señor Escarabajo                                                               |
| 418  | Gladiador despiadado                                                           |
| 419  | Gladiador vengativo                                                            |
| 420  | Gladiador brutal                                                               |
| 424  | ¿Por qué? Porque es rojo                                                       |
| 425  | Atiesh, gran báculo del Guardián                                               |
| 426  | Gujas de guerra de Azzinoth                                                    |
| 428  | Trueno furioso, espada bendita del Hijo del Viento                             |
| 429  | Sulfuras, Mano de Ragnaros                                                     |
| 430  | Oso de guerra Amani                                                            |
| 431  | Mano de A\'dal                                                                 |
| 432  | Campeón de los naaru                                                           |
| 433  | Gran mariscal                                                                  |
| 434  | Mariscal de campo                                                              |
| 435  | Comandante                                                                     |
| 436  | Teniente coronel                                                               |
| 437  | Campeón caballero                                                              |
| 438  | Capitán caballero                                                              |
| 439  | Caballero                                                                      |
| 440  | Alférez                                                                        |
| 441  | Sargento primero                                                               |
| 442  | Soldado                                                                        |
| 443  | Gran Señor de la Guerra                                                        |
| 444  | General                                                                        |
| 445  | Señor de la Guerra                                                             |
| 446  | Gran general                                                                   |
| 447  | Campeón                                                                        |
| 448  | Centurión                                                                      |
| 449  | Guardia de sangre                                                              |
| 450  | Capataz primero                                                                |
| 451  | Guardia de piedra                                                              |
| 452  | Gran capataz                                                                   |
| 453  | Capataz                                                                        |
| 454  | Rastreador                                                                     |
| 456  | ¡Primero del reino! Destripador obsidiana                                      |
| 457  | ¡Primero del reino con Nivel 80!                                               |
| 458  | ¡Primero del reino! Pícaro nivel 80                                            |
| 459  | ¡Primero del reino! Guerrero nivel 80                                          |
| 460  | ¡Primero del reino! Mago nivel 80                                              |
| 461  | ¡Primero del reino! Caballero de la Muerte nivel 80                            |
| 462  | ¡Primero del reino! Cazador nivel 80                                           |
| 463  | ¡Primero del reino! Brujo nivel 80                                             |
| 464  | ¡Primero del reino! Sacerdote nivel 80                                         |
| 465  | ¡Primero del reino! Paladín nivel 80                                           |
| 466  | ¡Primero del reino! Druida nivel 80                                            |
| 467  | ¡Primero del reino! Chamán nivel 80                                            |
| 468  | Bruto                                                                          |
| 469  | Legionario                                                                     |
| 470  | Cabo                                                                           |
| 471  | Sargento                                                                       |
| 472  | Teniente caballero                                                             |
| 473  | Mariscal                                                                       |
| 477  | Fortaleza de Utgarde                                                           |
| 478  | El Nexo                                                                        |
| 479  | La Matanza de Stratholme                                                       |
| 480  | Azjol-Nerub                                                                    |
| 481  | Ahn’kahet: El Antiguo Reino                                                    |
| 482  | Fortaleza de Drak\'Tharon                                                      |
| 483  | El Bastión Violeta                                                             |
| 484  | Gundrak                                                                        |
| 485  | Cámaras de Piedra                                                              |
| 486  | Cámaras de Relámpagos                                                          |
| 487  | El Oculus                                                                      |
| 488  | Pináculo de Utgarde                                                            |
| 489  | Heroico: Fortaleza de Utgarde                                                  |
| 490  | Heroico: El Nexo                                                               |
| 491  | Heroico: Azjol-Nerub                                                           |
| 492  | Heroico: Ahn\'kahet: El Antiguo Reino                                          |
| 493  | Heroico: La Fortaleza de Drak\'Tharon                                          |
| 494  | Heroico: El Bastión Violeta                                                    |
| 495  | Heroico: Gundrak                                                               |
| 496  | Heroico: Cámaras de Piedra                                                     |
| 497  | Heroico: Cámaras de Relámpagos                                                 |
| 498  | Heroico: El Oculus                                                             |
| 499  | Heroico: El Pináculo de Utgarde                                                |
| 500  | Heroico: La Matanza de Stratholme                                              |
| 503  | 50 misiones completadas                                                        |
| 504  | 100 misiones completadas                                                       |
| 505  | 250 misiones completadas                                                       |
| 506  | 500 misiones completadas                                                       |
| 507  | 1000 misiones completadas                                                      |
| 508  | 1500 misiones completadas                                                      |
| 509  | 10000 muertes con honor                                                        |
| 512  | 5000 muertes con honor                                                         |
| 513  | 100 muertes con honor                                                          |
| 515  | 500 muertes con honor                                                          |
| 516  | 1000 muertes con honor                                                         |
| 518  | 30 reputaciones Exaltado                                                       |
| 519  | 25 reputaciones Exaltado                                                       |
| 520  | 20 reputaciones Exaltado                                                       |
| 521  | 15 reputaciones Exaltado                                                       |
| 522  | A alguien le gusto                                                             |
| 523  | 5 reputaciones Exaltado                                                        |
| 524  | 10 reputaciones Exaltado                                                       |
| 527  | Mayor golpe recibido                                                           |
| 528  | Daño total recibido                                                            |
| 529  | Mayoría de facciones en Honorable o superior                                   |
| 545  | Cortar y peinar                                                                |
| 546  | Depósito seguro                                                                |
| 547  | Veterano de la Puerta de Cólera                                                |
| 556  | Épico                                                                          |
| 557  | Superior                                                                       |
| 558  | Avaricioso                                                                     |
| 559  | Necesitado                                                                     |
| 560  | La presa más mortífera                                                         |
| 561  | El quebradero de cabeza de D.E.H.T.A                                           |
| 562  | El Arrabal Arácnido (10 j.)                                                    |
| 563  | El Arrabal Arácnido (25 j.)                                                    |
| 564  | El Arrabal de los Ensamblajes (10 j.)                                          |
| 565  | El Arrabal de los Ensamblajes (25 j.)                                          |
| 566  | El Arrabal de la Peste (10 j.)                                                 |
| 567  | El Arrabal de la Peste (25 j.)                                                 |
| 568  | El Arrabal Militar (10 j.)                                                     |
| 569  | El Arrabal Militar (25 j.)                                                     |
| 572  | La muerte de Sapphiron (10 j.)                                                 |
| 573  | La muerte de Sapphiron (25 j.)                                                 |
| 574  | La derrota de Kel\'Thuzad (10 j.)                                              |
| 575  | La derrota de Kel\'Thuzad (25 j.)                                              |
| 576  | La caída de Naxxramas (10 j.)                                                  |
| 577  | La caída de Naxxramas (25 j.)                                                  |
| 578  | Los valientes (10 j.)                                                          |
| 579  | Los valientes (25 j.)                                                          |
| 582  | Estrella del Valle de Alterac                                                  |
| 583  | Estrella de la Cuenca de Arathi                                                |
| 584  | Asesino de la Cuenca de Arathi                                                 |
| 585  | Banderas del Ojo de la Tormenta capturadas                                     |
| 586  | Banderas devueltas en la Garganta Grito de Guerra                              |
| 587  | Asesino tormentoso                                                             |
| 588  | Muertes con honor                                                              |
| 589  | Mayor índice de equipo en grupos de 5 personas                                 |
| 590  | Mayor índice de equipo en grupos de 3 personas                                 |
| 593  | Muertes contra Vanndar Pico Tormenta                                           |
| 594  | Muertes contra Hogger                                                          |
| 595  | Mayor índice personal en grupos de 3 personas                                  |
| 596  | Mayor índice personal en grupos de 5 personas                                  |
| 603  | Cólera de la Horda                                                             |
| 604  | Cólera de la Alianza                                                           |
| 605  | Una moneda de linaje                                                           |
| 606  | 5 monedas de linaje                                                            |
| 607  | 10 monedas de linaje                                                           |
| 608  | 25 monedas de linaje                                                           |
| 609  | 50 monedas de linaje                                                           |
| 610  | ¡Muerte al Jefe de Guerra!                                                     |
| 611  | Pezuña de Sangre sangrante                                                     |
| 612  | Abajo con la Dama Oscura                                                       |
| 613  | Asesinado en Quel\'Thalas                                                      |
| 614  | ¡Por la Alianza!                                                               |
| 615  | Asaltar Ventormenta                                                            |
| 616  | ¡Muerte al Rey!                                                                |
| 617  | Ya no es inmortal                                                              |
| 618  | Apagar la luz                                                                  |
| 619  | ¡Por la Horda!                                                                 |
| 621  | Representa                                                                     |
| 622  | La caída del Tejehechizos (10 j.)                                              |
| 623  | La caída del Tejehechizos (25 j.)                                              |
| 624  | Menos es más (10 j.)                                                           |
| 625  | Vencer al Vuelo Negro (25 j.)                                                  |
| 626  | Las mejores para el Festival Lunar                                             |
| 627  | Dun Morogh                                                                     |
| 628  | Minas de la Muerte                                                             |
| 629  | Sima Ígnea                                                                     |
| 630  | Cuevas de los Lamentos                                                         |
| 631  | Castillo de Colmillo Oscuro                                                    |
| 632  | Cavernas de Brazanegra                                                         |
| 633  | Mazmorras de Ventormenta                                                       |
| 634  | Gnomeregan                                                                     |
| 635  | Horado Rajacieno                                                               |
| 636  | Zahúrda Rajacieno                                                              |
| 637  | Monasterio Escarlata                                                           |
| 638  | Uldaman                                                                        |
| 639  | Zul\'Farrak                                                                    |
| 640  | Maraudon                                                                       |
| 641  | Templo Sumergido                                                               |
| 642  | Profundidades de Roca Negra                                                    |
| 643  | Cumbre de Roca Negra inferior                                                  |
| 644  | Rey de La Masacre                                                              |
| 645  | Scholomance                                                                    |
| 646  | Stratholme                                                                     |
| 647  | Murallas del Fuego Infernal                                                    |
| 648  | El Horno de Sangre                                                             |
| 649  | Recinto de los Esclavos                                                        |
| 650  | La Sotiénaga                                                                   |
| 651  | Tumbas de Maná                                                                 |
| 652  | La Fuga de Durnholde                                                           |
| 653  | Salas Sethekk                                                                  |
| 654  | Laberinto de las Sombras                                                       |
| 655  | Apertura de El Portal Oscuro                                                   |
| 656  | La Cámara de Vapor                                                             |
| 657  | Las Salas Arrasadas                                                            |
| 658  | El Mechanar                                                                    |
| 659  | El Invernáculo                                                                 |
| 660  | El Arcatraz                                                                    |
| 661  | Bancal del Magister                                                            |
| 662  | Edición de coleccionista: Mini Diablo                                          |
| 663  | Edición de coleccionista: Panda                                                |
| 664  | Edición de coleccionista: Zergling                                             |
| 665  | Edición de coleccionista: Cría abisal                                          |
| 666  | Criptas Auchenai                                                               |
| 667  | Heroico: Murallas del Fuego Infernal                                           |
| 668  | Heroico: El Horno de Sangre                                                    |
| 669  | Heroico: El Recinto de los Esclavos                                            |
| 670  | Heroico: La Sotiénaga                                                          |
| 671  | Heroico: Tumbas de Maná                                                        |
| 672  | Heroico: Criptas Auchenai                                                      |
| 673  | Heroico: La Fuga de Durnholde                                                  |
| 674  | Heroico: Salas Sethekk                                                         |
| 675  | Heroico: Laberinto de las Sombras                                              |
| 676  | Heroico: Apertura de El Portal Oscuro                                          |
| 677  | Heroico: La Cámara de Vapor                                                    |
| 678  | Heroico: Las Salas Arrasadas                                                   |
| 679  | Heroico: El Mechanar                                                           |
| 680  | Heroico: El Invernáculo                                                        |
| 681  | Heroico: El Arcatraz                                                           |
| 682  | Heroico: Bancal del Magister                                                   |
| 683  | Edición de coleccionista: Cría de vermis de escarcha                           |
| 684  | Guarida de Onyxia (Nivel 60)                                                   |
| 685  | Guarida de Alanegra                                                            |
| 686  | Núcleo de Magma                                                                |
| 687  | Templo de Ahn\'Qiraj                                                           |
| 688  | Zul\'Gurub                                                                     |
| 689  | Ruinas de Ahn\'Qiraj                                                           |
| 690  | Karazhan                                                                       |
| 691  | Zul\'Aman                                                                      |
| 692  | Guarida de Gruul                                                               |
| 693  | Guarida de Magtheridon                                                         |
| 694  | Caverna Santuario Serpiente                                                    |
| 695  | La Batalla del Monte Hyjal                                                     |
| 696  | El Castillo de la Tempestad                                                    |
| 697  | El Templo Oscuro                                                               |
| 698  | Meseta de La Fuente del Sol                                                    |
| 699  | Ganador mundial                                                                |
| 700  | Libertad de la Horda                                                           |
| 701  | Libertad de la Alianza                                                         |
| 705  | Maestro armero                                                                 |
| 706  | Aullador Lobo Gélido                                                           |
| 707  | Carnero de batalla Pico Tormenta                                               |
| 708  | Héroe del clan Lobo Gélido                                                     |
| 709  | Héroe de la Guardia Pico Tormenta                                              |
| 710  | El Rapiñador                                                                   |
| 711  | Caballero de Arathor                                                           |
| 712  | Escolta Grito de Guerra                                                        |
| 713  | Centinela Ala de Plata                                                         |
| 714  | El conquistador                                                                |
| 725  | Thori\'dal, la furia de las estrellas                                          |
| 726  | Caja de cigalas mágicas de Tenacitas                                           |
| 727  | A mí la caballería                                                             |
| 728  | Durotar                                                                        |
| 729  | Riendas de destrero de la muerte                                               |
| 730  | Habilidades que pagan las facturas                                             |
| 731  | Experto profesional                                                            |
| 732  | Artesano profesional                                                           |
| 733  | Maestro profesional                                                            |
| 734  | Gran maestro profesional                                                       |
| 735  | Trabajar día y noche                                                           |
| 736  | Mulgore                                                                        |
| 750  | Los Baldíos                                                                    |
| 752  | Muertes en Naxxramas                                                           |
| 753  | Cantidad media de oro obtenida cada día                                        |
| 759  | Cantidad media de misiones diarias completadas cada día                        |
| 760  | Montañas de Alterac                                                            |
| 761  | Tierras Altas de Arathi                                                        |
| 762  | Embajador de la Horda                                                          |
| 763  | El cruzado ardiente                                                            |
| 764  | El cruzado ardiente                                                            |
| 765  | Tierras Inhóspitas                                                             |
| 766  | Las Tierras Devastadas                                                         |
| 768  | Claros de Tirisfal                                                             |
| 769  | Bosque de Argénteos                                                            |
| 770  | Tierras de la Peste del Oeste                                                  |
| 771  | Tierras de la Peste del Este                                                   |
| 772  | Laderas de Trabalomas                                                          |
| 773  | Las Tierras del Interior                                                       |
| 774  | La Garganta de Fuego                                                           |
| 775  | Las Estepas Ardientes                                                          |
| 776  | Bosque de Elwynn                                                               |
| 777  | Paso de la Muerte                                                              |
| 778  | Bosque del Ocaso                                                               |
| 779  | Loch Modan                                                                     |
| 780  | Montañas Crestagrana                                                           |
| 781  | Vega de Tuercespina                                                            |
| 782  | Pantano de las Penas                                                           |
| 783  | La tormenta perfecta                                                           |
| 784  | Dominio en el Ojo de la Tormenta                                               |
| 796  | Resucitado por sacerdotes                                                      |
| 798  | Renacer por druidas                                                            |
| 799  | Espíritu devuelto al cuerpo por chamanes                                       |
| 800  | Redimido por paladines                                                         |
| 801  | Resucitado con piedras de alma                                                 |
| 802  | Páramos de Poniente                                                            |
| 811  | Frascos consumidos                                                             |
| 812  | Piedras de salud usadas                                                        |
| 829  | Mayor sanación recibida                                                        |
| 830  | Sanación total recibida                                                        |
| 837  | Arenas ganadas                                                                 |
| 838  | Arenas jugadas                                                                 |
| 839  | Campos de batalla jugados                                                      |
| 840  | Campos de batalla ganados                                                      |
| 841  | Los Humedales                                                                  |
| 842  | Teldrassil                                                                     |
| 843  | Tormenta Abisal                                                                |
| 844  | Costa Oscura                                                                   |
| 845  | Vallefresno                                                                    |
| 846  | Las Mil Agujas                                                                 |
| 847  | Sierra Espolón                                                                 |
| 848  | Desolace                                                                       |
| 849  | Feralas                                                                        |
| 850  | Marjal Revolcafango                                                            |
| 851  | Desierto de Tanaris                                                            |
| 852  | Azshara                                                                        |
| 853  | Frondavil                                                                      |
| 854  | Cráter de Un\'Goro                                                             |
| 855  | Claro de la Luna                                                               |
| 856  | Silithus                                                                       |
| 857  | Cuna del Invierno                                                              |
| 858  | Tierras Fantasma                                                               |
| 859  | Bosque Canción Eterna                                                          |
| 860  | Isla Bruma Azur                                                                |
| 861  | Isla Bruma de Sangre                                                           |
| 862  | Península del Fuego Infernal                                                   |
| 863  | Marisma de Zangar                                                              |
| 864  | Valle Sombraluna                                                               |
| 865  | Montañas Filospada                                                             |
| 866  | Nagrand                                                                        |
| 867  | Bosque de Terokkar                                                             |
| 868  | Isla de Quel\'Danas                                                            |
| 869  | 50000 muertes con honor                                                        |
| 870  | 100000 muertes con honor                                                       |
| 871  | ¡Adelante, Almirante!                                                          |
| 872  | Defensor frenético                                                             |
| 873  | Perfección Lobo Gélido                                                         |
| 875  | Vengativamente entregado                                                       |
| 876  | Brutalmente entregado                                                          |
| 877  | La tarta es de verdad                                                          |
| 878  | Este no se escapó                                                              |
| 879  | Montura a la antigua usanza                                                    |
| 880  | Tigre Zulian presto                                                            |
| 881  | Raptor Razzashi presto                                                         |
| 882  | Riendas de caballo de guerra ígneo                                             |
| 883  | Riendas del Lord Cuervo                                                        |
| 884  | Halcón zancudo blanco presto                                                   |
| 885  | Cenizas de Al\'ar                                                              |
| 886  | Draco abisal presto                                                            |
| 887  | Draco abisal despiadado                                                        |
| 888  | Draco abisal vengativo                                                         |
| 889  | A todo gas                                                                     |
| 890  | Hacia la azul y salvaje lejanía                                                |
| 891  | ¡Arre!                                                                         |
| 892  | Elegido para la gloria                                                         |
| 893  | Hipogrifo de guerra Cenarion                                                   |
| 894  | Sobrevolando Skettis                                                           |
| 896  | Una misión al día llena a los ogros de alegría                                 |
| 897  | Resultas muy ofensivo                                                          |
| 898  | Sobre alas abisales                                                            |
| 899  | Qué guay, Kurenai                                                              |
| 900  | El zar de Esporaggar                                                           |
| 901  | Mag\'har de Draenor                                                            |
| 902  | Oficial jefe Exaltado                                                          |
| 903  | Shattrath dividida                                                             |
| 905  | Superar al Viejo Barlo                                                         |
| 906  | ¡Dale caña!                                                                    |
| 907  | El justicar                                                                    |
| 908  | ¡Llamamiento a las armas!                                                      |
| 909  | ¡Llamamiento a las armas!                                                      |
| 910  | Ancestros de las mazmorras                                                     |
| 911  | Ancestros de Kalimdor                                                          |
| 912  | Ancestros de los Reinos del Este                                               |
| 913  | Honrar a los ancestros personales                                              |
| 914  | Ancestros de la Horda                                                          |
| 915  | Ancestros de la Alianza                                                        |
| 916  | Muertes totales en banda (25 j.)                                               |
| 917  | Muertes totales en banda (10 j.)                                               |
| 918  | Muertes totales en mazmorras (5 j.)                                            |
| 919  | Oro total ganado en subastas                                                   |
| 921  | Cantidad de oro recibido de vendedores                                         |
| 922  | Pociones de maná consumidas                                                    |
| 923  | Elixires consumidos                                                            |
| 924  | Mayoría de facciones de Rasganorte a nivel Exaltado                            |
| 925  | Mayoría de facciones de Terrallende a nivel Exaltado                           |
| 926  | Mayoría de facciones de la Horda a nivel Exaltado                              |
| 927  | Objetos épicos equipados en ranuras                                            |
| 928  | Ranuras adicionales compradas en el banco                                      |
| 931  | Cantidad total de facciones encontradas                                        |
| 932  | Veces totales en mazmorras (5 j.)                                              |
| 933  | Veces totales en bandas (10 j.)                                                |
| 934  | Veces totales en bandas (25 j.)                                                |
| 937  | La bendición de Elune                                                          |
| 938  | Las nieves de Rasganorte                                                       |
| 939  | Montes como elekk blancos                                                      |
| 940  | Las verdes colinas de Tuercespina                                              |
| 941  | Hemet Nesingwary: las misiones recopiladas                                     |
| 942  | El diplomático                                                                 |
| 943  | El diplomático                                                                 |
| 944  | En ese túnel me adoran                                                         |
| 945  | El Campeón Argenta                                                             |
| 946  | El Alba Argenta                                                                |
| 947  | La Cruzada Argenta                                                             |
| 948  | Embajador de la Alianza                                                        |
| 949  | Colmillarrmagedón                                                              |
| 950  | Tribu Corazón Frenético                                                        |
| 951  | Los Oráculos                                                                   |
| 952  | Mercenario de Sholazar                                                         |
| 953  | Guardián de Cenarius                                                           |
| 955  | Srs. del Agua de Hydraxis                                                      |
| 956  | Linaje de Nozdormu                                                             |
| 957  | Héroe de la tribu Zandalar                                                     |
| 958  | Pleitesía para los Juramorte                                                   |
| 959  | La Escama de las Arenas                                                        |
| 960  | El Ojo Violeta                                                                 |
| 961  | Corazón Frenético honorario                                                    |
| 962  | Salvador de los Oráculos                                                       |
| 963  | Truco o trato en Kalimdor                                                      |
| 964  | ¿Bajas?                                                                        |
| 965  | Truco o trato en Kalimdor                                                      |
| 966  | Truco o trato en los Reinos del Este                                           |
| 967  | Truco o trato en los Reinos del Este                                           |
| 968  | Truco o trato en Terrallende                                                   |
| 969  | Truco o trato en Terrallende                                                   |
| 970  | Truco o trato en Azeroth                                                       |
| 971  | Truco o trato en Azeroth                                                       |
| 972  | ¡Truco o trato!                                                                |
| 973  | 5 misiones diarias completadas                                                 |
| 974  | 50 misiones diarias completadas                                                |
| 975  | 200 misiones diarias completadas                                               |
| 976  | 500 misiones diarias completadas                                               |
| 977  | 1000 misiones diarias completadas                                              |
| 978  | 3000 misiones completadas                                                      |
| 979  | La tarea de la máscara                                                         |
| 980  | Riendas de Jinete decapitado                                                   |
| 981  | Esa deslumbrante sonrisa                                                       |
| 1005 | Conoce a tu enemigo                                                            |
| 1006 | Defensor de la ciudad                                                          |
| 1007 | El Acuerdo del Reposo del Dragón                                               |
| 1008 | El Kirin Tor                                                                   |
| 1009 | Caballeros de la Espada de Ébano                                               |
| 1010 | Vanguardia de Rasganorte                                                       |
| 1011 | Los vientos del Norte                                                          |
| 1012 | Los vientos del Norte                                                          |
| 1014 | 35 reputaciones Exaltado                                                       |
| 1015 | 40 reputaciones Exaltado                                                       |
| 1017 | ¿Puedo quedármela?                                                             |
| 1020 | Diez tabardos                                                                  |
| 1021 | Todo sobre los tabardos                                                        |
| 1022 | Celador de las llamas de los Reinos del Este                                   |
| 1023 | Celador de las llamas de Kalimdor                                              |
| 1024 | Celador de las llamas de Terrallende                                           |
| 1025 | Vigilante de las llamas de los Reinos del Este                                 |
| 1026 | Vigilante de las llamas de Kalimdor                                            |
| 1027 | Vigilante de las llamas de Terrallende                                         |
| 1028 | Apagar los Reinos del Este                                                     |
| 1029 | Apagar Kalimdor                                                                |
| 1030 | Apagar Terrallende                                                             |
| 1031 | Apagar los Reinos del Este                                                     |
| 1032 | Apagar Kalimdor                                                                |
| 1033 | Apagar Terrallende                                                             |
| 1034 | Los fuegos de Azeroth                                                          |
| 1035 | Profanación de la Horda                                                        |
| 1036 | Los fuegos de Azeroth                                                          |
| 1037 | Profanación de la Alianza                                                      |
| 1038 | El celador de las llamas                                                       |
| 1039 | El vigilante de las llamas                                                     |
| 1040 | Santificación podrida                                                          |
| 1041 | Santificación podrida                                                          |
| 1042 | Número de personajes abrazados                                                 |
| 1043 | Tiros por codicia para el botín                                                |
| 1044 | Tiros por necesidad para el botín                                              |
| 1045 | Veces que has animado                                                          |
| 1047 | Veces que te has tapado la cara                                                |
| 1057 | Muertes en 2c2                                                                 |
| 1065 | Veces que has hecho /saludar                                                   |
| 1066 | Veces que has hecho /jaja                                                      |
| 1067 | Veces que has tocado el violín más pequeño del mundo                           |
| 1068 | Muertes de Keli\'dan el Ultrajador (El Horno de Sangre)                        |
| 1069 | Muertes del príncipe-nexo Shaffar (Tumbas de maná)                             |
| 1070 | Muertes del cazador de Época (La Fuga de Durnholde)                            |
| 1071 | Muertes de Quagmirran (Recinto de los Esclavos)                                |
| 1072 | Muertes de la acechadora negra (La Sotiénaga)                                  |
| 1073 | Muertes del exarca Maladaar (Criptas Auchenai)                                 |
| 1074 | Muertes del Rey Garra Ikiss (Salas Sethekk)                                    |
| 1075 | Muertes de Murmullo (Laberinto de las Sombras)                                 |
| 1076 | Muertes de Aeonus (Apertura de El Portal Oscuro)                               |
| 1077 | Muertes del señor de la guerra Kalithresh (Cámara de Vapor)                    |
| 1078 | Muertes del Jefe de Guerra K. Garrafilada (Salas Arrasadas)                    |
| 1079 | Muertes de Pathaleon el Calculador (El Mechanar)                               |
| 1080 | Muertes del disidente de distorsión (El Invernáculo)                           |
| 1081 | Muertes del presagista Cieloriss (El Arcatraz)                                 |
| 1082 | Muertes de Kael\'thas Caminante del Sol (Bancal del Magister)                  |
| 1083 | Muertes del príncipe Malchezaar (Karazhan)                                     |
| 1084 | Muertes de Zul\'jin (Zul\'Aman)                                                |
| 1085 | Muertes de Gruul (Guarida de Gruul)                                            |
| 1086 | Muertes de Magtheridon (Guarida de Magtheridon)                                |
| 1087 | Muertes de Lady Vashj (Caverna Santuario Serpiente)                            |
| 1088 | Muertes de Kael\'thas Caminante del Sol (Castillo Tempestad)                   |
| 1089 | Muertes de Illidan Tempestira (El Templo Oscuro)                               |
| 1090 | Muertes de Kil\'jaeden (Meseta de La Fuente del Sol)                           |
| 1091 | Muertes de Edwin VanCleef (Minas de la Muerte)                                 |
| 1092 | Muertes del archimago Arugal (Castillo de Colmillo Oscuro)                     |
| 1093 | Muertes del Comandante Escarlata Mograine (Mon. Escarlata)                     |
| 1094 | Muertes del jefe Ukorz Cabellarena (Zul\'Farrak)                               |
| 1095 | Muertes del Emperador D. Thaurissan (Prof. de Roca Negra)                      |
| 1096 | Muertes del General Drakkisath (Cumbre de Roca Negra)                          |
| 1097 | Muertes del Barón Osahendido (Stratholme)                                      |
| 1098 | Muertes de Onyxia (Guarida de Onyxia)                                          |
| 1099 | Muertes de Ragnaros (Núcleo de Magma)                                          |
| 1100 | Muertes de Nefarian (Guarida de Alanegra)                                      |
| 1101 | Muertes de C\'Thun (Templo de Ahn\'Qiraj)                                      |
| 1102 | Muertes de Hakkar (Zul\'Gurub)                                                 |
| 1103 | Lich King: Mazmorras completadas (5 j.) (jefe final asesinado)                 |
| 1104 | Lich King: Bandas completadas (10 j.) (jefe final asesinado)                   |
| 1106 | Muertes en el Ojo de la Tormenta                                               |
| 1107 | Muertes en 3c3                                                                 |
| 1108 | Muertes en 5c5                                                                 |
| 1109 | Muertes con honor en la arena 5c5                                              |
| 1110 | Muertes con honor en la arena 3c3                                              |
| 1111 | Muertes con honor en la arena 2c2                                              |
| 1112 | Muertes con honor en el Ojo de la Tormenta                                     |
| 1113 | Muertes con honor en el Valle de Alterac                                       |
| 1114 | Muertes con honor en la Cuenca de Arathi                                       |
| 1115 | Muertes con honor en la Garganta Grito de Guerra                               |
| 1125 | Venda más utilizada                                                            |
| 1145 | Rey del Festival de Fuego                                                      |
| 1146 | Cantidad de oro gastada en viajes                                              |
| 1147 | Cantidad de oro gastado en peluquerías                                         |
| 1148 | Cantidad de oro gastado en mensajes                                            |
| 1149 | Cantidad de cambios del árbol de talentos                                      |
| 1150 | Cantidad de oro gastado en cambiar el árbol de talentos                        |
| 1151 | Leal defensor                                                                  |
| 1153 | Demasiado defensivo                                                            |
| 1157 | Duelicioso                                                                     |
| 1159 | Entre tú y yo: 2200                                                            |
| 1160 | Tres son multitud: 2200                                                        |
| 1161 | Choca esos cinco: 2200                                                         |
| 1162 | Una racha mejor                                                                |
| 1164 | Todo cuenta                                                                    |
| 1165 | Mi bolsa es \'\'gigantesca\'\'                                                 |
| 1166 | El que despoja manda                                                           |
| 1167 | Maestro del Valle de Alterac                                                   |
| 1168 | Maestro del Valle de Alterac                                                   |
| 1169 | Maestro de la Cuenca de Arathi                                                 |
| 1170 | Maestro de la Cuenca de Arathi                                                 |
| 1171 | Maestro del Ojo de la Tormenta                                                 |
| 1172 | Maestro de la Garganta Grito de Guerra                                         |
| 1173 | Maestro de la Garganta Grito de Guerra                                         |
| 1174 | El maestro de la arena                                                         |
| 1175 | Maestro de batalla                                                             |
| 1176 | Pienso en mi dinero                                                            |
| 1177 | Pienso en mi dinero                                                            |
| 1178 | Pienso en mi dinero                                                            |
| 1180 | Pienso en mi dinero                                                            |
| 1181 | Pienso en mi dinero                                                            |
| 1182 | El que trae el pan a casa                                                      |
| 1183 | La cerveza del año                                                             |
| 1184 | Una extraña cerveza                                                            |
| 1185 | La dieta de la Fiesta de la cerveza                                            |
| 1186 | Abajo los Hierro Negro                                                         |
| 1187 | El Maestro de llaves                                                           |
| 1188 | ¡Pinchado!                                                                     |
| 1189 | Ida a Fuego Infernal y vuelta                                                  |
| 1190 | Misterios de la Marisma                                                        |
| 1191 | Terror de Terokkar                                                             |
| 1192 | Embate de Nagrand                                                              |
| 1193 | Sobre el filo de la espada                                                     |
| 1194 | A la tormenta                                                                  |
| 1195 | Sombra de El Traidor                                                           |
| 1197 | Muertes realizadas                                                             |
| 1198 | Cantidad de muertes que te han otorgado experiencia u honor                    |
| 1199 | Profesiones aprendidas                                                         |
| 1200 | Cantidad de habilidades secundarias al máximo nivel                            |
| 1201 | Cantidad de profesiones al máximo nivel                                        |
| 1202 | Cantidad de habilidades con armas al máximo nivel                              |
| 1203 | Una extraña cerveza                                                            |
| 1205 | Héroe de Shattrath                                                             |
| 1206 | A todas las ardillas que he amado                                              |
| 1225 | Pescador de Terrallende                                                        |
| 1229 | Revivido por druidas                                                           |
| 1231 | Muertes de Keristrasza (El Nexo)                                               |
| 1232 | Muertes de Anub\'arak (Azjol-Nerub)                                            |
| 1233 | Muertes del Heraldo Volazj (Ahn’kahet: El Antiguo Reino)                       |
| 1234 | Muertes del profeta Tharon\'ja (Fortaleza de Drak\'Tharon)                     |
| 1235 | Muertes de Cianigosa (El Bastión Violeta)                                      |
| 1236 | Muertes de Gal\'darah (Gundrak)                                                |
| 1237 | Muertes de Sjonnir el Afilador (Cámaras de Piedra)                             |
| 1238 | Muertes de Loken (Cámaras de Relámpagos)                                       |
| 1239 | Muertes del Guardián-Ley Eregos (El Oculus)                                    |
| 1240 | Muertes del Rey Ymiron (Pináculo de Utgarde)                                   |
| 1241 | Derrotas de Mal\'Ganis (Cavernas del Tiempo: Stratholme)                       |
| 1242 | Muertes de Ingvar el Desvalijador (Fortaleza de Utgarde)                       |
| 1243 | Los peces no dejan huellas                                                     |
| 1244 | Erudito                                                                        |
| 1248 | Plétora de mascotas                                                            |
| 1250 | Compra con cabeza, compra mascotas... con cabeza                               |
| 1251 | En mi casa no                                                                  |
| 1252 | Defensor supremo                                                               |
| 1253 | Convertido en un necrófago                                                     |
| 1254 | ¿Amigo o enemigo?                                                              |
| 1255 | Avaricioso                                                                     |
| 1257 | El carroñero                                                                   |
| 1258 | Tómate un tranquilizante                                                       |
| 1259 | No tan deprisa                                                                 |
| 1260 | Estupor de embriaguez                                                          |
| 1261 | Rabia C.H.U.C.H.E.G.                                                           |
| 1262 | Maestro cultural de Terrallende                                                |
| 1263 | Fiordo Aquilonal                                                               |
| 1264 | Tundra Boreal                                                                  |
| 1265 | Cementerio de Dragones                                                         |
| 1266 | Colinas Pardas                                                                 |
| 1267 | Zul\'Drak                                                                      |
| 1268 | Cuenca de Sholazar                                                             |
| 1269 | Las Cumbres Tormentosas                                                        |
| 1270 | Corona de Hielo                                                                |
| 1271 | Ida a Fuego Infernal y vuelta                                                  |
| 1272 | Terror de Terokkar                                                             |
| 1273 | Embate de Nagrand                                                              |
| 1274 | Maestro cultural de Terrallende                                                |
| 1275 | Bombas fuera                                                                   |
| 1276 | Bombardero de Filospada                                                        |
| 1277 | Defensa rápida                                                                 |
| 1279 | Flirtear con el desastre                                                       |
| 1280 | Flirtear con el desastre                                                       |
| 1281 | El resplandor rojo del cohete                                                  |
| 1282 | Tra-la-la-la-Ogri\'la                                                          |
| 1283 | Maestro de mazmorra clásico                                                    |
| 1284 | Maestro de mazmorras de Terrallende                                            |
| 1285 | Banda clásica                                                                  |
| 1286 | Banda de Terrallende                                                           |
| 1287 | Héroe de mazmorra de Terrallende                                               |
| 1288 | Maestro de mazmorra de Rasganorte                                              |
| 1289 | Héroe de mazmorra de Rasganorte                                                |
| 1291 | ¿Solo?                                                                         |
| 1292 | Jarra de la Fiesta de la cerveza amarilla                                      |
| 1293 | Jarra de la Fiesta de la cerveza azul                                          |
| 1295 | Coches de choque                                                               |
| 1296 | Mira cómo muere                                                                |
| 1297 | Hadronox rechazado                                                             |
| 1298 | Tipos de vendas diferentes usados                                              |
| 1299 | Poción de sanación más utilizada                                               |
| 1300 | Pociones de salud diferentes usadas                                            |
| 1301 | Poción de maná más utilizada                                                   |
| 1302 | Pociones de maná diferentes usadas                                             |
| 1303 | Elixir más consumido                                                           |
| 1304 | Elixires diferentes usados                                                     |
| 1305 | Frasco más consumido                                                           |
| 1306 | Frascos diferentes usados                                                      |
| 1307 | Cumbre de Roca Negra superior                                                  |
| 1308 | Victoria en la Playa de los Ancestros                                          |
| 1309 | Veterano de la Playa de los Ancestros                                          |
| 1310 | Asalta la playa                                                                |
| 1311 | Bastante exótica                                                               |
| 1312 | Sangrientamente exóticas                                                       |
| 1336 | Tipo de criatura que has matado más veces                                      |
| 1337 | Tipos de criaturas diferentes que has matado                                   |
| 1339 | Portal de mago que más veces has atravesado                                    |
| 1356 | He paseado por el Fiordo                                                       |
| 1357 | Mi furia por las pardas                                                        |
| 1358 | La Tundra no tiene nada de aburrida                                            |
| 1359 | El poder del Cementerio de Dragones                                            |
| 1360 | Maestro cultural de Rasganorte                                                 |
| 1361 | Muertes de Anub\'Rekhan (Naxxramas 10 j.)                                      |
| 1362 | Muertes de la Gran Viuda Faerlina (Naxxramas 10 j.)                            |
| 1363 | Muertes de Maexxna (Naxxramas 10 j.)                                           |
| 1364 | Muertes de Remendejo (Naxxramas 10 j.)                                         |
| 1365 | Muertes de Noth el Pesteador (Naxxramas 10 j.)                                 |
| 1366 | Muertes de Gothik el Cosechador (Naxxramas 10 j.)                              |
| 1367 | Muertes de Remendejo (Naxxramas 25 j.)                                         |
| 1368 | Muertes de Anub\'Rekhan (Naxxramas 25 j.)                                      |
| 1369 | Muertes de Heigan el Impuro (Naxxramas 10 j.)                                  |
| 1370 | Muertes de Loatheb (Naxxramas 10 j.)                                           |
| 1371 | Muertes de Grobbulus (Naxxramas 10 j.)                                         |
| 1372 | Muertes de Gluth (Naxxramas 10 j.)                                             |
| 1373 | Muertes de Thaddius (Naxxramas 10 j.)                                          |
| 1374 | Muertes del Instructor Razuvious (Naxxramas 10 j.)                             |
| 1375 | Muertes de Los Cuatro Jinetes (Naxxramas 10 j.)                                |
| 1376 | Muertes de Sapphiron (Naxxramas 10 j.)                                         |
| 1377 | Muertes de Kel\'Thuzad (Naxxramas 10 j.)                                       |
| 1378 | Muertes de Gluth (Naxxramas 25 j.)                                             |
| 1379 | Muertes de Gothik el Cosechador (Naxxramas 25 j.)                              |
| 1380 | Muertes de la Gran Viuda Faerlina (Naxxramas 25 j.)                            |
| 1381 | Muertes de Grobbulus (Naxxramas 25 j.)                                         |
| 1382 | Muertes de Heigan el Impuro (Naxxramas 25 j.)                                  |
| 1383 | Muertes de Los Cuatro Jinetes (Naxxramas 25 j.)                                |
| 1384 | Muertes del Instructor Razuvious (Naxxramas 25 j.)                             |
| 1385 | Muertes de Loatheb (Naxxramas 25 j.)                                           |
| 1386 | Muertes de Maexxna (Naxxramas 25 j.)                                           |
| 1387 | Muertes de Noth el Pesteador (Naxxramas 25 j.)                                 |
| 1388 | Muertes de Thaddius (Naxxramas 25 j.)                                          |
| 1389 | Muertes de Sapphiron (Naxxramas 25 j.)                                         |
| 1390 | Muertes de Kel\'Thuzad (Naxxramas 25 j.)                                       |
| 1391 | Muertes de Malygos (10 j.)                                                     |
| 1392 | Muertes de Sartharion (Cámara de los Aspectos 10 j.)                           |
| 1393 | Muertes de Sartharion (Cámara de los Aspectos 25 j.)                           |
| 1394 | Muertes de Malygos (25 j.)                                                     |
| 1396 | Ancestros de Rasganorte                                                        |
| 1400 | ¡Primero del reino! Buscador de magia                                          |
| 1402 | ¡Primero del reino! Conquistador de Naxxramas                                  |
| 1404 | ¡Primero del reino! Gnomo nivel 80                                             |
| 1405 | ¡Primero del reino! Elfo de sangre nivel 80                                    |
| 1406 | ¡Primero del reino! Draenei nivel 80                                           |
| 1407 | ¡Primero del reino! Enano nivel 80                                             |
| 1408 | ¡Primero del reino! Humano nivel 80                                            |
| 1409 | ¡Primero del reino! Elfo de la noche nivel 80                                  |
| 1410 | ¡Primero del reino! Orco nivel 80                                              |
| 1411 | ¡Primero del reino! Tauren nivel 80                                            |
| 1412 | ¡Primero del reino! Trol nivel 80                                              |
| 1413 | ¡Primero del reino! Renegado nivel 80                                          |
| 1414 | ¡Primero del reino! Gran maestro Herrero                                       |
| 1415 | ¡Primero del reino! Gran maestro Alquimista                                    |
| 1416 | ¡Primero del reino! Gran maestro Cocinero                                      |
| 1417 | ¡Primero del reino! Gran maestro Encantador                                    |
| 1418 | ¡Primero del reino! Gran maestro Ingeniero                                     |
| 1419 | ¡Primero del reino! Gran maestro en Primeros auxilios                          |
| 1420 | ¡Primero del reino! Gran maestro Pescador                                      |
| 1421 | ¡Primero del reino! Gran maestro Herborista                                    |
| 1422 | ¡Primero del reino! Gran maestro Escriba                                       |
| 1423 | ¡Primero del reino! Gran maestro Joyero                                        |
| 1424 | ¡Primero del reino! Gran maestro Peletero                                      |
| 1425 | ¡Primero del reino! Gran maestro Minero                                        |
| 1426 | ¡Primero del reino! Gran maestro Desollador                                    |
| 1427 | ¡Primero del reino! Gran maestro Sastre                                        |
| 1428 | Barredor de minas                                                              |
| 1436 | Amigos en lugares altos                                                        |
| 1456 | Peces y otras cosas pescadas                                                   |
| 1457 | Bosque Canto de Cristal                                                        |
| 1458 | Continente con más número de muertes con honor                                 |
| 1462 | Distintivos de justicia adquiridos                                             |
| 1463 | ¡Primero del reino! Vanguardia de Rasganorte                                   |
| 1464 | Emblemas de heroísmo adquiridos                                                |
| 1465 | Emblemas de valor adquiridos                                                   |
| 1466 | Mayoría de facciones de la Alianza a nivel Exaltado                            |
| 1467 | Lich King: Jefes asesinados (5 j.)                                             |
| 1485 | Lich King: Jefes diferentes asesinados (5 j.)                                  |
| 1486 | Muertes con honor en la Playa de los Ancestros                                 |
| 1487 | Golpes de gracia                                                               |
| 1488 | Golpes de gracia del mundo                                                     |
| 1489 | Continente con más número de golpes de gracia                                  |
| 1490 | Golpes de gracia en la arena                                                   |
| 1491 | Golpes de gracia en campos de batalla                                          |
| 1492 | Golpes de gracia en la arena 2c2                                               |
| 1493 | Golpes de gracia en la arena 3c3                                               |
| 1494 | Golpes de gracia en la arena 5c5                                               |
| 1495 | Golpes de gracia en el Valle de Alterac                                        |
| 1496 | Golpes de gracia en la Cuenca de Arathi                                        |
| 1497 | Golpes de gracia en la Garganta Grito de Guerra                                |
| 1498 | Golpes de gracia en el Ojo de la Tormenta                                      |
| 1499 | Golpes de gracia en la Playa de los Ancestros                                  |
| 1500 | Muertes en la Playa de los Ancestros                                           |
| 1501 | Veces que te han matado otros jugadores                                        |
| 1502 | Captura rápida                                                                 |
| 1504 | Muertes de Ingvar el Desvalijador (Fortaleza de Utgarde H.)                    |
| 1505 | Muertes de Keristrasza (El Nexo H.)                                            |
| 1506 | Muertes de Anub\'arak (Azjol-Nerub H.)                                         |
| 1507 | Muertes del Heraldo Volazj (Ahn\'Kahet: El Antiguo Reino H.)                   |
| 1508 | Muertes del profeta Tharon\'ja (Fortaleza de Drak\'Tharon H.)                  |
| 1509 | Muertes de Cianigosa (El Bastión Violeta H.)                                   |
| 1510 | Muertes de Gal\'darah (Gundrak H.)                                             |
| 1511 | Muertes de Sjonnir el Afilador (Cámaras de Piedra H.)                          |
| 1512 | Muertes de Loken (Cámaras de Relámpagos H.)                                    |
| 1513 | Muertes del Guardián-Ley Eregos (El Oculus H.)                                 |
| 1514 | Muertes del Rey Ymiron (Pináculo de Utgarde H.)                                |
| 1515 | Derrotas de Mal\'Ganis (Cavernas del Tiempo H.: Stratholme)                    |
| 1516 | El mejor pescador                                                              |
| 1517 | Pescador de Rasganorte                                                         |
| 1518 | Peces pescados                                                                 |
| 1519 | Habilidad en pesca                                                             |
| 1524 | Habilidad en cocina                                                            |
| 1525 | Misiones de cocina diarias completadas                                         |
| 1526 | Misiones de pesca diarias completadas                                          |
| 1527 | Habilidad en alquimia mayor                                                    |
| 1532 | Habilidad en herrería mayor                                                    |
| 1535 | Habilidad en encantamiento mayor                                               |
| 1536 | Habilidad en peletería mayor                                                   |
| 1537 | Habilidad en minería mayor                                                     |
| 1538 | Habilidad en herboristería mayor                                               |
| 1539 | Habilidad en inscripción mayor                                                 |
| 1540 | Habilidad en joyería mayor                                                     |
| 1541 | Habilidad en desuello mayor                                                    |
| 1542 | Habilidad en sastrería mayor                                                   |
| 1544 | Habilidad en ingeniería mayor                                                  |
| 1545 | Encuentros en el Círculo del Valor                                             |
| 1546 | Victorias en el Círculo del Valor                                              |
| 1547 | Encuentros en las Cloacas de Dalaran                                           |
| 1548 | Victorias en las Cloacas de Dalaran                                            |
| 1549 | Batallas en la Playa de los Ancestros                                          |
| 1550 | Victorias en la Playa de los Ancestros                                         |
| 1552 | Petardo frenético                                                              |
| 1556 | 25 peces                                                                       |
| 1557 | 50 peces                                                                       |
| 1558 | 100 peces                                                                      |
| 1559 | 250 peces                                                                      |
| 1560 | 500 peces                                                                      |
| 1561 | 1000 peces                                                                     |
| 1563 | Felicita al cocinero                                                           |
| 1576 | De sangre y angustia                                                           |
| 1596 | Gurú de Drakuru                                                                |
| 1636 | Tabardo de competidor                                                          |
| 1637 | Espíritu de competición                                                        |
| 1638 | Devastado                                                                      |
| 1656 | Santificado sea tu nombre                                                      |
| 1657 | Santificado sea tu nombre                                                      |
| 1658 | Campeón de los baldíos helados                                                 |
| 1676 | Maestro cultural de los Reinos del Este                                        |
| 1677 | Maestro cultural de los Reinos del Este                                        |
| 1678 | Maestro cultural de Kalimdor                                                   |
| 1680 | Maestro cultural de Kalimdor                                                   |
| 1681 | El maestro cultural                                                            |
| 1682 | El maestro cultural                                                            |
| 1683 | Maestro cervecero                                                              |
| 1684 | Maestro cervecero                                                              |
| 1685 | Hermanos antes del ho ho ho                                                    |
| 1686 | Hermanos antes del ho ho ho                                                    |
| 1687 | ¡Que nieve!                                                                    |
| 1688 | El gourmet del Festival de Invierno                                            |
| 1689 | Sabrá si has sido malo                                                         |
| 1690 | Meneíto helado                                                                 |
| 1691 | Juerguista                                                                     |
| 1692 | Juerguista                                                                     |
| 1693 | Loco de amor                                                                   |
| 1694 | La preciosa suerte está de tu lado                                             |
| 1695 | Amor peligroso                                                                 |
| 1696 | El resplandor rosa del cohete                                                  |
| 1697 | La nación de la adoración                                                      |
| 1698 | La nación de la adoración                                                      |
| 1699 | Puñado de amor                                                                 |
| 1700 | Pies Rápidos permanentes                                                       |
| 1701 | ¡Sé mío!                                                                       |
| 1702 | Goloso                                                                         |
| 1703 | Mi amor es como una rosa roja                                                  |
| 1704 | Me apiadé del loco                                                             |
| 1705 | Robot cohete de cuerda                                                         |
| 1706 | Coche de carreras triturador                                                   |
| 1707 | Loco de amor                                                                   |
| 1716 | Campo de batalla con más número de golpes de gracia                            |
| 1717 | Victoria en Conquista del Invierno                                             |
| 1718 | Veterano de Conquista del Invierno                                             |
| 1719 | Campo de batalla con más número de muertes con honor                           |
| 1721 | Archavon el Vigía de Piedra (25j.)                                             |
| 1722 | Archavon el Vigía de Piedra (10 j.)                                            |
| 1723 | Matanza de gnomos rodada                                                       |
| 1727 | La torre inclinada                                                             |
| 1729 | Recetas de alquimia conocidas                                                  |
| 1730 | Diseños de herrería conocidos                                                  |
| 1734 | Esquemas de ingeniería conocidos                                               |
| 1735 | Inscripciones conocidas                                                        |
| 1737 | Derbi destructivo                                                              |
| 1738 | Diseños de joyería conocidos                                                   |
| 1740 | Patrones de peletería conocidos                                                |
| 1741 | Patrones de sastrería conocidos                                                |
| 1745 | Recetas de cocina conocidas                                                    |
| 1748 | Manuales de primeros auxilios estudiados                                       |
| 1751 | No tenían posibilidades                                                        |
| 1752 | Maestro de Conquista del Invierno                                              |
| 1753 | Muertes de Archavon el Vigía de Piedra (Conquista del Invierno 10 j.)          |
| 1754 | Muertes de Archavon el Vigía de Piedra (Conquista del Invierno 25 j.)          |
| 1755 | En nuestras manos                                                              |
| 1756 | Lich King: Jefes asesinados (25 j.)                                            |
| 1757 | Defensa de los Ancestros                                                       |
| 1759 | Lich King: Jefes diferentes asesinados (25 j.)                                 |
| 1760 | Lich King: Jefe asesinado más veces (25 j.)                                    |
| 1761 | El zapador activo                                                              |
| 1762 | Sin un rasguño                                                                 |
| 1763 | Veterano artillero                                                             |
| 1764 | ¡Suéltalo!                                                                     |
| 1765 | Manos firmes                                                                   |
| 1766 | Protector de los Ancestros                                                     |
| 1768 | Lich King: Bandas completadas (25 j.) (jefe final asesinado)                   |
| 1770 | Lich King: Jefes asesinados (10 j.)                                            |
| 1771 | Lich King: Jefes diferentes asesinados (10 j.)                                 |
| 1772 | Lich King: Jefe asesinado más veces (10 j.)                                    |
| 1773 | Bebida más consumida                                                           |
| 1774 | Bebidas diferentes consumidas                                                  |
| 1775 | Comidas diferentes consumidas                                                  |
| 1776 | Comida más consumida                                                           |
| 1777 | El gourmet de Rasganorte                                                       |
| 1778 | El gourmet de Rasganorte                                                       |
| 1779 | El gourmet de Rasganorte                                                       |
| 1780 | Secundar esa emoción                                                           |
| 1781 | Coleccionista de alimañas                                                      |
| 1782 | Nuestro pan de cada día                                                        |
| 1783 | Nuestro pan de cada día                                                        |
| 1784 | Felicita al cocinero                                                           |
| 1785 | Cena imposible                                                                 |
| 1786 | Escuela de buenos golpes                                                       |
| 1788 | Mal ejemplo                                                                    |
| 1789 | Faenas diarias                                                                 |
| 1790 | ¡Saluda al rey, pequeño!                                                       |
| 1791 | Solo en casa                                                                   |
| 1792 | Mira qué monada                                                                |
| 1793 | Para los niños                                                                 |
| 1795 | Cocinillas                                                                     |
| 1796 | Cocinerillo de tres al cuarto                                                  |
| 1797 | Chef encargado                                                                 |
| 1798 | Asistente de chef                                                              |
| 1799 | Chef de cocina                                                                 |
| 1800 | El gourmet de Terrallende                                                      |
| 1801 | Cerveza del capitán Rumsey                                                     |
| 1816 | Indefensa                                                                      |
| 1817 | Matar el tiempo                                                                |
| 1832 | Sabe a pollo                                                                   |
| 1833 | Es la hora feliz en algún lugar                                                |
| 1834 | Descarga de relámpago                                                          |
| 1836 | El viejo Astuto                                                                |
| 1837 | El viejo Quijahierro                                                           |
| 1856 | Hazle un buen remiendo (10 j.)                                                 |
| 1857 | Hazle un buen remiendo (25 j.)                                                 |
| 1858 | Aracnofobia (10 j.)                                                            |
| 1859 | Aracnofobia (25 j.)                                                            |
| 1860 | ¡Me voy de aquí!                                                               |
| 1862 | La rápida muerte de Volazj                                                     |
| 1864 | ¿Quéck pasa aquí?                                                              |
| 1865 | ¡Encerrados!                                                                   |
| 1866 | ¡Qué pena!                                                                     |
| 1867 | Muerte calculada                                                               |
| 1868 | Haz que cuente                                                                 |
| 1869 | El dedo en la llaga (10 j.)                                                    |
| 1870 | El dedo en la llaga (25 j.)                                                    |
| 1871 | Jinete de dracos experto                                                       |
| 1872 | ¡Fiesta de zombis!                                                             |
| 1873 | Tralarí, tralarí, nos encanta Skadi                                            |
| 1874 | No tenemos toda la eternidad (10 j.)                                           |
| 1875 | No tenemos toda la eternidad (25 j.)                                           |
| 1876 | Vencer al Vuelo Negro (10 j.)                                                  |
| 1877 | Menos es más (25 j.)                                                           |
| 1919 | Con hielo                                                                      |
| 1936 | ¿Es persistente tu wolpertinger?                                               |
| 1956 | Conocimiento superior                                                          |
| 1957 | Hay oro en esa fuente de ahí                                                   |
| 1958 | Aquí huele a rata gigante                                                      |
| 1976 | Premios de cocina de Dalaran recibidos                                         |
| 1977 | Muestras de joyero de Dalaran recibidas                                        |
| 1996 | Baila por tu vida (10 j.)                                                      |
| 1997 | Mamá me dijo que te pegara (10 j.)                                             |
| 1998 | Premio de cocina de Dalaran                                                    |
| 1999 | 10 Premios de cocina de Dalaran                                                |
| 2000 | 25 Premios de cocina de Dalaran                                                |
| 2001 | 50 Premios de cocina de Dalaran                                                |
| 2002 | 100 Premios de cocina de Dalaran                                               |
| 2016 | Veterano Pardo                                                                 |
| 2017 | Veterano Pardo                                                                 |
| 2018 | Previsiones Tiemporeja                                                         |
| 2019 | Prueba de defunción                                                            |
| 2036 | Frío intenso                                                                   |
| 2037 | La teoría del caos                                                             |
| 2038 | Respeta a tus mayores                                                          |
| 2039 | Antes muerto…                                                                  |
| 2040 | Menos Moorabi                                                                  |
| 2041 | Deshidratación                                                                 |
| 2042 | Antipedacitos                                                                  |
| 2043 | La increíble mole                                                              |
| 2044 | Vacío rubí                                                                     |
| 2045 | Vacío esmeralda                                                                |
| 2046 | Vacío ámbar                                                                    |
| 2047 | Me voy cuando el volcán entre en erupción (10 j.)                              |
| 2048 | Me voy cuando el volcán entre en erupción (25 j.)                              |
| 2049 | Ayuda crepuscular (10 j.)                                                      |
| 2050 | Dúo crepuscular (10 j.)                                                        |
| 2051 | La Dimensión desconocida (10 j.)                                               |
| 2052 | Ayuda crepuscular (25 j.)                                                      |
| 2053 | Dúo crepuscular (25 j.)                                                        |
| 2054 | La Dimensión desconocida (25 j.)                                               |
| 2056 | Trabajo de voluntario                                                          |
| 2057 | Oh, ¡Novos!                                                                    |
| 2058 | Serpientes. ¿Por qué serpientes?                                               |
| 2076 | Oso marrón acorazado                                                           |
| 2077 | Mamut lanudo                                                                   |
| 2078 | Mamut de tundra viajero                                                        |
| 2079 | Tabardo del protector                                                          |
| 2080 | Mamut de guerra negro                                                          |
| 2081 | Gran mamut de guerra negro                                                     |
| 2082 | Mamut de hielo                                                                 |
| 2083 | Gran mamut de hielo                                                            |
| 2084 | Anillo del Kirin Tor                                                           |
| 2085 | 50 fragmentos de vigilante de piedra                                           |
| 2086 | 100 fragmentos de vigilante de piedra                                          |
| 2087 | 250 fragmentos de vigilante de piedra                                          |
| 2088 | 500 fragmentos de vigilante de piedra                                          |
| 2089 | 1000 fragmentos de vigilante de piedra                                         |
| 2090 | Contendiente                                                                   |
| 2091 | Gladiador                                                                      |
| 2092 | Duelista                                                                       |
| 2093 | Rival                                                                          |
| 2094 | La fuente de los deseos                                                        |
| 2095 | Plata en la ciudad                                                             |
| 2096 | El maestro de las monedas                                                      |
| 2097 | ¡Móntate en la chopper!                                                        |
| 2116 | Tabardo de El Alba Argenta                                                     |
| 2136 | La gloria del héroe                                                            |
| 2137 | La gloria del asaltante (10 j.)                                                |
| 2138 | La gloria del asaltante (25 j.)                                                |
| 2139 | Baila por tu vida (25 j.)                                                      |
| 2140 | Mamá me dijo que te pegara (25 j.)                                             |
| 2141 | Vigilante de establos                                                          |
| 2142 | Llenar el establo                                                              |
| 2143 | Liderar la caballería                                                          |
| 2144 | Ha sido un largo y raro viaje                                                  |
| 2145 | Ha sido un largo y raro viaje                                                  |
| 2146 | El club de los Cien (10 j.)                                                    |
| 2147 | El club de los Cien (25 j.)                                                    |
| 2148 | Rechazar al sucesor (10 j.)                                                    |
| 2149 | Rechazar al sucesor (25 j.)                                                    |
| 2150 | Doble personalidad                                                             |
| 2151 | Cruce de consumiciones                                                         |
| 2152 | Compartir el amor                                                              |
| 2153 | Un baile con el vacío                                                          |
| 2154 | Brann totalmente nuevo                                                         |
| 2155 | Abusar de los mocos                                                            |
| 2156 | A mi chica le encanta Skadi                                                    |
| 2157 | La pesadilla del Rey                                                           |
| 2176 | Y todos caerán a la misma vez (10 j.)                                          |
| 2177 | Y todos caerán a la misma vez (25 j.)                                          |
| 2178 | ¡Electrificante! (10 j.)                                                       |
| 2179 | ¡Electrificante! (25 j.)                                                       |
| 2180 | Sustraer (10 j.)                                                               |
| 2181 | Sustraer (25 j.)                                                               |
| 2182 | Perder las esporas (10 j.)                                                     |
| 2183 | Perder las esporas (25 j.)                                                     |
| 2184 | Nunca es suficiente (10 j.)                                                    |
| 2185 | Nunca es suficiente (25 j.)                                                    |
| 2186 | Los inmortales                                                                 |
| 2187 | Los indestructibles                                                            |
| 2188 | ¡Leeeeeeeeeeeeeroy!                                                            |
| 2189 | Experto artillero                                                              |
| 2190 | ¡Suéltalo ahora!                                                               |
| 2191 | Protector del Patio de los Ancestros                                           |
| 2192 | Sin un rasguño                                                                 |
| 2193 | Experto en explosivos                                                          |
| 2194 | Maestro de la Playa de los Ancestros                                           |
| 2195 | Maestro de la Playa de los Ancestros                                           |
| 2199 | Forestal de Conquista del Invierno                                             |
| 2200 | Defensa de los Ancestros                                                       |
| 2216 | Lich King: Jefe más mortífero (5 j.)                                           |
| 2217 | Lich King: Jefe más mortífero (10 j.)                                          |
| 2218 | Lich King: Jefe más mortífero (25 j.)                                          |
| 2219 | Muertes totales en mazmorras heroicas (5 j.)                                   |
| 2256 | Expuesto a Rasganorte                                                          |
| 2257 | Congelado                                                                      |
| 2277 | Invocaciones aceptadas                                                         |
| 2316 | Draco abisal brutal                                                            |
| 2336 | Demente supereminente                                                          |
| 2357 | Corcel nefasto xorothiano                                                      |
| 2358 | Destrero                                                                       |
| 2359 | Forma de vuelo presto                                                          |
| 2396 | Campo de batalla jugado más veces                                              |
| 2397 | Campo de batalla ganado más veces                                              |
| 2398 | 4º aniversario de WoW                                                          |
| 2416 | Huevo duro                                                                     |
| 2417 | ¡Chocolateee!                                                                  |
| 2418 | Chocohólico                                                                    |
| 2419 | La primavera, la sangre altera                                                 |
| 2420 | Jardín Noble                                                                   |
| 2421 | Jardín Noble                                                                   |
| 2422 | Sacude las orejitas                                                            |
| 2436 | Rosa del desierto                                                              |
| 2456 | Cazador de vampiros                                                            |
| 2476 | Derbi destructivo                                                              |
| 2496 | El quinto elemento                                                             |
| 2497 | La primavera, la sangre altera                                                 |
| 2516 | Caza menor                                                                     |
| 2536 | Un montón de monturas                                                          |
| 2537 | Un montón de monturas                                                          |
| 2556 | Control de plagas                                                              |
| 2557 | A todas las ardillas de mi vida                                                |
| 2576 | El sonrojo de la novia                                                         |
| 2596 | Muertes de Baldomero                                                           |
| 2676 | ¡He encontrado uno!                                                            |
| 2716 | Doble especialización de talentos                                              |
| 2756 | Aspiración Argenta                                                             |
| 2758 | Valor Argenta                                                                  |
| 2760 | Campeón Exaltado de Darnassus                                                  |
| 2761 | Campeón Exaltado de El Exodar                                                  |
| 2762 | Campeón Exaltado de Gnomeregan                                                 |
| 2763 | Campeón Exaltado de Forjaz                                                     |
| 2764 | Campeón Exaltado de Ventormenta                                                |
| 2765 | Campeón Exaltado de Orgrimmar                                                  |
| 2766 | Campeón Exaltado de Sen\'jin                                                   |
| 2767 | Campeón Exaltado de Ciudad de Lunargenta                                       |
| 2768 | Campeón Exaltado de Cima del Trueno                                            |
| 2769 | Campeón Exaltado de Entrañas                                                   |
| 2770 | Campeón Exaltado de la Alianza                                                 |
| 2771 | Campeón Exaltado de la Horda                                                   |
| 2772 | ¡Lanza en ristre!                                                              |
| 2773 | Solo es una herida superficial                                                 |
| 2776 | Maestro de Conquista del Invierno                                              |
| 2777 | Campeón de Darnassus                                                           |
| 2778 | Campeón de El Exodar                                                           |
| 2779 | Campeón de Gnomeregan                                                          |
| 2780 | Campeón de Forjaz                                                              |
| 2781 | Campeón de Ventormenta                                                         |
| 2782 | Campeón de la Alianza                                                          |
| 2783 | Campeón de Orgrimmar                                                           |
| 2784 | Campeón de Sen\'jin                                                            |
| 2785 | Campeón de Ciudad de Lunargenta                                                |
| 2786 | Campeón de Cima del Trueno                                                     |
| 2787 | Campeón de Entrañas                                                            |
| 2788 | Campeón de la Horda                                                            |
| 2796 | La cerveza del mes                                                             |
| 2797 | Jardinero Noble                                                                |
| 2798 | Jardinero Noble                                                                |
| 2816 | Campeón Argenta Exaltado de la Horda                                           |
| 2817 | Campeón Argenta Exaltado de la Alianza                                         |
| 2836 | Lanzalote                                                                      |
| 2856 | Muertes del Leviatán de llamas (Ulduar 10 j.)                                  |
| 2857 | Muertes de Tajoescama (Ulduar 10 j.)                                           |
| 2858 | Muertes de Ignis el Maestro de la Caldera (Ulduar 10 j.)                       |
| 2859 | Muertes del Desarmador XA-002 (Ulduar 10 j.)                                   |
| 2860 | Muertes de la Asamblea de Hierro (Ulduar 10 j.)                                |
| 2861 | Muertes de Kologarn (Ulduar 10 j.)                                             |
| 2862 | Victorias sobre Hodir (Ulduar 10 j.)                                           |
| 2863 | Victorias sobre Thorim (Ulduar 10 j.)                                          |
| 2864 | Victorias sobre Freya (Ulduar 10 j.)                                           |
| 2865 | Victorias sobre Mimiron (Ulduar 10 j.)                                         |
| 2866 | Muertes del general Vezax (Ulduar 10 j.)                                       |
| 2867 | Muertes de Algalon el Observador (Ulduar 10 j.)                                |
| 2868 | Muertes de Auriaya (Ulduar 10 j.)                                              |
| 2869 | Muertes de Yogg-Saron (Ulduar 10 j.)                                           |
| 2870 | Muertes de Emalon el Vigía de la Tormenta (Conquista del Invierno 10 j.)       |
| 2872 | Muertes del Leviatán de llamas (Ulduar 25 j.)                                  |
| 2873 | Muertes de Tajoescama (Ulduar 25 j.)                                           |
| 2874 | Muertes de Ignis el Maestro de la Caldera (Ulduar 25 j.)                       |
| 2875 | Muertes de Kologarn (Ulduar 25 j.)                                             |
| 2879 | Victorias sobre Mimiron (Ulduar 25 j.)                                         |
| 2880 | Muertes del general Vezax (Ulduar 25 j.)                                       |
| 2881 | Muertes de Algalon el Observador (Ulduar 25 j.)                                |
| 2882 | Muertes de Auriaya (Ulduar 25 j.)                                              |
| 2883 | Muertes de Yogg-Saron (Ulduar 25 j.)                                           |
| 2884 | Muertes del Desarmador XA-002 (Ulduar 25 j.)                                   |
| 2885 | Muertes de la Asamblea de Hierro (Ulduar 25 j.)                                |
| 2886 | El asedio de Ulduar (10 j.)                                                    |
| 2887 | El asedio de Ulduar (25 j.)                                                    |
| 2888 | La Antecámara de Ulduar (10 j.)                                                |
| 2889 | La Antecámara de Ulduar (25 j.)                                                |
| 2890 | Los vigilantes de Ulduar (10 j.)                                               |
| 2891 | Los vigilantes de Ulduar (25 j.)                                               |
| 2892 | El Descenso a la Locura (10 j.)                                                |
| 2893 | El Descenso a la Locura (25 j.)                                                |
| 2894 | Los secretos de Ulduar (10 j.)                                                 |
| 2895 | Los secretos de Ulduar (25 j.)                                                 |
| 2903 | Campeón de Ulduar                                                              |
| 2904 | Conquistador de Ulduar                                                         |
| 2905 | Irrompible (10 j.)                                                             |
| 2906 | Irrompible (25 j.)                                                             |
| 2907 | Garaje de tres plazas (10 j.)                                                  |
| 2908 | Garaje de tres plazas (25 j.)                                                  |
| 2909 | Derribad esas torretas (10 j.)                                                 |
| 2910 | Derribad esas torretas (25 j.)                                                 |
| 2911 | Cerrado (10 j.)                                                                |
| 2912 | Cerrado (25 j.)                                                                |
| 2913 | Bombardeo orbital (10 j.)                                                      |
| 2914 | Devastación orbital (10 j.)                                                    |
| 2915 | Bombardeo atómico orbital (10 j.)                                              |
| 2916 | Devastación orbital (25 j.)                                                    |
| 2917 | Bombardeo atómico orbital (25 j.)                                              |
| 2918 | Bombardeo orbital (25 j.)                                                      |
| 2919 | Un afeitado rápido (10 j.)                                                     |
| 2921 | Un afeitado rápido (25 j.)                                                     |
| 2923 | Enano férreo, poco hecho (10 j.)                                               |
| 2924 | Enano férreo, poco hecho (25 j.)                                               |
| 2925 | Arrasado (10 j.)                                                               |
| 2926 | Arrasado (25 j.)                                                               |
| 2927 | Horneado (10 j.)                                                               |
| 2928 | Horneado (25 j.)                                                               |
| 2929 | Avivar las llamas (25 j.)                                                      |
| 2930 | Avivar las llamas (10 j.)                                                      |
| 2931 | Apoca la ingeniería (10 j.)                                                    |
| 2932 | Apoca la ingeniería (25 j.)                                                    |
| 2933 | Apoca robots chatarra (10 j.)                                                  |
| 2934 | Apoca Bombas de gravedad (10 j.)                                               |
| 2935 | Apoca robots chatarra (25 j.)                                                  |
| 2936 | Apoca Bombas de gravedad (25 j.)                                               |
| 2937 | Hay que desarmar más deprisa (10 j.)                                           |
| 2938 | Hay que desarmar más deprisa (25 j.)                                           |
| 2939 | Te elijo a ti, maestro de runas Molgeim (10 j.)                                |
| 2940 | Te elijo a ti, clamatormentas Brundir (10 j.)                                  |
| 2941 | Te elijo a ti, Rompeacero (10 j.)                                              |
| 2942 | Te elijo a ti, maestro de runas Molgeim (25 j.)                                |
| 2943 | Te elijo a ti, clamatormentas Brundir (25 j.)                                  |
| 2944 | Te elijo a ti, Rompeacero (25 j.)                                              |
| 2945 | Pero estoy de vuestro lado (10 j.)                                             |
| 2946 | Pero estoy de vuestro lado (25 j.)                                             |
| 2947 | No puedes hacer eso mientras estés aturdido (10 j.)                            |
| 2948 | No puedes hacer eso mientras estés aturdido (25 j.)                            |
| 2951 | Con los brazos abiertos (10 j.)                                                |
| 2952 | Con los brazos abiertos (25 j.)                                                |
| 2953 | Desarmado (10 j.)                                                              |
| 2954 | Desarmado (25 j.)                                                              |
| 2955 | Si las miradas mataran (10 j.)                                                 |
| 2956 | Si las miradas mataran (25 j.)                                                 |
| 2957 | La gloria del asaltante de Ulduar (10 j.)                                      |
| 2958 | La gloria del asaltante de Ulduar (25 j.)                                      |
| 2959 | Roca-nrol (10 j.)                                                              |
| 2960 | Roca-nrol (25 j.)                                                              |
| 2961 | Soporta el frío (10 j.)                                                        |
| 2962 | Soporta el frío (25 j.)                                                        |
| 2963 | Mis amigos son unos frescos (10 j.)                                            |
| 2965 | Mis amigos son unos frescos (25 j.)                                            |
| 2967 | Aquí hace frío (10 j.)                                                         |
| 2968 | Aquí hace frío (25 j.)                                                         |
| 2969 | Pasar todo el invierno beneficiado (10 j.)                                     |
| 2970 | Pasar todo el invierno beneficiado (25 j.)                                     |
| 2971 | Apártate del rayo (10 j.)                                                      |
| 2972 | Apártate del rayo (25 j.)                                                      |
| 2973 | Me enfrentaré con todos (10 j.)                                                |
| 2974 | Me enfrentaré con todos (25 j.)                                                |
| 2975 | ¿Quién necesita Ansia de sangre? (10 j.)                                       |
| 2976 | ¿Quién necesita Ansia de sangre? (25 j.)                                       |
| 2977 | Con Sif (10 j.)                                                                |
| 2978 | Con Sif (25 j.)                                                                |
| 2979 | Hecho leña (10 j.)                                                             |
| 2980 | In-veloz-ero (10 j.)                                                           |
| 2981 | In-veloz-ero (25 j.)                                                           |
| 2982 | Regresar a la naturaleza (10 j.)                                               |
| 2983 | Regresar a la naturaleza (25 j.)                                               |
| 2984 | Deforestación (25 j.)                                                          |
| 2985 | Deforestación (10 j.)                                                          |
| 2989 | Ponednos una bomba (10 j.)                                                     |
| 2995 | Un fuego no tan amistoso (25 j.)                                               |
| 2996 | Esquivasombras (10 j.)                                                         |
| 2997 | Esquivasombras (25 j.)                                                         |
| 3002 | Supermasivo (25 j.)                                                            |
| 3003 | Supermasivo (10 j.)                                                            |
| 3004 | Se alimenta de tus lágrimas (10 j.)                                            |
| 3005 | Se alimenta de tus lágrimas (25 j.)                                            |
| 3006 | La loca de los gatos (10 j.)                                                   |
| 3007 | La loca de los gatos (25 j.)                                                   |
| 3008 | Vuélveme loco (10 j.)                                                          |
| 3009 | Daos un beso y haced las paces (10 j.)                                         |
| 3010 | Vuélveme loco (25 j.)                                                          |
| 3011 | Daos un beso y haced las paces (25 j.)                                         |
| 3012 | No se volverá más antiguo (10 j.)                                              |
| 3013 | No se volverá más antiguo (25 j.)                                              |
| 3014 | Salen de las paredes (10 j.)                                                   |
| 3015 | En su hogar espera soñando (10 j.)                                             |
| 3016 | En su hogar espera soñando (25 j.)                                             |
| 3017 | Salen de las paredes (25 j.)                                                   |
| 3018 | Emblemas de conquista adquiridos                                               |
| 3036 | Observado (10 j.)                                                              |
| 3037 | Observado (25 j.)                                                              |
| 3056 | Orbituario (10 j.)                                                             |
| 3057 | Orbituario (25 j.)                                                             |
| 3058 | Rompecorazones (10 j.)                                                         |
| 3059 | Rompecorazones (25 j.)                                                         |
| 3076 | Siete vidas (10 j.)                                                            |
| 3077 | Siete vidas (25 j.)                                                            |
| 3096 | Vermis de escarcha de Gladiador mortal                                         |
| 3097 | Enanicidio (10 j.)                                                             |
| 3098 | Enanicidio (25 j.)                                                             |
| 3117 | ¡Primero del reino! Heroico: Ejecutor de la muerte                             |
| 3118 | Hecho leña (25 j.)                                                             |
| 3136 | Emalon el Vigía de la Tormenta (10 j.)                                         |
| 3137 | Emalon el Vigía de la Tormenta (25 j.)                                         |
| 3138 | Un fuego no tan amistoso (10 j.)                                               |
| 3141 | Dos luces en la oscuridad (10 j.)                                              |
| 3142 | Val\'anyr, Martillo de los antiguos reyes                                      |
| 3157 | Tres luces en la oscuridad (10 j.)                                             |
| 3158 | Una luz en la oscuridad (10 j.)                                                |
| 3159 | Solo en la oscuridad (10 j.)                                                   |
| 3161 | Tres luces en la oscuridad (25 j.)                                             |
| 3162 | Dos luces en la oscuridad (25 j.)                                              |
| 3163 | Una luz en la oscuridad (25 j.)                                                |
| 3164 | Solo en la oscuridad (25 j.)                                                   |
| 3176 | Pierde tu ilusión (10 j.)                                                      |
| 3177 | Toca madera (10 j.)                                                            |
| 3178 | Toca, toca madera (10 j.)                                                      |
| 3179 | Toca, toca, toca madera (10 j.)                                                |
| 3180 | Bombero (10 j.)                                                                |
| 3181 | Me encanta el aroma de la saronita por la mañana (10 j.)                       |
| 3182 | Ya decía yo que este alijo era poco común (10 j.)                              |
| 3183 | Pierde tu ilusión (25 j.)                                                      |
| 3184 | Ya decía yo que este alijo era poco común (25 j.)                              |
| 3185 | Toca madera (25 j.)                                                            |
| 3186 | Toca, toca madera (25 j.)                                                      |
| 3187 | Toca, toca, toca madera (25 j.)                                                |
| 3188 | Me encanta el aroma de la saronita por la mañana (25 j.)                       |
| 3189 | Bombero (25 j.)                                                                |
| 3216 | Recetas de fundición aprendidas                                                |
| 3217 | Marcia y sedal                                                                 |
| 3218 | Tortugas hasta al fin                                                          |
| 3236 | Muertes de Emalon el Vigía de la Tormenta (Conquista del Invierno 25 j.)       |
| 3237 | Ponednos una bomba (25 j.)                                                     |
| 3256 | Victorias sobre Hodir (Ulduar 25 j.)                                           |
| 3257 | Victorias sobre Thorim (Ulduar 25 j.)                                          |
| 3258 | Victorias sobre Freya (Ulduar 25 j.)                                           |
| 3259 | ¡Primero del reino! Defensor celestial                                         |
| 3296 | Cocinar con estilo                                                             |
| 3316 | Heraldo de los titanes                                                         |
| 3336 | Gladiador mortal                                                               |
| 3356 | Sable de Hielo de Cuna del Invierno                                            |
| 3357 | Ravasaurio pellejo venenoso                                                    |
| 3436 | Gladiador furioso                                                              |
| 3456 | Una fiesta de muerte                                                           |
| 3457 | El botín de la capitana                                                        |
| 3478 | Peregrino                                                                      |
| 3496 | Una montura de fiesta veloz                                                    |
| 3516 | Muertes en Ulduar                                                              |
| 3536 | El soldado marino                                                              |
| 3556 | Panza del peregrino                                                            |
| 3557 | Panza del peregrino                                                            |
| 3558 | Compartir es querer                                                            |
| 3559 | Acechapavos                                                                    |
| 3576 | Ahora estamos cocinando                                                        |
| 3577 | Ahora estamos cocinando                                                        |
| 3578 | Pavonator                                                                      |
| 3579 | \'\'¡GUERRA DE COMIDA!\'\'                                                     |
| 3580 | Riesgo del peregrino                                                           |
| 3581 | Riesgo del peregrino                                                           |
| 3582 | Hora del pavo de Terokkar                                                      |
| 3596 | Progreso del peregrino                                                         |
| 3597 | Progreso del peregrino                                                         |
| 3618 | Murkimus el Gladiador                                                          |
| 3636 | Tigre de jade                                                                  |
| 3656 | Peregrino                                                                      |
| 3676 | Confidente de plata                                                            |
| 3677 | Los Atracasol                                                                  |
| 3736 | ¡Arriba el poni!                                                               |
| 3756 | Vermis de escarcha de Gladiador furioso                                        |
| 3757 | Vermis de escarcha de Gladiador incansable                                     |
| 3758 | Gladiador incansable                                                           |
| 3776 | Victoria en la Isla de la Conquista                                            |
| 3777 | Veterano de la Isla de la Conquista                                            |
| 3778 | Prueba del Campeón                                                             |
| 3797 | Lumbago (10 j.)                                                                |
| 3798 | El temple lo arreglará (10 j.)                                                 |
| 3799 | Sal y pimienta (10 j.)                                                         |
| 3800 | El rey traidor (10 j.)                                                         |
| 3802 | Confesora Argenta                                                              |
| 3803 | El aplastacaras                                                                |
| 3804 | Podría ser peor                                                                |
| 3808 | Un tributo a la habilidad (10 j.)                                              |
| 3809 | Un tributo a la habilidad loca (10 j.)                                         |
| 3810 | Un tributo a la locura (10 j.)                                                 |
| 3812 | La Llamada de la Gran Cruzada (25 j.)                                          |
| 3813 | Lumbago (25 j.)                                                                |
| 3814 | El temple lo arreglará (25 j.)                                                 |
| 3815 | Sal y pimienta (25 j.)                                                         |
| 3816 | El rey traidor (25 j.)                                                         |
| 3817 | Un tributo a la habilidad (25 j.)                                              |
| 3818 | Un tributo a la habilidad loca (25 j.)                                         |
| 3819 | Un tributo a la locura (25 j.)                                                 |
| 3836 | Koralon el Vigía de las Llamas (10 j.)                                         |
| 3837 | Koralon el Vigía de las Llamas (25 j.)                                         |
| 3838 | Emblema de mazmorra y banda                                                    |
| 3839 | 25 emblemas de mazmorras y bandas                                              |
| 3840 | 50 emblemas de mazmorras y bandas                                              |
| 3841 | 100 emblemas de mazmorras y bandas                                             |
| 3842 | 250 emblemas de mazmorras y bandas                                             |
| 3843 | 500 emblemas de mazmorras y bandas                                             |
| 3844 | 1000 emblemas de mazmorras y bandas                                            |
| 3845 | Estrella de la Isla de la Conquista                                            |
| 3846 | Abundancia de recursos                                                         |
| 3847 | Garaje para cuatro                                                             |
| 3848 | A-bombi-nable                                                                  |
| 3849 | A-bombi-nación                                                                 |
| 3850 | Acribillados                                                                   |
| 3851 | Mío                                                                            |
| 3852 | Corta el cable azul... ¡No! ¡El rojo!                                          |
| 3853 | Por toda la isla                                                               |
| 3854 | Por la puerta trasera                                                          |
| 3855 | Tumba de guja                                                                  |
| 3856 | Derbi demoledor                                                                |
| 3857 | Maestro de la Isla de la Conquista                                             |
| 3876 | 1500 emblemas de mazmorras y bandas                                            |
| 3896 | Pantera de ónice                                                               |
| 3916 | La Llamada de la Cruzada (25 j.)                                               |
| 3917 | La Llamada de la Cruzada (10 j.)                                               |
| 3918 | La Llamada de la Gran Cruzada (10 j.)                                          |
| 3936 | No uno, sino dos jormungar (10 j.)                                             |
| 3937 | No uno, sino dos jormungar (25 j.)                                             |
| 3957 | Maestro de la Isla de la Conquista                                             |
| 3996 | 360 grados de púas de dolor (10 j.)                                            |
| 3997 | 360 grados de púas de dolor (25 j.)                                            |
| 4016 | Tierra, viento y fuego (10 j.)                                                 |
| 4017 | Tierra, viento y fuego (25 j.)                                                 |
| 4018 | Victorias sobre el Campeón cazador (Prueba del Campeón)                        |
| 4019 | Victorias sobre el Campeón cazador (Prueba del Campeón heroica)                |
| 4022 | Victorias sobre la confesora Argenta Cabelloclaro (Prueba del Campeón)         |
| 4023 | Victorias sobre la confesora Argenta Cabelloclaro (Prueba del Campeón heroica) |
| 4024 | Victorias sobre Eadric el Puro (Prueba del Campeón)                            |
| 4025 | Victorias sobre Eadric el Puro (Prueba del Campeón heroica)                    |
| 4026 | Muertes de El Caballero Negro (Prueba del Campeón)                             |
| 4027 | Muertes de El Caballero Negro (Prueba del Campeón heroica)                     |
| 4028 | Victorias sobre las bestias de Rasganorte (Prueba del Cruzado 10 j.)           |
| 4029 | Victorias sobre las bestias de Rasganorte (Prueba del Gran Cruzado 25 j.)      |
| 4030 | Victorias sobre las bestias de Rasganorte (Prueba del Gran Cruzado 10 j.)      |
| 4031 | Victorias sobre las bestias de Rasganorte (Prueba del Cruzado 25 j.)           |
| 4032 | Muertes de Lord Jaraxxus (Prueba del Cruzado 10 j.)                            |
| 4033 | Muertes de Lord Jaraxxus (Prueba del Gran Cruzado 10 j.)                       |
| 4034 | Muertes de Lord Jaraxxus (Prueba del Cruzado 25 j.)                            |
| 4035 | Muertes de Lord Jaraxxus (Prueba del Gran Cruzado 25 j.)                       |
| 4036 | Victorias sobre los campeones de la facción (Prueba del Cruzado 10 j.)         |
| 4037 | Victorias sobre los campeones de la facción (Prueba del Gran Cruzado 10 j.)    |
| 4038 | Victorias sobre los campeones de la facción (Prueba del Cruzado 25 j.)         |
| 4039 | Victorias sobre los campeones de la facción (Prueba del Gran Cruzado 25 j.)    |
| 4040 | Muertes de las Gemelas Val\'kyr (Prueba del Cruzado 10 j.)                     |
| 4041 | Muertes de las Gemelas Val\'kyr (Prueba del Gran Cruzado 10 j.)                |
| 4042 | Muertes de las Gemelas Val\'kyr (Prueba del Cruzado 25 j.)                     |
| 4043 | Muertes de las Gemelas Val\'kyr (Prueba del Gran Cruzado 25 j.)                |
| 4044 | Veces que has completado la Prueba del Cruzado (10 j.)                         |
| 4045 | Veces que has completado la Prueba del Gran Cruzado (10 j.)                    |
| 4046 | Veces que has completado la Prueba del Cruzado (25 j.)                         |
| 4047 | Veces que has completado la Prueba del Gran Cruzado (25 j.)                    |
| 4048 | Victorias sobre el Campeón mago (Prueba del Campeón)                           |
| 4049 | Victorias sobre el Campeón mago (Prueba del Campeón heroica)                   |
| 4050 | Victorias sobre el Campeón pícaro (Prueba del Campeón)                         |
| 4051 | Victorias sobre el Campeón pícaro (Prueba del Campeón heroica)                 |
| 4052 | Victorias sobre el Campeón chamán (Prueba del Campeón)                         |
| 4053 | Victorias sobre el Campeón chamán (Prueba del Campeón heroica)                 |
| 4054 | Victorias sobre el Campeón guerrero (Prueba del Campeón)                       |
| 4055 | Victorias sobre el Campeón guerrero (Prueba del Campeón heroica)               |
| 4074 | Muertes de Koralon el Vigía de las Llamas (Conquista del Invierno 10 j.)       |
| 4075 | Muertes de Koralon el Vigía de las Llamas (Conquista del Invierno 25 j.)       |
| 4078 | ¡Primero del reino! Gran Cruzado                                               |
| 4079 | Un tributo a la inmortalidad                                                   |
| 4080 | Un tributo a la locura entregada                                               |
| 4096 | Batallas en la Isla de la Conquista                                            |
| 4097 | Victorias en la Isla de la Conquista                                           |
| 4156 | Un tributo a la inmortalidad                                                   |
| 4176 | Abundancia de recursos                                                         |
| 4177 | Mío                                                                            |
| 4256 | Derbi demoledor                                                                |
| 4296 | Prueba del Campeón                                                             |
| 4297 | Heroico: Prueba del Campeón                                                    |
| 4298 | Heroico: Prueba del Campeón                                                    |
| 4316 | 2500 emblemas de mazmorras y bandas                                            |
| 4396 | Guarida de Onyxia (10 j.)                                                      |
| 4397 | Guarida de Onyxia (25 j.)                                                      |
| 4400 | 5º aniversario de WoW                                                          |
| 4402 | ¡Más daño! (10 j.)                                                             |
| 4403 | ¡Qué de vástagos! ¡Haz algo! (10 j.)                                           |
| 4404 | Su aliento ahora es más profundo (10 j.)                                       |
| 4405 | ¡Más daño! (25 j.)                                                             |
| 4406 | ¡Qué de vástagos! ¡Haz algo! (25 j.)                                           |
| 4407 | Su aliento ahora es más profundo (25 j.)                                       |
| 4436 | Rey del Rifle                                                                  |
| 4437 | Rey del Rifle                                                                  |
| 4456 | Mazmorras aleatorias (normales) de Lich King completadas                       |
| 4476 | Buscar más                                                                     |
| 4477 | Buscar mucho más                                                               |
| 4478 | Buscar muchísimo más                                                           |
| 4496 | ¡Toma, 9000 puntazos!                                                          |
| 4516 | La Forja de Almas                                                              |
| 4517 | El Foso de Saron                                                               |
| 4518 | Las Cámaras de Reflexión                                                       |
| 4519 | Heroico: La Forja de Almas                                                     |
| 4520 | Heroico: El Foso de Saron                                                      |
| 4521 | Heroico: Las Cámaras de Reflexión                                              |
| 4522 | Ay mi alma                                                                     |
| 4523 | Tres caras                                                                     |
| 4524 | Solo once campanadas                                                           |
| 4525 | No mires hacia arriba                                                          |
| 4526 | No nos retiramos: avanzamos en otra dirección                                  |
| 4527 | Las Cámaras de Alaescarcha (10 j.)                                             |
| 4528 | Los Talleres de la Peste (10 j.)                                               |
| 4529 | La Sala Carmesí (10 j.)                                                        |
| 4530 | El Trono Helado (10 j.)                                                        |
| 4531 | Asaltar la Ciudadela (10 j.)                                                   |
| 4532 | La caída del Rey Exánime (10 j.)                                               |
| 4534 | Deshuesado (10 j.)                                                             |
| 4535 | Full (10 j.)                                                                   |
| 4536 | Al pasar la barca (10 j.)                                                      |
| 4537 | Mira la que he montado (10 j.)                                                 |
| 4538 | Bailando con mocos (10 j.)                                                     |
| 4539 | Devórame otra vez (10 j.)                                                      |
| 4556 | Mazmorras aleatorias (heroicas) de Lich King completadas                       |
| 4576 | ¡Primero del reino! La caída del Rey Exánime                                   |
| 4577 | Sin vacunas (10 j.)                                                            |
| 4578 | Náuseas, acidez, indigestión (10 j.)                                           |
| 4579 | Sereno (10 j.)                                                                 |
| 4580 | Sacúdete (10 j.)                                                               |
| 4581 | Hasta arriba de espíritus malvados (10 j.)                                     |
| 4582 | El hombre que susurraba a los orbes (10 j.)                                    |
| 4583 | La perdición del Rey caído                                                     |
| 4584 | La Luz del Alba                                                                |
| 4585 | Toravon el Vigía de Hielo (10 j.)                                              |
| 4586 | Toravon el Vigía de Hielo (25 j.)                                              |
| 4596 | La Espada prometida                                                            |
| 4597 | El Trono Helado (25 j.)                                                        |
| 4598 | El Veredicto Cinéreo                                                           |
| 4599 | Gladiador colérico                                                             |
| 4600 | Vermis de escarcha de Gladiador colérico                                       |
| 4601 | Hemos estado esperando mucho tiempo (10 j.)                                    |
| 4602 | La gloria del asaltante de Corona de Hielo (10 j.)                             |
| 4603 | La gloria del asaltante de Corona de Hielo (25 j.)                             |
| 4604 | Asaltar la Ciudadela (25 j.)                                                   |
| 4605 | Los Talleres de la Peste (25 j.)                                               |
| 4606 | La Sala Carmesí (25 j.)                                                        |
| 4607 | Las Cámaras de Alaescarcha (25 j.)                                             |
| 4608 | La caída del Rey Exánime (25 j.)                                               |
| 4610 | Deshuesado (25 j.)                                                             |
| 4611 | Full (25 j.)                                                                   |
| 4612 | Al pasar la barca (25 j.)                                                      |
| 4613 | Mira la que he montado (25 j.)                                                 |
| 4614 | Bailando con mocos (25 j.)                                                     |
| 4615 | Sin vacunas (25 j.)                                                            |
| 4616 | Náuseas, acidez, indigestión (25 j.)                                           |
| 4617 | El hombre que susurraba a los orbes (25 j.)                                    |
| 4618 | Devórame otra vez (25 j.)                                                      |
| 4619 | Sereno (25 j.)                                                                 |
| 4620 | Sacúdete (25 j.)                                                               |
| 4621 | Hemos estado esperando mucho tiempo (25 j.)                                    |
| 4622 | Hasta arriba de espíritus malvados (25 j.)                                     |
| 4623 | Agonía de Sombras                                                              |
| 4624 | El amor duele                                                                  |
| 4625 | Riendas de Invencible                                                          |
| 4626 | ¡Yo pongo la cabeza!                                                           |
| 4627 | Gran cohete de amor                                                            |
| 4628 | Heroico: Asaltar la Ciudadela (10 j.)                                          |
| 4629 | Heroico: Los Talleres de la Peste (10 j.)                                      |
| 4630 | Heroico: La Sala Carmesí (10 j.)                                               |
| 4631 | Heroico: Las Cámaras de Alaescarcha (10 j.)                                    |
| 4632 | Heroico: Asaltar la Ciudadela (25 j.)                                          |
| 4633 | Heroico: Los Talleres de la Peste (25 j.)                                      |
| 4634 | Heroico: La Sala Carmesí (25 j.)                                               |
| 4635 | Heroico: Las Cámaras de Alaescarcha (25 j.)                                    |
| 4636 | Heroico: La Caída del Rey Exánime (10 j.)                                      |
| 4637 | Heroico: La Caída del Rey Exánime (25 j.)                                      |
| 4639 | Muertes de Lord Tuétano (Corona de Hielo 10 j.)                                |
| 4640 | Muertes de Lord Tuétano (Corona de Hielo heroica 10 j.)                        |
| 4641 | Muertes de Lord Tuétano (Corona de Hielo 25 j.)                                |
| 4642 | Muertes de Lord Tuétano (Corona de Hielo heroica 25 j.)                        |
| 4643 | Muertes de Lady Susurramuerte (Corona de Hielo 10 j.)                          |
| 4644 | Victorias en la Batalla de naves de guerra (Corona de Hielo 10 j.)             |
| 4645 | Muertes de El Libramorte (Corona de Hielo 10 j.)                               |
| 4646 | Muertes de Panzachancro (Corona de Hielo 10 j.)                                |
| 4647 | Muertes de Carapútrea (Corona de Hielo 10 j.)                                  |
| 4648 | Muertes del Consejo de Príncipes de Sangre (Corona de Hielo 10 j.)             |
| 4649 | Rescates de Valithria Caminasueños (Corona de Hielo 10 j.)                     |
| 4650 | Muertes del profesor Putricidio (Corona de Hielo 10 j.)                        |
| 4651 | Muertes de la Reina de Sangre Lana\'thel (Corona de Hielo 10 j.)               |
| 4652 | Muertes de Sindragosa (Corona de Hielo 10 j.)                                  |
| 4653 | Victorias sobre el Rey Exánime (Corona de Hielo 10 j.)                         |
| 4654 | Muertes de Lady Susurramuerte (Corona de Hielo heroica 10 j.)                  |
| 4655 | Muertes de Lady Susurramuerte (Corona de Hielo 25 j.)                          |
| 4656 | Muertes de Lady Susurramuerte (Corona de Hielo heroica 25 j.)                  |
| 4657 | Muertes de Toravon el Vigía de Hielo (Conquista del Invierno 10 j.)            |
| 4658 | Muertes de Toravon el Vigía de Hielo (Conquista del Invierno 25 j.)            |
| 4659 | Victorias en la Batalla de naves de guerra (Corona de Hielo heroica 10 j.)     |
| 4660 | Victorias en la Batalla de naves de guerra (Corona de Hielo 25 j.)             |
| 4661 | Victorias en la Batalla de naves de guerra (Corona de Hielo heroica 25 j.)     |
| 4662 | Muertes de El Libramorte (Corona de Hielo heroica 10 j.)                       |
| 4663 | Muertes de El Libramorte (Corona de Hielo 25 j.)                               |
| 4664 | Muertes de El Libramorte (Corona de Hielo heroica 25 j.)                       |
| 4665 | Muertes de Panzachancro (Corona de Hielo heroica 10 j.)                        |
| 4666 | Muertes de Panzachancro (Corona de Hielo 25 j.)                                |
| 4667 | Muertes de Panzachancro (Corona de Hielo heroica 25 j.)                        |
| 4668 | Muertes de Carapútrea (Corona de Hielo heroica 10 j.)                          |
| 4669 | Muertes de Carapútrea (Corona de Hielo 25 j.)                                  |
| 4670 | Muertes de Carapútrea (Corona de Hielo heroica 25 j.)                          |
| 4671 | Muertes del Consejo de Príncipes de Sangre (Corona de Hielo heroica 10 j.)     |
| 4672 | Muertes del Consejo de Príncipes de Sangre (Corona de Hielo 25 j.)             |
| 4673 | Muertes del Consejo de Príncipes de Sangre (Corona de Hielo heroica 25 j.)     |
| 4674 | Rescates de Valithria Caminasueños (Corona de Hielo heroica 10 j.)             |
| 4675 | Rescates de Valithria Caminasueños (Corona de Hielo 25 j.)                     |
| 4676 | Rescates de Valithria Caminasueños (Corona de Hielo heroica 25 j.)             |
| 4677 | Muertes del profesor Putricidio (Corona de Hielo heroica 10 j.)                |
| 4678 | Muertes del profesor Putricidio (Corona de Hielo 25 j.)                        |
| 4679 | Muertes del profesor Putricidio (Corona de Hielo heroica 25 j.)                |
| 4680 | Muertes de la Reina de Sangre Lana\'thel (Corona de Hielo heroica 10 j.)       |
| 4681 | Muertes de la Reina de Sangre Lana\'thel (Corona de Hielo 25 j.)               |
| 4682 | Muertes de la Reina de Sangre Lana\'thel (Corona de Hielo heroica 25 j.)       |
| 4683 | Muertes de Sindragosa (Corona de Hielo 25 j.)                                  |
| 4684 | Muertes de Sindragosa (Corona de Hielo heroica 10 j.)                          |
| 4685 | Muertes de Sindragosa (Corona de Hielo heroica 25 j.)                          |
| 4686 | Victorias sobre el Rey Exánime (Corona de Hielo heroica 10 j.)                 |
| 4687 | Victorias sobre el Rey Exánime (Corona de Hielo 25 j.)                         |
| 4688 | Victorias sobre el Rey Exánime (Corona de Hielo heroica 25 j.)                 |
| 4713 | Muertes de Bronjahm (La Forja de Almas)                                        |
| 4714 | Muertes de Bronjahm (La Forja de Almas heroica)                                |
| 4715 | Muertes de Devoraalmas (La Forja de Almas)                                     |
| 4716 | Muertes de Devoraalmas (La Forja de Almas heroica)                             |
| 4717 | Muertes del maestro de forja Gargelus (Foso de Saron)                          |
| 4718 | Muertes de Agh y Puagh (Foso de Saron)                                         |
| 4719 | Muertes de Agh y Puagh (Foso de Saron heroico)                                 |
| 4720 | Muertes del Señor de la Plaga Tyrannus (Foso de Saron)                         |
| 4721 | Muertes del Señor de la Plaga Tyrannus (Foso de Saron heroico)                 |
| 4722 | Muertes de Falric (Cámaras de Reflexión)                                       |
| 4723 | Muertes de Falric (Cámaras de Reflexión heroica)                               |
| 4724 | Muertes de Marwyn (Cámaras de Reflexión)                                       |
| 4725 | Muertes de Marwyn (Cámaras de Reflexión heroica)                               |
| 4726 | Huidas del Rey Exánime (Cámaras de Reflexión)                                  |
| 4727 | Huidas del Rey Exánime (Cámaras de Reflexión heroica)                          |
| 4728 | Muertes del maestro de forja Gargelus (Foso de Saron heroico)                  |
| 4729 | Emblemas de triunfo adquiridos                                                 |
| 4730 | Emblemas de escarcha adquiridos                                                |
| 4777 | Golpes de gracia en la Isla de la Conquista                                    |
| 4778 | Tiros por desencantar para el botín                                            |
| 4779 | Muertes con honor en la Isla de la Conquista                                   |
| 4780 | Muertes en la Prueba del Cruzado                                               |
| 4781 | Muertes en la Ciudadela de la Corona de Hielo                                  |
| 4782 | Jarra de la Fiesta de la cerveza verde                                         |
| 4784 | Emblemático                                                                    |
| 4785 | Emblemático                                                                    |
| 4786 | Operación: Gnomeregan                                                          |
| 4790 | Caída de Zalazane                                                              |
| 4815 | El Destructor del Crepúsculo (25 j.)                                           |
| 4816 | Heroico: El Destructor del Crepúsculo (25 j.)                                  |
| 4817 | El Destructor del Crepúsculo (10 j.)                                           |
| 4818 | Heroico: El Destructor del Crepúsculo (10 j.)                                  |
| 4820 | Muertes de Halion (El Sagrario Rubí 25 j.)                                     |
| 4821 | Muertes de Halion (El Sagrario Rubí 10 j.)                                     |
| 4822 | Muertes de Halion (El Sagrario Rubí heroica 10 j.)                             |
| 4823 | Muertes de Halion (El Sagrario Rubí heroica 25 j.)                             |
| 4824 | Edición de coleccionista: Mini thor                                            |
