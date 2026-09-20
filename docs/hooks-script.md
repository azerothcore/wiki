---
tableofcontents: 1
---

# The ScriptAI system

The ScriptAI system implemented by AC uses a special [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) strategy to implement an event-driven programming which is also the **CORE** of our modular system.

This guide, together with our [module system](create-a-module) lets you extend the AzerothCore without patching it directly. This allows you to update your repository by keeping your additions and customizations conflict-free!

## Resources

### Hook List

The full hook catalog is documented in [Hooks C++ Reference](hooks-script-reference) and mirrors the declarations in the [ScriptMgr.h file](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h).

### Hook reference

AzerothCore groups its C++ hooks by **script type** inside `ScriptMgr.h`.

Pick the script type that matches the subsystem you want to extend, then inspect that class in `ScriptMgr.h` for the complete signatures and the full list of available callbacks.

#### Lifecycle and server hooks

| Script type | Use it for | Example hooks |
| --- | --- | --- |
| `ServerScript` | Network startup, sockets and packet filtering | `OnNetworkStart`, `CanPacketReceive`, `CanPacketSend` |
| `WorldScript` | Server lifecycle, config loading and world updates | `OnBeforeConfigLoad`, `OnStartup`, `OnShutdown` |
| `FormulaScript` | Gameplay formulas and rating calculations | `OnHonorCalculation`, `OnGainCalculation`, `OnAfterArenaRatingCalculation` |
| `CommandScript` | Registering chat commands | `GetChatCommands` |

#### Entity and map hooks

| Script type | Use it for | Example hooks |
| --- | --- | --- |
| `MapScript` | Map creation, unloading and per-map updates | `OnCreateMap`, `OnPlayerEnterMap`, `OnMapUpdate` |
| `InstanceMapScript` | Providing the `InstanceScript` implementation for an instance map | `CreateInstanceScript` |
| `PlayerScript` | Player login, progression, inventory, chat, battlegrounds and many other player events | `OnPlayerLogin`, `OnPlayerGiveXP`, `OnPlayerBeforeTeleport` |
| `UnitScript` | Generic combat and aura events for any unit | `OnHeal`, `OnDamage`, `OnUnitDeath` |
| `CreatureScript` | NPC gossip, quests and custom `CreatureAI` binding | `OnGossipHello`, `OnQuestReward`, `GetCreatureAI` |
| `GameObjectScript` | GameObject gossip, state changes and custom `GameObjectAI` binding | `OnGossipHello`, `OnGameObjectStateChanged`, `GetGameObjectAI` |
| `ItemScript` | Item use, item quests and item gossip | `OnItemUse`, `OnQuestAccept`, `OnGossipSelect` |
| `AreaTriggerScript` | Area trigger activation | `OnAreaTrigger` |
| `BattlegroundScript` | Creating custom battleground implementations | `CreateBattleground` |
| `OutdoorPvPScript` | Creating custom outdoor PvP implementations | `CreateOutdoorPvP` |
| `VehicleScript` | Vehicle seat and passenger lifecycle | `OnInstall`, `OnAddPassenger`, `OnRemovePassenger` |
| `DynamicObjectScript` | Dynamic object updates | `OnDynamicObjectUpdate` |
| `TransportScript` | Transport movement and passengers | `OnTransportUpdate`, `OnAddPassenger`, `OnRelocate` |
| `WeatherScript` | Weather changes and ticks | `OnWeatherChange`, `OnWeatherUpdate` |

#### Systems and game-rule hooks

