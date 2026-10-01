---
tableofcontents: 1
---

# C++ 代码规范

## 简介

### 为什么编码规范很重要？

它让每个人都能更容易地维护和阅读已编写的代码，同时也让我们对代码有更多的掌控力。

它还可以作为一种保障，防止代码中出现错误。

### 为什么每个人遵循规范都很重要？

我们只接受符合规范的代码，这意味着如果你从一开始就遵循规范，你想要贡献的 PR 就能更快地被合并。

## 编码规范

### 制表符与缩进

我们从不使用制表符，而是使用空格。

一个制表符等于 4 个空格，整个项目都应使用这一标准。

Visual Studio：

Tools -> Options -> Text Editor -> C/C++ -> Tabs -> Smart, 4, 4, Insert spaces。

Notepad++：

Settings -> Preferences -> Language -> Tab size: 4, Replace by space: 勾选

### 注释

对于非典型重复代码以及代码本身无法自解释的情况，务必添加注释。

避免在代码注释中包含超链接，因为它们可能会随着时间推移而过时或失效。如果某个链接是相关的，请将其包含在 Pull Request 的描述中——之后可以通过 Git 历史来引用它。

注释应放置在代码正上方，或紧邻代码旁边。

```cpp
// 一条注释
if (a == b)

if (a == b)
{
    a = b; // 一条注释
```

### 空白

不允许有行尾空白（trailing whitespace）。

括号内也不应有多余的空格。

错误示例：

```cpp
if( var )
if ( var )
```

正确示例：

```cpp
if (var)
```

### 大括号

对于后面只跟一行代码的 if 语句，应避免使用大括号。

```cpp
if (var)
{
    me->DoA();
    me->DoB();
}
else
    me->DoC();
```

### 循环语法

```cpp
for (uint32 i = 0; i < loopEnd; ++i)
{
    DoSomething();
    DoSomethingElse();
}

uint32 i = 0;
while (i < 10)
{
    DoSomething();
    DoSomethingElse();
    ++i;
}

do
{
    DoSomething();
    DoSomethingElse();
    ++i;
} while (i > 0);
```

**请注意，大括号应始终另起一行，如上例所示。**

### 随机数字 vs. 常量

常量让代码更容易阅读和理解，它们还能提供保障并防止数字被硬编码。

错误示例：

```cpp
if (player->GetQuestStatus(10090) == 1)
    me->RemoveFlag(58, 2);
```

正确示例：

```cpp
if (player->GetQuestStatus(QUEST_BEAT_UP) == QUEST_STATUS_INCOMPLETE)
    me->RemoveFlag(UNIT_FIELD_FLAGS, UNIT_FLAG_NON_ATTACKABLE);
```

常量通过 #define、constexpr 或 enum/enum class 来定义。如果不存在这样的常量，就创建一个。

### Switch 语句

switch 语句中应始终包含 default 分支，即使它只是一个 break。

```cpp
switch (spells)
{
    case SPELL_1:
    case SPELL_2:
    {
        if (moreThanOneLine)
            UseBrackets();
        break;
    }
    case SPELL_3:
        DoSomethinCool();
        [[fallthrough]]
    default:
        break;
}
```

### 枚举 vs. define

强烈建议避免使用 #define 来定义常量。如果多个变量可以组合在一起，请使用 const 变量或枚举。

枚举必须有名称。根据类型的不同，将相关的常量划分到不同的枚举中。

```cpp
enum Spells
{
    SPELL_1 = 1111,
    SPELL_2 = 2222,
    SPELL_3 = 3333
};

constexpr uint32 SPELL_4 = 4444;
```

### 枚举 vs. 枚举类

优先使用枚举类（enum class），因为它们能带来更少的意外，避免因枚举隐式转换为其他类型（如整数或其他枚举）而导致 bug。

```cpp
enum class Spell : uint32
{
    One   = 1111,
    Two   = 2222,
    Three = 3333
}
```

### 常量的标准前缀

我们存储的所有常量都有一个标准化的前缀。

