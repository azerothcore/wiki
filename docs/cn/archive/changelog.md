# 更新日志

本文件包含所有重大 API 变更的更新日志。

## 6.0.0-dev.1 | Commit: [de13bf426e162ee10cbd5470cec74122d1d4afa0](https://github.com/azerothcore/azerothcore-wotlk/commit/de13bf426e162ee10cbd5470cec74122d1d4afa0)


### 如何升级
- `PrepareStatment`

```diff
- setNull(...)
+ SetData(...)
```
```diff
- setBool(...)
+ SetData(...)
```
```diff
- setUInt8(...)
+ SetData(...)
```
```diff
- setInt8(...)
+ SetData(...)
```
```diff
- setUInt16(...)
+ SetData(...)
```
```diff
- setInt16(...)
+ SetData(...)
```
```diff
- setUInt32(...)
+ SetData(...)
```
```diff
- setUInt64(...)
+ SetData(...)
```
```diff
- setInt64(...)
+ SetData(...)
```
```diff
- setFloat(...)
+ SetData(...)
```
```diff
- setDouble(...)
+ SetData(...)
```
```diff
- setString(...)
+ SetData(...)
```
```diff
- setStringView(...)
+ SetData(...)
```
```diff
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


### 如何升级

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


我们建议你始终使用我们 master 分支的最新版本。
https://github.com/azerothcore/azerothcore-wotlk/tree/master

### 如何升级

对于服务器管理员：关于如何升级现有服务器的说明可参见[此处](http://www.azerothcore.org/wiki/Upgrade-from-pre-2.0.0-to-latest-master)。

### 发布说明

此 PR 从 creature 表中移除了 modelId 列，以便我们迁移到双 entry 刷新系统。

如果这对游戏内或自定义刷新造成问题，可以使用以下 SAI 语句来更新 modelId。

(#entryorguid,0,0,0,11,0,100,0,0,0,0,0,0,3,0,#modelId,0,0,0,0,1,0,0,0,0,0,0,0,0,"Creature Name - On Spawn - Change Model to #modelId"),

特别感谢 @Shin @Kitzunu @M'Dic 的协助。

## 4.0.0-dev.13 | Commit: [bc82f36f1ff46bb21d32e1cfdaec8271dde08af1](https://github.com/azerothcore/azerothcore-wotlk/commit/bc82f36f1ff46bb21d32e1cfdaec8271dde08af1)


### 新增

```cpp
// Unit.cpp
    virtual void Talk(std::string_view text, ChatMsg msgType, Language language, float textRange, WorldObject const* target);
    virtual void Say(std::string_view text, Language language, WorldObject const* target = nullptr);
    virtual void Yell(std::string_view text, Language language, WorldObject const* target = nullptr);
    virtual void TextEmote(std::string_view text, WorldObject const* target = nullptr, bool isBossEmote = false);
    virtual void Whisper(std::string_view text, Language language, Player* target, bool isBossWhisper = false);
    virtual void Talk(uint32 textId, ChatMsg msgType, float textRange, WorldObject const* target);
    virtual void Say(uint32 textId, WorldObject const* target = nullptr);
    virtual void Yell(uint32 textId, WorldObject const* target = nullptr);
    virtual void TextEmote(uint32 textId, WorldObject const* target = nullptr, bool isBossEmote = false);
    virtual void Whisper(uint32 textId, Player* target, bool isBossWhisper = false);
```

### 移除

```cpp
// Object.cpp
    void MonsterSay(const char* text, uint32 language, WorldObject const* target);
    void MonsterYell(const char* text, uint32 language, WorldObject const* target);
    void MonsterTextEmote(const char* text, WorldObject const* target, bool IsBossEmote = false);
    void MonsterWhisper(const char* text, Player const* target, bool IsBossWhisper = false);
    void MonsterSay(int32 textId, uint32 language, WorldObject const* target);
    void MonsterYell(int32 textId, uint32 language, WorldObject const* target);
    void MonsterTextEmote(int32 textId, WorldObject const* target, bool IsBossEmote = false);
    void MonsterWhisper(int32 textId, Player const* target, bool IsBossWhisper = false);

    void SendPlaySound(uint32 Sound, bool OnlySelf);
```

### 如何升级

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
 PlayDirectSound(uint32 sound_id, Player* target = nullptr);
```

## 4.0.0-dev.12 | Commit: [bcec4191e43de8a7b57a4219d6baaa7c5e3dfaf1](https://github.com/azerothcore/azerothcore-wotlk/commit/bcec4191e43de8a7b57a4219d6baaa7c5e3dfaf1)



### 新增

- 新增了 `OnPlayerPVPFlagChange` 钩子，它会在玩家的 PVP 标记发生改变后被触发。



