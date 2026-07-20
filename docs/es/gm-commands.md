---
redirect_from: "/GM-Commands"
---

# Comandos GM

Los comandos GM se pueden introducir principalmente de 2 formas. O bien escribiéndolos directamente en la ventana de la consola del world. En la ventana de la consola del world el punto inicial (.) no es obligatorio, pero puedes usarlo. La otra forma es usar el comando gm dentro del juego en la consola de chat del cliente de wow. Allí, todos los comandos deben empezar con un punto inicial, p. ej.: .gm on

Nota: algunos comandos solo funcionan seleccionando a un jugador o a una creature. Estos comandos no se pueden usar en la consola del world.

Algunos comandos requieren un nivel de seguridad más alto. Para concederlo necesitas usar el comando `account set gmlevel` a través de la consola.

| Command | Security | Syntax | Description |
| --- | --- | --- | --- |
| account addon | 1 | `.account addon #addon` | Establece el nivel de expansión (addon) permitido. Valores de addon: 0 - normal, 1 - tbc, 2 - wotlk. |
| account 2fa | 0 | `.account 2fa <setup/remove>` | Escribe .account 2fa para ver la lista de posibles subcomandos o .help account 2fa $subcommand para ver información sobre los subcomandos. |
| account 2fa setup | 0 | `.account 2fa setup` | Configura la autenticación 2fa. Usa .account 2fa setup 1 para recibir el token. Aplica el token en la app de autenticación (sensible a mayúsculas/minúsculas). Usa el pin de la app con .account 2fa setup PIN para confirmar la configuración. |
| account 2fa remove | 0 | `.account 2fa remove` | Elimina la autenticación 2fa. |
| account create | 4 | `.account create $account $password [$email]` | Crea una cuenta y le establece una contraseña, con el email como valor opcional. |
| account delete | 4 | `.account delete $account` | Elimina la cuenta con todos los personajes. |
| account flag | 2 | `.account flag $subcommand` | Escribe .account flag para ver la lista de posibles subcomandos o .help account flag $subcommand para ver información sobre los subcomandos. |
| account flag list | 2 | `.account flag list [$account]` | Lista todos los AccountFlag actualmente establecidos en $account. Por defecto muestra tu propia cuenta si no se proporciona ningún argumento. |
| account flag add | 3 | `.account flag add $account $flag` | Establece un AccountFlag en $account. $flag es un nombre simbólico en su forma completa (p. ej. ACCOUNT_FLAG_TRIAL) o forma corta (p. ej. TRIAL). ACCOUNT_FLAG_GM se gestiona automáticamente y no puede modificarse manualmente. |
| account flag remove | 3 | `.account flag remove $account $flag` | Elimina un AccountFlag de $account. $flag es un nombre simbólico en su forma completa (p. ej. ACCOUNT_FLAG_TRIAL) o forma corta (p. ej. TRIAL). ACCOUNT_FLAG_GM se gestiona automáticamente y no puede modificarse manualmente. |
| account lock country | 0 | `.account lock country [on/off]` | Permite el login a la cuenta solo desde el país usado actualmente o elimina este requisito. |
| account lock ip | 0 | `.account lock ip [on/off]` | Permite el login a la cuenta solo desde la IP usada actualmente o elimina este requisito. |
| account lock | 0 | `.account lock [on/off]` | Permite el login a la cuenta solo desde la IP usada actualmente o elimina este requisito. |
| account onlinelist | 4 | `.account onlinelist` | Muestra la lista de cuentas online. |
| account password | 0 | `.account password $old_password $new_password $new_password` | Cambia la contraseña de tu cuenta. |
| account remove country | 3 | `.account remove country <account>` | Elimina la información de país asociada a la cuenta especificada. |
| account set 2fa | 0 | `.account set 2fa <account> <secret/off>` | Proporciona un secreto codificado en base32 para configurar la autenticación de dos factores para la cuenta. Especifica 'off' para desactivar la autenticación de dos factores para la cuenta. |
| account set addon | 2 | `.account set addon [$account] #addon` | Establece el nivel de expansión (addon) permitido para el usuario (posiblemente seleccionado). Valores de addon: 0 - normal, 1 - tbc, 2 - wotlk. |
| account set gmlevel | 4 | `.account set gmlevel [$account] #level [#realmid]` | Establece el nivel de seguridad para el jugador seleccionado (no se puede usar sobre uno mismo) o para la cuenta $name a un nivel de #level en el realm #realmID. #level puede ir de 0 a 3. #reamID puede ser -1 para todos los realms. |
| account set email | 3 | `.account set email $account $email $email_confirmation` | Añade o cambia un email a la cuenta. |
| account set password | 4 | `.account set password $account $password $password` | Establece la contraseña para la cuenta. |
| account set | 2 | `.account set $subcommand` | Escribe .account set para ver la lista de posibles subcomandos o .help account set $subcommand para ver información sobre los subcomandos. |
| account | 0 | `.account` | Muestra el nivel de acceso de tu cuenta. |
| achievement add | 2 | `.achievement add $achievement` | Añade un achievement al jugador seleccionado. $achievement: puede ser el id del achievement o un enlace de achievement. |
| achievement checkall | 3 | `.achievement checkall` | Comprueba todos los criterios de achievement del jugador seleccionado. |
| achievement | 2 | `.achievement $subcommand` | Escribe .achievement para ver la lista de posibles subcomandos o .help achievement $subcommand para ver información sobre los subcomandos. |
| additem | 2 | `.additem Optional(playerName/playerGUID) #itemid/[#itemname]/#itemLink #itemcount` | Añade el item especificado a ti, al personaje seleccionado o al nombre/GUID de personaje especificado. Si #itemCount es negativo, eliminarás el #itemID. |
| additem set | 2 | `.additem set #itemsetid` | Añade los items del itemset con id #itemsetid al inventario tuyo o del personaje seleccionado. Añadirá un ejemplar de cada item del itemset. |
| announce | 2 | `.announce $MessageToBroadcast` | Envía un mensaje global a todos los jugadores online en el log de chat. |
| appear | 1 | `.appear [$charactername]` | Teletranspórtate al personaje dado. Especifica el nombre del personaje o haz click en su retrato, p. ej. cuando estés en un grupo. El personaje puede estar offline. |
| arena captain | 3 | `.arena captain #TeamID $name` | Un comando para establecer un nuevo capitán del equipo. $name debe estar en el equipo. |
| arena create | 3 | `.arena create $name "arena name" [2/3/5]` | Comando para crear un nuevo equipo de Arena en el juego. |
| arena disband | 3 | `.arena disband #TeamID` | Comando para disolver un equipo de Arena en el juego. |
| arena info | 2 | `.arena info #TeamID` | Comando que muestra información sobre un equipo de arena. |
| arena lookup | 2 | `.arena lookup $name` | Comando que da una lista de equipos de arena con el $name dado. |
| arena rename | 3 | `.arena rename "oldname" "newname"` | Comando para renombrar el nombre de un equipo de Arena. |
| arena season start | 3 | `.arena season start $season_id` | Inicia una nueva temporada de arena, coloca los vendors correctos y establece el estado de la nueva temporada en IN PROGRESS. |
| arena season reward | 3 | `.arena season reward $brackets` | Construye una clasificación combinando los brackets de equipos y otorga recompensas de la tabla arena_season_reward.\nEjemplo de uso:\n \n# Combina todos los brackets, construye una clasificación y distribuye las recompensas entre ellos\n.arena season reward all\n \n# Construye clasificaciones por separado para los brackets 2v2, 3v3 y 5v5 para que cada bracket reciba sus propias recompensas\n.arena season reward 2\n.arena season reward 3\n.arena season reward 5\n \n# Combina los brackets 2v2 y 3v3 y distribuye las recompensas\n.arena season reward 2,3 |
| arena season deleteteams | 3 | `.arena season deleteteams` | Elimina TODOS los equipos de arena. |
| arena season set state | 3 | `.arena season set state $state` | Cambia el estado de la temporada actual.\nEstados disponibles:\n 0 - deshabilitado. Los jugadores no pueden ponerse en cola para la arena.\n 1 - en progreso. Los jugadores pueden usar la funcionalidad relacionada con la arena. |
| aura | 2 | `.aura #spellid` | Añade el aura del hechizo #spellid a la Unidad seleccionada. |
| aura stack | 2 | `.aura stack #spellid #stacks` | Modifica los #stacks de un #spellid ya aplicado a la Unidad seleccionada. |
| autobroadcast | 2 | `.autobroadcast $subcommand` | Escribe .autobroadcast para ver una lista de subcomandos o .help autobroadcast $subcommand para ver información sobre los subcomandos. |
| autobroadcast add | 3 | `.autobroadcast add $weight $text` | Añade una nueva entrada de autobroadcast con el peso y el texto dados. |
| autobroadcast list | 2 | `.autobroadcast list` | Lista todas las entradas de autobroadcast. |
| autobroadcast locale | 3 | `.autobroadcast locale $id $locale $text` | Añade o reemplaza un texto localizado para la entrada de autobroadcast con el ID dado. |
| autobroadcast remove | 3 | `.autobroadcast remove $id` | Elimina la entrada de autobroadcast con el ID dado y sus entradas de locale. |
| bags | 2 | `.bags $subcommand` | Escribe .bags para ver una lista de todos los subcomandos. |
| bags clear | 2 | `.bags clear $itemquality` | Limpia de las bolsas del jugador todos los items de calidad $itemQuality e inferior. |
| bags clear all | 2 | `.bags clear all` | Limpia todos los items del jugador. |
| ban account | 2 | `.ban account $account_name $bantime $reason` | Banea la cuenta y expulsa al jugador si está en el juego en cualquier personaje. $bantime: un valor negativo lleva a un ban permanente; de lo contrario usa una cadena de tiempo como `4d20h3s`. |
| ban character | 2 | `.ban character $character_name $bantime $reason` | Banea el personaje y expulsa a ese personaje si está en el juego. $bantime: un valor negativo lleva a un ban permanente; de lo contrario usa una cadena de tiempo como `4d20h3s`. |
| ban ip | 2 | `.ban ip $Ip $bantime $reason` | Banea una IP. $bantime: un valor negativo lleva a un ban permanente; de lo contrario usa una cadena de tiempo como `4d20h3s`. |
| ban playeraccount | 2 | `.ban playeraccount $character_name $bantime $reason` | Banea una cuenta basándose en el nombre del personaje y expulsa a ese personaje si está en el juego. $bantime: un valor negativo lleva a un ban permanente; de lo contrario usa una cadena de tiempo como `4d20h3s`. |
| ban | 2 | `.ban $subcommand` | Escribe .ban para ver la lista de posibles subcomandos o .help ban $subcommand para ver información sobre los subcomandos. |
| baninfo account | 2 | `.baninfo account $accountid` | Muestra información completa sobre un ban específico. |
| baninfo character | 2 | `.baninfo character $charactername` | Muestra información completa sobre un ban específico. |
| baninfo ip | 2 | `.baninfo ip $ip` | Muestra información completa sobre un ban específico. |
| baninfo | 2 | `.baninfo $subcommand` | Escribe .baninfo para ver la lista de posibles subcomandos o .help baninfo $subcommand para ver información sobre los subcomandos. |
| banlist account | 2 | `.banlist account [$Name]` | Busca en la banlist un patrón de nombre de cuenta o muestra la lista completa de bans de cuenta. |
| banlist character | 2 | `.banlist character $Name` | Busca en la banlist un patrón de nombre de personaje. Se requiere el patrón. |
| banlist ip | 2 | `.banlist ip [$Ip]` | Busca en la banlist un patrón de IP o muestra la lista completa de bans de IP. |
| banlist | 2 | `.banlist $subcommand` | Escribe .banlist para ver la lista de posibles subcomandos o .help banlist $subcommand para ver información sobre los subcomandos. |
| bf | 3 | `.bf $subcommand` | Escribe .bf para ver la lista de posibles subcomandos o .help bf $subcommand para ver información sobre los subcomandos. |
| bf enable | 3 | `.bf enable #battleid` | |
| bf queue | 2 | `.bf queue #battleid` | Muestra todos los jugadores actualmente en cola, invitados o activamente en guerra en el battlefield especificado. #battleid: el ID de la batalla (p. ej. 1 para Wintergrasp). |
| bf start | 3 | `.bf start #battleid` | |
| bf stop | 3 | `.bf stop #battleid` | |
| bf switch | 3 | `.bf switch #battleid` | |
| bf timer | 3 | `.bf timer #battleid #timer` | |
| bindsight | 3 | `.bindsight` | Vincula la visión a la unidad seleccionada indefinidamente. No se puede usar mientras se está poseyendo un objetivo. |
| bm | 2 | `.bm [on/off]` | Activa o desactiva el modo Beastmaster en el juego o muestra el estado actual si no se proporciona on/off. |
| cache | 2 | `.cache $subcommand` | Datos de personaje cacheados durante el arranque. Escribe .cache para ver una lista de subcomandos o .help $subcommand para ver información sobre los subcomandos. |
| cache delete | 3 | `.cache delete $playername` | Elimina los datos cacheados del personaje seleccionado. ¡Usar solo para depuración! |
| cache info | 2 | `.cache info $playerNameDisplays` | datos cacheados del personaje seleccionado. |
| cache refresh | 2 | `.cache refresh $playerName` | Elimina la caché actual y la refresca con datos actualizados. |
| cast back | 2 | `.cast back #spellid [triggered]` | El objetivo seleccionado lanzará #spellid a tu personaje. Si se proporciona 'triggered' o parte, el hechizo se lanza con el flag triggered. |
| cast dest | 2 | `.cast dest #spellid #x #y #z [triggered]` | El objetivo seleccionado lanzará #spellid en el destino proporcionado. Si se proporciona 'triggered' o parte, el hechizo se lanza con el flag triggered. |
| cast dist | 2 | `.cast dist #spellid [#dist [triggered]]` | Lanzarás el hechizo a un punto a distancia #dist. Si se proporciona 'triggered' o parte, el hechizo se lanza con el flag triggered. No todos los hechizos se pueden lanzar como hechizos de área. |
| cast self | 2 | `.cast self #spellid [triggered]` | Hace que el objetivo lance #spellid sobre sí mismo. Si se proporciona 'triggered' o parte, el hechizo se lanza con el flag triggered. |
| cast target | 2 | `.cast target #spellid [triggered]` | El objetivo seleccionado lanzará #spellid a su víctima. Si se proporciona 'triggered' o parte, el hechizo se lanza con el flag triggered. |
| cast | 2 | `.cast #spellid [triggered]` | Lanza #spellid al objetivo seleccionado. Si no hay objetivo seleccionado, lo lanza sobre uno mismo. Si se proporciona 'triggered' o parte, el hechizo se lanza con el flag triggered. |
| character | 2 | `.character $subcommand` | Escribe .character para ver una lista de posibles subcomandos o .help character $subcommand para ver información sobre el subcomando. |
| character changeaccount | 3 | `.character changeaccount $NewAccountNAme $Name` | Mueve el personaje especificado a la cuenta proporcionada. Expulsa al jugador si el personaje está online. |
| character changefaction | 2 | `.character changefaction $name` | Cambia la facción del personaje. |
| character changerace | 2 | `.character changerace $name` | Cambia la raza del personaje. |
| character check bag | 2 | `.character check bag [$target_player] #bagSlot 1 - 4 ` | Revisa la bolsa de un jugador. |
| character check bank | 2 | `.character check bank ` | Revisa tu propio banco. |
| character check profession | 2 | `.character check profession [$target_player] ` | Muestra la lista de profesiones conocidas del jugador seleccionado. |
| character customize | 2 | `.character customize [$name]` | Marca al personaje seleccionado en el juego o por $name en el comando para personalizarlo en el próximo login. |
| character deleted delete | 4 | `.character deleted delete #guid\$name` | Elimina completamente los personajes seleccionados. Si se proporciona $name, solo se eliminarán los personajes con esa cadena en su nombre; si se proporciona #guid, solo se eliminará el personaje con ese GUID. |
| character deleted list | 3 | `.character deleted list [#guid\$name]` | Muestra una lista con todos los personajes eliminados. Si se proporciona $name, solo se seleccionarán los personajes con esa cadena en su nombre; si se proporciona #guid, solo se seleccionará el personaje con ese GUID. |
| character deleted purge | 4 | `.character deleted purge [#keepDays]` | Elimina completamente de la base de datos todos los personajes que fueron eliminados hace más de #keepDays. Si no se proporciona #keepDays, se usa el valor de la opción 'CharDelete.KeepDays' de worldserver.conf. Si la opción 'CharDelete.KeepDays' está deshabilitada (valor 0), este comando no se puede usar sin especificar el parámetro #keepDays. |
| character deleted restore | 3 | `.character deleted restore #guid\$name [$newname] [#new account]` | Restaura personajes eliminados. Si se proporciona $name, solo se restaurarán los personajes con esa cadena en su nombre; si se proporciona $guid, solo se restaurará el personaje con ese GUID. Si se establece $newname, el personaje se restaurará con ese nombre en lugar del original. Si se establece #newaccount, el personaje se restaurará en la lista de personajes de esa cuenta específica. ¡Esto solo funciona con un personaje! |
| character erase | 4 | `.character erase $name` | Elimina el personaje $name. El personaje se elimina definitivamente sin tener en cuenta ninguna opción de borrado. |
| character level | 3 | `.character level [$playername] [#level]` | Establece el nivel del personaje $playername (o el seleccionado si no se proporciona nombre) en #numberoflevels o +1 si no se proporciona #numberoflevels. Si se omite #numberoflevels, el nivel aumentará en 1. Si #numberoflevels es 0, se reinicia el mismo nivel. Si no hay personaje seleccionado y no se proporciona nombre, aumenta tu nivel. El comando se puede usar en personajes offline. Se recalculan todas las stats y valores dependientes. Al bajar de nivel se pueden resetear los talentos si es necesario. También al bajar de nivel se pueden perder items equipados con un requisito de nivel mayor. |
| character rename | 2 | `.character rename [$character_name] [1]` | Marca al personaje seleccionado en el juego o por $character_name en el comando para renombrarlo en el próximo login. Añadir un `1` al final guarda el nombre antiguo en la tabla `characters.reserved_name` e impide que las cuentas con GMlevel 0 reutilicen dicho nombre antiguo. |
| character reputation | 2 | `.character reputation [$player_name]` | Muestra información de reputación del jugador seleccionado o del jugador encontrado por $player_name. |
| character titles | 2 | `.character titles [$player_name]` | Muestra la lista de títulos conocidos del jugador seleccionado o del jugador encontrado por $player_name. |
| chatfilter | 2 | `.chatfilter $subcommand` | Escribe .chatfilter para ver una lista de subcomandos o .help chatfilter $subcommand para ver información sobre los subcomandos. |
| chatfilter add | 3 | `.chatfilter add $word` | Añade $word a la tabla `chat_filter` y recarga el filtro de chat. |
| chatfilter list | 2 | `.chatfilter list` | Lista todas las entradas de la tabla `chat_filter`. |
| chatfilter remove | 3 | `.chatfilter remove $word` | Elimina $word de la tabla `chat_filter` y recarga el filtro de chat. |
| cheat casttime | 2 | `.cheat casttime [on/off]` | Activa o desactiva los tiempos de lanzamiento de hechizos de tu personaje. |
| cheat cooldown | 2 | `.cheat cooldown [on/off]` | Activa o desactiva los cooldowns de hechizos de tu personaje. |
| cheat explore | 2 | `.cheat explore #flag` | Revela u oculta todos los mapas para el jugador seleccionado. Si no hay jugador seleccionado, oculta o revela los mapas para ti. Usa un #flag con valor 1 para revelar, usa un #flag con valor 0 para ocultar todos los mapas. |
| cheat god | 2 | `.cheat god [on/off]` | Activa o desactiva la capacidad de tu personaje de recibir daño. |
| cheat power | 2 | `.cheat power [on/off]` | Activa o desactiva el coste de los hechizos de tu personaje (p. ej. maná). |
| cheat status | 2 | `.cheat status` | Muestra los cheats que tienes activados actualmente. |
| cheat taxi | 2 | `.cheat taxi on/off` | Concede o retira temporalmente el acceso a todas las rutas de taxi para el personaje seleccionado. Si no hay personaje seleccionado, oculta o revela todas las rutas para ti. Los nodos de taxi ya visitados siguen siendo accesibles tras retirar el acceso. |
| cheat waterwalk | 2 | `.cheat waterwalk on/off` | Activa/desactiva el estado waterwalk para el jugador seleccionado o para uno mismo si no hay jugador seleccionado. |
| cheat | 2 | `.cheat $subcommand` | Escribe .cheat para ver la lista de posibles subcomandos o .help cheat $subcommand para ver información sobre los subcomandos. |
| combatstop | 2 | `.combatstop [$playername]` | Detiene el combate del personaje seleccionado. Si el seleccionado no es un jugador, el comando se aplica a uno mismo. Si se proporciona $playername, el intento se aplica al jugador online $playername. |
| cometome | 3 | `.cometome $parameter` | Hace que la creature seleccionada venga a tu ubicación actual (la nueva posición no se guarda en la BD). |
| commands | 0 | `.commands` | Muestra una lista de los comandos disponibles para el nivel de tu cuenta. |
| commentator | 1 | `.commentator [on/off]` | Activa o desactiva la etiqueta de Commentator en el juego o muestra el estado actual si no se proporciona on/off. |
| cooldown | 2 | `.cooldown [#spell_id]` | Elimina todos (si no se proporciona spell_id) o el cooldown del hechizo #spell_id del personaje seleccionado o de ti (si no hay selección). |
| damage | 2 | `.damage $damage_amount [$school [$spellid]]` | Aplica $damage al objetivo. Si no se proporcionan $school ni $spellid, es daño cuerpo a cuerpo plano y limpio sin modificadores. Si se proporciona $school, el daño se modifica por la reducción de armadura (si la escuela es física) y los modificadores de absorción del objetivo, y el resultado se aplica como daño cuerpo a cuerpo al objetivo. Si se proporciona spell, el daño se modifica y se aplica como daño de hechizo. $spellid puede ser un shift-link. |
| debug anim | 3 | `.debug anim` | TODO |
| debug areatriggers | 3 | `.debug areatriggers` | Activa el modo debug para los areatriggers. En modo debug se notificará al GM si alcanza un areatrigger. |
| debug arena | 3 | `.debug arena` | Activa el modo debug para las arenas. En modo debug el GM puede iniciar una arena con un solo jugador. |
| debug bg | 3 | `.debug bg` | Activa el modo debug para los battlegrounds. En modo debug el GM puede iniciar un battleground con un solo jugador. |
| debug boundary | 3 | `.debug boundary [duration] [fill] [z]` | Visualiza los límites del mapa para el GM. Argumentos opcionales: <br/>`duration`: duración en ms (por defecto: 5000 [5 segundos], máx: 180000 [3 minutos]).<br/> `fill`: rellena el límite con marcadores.<br/> `z`: incluye el eje z en la visualización. |
| debug cooldown | 3 | `.debug cooldown #spellID #cooldownTime #itemID` | Aplica un cooldown de la duración dada (en milisegundos) para el hechizo e item ID dados. |
| debug dummy | 3 | `.debug dummy` | Comando debug genérico. No hace nada por defecto. |
| debug entervehicle | 3 | | Entra en el vehículo objetivo. |
| debug factionchange | 3 | `.debug factionchange [$playerName]` | Comprueba todos los requisitos de cambio de facción/raza para el jugador objetivo e informa de pass/fail para cada condición (flags AT_LOGIN, hermandad, capitán de arena, correo, subastas, límite de oro). |
| debug getitemstate | 3 | `.debug getitemstate [unchanged\changed\new\removed\queue\check_all]` | Obtiene el estado de item especificado de los items del jugador seleccionado. |
| debug getitemvalue | 3 | `.debug getitemvalue $guid $index` | Obtiene el valor del item con $guid en $index. |
| debug getvalue | 3 | `.debug $field [1\0]` | 1: obtiene el valor uint32 de $field de la unidad seleccionada; 0: obtiene el valor float de $field de la unidad seleccionada. |
| debug hostil | 1 | | Obtiene la lista de referencias hostiles de la unidad seleccionada. |
| debug hostile | 3 | `.debug hostile` | Devuelve la lista de referencias hostiles de un jugador dado. |
| debug itemexpire | 3 | `.debug itemexpire $guid` | Elimina el item con $guid. |
| debug lfg | 3 | `.debug lfg` | Activa el modo debug para lfg. En modo debug el GM puede iniciar la cola lfg con un solo jugador. |
| debug loot | 2 | `.debug loot <type> <id> [count]` | Simula la generación de loot para el tipo de loot e ID dados, mostrando los resultados en el chat sin crear items. El count opcional (1-100) repite la simulación y muestra las tasas de drop agregadas. Tipos válidos: creature, gameobject, fishing, item, pickpocketing, skinning, disenchant, prospecting, milling, spell, reference, mail, player. |
| debug lootrecipient | 3 | `.debug lootrecipient` | Obtiene el destinatario del loot de la creature seleccionada. |
| debug los | 3 | `.debug los` | Muestra información sobre el estado de la línea de visión. |
| debug mapdata | 3 | `.debug mapdata` | Muestra información de depuración sobre el mapa actual. |
| debug Mod32Value | 3 | `.debug Mod32Value #field #value` | Añade #value al field #field de tu personaje. |
| debug moveflags | 3 | `.debug moveflags [$newMoveFlags [$newMoveFlags2]]` | Si no se dan parámetros, muestra los moveflags actuales del objetivo. |
| debug objectcount | 3 | `.debug objectcount <optional map id>` | Muestra el número de Creatures y GameObjects para el map id especificado o para todos los mapas si no se especifica ninguno. |
| debug play | 1 | `.debug play $subcommand` | Escribe .debug play para ver la lista de posibles subcomandos o .help debug play $subcommand para ver información sobre los subcomandos. |
| debug play cinematic | 1 | `.debug play cinematic #cinematicid` | Reproduce la cinemática #cinematicid para ti. Te quedas en el sitio mientras tu mente vuela. |
| debug play movie | 1 | `.debug play movie #movieid` | Reproduce la película #movieid para ti. |
| debug play music | 3 | `.debug play music <musicId>` | Reproduce la música con el musicId dado. La música se reproducirá solo para ti. Otros jugadores no la oirán. |
| debug play sound | 1 | `.debug play sound #soundid` | Reproduce el sonido con #soundid. El sonido se reproducirá solo para ti. Otros jugadores no lo oyen. Advertencia: el cliente puede tener más de 5000 sonidos... |
| debug play visual | 3 | `.debug play visual #visualid` | Reproduce el spell visual con #visualid. #visualid se refiere al ID de SpellVisualKit.dbc. |
| debug send | 3 | `.debug send $subcommand` | Escribe .debug send para ver la lista de posibles subcomandos o .help debug send $subcommand para ver información sobre los subcomandos. |
| debug send buyerror | 3 | `.debug send buyerror #errorid` | Prueba un id de error de compra. |
| debug send channelnotify | 3 | `.debug send channelnotify #notifytype` | Envía #notifytype al canal "test". |
| debug send chatmessage | 3 | `.debug send chatmessage #type` | Envía un mensaje de chat del tipo dado. |
| debug send chatmmessage | 3 | `.debug send chatmmessage #msgtype` | Envía un mensaje "testtest" del tipo #msgtype. |
| debug send equiperror | 3 | `.debug send equiperror #errorid` | Prueba un id de error de equipar. |
| debug send largepacket | 3 | `.send largepacket` | Envía un paquete grande (>128000 bytes). |
| debug send opcode | 3 | `.debug send opcode` | Envía un paquete al jugador actual según se especifica en el archivo "opcode.txt", que debe estar en el directorio de trabajo del servidor. Ejemplo del contenido del archivo: `631 uint32 6146`, que inicia una música de fondo diferente en el cliente: Opcode "SMSG_PLAY_MUSIC" (dec 631, hex 0x277) que necesita en este caso un uint32 para especificar el sound ID (aquí: 6146 "Zone - Orgrimmar02"). |
| debug send qinvalidmsg | 3 | `.debug send qinvalidmsg #questfailedreasons` | Envía un mensaje de quest fallida del tipo #questfailedreasons al jugador actual. |
| debug send qpartymsg | 3 | `.debug send qpartymsg #questsharemessages` | Envía un mensaje de compartir quest del tipo #questsharemessages al jugador actual. |
| debug send sellerror | 3 | `.debug send sellerror #errorid` | Prueba un id de error de venta. |
| debug send setphaseshift | 3 | `.debug send setphaseshift #phaseshift` | Envía un paquete de phase shift al jugador actual. |
| debug send spellfail | 3 | `.debug send spellfail #resultid [#arg1] [#arg2]` | Envía un paquete de fallo de hechizo al jugador actual usando el resultado de hechizo #resultid y los argumentos opcionales #arg1 y #arg2. |
| debug setaurastate | 3 | `.debug setaurastate #aurastatetype` | Modifica el aura state de la unidad seleccionada (#aurastatetype > 0) o resetea el estado (#aurastatetype = 0). |
| debug setbit | 3 | `.debug setbit #fieldnumber #bitnumber` | Establece el bit #bitnumber del field #fieldnumber para la unidad seleccionada. |
| debug setitemvalue | 3 | `.debug getitemvalue $guid $index $value` | Establece $value para el item con $guid en $index. |
| debug setvalue | 3 | `.debug $field $value [1\0]` | 1: establece el $value uint32 para $field de la unidad seleccionada; 0: establece el $value float para $field de la unidad seleccionada. |
| debug setvid | 3 | `.debug setvid #ID` | Actualmente deshabilitado. Establece el vehicle ID del objetivo dado al valor dado. |
| debug spawnvehicle | 3 | `.debug spawnvehicle #entry [#vehicleid]` | Spawnea un vehículo con la creature template #entry y el #vehicleid opcional. |
| debug threat | 3 | `.debug threat` | Devuelve la lista de amenaza de una creature dada. |
| debug unitstate | 3 | `.debug unitstate [#unitstate]` | Establece #unitstate para la unidad seleccionada. Si no se especifica ningún parámetro, muestra el unit state y el react state de la unidad. |
| debug update | 3 | `.debug update #index [#value]` | Lee o escribe el campo de actualización bruto de 32 bits en #index de la unidad seleccionada. Sin #value, muestra el valor actual; con #value, lo establece. Escribir un valor no válido puede bloquear el servidor. Los #index válidos son los enums \*\_FIELD en src/server/game/Entities/Object/Updates/UpdateFields.h (UNIT\_FIELD\_\* para criaturas, PLAYER\_FIELD\_\* para jugadores). |
| debug uws | 3 | `.debug uws #worldstate #value` | Envía la actualización de world state para #worldstate y #value al jugador actual. |
| debug visibilitydata | 3 | `.debug visibilitydata` | Muestra información de depuración relacionada con la visibilidad de objetos alrededor del jugador. |
| debug zonestats | 1 | `.debug zonestats [$playerName]` | Muestra la cantidad de jugadores en la zona actual del jugador. |
| debug | 2 | `.debug $subcommand` | Escribe .debug para ver la lista de posibles subcomandos o .help debug $subcommand para ver información sobre los subcomandos. |
| deserter bg add | 3 | `.deserter bg add [$playerName] [$time]` | Añade el debuff de desertor de bg a un jugador o a tu objetivo con duración $time. $time por defecto: 15m. |
| deserter bg remove | 3 | `.deserter bg remove [$playerName]` | Elimina el debuff de desertor de bg de un jugador o de tu objetivo. |
| deserter bg remove all | 3 | `.deserter bg remove all [$maxDuration]` | Elimina el debuff de desertor de bg de todos los jugadores online y offline. $maxDuration establece la duración máxima a eliminar. Por defecto: 15m. |
| deserter instance add | 3 | `.deserter instance add [$playerName] [$time]` | Añade el debuff de desertor de instancia a un jugador o a tu objetivo con duración $time. $time por defecto: 30m. |
| deserter instance remove | 3 | `.deserter instance remove [$playerName]` | Elimina el debuff de desertor de instancia de un jugador o de tu objetivo. |
| deserter instance remove all | 3 | `.deserter instance remove all [$maxDuration]` | Elimina el debuff de desertor de instancia de todos los jugadores online y offline. $maxDuration establece la duración máxima a eliminar. Por defecto: 30m. |
| dev | 3 | `.dev [on/off]` | Activa o desactiva la etiqueta de Dev en el juego o muestra el estado actual si no se proporciona on/off. |
| die | 2 | `.die` | Mata al jugador seleccionado. Si no hay jugador seleccionado, te matará a ti. |
| disable add battleground | 3 | `.disable add battleground $entry $flag $comment` | |
| disable add map | 3 | `.disable add map $entry $flag $comment` | |
| disable add outdoorpvp | 3 | `.disable add outdoorpvp $entry $flag $comment` | |
| disable add quest | 3 | `.disable add quest $entry $flag $comment` | |
| disable add spell | 3 | `.disable add spell $entry $flag $comment` | |
| disable add vmap | 3 | `.disable add vmap $entry $flag $comment` | |
| disable remove battleground | 3 | `.disable remove battleground $entry` | |
| disable remove map | 3 | `.disable remove map $entry` | |
| disable remove outdoorpvp | 3 | `.disable remove outdoorpvp $entry` | |
| disable remove quest | 3 | `.disable remove quest $entry` | |
| disable remove spell | 3 | `.disable remove spell $entry` | |
| disable remove vmap | 3 | `.disable remove vmap $entry` | |
| dismount | 0 | `.dismount` | Te desmonta, si estás montado. |
| distance | 3 | `.distance` | Muestra la distancia desde tu personaje hasta la creature seleccionada. |
| event activelist | 2 | `.event activelist` | Muestra la lista de eventos actualmente activos. |
| event info | 2 | `.event info [event_id]` | Muestra información sobre los game events. |
| event start | 2 | `.event start #event_id` | Inicia el evento #event_id. Establece la hora de inicio del evento al momento actual (el cambio no se guarda en la BD). |
| event stop | 2 | `.event stop #event_id` | Detiene el evento #event_id. Establece la hora de inicio del evento en un momento del pasado que hace que el momento actual sea la hora de parada del evento (el cambio no se guarda en la BD). |
| event | 2 | `.event #event_id` | Muestra detalles sobre el evento con #event_id. |
| flusharenapoints | 3 | `.flusharenapoints` | Úsalo para distribuir los puntos de arena según los ratings de los equipos de arena, e iniciar una nueva semana. |
| freeze | 2 | `.freeze (#player)` | "Congela" a #player y desactiva su chat. Al usar esto sin #name congelará a tu objetivo. |
| gear repair | 2 | `.gear repair` | Repara todos los items del jugador seleccionado. |
| gear stats | 0 | `.gear stats` | Muestra el itemlevel medio del jugador objetivo. |
| gm chat | 2 | `.gm chat [on/off]` | Activa o desactiva el MODO GM del chat (muestra la insignia de gm en los mensajes) o muestra el estado actual si no se proporciona on/off. |
| gm fly | 2 | `.gm fly [on/off]` | Activa/desactiva el modo de vuelo gm. |
| gm ingame | 0 | `.gm ingame` | Muestra una lista de los Game Masters disponibles en el juego. |
| gm list | 3 | `.gm list` | Muestra una lista de todas las cuentas de Game Master y sus niveles de seguridad. |
| gm off | 1 | `.gm off` | Desactiva el flag GM. |
| gm on | 1 | `.gm on` | Activa el flag GM. |
| gm spectator | 2 | `.gm spectator on/off` | Requiere `.gm on`, permite al personaje `GM` usar `/follow` sobre miembros de la facción opuesta. `Nota`: puede que necesites teletransportarte a otra zona / cargar una nueva área, no se actualiza al momento. |
| gm visible | 2 | `.gm visible on/off` | Muestra el estado de visibilidad actual o hace al GM visible (on) e invisible (off) para otros jugadores. |
| gm | 1 | `.gm [on/off]` | Activa o desactiva el MODO GM en el juego o muestra el estado actual si no se proporciona on/off. |
| gmannounce | 2 | `.gmannounce $announcement` | Envía un anuncio a los Gamemasters online. |
| gmnameannounce | 2 | `.gmnameannounce $announcement` | Envía un anuncio a todos los GM online, mostrando el nombre del remitente. |
| gmnotify | 2 | `.gmnotify $notification` | Muestra una notificación en la pantalla de todos los GM online. |
| go creature | 1 | `.go creature $creature.guid` | Te teletransporta a la creature usando el valor `guid` de la tabla `creature`. |
| go creature id | 1 | `.go creature id $creature_template.entry [#spawn]` | Te teletransporta a una creature usando el valor `entry` de la tabla `creature_template`. <br/>Usar el valor `#spawn` usará la posición (fila) en la base de datos `creature`; en caso de no proporcionar valor y existir varias creatures del mismo `entry(id1)` en el mundo, serás teletransportado a la creature con el `guid` más bajo. |
| go creature name | 1 | `.go creature name $creature_template.name` | Te teletransporta a una creature usando el valor `name` de la tabla `creature_template`. <br/>En caso de existir varias creatures con el mismo `name` en el mundo, serás teletransportado a la creature con el `guid` más bajo.<br/>Al ejecutar el comando para nombres con espacios no rompas la cadena, ejemplo: `.go creature name Ruby Scalebane` |
| go gameobject | 1 | `.go gameobject $gameobject.guid` | Te teletransporta al gameobject usando el valor `guid` de la tabla `gameobject`. |
| go gameobject id | 1 | `.go gameobject id $gameobject_template.entry [#spawn]` | Te teletransporta a un gameobject usando el valor `entry` de la tabla `gameobject_template`. <br/>Usar el valor `#spawn` usará la posición (fila) en la base de datos `gameobject`; en caso de no proporcionar valor y existir varias creatures del mismo `entry(id)` en el mundo, serás teletransportado al objeto con el `guid` más bajo. |
| go graveyard | 1 | `.go graveyard #graveyardId` | Teletransporte al cementerio con el graveyardId especificado. |
| go grid | 1 | `.go grid #gridX #gridY [#mapId]` | Teletransporta al gm al centro del grid con los índices proporcionados en el mapa #mapId (o el mapa actual si no se proporciona). |
| go quest | 1 | `.go quest <starter/ender> <quest>` | Te teletransporta a la creature u objeto que inicia/termina la quest. |
| go taxinode | 1 | `.go taxinode #taxinode` | Teletransporta al jugador a las coordenadas del taxinode. Puedes buscar la zona usando .lookup taxinode $namepart |
| go ticket | 2 | `.go ticket #ticketid` | Teletransporta al usuario a la ubicación donde se creó el $ticketid. |
| go trigger | 1 | `.go trigger #trigger_id` | Teletransporta tu personaje al areatrigger con id #trigger_id. El personaje será teletransportado al destino del trigger si el areatrigger seleccionado es un trigger de teletransporte. |
| go xyz | 1 | `.go xyz #x #y [#z [#mapid [#orientation]]]` | Teletransporta al jugador al punto con coordenadas (#x,#y,#z) en el mapa #mapid con orientación #orientation. Si no se proporciona z, se usará el nivel del suelo/agua. Si no se proporciona mapid, se usará el mapa actual. Si no se proporciona #orientation, se usará la orientación actual. Se permiten valores no numéricos y serán ignorados. |
| go zonexy | 1 | `.go zonexy #x #y [#zone]` | Teletransporta al jugador al punto con coordenadas de cliente (#x,#y) al nivel del suelo (agua) en la zona #zoneid o la zona actual si no se proporciona #zoneid. Puedes buscar la zona usando .lookup area $namepart |
| go | 1 | `.go $subcommand` | Escribe .go para ver la lista de posibles subcomandos o .help go $subcommand para ver información sobre los subcomandos. |
| gobject activate | 2 | `.gobject activate #guid` | Activa un objeto como una puerta o un botón. |
| gobject add temp | 2 | | Añade un gameobject temporal que no se guarda en la BD. |
| gobject add | 3 | `.gobject add #id` | Añade un game object desde las game object templates al mundo en tu ubicación actual usando el #id. spawntimesecs establece el tiempo de spawn, es opcional. Nota: esto es una copia de .gameobject. |
| gobject delete | 3 | `.gobject delete #go_guid` | Elimina el gameobject con guid #go_guid. |
| gobject despawngroup | 3 | `.gobject despawngroup #groupId` | Despawnea todos los gameobjects del spawn group dado. |
| gobject info | 1 | `.gobject info [$object_entry]` | Consulta la información del Gameobject para el gameobject seleccionado o el entry dado. |
| gobject load | 3 | `.gobject load #spawnId` | Carga un spawn de gameobject de la base de datos al mundo por su GUID. |
| gobject move | 3 | `.gobject move #goguid [#x #y #z]` | Mueve el gameobject #goguid a las coordenadas del personaje (o a las coordenadas (#x,#y,#z) si se proporcionan). |
| gobject near | 3 | `.gobject near [#distance]` | Muestra los gameobjects a distancia #distance del jugador. Muestra los guids y coordenadas de los gameobjects ordenados por distancia desde el personaje. Si no se proporciona #distance, usa 10 como valor por defecto. |
| gobject respawn | 1 | `.gobject respawn #guid` | Respawnea el gameobject objetivo. |
| gobject set | 3 | `.gobject set` | |
| gobject set phase | 3 | `.gobject set phase #guid #phasemask` | El phasemask del gameobject con guid de BD #guid se cambia a #phasemask con la actualización de visión del mundo correspondiente para los jugadores. El estado del gameobject se guarda en la BD y es persistente. |
| gobject set state | 3 | | |
| gobject spawngroup | 3 | `.gobject spawngroup #groupId` | Spawnea todos los gameobjects del spawn group dado. |
| gobject target | 1 | `.gobject target [#go_id\#go_name_part]` | Localiza y muestra la posición del gameobject más cercano. Si se proporciona #go_id o #go_name_part, localiza y muestra la posición del gameobject más cercano con el id de gameobject template #go_id o el nombre que incluya #go_name_part como parte. |
| gobject turn | 3 | `.gobject turn #goguid` | Establece para el gameobject #goguid la misma orientación que la orientación actual del personaje. |
| gobject | 2 | `.gobject $subcommand` | Escribe .gobject para ver la lista de posibles subcomandos o .help gobject $subcommand para ver información sobre los subcomandos. |
| gps | 1 | `.gps [$name\$shift-link]` | Muestra la información de posición de un personaje o creature seleccionado (también si se proporciona el nombre de jugador $name, para el jugador nombrado, o si se proporciona un shift-link de creature/gameobject, para la creature/gameobject señalado si está cargado). La información de posición incluye X, Y, Z y orientación, map Id y zone Id. |
| group disband | 2 | `.group disband [$characterName]` | Disuelve el grupo del personaje dado. |
| group invites | 2 | `.group invites [on/off]` | Activa/desactiva la aceptación de invitaciones de grupo. Si no se proporciona ningún argumento, muestra el estado de aceptación actual. |
| group join | 2 | `.group join $AnyCharacterNameFromGroup [$CharacterName]` | Añade al grupo del jugador $AnyCharacterNameFromGroup al jugador $CharacterName (o al seleccionado). |
| group leader | 2 | `.group leader [$characterName]` | Establece al personaje dado como líder de su grupo. |
| group list | 2 | `.group list [$CharacterName]` | Lista todos los miembros del grupo/party en el que está el jugador. |
| group revive | 2 | `.group revive $characterName` | Revive a todos los miembros del grupo del personaje dado o a uno mismo si no se proporciona. |
| group remove | 2 | `.group remove [$characterName]` | Elimina al personaje dado de su grupo. |
| group | 2 | `.group $subcommand` | Escribe .group para ver la lista de posibles subcomandos o .help group $subcommand para ver información sobre los subcomandos. |
| groupsummon | 2 | `.groupsummon [$charactername]` | Teletransporta al personaje dado y a su grupo hacia ti. Solo se teletransportan los personajes online, pero el miembro del grupo originalmente seleccionado puede estar offline. |
| guid | 2 | `.guid` | Muestra el GUID del personaje seleccionado. |
| guild create | 2 | `.guild create [$GuildLeaderName] "$GuildName"` | Crea una hermandad llamada $GuildName con el jugador $GuildLeaderName (o el seleccionado) como líder. El nombre de la hermandad debe ir entre comillas. |
| guild delete | 2 | `.guild delete "$GuildName"` | Elimina la hermandad $GuildName. El nombre de la hermandad debe ir entre comillas. |
| guild info | 2 | `.guild info` | Muestra información sobre la hermandad del objetivo o de un Guild Id o Name dado. |
| guild invite | 2 | `.guild invite [$CharacterName] "$GuildName"` | Añade al jugador $CharacterName (o al seleccionado) a la hermandad $GuildName. El nombre de la hermandad debe ir entre comillas. |
| guild rank | 2 | `.guild rank [$CharacterName] #RankNumber` | Establece para el jugador $CharacterName (o el seleccionado) el rango #Rank en una hermandad. Los valores de rango son numéricos, 0 = Guild Master, 1 = Officer, etc... |
| guild rename | 2 | `.guild rename "$GuildName" "$NewGuildName"` | Renombra una hermandad llamada $GuildName con $NewGuildName. El nombre de la hermandad y el nuevo nombre deben ir entre comillas. |
| guild uninvite | 2 | `.guild uninvite [$CharacterName]` | Elimina al jugador $CharacterName (o al seleccionado) de una hermandad. |
| guild | 2 | `.guild $subcommand` | Escribe .guild para ver la lista de posibles subcomandos o .help guild $subcommand para ver información sobre los subcomandos. |
| help | 0 | `.help [$command]` | Muestra las instrucciones de uso del $command dado. Si no se proporciona $command, muestra la lista de comandos disponibles. |
| hidearea | 3 | `.hidearea #areaid` | Oculta el área con #areaid al personaje seleccionado. Si no hay personaje seleccionado, oculta esta área para ti. |
| ~~honor add kill~~ NOT IMPLEMENTED | 2 | gi`.honor add kill` | Añade la unidad objetivo como una de tus muertes pvp de hoy (solo obtienes honor si es un líder racial o un jugador). |
| honor add | 2 | `.honor add $amount` | Añade una cierta cantidad de honor (ganado hoy) al jugador seleccionado. |
| honor add kill | 2 | `.honor add kill` | Añade la unidad objetivo como una de tus muertes pvp de hoy (solo obtienes honor si es un líder racial o un jugador). |
| honor update | 2 | `.honor update` | Fuerza que los campos de honor de ayer se actualicen con los datos de hoy, que se resetearán para el jugador seleccionado. |
| honor | 2 | `.honor $subcommand` | Escribe .honor para ver la lista de posibles subcomandos o .help honor $subcommand para ver información sobre los subcomandos. |
| instance getbossstate | 1 | `.instance getbossstate $bossId [$Name]` | Obtiene el EncounterState actual para el boss id proporcionado. Si no se proporciona nombre de personaje, se usará el mapa actual como objetivo. |
| instance listbinds | 1 | `.instance listbinds` | Lista los binds del jugador seleccionado. |
| instance savedata | 3 | `.instance savedata` | Guarda el InstanceData del mapa del jugador actual en la BD. |
| instance setbossstate | 2 | `.instance setbossstate $bossId $encounterState [$Name]` | Establece el EncounterState del boss id dado a un nuevo valor. Los EncounterStates van de 0 a 5. Si no se proporciona nombre de personaje, se usará el mapa actual como objetivo. |
| instance stats | 1 | `.instance stats` | Muestra estadísticas sobre las instancias. |
| instance unbind | 2 | `.instance unbind <mapid\all> [difficulty]` | Limpia todos/algunos de los binds del jugador. |
| instance | 1 | `.instance $subcommand` | Escribe .instance para ver la lista de posibles subcomandos o .help instance $subcommand para ver información sobre los subcomandos. |
| item move | 2 | `.itemmove #sourceslotid #destinationslotid` | Mueve un item del slot #sourceslotid al #destinationslotid en tu inventario. Aún no implementado. |
| inventory | 1 | `.inventory $subcommand` | Escribe .inventory para ver la lista de posibles subcomandos o .help inventory $subcommand para ver información sobre los subcomandos. |
| inventory count | 1 | `.inventory count $playerName or $playerGuid` | Cuenta los slots libres en las bolsas divididos en diferentes tipos de bolsa. |
| item refund | 3 | `.item refund <name> <item> <extendedCost>` | Elimina el item y restaura honor/arena/items según el extended cost. |
| item restore | 2 | `.item restore [#recoveryItemId] [#playername]` | Restaura un item desechado para el jugador especificado. |
| item restore list | 2 | `.item restore list [#playername]` | Muestra los items restaurables para el jugador especificado. |
| kick | 2 | `.kick [$charactername] [$reason]` | Expulsa del mundo al personaje dado con o sin razón. Si no se proporciona nombre de personaje, se expulsará al jugador seleccionado (excepto a ti mismo). Si no se proporciona razón, la predeterminada es "No Reason". |
| learn all | 2 | `.learn all $subcommand` | Escribe .learn all para ver la lista de posibles subcomandos o .help learn all $subcommand para ver información sobre los subcomandos. |
| learn all crafts | 2 | `.learn crafts` | Aprende todas las profesiones y recetas. |
| learn all default | 2 | `.learn all default [$playername]` | Hace que el jugador seleccionado/$playername aprenda todos los hechizos por defecto de su raza/clase y los hechizos otorgados por quests completadas. |
| learn all gm | 2 | `.learn all gm` | Aprende todos los hechizos por defecto para Game Masters. |
| learn all lang | 2 | `.learn all lang` | Aprende todos los idiomas. |
| learn all my | 2 | `.learn all my $subcommand` | Escribe .learn all my para ver la lista de posibles subcomandos o .help learn all my $subcommand para ver información sobre los subcomandos. |
| learn all my class | 2 | `.learn all my class` | Aprende todos los hechizos y talentos disponibles para su clase. |
| learn all my pettalents | 2 | `.learn all my pettalents` | Aprende todos los talentos disponibles para tu mascota según su tipo de creature (solo para mascotas de cazador). |
| learn all my quest | 2 | `.learn all my quest` | Aprende todos los hechizos recompensados por quests para tu clase. |
| learn all my spells | 2 | `.learn all my spells` | Aprende todos los hechizos (excepto talentos y hechizos cuyo primer rango se aprende como talento) disponibles para su clase. |
| learn all my talents | 2 | `.learn all my talents` | Aprende todos los talentos (y hechizos cuyo primer rango se aprende como talento) disponibles para su clase. |
| learn all my trainer | 2 | `.learn all my trainer` | Aprende todos los hechizos enseñados por los trainers para tu clase. |
| learn all recipes | 2 | `.learn all recipes [$profession]` | Aprende todas las recetas de la profesión especificada y establece el nivel de skill al máximo. Ejemplo: .learn all recipes enchanting |
| learn | 2 | `.learn #spell [all]` | El personaje seleccionado aprende un hechizo con id #spell. Si se proporciona 'all', se aprenden todos los rangos. |
| levelup | 2 | `.levelup [$playername] [#numberoflevels]` | Aumenta/disminuye el nivel del personaje $playername (o el seleccionado si no se proporciona nombre) en #numberoflevels o +1 si no se proporciona #numberoflevels. Si se omite #numberoflevels, el nivel aumentará en 1. Si #numberoflevels es 0, se reinicia el mismo nivel. Si no hay personaje seleccionado y no se proporciona nombre, aumenta tu nivel. El comando se puede usar en personajes offline. Se recalculan todas las stats y valores dependientes. Al bajar de nivel se pueden resetear los talentos si es necesario. También al bajar de nivel se pueden perder items equipados con un requisito de nivel mayor. |
| lfg | 1 | `.lfg $subcommand` | Escribe .lfg para ver la lista de posibles subcomandos o .help lfg $subcommand para ver información sobre los subcomandos. |
| lfg clean | 3 | `.lfg clean` | Limpia la cola actual, solo con fines de depuración. |
| lfg cooldown | 3 | `.lfg cooldown` | Limpia todos los cooldowns de dungeon LFG de todos los jugadores. |
| lfg group | 1 | `.lfg group` | Muestra información sobre todos los jugadores del grupo (estado, roles, comentario, dungeons seleccionados). |
| lfg options | 2 | `.lfg options [new value]` | Muestra las opciones lfg actuales. Se establece un nuevo valor si hay un parámetro extra. |
| lfg player | 1 | `.lfg player` | Muestra información sobre el jugador (estado, roles, comentario, dungeons seleccionados). |
| lfg queue | 1 | `.lfg queue` | Muestra información sobre las colas lfg actuales. |
| linkgrave | 3 | `.linkgrave #graveyard_id [alliance\horde]` | Vincula la zona actual a un cementerio para cualquier fantasma (o de facción alliance/horde). Esto permite que el personaje fantasma de la zona se teletransporte al cementerio tras morir si el cementerio es el más cercano de los vinculados a la zona y acepta fantasmas de esta facción. Añade solo un cementerio en otro mapa y solo si no hay cementerios vinculados (o planeados vincular en el mismo mapa). |
| list auras | 1 | `.list auras` | Lista las auras (pasivas y activas) de la creature o jugador seleccionado. Si no hay creature o jugador seleccionado, lista tus propias auras. |
| list auras id | 1 | `.list auras id` | Lista todas las auras activas en la unidad seleccionada por spell ID. |
| list auras name | 1 | `.list auras name` | Lista todas las auras activas en la unidad seleccionada por nombre de hechizo. |
| list creature | 1 | `.list creature #creature_id [#max_count]` | Muestra las creatures con creature id #creature_id encontradas en el mundo. Muestra los guids y coordenadas de las creatures ordenados por distancia desde el personaje. Se mostrará un máximo de #max_count creatures. Si no se proporciona #max_count, usa 10 como valor por defecto. |
| list gobject | 1 | `.list gobject #gameobject_id [#max_count]` | Muestra los gameobjects con gameobject id #gameobject_id encontrados en el mundo. Muestra los guids y coordenadas de los gameobjects ordenados por distancia desde el personaje. Se mostrará un máximo de #max_count gameobject. Si no se proporciona #max_count, usa 10 como valor por defecto. |
| list item | 1 | `.list item #item_id [#max_count]` | Muestra los items con item id #item_id encontrados en todos los inventarios de personajes, correos, subastas y bancos de hermandad. Muestra los guids del item, el guid del propietario, la cuenta y el nombre del propietario (nombre y guid de la hermandad en caso de banco de hermandad). Se mostrará un máximo de #max_count items. Si no se proporciona #max_count, usa 10 como valor por defecto. |
| list object | 1 | `.list object #object_guid` | [DEPRECADO] Usa ".list gobject" en su lugar. |
| list respawns | 2 | `.list respawns` | Muestra todos los respawns pendientes de creatures y gameobjects en el mapa actual. |
| list | 1 | `.list $subcommand` | Escribe .list para ver la lista de posibles subcomandos o .help list $subcommand para ver información sobre los subcomandos. |
| lookup area | 1 | `.lookup area $namepart` | Busca un área por $namepart, y devuelve todas las coincidencias con sus IDs de área. |
| lookup creature | 1 | `.lookup creature $namepart` | Busca una creature por $namepart, y devuelve todas las coincidencias con sus IDs de creature. |
| lookup event | 1 | `.lookup event $name` | Intenta encontrar el ID del evento con el $name proporcionado. |
| lookup faction | 1 | `.lookup faction $name` | Intenta encontrar el ID de la facción con el $name proporcionado. |
| lookup gobject | 1 | `.lookup gobject $objname` | Devuelve el/los ID(s) de gameobject que coinciden con $objname. |
| lookup item | 1 | `.lookup item $itemname` | Busca un item por $itemname, y devuelve todas las coincidencias con sus IDs de Item. |
| lookup item set | 1 | `.lookup itemset $itemname` | Busca un item set por $itemname, y devuelve todas las coincidencias con sus IDs de Item set. |
| lookup itemset | 1 | `.lookup itemset $itemname` | Busca un item set por $itemname, y devuelve todas las coincidencias con sus IDs de Item set. |
| lookup map | 1 | `.lookup map $namepart` | Busca un mapa por $namepart, y devuelve todas las coincidencias con sus IDs de mapa. |
| lookup object | 1 | `.lookup object` | [DEPRECADO] Usa ".lookup gobject" en su lugar. |
| lookup player | 2 | `.lookup player $subcommand` | Escribe .lookup player para ver la lista de posibles subcomandos o .help lookup player $subcommand para ver información sobre los subcomandos. |
| lookup player account | 2 | `.lookup player account $account ($limit)` | Busca jugadores cuyo nombre de usuario de cuenta sea $account con el parámetro opcional $limit de resultados. |
| lookup player email | 2 | `.lookup player email $email ($limit)` | Busca jugadores cuyo email de cuenta sea $email con el parámetro opcional $limit de resultados. |
| lookup player ip | 2 | `.lookup player ip $ip ($limit)` | Busca jugadores cuya last_ip de cuenta sea $ip con el parámetro opcional $limit de resultados. |
| lookup quest | 1 | `.lookup quest $namepart` | Busca una quest por $namepart, y devuelve todas las coincidencias con sus IDs de quest. |
| lookup skill | 1 | `.lookup skill $$namepart` | Busca un skill por $namepart, y devuelve todas las coincidencias con sus IDs de skill. |
| lookup spell id | 1 | `.lookup spell id #spellid` | Busca un hechizo por #spellid, y devuelve la coincidencia con su nombre de hechizo. |
| lookup spell | 1 | `.lookup spell $namepart` | Busca un hechizo por $namepart, y devuelve todas las coincidencias con sus IDs de hechizo. |
| lookup taxinode | 1 | `.lookup taxinode $substring` | Busca y muestra todos los taxinodes con la $substring proporcionada en el nombre. |
| lookup teleport | 1 | `.lookup teleport $substring` | Busca y muestra todas las ubicaciones del comando .teleport con la $substring proporcionada en el nombre. |
| lookup title | 1 | `.lookup title $$namepart` | Busca un título por $namepart, y devuelve todas las coincidencias con sus IDs e índices de título. |
| lookup | 1 | `.lookup $subcommand` | Escribe .lookup para ver la lista de posibles subcomandos o .help lookup $subcommand para ver información sobre los subcomandos. |
| mail | 2 | `.mail $subcommand` | Escribe .mail para ver una lista de subcomandos o .help mail $subcommand para ver información sobre los subcomandos. |
| mail list | 2 | `.mail list [$player]` | Muestra todos los datos de correo (excepto asunto y cuerpo) del jugador objetivo. |
| mail return | 2 | `.mail return $player $mailId` | Devuelve el correo especificado a su remitente original. |
| mailbox | 1 | `.mailbox` | Abre el buzón. |
| maxskill | 2 | `.maxskill` | Establece todos los skills del jugador objetivo a sus valores máximos para su nivel actual. |
| mmap | 3 | `.mmap $subcommand` | Escribe .mmap para ver la lista de posibles subcomandos o .help mmap $subcommand para ver información sobre los subcomandos. |
| mmap loadedtiles | 3 | `.mmap loadedtiles` | Muestra qué tiles están cargados actualmente. |
| mmap loc | 3 | `.mmap loc` | Imprime en qué tile se está. |
| mmap path | 3 | `.mmap path` | Calcula y muestra una ruta hasta la unidad seleccionada actualmente. |
| mmap stats | 3 | `.mmap stats` | Muestra información sobre el estado actual de los mmaps. |
| mmap testarea | 3 | `.mmap testarea` | Calcula las rutas de todos los npcs cercanos al jugador. |
| modify arenapoints | 1 | `.modify arenapoints #value` | Añade $amount puntos de arena al jugador seleccionado. |
| modify bit | 2 | `.modify bit #field #bit` | Alterna el bit #bit del field #field para el jugador seleccionado. Si no hay jugador seleccionado, modifica tu personaje. |
| modify drunk | 2 | `.modify drunk #value` | Establece el nivel de embriaguez a #value (0..100). El valor 0 elimina el estado de embriaguez, 100 es el estado máximo de embriaguez. |
| modify energy | 2 | `.modify energy #energy` | Modifica la energía del jugador seleccionado. Si no hay jugador seleccionado, modifica tu energía. |
| modify faction | 3 | `.modify faction #factionid #flagid #npcflagid #dynamicflagid` | Modifica la facción y los flags de la creature seleccionada. Sin argumentos, muestra la facción y los flags de la creature seleccionada. |
| modify gender | 2 | `.modify gender male/female` | Cambia el género del jugador seleccionado. |
| modify honor | 2 | `.modify honor $amount` | Añade $amount puntos de honor al jugador seleccionado. |
| modify hp | 2 | `.modify hp #newhp` | Modifica los hp del jugador seleccionado. Si no hay jugador seleccionado, modifica tus hp. |
| modify mana | 2 | `.modify mana #newmana` | Modifica el maná del jugador seleccionado. Si no hay jugador seleccionado, modifica tu maná. |
| modify money | 2 | `.modify money #money` | Añade o elimina dinero al jugador seleccionado. Si no hay jugador seleccionado, modifica tu dinero. #gold puede ser negativo para eliminar dinero. |
| modify mount | 2 | `.modify mount #id #speed` | Muestra al jugador seleccionado como montado en la creature #id y establece la velocidad al valor #speed. |
| modify phase | 2 | `.modify phase #phasemask` | El phasemask del personaje seleccionado se cambia a #phasemask con la actualización de visión del mundo correspondiente. El cambio está activo hasta que se cambie la phase en el juego, o se active/desactive el modo GM, o se vuelva a iniciar sesión. El phasemask de la mascota del personaje se actualiza al mismo valor. |
| modify rage | 2 | `.modify rage #newrage` | Modifica la ira del jugador seleccionado. Si no hay jugador seleccionado, modifica tu ira. |
| modify reputation | 2 | `.modify reputation #repId (#repvalue \ $rankname [#delta])` | Establece la reputación del jugador seleccionado con la facción #repId a #repvalue o a $reprank. Si se proporciona el nombre del rango de reputación, la reputación resultante será la más baja de ese rango más la cantidad delta, si se especifica. Puedes usar '.pinfo rep' para listar todos los ids de reputación conocidos, o usar '.lookup faction $name' para localizar un id de facción específico. |
| modify runicpower | 2 | `.modify runicpower #newrunicpower` | Modifica el poder rúnico del jugador seleccionado. Si no hay jugador seleccionado, modifica tu poder rúnico. |
| modify scale | 2 | `.modify scale #scale` | Modifica el tamaño del jugador o creature seleccionado a "escala normal"*rate. Si no hay jugador o creature seleccionado, modifica tu tamaño. #rate puede ir de 0.1 a 10. |
| modify speed all | 2 | `.modify speed #rate` | Modifica todas las velocidades -correr, nadar, correr hacia atrás, nadar hacia atrás- del jugador seleccionado a "velocidad base normal para este tipo de movimiento"*rate. Si no hay jugador seleccionado, modifica tu velocidad. #rate puede ir de 0.1 a 50. |
| modify speed backwalk | 2 | `.modify speed backwalk #rate` | Modifica la velocidad del jugador seleccionado mientras corre hacia atrás a "velocidad normal de andar hacia atrás"*rate. Si no hay jugador seleccionado, modifica tu velocidad. #rate puede ir de 0.1 a 50. |
| modify speed fly | 2 | `.modify speed fly #rate` | Modifica la velocidad de vuelo del jugador seleccionado a "velocidad de vuelo normal"*rate. Si no hay jugador seleccionado, modifica tu velocidad. #rate puede ir de 0.1 a 50. |
| modify speed swim | 2 | `.modify speed swim #rate` | Modifica la velocidad de nado del jugador seleccionado a "velocidad de nado normal"*rate. Si no hay jugador seleccionado, modifica tu velocidad. #rate puede ir de 0.1 a 50. |
| modify speed walk | 2 | `.modify speed bwalk #rate` | Modifica la velocidad del jugador seleccionado mientras corre a "velocidad de andar normal"*rate. Si no hay jugador seleccionado, modifica tu velocidad. #rate puede ir de 0.1 a 50. |
| modify speed | 2 | `.modify speed $speedtype #rate` | Modifica la velocidad de carrera del jugador seleccionado a "velocidad de carrera base normal"= 1. Si no hay jugador seleccionado, modifica tu velocidad. $speedtypes puede ser fly, all, walk, backwalk o swim. #rate puede ir de 0.1 a 50. |
| modify spell | 2 | | TODO |
| modify standstate | 2 | `.modify standstate #emoteid` | Cambia el emote de tu personaje mientras está de pie a #emoteid. |
| modify talentpoints | 2 | `.modify talentpoints #amount` | Establece los puntos de talento libres para el personaje seleccionado o la mascota del personaje. Se resetearán al valor por defecto esperado en el próximo levelup/login/recompensa de quest. |
| modify | 2 | `.modify $subcommand` | Escribe .modify para ver la lista de posibles subcomandos o .help modify $subcommand para ver información sobre los subcomandos. |
| morph mount | 1 | `.morph mount #displayid` | Cambia el model ID de la montura del objetivo seleccionado a #displayid. |
| morph reset | 1 | `.morph reset` | Resetea el modelo original del objetivo seleccionado. |
| morph target | 1 | `.morph target #displayid` | Cambia el model id actual del objetivo seleccionado a #displayid. |
| morph | 1 | `.morph #displayid` | Cambia tu model id actual a #displayid. |
| movegens | 3 | `.movegens` | Muestra la pila de generadores de movimiento de la creature o jugador seleccionado. |
| mute | 2 | `.mute [$playerName] $timeInMinutes [$reason]` | Desactiva la mensajería de chat para cualquier personaje de la cuenta del personaje $playerName (o el seleccionado actualmente) durante $timeInMinutes minutos. El jugador puede estar offline. |
| mutehistory | 2 | `.mutehistory #accountname` | Muestra el historial de muteos de la cuenta #accountname. |
| nameannounce | 2 | `.nameannounce $announcement` | Envía un anuncio a todos los jugadores online, mostrando el nombre del remitente. |
| neargrave | 2 | `.neargrave [alliance\horde]` | Encuentra el cementerio más cercano vinculado a la zona (o solo el más cercano que acepte fantasmas de facción alliance u horde). |
| notify | 2 | `.notify $MessageToBroadcast` | Envía un mensaje global a todos los jugadores online en pantalla. |
| npc add formation | 3 | `.npc add formation $leader` | Añade la creature seleccionada a la formación de un líder. |
| npc add item | 3 | `.npc add item #itemId <#maxcount><#incrtime><#extendedcost>r` | Añade el item #itemid a la lista de items del vendor seleccionado. También, opcionalmente, establece el count máximo del item en la lista del vendor, el tiempo de restauración del count del item y el ExtendedCost de los items. |
| npc add move | 3 | `.npc add move #creature_guid [#waittime]` | Añade tu ubicación actual como waypoint para la creature con guid #creature_guid. Y, opcionalmente, añade un tiempo de espera. |
| npc add temp | 3 | `.npc add temp` | Añade un NPC temporal, no guardado en la base de datos. |
| npc add | 3 | `.npc add #creatureid` | Spawnea una creature por el id de template dado #creatureid. |
| npc delete item | 3 | `.npc delete item #itemId` | Elimina el item #itemid de la lista de items del vendor seleccionado. |
| npc delete | 3 | `.npc delete [#guid]` | Elimina la creature con guid #guid (o la seleccionada si no se proporciona guid). |
| npc do | 3 | `.npc do $action` | Solicita al NPC que realice DoAction con el ActionID especificado. Se usa para probar scripts. |
| npc follow stop | 2 | `.npc follow stop` | La creature seleccionada (no mascota) deja de seguirte. |
| npc follow | 2 | `.npc follow start` | La creature seleccionada empieza a seguirte hasta la muerte/pelea/etc. |
| npc guid | 1 | `.npc guid` | Pensado para mostrar el GUID de base de datos de la creature objetivo. Actualmente muestra GUID, facción, NPC flags, Entry ID y Model ID de la creature seleccionada. |
| npc info | 1 | `.npc info` | Muestra una lista de detalles de la creature seleccionada. La lista incluye: - GUID, Facción, NPC flags, Entry ID, Model ID, - Nivel, - Salud (actual/máxima), - Field flags, dynamic flags, faction template, - Información de posición, - y el tipo de creature, p. ej. si la creature es un vendor. |
| npc load | 3 | `.npc load #spawnId` | Carga un spawn de creature de la base de datos al mundo por su GUID. |
| npc move | 3 | `.npc move [#creature_guid]` | Mueve el punto de spawn de la creature objetivo a tus coordenadas. |
| npc near | 2 | `.npc near #distance` | Devuelve todos los spawns de creature de la base de datos a una distancia dada. |
| npc playemote | 3 | `.npc playemote #emoteid` | Hace que la creature seleccionada haga un emote con id #emoteid. |
| npc say | 2 | `.npc say $message` | Hace que la creature seleccionada diga el mensaje especificado. |
| npc set | 3 | `.npc set $subcommand` | Escribe .npc set para ver la lista de posibles subcomandos o .help npc set $subcommand para ver información sobre los subcomandos. |
| npc set allowmove | 3 | `.npc set allowmove` | Activa o desactiva el movimiento de las creatures en el mundo. No implementado. |
| npc set data | 3 | `.npc set data $field $data` | Establece data para la creature seleccionada. Se usa para probar Scripting. |
| npc set entry | 3 | `.npc set entry $entry` | Cambia la creature seleccionada por otra entry de creature_template. - El nuevo valor creature.id no se guarda en la BD. |
| npc set faction original | 3 | `.npc set faction original` | Revierte la facción temporal de la creature seleccionada. |
| npc set faction permanent | 3 | `.npc set faction permanent #factionid` | Establece permanentemente la facción de la creature seleccionada a #factionid. |
| npc set faction temp | 3 | `.npc set faction temp #factionid` | Establece temporalmente la facción de la creature seleccionada a #factionid. |
| npc set flag | 3 | `.npc set flag #npcflag` | Establece los NPC flags de la creature template de la creature seleccionada y de la creature seleccionada a #npcflag. Los NPC flags se aplicarán a todas las creatures de la creature template seleccionada tras reiniciar el servidor o descargar/cargar el grid. |
| npc set level | 3 | `.npc set level #level` | Cambia el nivel de la creature seleccionada a #level. #level puede ir de 1 a (CONFIG_MAX_PLAYER_LEVEL) + 3. |
| npc set link | 3 | `.npc set link $creatureGUID` | Vincula el respawn de la creature seleccionada a la condición de que el $creatureGUID definido esté vivo. |
| npc set model | 3 | `.npc set model #displayid` | Cambia el model id de la creature seleccionada a #displayid. |
| npc set movetype | 3 | `.npc set movetype [#creature_guid] stay/random/way [NODEL]` | Establece para la creature señalada por #creature_guid (o la seleccionada si no se proporciona #creature_guid) el tipo de movimiento y la mueve a la posición de respawn (si la creature está viva). Cualquier waypoint existente de la creature se eliminará de la base de datos si no usas NODEL. Si la creature está muerta, el tipo de movimiento se aplicará al respawnear la creature. Asegúrate de usar NODEL si quieres conservar los waypoints. |
| npc set phase | 3 | `.npc set phase #phasemask` | El phasemask de la unidad o mascota seleccionada se cambia a #phasemask con la actualización de visión del mundo correspondiente para los jugadores. En el caso de una creature, el estado se guarda en la BD y es persistente. En el caso de una mascota, el cambio está activo hasta que se cambie la phase en el juego para el propietario, el propietario vuelva a iniciar sesión, o se active/desactive el modo GM. |
| npc set spawntime | 3 | `.npc set spawntime #time` | Ajusta el spawntime de la creature seleccionada a time. |
| npc set wanderdistance | 3 | `.npc set wanderdistance #dist` | Ajusta la wanderdistance de la creature seleccionada a dist. |
| npc showloot | 2 | `.npc showloot` | Muestra el loot generado en el cadáver de la creature seleccionada. |
| npc despawngroup | 3 | `.npc despawngroup #groupId` | Despawnea todas las creatures del spawn group dado. |
| npc spawngroup | 3 | `.npc spawngroup #groupId` | Spawnea todas las creatures del spawn group dado. |
| npc tame | 2 | `.npc tame` | Domestica la creature seleccionada (si es domesticable). |
| npc textemote | 2 | `.npc textemote #emoteid` | Hace que la creature seleccionada haga un textemote con id #emoteid. |
| npc whisper | 2 | `.npc whisper #playerguid #text` | Hace que el npc seleccionado susurre #text a #playerguid. |
| npc yell | 2 | `.npc yell $message` | Hace que la creature seleccionada grite el mensaje especificado. |
| npc | 2 | `.npc $subcommand` | Escribe .npc para ver la lista de posibles subcomandos o .help npc $subcommand para ver información sobre los subcomandos. |
| opendoor | 1 | `.opendoor [$range]` | Abre la puerta más cercana dentro del rango proporcionado (por defecto 5.0yd). |
| packetlog | 2 | `.packetlog [on/off]` | Alterna el logging de paquetes para el personaje. Hay que establecer PacketLogFile con un nombre de archivo válido. |
| pdump load | 3 | `.pdump load $filename $account [$newname] [$newguid]` | Carga un dump de personaje desde un archivo de dump a la lista de personajes de $account con el nombre guardado o $newname, con el guid guardado (o el primero libre) o $newguid. |
| pdump write | 3 | `.pdump write $filename $playerNameOrGUID` | Escribe un dump del personaje con nombre/guid $playerNameOrGUID al archivo $filename. |
| pdump | 3 | `.pdump $subcommand` | Escribe .pdump para ver la lista de posibles subcomandos o .help pdump $subcommand para ver información sobre los subcomandos. |
| pet create | 2 | `.pet create` | Crea una mascota de la creature seleccionada. |
| pet delete | 3 | `.pet delete $ownerName/#GUID $petNumber` | Elimina una mascota específica (por su número de lista de `.pet list`) de la base de datos para el nombre de jugador o GUID dado, desinvocándola primero si está activa actualmente. |
| pet learn | 2 | `.pet learn` | Enseña #spellid a la mascota. |
| pet list | 1 | `.pet list $ownerName/#GUID` | Lista todas las mascotas almacenadas en la base de datos para el nombre de jugador o GUID dado, mostrando el número, nombre, entry, nivel y slot de cada mascota. |
| pet unlearn | 2 | `.pet unlean` | Desaprende #spellid de la mascota. |
| pet | 2 | `.pet $subcommand` | Escribe .pet para ver la lista de posibles subcomandos o .help pet $subcommand para ver información sobre los subcomandos. |
| pinfo | 2 | `.pinfo [$player_name/#GUID]` | Muestra información de cuenta del jugador seleccionado o del jugador encontrado por $player_name o #GUID. |
| playall | 2 | `.playall #soundid` | Reproduce un sonido para todo el servidor. |
| player learn | 2 | `.player learn #playername #spell [all]` | Enseña el hechizo #spell al jugador especificado. Si se añade 'all', se aprenden todos los rangos. |
| player unlearn | 2 | `.player unlearn #playername #spell [all]` | Desaprende el hechizo #spell del jugador especificado. Si se añade 'all', se desaprenden todos los rangos. |
| pooltools | 3 | `.pooltools $subcommand` | Escribe .pooltools para ver la lista de posibles subcomandos. Para usar pooltools, descomenta Appender.Dev y Logger.sql.dev en la configuración del worldserver. |
| pooltools start | 3 | `.pooltools start #description` | Inicia una sesión de pooling con la descripción especificada. |
| pooltools def | 3 | `.pooltools def #GameobjectID #Chance #GameobjectID #Chance (...)` | Define las entries de Gameobject a detectar junto con sus chances asociadas. |
| pooltools add | 3 | `.pooltools add [radius]` | Añade los gameobjects cercanos a la sesión de pooling. El radio por defecto es 5y. |
| pooltools end | 3 | `.pooltools end` | Registra la sesión de pooling actual y la limpia. |
| pooltools remove | 3 | `.pooltools remove` | Elimina el último grupo de la sesión de pooling. |
| pooltools clear | 3 | `.pooltools clear` | Limpia la sesión de pooling actual. |
| possess | 2 | `.possess` | Posee indefinidamente la creature seleccionada. |
| quest add | 2 | `.quest add #quest_id` | Añade al log de quests del personaje la quest #quest_id. Las quests iniciadas desde un item no se pueden añadir con este comando, pero se proporciona la llamada .additem correcta en la salida del comando. |
| quest complete | 2 | `.quest complete #questid` | Marca todos los objetivos de la quest como completados para la quest activa del personaje objetivo. Después de esto, el personaje objetivo puede ir a obtener la recompensa de la quest. |
| quest remove | 2 | `.quest remove #quest_id` | Establece el estado de la quest #quest_id a no completada y no activa (y la elimina de la lista de quests activas) para el jugador seleccionado. |
| quest reward | 2 | `.quest reward #questId` | Otorga la recompensa de la quest al jugador seleccionado y elimina la quest de su log (la quest debe estar en estado completado). |
| quest status | 2 | `.quest status $id [$name]` | Muestra el estado del jugador seleccionado para la quest especificada. |
| quest | 2 | `.quest $subcommand` | Escribe .quest para ver la lista de posibles subcomandos o .help quest $subcommand para ver información sobre los subcomandos. |
| recall | 2 | `.recall [$playername]` | Teletransporta a $playername o al jugador seleccionado al lugar donde estaba antes del último uso de un comando de teletransporte. Si no se introduce $playername y no hay jugador seleccionado, te teletransportará a ti. |
| reload access_requirement | 3 | `.reload access_requirement` | Recarga la tabla access_requirement. |
| reload achievement_reward_locale | 3 | `.reload achievement_reward_locale` | Recarga la tabla achievement_reward_locale. |
| reload achievement_reward | 3 | `.reload achievement_reward` | Recarga la tabla achievement_reward. |
| reload acore_string | 3 | `.reload acore_string` | Recarga la tabla acore_string. |
| reload achievement_criteria_data | 3 | `.reload achievement_criteria_data` | Recarga la tabla achievement_criteria_data. |
| reload all achievement | 3 | `.reload all achievement` | Recarga las tablas achievement_reward, achievement_criteria_data. |
| reload all area | 3 | `.reload all area` | Recarga las tablas areatrigger_teleport, areatrigger_tavern, game_graveyard_zone. |
| reload all gossips | 3 | `.reload all gossips` | Recarga las tablas gossip_menu, gossip_menu_option, gossip_scripts, points_of_interest. |
| reload all item | 3 | `.reload all item` | Recarga las tablas page_text, item_enchantment_table. |
| reload all locales | 3 | `.reload all locales` | Recarga todas las tablas locales_* con soporte de recarga añadido y que se pueden recargar de forma segura. |
| reload all loot | 3 | `.reload all loot` | Recarga todas las tablas *_loot_template. Esta puede ser una operación lenta con lags durante la ejecución del servidor. |
| reload all npc | 3 | `.reload all npc` | Recarga las tablas npc_option, npc_trainer, npc vendor, points of interest. |
| reload all quest | 3 | `.reload all quest` | Recarga todas las tablas relacionadas con quests si se ha añadido soporte de recarga para esa tabla y esta se puede recargar de forma segura. |
| reload all scripts | 3 | `.reload all scripts` | Recarga las tablas gameobject_scripts, event_scripts, quest_end_scripts, quest_start_scripts, spell_scripts, db_script_string, waypoint_scripts. |
| reload all spell | 3 | `.reload all spell` | Recarga todas las tablas spell_* con soporte de recarga añadido y que se pueden recargar de forma segura. |
| reload all | 3 | `.reload all` | Recarga todas las tablas con soporte de recarga añadido y que se pueden recargar de forma segura. |
| reload antidos_opcode_policies | 3 | `.reload antidos_opcode_policies` | Recarga la tabla antidos_opcode_policies. |
| reload areatrigger | 3 | `.reload areatrigger` | Recarga la tabla areatrigger. |
| reload areatrigger_involvedrelation | 3 | `.reload areatrigger_involvedrelation` | Recarga la tabla areatrigger_involvedrelation. |
| reload areatrigger_tavern | 3 | `.reload areatrigger_tavern` | Recarga la tabla areatrigger_tavern. |
| reload areatrigger_teleport | 3 | `.reload areatrigger_teleport` | Recarga la tabla areatrigger_teleport. |
| reload auctions | 3 | `.reload auctions` | Recarga las tablas de datos dinámicos desde la base de datos. |
| reload autobroadcast | 3 | `.reload autobroadcast` | Recarga la tabla autobroadcast. |
| reload battleground_template | 3 | `.reload battleground_template` | Recarga la tabla battleground_template. |
| reload broadcast_text | 3 | `.reload broadcast_text` | Recarga la tabla broadcast_text. |
| reload command | 3 | `.reload command` | Recarga la tabla command. |
| reload conditions | 3 | | Recarga la tabla conditions. |
| reload config | 3 | `.reload config` | Recarga los ajustes de configuración (por defecto almacenados en worldserver.conf). No todos los ajustes se pueden cambiar al recargar: algunos nuevos valores de ajuste se ignorarán hasta reiniciar, algunos valores se aplicarán con retraso o solo a nuevos objetos/mapas, algunos valores se rechazarán explícitamente al recargar. |
| reload chat_filter | 3 | `.reload chat_filter` | Recarga la tabla `chat_filter`. |
| reload creature_linked_respawn | 2 | `.reload creature_linked_respawn` | Recarga la tabla creature_linked_respawn. |
| reload creature_loot_template | 3 | `.reload creature_loot_template` | Recarga la tabla creature_loot_template. |
| reload creature_movement_override | 3 | `.reload creature_movement_override` | Recarga la tabla creature_movement_override. |
| reload creature_onkill_reputation | 3 | `.reload creature_onkill_reputation` | Recarga la tabla creature_onkill_reputation. |
| reload creature_questender | 3 | `.reload creature_questender` | Recarga la tabla creature_questender. |
| reload creature_queststarter | 3 | `.reload creature_queststarter` | Recarga la tabla creature_queststarter. |
| reload creature_template_locale | 3 | `.reload creature_template_locale` | Recarga la tabla creature_template_locale. |
| reload creature_template | 3 | `.reload creature_template $entry` | Recarga la template de la creature especificada. |
| reload creature_text_locale | 3 | `.reload creature_text_locale` | Recarga la tabla creature_text_locale. |
| reload creature_text | 3 | `.reload creature_text` | Recarga la tabla creature_text. |
| reload disables | 3 | `.reload disables` | Recarga la tabla disables. |
| reload disenchant_loot_template | 3 | `.reload disenchant_loot_template` | Recarga la tabla disenchant_loot_template. |
| reload dungeon_access_requirements | 3 | `.reload dungeon_access_requirements` | Recarga la tabla dungeon_access_requirements. |
| reload dungeon_access_template | 3 | `.reload dungeon_access_template` | Recarga la tabla dungeon_access_template. |
| reload event_scripts | 3 | `.reload event_scripts` | Recarga la tabla event_scripts. |
| reload fishing_loot_template | 3 | `.reload fishing_loot_template` | Recarga la tabla fishing_loot_template. |
| reload game_event_npc_vendor | 3 | `.reload game_event_npc_vendor` | Recarga la tabla game_event_npc_vendor. |
| reload game_graveyard | 3 | `.reload game_graveyard` | Recarga la tabla game_graveyard. |
| reload game_tele | 3 | `.reload game_tele` | Recarga la tabla game_tele. |
| reload gameobject_loot_template | 3 | `.reload gameobject_loot_template` | Recarga la tabla gameobject_loot_template. |
| reload gameobject_questender | 3 | `.reload gameobject_questender` | Recarga la tabla gameobject_questender. |
| reload gameobject_queststarter | 3 | `.reload gameobject_queststarter` | Recarga la tabla gameobject_queststarter. |
| reload gameobject_template_locale | 3 | `.reload gameobject_template_locale` | Recarga la tabla gameobject_template_locale. |
| reload gm_tickets | 3 | `.reload gm_tickets` | Recarga la tabla gm_tickets. |
| reload gossip_menu_option_locale | 3 | `.reload gossip_menu_option_locale` | Recarga la tabla gossip_menu_option_locale. |  | reload item_enchantment_template | 3 | `.reload item_enchantment_template` | Recarga la tabla item_enchantment_template. |
| reload gossip_menu_option | 3 | `.reload gossip_menu_option` | Recarga la tabla gossip_menu_option. |
| reload gossip_menu | 3 | `.reload gossip_menu` | Recarga la tabla gossip_menu. |
| reload graveyard_zone | 3 | `.reload graveyard_zone` | Recarga la tabla graveyard_zone. |
| reload item_enchantment_template | 3 | `.reload item_enchantment_template` | Recarga la tabla item_enchantment_template. |
| reload item_loot_template | 3 | `.reload item_loot_template` | Recarga la tabla item_loot_template. |
| reload item_set_name_locale | 3 | `.reload item_set_name_locale` | Recarga la tabla item_set_name_locale. |
| reload item_set_names | 3 | `.reload item_set_names` | Recarga la tabla item_set_names. |
| reload item_template_locale | 3 | `.reload item_template_locale` | Recarga la tabla item_template_locale. |
| reload lfg_dungeon_rewards | 3 | `.reload lfg_dungeon_rewards` | Recarga la tabla lfg_dungeon_rewards. |
| reload mail_level_reward | 3 | `.reload mail_level_reward` | Recarga la tabla mail_level_reward. |
| reload mail_loot_template | 3 | `.reload quest_mail_loot_template` | Recarga la tabla quest_mail_loot_template. |
| reload mail_server_template | 3 | `.reload mail_server_template` | Recarga la tabla mail_server_template. |
| reload milling_loot_template | 3 | `.reload milling_loot_template` | Recarga la tabla milling_loot_template. |
| reload module_string | 3 | `.reload module_string` | Recarga la tabla module_string. |
| reload motd | 3 | `.reload motd` | Recarga la tabla motd. |
| reload npc_spellclick_spells | 3 | `.reload npc_spellclick_spells` | Recarga la tabla npc_spellclick_spells. |
| reload npc_text_locale | 3 | `.reload npc_text_locale` | Recarga la tabla npc_text_locale. |
| reload trainer | 3 | `.reload trainer` | Recarga las tablas trainer, trainer_locale, trainer_spell y creature_default_trainer. |
| reload npc_vendor | 3 | `.reload npc_vendor` | Recarga la tabla npc_vendor. |
| reload page_text_locale | 3 | `.reload page_text_locale` | Recarga la tabla page_tex_locale. |
| reload page_text | 3 | `.reload page_text` | Recarga la tabla page_text. |
| reload pickpocketing_loot_template | 3 | `.reload pickpocketing_loot_template` | Recarga la tabla pickpocketing_loot_template. |
| reload player_loot_template | 3 | `.reload player_loot_template` | Recarga la tabla player_loot_template. |
| reload points_of_interest_locale | 3 | `.reload points_of_interest_locale` | Recarga la tabla points_of_interest_locale. |
| reload points_of_interest | 3 | `.reload points_of_interest` | Recarga la tabla points_of_interest. |
| reload profanity_name | 3 | `.reload profanity_name` | Recarga la tabla profanity_name. |
| reload prospecting_loot_template | 3 | `.reload prospecting_loot_template` | Recarga la tabla prospecting_loot_template. |
| reload quest_greeting | 3 | `.reload quest_greeting` | Recarga la tabla quest_greeting. |
| reload quest_offer_reward_locale | 3 | `.reload quest_offer_reward_locale` | Recarga la tabla quest_offer_reward_locale. |
| reload quest_poi | 3 | `.reload quest_poi` | Recarga la tabla quest_poi. |
| reload quest_request_item_locale | 3 | `.reload quest_request_item_locale` | Recarga la tabla quest_request_item_locale. |
| reload quest_template_locale | 3 | `.reload quest_template_locale` | Recarga la tabla quest_template_locale. |
| reload quest_template | 3 | `.reload quest_template` | Recarga la tabla quest_template. |
| reload reference_loot_template | 3 | `.reload reference_loot_template` | Recarga la tabla reference_loot_template. |
| reload reputation_reward_rate | 3 | `.reload reputation_reward_rate` | Recarga la tabla reputation_reward_rate. |
| reload reputation_spillover_template | 3 | `.reload reputation_spillover_template` | Recarga la tabla reputation_spillover_template. |
| reload reserved_name | 3 | `.reload reserved_name` | Recarga la tabla reserved_name. |
| reload skill_discovery_template | 3 | `.reload skill_discovery_template` | Recarga la tabla skill_discovery_template. |
| reload skill_extra_item_template | 3 | `.reload skill_extra_item_template` | Recarga la tabla skill_extra_item_template. |
| reload skill_fishing_base_level | 3 | `.reload skill_fishing_base_level` | Recarga la tabla skill_fishing_base_level. |
| reload skinning_loot_template | 3 | `.reload skinning_loot_template` | Recarga la tabla skinning_loot_template. |
| reload smart_scripts | 3 | `.reload smart_scripts` | Recarga la tabla smart_scripts. |
| reload spawn_group | 3 | `.reload spawn_group` | Recarga las tablas spawn_group_template y spawn_group. |
| reload spell_area | 3 | `.reload spell_area` | Recarga la tabla spell_area. |
| reload spell_bonus_data | 3 | `.reload spell_bonus_data` | Recarga la tabla spell_bonus_data. |
| reload spell_group_stack_rules | 3 | `.reload spell_group` | Recarga la tabla spell_group_stack_rules. |
| reload spell_group | 3 | `.reload spell_group` | Recarga la tabla spell_group. |
| reload spell_linked_spell | 3 | `.reload spell_linked_spell` | Recarga la tabla de BD spell_linked_spell. |
| reload spell_loot_template | 3 | `.reload spell_loot_template` | Recarga la tabla spell_loot_template. |
| reload spell_pet_auras | 3 | `.reload spell_pet_auras` | Recarga la tabla spell_pet_auras. |
| reload spell_proc_event | 3 | `.reload spell_proc_event` | Recarga la tabla spell_proc_event. |
| reload spell_proc | 3 | `.reload spell_proc` | Recarga la tabla spell_proc. |
| reload spell_required | 3 | `.reload spell_required` | Recarga la tabla spell_required. |
| reload spell_scripts | 3 | `.reload spell_scripts` | Recarga la tabla spell_scripts. |
| reload spell_target_position | 3 | `.reload spell_target_position` | Recarga la tabla spell_target_position. |
| reload spell_threats | 3 | `.reload spell_threats` | Recarga la tabla spell_threats. |
| reload vehicle_accessory | 3 | `.reload vehicle_accessory` | Recarga las definiciones de accesorios de vehículo basadas en GUID desde la base de datos. |
| reload vehicle_template_accessory | 3 | `.reload vehicle_template_accessory` | Recarga las definiciones de accesorios de vehículo basadas en entry desde la base de datos. |
| reload warden_action | 3 | `.reload warden_action` | Recarga la tabla warden_action. |
| reload waypoint_data | 3 | `.reload waypoint_data` | Recargará la tabla waypoint_data. |
| reload waypoint_scripts | 3 | `.reload waypoint_scripts` | Recarga la tabla waypoint_scripts. |
| reload | 3 | `.reload $subcommand` | Escribe .reload para ver la lista de posibles subcomandos o .help reload $subcommand para ver información sobre los subcomandos. |
| reset achievements | 4 | `.reset achievements [$playername]` | Resetea los datos de achievements del personaje seleccionado o nombrado (online u offline). Los achievements de datos de progreso persistente como quests completadas/etc se rellenan de nuevo al resetear. Los achievements de eventos como muertes/lanzamientos/etc se perderán. |
| reset all | 4 | `.reset all [spells/talents]` | Solicita resetear los hechizos o talentos (incluyendo los talentos de todas las mascotas del personaje, si las hay) en el próximo login de cada personaje existente. |
| reset honor | 3 | `.reset honor [Playername]` | Resetea todos los datos de honor del personaje objetivo. |
| reset items | 3 | `.reset items equipped\|bags\|bank\|keyring\|currency\|vendor_buyback\|all\|allbags [$playername]` | Elimina items del inventario del jugador según la opción elegida. |
| reset items all | 3 | `.reset items all [$playername]` | Elimina todos los items del inventario del jugador seleccionado (equipados, en bolsas, en el banco, en el llavero, en la lista de monedas y en la pestaña de recompra del vendor). |
| reset items allbags | 3 | `.reset items allbags [$playername]` | Elimina todos los items del inventario del jugador seleccionado, incluidas las propias bolsas. |
| reset items bags | 3 | `.reset items bags [$playername]` | Elimina todos los items de las bolsas del jugador seleccionado. |
| reset items bank | 3 | `.reset items bank [$playername]` | Elimina todos los items del banco del jugador seleccionado. |
| reset items currency | 3 | `.reset items currency [$playername]` | Elimina todos los items de la lista de monedas del jugador seleccionado. |
| reset items equipped | 3 | `.reset items equipped [$playername]` | Elimina todos los items equipados en el jugador objetivo. |
| reset items keyring | 3 | `.reset items keyring [$playername]` | Elimina todos los items del llavero del jugador seleccionado. |
| reset items vendor_buyback | 3 | `.reset items vendor_buyback [$playername]` | Elimina todos los items de la pestaña de recompra del vendor del jugador seleccionado. |
| reset level | 3 | `.reset level [Playername]` | Resetea el nivel a 1 incluyendo el reseteo de stats y talentos. Se pueden perder items equipados con un requisito de nivel mayor. |
| reset spells | 3 | `.reset spells [Playername]` | Elimina todos los hechizos no originales del libro de hechizos. Playername puede ser el nombre de un personaje offline. |
| reset stats | 3 | `.reset stats [Playername]` | Resetea (recalcula) todas las stats del jugador objetivo a sus valores originales en el nivel actual. |
| reset talents | 3 | `.reset talents [Playername]` | Elimina todos los talentos del jugador objetivo o de su mascota o del jugador nombrado. Playername puede ser el nombre de un personaje offline. Con los talentos del jugador también se resetearán los talentos de todas las mascotas del personaje, si las hay. |
| reset | 3 | `.reset $subcommand` | Escribe .reset para ver la lista de posibles subcomandos o .help reset $subcommand para ver información sobre los subcomandos. |
| respawn | 2 | `.respawn` | Respawnea la creature y GO objetivo sin esperar a que expire el tiempo de respawn. Si no se proporciona objetivo, respawnea todas las creatures más cercanas. |
| respawn all | 2 | `.respawn all` | Respawnea todas las creatures y gameobjects más cercanos sin esperar a que expire el tiempo de respawn. También fuerza el respawn de todos los respawns de spawn group pendientes en el mapa actual. |
| revive | 2 | `.revive` | Revive al jugador seleccionado. Si no hay jugador seleccionado, te revivirá a ti. |
| save | 0 | `.save` | Guarda tu personaje. |
| saveall | 2 | `.saveall` | Guarda todos los personajes en el juego. |
| send | 2 | `.send $subcommand` | Escribe .send para ver una lista de posibles subcomandos o .help send $subcommand para ver información sobre el subcomando. |
| send items | 2 | `.send items #playername "#subject" "#text" itemid1[:count1] itemid2[:count2] ... itemidN[:countN]` | Envía un correo a un jugador. El asunto y el texto del correo deben ir entre "". Si para un itemid no se proporciona el valor de count, se espera 1; si count > máximo de items en un stack, los items se enviarán en la cantidad de stacks necesaria. La cantidad total de stacks en un correo está limitada a 12. |
| send mail | 2 | `.send mail #playername "#subject" "#text"` | Envía un correo a un jugador. El asunto y el texto del correo deben ir entre "". |
| send message | 3 | `.send message $playername $message` | Envía un mensaje en pantalla al jugador de parte de ADMINISTRATOR. **¡Devolverá un error si el jugador está offline (puede ser problemático con SOAP, por ejemplo)!** |
| send money | 2 | `.send money #playername "#subject" "#text" $money` | Envía un correo con dinero a un jugador. El asunto y el texto del correo deben ir entre "". El dinero se puede especificar como una cantidad de cobre en bruto (p. ej. `1000`) o como una cadena de moneda usando los sufijos `g`/`s`/`c` para oro/plata/cobre (p. ej. `1g2s3c`, `5g`, `50s`). |
| server corpses | 2 | `.server corpses` | Dispara la comprobación de expiración de cadáveres en el mundo. |
| server debug | 3 | `.server debug` | Muestra información detallada sobre la configuración del servidor, útil al reportar un bug. |
| server exit | 4 | `.server exit` | Termina el worldserver AHORA. Código de salida 0. |
| server idlerestart cancel | 3 | `.server idlerestart cancel` | Cancela el temporizador de reinicio/apagado, si lo hay. |
| server idlerestart | 4 | `.server idlerestart #delay [#exit_code]` | Reinicia el servidor tras #delay segundos si no hay conexiones activas presentes (sin jugadores). Usa #exit_code para cambiar el código de salida, por defecto = 2. |
| server idleshutdown cancel | 4 | `.server idleshutdown cancel` | Cancela el temporizador de reinicio/apagado, si lo hay. |
| server idleshutdown | 3 | `.server idleshutdown #delay [#exit_code]` | Apaga el servidor tras #delay segundos si no hay conexiones activas presentes (sin jugadores). Usa #exit_code para cambiar el código de salida, por defecto = 0. |
| server info | 0 | `.server info` | Muestra la versión del servidor y el número de jugadores conectados. |
| server motd | 0 | `.server motd` | Muestra el Mensaje del día del servidor. |
| server restart cancel | 3 | `.server restart cancel` | Cancela el temporizador de reinicio/apagado, si lo hay. |
| server restart | 3 | `.server restart #delay [#exit_code]` | Reinicia el servidor tras #delay segundos. Usa #exit_code para cambiar el código de salida, por defecto = 2. |
| server set closed | 4 | `.server set closed [on/off]` | Establece si el mundo acepta nuevas conexiones de cliente. |
| server set difftime | 4 | `.server set difftime $time` | Cada $time (en milisegundos) se escribe el update time diff en el archivo de log. |
| server set loglevel | 4 | `.server set loglevel $facility $name $loglevel` | $facility puede tomar los valores: appender (a) o logger (l). $loglevel puede tomar los valores: disabled (0), trace (1), debug (2), info (3), warn (4), error (5) o fatal (6). |
| server set motd | 3 | `.server set motd Optional($realmId) $MOTD` | Establece el Mensaje del día del servidor para el $realmId especificado. Si no se proporciona $realmId, se actualizará para el realm actual. Usa $realmId -1 para establecer el motd para todos los realms. |
| server set security | 4 | `.server set security $level` | Establece el nivel de seguridad de cuenta mínimo (0 = jugador, 1 = moderador, 2 = gamemaster, 3 = administrador) permitido para iniciar sesión en el realm actual. Actualiza realmlist.allowedSecurityLevel y se aplica de inmediato. |
| server shutdown cancel | 3 | `.server shutdown cancel` | Cancela el temporizador de reinicio/apagado, si lo hay. |
| server shutdown | 3 | `.server shutdown #delay [#exit_code]` | Apaga el servidor tras #delay segundos. Usa #exit_code para cambiar el código de salida, por defecto = 0. |
| server togglequerylog | 4 | `.server togglequerylog` | Alterna el log de consultas SQL on/off. |
| server | 3 | `.server $subcommand` | Escribe .server para ver la lista de posibles subcomandos o .help server $subcommand para ver información sobre los subcomandos. |
| settings | 1 | `.settings $subcommand` | Escribe .settings para ver la lista de todos los comandos disponibles. |
| settings announcer | 1 | `.settings announcer <type> <on/off>` | Desactiva la recepción de anuncios. Los tipos de anuncio válidos son: 'autobroadcast', 'arena', 'bg', 'pvpstart' y 'pvpall'. |
| setskill | 2 | `.setskill #skill #level [#max]` | Establece un skill con id #skill con un valor de skill actual de #level y un valor máximo de #max (o igual al máximo actual si no se proporciona) para el personaje seleccionado. Si no hay personaje seleccionado, tú aprendes el skill. |
| showarea | 2 | `.showarea #areaid` | Revela el área con #areaid al personaje seleccionado. Si no hay personaje seleccionado, revela esta área para ti. |
| skirmish | 3 | `.skirmish [arena] [XvX] [Nick1] [Nick2] ... [NickN]` | [arena] puede ser "all" o una lista separada por comas de arenas posibles (NA,BE,RL,DS,RV). [XvX] puede ser 1v1, 2v2, 3v3, 5v5. Después de [XvX] especifica suficientes nicknames para ese modo. |
| spect | 0 | `.spect $subcommand` | Escribe .spect para ver la lista de posibles subcomandos o .help spect $subcommand para ver información sobre los subcomandos. |
| spect leave | 0 | `.spect leave` | Sale del modo espectador de arena. |
| spect reset | 0 | `.spect reset` | Resetea el espectador de arena. |
| spect spectate | 0 | `.spect spectate #playername` | Inicia el espectador de arena, observa a #playername. |
| spect version | 0 | `.spect version` | Comprueba la versión del addon de espectador. |
| spect watch | 0 | `.spect watch #playername` | Observa a #playername. |
| spellinfo | 2 | `.spellinfo $subcommand` | Escribe .spellinfo para ver una lista de subcomandos o .help spellinfo $subcommand para ver información sobre los subcomandos. |
| spellinfo all | 2 | `.spellinfo all #spellid` | Muestra todos los datos disponibles del hechizo #spellid incluyendo atributos, propiedades generales, efectos y objetivos. |
| spellinfo attributes | 2 | `.spellinfo attributes #spellid` | Muestra información básica y los flags de atributo del hechizo #spellid incluyendo SpellAttr0-7, atributos personalizados, stances, tipo de dispel y mechanic. |
| spellinfo effects | 2 | `.spellinfo effects #spellid` | Muestra los datos de efecto del hechizo #spellid incluyendo tipo de efecto, tipo de aura, base points, multiplicadores, misc values, mechanic, trigger spell, amplitude y class mask por efecto. |
| spellinfo targets | 2 | `.spellinfo targets #spellid` | Muestra los datos de objetivo del hechizo #spellid incluyendo target mask, tipo de creature, máximo de objetivos afectados, y por efecto TargetA, TargetB, radio y chain targets. |
| string | 2 | `.string #id [#locale]` | Muestra una cadena del servidor por su ID y locale opcional. |
| summon | 2 | `.summon [$charactername]` | Teletransporta al personaje dado hacia ti. El personaje puede estar offline. |
| teleport add | 3 | `.teleport add $name` | Añade tu posición actual a la lista de ubicaciones objetivo del comando .teleport con el nombre $name. |
| teleport del | 3 | `.teleport del $name` | Elimina la ubicación con nombre $name de la lista de ubicaciones del comando .teleport. |
| teleport group | 2 | `.teleport group#location` | Teletransporta al jugador seleccionado y a los miembros de su grupo a una ubicación dada. |
| teleport name | 2 | `.teleport name [#playername] #location` | Teletransporta al personaje dado a una ubicación dada. El personaje puede estar offline. Para teletransportar al homebind, establece #location como "$home" (sin comillas). |
| teleport name npc guid | 2 | `.teleport name npc guid $playername #creatureSpawnId` | Teletransporta al personaje dado a la creature con spawn id #creatureSpawnId. El personaje puede estar offline. |
| teleport name npc id | 2 | `.teleport name npc id $playername #creatureId` | Teletransporta al personaje dado a la primera creature encontrada con id #creatureId. El personaje puede estar offline. |
| teleport name npc name | 2 | `.teleport name npc name $playername #creatureName` | Teletransporta al personaje dado a la primera creature encontrada con nombre (debe coincidir exactamente) #creatureName. El personaje puede estar offline. |
| teleport | 1 | `.teleport #location` | Teletransporta al jugador a una ubicación dada. |
| ticket assign | 2 | `.ticket assign $ticketid $gmname` | Asigna el ticket especificado al Game Master especificado. |
| ticket close | 2 | `.ticket close $ticketid` | Cierra el ticket especificado. No lo elimina permanentemente. |
| ticket closedlist | 2 | | Muestra una lista de tickets GM cerrados. |
| ticket comment | 2 | `.ticket comment $ticketid $comment` | Permite añadir o modificar un comentario al ticket especificado. |
| ticket complete | 2 | `.ticket complete #ticketID` | Marca un ticket del ID dado como completado. |
| ticket delete | 3 | `.ticket delete $ticketid` | Elimina el ticket especificado permanentemente. El ticket debe cerrarse primero. |
| ticket escalate | 2 | `.ticket escalate $ticketid` | Coloca el ticket especificado en la cola de escalación. |
| ticket escalatedlist | 2 | | Muestra todos los tickets en la cola de escalación. |
| ticket list | 2 | | Muestra una lista de tickets GM abiertos. |
| ticket onlinelist | 2 | | Muestra una lista de tickets GM abiertos cuyo propietario está online. |
| ticket reset | 2 | `.ticket reset` | Elimina todos los tickets cerrados y resetea el contador, si no hay tickets abiertos pendientes. |
| ticket response | 2 | `.ticket response $subcommand` | Escribe .ticket response para ver la lista de posibles subcomandos o .help ticket response $subcommand para ver información sobre los subcomandos. |
| ticket response append | 2 | `.ticket response append $ticketId $response` | Añade una respuesta al ticket especificado (sin salto de línea). |
| ticket response appendln | 2 | `.ticket response appendln $ticketId $response` | Añade una respuesta al ticket especificado (con salto de línea). |
| ticket response delete | 2 | `.ticket response delete $ticketId` | Elimina una respuesta de un ticket. |
| ticket response show | 2 | `.ticket response show $ticketId` | Muestra una respuesta de un ticket. |
| ticket togglesystem | 4 | `.ticket togglesystem` | Alterna el sistema de tickets on/off. |
| ticket unassign | 2 | `.ticket unassign $ticketid` | Desasigna el ticket especificado del Game Master actualmente asignado. |
| ticket viewid | 2 | `.ticket viewid $ticketid` | Devuelve detalles sobre el ticket especificado. El ticket debe estar abierto y no eliminado. |
| ticket viewname | 2 | `.ticket viewname $creatorname` | Devuelve detalles sobre el ticket especificado. El ticket debe estar abierto y no eliminado. |
| ticket | 2 | `.ticket $subcommand` | Escribe .ticket para ver la lista de posibles subcomandos o .help ticket $subcommand para ver información sobre los subcomandos. |
| titles | 2 | `.titles $subcommand` | Escribe .titles para ver la lista de posibles subcomandos o .help titles $subcommand para ver información sobre los subcomandos. |
| titles add | 2 | `.titles add #title` | Añade el título #title (id o shift-link) a la lista de títulos conocidos del jugador seleccionado. |
| titles current | 2 | `.titles current #title` | Establece el título #title (id o shift-link) como título actualmente seleccionado para el jugador seleccionado. Si el título no está en la lista de títulos conocidos del jugador, se añadirá a la lista. |
| titles remove | 2 | `.titles remove #title` | Elimina el título #title (id o shift-link) de la lista de títulos conocidos del jugador seleccionado. |
| titles set | 2 | `.titles set $subcommand` | Escribe .titles set para ver la lista de posibles subcomandos o .help titles set $subcommand para ver información sobre los subcomandos. |
| titles set mask | 2 | `.titles set mask #mask` | Permite al usuario usar todos los títulos de #mask. #mask=0 desactiva el campo de elección de título. |
| unaura | 2 | `.unaura #spellid` | Elimina el aura del hechizo #spellid de la Unidad seleccionada. |
| unban account | 3 | `.unban account $Name` | Desbanea cuentas para un patrón de nombre de cuenta. |
| unban character | 3 | `.unban character $Name` | Desbanea cuentas para un patrón de nombre de personaje. |
| unban ip | 3 | `.unban ip $Ip` | Desbanea cuentas para un patrón de IP. |
| unban playeraccount | 3 | `.unban playeraccount $characterName` | Desbanea la cuenta propietaria del personaje con el nombre de personaje designado. |
| unban | 3 | `.unban $subcommand` | Escribe .unban para ver la lista de posibles subcomandos o .help unban $subcommand para ver información sobre los subcomandos. |
| unbindsight | 3 | `.unbindsight` | Elimina la visión vinculada. No se puede usar mientras se está poseyendo un objetivo. |
| unfreeze | 2 | `.unfreeze (#player)` | "Descongela" a #player y vuelve a activar su chat. Al usar esto sin #name descongelará a tu objetivo. |
| unlearn | 2 | `.unlearn #spell [all]` | Desaprende para el jugador seleccionado un hechizo #spell. Si se proporciona 'all', se desaprenden todos los rangos. |
| unmute | 2 | `.unmute [$playerName]` | Restaura la mensajería de chat para cualquier personaje de la cuenta del personaje $playerName (o el seleccionado). El personaje puede estar offline. |
| unpossess | 2 | `.unpossess` | Si estás poseído, deja de poseerte; de lo contrario, deja de poseer al objetivo poseído actual. |
| unstuck | 2 | `.unstuck $playername [inn/graveyard/startzone]` | Teletransporta al jugador especificado a la ubicación especificada. La ubicación por defecto es la ubicación de hearth actual del jugador. |
| wchange | 3 | `.wchange #weathertype #grade` | Establece el clima actual a #weathertype con una intensidad de #grade. <br/>`#weathertype` puede ser 0 para despejado, 1 para lluvia, 2 para nieve, 3 para tormenta, 86 para truenos, 90 para lluvia negra.<br/>`#grade` es un valor float de 0.0 (desactivado) a 1.0 (intensidad máxima).' |
| whispers | 1 | `.whispers on\off` | Activa/desactiva la aceptación de susurros por parte del GM de los jugadores. Por defecto usa el ajuste de worldserver.conf. |
| worldstate scourgeinvasion battleswon | 3 | `.worldstate scourgeinvasion battleswon <value>` | Ajusta el recuento de batallas ganadas de la Scourge Invasion en <value> (puede ser negativo). |
| worldstate scourgeinvasion show | 3 | `.worldstate scourgeinvasion show` | Muestra el estado actual de la Scourge Invasion. |
| worldstate scourgeinvasion startzone | 3 | `.worldstate scourgeinvasion startzone <id>` | Inicia un evento de Scourge Invasion en la zona especificada por <id>. IDs de zona válidos: 0-7. |
| worldstate scourgeinvasion state | 3 | `.worldstate scourgeinvasion state <value>` | Establece el estado de la Scourge Invasion. Valores válidos: 0 = Deshabilitado, 1 = Habilitado. |
| worldstate sunsreach counter | 3 | `.worldstate sunsreach counter <index> <value>` | Establece un contador de worldstate de Suns Reach y muestra el estado actual de Suns Reach. |
| worldstate sunsreach gate | 3 | `.worldstate sunsreach gate <gate>` | Establece la fase de la Sunwell Plateau Gate. Valores válidos: 0 = Todas las puertas cerradas, 1 = Puerta 1 Agamath abierta, 2 = Puerta 2 Rohendar abierta, 3 = Puerta 3 Archonisus abierta. |
| worldstate sunsreach gatecounter | 3 | `.worldstate sunsreach gatecounter <index> <value>` | Establece un contador de progresión de puerta de Sunwell y muestra el estado actual de las puertas de Suns Reach. |
| worldstate sunsreach phase | 3 | `.worldstate sunsreach phase <value>` | Establece la fase de Sun's Reach. Valores válidos: 0 = Staging Area, 1 = Sanctum, 2 = Armory, 3 = Harbor. |
| worldstate sunsreach status | 3 | `.worldstate sunsreach status` | Muestra el estado actual de progresión de Suns Reach y de las puertas de Sunwell. |
| worldstate sunsreach subphase | 3 | `.worldstate sunsreach subphase <mask>` | Establece la máscara de subfase de Sun's Reach. Valores válidos: 1 = Portal, 2 = Anvil, 4 = Alchemy Lab, 8 = Monument, 15 = Todo. |
| wp | 3 | `.wp $subcommand` | Escribe .wp para ver una lista de posibles subcomandos o .help wp $subcommand para ver información sobre el subcomando. |
| wp add | 3 | `.wp add` | Añade un waypoint para la creature seleccionada en tu posición actual. |
| wp event | 3 | `.wp event $subcommand` | Escribe .path event para ver la lista de posibles subcomandos o .help path event $subcommand para ver información sobre los subcomandos. |
| wp load | 3 | `.wp load $pathid` | Carga el número pathid para la creature seleccionada. La creature no debe tener datos de waypoint. |
