# Registro de cambios

Este archivo contiene los registros de cambios de todos los grandes cambios de la API.

## 6.0.0-dev.1 | Commit: [de13bf426e162ee10cbd5470cec74122d1d4afa0](https://github.com/azerothcore/azerothcore-wotlk/commit/de13bf426e162ee10cbd5470cec74122d1d4afa0)

### Cómo actualizar

- `PrepareStatement`

```diff
- setNull(...)
- setBool(...)
- setUInt8(...)
- setInt8(...)
- setUInt16(...)
- setInt16(...)
- setUInt32(...)
- setUInt64(...)
- setInt64(...)
- setFloat(...)
- setDouble(...)
- setString(...)
- setStringView(...)
- setBinary(...)
+ SetData(...)
```

- `Fields`

```diff
- GetBool()
+ Get<bool>()
```
```diff
- GetUInt8()
+ Get<uint8>()
```
```diff
- GetInt8()
+ Get<int8>()
```
```diff
- GetUInt16()
+ Get<uint16>()
```
```diff
- GetInt16()
+ Get<int16>()
```
```diff
- GetUInt32()
+ Get<uint32>()
```
```diff
- GetInt32()
+ Get<int32>()
```
```diff
- GetUInt64()
+ Get<uint64>()
```
```diff
- GetInt64()
+ Get<int64>()
```
```diff
- GetFloat()
+ Get<float>()
```
```diff
- GetDouble()
+ Get<double>()
```
```diff
- GetString()
+ Get<std::string>()
```
```diff
- GetStringView()
+ Get<std::string_view>()
```
```diff
- GetBinary()
+ Get<Binary>()
```

## 5.0.0-dev.1 | Commit: [8b7df23f064f8c1c41aea222342b53f109c4e3b9](https://github.com/azerothcore/azerothcore-wotlk/commit/8b7df23f064f8c1c41aea222342b53f109c4e3b9)

### Cómo actualizar

```diff
- time(nullptr)
+ GameTime::GetGameTime().count()
```
```diff
- sWorld->GetGameTime()
+ GameTime::GetGameTime().count()
```
```diff
- World::GetGameTimeMS()
+ GameTime::GetGameTimeMS().count()
```

## 5.0.0-dev.0 | Commit: [2fd8b00d7bac1f9c9b565916453cf490fb069df0](https://github.com/azerothcore/azerothcore-wotlk/commit/2fd8b00d7bac1f9c9b565916453cf490fb069df0)

Le sugerimos que utilice siempre la última versión de nuestra rama maestra.

- https://github.com/azerothcore/azerothcore-wotlk/tree/master

### Cómo actualizar

