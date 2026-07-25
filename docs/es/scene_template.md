# scene\_template

[<-Volver a: World](database-world)

**Tabla \`scene\_template\`**

Esta tabla se usa para almacenar los datos necesarios para que las escenas se ejecuten, p. ej. ScriptPackageId y Flags.

**Estructura**

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

**Descripción de los campos**

### SceneId

SceneId dado por las auras que tienen SPELL\_AURA\_SCENE\_PLAY (430).

Algunas escenas no tienen un hechizo, estas se gestionan mediante scripts.
Usa un hook de C++ para iniciarlas, p. ej.:

> player-&gt;GetSceneMgr().PlayScene(SceneId); 

### Flags

Estos flags controlan el comportamiento de la escena.

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

ScriptPackageId es el Id del SceneScriptPackage del lado del cliente, ver SceneScriptPackage.db2

### ScriptName

Nombre del script definido en: scene\_scripts.cpp
