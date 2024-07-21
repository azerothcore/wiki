# characters 

[<-Volver a:Characters](database-characters)

**Tabla \`characters\`**

La tabla contiene información estática vital para cada personaje. Su función radica en crear los objetos respectivos del jugador dentro del propio juego.

**Estructura**

| Field                      | Type         | Attributes | Key | Null | Default           | Extra  | Comment                  |
| -------------------------- | ------------ | ---------- | --- | ---- | ----------------- | ------ | ------------------------ |
| [guid][1]                  | INT          | UNSIGNED   | PRI | NO   | 0                 | Unique | Global Unique Identifier |
| [account][2]               | INT          | UNSIGNED   |     | NO   | 0                 |        | Account Identifier       |
| [name][3]                  | VARCHAR(12)  | SIGNED     |     | NO   |                   |        |                          |
| [race][4]                  | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [class][5]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [gender][6]                | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [level][7]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [xp][8]                    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [money][9]                 | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [skin][10]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [face][11]                 | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [hairStyle][12]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [hairColor][13]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [facialStyle][14]          | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [bankSlots][15]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [restState][16]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [playerflags][17]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [position_x][18]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [position_y][19]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [position_z][20]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [map][21]                  | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        | Map Identifier           |
| [instance_id][22]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [instance_mode_mask][23]   | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [orientation][24]          | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [taximask][25]             | TEXT         | SIGNED     |     | NO   |                   |        |                          |
| [online][26]               | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [cinematic][27]            | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totaltime][28]            | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [leveltime][29]            | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [logout_time][30]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [is_logout_resting][31]    | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [rest_bonus][32]           | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [resettalents_cost][33]    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [resettalents_time][34]    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [trans_x][35]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_y][36]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_z][37]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [trans_o][38]              | FLOAT        | SIGNED     |     | NO   | 0                 |        |                          |
| [transguid][39]            | MEDIUMINT    | SIGNED     |     | NO   | 0                 |        |                          |
| [extra_flags][40]          | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [stable_slots][41]         | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [at_login][42]             | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [zone][43]                 | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [death_expire_time][44]    | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [taxi_path][45]            | TEXT         | SIGNED     |     | YES  |                   |        |                          |
| [arenaPoints][46]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totalHonorPoints][47]     | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [todayHonorPoints][48]     | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [yesterdayHonorPoints][49] | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [totalKills][50]           | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [todayKills][51]           | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [yesterdayKills][52]       | SMALLINT     | UNSIGNED   |     | NO   | 0                 |        |                          |
| [chosenTitle][53]          | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [knownCurrencies][54]      | BIGINT       | UNSIGNED   |     | NO   | 0                 |        |                          |
| [watchedFaction][55]       | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [drunk][56]                | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [health][57]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power1][58]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power2][59]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power3][60]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power4][61]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power5][62]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power6][63]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [power7][64]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [latency][65]              | MEDIUMINT    | UNSIGNED   |     | NO   | 0                 |        |                          |
| [talentGroupsCount][66]    | TINYINT      | UNSIGNED   |     | NO   | 1                 |        |                          |
| [activeTalentGroup][67]    | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [exploredZones][68]        | LONGTEXT     | SIGNED     |     | YES  |                   |        |                          |
| [equipmentCache][69]       | LONGTEXT     | SIGNED     |     | YES  |                   |        |                          |
| [ammoId][70]               | INT          | UNSIGNED   |     | NO   | 0                 |        |                          |
| [knownTitles][71]          | LONGTEXT     | SIGNED     |     | YES  |                   |        |                          |
| [actionBars][72]           | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [grantableLevels][73]      | TINYINT      | UNSIGNED   |     | NO   | 0                 |        |                          |
| [order][74]                | TINYINT      | SIGNED     |     | YES  |                   |        |                          |
| [creation_date][75]        | TIMESTAMP    | SIGNED     |     | NO   | CURRENT_TIMESTAMP |        |                          |
| [deleteInfos_Account][76]  | INT          | UNSIGNED   |     | YES  |                   |        |                          |
| [deleteInfos_Name][77]     | VARCHAR(12)  | SIGNED     |     | YES  |                   |        |                          |
| [deleteDate][78]           | INT          | UNSIGNED   |     | YES  |                   |        |                          |
  
[1]: #guid
[2]: #account
[3]: #name
[4]: #race
[5]: #class
[6]: #gender
[7]: #level
[8]: #xp
[9]: #money
[10]: #skin
[11]: #face
[12]: #hairstyle
[13]: #haircolor
[14]: #facialstyle
[15]: #bankslots
[16]: #reststate
[17]: #playerflags
[18]: #positionx
[19]: #positiony
[20]: #positionz
[21]: #map
[22]: #instanceid
[23]: #instancemodemask
[24]: #orientation
[25]: #taximask
[26]: #online
[27]: #cinematic
[28]: #totaltime
[29]: #leveltime
[30]: #logouttime
[31]: #islogoutresting
[32]: #restbonus
[33]: #resettalentscost
[34]: #resettalentstime
[35]: #transx
[36]: #transy
[37]: #transz
[38]: #transo
[39]: #transguid
[40]: #extraflags
[41]: #stableslots
[42]: #atlogin
[43]: #zone
[44]: #deathexpiretime
[45]: #taxipath
[46]: #arenaPoints
[47]: #totalhonorpoints
[48]: #todayhonorpoints
[49]: #yesterdayhonorpoints
[50]: #totalkills
[51]: #todaykills
[52]: #yesterdayKills
[53]: #chosentitle
[54]: #knowncurrencies
[55]: #watchedfaction
[56]: #drunk
[57]: #health
[58]: #power
[59]: #power
[60]: #power
[61]: #power
[62]: #power
[63]: #power
[64]: #power
[65]: #latency
[66]: #talentgroupscount
[67]: #activetalentgroup
[68]: #exploredzones
[69]: #equipmentcache
[70]: #ammoid
[71]: #knownTitles
[72]: #actionbars
[73]: #grantablelevels
[74]: #order
[75]: #creationdate
[76]: #deleteinfosaccount
[77]: #deleteinfosname
[78]: #deletedate

**Descripción de los Campos**

### guid

Globally Unique Identifier o Identificador Global Único del personaje. Este número debe de ser único, ya que es la mejor manera de identificar personajes por separado.

### account

El ID de la cuenta en la que reside este personaje. Véase [account.id](account#id) en la Base de Datos Auth.

### name

El nombre del personaje. La longitud máxima es de 12 caracteres.

### race

La raza del personaje. Véase [ChrRaces.dbc](chrraces).

### class

La clase del personaje. Véase [ChrClasses.dbc](chrclasses).

### gender

El género del personaje

| ID | Género           |
| -- | ---------------- |
| 0  | Masculino        |
| 1  | Femenino         |
| 2  | Desconocido (?)  |

El número `2` puede verse en la tabla [creature\_model\_info](creature_model_info) en particular.

### level

El nivel actual del personaje.

### xp

La cantidad de experiencia que éste personaje ha ganado para el siguiente nivel.

### money

La cantidad de cobre que el personaje posée ( Téngase en cuenta que todo el dinero que se tiene dentro del juego se mide en monedas de cobre )

### skin

Contiene datos acerca del color de la piel del personaje.
skinColor = playerbytes % 256

### face

Contiene datos acerca del estilo facial del personaje.
faceStyle = (playerbytes &gt;&gt; 8) % 256

### hairStyle

Contiene datos acerca del estilo del cabello del personaje.
hairStyle = (playerbytes &gt;&gt; 16) % 256

### hairColor

Contiene datos acerca del color del cabello del personaje.
hairColor = (playerbytes &gt;&gt; 24) % 256

### facialStyle

Contiene datos acerca del vello facial del personaje.
facialHair = playerBytes2 % 256

### bankSlots

Cantidad de casillas en el banco.

### restState

Estado de reposo.

### playerFlags

Una 'Máscara de Bits/Tabla de Bits' o BitMask que representan aquellos marcadores que posée el jugador. Cada bit controla un marcador distinto, y para combinar marcadores puedes sumar cada marcador que desées uno por uno, activando en efecto los respectivos bits.

| Flag     |            | Name                          | Comment                                                                                                                     |
| -------- | ---------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| 1        | 0x00000001 | PLAYER_FLAGS_GROUP_LEADER     |                                                                                                                             |
| 2        | 0x00000002 | PLAYER_FLAGS_AFK              |                                                                                                                             |
| 4        | 0x00000004 | PLAYER_FLAGS_DND              |                                                                                                                             |
| 8        | 0x00000008 | PLAYER_FLAGS_GM               |                                                                                                                             |
| 16       | 0x00000010 | PLAYER_FLAGS_GHOST            |                                                                                                                             |
| 32       | 0x00000020 | PLAYER_FLAGS_RESTING          |                                                                                                                             |
| 64       | 0x00000040 | PLAYER_FLAGS_UNK7             |                                                                                                                             |
| 128      | 0x00000080 | PLAYER_FLAGS_UNK8             | Marcador pre-3.0.3 PLAYER_FLAGS_FFA_PVP para el estado FFA PVP (FreeForAll o Todos contra Todos )                           |
| 256      | 0x00000100 | PLAYER_FLAGS_CONTESTED_PVP    | El jugador se ha visto envuelto en un combate PvP y será atacado por guardias de la Zona en Disputa respectiva              |
| 512      | 0x00000200 | PLAYER_FLAGS_IN_PVP           |                                                                                                                             |
| 1024     | 0x00000400 | PLAYER_FLAGS_HIDE_HELM        |                                                                                                                             |
| 2048     | 0x00000800 | PLAYER_FLAGS_HIDE_CLOAK       |                                                                                                                             |
| 4096     | 0x00001000 | PLAYER_FLAGS_PLAYED_LONG_TIME | Jugó mucho tiempo                                                                                                           |
| 8192     | 0x00002000 | PLAYER_FLAGS_TOO_LONG         | Jugó demasiado tiempo                                                                                                       |
| 16384    | 0x00004000 | PLAYER_FLAGS_IS_OUT_OF_BOUNDS |                                                                                                                             |
| 32768    | 0x00008000 | PLAYER_FLAGS_DEVELOPER        | ¿prefijo para algo?                                                                                                         |
| 65536    | 0x00010000 | PLAYER_FLAGS_UNK17            | Marcador pre-3.0.3 PLAYER_FLAGS_SANCTUARY para el jugador que entró a un santuario                                          |
| 131072   | 0x00020000 | PLAYER_FLAGS_TAXI_BENCHMARK   | Modo prueba de rendimiento de transporte (taxi) (on/off) (2.0.1)                                                            |
| 262144   | 0x00040000 | PLAYER_FLAGS_PVP_TIMER        | 3.0.2, temporizador de pvp activo (luego de desactivar el pvp manualmente)                                                  |
| 524288   | 0x00080000 | PLAYER_FLAGS_UNK20            |                                                                                                                             |
| 1048576  | 0x00100000 | PLAYER_FLAGS_UNK21            |                                                                                                                             |
| 2097152  | 0x00200000 | PLAYER_FLAGS_UNK22            |                                                                                                                             |
| 4194304  | 0x00400000 | PLAYER_FLAGS_COMMENTATOR2     |                                                                                                                             |
| 8388608  | 0x00800000 | PLAYER_ALLOW_ONLY_ABILITY     | Usado para Filotormenta (guerrero) y Asesinato múltiple (pícaro)                                                            |
| 16777216 | 0x01000000 | PLAYER_FLAGS_UNK25            | Desactiva todas las habilidades cuerpo a cuerpo en el teclado incluyendo Ataque Automático                                  |
| 33554432 | 0x02000000 | PLAYER_FLAGS_NO_XP_GAIN       |                                                                                                                             |

### position\_x

Posición cartesiana en X en la que se encuentra ubicado el personaje.

### position\_y

Posición cartesiana en Y en la que se encuentra ubicado el personaje.

### position\_z

Posición cartesiana en Z en la que se encuentra ubicado el personaje.

### map

ID del mapa en el que se encuentra el personaje.

### instance\_id

ID de la instancia en la que se encuentra el personaje y a la que está vinculado.

### instance\_mode\_mask

La dificultad actual de la mazmorra en la que se encuentra el jugador. Este campo es una Máscara/Tabla de bits. Los valores son asignados juntos, sin embargo, sólo dos de los cuatro deben ser usados a la vez. Cabe recalcar que ésta descripción puede no ser ciento por ciento correcta.

| Flag | Comment       |
| ---- | ------------- |
| 0    | Normal        |
| 1    | Heróico       |
| 16   | 10 Jugadores  |
| 32   | 25 Jugadores  |

### orientation

Orientación del personaje. (Norte = 0,0, Sur = 3,14159)

### taximask

TaxiNodes/rutas de vuelo conocidas separadas con espacio.

### online

Registra si el personaje está conectado (1) o desconectado (0).

### cinematic

Booleano del 0 al 1 que controla si la cinemática de inicio ha sido mostrada al jugador o no.

### totaltime

Tiempo total de juego del personaje desde que ha estado activo en el mundo, medido en segundos.

### leveltime

Tiempo total de juego en el cual el personaje ha estado inmerso desde el nivel actual, medido en segundos.

### logout\_time

Hora en la cual el personaje se desconectó por última vez, medida en tiempo Unix.

### is\_logout\_resting

Booleano del 0 al 1 que controla si el personaje está actualmente en una zona de descanso o no.

### rest_bonus

Bonificación acumulada de la tasa de descanso a la hora de ganar experiencia.

### resettalents\_cost

El coste para restablecer los talentos del personaje, medido en monedas de cobre.

### resettalents\_time

Cantidad de veces en las que se han restablecido los talentos del personaje.

### trans\_x

Posición cartesiana en X del transporte en el que se encontraba el personaje desde la última vez que se guardó.

### trans\_y

Posición cartesiana en Y del transporte en el que se encontraba el personaje desde la última vez que se guardó.

### trans\_z

Posición cartesiana en Z del transporte en el que se encontraba el personaje desde la última vez que se guardó.

### trans\_o

La orientación del transporte en el que se encontraba el personaje la última vez que se guardó.

### transguid

Globally Unique Identifier o Identificador Único global del transporte en el que se encontraba el personaje cuando fue guardado por última vez.

### extra\_flags

Éstos Marcadores o 'flags' controlan ciertos atributos específicos del jugador, en su mayoría características del GM.

| Flag |            | Name                           | Description                                                                               |
| ---- | ---------- | ------------------------------ | ----------------------------------------------------------------------------------------- |
| 1    | 0x00000001 | PLAYER_EXTRA_GM_ON             | Define el estado del GM                                                                   |
| 2    | 0x00000002 | PLAYER_EXTRA_GM_ACCEPT_TICKETS | EN DESUSO Define si el personaje acepta tickets                                           |
| 4    | 0x00000004 | PLAYER_EXTRA_ACCEPT_WHISPERS   | Define si acepta susurros                                                                 |
| 8    | 0x00000008 | PLAYER_EXTRA_TAXICHEAT         | Establece un TaxiCheat                                                                    |
| 16   | 0x00000010 | PLAYER_EXTRA_GM_INVISIBLE      | Define la visibilidad del GM                                                              |
| 32   | 0x00000020 | PLAYER_EXTRA_GM_CHAT           | Muestra el ícono del GM en los mensajes del chat                                          |
| 64   | 0x00000040 | PLAYER_EXTRA_HAS_310_FLYER     | Marca si el jugador ya tiene una montura voladora de 310% de velocidad                    |
| 256  | 0x00000100 | PLAYER_EXTRA_PVP_DEATH         | Almacena el estado de muerte en CjC (PvP) hasta la creación del cadáver dentro del juego  |

### stable\_slots

Las ranuras disponibles (compradas) en el Maestro de Establo.

### at\_login

Este campo es una Máscara/Tabla de Bits, cuya función es controlar las diferentes acciones que se llevan a cabo una vez que el jugador inicie sesión con el personaje.

| Flag |      | Name                       | Description                                               |
| ---- | ---- | -------------------------- | --------------------------------------------------------- |
| 1    | 0x01 | AT_LOGIN_RENAME            | Forzar el cambio de nombre del personaje                  |
| 2    | 0x02 | AT_LOGIN_RESET_SPELLS      | Restablecer los hechizos (también las profesiones)        |
| 4    | 0x04 | AT_LOGIN_RESET_TALENTS     | Restablecer los talentos                                  |
| 8    | 0x08 | AT_LOGIN_CUSTOMIZE         | Personalizar el personaje                                 |
| 16   | 0x10 | AT_LOGIN_RESET_PET_TALENTS | Restablecer los talentos de la mascota                    |
| 32   | 0x20 | AT_LOGIN_FIRST             | Fijar y remover después del primer inicio de sesión       |
| 64   | 0x40 | AT_LOGIN_CHANGE_FACTION    | Cambiar de facción                                        |
| 128  | 0x80 | AT_LOGIN_CHANGE_RACE       | Cambiar de raza                                           |

Para crear acciones múltiples en esta casila, sume los valores entre sí.

### zone

ID de la zona en la que se encuentra el personaje.

### death\_expire\_time

Tiempo en el cual el personaje del jugador puede ser resucitado en caso de caída del servidor o salida del cliente mientras está en forma fantasmal, medido en tiempo Unix.

### taxi\_path

Almacena la ruta del taxi actual del personaje ([TaxiPath.dbc](TaxiPath)) si el jugador se desconecta mientras se encuentre en uno.

### arenaPoints

La cantidad de puntos de arena acumuldados por el personaje del jugador, y también aquellos que recibirá la próxima vez que se distribuyan los puntos de arena.

### totalHonorPoints

La cantidad de puntos de honor que tiene este personaje.

### todayHonorPoints

La cantidad de puntos de honor que el personaje obtuvo hoy.

### yesterdayHonorPoints

La cantidad de puntos de honor que el personaje obtuvo ayer.

### totalKills

La cantidad de jugadores que el personaje ha matado.

### todayKills

La cantidad de jugadores que el personaje mató hoy.

### yesterdayKills

La cantidad de jugadores que el personaje mató ayer.

### chosenTitle

Título actual, utilizando el campo bit_index (En orden de juego o InGameOrder dentro de [CharTitles.dbc](CharTitles)).

### knownCurrencies

Monedas/distintivos/insignias conocidas (Aquello que debe figurar en la pestaña Monedas), Máscara/Tabla de bits (sumatoria de Marcadores o 'flags) de BitIndexes, véase [CurrencyTypes.dbc](CurrencyTypes).

### watchedFaction

Seguimiento de una facción en la barra de experiencia (utilizando el ID de la reputación, véase [Faction.dbc](faction)).

### drunk

Estado de embriaguez del personaje, 0-100

-   0 = Sobrio
-   1-49 = Prendido
-   50-89 = Borracho
-   90-100 = Destrozado (El exceso de alcohol es malo para la salud, esto va para quien lo lea XD)

### health

Estado de salud actual del personaje.

### power

Poder actual del personaje (Desde el momento en el que se guardó el personaje).

| Field  | Power name   |
| ------ | ------------ |
| power1 | Maná         |
| power2 | ira          |
| power3 | Focus        |
| power4 | Energía      |
| power5 | Felicidad    |
| power6 | Runas        |
| power7 | Poder rúnico |

(Recordemos que son 7 columnas, dependiendo del poder que esté utilizando su clase estará almacemado el valor del mismo en la respectiva casilla)

### latency

Latencia del personaje o ping en milisegundos, a partir del último autoguardado.

### talentGroupsCount

El número de especializaciones a las que tiene acceso este personaje. El valor por defecto es 1. El valor máximo actualmente soportado es 2. Nunca debe de ser 0 (Esto es signo de un personaje creado antes de la implementación del la doble especialización de talentos).

### activeTalentGroup

Las especializaciones actuales habilitadas para este personaje, spec = 0 es la primera especialización, spec = 1 es la segunda especialización.

### exploredZones

Máscara/Tabla de bits para las zonas exploradas (1 bit para las exploradas, 0 bit para las no exploradas).

### equipmentCache

Equipamiento del personaje y alijo de la bolsa. 

### ammoId

[ID](item_template#entry) del Item de la munición.

### knownTitles

Contiene datos acerca de los títulos conocidos por el jugador almacenados en enteros de 6 x 16bit. Para calcular dónde se encuentra un título conocido en alguno de éstos 6 enteros se hace lo siguiente: Seleccionamos uno de los títulos en [CharTitles.dbc](CharTitles), a continuación tomamos el título de Archimago por ejemplo:

| TitleID | UnkRef? | MaleTitle   | FemaleTitle | InGameOrder |
| ------- | ------- | ----------- | ----------- | ----------- |
| 93      | 0       | Archmage %s | Archmage %s | 61          |

Usamos el InGameOrder (orden de juego) para calcular en cuál de los 6 enteros (16bit) está el título almacenado:

```
InGameOrder / 32 = X
61 / 32 = **1,90625** (1 - **¡No** redondee el valor!)
```

Por lo que el primer entero almacena el título. Ya que el conteo comienza de **0** a 5, sería "0 **TITLE_BIT** 0 0 0 0".

Ahora, ¿Qué bit almacena el título? Usamos el módulo para calcularlo.

```
InGameOrder Modulo 32 = X
61 Mod 32 = **29**
```
Por lo que el 29bit almacena el título. Esto sería 2 ^ 29 = 536870912. Este bit almacena el título de Archimago. Esto significaría que si **sólo tú** tienes el título de Archimago, characters.knownTitles sería "0 536870912 0 0 0 0".

### actionBars

Una Máscara/Tabla de bits que contiene las barras de acción visibles para el jugador.

| Flag |            | Comment                   |
| ---- | ---------- | ------------------------- |
| 1    | 0x00000001 | Barra inferior izquierda  |
| 2    | 0x00000002 | Barra inferior derecha    |
| 4    | 0x00000004 | Barra derecha             |
| 8    | 0x00000008 | Barra derecha 2           |

### grantableLevels

Casilla de Reclutar a un Amigo.

### order

Campo utilizado para cambiar el órden en el que aparecen los personajes de la pantalla de selección de personajes. Éste campo es utilizado primero, y luego [characters.guid](characters#guid), lo que significa que si ésta columna apunta a NULL para cada personaje de una cuenta, se ordenarán [characters.guid](characters#guid) por defecto.

### creation\_date

Fecha y hora de la creación del personaje. Formato AAA-MM-DD HH:MM:SS según la hora del servidor.

### deleteInfos\_Account

Almacena la ID de la cuenta si el personaje es eliminado y CharDelete.Method en worldserver.conf se establece en 1.

### deleteInfos\_Name

Almacena el nombre del personaje si éste es eliminado y CharDelete.Method en worldserver.conf se establece en 1.

### deleteDate

Almacena la fecha en que el personaje fue eliminado y CharDelete.Method en worldserver.conf.dist se establece en 1. Será comprobado por worldserver dentro de CharDelete.KeepDays en worldserver.conf.dist o worldserver.conf Si este valor es menor que deleteDate + CharDelete.KeepDays el personaje será purgado.