| Script type | Use it for | Example hooks |
| --- | --- | --- |
| `AccountScript` | Account login and account management events | `OnAccountLogin`, `OnPasswordChange`, `CanAccountCreateCharacter` |
| `GuildScript` | Guild events and guild bank behavior | `OnGuildAddMember`, `OnGuildDisband`, `CanGuildSendBankList` |
| `GroupScript` | Group invites, removals and battleground queue checks | `OnGroupAddMember`, `OnGroupDisband`, `CanGroupJoinBattlegroundQueue` |
| `GlobalScript` | Cross-cutting hooks used by multiple systems | `OnArenaWeekReset`, `OnLoadSpellCustomAttr`, `OnBeforeSetBossState` |
| `MovementHandlerScript` | Player movement packets | `OnPlayerMove` |
| `AllCreatureScript` | Hooks that run for every creature | `OnBeforeCreatureSelectLevel`, `OnCreatureSaveToDB` |
| `AllGameObjectScript` | Hooks that run for every gameobject | `OnGameObjectSaveToDB` |
| `AllMapScript` | Cross-instance hooks for instance script creation and instance destruction | `OnBeforeCreateInstanceScript`, `OnDestroyInstance` |
| `BattlefieldScript` | Outdoor battlefield events | `OnBattlefieldPlayerEnterZone`, `OnBattlefieldWarEnd` |
| `BGScript` | Battleground and queue flow | `OnBattlegroundStart`, `OnQueueUpdate`, `OnBeforeSendJoinMessageArenaQueue` |
| `ArenaScript` | Arena match rules and member update behavior | `OnArenaStart`, `OnBeforeArenaCheckWinConditions`, `OnAddMember` |
| `ArenaTeamScript` | Arena team slot and point calculations | `OnGetSlotByType`, `OnGetArenaPoints`, `OnSetArenaMaxPlayersPerTeam` |
| `AuctionHouseScript` | Auction events and auction mail behavior | `OnAuctionAdd`, `OnAuctionExpire`, `OnBeforeAuctionHouseMgrSendAuctionWonMail` |
| `ConditionScript` | Custom condition checks | `OnConditionCheck` |
| `GameEventScript` | Seasonal or scheduled game events | `OnGameEventStart`, `OnGameEventStop` |
| `WorldObjectScript` | Generic world object lifecycle and map updates | `OnWorldObjectCreate`, `OnWorldObjectDestroy`, `OnWorldObjectUpdate` |
| `LootScript` | Loot-related events | `OnLootMoney` |
| `TicketScript` | GM ticket lifecycle events | `OnTicketCreate`, `OnTicketStatusUpdate`, `OnTicketResolve` |
| `MiscScript` | Cross-cutting object, item and utility hooks | `OnConstructObject`, `OnItemCreate`, `CanApplySoulboundFlag` |
| `CommandSC` | Internal command execution handlers | `OnHandleDevCommand`, `OnTryExecuteCommand`, `OnBeforeIsInvokerVisible` |
| `DatabaseScript` | Module-owned database lifecycle and revision hooks | `OnModuleDatabasesLoading`, `OnAfterDatabasesLoaded`, `OnDatabaseGetDBRevision` |
| `MailScript` | Mail delivery customization | `OnBeforeMailDraftSendMailTo` |
| `AchievementScript` | Achievement and criteria flow | `SetRealmCompleted`, `CanCheckCriteria` |
| `AchievementCriteriaScript` | Criteria checks bound to a scripted ID | `OnCriteriaCheck` |
| `PetScript` | Pet stats, talents and unlearn checks | `OnInitStatsForLevel`, `CanResetTalents` |
| `SpellSC` | Global spell-system hooks exposed through `ScriptMgr` | `OnSpellCheckCast`, `OnSpellCast`, `OnCalcMaxDuration` |

For spell-specific handlers implemented with `SpellScript`, `AuraScript` and registration macros, see [Core Scripts](core-scripts) and the [Spell system](spell_system) documentation.

### What the most common hooks do

Use the full [Hooks C++ Reference](hooks-script-reference) when you need exact signatures. Use the notes below when you want to quickly understand **when** a hook runs and **why** you would use it.

#### Startup, shutdown and global flow

- `OnBeforeConfigLoad` / `OnAfterConfigLoad`: run before configuration loading starts or after it finishes. Use `OnBeforeConfigLoad` for pre-load behavior and `OnAfterConfigLoad` to react to values that are already loaded.
- `OnStartup` / `OnShutdown`: run during server startup and shutdown. Use them for module initialization, final cleanup or reporting.
- `OnWorldUpdate`: runs on the world update loop. Use it only for lightweight periodic logic.
- `OnBeforeWorldInitialized`: runs before the world finishes initializing. Useful when you need to prepare state early in the boot sequence.

