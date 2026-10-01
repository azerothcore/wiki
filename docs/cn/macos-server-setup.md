# macOS 服务器设置

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 2 步：核心安装](macos-core-installation)                                                                                      | [第 4 步：数据库安装 >>](database-installation)              |

**目录**
- [客户端数据文件（下载预解压文件）](#option-1-download-pre-extracted-files)
- [客户端数据解压工具（自行解压文件）](#option-2-extract-files-yourself)
- [配置文件：Worldserver 和 Authserver](#config-files-worldserver-and-authserver)

现在你已经编译好了源代码，需要添加必要的客户端数据。你可以下载预解压的文件，也可以使用编译好的解压工具自行解压文件。数据准备好之后，你必须更新 **worldserver.conf** 文件中的 **DataDir** 选项，使其指向包含数据的目录。

有些文件是可选的，但强烈推荐：

| 目录     |                    |
| :------- | :----------------- |
| dbc      | 必需               |
| maps     | 必需               |
| vmaps    | 强烈推荐           |
| mmaps    | 强烈推荐           |
| cameras  | 推荐               |

## 选项 1：下载预解压文件 {#option-1-download-pre-extracted-files}

如果你打算使用 enUS 客户端，可以下载下面的数据文件。如果你打算使用任何其他语言的客户端，则需要[自行解压](#option-2-extract-files-yourself)数据。

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> 数据文件 enUS (AC Data v20)</a>

1. 下载上面的文件。

2. 在 build 文件夹内创建一个名为 **data** 的新文件夹。例如 **$HOME/azeroth-server/data/**

3. 将 zip 文件中的文件解压到 **data** 文件夹中。

4. 编辑你的 [DataDir](#updating-datadir) 配置选项，将其指向你的文件夹位置。

## 选项 2：自行解压文件 {#option-2-extract-files-yourself}

**（如果你已经下载了上面的文件，则不需要执行此操作）**

进入你的 AzerothCore 构建目录（例如 $HOME/azeroth-server/bin/），并将以下文件复制到你的 World of Warcraft 二进制文件目录中。

* **mapextractor**
* **mmaps_generator**
* **vmap4assembler**
* **vmap4extractor**

**DBC 和 Maps 文件**

```
cd <your WoW client directory>
./mapextractor
```

**视觉地图（又称 vmaps）注意：如果在 vmap4extractor 完成之前停止它，你需要先删除 Buildings 目录再重新开始。**

你也可以解压 vmaps，根据你的机器配置，这将花费相当长的时间（在老硬件上可能需要数小时）。

```
cd <your WoW client directory>
./vmap4extractor
mkdir vmaps;
./vmap4assembler Buildings vmaps
```

完成后你会收到以下消息，可以安全地忽略它。

```
Processing Map 724
[################################################################]
Extracting GameObject models...Extracting World\Wmo\Band\Final_Stage.wmo
No such file.
Couldn't open RootWmo!!!
Done!
  
Extract V4.00 2012_02. Work complete. No errors.
```

**移动地图（又称 mmaps - 可选但推荐）**

解压 mmaps 将花费相当长的时间，具体取决于你的机器配置（最多可能需要数小时）。

```
cd <your WoW client directory>
mkdir mmaps;
./mmaps_generator
```

现在所有操作都已完成，你需要将 **dbc**、**maps**、**vmaps** 和 **mmaps** 文件夹复制到你的 AzerothCore 构建目录（例如 **$HOME/azeroth-server/data/**）。

## 配置文件：Worldserver 和 Authserver {#config-files-worldserver-and-authserver}

首先你需要找到两个默认配置文件（名为 **worldserver.conf.dist** 和 **authserver.conf.dist**）并复制它们。然后将副本重命名为不带 .dist 扩展名的同名文件。你可以在 /build/configs/ 中找到它们（位置可能有所不同）。

打开 .conf 文件并向下滚动到 LoginDatabaseInfo、WorldDatabaseInfo 和 CharacterDatabaseInfo，输入 MySQL 登录信息，以便服务器能够访问你的数据库。

在新编译的配置中，默认情况下你会得到以下值：
```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

它们遵循以下结构：

```
Variablename = "MySQLIP;Port;Username;Password;database"  
```

以下步骤必须验证：

- 如果 AzerothCore 安装在与运行 WoW 相同的计算机上，主机名（127.0.0.1）可以保持不变。
  如果不是，请遵循 [Realmlist 表](realmlist) 中的说明。

- 端口（3306）是标准配置值。如果你在 MySQL 设置中更改了默认端口，则必须相应地更改它。
  用户名和密码可以变化。你可以选择：

    - 使用默认的 acore / acore 用户名和密码组合。

    - 在你首选的数据库管理工具中的用户管理器（通常以一个像人形的图标标识）里创建一个独立的登录账号，并授予它必要的权限（SELECT、INSERT、UPDATE、DELETE 权限就足够了，而且更安全）。

### 更新 DataDir {#updating-datadir}

1. 在你的 **worldserver.conf** 文件中找到 **DataDir** 选项。

1. 将其编辑为你文件夹的路径。例如 **$HOME/azeroth-server/data/**

{% include tip.html content="对于大多数 **worldserver.conf** 设置的更改，你可以直接在游戏中输入 .reload config 来立即看到更改，而无需重启服务器。" %}

{% include warning.html content="AzerothCore 团队和所有者绝不赞助也不支持非法的公共服务器。如果你使用这些项目来运营非法的公共服务器，而不是用于测试和学习，那是你自己的个人选择。" %}

### （可选）通过环境变量配置选项

可以通过环境变量加载配置选项，你可以[在此处](config-overrides-with-env-var)阅读相关内容。

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                              |
| :----------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 2 步：核心安装](macos-core-installation)                                                                                      | [第 4 步：数据库安装 >>](database-installation)              |