## 4.0.0-dev.11 | Commit: [d18545263fda54e19c875d22adfb28ae4072ec01](https://github.com/azerothcore/azerothcore-wotlk/commit/d18545263fda54e19c875d22adfb28ae4072ec01)


### 新增

- 新增了 `OnBeforeFinalizePlayerWorldSession `，可用于通过模块修改发送给客户端的缓存版本。
## 4.0.0-dev.10 | Commit: [0897705a6814fc19007e5f88fbcb98b3689880c9](https://github.com/azerothcore/azerothcore-wotlk/commit/0897705a6814fc19007e5f88fbcb98b3689880c9)


### 如何升级

将你的 Boost 版本升级到 1.74 或更高。

## 4.0.0-dev.9 | Commit: [edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23](https://github.com/azerothcore/azerothcore-wotlk/commit/edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23)


提交 "[feature(Core/Spells): Allow to learn all spells for characters on creation](https://github.com/azerothcore/azerothcore-wotlk/commit/06ee4ea7c46a5c0494dd7502a7646e84f83dab89)" 的更新日志

### 新增

- 将 TBC 及之前各职业的所有技能写入 playercreateinfo_spell_custom
- 配置项 PlayerStart.AllSpells - 如果启用，玩家将拥有其职业的所有技能（不包括天赋）。你必须先在 playercreateinfo_spell_custom 表中填入你想要的技能，否则此功能不会生效！该表包含 TBC 及之前版本中所有职业 / 种族的数据。

### 移除

- 配置项 PlayerStart.CustomSpells

### 如何升级

- 如果你想将 PlayerStart.AllSpells 改为 "ON"，请在 worldserver.conf 文件中更新该配置项。否则它将使用 worldserver.conf.dist 文件中的默认值 "OFF"。

## 4.0.0-dev.8 | Commit: [edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23](https://github.com/azerothcore/azerothcore-wotlk/commit/edfc2a8db48a17bf3e9ace0b36edc819aa0e5e23)


提交 "[fix(Core/Player): Use SkillLineAbility.dbc to determine player initial spells - skill assignment done in a new table `playercreateinfo_skills`](https://github.com/azerothcore/azerothcore-wotlk/commit/1be561e03b56dc396270335886e59eddad9fa0c6)" 的更新日志

### 新增

- playercreateinfo_skills - 用于技能分配的新数据库表。

### 移除

- playercreateinfo_spells

### 变更

- 使用 SkillLineAbility.dbc 确定玩家的初始技能。
- 重命名了 SkillLineAbilityEntry 字段

### 如何升级

```diff
-    uint32    id;                                           // 0        m_ID
-    uint32    skillId;                                      // 1        m_skillLine
-    uint32    spellId;                                      // 2        m_spell
-    uint32    racemask;                                     // 3        m_raceMask
-    uint32    classmask;                                    // 4        m_classMask
-    //uint32    racemaskNot;                                // 5        m_excludeRace
-    //uint32    classmaskNot;                               // 6        m_excludeClass
-    uint32    req_skill_value;                              // 7        m_minSkillLineRank
-    uint32    forward_spellid;                              // 8        m_supercededBySpell
-    uint32    learnOnGetSkill;                              // 9        m_acquireMethod
-    uint32    max_value;                                    // 10       m_trivialSkillLineRankHigh
-    uint32    min_value;                                    // 11       m_trivialSkillLineRankLow
-    //uint32    characterPoints[2];                         // 12-13    m_characterPoints[2]
+    uint32 ID;                                              // 0
+    uint32 SkillLine;                                       // 1
+    uint32 Spell;                                           // 2
+    uint32 RaceMask;                                        // 3
+    uint32 ClassMask;                                       // 4
+    //uint32 ExcludeRace;                                   // 5
+    //uint32 ExcludeClass;                                  // 6
+    uint32 MinSkillLineRank;                                // 7
+    uint32 SupercededBySpell;                               // 8
+    uint32 AcquireMethod;                                   // 9
+    uint32 TrivialSkillLineRankHigh;                        // 10
+    uint32 TrivialSkillLineRankLow;                         // 11
+    //uint32 CharacterPoints[2];                            // 12-13
```

- 例如 skillLine->forward_spellid 将变为 skillLine->SupercededBySpell

## 4.0.0-dev.7 | Commit: [59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244](https://github.com/azerothcore/azerothcore-wotlk/commit/59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244)