#### Player and gameplay events

- `OnPlayerLogin`, `OnPlayerFirstLogin`, `OnPlayerLogout`: player session lifecycle hooks.
- `OnPlayerGiveXP`, `OnPlayerLevelChanged`, `OnPlayerCompleteQuest`: progression hooks for custom rewards, scaling or progression rules.
- `OnPlayerBeforeTeleport`: runs before a teleport is executed and can be used to block or alter teleport-related behavior.
- `OnPlayerCanUseItem`, `OnPlayerCanEquipItem`, `OnPlayerCanSellItem`: validation hooks that let you enforce custom restrictions.
- `OnPlayerBeforeSendChatMessage` / `OnPlayerCanUseChat`: chat filtering and moderation hooks.

#### Creatures, gameobjects and maps

- `GetCreatureAI` / `GetGameObjectAI`: bind a custom AI class to a creature or gameobject script.
- `OnGossipHello`, `OnGossipSelect`, `OnQuestAccept`, `OnQuestReward`: common interaction hooks for NPCs, items and gameobjects.
- `OnCreateMap`, `OnPlayerEnterMap`, `OnMapUpdate`: map lifecycle hooks for map-wide systems.
- `CreateInstanceScript`: creates the `InstanceScript` used by an instance map.
- `OnAreaTrigger`: runs when a player activates an area trigger.

#### Combat, spells and formulas

- `OnHeal`, `OnDamage`, `OnUnitDeath`: generic unit combat hooks used by combat-wide systems.
- `OnSpellCheckCast`, `OnSpellCast`, `OnSpellPrepare`: global spell pipeline hooks exposed through `SpellSC`.
- `OnHonorCalculation`, `OnGainCalculation`, `OnAfterArenaRatingCalculation`: formula hooks for core numeric calculations.
- `OnLoadSpellCustomAttr`: lets modules adjust spell custom attributes during spell data initialization.

#### Battlegrounds, arena and social systems

- `OnBattlegroundStart`, `OnQueueUpdate`, `OnBattlegroundEnd`: battleground flow hooks.
- `OnBeforeSendJoinMessageArenaQueue` / `OnBeforeSendExitMessageArenaQueue`: arena queue messaging hooks.
- `OnArenaStart`, `OnBeforeArenaCheckWinConditions`: `ArenaScript` hooks for arena match flow and win-condition handling.
- `CanAddMember`, `OnAddMember`, `OnBeforeArenaTeamMemberUpdate`: `ArenaScript` hooks specifically for `ArenaTeam` membership validation, post-add handling and member-update flow.
- `OnGetArenaPoints`, `OnGetSlotByType`, `OnGetPoints`: `ArenaTeamScript` hooks for slot resolution and arena-point values exposed by the arena team system.
- `OnGuildAddMember`, `OnGroupAddMember`, `OnGroupDisband`: guild and group lifecycle hooks.

#### Economy, loot and support systems

- `OnAuctionAdd`, `OnAuctionExpire`, `OnBeforeAuctionHouseMgrSendAuctionWonMail`: auction house behavior hooks.
- `OnLootMoney`: runs when money is awarded from loot.
- `OnTicketCreate`, `OnTicketStatusUpdate`, `OnTicketResolve`: GM ticket workflow hooks.
- `OnBeforeMailDraftSendMailTo`: mail customization hook before a message is sent.

#### Module and database hooks

- `OnModuleDatabasesLoading`: open module-owned connections, initialize schema and fail startup if needed.
- `OnAfterDatabasesLoaded`: runs after database loading completes, useful for follow-up initialization.
- `OnModuleDatabasesKeepAlive`: keep module database connections alive during runtime.
- `OnModuleDatabasesClosing`: close module-owned connections during shutdown.
- `OnDatabaseGetDBRevision`: expose your module database revision to `.server info`.

### Database hooks

