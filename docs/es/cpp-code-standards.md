---
tableofcontents: 1
---

# Estándares de código C++

## Introducción

### ¿Por qué son importantes los estándares de codificación?

Facilita que todos mantengan y lean el código escrito y además nos da más control sobre él.

También puede actuar como medida de protección para evitar errores en el código.

### ¿Por qué es importante que todos cumplan las normas?

Solo aceptamos código escrito según los estándares, esto significa que un PR con el que desea contribuir se puede fusionar más rápido si sigue los estándares desde el principio.

## Estándares de codificación

### Tabulaciones y sangrías

Nunca utilizamos tabulaciones, en su lugar utilizamos espacios.

Una tabulación equivale a 4 espacios y eso es lo que se debe utilizar en todo el proyecto.

Visual Studio:

Tools -> Options -> Text Editor -> C/C++ -> Tabs -> Smart, 4, 4, Insert spaces.

Notepad++:

Settings -> Preferences -> Language -> Tab size: 4, Replace by space: checked

### Comentarios

Comente siempre el código cuando no sea un código repetido típico y cuando el código no se explique por sí solo.

Evite incluir hipervínculos en los comentarios de código, ya que podrían quedar obsoletos o inutilizables con el tiempo. Si un enlace es relevante, inclúyalo en la descripción de la solicitud de extracción; podrá consultarlo posteriormente a través del historial de Git.

Los comentarios deben colocarse directamente encima del código o directamente al lado de él.

```cpp
// Un comentario
if (a == b)

if (a == b)
{
    a = b; // Un comentario
```

### Espacio en blanco

No se permiten espacios finales.

Tampoco debe haber espacios innecesarios dentro de un corchete.

Equivocado:

```cpp
if( var )
if ( var )
```

Correcto:

```cpp
if (var)
```

### Soportes

Se debe evitar el uso de corchetes en sentencias if seguidas de una línea.

```cpp
if (var)
{
    me->DoA();
    me->DoB();
}
else
    me->DoC();
```

### Loop syntax

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

**Tenga en cuenta que los corchetes siempre deben comenzar en una nueva línea, como se muestra en el ejemplo anterior.**

### Números aleatorios vs. constantes

Las constantes hacen que el código sea más fácil de leer y comprender, también brindan protección y evitan que los números queden codificados.

Equivocado:

```cpp
if (player->GetQuestStatus(10090) == 1)
    me->RemoveFlag(58, 2);
```

Correct:

```cpp
if (player->GetQuestStatus(QUEST_BEAT_UP) == QUEST_STATUS_INCOMPLETE)
    me->RemoveFlag(UNIT_FIELD_FLAGS, UNIT_FLAG_NON_ATTACKABLE);
```

Las constantes se definen con #defines, constexpr o la clase enum/enum. Si no existe, se crea una.

### Sentencias de cambio

Una acción predeterminada siempre debe estar presente en una declaración switch, incluso si es solo una interrupción.

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

### Enumeraciones vs. definir

Se recomienda encarecidamente evitar el uso de #define para constantes. Utilice una variable constante o una enumeración si se pueden agrupar varias variables.

Las enumeraciones deben tener un nombre. Constantes independientes en diferentes enumeraciones según su tipo.

```cpp
enum Spells
{
    SPELL_1 = 1111,
    SPELL_2 = 2222,
    SPELL_3 = 3333
};

constexpr uint32 SPELL_4 = 4444;
```

### Enumeración vs. Clase de enumeración

Se prefiere utilizar clases de enumeración porque pueden causar menos sorpresas que podrían generar errores, ya que la enumeración no se convertirá implícitamente a otros tipos, como números enteros u otras enumeraciones.

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

| PREFIJO | Comentario                                                                                                                                                          |
| :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SPELL_  | Identificación del hechizo                                                                                                                                          |
| NPC_    | [creature_template.entry](creature_template#entry)                                                                                                                  |
| ITEM_   | [item_template.entry](item_template#entry)                                                                                                                          |
| GO_     | [gameobject_template.entry](gameobject_template#entry)                                                                                                              |
| QUEST_  | [quest_template.id](quest_template#id)                                                                                                                              |
| SAY_    | [creature_text.GroupID](creature_text#groupid)                                                                                                                      |
| EMOTE_  | [creature_text.GroupID](creature_text#groupid) Prefijo diferente de SAY_ para indicar que se trata de un gesto.                                                     |
| MODEL_  | Modelo de criatura, DisplayID                                                                                                                                       |
| XX_G    | Prefijo del modo heroico (va después del otro prefijo). XX es la cantidad máxima de jugadores del modo. (OBSOLETO A PARTIR DEL PARCHE 3.2 CON SpellDifficulty.dbc)  |
| RAID_XX | Prefijo del modo Incursión (antes del otro prefijo) XX: número máximo de jugadores del modo. (OBSOLETO A PARTIR DEL PARCHE 3.2 CON SpellDifficulty.dbc)             |
| EVENT_  | Identificador de evento/encuentro para instancias                                                                                                                   |
| DATA_   | Identificadores en la instancia utilizados para GUID/datos que no son eventos/encuentros                                                                            |
| ACHIEV_ | Identificación del logro                                                                                                                                            |

Correcto:

```
SPELL_ENRAGE
SPELL_ENRAGE_H
EVENT_ILLIDAN
DATA_ILLIDAN
ACHIEVE_MAKE_IT_COUNT
```

### Nomenclatura de variables y funciones

¡Nunca utilice NOTACIÓN HÚNGARA en los nombres de variables!

para miembros públicos/protegidos o variables globales:

```cpp
uint64 SomeGuid;
uint32 ShadowBoltTimer;
uint8 ShadowBoltCount;
bool IsEnraged;
float HeightData;
```

Para miembros privados:

```cpp
uint64 _someGuid;
uint32 _mapEntry;
uint8 _count;
bool _isDead;
float _heightData;
```

Los métodos siempre están en UpperCamelCase y sus parámetros en lowerCamelCase

```cpp
void DoSomething(uint32 someNumber)
{
    uint32 someOtherNumber = 5;
}
```

Utilice siempre 'f' después de los valores flotantes al declararlos para evitar advertencias de compilación.

```cpp
float posX = 234.3456f;
```

### Matriz de estructuras:

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

Definimos WorldObjects de esta manera:

```cpp
GameObject* go;
Creature* creature;
Item* item;
Player* player;
Unit* unit;
```

Nunca utilizamos declaraciones múltiples con punteros.

```cpp
Something* obj1, *obj2;
```

La forma correcta de hacerlo es

```cpp
Something* obj1;
Something* obj2;
```

Las referencias se definen de manera similar (y deben ajustarse al tipo)

```cpp
Creature& creature;
```

¡Nunca definas "yo" en un guión de criatura u objeto!

'me' es el puntero a la criatura u objeto programado.

### Definición de variables constantes

La palabra clave const siempre debe ir después del nombre del tipo

```cpp
Player const* player; // player object is constant
Unit* const unit; // pointer to the unit is constant
SpellEntry const* const spell; // both spell and pointer to spell are constant
```

### Variables estáticas

La palabra clave estática siempre debe colocarse primero

```cpp
static uint32 someVar = 5;
static float const otherVar = 1.0f;
```

### Protectores de cabecera

Todos los archivos de encabezado deben contener protectores de encabezado

```cpp
#ifndef MY_HEADER_H
#define MY_HEADER_H

// Contenido del encabezado aquí

#endif // MY_HEADER_H
```