### 移除
- 旧的 gossips API [#5414](https://github.com/azerothcore/azerothcore-wotlk/pull/5414)

### 如何升级
- `player->ADD_GOSSIP_ITEM(whatever)` -> `AddGossipItemFor(player, whatever)`
- `player->ADD_GOSSIP_ITEM_DB(whatever)` -> `AddGossipItemFor(player, whatever)`
- `player->ADD_GOSSIP_ITEM_EXTENDED(whatever)` -> `AddGossipItemFor(player, whatever)`
- `player->CLOSE_GOSSIP_MENU()` -> `CloseGossipMenuFor(player)`
- `player->SEND_GOSSIP_MENU(textid, creature->GetGUID())` -> `SendGossipMenuFor(player, textid, creature->GetGUID())`

你还需要在你的 cpp 文件中包含 `#include "ScriptedGossip.h"`

## 4.0.0-dev.6 | Commit: [59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244](https://github.com/azerothcore/azerothcore-wotlk/commit/59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244)


### 变更
- 新增脚本加载选项 `static dynamic minimal-static minimal-dynamic` [#5346](https://github.com/azerothcore/azerothcore-wotlk/pull/5346)
```
static - 静态构建。默认选项。适用于所有脚本（和之前一样）
dynamic - 动态构建。后续将支持动态链接库（DLL），可为每个脚本生成独立的库。目前不支持
minimal-static - 静态构建命令和技能
minimal-dynamic - 动态构建命令和技能。目前不支持
```
- 此外，由 `SCRIPTS` 变量提供的默认值可以通过 `SCRIPTS_COMMANDS, SCRIPTS_SPELLS...` 变量覆盖。
- 现在每个子目录都包含自己的翻译单元（translation unit），负责加载其所在目录
- 如果模块使用了已废弃的脚本加载器 API，你将收到错误提示。
```cmake
> Module (mod-ah-bot) using deprecated loader api
```

### 如何升级
- 对大多数模块而言，不再需要 `CMakeLists.txt' 文件
- 需要修改脚本加载器文件。
```
1. 将文件中的扩展名改为 `.cpp`
2. 将通用加载函数重命名为 `Add(模块名（将所有空白字符替换为 '_')Scripts()`。
3. 从 `CMakeLists.txt` 中删除宏 `AC_ADD_SCRIPT_LOADER`
```
- 模块的加载脚本示例：
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
- 支持新脚本加载器 API 的模块列表：
https://github.com/azerothcore/mod-server-auto-shutdown

## 4.0.0-dev.5 | Commit: [59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244](https://github.com/azerothcore/azerothcore-wotlk/commit/59a3912a3b3bd4dd2d8e2b1c2cdd225b9c4d6244)


### 新增
- 新的 cmake 选项 `WITH_STRICT_DATABASE_TYPE_CHECKS` [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)

### 变更
- 防止将不同的数据库与查询持有者（query holder）混用 [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)
- 防止在错误的数据库上使用预编译语句（prepared statement） [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)
- 防止提交在其他数据库上启动的事务 [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)
- 将异步查询转换为新的查询回调 [#5611](https://github.com/azerothcore/azerothcore-wotlk/pull/5611)

### 如何升级
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


### 新增
- 新的钩子 `OnBeforeSendJoinMessageArenaQueue` 和 `OnBeforeSendExitMessageArenaQueue`

### 变更
- 将 `CanExitJoinMessageArenaQueue` 重命名为 `OnBeforeSendExitMessageArenaQueue`
- 将 `CanSendJoinMessageArenaQueue` 重命名为 `OnBeforeSendJoinMessageArenaQueue`

### 如何升级
- 只需将所有 `CanExitJoinMessageArenaQueue` 和 `CanSendMessageArenaQueue` 钩子重命名为 `OnBeforeSendExitMessageArenaQueue`
- 只需将所有 `CanSendJoinMessageArenaQueue` 钩子重命名为 `OnBeforeSendJoinMessageArenaQueue`

## 4.0.0-dev.3 | Commit: [c35dde6fae732269357b78fb796fba21956b83fc](https://github.com/azerothcore/azerothcore-wotlk/commit/c35dde6fae732269357b78fb796fba21956b83fc)


提交 "[refactor(Collision): Update some methods to UpperCamelCase](https://github.com/azerothcore/azerothcore-wotlk/commit/b84f9b8a4b334632cb37dcebbb2dd4e087f65610)" 的更新日志

### 变更

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

### 如何升级

如果你使用了这些方法中的任何一个，只需将方法名的首字母从小写改为大写即可。

示例：`getAreaInfo` -> `GetAreaInfo`

## 4.0.0-dev.2 | Commit: [3f70d0b80ff483f142ffbebf8960aeb503913a35](https://github.com/azerothcore/azerothcore-wotlk/commit/3f70d0b80ff483f142ffbebf8960aeb503913a35)


### 新增
- 创建了新的更新日志系统。
