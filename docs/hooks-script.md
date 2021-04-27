# The ScriptAI system

The ScriptAI system implemented by AC uses a special [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) strategy to implement an event-driven programming which is also the **CORE** of our modular system.

This guide, together with the our [module system](Create-a-Module.md) lets you to extend the AzerothCore without patching the core directly. This allows you to update your core by keeping your additions and customizations conflict-free!

# Resources

## Hook List

The list of the hooks can be found here: [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h)

## Glossary

* **Hook**: A function that is declared inside a **_ScriptObject_** and that calls the **_Listeners_**
* **ScriptObject**: Abstract class that should be extended to create the **_Observer_**.
* **Script type**: The class that extends the ScriptObject (E.g. PLayerScript, CreatureScript etc.), 
  when you extend the script type class you are initializing a **_Concrete Observer_**
* **ScriptRegistry**: This class contains the registry of all the registered Observers.
* **ScriptMgr**: The singleton class that contains the list of all the available hooks and acts as a **_Observable_** by notifying the **_Listeners_** when an event is dispatched.

## How to create a hook

Before going through the next step you should ask yourself: do I have to create a new script type based on ScriptObject class or can I reuse one of those already existing?

A script type is normally strictly related to certain classes of the core. For example: 
* PlayerScript -> Player class
* WorldScript -> World class
* CreatureScript -> Creature class
etc.

There are some exception such as the GlobalScript which is an Observer used in different classes throughout the core. But generally speaking a script type should refer to a specific class.

Therefore, if you create a new class inside that has to be extended with hooks, then you can proceed with the first point.

However, most of the time you just have to add new hooks to existing scripts, in this case just jump to point 2 of this chapter.

### 1) Standard procedure when adding new script type classes

First of all, define the actual class, and have it inherit from ScriptObject, like so:
    
 ```C++
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
```C++
template class ScriptRegistry<MyScriptType>;
```

Now add the register at the bottom of the ScriptMgr.cpp:

```C++
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

If you didn't follow point 1 and you want to reuse an existing ScriptObject, then you have to declare the functions 
within one of the pre-existing ScriptObject classes first (such as PlayerScript, ServerScript etc.)
    
#### Declare you hooks
What you need to do now is add functions to ScriptMgr that can be called from the core to actually trigger
certain events.

In ScriptMgr.h , inside the `class ScriptMgr`

```C++
void OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2);
void OnAnotherEvent(uint32 someArg);
```

NOTE: for certain scripts the method declared inside the ScriptMgr class and the one declared into the related ScriptObject,
they don't always match. For instance: `OnLogin` is a hook from the PlayerScript that is declared as `OnPlayerLogin` when 
used inside the ScriptMgr class, thus avoid collisions with other method since the ScriptMgr class collects hooks from all
the ScriptObjects within the same list.

#### Define your hooks

This step define the way your hook should call the registered listeners.
The most common way to do it is the following

In ScriptMgr.cpp:

```C++
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

```C++
void CoreClass::SomeEvent() 
{
    uint32 arg1=10;
    std::string arg2="something";

    sScriptMgr->OnBeforeSomeEvent(arg1, arg2);
    
    //[...]
}
```

## Documenting your hook

Remember to document your new hook by following the [How to document your code](how-to-document-code.md) guide.

When you create a new hook to publish into the AC repo, one of the acceptance criteria is to write a proper documentation for it,
hence other people know how to use it properly. So please, read that guide carefully. 

## Naming conventions

Every hook must have the following naming convention:

`On[When]<Action>`

For example:

* `OnBeforeConfigLoad`
* `OnAfterArenaRatingCalculation`

The action normally match the name of the function within which the hook is called.
If the parent function is complex enough to even host different hooks, then the action
should reflect what the hook is used for.

The `[When]` part is optional, but strongly suggested.
It helps to understand in which part of the parent function the hook is called.
For instance, you can have both `OnBeforeConfigLoad` and `OnAfterConfigLoad`,
to change the behaviour before and after the config are loaded.

## Advanced hooks

### How to change the behaviour of a function (filtering)

With hooks you can't only run specific actions at a specific time, you can even change the behaviour of the script where the hook is called
To do so, you have 2 solutions:

#### 1) Using reference parameters

This is the most common one. Basically using the concept of passing a parameter by reference you can change everything is passed to the hook itself.
For instance:

```C++
OnMotdChange(std::string& newMotd)
``` 

Passing the newMotd with the '&' character you allow the listeners to change the value of the Motd when that action is called.

#### 2) Using a bool return value

This approach is not very common, most of the hooks return a "void" type and working with references is easier most of the time, but if you really need it you can implement a hook which is declared in this way:

```C++
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
In this particular case this hook is used within an if-condition to disallow a player to be teleported if one of the listener returns **false** for some reason.

You can implement your different logic (e.g. false by default, true if any) just remember to document it properly!

### Create your hook system within your module

By using the guide above you can even create your ScriptObject within your module to allow people extending it. 
Some modules, such as the autobalance, allows to customize certain part of their function by using internal hooks

You can take a look at this file as example: https://github.com/azerothcore/mod-autobalance/blob/master/src/AutoBalance.h

NOTE: You also need to create your own ScriptMgr implementation and offer a singleton to allow calling your hooks.


### Final considerations

There are different other features of the ScriptAI system that have not been included in this documentation, such as the creation of scripts binded 
to specific entities inside our database (E.g. CreatureScript). This advanced usage can be implemented by replicate the related code we have inside the ScriptMgr files.
If you need any help or you want to improve this documentation, feel free to ask support and edit this page.

