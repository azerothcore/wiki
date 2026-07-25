---
tableofcontents: 1
---

# Estándares de código C++

## Introducción

### ¿Por qué son importantes los estándares de código?

Hacen más fácil para todos mantener y leer el código escrito, además de darnos más control sobre él.

También pueden actuar como una salvaguarda para prevenir errores en el código.

### ¿Por qué es importante que todos sigan los estándares?

Solo aceptamos código que esté escrito según los estándares; esto significa que un PR con el que quieras contribuir puede integrarse más rápido si sigues los estándares desde el principio.

## Estándares de código

### Tabs e indentación

Nunca usamos tabs; en su lugar, usamos espacios.

Un tab equivale a 4 espacios y eso es lo que debe usarse en todo el proyecto.

Visual Studio:

Tools -> Options -> Text Editor -> C/C++ -> Tabs -> Smart, 4, 4, Insert spaces.

Notepad++:

Settings -> Preferences -> Language -> Tab size: 4, Replace by space: checked

### Comentarios

Comenta siempre el código donde no sea código repetido típico y donde el código no sea autoexplicativo.

Evita incluir hipervínculos en los comentarios del código, ya que pueden quedar desactualizados o rotos con el tiempo. Si un enlace es relevante, inclúyelo en la descripción del pull request en su lugar; se puede referenciar más adelante mediante el historial de Git.

Los comentarios deben colocarse directamente encima del código, o directamente al lado de él.

```cpp
// A Comment
if (a == b)

if (a == b)
{
    a = b; // A Comment
```

### Espacios en blanco

No se permiten espacios en blanco al final de la línea (trailing whitespace).

Tampoco deberías tener espacios innecesarios dentro de un paréntesis. 

Incorrecto:

```cpp
if( var )
if ( var )
```

Correcto:

```cpp
if (var)
```

### Llaves

Se debe evitar usar llaves para las sentencias if que van seguidas de una sola línea.

```cpp
if (var)
{
    me->DoA();
    me->DoB();
}
else
    me->DoC();
```

### Sintaxis de bucles

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

**Ten en cuenta que las llaves siempre deben empezar en una nueva línea, como se muestra en el ejemplo de arriba.**

### Números aleatorios vs. constantes

Las constantes hacen el código más fácil de leer y entender; también proporcionan una salvaguarda y evitan que los números queden hard-coded.

Incorrecto:

```cpp
if (player->GetQuestStatus(10090) == 1)
    me->RemoveFlag(58, 2);
```

Correcto:

```cpp
if (player->GetQuestStatus(QUEST_BEAT_UP) == QUEST_STATUS_INCOMPLETE)
    me->RemoveFlag(UNIT_FIELD_FLAGS, UNIT_FLAG_NON_ATTACKABLE);
```

Las constantes se establecen con #defines, constexpr, o enum/enum class. Si no existe, crea una.

### Sentencias switch

Siempre debe estar presente una acción default en una sentencia switch, aunque sea solo un break.

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

### Enumeraciones vs. define

Se aconseja encarecidamente evitar usar #define para las constantes. Usa o bien una variable const o un enum si se pueden agrupar varias variables.

Los enums deben tener un nombre. Separa las constantes en diferentes enums según su tipo.

```cpp
enum Spells
{
    SPELL_1 = 1111,
    SPELL_2 = 2222,
    SPELL_3 = 3333
};

constexpr uint32 SPELL_4 = 4444;
```

### Enum vs. Enum Class

Se prefiere usar enum classes, ya que pueden causar menos sorpresas que podrían llevar a bugs, dado que el enum no se convertirá implícitamente a otros tipos como enteros u otros enums.

```cpp
enum class Spell : uint32
{
    One   = 1111,
    Two   = 2222,
    Three = 3333
}
```

### Prefijos estándar para constantes

Todas las constantes que almacenamos tienen un prefijo estandarizado.

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
| XX_G   | Heroic mode prefix (goes after the other prefix) XX is the max man amount from mode. (OBSOLETE AS OF PATCH 3.2 WITH SpellDifficulty.dbc) |
| RAID_XX | Raid mode prefix (goes before the other prefix) XX is the max man amount from mode. (OBSOLETE AS OF PATCH 3.2 WITH SpellDifficulty.dbc) |
| EVENT_ | Event/Encounter identifier for instances |
| DATA_  | Identifiers in instance used for GUIDs/data not being event/encounter |
| ACHIEV_ | Achievement ID |

Correcto:

```
SPELL_ENRAGE
SPELL_ENRAGE_H
EVENT_ILLIDAN
DATA_ILLIDAN
ACHIEVE_MAKE_IT_COUNT
```

### Nomenclatura de variables y funciones

¡Nunca uses NOTACIÓN HÚNGARA en los nombres de variables!

para miembros public/protected o variables globales:

```cpp
uint64 SomeGuid;
uint32 ShadowBoltTimer;
uint8 ShadowBoltCount;
bool IsEnraged;
float HeightData;
```

para miembros private:

```cpp
uint64 _someGuid;
uint32 _mapEntry;
uint8 _count;
bool _isDead;
float _heightData;
```

Los métodos siempre van en UpperCamelCase y sus parámetros en lowerCamelCase

```cpp
void DoSomething(uint32 someNumber)
{
    uint32 someOtherNumber = 5;
}
```

Usa siempre 'f' después de los valores float al declararlos para evitar warnings de compilación.

```cpp
float posX = 234.3456f;
```

### Array de structs:

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

Definimos los WorldObjects de esta forma:

```cpp
GameObject* go;
Creature* creature;
Item* item;
Player* player;
Unit* unit;
```

Nunca usamos declaraciones múltiples con punteros

```cpp
Something* obj1, *obj2;
```

La forma correcta de hacer esto es

```cpp
Something* obj1;
Something* obj2;
```

Las referencias se definen de forma similar (el & debe ir pegado al tipo)

```cpp
Creature& creature;
```

¡Nunca definas "me" en un script de creature u objeto!

'me' es el puntero a la creature u objeto scripteado.

### Definir variables const

La palabra clave const siempre debe ir después del nombre del tipo

```cpp
Player const* player; // player object is constant
Unit* const unit; // pointer to the unit is constant
SpellEntry const* const spell; // both spell and pointer to spell are constant
```

### Variables static

La palabra clave static siempre debe ponerse la primera

```cpp
static uint32 someVar = 5;
static float const otherVar = 1.0f;
```

### Header Guards

Todos los archivos de cabecera deben contener header guards

```cpp
#ifndef MY_HEADER_H
#define MY_HEADER_H

// Header content here

#endif // MY_HEADER_H
```

### Salida de texto

Toda la salida de texto de scripts/sistema/comandos de C++ debe usar [acore_string](acore_string) siempre que sea posible (p. ej. mensajes de ChatHandler, mensajes del sistema de scripts).

Los diálogos de NPC, emotes y otros textos dentro del juego que se gestionan mediante los sistemas de texto de la base de datos (como `creature_text`, `broadcast_text`, etc.) deben seguir usando esos sistemas en lugar de `acore_string`.

Al añadir nuevas strings, se debe proporcionar la localización para todos los idiomas disponibles.

**Consejo:** puedes usar IA para ayudarte a traducir las strings de localización.
