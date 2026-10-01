---
tableofcontents: 1
---

# ScriptAI 系统

AC 实现的 ScriptAI 系统使用了一种特殊的 [观察者模式](https://en.wikipedia.org/wiki/Observer_pattern) 策略来实现事件驱动编程，这也是我们模块化系统的**核心**。

本指南连同我们的 [模块系统](create-a-module) 一起，让你无需直接修补 AzerothCore 即可扩展它。这样你可以在更新仓库的同时，保持你的新增内容和自定义修改零冲突！

## 资源

### 钩子列表

钩子列表可以在 [ScriptMgr.h 文件](https://github.com/azerothcore/azerothcore-wotlk/blob/master/src/server/game/Scripting/ScriptMgr.h) 中找到。

### 术语表

* **钩子（Hook）**：在 **_ScriptObject_** 中声明、并由 **_Listeners（监听器）_** 定义的函数。
* **ScriptObject**：抽象类，应被继承以创建 **_Observer（观察者）_**。
* **脚本类型（Script type）**：继承 `ScriptObject` 并包含钩子的类（例如 `PLayerScript`、`CreatureScript` 等），
  当你继承脚本类型类时，你就是在初始化一个 **_Concrete Observer（具体观察者）_**。
* **ScriptRegistry**：包含所有已注册观察者注册表的类。
* **ScriptMgr**：单例类，包含所有可用钩子的列表，并充当 **_Observable（可观察对象）_**，在事件派发时通知 **_Listeners（监听器）_**。

## 如何创建钩子

别担心！这并没有你想象的那么可怕！

![](https://media4.giphy.com/media/B4ZgcoPTHYXL2/giphy.gif?cid=ecf05e47mvpbtn5sbmgkcg2gurnrjk35hsdt3m7faillyp26&rid=giphy.gif&ct=g)

在进入下一步之前，你应该问自己：我是需要创建一个基于 `ScriptObject` 类的新脚本类型，还是可以复用现有的某个脚本类型？

脚本类型通常与核心的某个特定类紧密相关。例如：

- `PlayerScript` -> `Player` 类
- `WorldScript` -> `World` 类
- `CreatureScript` -> `Creature` 类

以此类推。

也有一些例外，比如 `GlobalScript`，它是一个在整个核心中用于不同类的观察者。但一般来说，一个脚本类型应该对应一个特定的类。

因此，如果你创建了一个需要用钩子扩展的新类，那么你可以继续第一点。

然而，大多数情况下你只需为现有脚本添加新的钩子，这种情况下直接跳到本章的第 2 点即可。

### 1) 添加新的脚本类型类的标准流程

首先，定义实际的类，并让它继承自 ScriptObject，如下所示：

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
        // 如果你的脚本类型类中的虚函数不一定要被重写，
        // 只需将其声明为 virtual 并提供一个空实现。
        // 反之，如果逻辑上只应重写它（即它是类中唯一的方法），
        // 就通过添加 = 0 将其声明为纯虚函数。
        virtual void OnBeforeSomeEvent(uint32 /*someArg1*/, std::string& /*someArg2/*) { }
        // 这是一个纯虚函数：
        virtual void OnAnotherEvent(uint32 /*someArg*/) = 0;
}
```

接下来，你需要为 ScriptRegistry 添加一个特化。把它放在 ScriptMgr.cpp 的开头：

```cpp
template class ScriptRegistry<MyScriptType>;
```

现在在 ScriptMgr.cpp 的底部添加注册：

```cpp
MyScriptType::MyScriptType(const char* name)
    : ScriptObject(name)
{
    ScriptRegistry<MyScriptType>::AddScript(this);
}
```

然后在 `ScriptMgr::unload()` 中添加清理例程：

```
SCR_CLEAR(MyScriptType);
```

最后，你的类就可以与脚本系统一起使用了！

### 2) 实现钩子函数

如果你没有按照第 1 点操作，而是想复用一个现有的 ScriptObject，那么你必须先在预先存在的某个 ScriptObject 类（如 PlayerScript、ServerScript 等）中声明这些函数。

#### 声明你的钩子

你现在需要做的是向 ScriptMgr 添加函数，这些函数可以从核心调用以真正触发某些事件。

在 ScriptMgr.h 的 `class ScriptMgr` 中：

```cpp
void OnBeforeSomeEvent(uint32 someArg1, std::string& someArg2);
void OnAnotherEvent(uint32 someArg);
```

{% include note.html content="对于某些脚本，在 ScriptMgr 类中声明的方法与在相关 ScriptObject 中声明的方法并不总是匹配。例如：<b>OnLogin</b> 是 PlayerScript 的一个钩子，但在 ScriptMgr 类中使用时声明为 <b>OnPlayerLogin</b>，这是为了避免与其他方法冲突，因为 ScriptMgr 类会收集同一列表中所有 ScriptObject 的钩子。" %}

#### 定义你的钩子

这一步定义了你的钩子应该如何调用已注册的监听器。
最常见的做法如下：

在 ScriptMgr.cpp 中：

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

现在你可以简单地从核心的任何地方调用这两个函数，来触发该类型所有已注册脚本上的事件。

### 如何调用你的钩子

ScriptMgr 类在 AC 中被初始化为一个单例，它将包含所有观察者（ScriptObjects）及其相关的已注册监听器（钩子）。

AC 提供了一个名为 "sScriptMgr" 的全局属性，你可以用它来在 AC 函数中调用你的脚本。

例如：

```cpp
void CoreClass::SomeEvent() 
{
    uint32 arg1=10;
    std::string arg2="something";

    sScriptMgr->OnBeforeSomeEvent(arg1, arg2);

    //[...]
}
```

## 记录你的钩子

记得按照 [如何记录你的代码](how-to-document-code) 指南来记录你的新钩子。

当你创建了一个要发布到 AC 仓库的新钩子时，验收标准之一就是为其编写适当的文档，以便其他人知道如何正确使用它。所以，请仔细阅读该指南。

## 命名规范

每个钩子必须遵循以下命名规范：

`On[When]<Action>`

例如：

* `OnBeforeConfigLoad`
* `OnAfterArenaRatingCalculation`

动作（Action）通常与调用钩子的函数名保持一致。

如果父函数足够复杂，甚至包含多个不同的钩子，那么动作应反映该钩子的用途。

`[When]` 部分是可选的，但强烈建议保留。

它有助于理解钩子在父函数的哪个部分被调用。

例如，你可以同时拥有 `OnBeforeConfigLoad` 和 `OnAfterConfigLoad`，以在配置加载之前和之后改变行为。

## 高级钩子

### 如何改变函数的行为（过滤）

使用钩子，你不仅可以在特定时间运行特定操作，甚至还可以改变调用钩子的函数的行为。你有两种解决方案：

#### 1) 使用引用参数

这是最常见的一种。基本上利用按引用传递参数的概念，你可以改变传递给钩子本身的任何内容。
例如：

```cpp
OnMotdChange(std::string& newMotd)
```

通过使用 '&' 字符传递 newMotd，你允许监听器在该操作被调用时改变 Motd 的值。

#### 2) 使用 bool 返回值

这种方法不太常见，大多数钩子返回 "void" 类型，而且在大多数情况下使用引用更容易。但如果你确实需要，你可以实现一个以这种方式声明的钩子：

```cpp
bool ScriptMgr::OnBeforePlayerTeleport(Player* player, uint32 mapid, float x, float y, float z, float orientation, uint32 options, Unit* target)
{
    bool ret = true;

    FOR_SCRIPTS_RET(PlayerScript, itr, end, ret) // 如果没有脚本则默认返回 true
    if (!itr->second->OnBeforeTeleport(player, mapid, x, y, z, orientation, options, target))
        ret = false; // 只有当脚本返回 false 时我们才改变 ret 值

    return ret;
}
```

这个钩子会通知所有监听器，同时也会捕获是否有至少一个已注册的监听器返回了 "false"，在这种情况下最终返回值也将为 false。

在这个特定情况下，该钩子被用于一个 if 条件中，如果某个监听器因为某种原因返回了 **false**，则禁止玩家被传送。

你可以实现自己的不同逻辑（例如默认返回 false，只要有任何一个返回 true 即可），只要记得为它写合适的文档即可！

### 在你的模块内创建你自己的钩子系统

通过使用上面的指南，你甚至可以在你的模块中创建自己的 ScriptObject，以允许其他人扩展它。

有些模块，例如 auto-balance，通过使用内部钩子允许自定义其函数的某些部分。

你可以参考这个文件作为示例：https://github.com/azerothcore/mod-autobalance/blob/master/src/AutoBalance.h

{% include note.html content="你还需要创建自己的 ScriptMgr 实现，并提供一个单例来允许调用你的钩子。" %}

### 最后的考虑

ScriptAI 系统还有其它不同的功能没有包含在这份文档中，例如创建绑定到我们数据库中特定实体的脚本（例如 CreatureScript）。这种高级用法可以通过复制我们在 ScriptMgr 文件中的相关代码来实现。

如果你需要任何帮助，或者你想改进这份文档，请随时寻求支持并编辑此页面。

## 外部资源

- [Stack overflow 话题：是否可以把核心补丁转换成 AzerothCore 的模块？](https://stackoverflow.com/questions/66340549/is-it-possible-to-turn-a-core-patch-into-a-module-for-azerothcore/66340683#66340683)
