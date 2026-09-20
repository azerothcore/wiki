# El sistema ScriptAI

El sistema ScriptAI implementado por AC utiliza una estrategia especial: [Patrón del observador](https://en.wikipedia.org/wiki/Observer_pattern) para implementar una programación dirigida por eventos que es también el **CORE** de nuestro sistema modular.

Esta guía, junto con nuestro [sistema de módulos](create-a-module) te permite ampliar el AzerothCore sin parchearlo directamente. ¡Esto le permite actualizar su repositorio manteniendo sus adiciones y personalizaciones libres de conflictos!

## Recursos

### Lista de hooks

El catálogo completo de hooks está documentado en [Referencia de hooks C++](hooks-script-reference) y refleja las declaraciones del archivo [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h).

### Referencia de hooks

AzerothCore agrupa sus hooks de C++ por **tipo de script** dentro de `ScriptMgr.h`.

Elige el tipo de script que coincida con el subsistema que quieres extender y luego revisa esa clase en `ScriptMgr.h` para ver las firmas completas y la lista completa de callbacks disponibles.

#### Hooks de ciclo de vida y del servidor

| Tipo de script | Úsalo para | Hooks de ejemplo |
| --- | --- | --- |
| `ServerScript` | Inicio de red, sockets y filtrado de paquetes | `OnNetworkStart`, `CanPacketReceive`, `CanPacketSend` |
| `WorldScript` | Ciclo de vida del servidor, carga de configuración y actualizaciones del mundo | `OnBeforeConfigLoad`, `OnStartup`, `OnShutdown` |
| `FormulaScript` | Fórmulas de juego y cálculo de ratings | `OnHonorCalculation`, `OnGainCalculation`, `OnAfterArenaRatingCalculation` |
| `CommandScript` | Registrar comandos de chat | `GetChatCommands` |

#### Hooks de entidades y mapas

| Tipo de script | Úsalo para | Hooks de ejemplo |
| --- | --- | --- |
| `MapScript` | Creación de mapas, descarga y actualizaciones por mapa | `OnCreateMap`, `OnPlayerEnterMap`, `OnMapUpdate` |
| `InstanceMapScript` | Proporcionar la implementación de `InstanceScript` para un mapa de instancia | `CreateInstanceScript` |
| `PlayerScript` | Login, progreso, inventario, chat, campos de batalla y muchos otros eventos del jugador | `OnPlayerLogin`, `OnPlayerGiveXP`, `OnPlayerBeforeTeleport` |
| `UnitScript` | Eventos genéricos de combate y auras para cualquier unidad | `OnHeal`, `OnDamage`, `OnUnitDeath` |
| `CreatureScript` | Gossip de NPC, quests y asociación con `CreatureAI` personalizado | `OnGossipHello`, `OnQuestReward`, `GetCreatureAI` |
| `GameObjectScript` | Gossip de gameobjects, cambios de estado y asociación con `GameObjectAI` personalizado | `OnGossipHello`, `OnGameObjectStateChanged`, `GetGameObjectAI` |
| `ItemScript` | Uso de ítems, quests de ítems y gossip de ítems | `OnItemUse`, `OnQuestAccept`, `OnGossipSelect` |
| `AreaTriggerScript` | Activación de area triggers | `OnAreaTrigger` |
| `BattlegroundScript` | Creación de implementaciones personalizadas de battlegrounds | `CreateBattleground` |
| `OutdoorPvPScript` | Creación de implementaciones personalizadas de outdoor PvP | `CreateOutdoorPvP` |
| `VehicleScript` | Ciclo de vida de vehículos, asientos y pasajeros | `OnInstall`, `OnAddPassenger`, `OnRemovePassenger` |
| `DynamicObjectScript` | Actualizaciones de objetos dinámicos | `OnDynamicObjectUpdate` |
| `TransportScript` | Movimiento de transportes y pasajeros | `OnTransportUpdate`, `OnAddPassenger`, `OnRelocate` |
| `WeatherScript` | Cambios de clima y ticks | `OnWeatherChange`, `OnWeatherUpdate` |

#### Hooks de sistemas y reglas del juego

| Tipo de script | Úsalo para | Hooks de ejemplo |
| --- | --- | --- |
| `AccountScript` | Login de cuenta y eventos de administración de cuentas | `OnAccountLogin`, `OnPasswordChange`, `CanAccountCreateCharacter` |
| `GuildScript` | Eventos de hermandad y comportamiento del banco de hermandad | `OnGuildAddMember`, `OnGuildDisband`, `CanGuildSendBankList` |
| `GroupScript` | Invitaciones a grupos, expulsiones y validaciones de cola de BG | `OnGroupAddMember`, `OnGroupDisband`, `CanGroupJoinBattlegroundQueue` |
| `GlobalScript` | Hooks transversales usados por varios sistemas | `OnArenaWeekReset`, `OnLoadSpellCustomAttr`, `OnBeforeSetBossState` |
| `MovementHandlerScript` | Paquetes de movimiento del jugador | `OnPlayerMove` |
| `AllCreatureScript` | Hooks que se ejecutan para todas las criaturas | `OnBeforeCreatureSelectLevel`, `OnCreatureSaveToDB` |
| `AllGameObjectScript` | Hooks que se ejecutan para todos los gameobjects | `OnGameObjectSaveToDB` |
| `AllMapScript` | Hooks transversales para la creación de `InstanceScript` y la destrucción de instancias | `OnBeforeCreateInstanceScript`, `OnDestroyInstance` |
| `BattlefieldScript` | Eventos de battlefields exteriores | `OnBattlefieldPlayerEnterZone`, `OnBattlefieldWarEnd` |
| `BGScript` | Flujo de battlegrounds y colas | `OnBattlegroundStart`, `OnQueueUpdate`, `OnBeforeSendJoinMessageArenaQueue` |
| `ArenaScript` | Reglas de las partidas de arena y comportamiento de actualización de miembros | `OnArenaStart`, `OnBeforeArenaCheckWinConditions`, `OnAddMember` |
| `ArenaTeamScript` | Cálculo de slots y puntos de arena teams | `OnGetSlotByType`, `OnGetArenaPoints`, `OnSetArenaMaxPlayersPerTeam` |
| `AuctionHouseScript` | Eventos de subastas y comportamiento del correo de subastas | `OnAuctionAdd`, `OnAuctionExpire`, `OnBeforeAuctionHouseMgrSendAuctionWonMail` |
| `ConditionScript` | Validaciones de condiciones personalizadas | `OnConditionCheck` |
| `GameEventScript` | Eventos de juego estacionales o programados | `OnGameEventStart`, `OnGameEventStop` |
| `WorldObjectScript` | Ciclo de vida genérico de world objects y actualizaciones de mapa | `OnWorldObjectCreate`, `OnWorldObjectDestroy`, `OnWorldObjectUpdate` |
| `LootScript` | Eventos relacionados con el loot | `OnLootMoney` |
| `TicketScript` | Eventos del ciclo de vida de tickets de GM | `OnTicketCreate`, `OnTicketStatusUpdate`, `OnTicketResolve` |
| `MiscScript` | Hooks transversales de objetos, ítems y utilidades | `OnConstructObject`, `OnItemCreate`, `CanApplySoulboundFlag` |
| `CommandSC` | Manejadores internos de ejecución de comandos | `OnHandleDevCommand`, `OnTryExecuteCommand`, `OnBeforeIsInvokerVisible` |
| `DatabaseScript` | Hooks del ciclo de vida y de revisión de bases de datos de módulos | `OnModuleDatabasesLoading`, `OnAfterDatabasesLoaded`, `OnDatabaseGetDBRevision` |
| `MailScript` | Personalización del envío de correo | `OnBeforeMailDraftSendMailTo` |
| `AchievementScript` | Flujo de logros y criterios | `SetRealmCompleted`, `CanCheckCriteria` |
| `AchievementCriteriaScript` | Validaciones de criterios vinculadas a un ID controlado por un script | `OnCriteriaCheck` |
| `PetScript` | Estadísticas, talentos y validaciones de mascotas | `OnInitStatsForLevel`, `CanResetTalents` |
| `SpellSC` | Hooks globales del sistema de hechizos expuestos por `ScriptMgr` | `OnSpellCheckCast`, `OnSpellCast`, `OnCalcMaxDuration` |

Para manejadores específicos de hechizos implementados con `SpellScript`, `AuraScript` y macros de registro, consulta [Scripts del Core](core-scripts) y la documentación del [sistema de hechizos](spell_system).

### Qué hacen los hooks más comunes

Usa la [Referencia de hooks C++](hooks-script-reference) cuando necesites las firmas exactas. Usa las notas de abajo cuando quieras entender rápidamente **cuándo** se ejecuta un hook y **para qué** suele utilizarse.

#### Inicio, apagado y flujo global

- `OnBeforeConfigLoad` / `OnAfterConfigLoad`: se ejecutan antes de que empiece la carga de configuración o después de que termine. Usa `OnBeforeConfigLoad` para comportamiento previo a la carga y `OnAfterConfigLoad` para reaccionar a valores que ya fueron cargados.
- `OnStartup` / `OnShutdown`: se ejecutan durante el arranque y el apagado del servidor. Úsalos para inicialización del módulo, limpieza final o informes.
- `OnWorldUpdate`: se ejecuta dentro del bucle de actualización del mundo. Úsalo solo para lógica periódica ligera.
- `OnBeforeWorldInitialized`: se ejecuta antes de que el mundo termine de inicializarse. Es útil cuando necesitas preparar estado temprano en el arranque.

#### Eventos del jugador y del gameplay

- `OnPlayerLogin`, `OnPlayerFirstLogin`, `OnPlayerLogout`: hooks del ciclo de vida de la sesión del jugador.
- `OnPlayerGiveXP`, `OnPlayerLevelChanged`, `OnPlayerCompleteQuest`: hooks de progresión para recompensas personalizadas, escalado o reglas de progreso.
- `OnPlayerBeforeTeleport`: se ejecuta antes de realizar un teletransporte y puede usarse para bloquear o modificar comportamiento relacionado con el teletransporte.
- `OnPlayerCanUseItem`, `OnPlayerCanEquipItem`, `OnPlayerCanSellItem`: hooks de validación para aplicar restricciones personalizadas.
- `OnPlayerBeforeSendChatMessage` / `OnPlayerCanUseChat`: hooks para filtrado y moderación del chat.

#### Criaturas, gameobjects y mapas

- `GetCreatureAI` / `GetGameObjectAI`: asocian una clase de IA personalizada a un script de criatura o gameobject.
- `OnGossipHello`, `OnGossipSelect`, `OnQuestAccept`, `OnQuestReward`: hooks comunes de interacción para NPCs, ítems y gameobjects.
- `OnCreateMap`, `OnPlayerEnterMap`, `OnMapUpdate`: hooks del ciclo de vida de mapas para sistemas que afectan a todo el mapa.
- `CreateInstanceScript`: crea el `InstanceScript` usado por un mapa de instancia.
- `OnAreaTrigger`: se ejecuta cuando un jugador activa un area trigger.

#### Combate, hechizos y fórmulas

- `OnHeal`, `OnDamage`, `OnUnitDeath`: hooks genéricos de combate de unidad usados por sistemas globales de combate.
- `OnSpellCheckCast`, `OnSpellCast`, `OnSpellPrepare`: hooks globales del flujo de hechizos expuestos por `SpellSC`.
- `OnHonorCalculation`, `OnGainCalculation`, `OnAfterArenaRatingCalculation`: hooks de fórmulas para cálculos numéricos del core.
- `OnLoadSpellCustomAttr`: permite a los módulos ajustar atributos personalizados de hechizos durante la inicialización de datos de hechizos.

#### Battlegrounds, arena y sistemas sociales

- `OnBattlegroundStart`, `OnQueueUpdate`, `OnBattlegroundEnd`: hooks del flujo de battlegrounds.
- `OnBeforeSendJoinMessageArenaQueue` / `OnBeforeSendExitMessageArenaQueue`: hooks de mensajes de cola de arena.
- `OnArenaStart`, `OnBeforeArenaCheckWinConditions`: hooks de `ArenaScript` para el flujo de partidas de arena y la validación de condiciones de victoria.
- `CanAddMember`: hook de prevalidación de `ArenaScript` para reglas de membresía de arena teams antes de aceptar a un miembro.
- `OnAddMember`: hook de `ArenaScript` que se ejecuta después de añadir un miembro a un arena team.
- `OnGetArenaPoints`, `OnGetSlotByType`: hooks de `ArenaTeamScript` para el cálculo de puntos y slots de arena teams.
- `OnGuildAddMember`, `OnGroupAddMember`, `OnGroupDisband`: hooks del ciclo de vida de guilds y grupos.

#### Economía, loot y sistemas de soporte

- `OnAuctionAdd`, `OnAuctionExpire`, `OnBeforeAuctionHouseMgrSendAuctionWonMail`: hooks de comportamiento de la casa de subastas.
- `OnLootMoney`: se ejecuta cuando se entrega dinero procedente del loot.
- `OnTicketCreate`, `OnTicketStatusUpdate`, `OnTicketResolve`: hooks del flujo de tickets de GM.
- `OnBeforeMailDraftSendMailTo`: hook de personalización del correo antes de enviar un mensaje.

#### Hooks de módulo y base de datos

- `OnModuleDatabasesLoading`: abre conexiones propias del módulo, inicializa el esquema y puede abortar el arranque si hace falta.
- `OnAfterDatabasesLoaded`: se ejecuta después de completar la carga de bases de datos y sirve para inicialización adicional.
- `OnModuleDatabasesKeepAlive`: mantiene activas las conexiones de base de datos del módulo durante la ejecución.
- `OnModuleDatabasesClosing`: cierra las conexiones propias del módulo durante el apagado.
- `OnDatabaseGetDBRevision`: expone la revisión de la base de datos del módulo en `.server info`.

### Hooks de base de datos

Los módulos que necesitan su propia base de datos deben usar `DatabaseScript`.

Los hooks más relevantes son:

- `OnModuleDatabasesLoading()` para abrir el pool, crear/poblar/actualizar el esquema y abortar el arranque devolviendo `false` si falla
- `OnModuleDatabasesKeepAlive()` para hacer ping a las conexiones del módulo durante el tick de keep-alive del mundo
- `OnModuleDatabasesClosing()` para cerrar el pool durante el apagado
- `OnDatabaseGetDBRevision()` para mostrar la revisión de la base de datos del módulo en `.server info`
- `OnDatabaseWarnAboutSyncQueries(bool apply)` si tu módulo quiere reflejar el estado de advertencia del core sobre consultas síncronas

### Glosario

- **Hook**: Una función que se declara dentro de un **_ScriptObject_** y que es definida por el **_Listeners_**
- **ScriptObject**: Clase abstracta que debe ser extendida para crear el **_Observer_**.
- **Script type**: La clase que extiende el `ScriptObject` y contiene hooks (por ejemplo, `PLayerScript`, `CreatureScript`, etc.), cuando extiendes la clase de tipo script estás inicializando un **_Concrete Observer_**
- **ScriptRegistry**: Esta clase contiene el registro de todos los `Observers` registrados.
- **ScriptMgr**: La clase singleton que contiene la lista de todos los hooks disponibles y actúa como un **_Observer_** notificando a los **_Listeners_** cuando se despacha un evento.

## Cómo crear un hook

¡No se preocupe, no es tan aterrador como puede pensar!.

![hook](https://media4.giphy.com/media/B4ZgcoPTHYXL2/giphy.gif?cid=ecf05e47mvpbtn5sbmgkcg2gurnrjk35hsdt3m7faillyp26&rid=giphy.gif&ct=g)

Antes de pasar al siguiente paso deberías preguntarte: ¿tengo que crear un nuevo tipo de script basado en la clase `ScriptObject` o puedo reutilizar uno de los ya existentes?

Un tipo de script suele estar estrictamente relacionado con una determinada clase del core. Por ejemplo:

- `PlayerScript` -> `Player` class
- `WorldScript` -> `World` class
- `CreatureScript` -> `Creature` class

Y así sucesivamente.

Hay algunas excepciones como el `GlobalScript` que es un Observador utilizado en diferentes clases a lo largo del núcleo. Pero en general, un tipo de script debe referirse a una clase específica.

Por lo tanto, si ha creado una nueva clase que tiene que ser extendida con hooks, entonces puede proceder con el primer punto.

Sin embargo, la mayoría de las veces sólo tienes que añadir nuevos hooks a los scripts existentes, en este caso sólo salta al punto 2 de este capítulo.

### 1) Procedimiento estándar al añadir nuevas clases de scripts

En primer lugar, define la clase actual, y haz que herede de `ScriptObject`, así:

```cpp
class MyScriptType : public ScriptObject
{
    uint32 _someId;
    private:
        void RegisterSelf();
    protected:
        MyScriptType(const char* name, uint32 someId)
            : ScriptObject(name), _someId(someId)
        {
            ScriptRegistry<MyScriptType>::AddScript(this);
        }
    public:
        // Si una función virtual en tu clase de tipo script
        // no tiene que ser necesariamente anulada, simplemente declárala virtual
        // con un cuerpo vacío. Si, por el contrario, es lógico anularla
        // (es decir, si es el único método de la clase), hazla virtual pura, añadiéndole = 0.
        virtual void OnBeforeSomeEvent(uint32 /*someArg1*/, std::string& /*someArg2/*) { }
        // Esta es una función virtual pura:
        virtual void OnAnotherEvent(uint32 /*someArg*/) = 0;
}
```

A continuación, tienes que añadir una especialización para ScriptRegistry. Pon esto al principio de `ScriptMgr.cpp`:

```cpp
template class ScriptRegistry<MyScriptType>;
```

Ahora añade el registro en la parte inferior del `ScriptMgr.cpp`:

```cpp
MyScriptType::MyScriptType(const char* name)
    : ScriptObject(name)
{
    ScriptRegistry<MyScriptType>::AddScript(this);
}
```

Entonces añade una rutina de limpieza en `ScriptMgr::unload()`.

```
SCR_CLEAR(MyScriptType);
```

¡Y finalmente tu clase está lista para funcionar con el sistema de scripts!

### 2) Implementar las funciones de los hooks

Si no has seguido el punto 1 y quieres reutilizar un `ScriptObject` existente, entonces tienes que declarar primero las funciones dentro de una de las clases de `ScriptObject` preexistentes (como `PlayerScript`, `ServerScript`, etc.)

#### Declarar los hooks

Lo que tienes que hacer ahora es añadir funciones a `ScriptMgr` que puedan ser llamadas desde el núcleo para desencadenar realmente ciertos eventos.

En `ScriptMgr.h`, dentro de `class ScriptMgr`

```cpp
void OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2);
void OnAnotherEvent(uint32 someArg);
```

**NOTA:** para ciertos scripts el método declarado dentro de la clase `ScriptMgr` y el declarado en el `ScriptObject` relacionado, no siempre coinciden. Por ejemplo: `OnLogin` es un hook del PlayerScript que se declara como `OnPlayerLogin` cuando se utiliza dentro de la clase `ScriptMgr`, evitando así colisiones con otros métodos ya que la clase `ScriptMgr` recoge los hooks de todos los `ScriptObjects` dentro de la misma lista.

#### Defina sus hooks

Este paso define la forma en que su hook debe llamar a los listeners registrados.

La forma más habitual de hacerlo es la siguiente

En `ScriptMgr.cpp`:

```cpp
void ScriptMgr::OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2)
{
    FOREACH_SCRIPT(MyScriptType)->OnBeforeSomeEvent(someArg1, someArg2);
}

void ScriptMgr::OnAnotherEvent(uint32 someArg)
{
    FOREACH_SCRIPT(MyScriptType)->OnAnotherEvent(someArg);
}
```

Ahora basta con llamar a estas dos funciones desde cualquier lugar del core para activar el evento en todos los scripts registrados de ese tipo.

### Cómo llamar a tus hooks

La clase `ScriptMgr` se inicializa dentro del AC como un singleton que contendrá todos los observers (ScriptObjects) y sus listeners registrados relacionados (hooks). AC proporciona una propiedad global llamada "sScriptMgr" que puede utilizar para llamar a su script dentro de las funciones de AC.

Por ejemplo:

```cpp
void CoreClass::SomeEvent() 
{
    uint32 arg1=10;
    std::string arg2="something";

    sScriptMgr->OnBeforeSomeEvent(arg1, arg2);

    //[...]
}
```

## Documentar su hook

Recuerda documentar tu nuevo hook siguiendo la guía [Cómo documentar tu código](how-to-document-code).

Cuando creas un nuevo hook para publicarlo en el repo de `AzerothCore`, uno de los criterios de aceptación es escribir una documentación adecuada para él, para que otras personas sepan cómo usarlo correctamente. Así que, por favor, lee esa guía con atención.

## Convenciones de nomenclatura

Cada `hook` debe tener la siguiente convención de nombres:

`On[When]<Action>`

Por ejemplo:

- `OnBeforeConfigLoad`
- `OnAfterArenaRatingCalculation`

La acción normalmente coincide con el nombre de la función dentro de la cual se llama al `hook`.

Si la función madre es lo suficientemente compleja como para contener diferentes hooks, entonces la acción debe reflejar para qué se utiliza el `hook`.

La parte "Cuando" es opcional, pero se recomienda encarecidamente.

Ayuda a entender en qué parte de la función padre se llama al `hook`.

Por ejemplo, puedes tener tanto `OnBeforeConfigLoad` como `OnAfterConfigLoad`, para cambiar el comportamiento antes y después de cargar la configuración.

## Hooks avanzados

### Cómo cambiar el comportamiento de una función (filtrado)

Con los hooks no sólo puedes ejecutar acciones específicas en un momento determinado, incluso puedes cambiar el comportamiento de la función donde se llama al `hook` para hacerlo, tienes 2 soluciones:

#### 1) Utilización de los parámetros de referencia

Este es el más común. Básicamente utilizando el concepto de pasar un parámetro por referencia se puede cambiar todo lo que se pasa al propio `hook`.

Por ejemplo:

```cpp
OnMotdChange(std::string& newMotd)
```

Pasando el `newMotd` con el carácter '&' se permite a los listeners cambiar el valor del `Motd` cuando se llama a esa acción.

#### 2) Utilizar un valor de retorno `bool`

Este enfoque no es muy común, la mayoría de los hooks devuelven un tipo **"void"**, y trabajar con referencias es más fácil la mayoría de las veces, pero si realmente lo necesitas puedes implementar un hook declarado de esta manera:

```cpp
bool ScriptMgr::OnBeforePlayerTeleport(Player* player, uint32 mapid, float x, float y, float z, float orientation, uint32 options, Unit* target)
{
    bool ret = true;

    FOR_SCRIPTS_RET(PlayerScript, itr, end, ret) // Devuelve true por defecto si no son scripts
    if (!itr->second->OnBeforeTeleport(player, mapid, x, y, z, orientation, options, target))
        ret = false; // Cambiamos el valor de ret sólo cuando los scripts devuelven false

    return ret;
}
```

Este hook notifica a todos los listeners pero también captura cuando al menos uno de los listeners registrados devuelve **"false"**, en ese caso el valor de retorno final también será false.

En este caso particular, este hook se utiliza dentro de una condición if para no permitir que un jugador sea teletransportado si uno de los listeners devuelve **false** por alguna razón.

Puedes implementar tu lógica diferente (por ejemplo, falso por defecto, verdadero si lo hay) sólo recuerda documentarlo adecuadamente.

### Cree su sistema de hooks dentro de su módulo

Usando la guía anterior puedes incluso crear tu `ScriptObject` dentro de tu módulo para permitir que la gente lo extienda.

Algunos módulos, como el de balance automático, permiten personalizar cierta parte de su función mediante el uso de hooks internos.

Puede ver este archivo como ejemplo: https://github.com/azerothcore/mod-autobalance/blob/master/src/AutoBalance.h

**NOTA:** También necesitas crear tu propia implementación de `ScriptMgr` y ofrecer un singleton que permita llamar a tus hooks.

### Consideraciones finales

Existen otras características del sistema `ScriptAI` que no han sido incluidas en esta documentación, como la creación de scripts vinculados a entidades específicas dentro de nuestra base de datos (Ej. `CreatureScript`). Este uso avanzado puede ser implementado replicando el código relacionado que tenemos dentro de los archivos `ScriptMgr`. Si necesitas ayuda o quieres mejorar esta documentación, no dudes en pedir apoyo y editar esta página.

## Recursos externos

- [Stack overflow topic: Is it possible to turn a core patch into a module for AzerothCore?](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683)