| 前缀    | 注释                                                                       |
| :------ | :------------------------------------------------------------------------- |
| SPELL_  | 法术 ID                                                                    |
| NPC_    | [creature_template.entry](creature_template#entry)                         |
| ITEM_   | [item_template.entry](item_template#entry)                                 |
| GO_     | [gameobject_template.entry](gameobject_template#entry)                     |
| QUEST_  | [quest_template.id](quest_template#id)                                     |
| SAY_    | [creature_text.GroupID](creature_text#groupid)                             |
| EMOTE_  | [creature_text.GroupID](creature_text#groupid)，与 SAY_ 前缀不同，用于表示这是表情。 |
| MODEL_  | 生物模型，DisplayID                                                        |
| XX_G    | 英雄模式前缀（位于其他前缀之后）XX 是模式中的最大人数。（自补丁 3.2 起已弃用，见 SpellDifficulty.dbc） |
| RAID_XX | 团队模式前缀（位于其他前缀之前）XX 是模式中的最大人数。（自补丁 3.2 起已弃用，见 SpellDifficulty.dbc） |
| EVENT_  | 副本的事件/Boss 战标识符                                                    |
| DATA_   | 副本中用于 GUID/数据（非事件/Boss 战）的标识符                              |
| ACHIEV_ | 成就 ID                                                                    |

正确示例：

```
SPELL_ENRAGE
SPELL_ENRAGE_H
EVENT_ILLIDAN
DATA_ILLIDAN
ACHIEVE_MAKE_IT_COUNT
```

### 变量和函数的命名

变量名中绝不使用匈牙利命名法（HUNGARIAN NOTATION）！

对于 public/protected 成员或全局变量：

```cpp
uint64 SomeGuid;
uint32 ShadowBoltTimer;
uint8 ShadowBoltCount;
bool IsEnraged;
float HeightData;
```

对于 private 成员：

```cpp
uint64 _someGuid;
uint32 _mapEntry;
uint8 _count;
bool _isDead;
float _heightData;
```

方法始终使用大驼峰命名（UpperCamelCase），其参数使用小驼峰命名（lowerCamelCase）。

```cpp
void DoSomething(uint32 someNumber)
{
    uint32 someOtherNumber = 5;
}
```

声明浮点数值时，始终在值后面加上 'f'，以避免编译警告。

```cpp
float posX = 234.3456f;
```

### 结构体数组：

```cpp
Position const PosMobs[5] =
{
    {-724.12f, -176.64f, 430.03f, 2.543f},
    {-766.70f, -225.03f, 430.50f, 1.710f},
    {-729.54f, -186.26f, 430.12f, 1.902f},
    {-756.01f, -219.23f, 430.50f, 2.369f},
    {-798.01f, -227.24f, 429.84f ,1.446f},
};
```

### WorldObjects

我们以这种方式定义 WorldObject：

```cpp
GameObject* go;
Creature* creature;
Item* item;
Player* player;
Unit* unit;
```

我们绝不在一条声明语句中使用多个带指针的变量。

```cpp
Something* obj1, *obj2;
```

正确的方式是：

```cpp
Something* obj1;
Something* obj2;
```

引用以类似的方式定义（& 必须紧贴类型）。

```cpp
Creature& creature;
```

绝不在生物或对象脚本中定义 "me"！

'me' 是指向被脚本化的生物或对象的指针。

### 定义 const 变量

const 关键字应始终放在类型名之后。

```cpp
Player const* player; // player 对象是常量
Unit* const unit; // 指向 unit 的指针是常量
SpellEntry const* const spell; // spell 和指向 spell 的指针都是常量
```

### 静态变量

static 关键字应始终放在最前面。

```cpp
static uint32 someVar = 5;
static float const otherVar = 1.0f;
```

### 头文件保护符

所有头文件都应包含头文件保护符（header guard）。

```cpp
#ifndef MY_HEADER_H
#define MY_HEADER_H

// 此处为头文件内容

#endif // MY_HEADER_H
```

### 包含（Includes）

每个头文件都必须**自包含（self-contained）**：它必须能够独立编译，而不依赖其他头文件提前被包含。这样可以防止隐藏的脆弱依赖关系。如果 `A` 需要 `B` 和 `C`，它就应该同时包含 `B` 和 `C`。它不应该仅仅因为 `B` 恰好当前包含了 `C` 就只包含 `B`。`A` 也不应包含任何它不直接使用的内容。

包含语句应写成一个单独的代码块，块内不包含空行，并按以下顺序排列：

1. 在 .cpp 文件中，首先包含文件自身的头文件（如果该 .cpp 需要包含自身的头文件）。
2. 然后包含所有其他项目头文件，按字母顺序排列。
3. 最后包含所有库头文件，按字母顺序排列。

ItemEnchantmentMgr.cpp 示例：

```cpp
#include "ItemEnchantmentMgr.h"   // 文件自身的头文件，放在最前面
#include "DBCStores.h"            // 然后是按字母顺序排列的项目头文件
#include "DatabaseEnv.h"
#include "Log.h"
#include "ObjectMgr.h"
#include "QueryResult.h"
#include "Timer.h"
#include "Util.h"
#include <cmath>                  // 然后是按字母顺序排列的库头文件
#include <functional>
#include <vector>
```

字母顺序区分大小写（ASCII 顺序）：大写字母排在小写字母之前。在上面的示例中，`DBCStores.h` 排在 `DatabaseEnv.h` 之前，因为大写 `B` 排在小写 `a` 之前。

项目头文件使用双引号（`"..."`）；库头文件（C++ 标准库、boost 等）使用尖括号（`<...>`）。捆绑在代码库中的第三方库（如 G3D）是例外，它使用双引号，但排序时仍与库头文件放在一起，而不是与项目头文件放在一起。

WaypointDefines.h 示例：

```cpp
#include "Define.h"          // 按字母顺序排列的项目头文件
#include "G3D/Vector3.h"     // 然后是按字母顺序排列的库头文件
#include <optional>
#include <vector>
```

条件编译的包含是单块规则的一个例外。将所有无条件包含保持在一个有序的代码块中，然后将带 `#if` / `#ifdef` 保护的包含放在其后，并用一个空行分隔。不要为了把受保护的包含放在相关包含旁边而打乱有序的代码块。

Errors.cpp 示例（已简化）：

```cpp
#include "Errors.h"
#include "Duration.h"
#include <cstdio>
#include <cstdlib>
#include <thread>

#if AC_PLATFORM == AC_PLATFORM_WINDOWS
#include <Windows.h>
#endif
```

只有当头文件本身是针对特定平台或特定配置时，才需要为包含添加保护。绝不要为了绕过其他地方的构建错误而用保护包裹普通包含，也绝不要因为其他头文件恰好会在当前配置下引入某个头文件就省略该包含——这正是自包含规则要防止的隐藏依赖。

### 文本输出

所有 C++ 脚本/系统/命令的文本输出，只要可能，都必须使用 [acore_string](acore_string)（例如，ChatHandler 消息、脚本系统消息）。

NPC 对话、表情以及其他通过数据库文本系统（如 `creature_text`、`broadcast_text` 等）管理的游戏内文本，应继续使用这些系统，而不是 `acore_string`。

在添加新字符串时，必须为所有可用语言提供本地化翻译。

**提示：** 你可以使用 AI 来协助翻译本地化字符串。