Modules that need their own database should use `DatabaseScript`.

The most relevant hooks are:

- `OnModuleDatabasesLoading()` to open the pool, create/populate/update the schema and abort startup by returning `false` on failure
- `OnModuleDatabasesKeepAlive()` to ping the module-owned connections during the world keep-alive tick
- `OnModuleDatabasesClosing()` to close the pool during shutdown
- `OnDatabaseGetDBRevision()` to expose your module database revision in `.server info`
- `OnDatabaseWarnAboutSyncQueries(bool apply)` if your module wants to mirror the core synchronous-query warning state

### Glossary

* **Hook**: A function that is declared inside a **_ScriptObject_** and that is defined by the **_Listeners_**
* **ScriptObject**: Abstract class that should be extended to create the **_Observer_**.
* **Script type**: The class that extends the `ScriptObject` and contains hooks (e.g. `PLayerScript`, `CreatureScript`, etc.), 
  when you extend the script type class you are initializing a **_Concrete Observer_**
* **ScriptRegistry**: This class contains the registry of all the registered Observers.
* **ScriptMgr**: The singleton class that contains the list of all the available hooks and acts as a **_Observable_** by notifying the **_Listeners_** when an event is dispatched.

## How to create a hook

Don't worry! is not scary as you may think!

![](https://media4.giphy.com/media/B4ZgcoPTHYXL2/giphy.gif?cid=ecf05e47mvpbtn5sbmgkcg2gurnrjk35hsdt3m7faillyp26&rid=giphy.gif&ct=g)

Before going through the next step you should ask yourself: do I have to create a new script type based on `ScriptObject` class or can I reuse one of those already existing?

A script type is normally strictly related to a certain class of the core. For example:

- `PlayerScript` -> `Player` class
- `WorldScript` -> `World` class
- `CreatureScript` -> `Creature` class

And so on.

There are some exceptions such as the `GlobalScript` which is an Observer used in different classes throughout the core. But generally speaking, a script type should refer to a specific class.

Therefore, if you have created a new class that has to be extended with hooks, then you can proceed with the first point.

However, most of the time you just have to add new hooks to existing scripts, in this case just jump to point 2 of this chapter.

### 1) Standard procedure when adding new script type classes

First of all, define the actual class, and have it inherit from ScriptObject, like so:

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
        // If a virtual function in your script type class is not necessarily
        // required to be overridden, just declare it virtual with an empty
        // body. If, on the other hand, it's logical only to override it (i.e.
        // if it's the only method in the class), make it pure virtual, by adding
        // = 0 to it.
        virtual void OnBeforeSomeEvent(uint32 /*someArg1*/, std::string& /*someArg2/*) { }
        // This is a pure virtual function:
        virtual void OnAnotherEvent(uint32 /*someArg*/) = 0;
}
```

Next, you need to add a specialization for ScriptRegistry. Put this at the beginning of ScriptMgr.cpp:

```cpp
template class ScriptRegistry<MyScriptType>;
```

Now add the register at the bottom of the ScriptMgr.cpp:

```cpp
MyScriptType::MyScriptType(const char* name)
    : ScriptObject(name)
{
    ScriptRegistry<MyScriptType>::AddScript(this);
}
```

Then add a cleanup routine in `ScriptMgr::unload()`

```
SCR_CLEAR(MyScriptType);
```

And finally your class is good to go with the script system!

### 2) Implement the hooks functions

If you didn't follow point 1 and you want to reuse an existing ScriptObject, then you have to declare the functions within one of the pre-existing ScriptObject classes first (such as PlayerScript, ServerScript etc.)

#### Declare your hooks

What you need to do now is add functions to ScriptMgr that can be called from the core to actually trigger certain events.

In ScriptMgr.h, inside the `class ScriptMgr`

```cpp
void OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2);
void OnAnotherEvent(uint32 someArg);
```

{% include note.html content="for certain scripts the method declared inside the ScriptMgr class and the one declared into the related ScriptObject, don't always match. For instance: <b>OnLogin</b> is a hook from the PlayerScript that is declared as <b>OnPlayerLogin</b> when used inside the ScriptMgr class, thus avoid collisions with other methods since the ScriptMgr class collects hooks from allnthe ScriptObjects within the same list." %}

#### Define your hooks

This step defines the way your hook should call the registered listeners.
The most common way to do it is the following

In ScriptMgr.cpp:

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

Now you simply call these two functions from anywhere in the core to trigger the
event on all registered scripts of that type.

### How to call your hooks

The ScriptMgr class is initialized within the AC as a singleton that will contain all the observers (ScriptObjects) and their related registered listeners (hooks).

AC provides a global property called "sScriptMgr" that you can use to call your script within the AC functions.

For instance:

```cpp
void CoreClass::SomeEvent() 
{
    uint32 arg1=10;
    std::string arg2="something";

    sScriptMgr->OnBeforeSomeEvent(arg1, arg2);

    //[...]
}
```

## Documenting your hook

Remember to document your new hook by following the [How to document your code](how-to-document-code) guide.

When you create a new hook to publish into the AC repo, one of the acceptance criteria is to write proper documentation for it, hence other people know how to use it properly. So please, read that guide carefully.

## Naming conventions

Every hook must have the following naming convention:

`On[When]<Action>`

For example:

* `OnBeforeConfigLoad`
* `OnAfterArenaRatingCalculation`

The action normally matches the name of the function within which the hook is called.

If the parent function is complex enough to even host different hooks, then the action should reflect what the hook is used for.

The `[When]` part is optional, but strongly suggested.

It helps to understand in which part of the parent function the hook is called.

For instance, you can have both `OnBeforeConfigLoad` and `OnAfterConfigLoad`, to change the behaviour before and after the config is loaded.

## Advanced hooks

### How to change the behaviour of a function (filtering)

With hooks you can't only run specific actions at a specific time, you can even change the behaviour of the function where the hook is called to do so, you have 2 solutions:

#### 1) Using reference parameters

This is the most common one. Basically using the concept of passing a parameter by reference you can change everything that is passed to the hook itself.
For instance:

```cpp
OnMotdChange(std::string& newMotd)
```

Passing the newMotd with the '&' character you allow the listeners to change the value of the Motd when that action is called.

#### 2) Using a bool return value

This approach is not very common, most of the hooks return a "void" type, and working with references is easier most of the time, but if you really need it you can implement a hook that is declared in this way:

```cpp
bool ScriptMgr::OnBeforePlayerTeleport(Player* player, uint32 mapid, float x, float y, float z, float orientation, uint32 options, Unit* target)
{
    bool ret = true;

    FOR_SCRIPTS_RET(PlayerScript, itr, end, ret) // return true by default if not scripts
    if (!itr->second->OnBeforeTeleport(player, mapid, x, y, z, orientation, options, target))
        ret = false; // we change ret value only when scripts return false

    return ret;
}
```

This hook notifies all the listeners but also catches when at least one of the registered listener returns "false", in that case the final return value will be false as well.

In this particular case, this hook is used within an if-condition to disallow a player to be teleported if one of the listeners returns **false** for some reason.

You can implement your different logic (e.g. false by default, true if any) just remember to document it properly!

### Create your hook system within your module

By using the guide above you can even create your ScriptObject within your module to allow people to extend it.

Some modules, such as the auto-balance, allows customizing certain part of their function by using internal hooks

You can take a look at this file as an example: https://github.com/azerothcore/mod-autobalance/blob/master/src/AutoBalance.h

{% include note.html content="You also need to create your own ScriptMgr implementation and offer a singleton to allow calling your hooks." %}

### Final considerations

There are different other features of the ScriptAI system that have not been included in this documentation, such as the creation of scripts bound to specific entities inside our database (E.g. CreatureScript). This advanced usage can be implemented by replicate the related code we have inside the ScriptMgr files.

If you need any help or you want to improve this documentation, feel free to ask for support and edit this page.

## External resources

- [Stack overflow topic: Is it possible to turn a core patch into a module for AzerothCore?](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683)
