# scene\_template

[<-Back-to:World](database-world)

**The \`scene\_template\` table**

This table is used to store necessary data for scenes to run, e.g. ScriptPackageId and Flags.

**Table Structure**

| Field                | Type     | Attributes | Key | Null | Default | Extra | Comment |
| -------------------- | -------- | ---------- | --- | ---- | ------- | ----- | ------- |
| [SceneId][1]         | in(10)   | UNSIGNED   | PRI | NO   | NONE    |       |         |
| [Flags][2]           | INT      | UNSIGNED   |     | NO   | 16      |       |         |
| [ScriptPackageId][3] | INT      | UNSIGNED   |     | NO   | NONE    |       |         |
| [ScriptName][4]      | char(64) | UNSIGNED   |     | NO   | ' '     |       |         |

[1]: #sceneid
[2]: #flags
[3]: #scriptpackageid
[4]: #scriptname

**Description of the fields**

### SceneId

SceneId given by auras which have SPELL\_AURA\_SCENE\_PLAY (430).

Some scenes do not have a spell, this are handled by scripts.
Use C++ hook to start them, e.g.:

> player-&gt;GetSceneMgr().PlayScene(SceneId); 

### Flags

This flags handle behavior of scene.

| Flag                                            | Int Value | Bit value  | Comment                                         |
| ----------------------------------------------- | --------- | ---------- | ----------------------------------------------- |
| SCENEFLAG\_NONE                                 | 0         | 0x00000000 |                                                 |
| SCENEFLAG\_UNK1                                 | 1         | 0x00000001 | NYI                                             |
| SCENEFLAG\_UNK2 \| (SCENEFLAG\_CANCLE\_AT\_END) | 2         | 0x00000002 | Scene is being canceled at SceneComplete // NYI |
| SCENEFLAG\_NOT\_CANCELABLE                      | 4         | 0x00000004 | Player can't cancle scene (cinematic scenes)    |
| SCENEFLAG\_UNK8                                 | 8         | 0x00000008 | NYI                                             |
| SCENEFLAG\_UNK16                                | 16        | 0x00000010 | NYI                                             |
| SCENEFLAG\_UNK32                                | 32        | 0x00000020 | NYI                                             |

### ScriptPackageId

ScriptPackageId is the Id of the clientside SceneScriptPackage, see SceneScriptPackage.db2

### ScriptName

Name of script defined in: scene\_scripts.cpp
