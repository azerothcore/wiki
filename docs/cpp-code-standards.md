---
tableofcontents: 1
---

# C++ Code Standards

## Intro

### Why are conding standards important?

It makes it easier for everyone to maintain and read the written code as well as it gives us more control over it.

It can also act as a safe guard to prevent errors in the code.

### Why is it important for everyone to follow the standards?

We only accept code that is written to the standards, this means that a PR you want to contribute with can be merged faster if you follow the standards from the beginning.

## Coding Standards

### Tabs and Indents

We never use tabs, instead we use spaces.

One tab is equal to 4 spaces and that is what should be used throughout the whole project.

Visual Studio:

Tools -> Options -> Text Editor -> C/C++ -> Tabs -> Smart, 4, 4, Insert spaces.

Notepad++:

Settings -> Preferences -> Language -> Tab size: 4, Replace by space: checked

### Comments

Always comment code where it is not typical repeated code and where the code is not self-explanatory.

Comments should either be placed dierectly above the code, or directly beside it.

```cpp
// A Comment
if (a == b)

if (a == b)
{
    a = b; // A Comment
```

### Whitespace

Trailing whitespace is a not allowed.

You should also not have unneeded spaces within a bracket. 

Wrong:

```cpp
if( var )
if ( var )
```

Correct:

```cpp
if (var)
```

### Brackets

When we work with if or else statements, etc, we always use brackets.

```cpp
if (var)
{
    me->DoA();
    me->DoB();
}
else
{
    me->DoC();
}
```

### Random numbers vs. Constants

Constants makes the code easier to read and understand, they also provide a safe guard and prevents numbers from being hard-coded.

Wrong:

```cpp
if (player->GetQuestStatus(10090) == 1)
{
    me->RemoveFlag(58, 2);
}
```

Correct:

```cpp
if (player->GetQuestStatus(QUEST_BEAT_UP) == QUEST_STATUS_INCOMPLETE)
{
    me->RemoveFlag(UNIT_FIELD_FLAGS, UNIT_FLAG_NON_ATTACKABLE);
}
```

### Enumerations vs. define

It is strongly advised to avoid using #define for constants. use either a const variable or an enum if multiple variables can be grouped togehter.

Enums must have a name. Separate constant on different enums depending on their type.

```cpp
enum Spells
{
    SPELL_1 = 1111
    SPELL_2 = 2222
    SPELL_3 = 3333
};

constexpr uint32 SPELL_4 = 4444;
```

### Standard prefixes for constants

All constants that we store have a standardized prefix.

| PREFIX | Comment  |
| :----- | :------- |
| SPELL_ | Spell ID |
| NPC_   | [creature_template.entry](creature_template#entry) |
| ITEM_  | [item_template.entry](item_template#entry) |
| GO_    | [gameobject_template.entry](gameobject_template#entry) |
| QUEST_ | [quest_template.id](quest_template#id) |
| SAY_   | [creature_text.GroupID](creature_text#groupid) |
| EMOTE_ | [creature_text.GroupID](creature_text#groupid) Different prefix from SAY_ to show that this is an emote. |
| MODEL_ | Creature model, DisplayID |
| H_XX   | Heroic mode prefix (goes before the other prefix) XX is max man amount from mode. (OBSOLETE AS OF PATCH 3.2 WITH SpellDifficulty.dbc) |
| RAID_XX | Raid mode prefix (goes before the other prefix) XX is max man amount from mode. (OBSOLETE AS OF PATCH 3.2 WITH SpellDifficulty.dbc) |
| EVENT_ | Event/Encounter identifier for instances |
| DATA_  | Identifiers in instance used for GUIDs/data not being event/encounter |
| ACHIEV_ | Achievement ID |

Correct:

```
SPELL_ENRAGE
H_SPELL_ENRAGE
EVENT_ILLIDAN
DATA_ILLIDAN
ACHIEVE_MAKE_IT_COUNT
```

### Naming of variables and functions

Never use HUNGARIAN NOTATION in variable names!

for public/protected members or global variables:

```cpp
uint64 SomeGuid;
uint32 ShadowBoltTimer;
uint8 ShadowBoltCount;
bool IsEnraged;
float HeightData;
```

for private members:

```cpp
uint64 _someGuid;
uint32 _mapEntry;
uint8 _count;
bool _isDead;
float _heightData;
```

Methods are always UpperCamelCase and their parameters in lowerCamelCase

```cpp
void DoSomething(uint32 someNumber)
{
    uint32 someOtherNumber = 5;
}
```

Always use 'f' after float values when declaring them to avoid compile warnings.

```cpp
float posX = 234.3456f;
```

### WorldObjects

We define WorldObjects in this way:

```cpp
GameObject* go;
Creature* creature;
Item* item;
Player* player;
Unit* unit;
```

We never use multiple declaration with pointers

```cpp
Something* obj1, *obj2;
```

The proper way to do this is

```cpp
Something* obj1;
Something* obj2;
```

References are defined in a similar way (& must be stuck to the type)

```cpp
Creature& creature;
```

Never define Creature\* me; in a creature script!
'me' is the pointer to the scripted creature.

### Defining const variables

const keyword should always go after type name

```cpp
Player const* player; // player object is constant
Unit* const unit; // pointer to the unit is constant
SpellEntry const* const spell; // both spell and pointer to spell are constant
```

### Static variables

static keyword always should be put as first

```cpp
static uint32 someVar = 5;
static float const otherVar = 1.0f;
```
