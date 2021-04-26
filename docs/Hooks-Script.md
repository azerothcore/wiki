# The ScriptAI system

The ScriptAI system implemented by AC uses a special [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) strategy to implement an event-driven programming which is also the **CORE** of our modular system. 

## Hook list

The list of the hooks can be found here: [ScriptMgr.h](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h)

Remember to document your new hook by following the [How to document your code](how-to-document-code.md) guide.


## How to create an hook

Standard procedure when adding new script type classes:
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
            virtual void OnSomeEvent(uint32 someArg1, std::string& someArg2) { }
            // This is a pure virtual function:
            virtual void OnAnotherEvent(uint32 someArg) = 0;
    }
```

Next, you need to add a specialization for ScriptRegistry. Put this in the bottom of
ScriptMgr.cpp:
```C++
template class ScriptRegistry<MyScriptType>;
```
    
Now, add a cleanup routine in `ScriptMgr::unload()`

```
SCR_CLEAR(MyScriptType);
```
    
Now your script type is good to go with the script system. What you need to do now
is add functions to ScriptMgr that can be called from the core to actually trigger
certain events. For example, in ScriptMgr.h:

```C++
void OnSomeEvent(uint32 someArg1, std::string& someArg2);
void OnAnotherEvent(uint32 someArg);
```

In ScriptMgr.cpp:

```C++
void ScriptMgr::OnSomeEvent(uint32 someArg1, std::string& someArg2)
{
    FOREACH_SCRIPT(MyScriptType)->OnSomeEvent(someArg1, someArg2);
}
void ScriptMgr::OnAnotherEvent(uint32 someArg)
{
    FOREACH_SCRIPT(MyScriptType)->OnAnotherEvent(someArg);
}
```

Now you simply call these two functions from anywhere in the core to trigger the
event on all registered scripts of that type.

## Naming conventions

Every hook must have the following naming convention:

`On[When]<Action>`

For example:

* `OnBeforeConfigLoad`
* `OnAfterArenaRatingCalculation`

the `[When]` part is optional, but strongly suggested

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

This approach is not very common, most of the hooks return a "void" type and working with references is easier most of the time, but if you really need it you can implement an hook which is declared in this way:

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