Para los administradores de servidores: las instrucciones sobre cómo actualizar los servidores existentes están disponibles [aquí](http://www.azerothcore.org/wiki/Upgrade-from-pre-2.0.0-to-latest-master).

### Notas de publicación

Este PR elimina la columna modelId de la tabla de criaturas para permitirnos pasar a un sistema de spawn de doble entrada.

Si esto causa un problema para los spawns del juego o personalizados, la siguiente línea de SAI puede actualizar el modelId.

```sql
(#entryorguid,0,0,0,11,0,100,0,0,0,0,0,0,3,0,#modelId,0,0,0,0,1,0,0,0,0,0,0,0,0,"Creature Name - On Spawn - Change Model to #modelId"),
```

Un agradecimiento especial a @Shin @Kitzunu @M'Dic por su ayuda.

## 4.0.0-dev.13 | Commit: [bc82f36f1ff46bb21d32e1cfdaec8271dde08af1](https://github.com/azerothcore/azerothcore-wotlk/commit/bc82f36f1ff46bb21d32e1cfdaec8271dde08af1)

### Añadido

```diff
// Unit.cpp
+ virtual void Talk(std::string_view text, ChatMsg msgType, Language language, float textRange, WorldObject const* target);
+ virtual void Say(std::string_view text, Language language, WorldObject const* target = nullptr);
+ virtual void Yell(std::string_view text, Language language, WorldObject const* target = nullptr);
+ virtual void TextEmote(std::string_view text, WorldObject const* target = nullptr, bool isBossEmote = false);
+ virtual void Whisper(std::string_view text, Language language, Player* target, bool isBossWhisper = false);
+ virtual void Talk(uint32 textId, ChatMsg msgType, float textRange, WorldObject const* target);
+ virtual void Say(uint32 textId, WorldObject const* target = nullptr);
+ virtual void Yell(uint32 textId, WorldObject const* target = nullptr);
+ virtual void TextEmote(uint32 textId, WorldObject const* target = nullptr, bool isBossEmote = false);
+ virtual void Whisper(uint32 textId, Player* target, bool isBossWhisper = false);
```

### Eliminado

```diff
// Object.cpp
- void MonsterSay(const char* text, uint32 language, WorldObject const* target);
- void MonsterYell(const char* text, uint32 language, WorldObject const* target);
- void MonsterTextEmote(const char* text, WorldObject const* target, bool IsBossEmote = false);
- void MonsterWhisper(const char* text, Player const* target, bool IsBossWhisper = false);
- void MonsterSay(int32 textId, uint32 language, WorldObject const* target);
- void MonsterYell(int32 textId, uint32 language, WorldObject const* target);
- void MonsterTextEmote(int32 textId, WorldObject const* target, bool IsBossEmote = false);
- void MonsterWhisper(int32 textId, Player const* target, bool IsBossWhisper = false);
- void SendPlaySound(uint32 Sound, bool OnlySelf);
```

### Cómo actualizar

```diff
- creature->MonsterSay(text, LANG_XXX, nullptr);
+ creature->Say(text, LANG_XXX);

- creature->MonsterTextEmote(text, 0);
+ creature->TextEmote(text);

- creature->MonsterWhisper(text, receiver);
+ creature->Whisper(text, LANG_XXX, receiver);

- creature->MonsterYell(text, LANG_XXX, NULL);
+ creature->Yell(text, LANG_XXX);

- creature->MonsterWhisper(text, target, isBossWhisper);
+ creature->Whisper(text, LANG_XXX, target, isBossWhisper);

- SendPlaySound(uint32 Sound, bool OnlySelf);
+ PlayDirectSound(uint32 sound_id, Player* target = nullptr);
```

## 4.0.0-dev.12 | Commit: [bcec4191e43de8a7b57a4219d6baaa7c5e3dfaf1](https://github.com/azerothcore/azerothcore-wotlk/commit/bcec4191e43de8a7b57a4219d6baaa7c5e3dfaf1)

### Añadido

- Se ha añadido el hook `OnPlayerPVPFlagChange`, que se ejecutará cuando se cambie la bandera pvp de un jugador.

## 4.0.0-dev.11 | Commit: [d18545263fda54e19c875d22adfb28ae4072ec01](https://github.com/azerothcore/azerothcore-wotlk/commit/d18545263fda54e19c875d22adfb28ae4072ec01)

### Añadido

- Se ha añadido `OnBeforeFinalizePlayerWorldSession` que puede utilizarse para modificar la versión de la caché que se envía al cliente a través de los módulos.

## 4.0.0-dev.10 | Commit: [0897705a6814fc19007e5f88fbcb98b3689880c9](https://github.com/azerothcore/azerothcore-wotlk/commit/0897705a6814fc19007e5f88fbcb98b3689880c9)

### Cómo actualizar

Actualiza tu versión de Boost a la 1.74 o superior.

## 4.0.0-dev.9 | Commit: [edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23](https://github.com/azerothcore/azerothcore-wotlk/commit/edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23)

Changelog para el commit "[feature(Core/Spells): Permitir aprender todos los hechizos para los personajes en la creación](https://github.com/azerothcore/azerothcore-wotlk/commit/06ee4ea7c46a5c0494dd7502a7646e84f83dab89)"

### Añadido

- Todas las habilidades de las clases hasta TBC en `playercreateinfo_spell_custom`.
- Opción de configuración PlayerStart.AllSpells - Si está activada, los jugadores empezarán con todos sus hechizos de clase (no talentos). Debes rellenar la tabla playercreateinfo_spell_custom con los hechizos que quieras, o no funcionará. La tabla tiene datos para todas las clases / razas hasta la expansión TBC.

### Eliminado

- Opción de configuración PlayerStart.CustomSpells

### Cómo actualizar

- Actualiza el archivo worldserver.conf con el nuevo PlayerStart.AllSpells si quieres cambiarlo a "ON". De lo contrario, irá con la opción por defecto "OFF" del archivo worldserver.conf.dist.

## 4.0.0-dev.8 | Commit: [edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23](https://github.com/azerothcore/azerothcore-wotlk/commit/edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23)

Registro de cambios para el commit "[fix(Core/Player): Use SkillLineAbility.dbc to determine player initial spells - skill assignment done in a new table `playercreateinfo_skills`](https://github.com/azerothcore/azerothcore-wotlk/commit/1be561e03b56dc396270335886e59eddad9fa0c6)"

### Añadido

- `playercreateinfo_skills` - Nueva tabla de base de datos para la asignación de habilidades.

### Eliminado

- `playercreateinfo_spells`

### Cambiado

- Utiliza `SkillLineAbility.dbc` para determinar los hechizos iniciales del jugador.
- Cambio de nombre de los campos `SkillLineAbilityEntry`

### Cómo actualizar

```diff
- uint32    id;                                           // 0        m_ID
- uint32    skillId;                                      // 1        m_skillLine
- uint32    spellId;                                      // 2        m_spell
- uint32    racemask;                                     // 3        m_raceMask
- uint32    classmask;                                    // 4        m_classMask
- //uint32    racemaskNot;                                // 5        m_excludeRace
- //uint32    classmaskNot;                               // 6        m_excludeClass
- uint32    req_skill_value;                              // 7        m_minSkillLineRank
- uint32    forward_spellid;                              // 8        m_supercededBySpell
- uint32    learnOnGetSkill;                              // 9        m_acquireMethod
- uint32    max_value;                                    // 10       m_trivialSkillLineRankHigh
- uint32    min_value;                                    // 11       m_trivialSkillLineRankLow
- //uint32    characterPoints[2];                         // 12-13    m_characterPoints[2]
+ uint32 ID;                                              // 0
+ uint32 SkillLine;                                       // 1
+ uint32 Spell;                                           // 2
+ uint32 RaceMask;                                        // 3
+ uint32 ClassMask;                                       // 4
+ //uint32 ExcludeRace;                                   // 5
+ //uint32 ExcludeClass;                                  // 6
+ uint32 MinSkillLineRank;                                // 7
+ uint32 SupercededBySpell;                               // 8
+ uint32 AcquireMethod;                                   // 9
+ uint32 TrivialSkillLineRankHigh;                        // 10
+ uint32 TrivialSkillLineRankLow;                         // 11
+ //uint32 CharacterPoints[2];                            // 12-13
```

- Por ejemplo `skillLine->forward_spellid` se convertirá en `skillLine->SupercededBySpell`

## 4.0.0-dev.7 | Commit: [59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244](https://github.com/azerothcore/azerothcore-wotlk/commit/59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244)

### Eliminado

- Gossip antiguos api [#5414](https://github.com/azerothcore/azerothcore-wotlk/pull/5414)

### Cómo actualizar

- `player->ADD_GOSSIP_ITEM(whatever)` -> `AddGossipItemFor(player, whatever)`
- `player->ADD_GOSSIP_ITEM_DB(whatever)` -> `AddGossipItemFor(player, whatever)`
- `player->ADD_GOSSIP_ITEM_EXTENDED(whatever)` -> `AddGossipItemFor(player, whatever)`
- `player->CLOSE_GOSSIP_MENU()` -> `CloseGossipMenuFor(player)`
- `player->SEND_GOSSIP_MENU(textid, creature->GetGUID())` -> `SendGossipMenuFor(player, textid, creature->GetGUID())`

También necesitas `#include "ScriptedGossip.h"` en tus archivos `.cpp`

## 4.0.0-dev.6 | Commit: [59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244](https://github.com/azerothcore/azerothcore-wotlk/commit/59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244)

### Cambiado

- Nuevas opciones para la carga de scripts `static dynamic minimal-static minimal-dynamic` [#5346](https://github.com/azerothcore/azerothcore-wotlk/pull/5346)

```
static - Construye estáticamente. Opción por defecto. para todos los scripts (Como era antes)

dynamic - Construye dinámicamente. Después de iniciar el soporte de Dynamic Linking Library (DLL) puede hacer una biblioteca separada para cada script. Ahora no soporta

minimal-static - construye comandos y hechizos estáticamente

minimal-dynamic - construye comandos y hechizos dinámicamente. Ahora no soporta
```

- También el valor por defecto que es proporcionado por la variable `SCRIPTS` es sobrescribible a través de la variable `SCRIPTS_COMMANDS, SCRIPTS_SPELLS...`.
- Cada subdirectorio contiene ahora su propia unidad de traducción que es responsable de cargar su directorio
- Si el módulo utiliza la api del cargador de scripts obsoleta, obtendrá un mensaje de error.

```cmake
> Module (mod-ah-bot) using deprecated loader api
```

### Cómo actualizar

- Para la mayoría de los módulos, el archivo `'CMakeLists.txt' ya no es necesario`.
- Es necesario cambiar el archivo del cargador de scripts.

```
1. Cambiar la extensión del archivo a `.cpp`.
2. Renombrar la función de carga general a `Add(nombre del módulo con reemplazo de todos los espacios en blanco a guiones bajos)Scripts()`.
3. Eliminar las macros `AC_ADD_SCRIPT_LOADER` de `CMakeLists.txt`.
```

- Ejemplo de script cargador de módulos:

```cpp
/*
 * Copyright (C) 2016+ AzerothCore <www.azerothcore.org>, released under GNU AGPL v3 license: https://github.com/azerothcore/azerothcore-wotlk/blob/master/LICENSE-AGPL3
 */

// From SC
void AddSC_ServerAutoShutdown();

// Add all scripts
void Addmod_server_auto_shutdownScripts()
{
    AddSC_ServerAutoShutdown();
}
```

- Los módulos de la lista soportan la nueva api del cargador de scripts:

https://github.com/azerothcore/mod-server-auto-shutdown

## 4.0.0-dev.5 | Commit: [59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244](https://github.com/azerothcore/azerothcore-wotlk/commit/59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244)

### Añadido
- Nueva opción de cmake `WITH_STRICT_DATABASE_TYPE_CHECKS` [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)

### Cambiado

- Evitar la mezcla de bases de datos con titulares de consultas [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)
- Evitar el uso de sentencias preparadas en una base de datos errónea [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)
- Impedir la confirmación de transacciones iniciadas en una base de datos diferente [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)
- Convertir las consultas asíncronas en nuevos callbacks de consulta [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)

### Cómo actualizar

- `PreparedStatement`

```diff
- PreparedStatement* stmt = LoginDatabase.GetPreparedStatement(LOGIN_UPD_LOGONPROOF);
+ LoginDatabasePreparedStatement* stmt = LoginDatabase.GetPreparedStatement(LOGIN_UPD_LOGONPROOF);
```

- `SQLTransaction`

```diff
- SQLTransaction trans = CharacterDatabase.BeginTransaction();
+ CharacterDatabaseTransaction trans = CharacterDatabase.BeginTransaction();
```

## 4.0.0-dev.4 | Commit: [fbad1f3d6c27a5d3eea22483913c67a827ab01be](https://github.com/azerothcore/azerothcore-wotlk/commit/fbad1f3d6c27a5d3eea22483913c67a827ab01be)

### Añadido

- Nuevo hook `OnBeforeSendJoinMessageArenaQueue` y `OnBeforeSendExitMessageArenaQueue`.

### Cambiado

- Cambiar el nombre de `CanExitJoinMessageArenaQueue` a `OnBeforeSendExitMessageArenaQueue`.
- Cambiar el nombre de `CanSendJoinMessageArenaQueue` a `OnBeforeSendJoinMessageArenaQueue`.

### Cómo actualizar

- Cambie el nombre de todos los hooks de `CanExitJoinMessageArenaQueue` y `CanSendMessageArenaQueue` por `OnBeforeSendExitMessageArenaQueue`.
- Cambia el nombre de todos los hooks de `CanSendJoinMessageArenaQueue` y `OnBeforeSendJoinMessageArenaQueue`.

## 4.0.0-dev.3 | Commit: [c35dde6fae732269357b78fb796fba21956b83fc](https://github.com/azerothcore/azerothcore-wotlk/commit/c35dde6fae732269357b78fb796fba21956b83fc)

- Registro de cambios para el commit "[refactor(Collision): Update some methods to UpperCamelCase](https://github.com/azerothcore/azerothcore-wotlk/commit/b84f9b8a4b334632cb37dcebbb2dd4e087f65610)"

### Changes

```diff
- getPosition
- getBounds
- getBounds2
- getInstanceMapTree
- getModelInstances
- getPosInfo
- getMeshData
- getGroupModels
- getIntersectionTime
- getObjectHitPos
- getAreaInfo
+ GetPosition
+ GetBounds
+ GetBounds2
+ GetInstanceMapTree
+ GetModelInstances
+ GetPosInfo
+ GetMeshData
+ GetGroupModels
+ GetIntersectionTime
+ GetObjectHitPos
+ GetAreaInfo
```

### Cómo actualizar

Si está utilizando alguno de esos métodos, simplemente cambie el nombre cambiando la primera letra del método de minúscula a mayúscula.

Ejemplo: `getAreaInfo` -> `GetAreaInfo`

## 4.0.0-dev.2 | Commit: [3f70d0b80ff483f142ffbebf8960aeb503913a35](https://github.com/azerothcore/azerothcore-wotlk/commit/3f70d0b80ff483f142ffbebf8960aeb503913a35)

### Añadido

- Se ha creado un nuevo sistema de registro de cambios.

### Cómo actualizar

Para crear un nuevo registro de cambios, siga las instrucciones de nuestra [página wiki].(https://www.azerothcore.org/wiki/es/how-to-use-changelog)
