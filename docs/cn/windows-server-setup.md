# Windows 服务器设置

| 安装指南                                                                                                                        |                                                          |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上一个链接在各步骤之间轻松跳转。                                                |
| [<< 第 2 步：核心安装](windows-core-installation)                                                                                | [第 4 步：数据库安装 >>](database-installation)          |

**目录**
- [客户端数据文件（下载预提取文件）](#option-1-download-pre-extracted-files)
- [客户端数据提取器（自行提取文件）](#option-2-extract-files-yourself)
- [配置文件：Worldserver 和 Authserver](#config-files-worldserver-and-authserver)

现在你已经编译好了源代码，接下来需要添加必要的客户端数据。你可以选择下载预提取的文件，也可以使用编译好的提取器自行提取文件。数据准备好后，你必须更新 **worldserver.conf** 文件中的 **DataDir** 选项，使其指向包含数据的目录。

有些文件是可选的，但强烈推荐：

| 目录     |                    |
| :------- | :----------------- |
| dbc      | 必需               |
| maps     | 必需               |
| vmaps    | 强烈推荐           |
| mmaps    | 强烈推荐           |
| cameras  | 推荐               |

## 选项 1：下载预提取文件 {#option-1-download-pre-extracted-files}

如果你打算使用 enUS 客户端，可以下载下面的数据文件。如果你打算使用任何其他语言的客户端，则需要自行 [提取](#option-2-extract-files-yourself) 数据。

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> 数据文件 enUS（AC Data v20）</a>

1. 下载上面的文件。

2. 在构建文件夹中创建一个名为 **Data** 的新文件夹。例如 **C:\Build\bin\RelWithDebInfo\Data**

3. 解压 zip 文件中的文件，并将它们放入 **Data** 文件夹中。

4. 将 [DataDir](#updating-datadir) 配置选项修改为你文件夹的位置。

## 选项 2：自行提取文件 {#option-2-extract-files-yourself}

**（如果你下载了上面的文件，则不需要）**

1. 进入你的构建目录（**C:\Build\bin\RelWithDebInfo\\**），并将以下文件复制到你的 World of Warcraft 文件夹中（wow.exe 所在的位置）。
```
mapextractor.exe
mmaps_generator.exe
vmap4extractor.exe
vmap4assembler.exe
mmaps-config.yaml
```

2. 进入 **C:\Azerothcore\apps\extractor**，将"**extractor.bat**"与之前的文件一起复制到你的 World of Warcraft 文件夹中。

3. 在你的 World of Warcraft 目录中创建 **mmaps** 和 **vmaps** 文件夹。

4. 启动 extractor.bat 并选择你的提取选项。

{{site.data.alerts.important}}
</br>

   - <b>dbc</b>、<b>maps</b> 和 <b>vmaps</b> 是让服务器正常工作的必需文件！

   - 不要试图停止 <b>vmaps</b> 提取过程。当它打印出"Press any key..."时就表示完成了。它会创建两个新文件夹：<b>buildings</b> 和 <b>vmaps</b>。<b>buildings</b> 文件夹在运行完成后完全没有用处，可以安全删除。

   - 在第一个任务完成之前不要运行另一个任务，否则你会遇到错误。

   - 如果你在 vmap4extractor 完成之前停止了它，再次开始之前你需要删除 Buildings 目录。

   - <b>可选但强烈推荐：提取 mmaps。</b>不要试图在此过程提取期间停止它。
{{site.data.alerts.end}}

5. 在 <b>C:\Build\bin\RelWithDebInfo</b> 中创建一个名为 <b>Data</b> 的新文件夹

6. 将 vmaps、maps、dbc、cameras 移动到 <b>Data</b> 文件夹中。

## 配置文件：Worldserver 和 Authserver {#config-files-worldserver-and-authserver}

首先，找到两个默认配置文件（名为 **worldserver.conf.dist** 和 **authserver.conf.dist**）并复制它们。然后将副本重命名为去掉 .dist 扩展名的同名文件。你可以在 C:\Build\bin\RelWithDebInfo\configs\ 中找到它们（位置可能有所不同）。

打开 .conf 文件，向下滚动到 LoginDatabaseInfo、WorldDatabaseInfo 和 CharacterDatabaseInfo，输入 MySQL 登录信息，以便服务器能够访问你的数据库。

在新编译的配置上，默认情况下你会得到以下值：
```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

它们遵循以下结构：

```
Variablename = "MySQLIP;Port;Username;Password;database"
```

以下步骤必须核实：

- 如果 AzerothCore 与运行 WoW 的是同一台电脑，主机名（127.0.0.1）可以保持不变。
  如果不是，请遵循 [Realmlist 表](realmlist) 中的说明。

- 端口（3306）是标准配置值。如果你在 MySQL 设置中更改了默认端口，则必须相应地进行更改。
  用户名和密码可以是可变的。你可以选择：

    - 使用默认的 acore / acore 用户名和密码组合。

    - 在你首选的数据库管理工具中的用户管理器（通常以一个看起来像人物形象的图标标识）内创建一个独立的登录账号，并赋予其必要的权限（SELECT、INSERT、UPDATE、DELETE 权限就足够了，而且更安全）。

### 更新 DataDir {#updating-datadir}

1. 在你的 **worldserver.conf** 文件中找到 **DataDir** 选项。

1. 将其修改为你文件夹的路径。例如 **C:\Build\bin\RelWithDebInfo\Data**

{% include tip.html content="对于大多数 **worldserver.conf** 设置的更改，你可以直接在游戏内输入 .reload config 来即时查看更改效果，而无需重启服务器。" %}

{% include warning.html content="AzerothCore 团队和所有者绝不赞助或支持任何非法公开服务器。如果你使用这些项目来运行非法公开服务器，而不是用于测试和学习，那完全是你个人的选择。" %}

### （可选）通过环境变量配置选项

可以通过环境变量加载配置选项，你可以点击 [此处](config-overrides-with-env-var) 了解相关信息。

## 帮助

{% include help.html %}

| 安装指南                                                                                                                        |                                                          |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上一个链接在各步骤之间轻松跳转。                                                |
| [<< 第 2 步：核心安装](windows-core-installation)                                                                                | [第 4 步：数据库安装 >>](database-installation)          |
