# 如何将 DBC 数据导入到 AC 数据库中

本指南将展示如何将 DBC 数据导入到 AzerothCore 数据库并对其进行编辑。在指南中，我们将以 AreaTable.dbc 为例，
将海加尔（Hyjal）区域从"普通"（Normal）改为"庇护所（允许决斗）"（Sanctuary (with duels allowed)）。
如果你这样做，该区域将变为跨阵营区域，例如你可以将其用于活动。

## 前置要求

- 用于 node-dbc-reader 的 [Nodejs](https://nodejs.org/en/)

## 快速入门

### 1. 安装我的 dbc-reader

克隆或下载[这个仓库](https://github.com/wowgaming/node-dbc-reader)，并在下载的文件夹内运行 `npm install`。

*如果你需要运行更复杂的命令，请阅读该仓库的文档。*

### 2. 搜索你的数据

运行此命令来检查区域是否正确：`npm run start -- --search="[616].includes({*})" --columns=ID AreaTable`

此命令将使用以下条件在 **ID** 列中搜索：`[616].includes({*})`，这意味着程序将搜索所有包含 [ ] 数组内值的 ID。在这种情况下，我们只需要值 616。

*注意：--search 选项基于 eval 实现，这意味着你可以运行任何 javascript 方法来执行比较。*

该命令的结果将是：
```json
{
    "ID": 616,
    "ContinentID": 1,
    "ParentAreaID": 0,
    "AreaBit": 619,
    "Flags": 64,
    "SoundProviderPref": 0,
    "SoundProviderPrefUnderwater": 11,
    "AmbienceID": 31,
    "ZoneMusic": 0,
    "IntroSound": 0,
    "ExplorationLevel": 0,
    "AreaName_Lang_enUS": "Hyjal",
    "AreaName_Lang_enGB": "",
    "AreaName_Lang_koKR": "",
    "AreaName_Lang_frFR": "",
    "AreaName_Lang_deDE": "",
    "AreaName_Lang_enCN": "",
    "AreaName_Lang_zhCN": "",
    "AreaName_Lang_enTW": "",
    "AreaName_Lang_zhTW": "",
    "AreaName_Lang_esES": "",
    "AreaName_Lang_esMX": "",
    "AreaName_Lang_ruRU": "",
    "AreaName_Lang_ptPT": "",
    "AreaName_Lang_ptBR": "",
    "AreaName_Lang_itIT": "",
    "AreaName_Lang_Unk": "",
    "AreaName_Lang_Mask": 16712190,
    "FactionGroupMask": 0,
    "LiquidTypeID_1": 0,
    "LiquidTypeID_2": 0,
    "LiquidTypeID_3": 0,
    "LiquidTypeID_4": 0,
    "MinElevation": -500,
    "Ambient_Multiplier": 0,
    "Lightid": 0
  }
  ````

值 `"Flags": 64` 表示"普通区域"，我们必须将其覆盖为 `19456 - 庇护所（允许决斗）`（Sanctuary (Duels allowed)）。

关于 DBC 文档，请查看[这个 wiki](https://wowdev.wiki/Category:DBC_WotLK)

你可以在[这里](areatable)查看标志列表

3. 导出 SQL

现在运行上面相同的命令，但使用输出类型：`npm run start -- -s "[616].includes({*})" -t sql  --columns=ID AreaTable` 来提取 INSERT 查询

输出：
```sql
INSERT IGNORE INTO areatable_dbc (`ID`,`ContinentID`,`ParentAreaID`,`AreaBit`,`Flags`,`SoundProviderPref`,`SoundProviderPrefUnderwater`,`AmbienceID`,`ZoneMusic`,`IntroSound`,`ExplorationLevel`,`AreaName_Lang_enUS`,`AreaName_Lang_enGB`,`AreaName_Lang_koKR`,`AreaName_Lang_frFR`,`AreaName_Lang_deDE`,`AreaName_Lang_enCN`,`AreaName_Lang_zhCN`,`AreaName_Lang_enTW`,`AreaName_Lang_zhTW`,`AreaName_Lang_esES`,`AreaName_Lang_esMX`,`AreaName_Lang_ruRU`,`AreaName_Lang_ptPT`,`AreaName_Lang_ptBR`,`AreaName_Lang_itIT`,`AreaName_Lang_Unk`,`AreaName_Lang_Mask`,`FactionGroupMask`,`LiquidTypeID_1`,`LiquidTypeID_2`,`LiquidTypeID_3`,`LiquidTypeID_4`,`MinElevation`,`Ambient_Multiplier`,`Lightid`)
 VALUES (616,1,0,619,64,0,11,31,0,0,0,"Hyjal","","","","","","","","","","","","","","","",16712190,0,0,0,0,0,-500,0,0);
````

4. 创建更新查询

创建更新查询以设置正确的阵营：

```sql
UPDATE areatable_dbc SET Flags=19456 WHERE ID=616
```

5. 创建你的 PR

如果你使用本指南来修复一个 bug（而不是用于定制目的），
现在你可以用上面的 2 个查询创建[你的 PR](how-to-create-a-pr)
