# Linux 服务器设置

| 安装指南                                                                                                                             |                                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 2 步：核心安装](linux-core-installation)                                                                                      | [第 4 步：数据库安装 >>](database-installation)                                |

**目录**
- [客户端数据文件（下载预提取文件）](#option-1-download-pre-extracted-files)
- [客户端数据提取器（自行提取文件）](#option-2-extract-files-yourself)
- [配置文件：Worldserver 和 Authserver](#config-files-worldserver-and-authserver)

既然你已经编译好了源码，就需要添加必要的客户端数据。你可以下载预提取的文件，也可以使用编译好的提取器自行提取文件。数据准备好后，你必须核验 **worldserver.conf** 文件中的 **DataDir** 选项，使其指向包含数据的目录。

有些文件是可选的，但强烈推荐：

| 目录     |                    |
| :-------- | :----------------- |
| dbc       | 必需              |
| maps      | 必需              |
| vmaps     | 强烈推荐          |
| mmaps     | 强烈推荐          |
| cameras   | 推荐              |

## 方案一：下载预提取文件 {#option-1-download-pre-extracted-files}


如果你打算使用 enUS 客户端，可以下载下面的数据文件。如果你打算使用任何其他语言的客户端，则需要[自行提取](#option-2-extract-files-yourself)数据。

<a class="no-icon" href="https://github.com/wowgaming/client-data/releases/" target="_blank"><i class="fa-solid fa-download"></i> 数据文件 enUS（AC Data v20）</a>

1. 下载压缩包 `data.zip`。

2. 将压缩包直接解压到默认的 **$AC_CODE_DIR/env/dist/bin/** 目录中，即 **worldserver.conf** 中 DataDir 选项所指定的位置。你也可以选择其他文件夹，但需要将[DataDir](#updating-datadir)配置选项编辑为你文件夹的位置。

**$AC_CODE_DIR/env/dist/bin** 的默认文件夹结构（由 `tree -L 1` 显示）：
```
.
├── authserver
├── Cameras
├── data-version
├── dbc
├── maps
├── mmaps
├── vmaps
└── worldserver
```

## 方案二：自行提取文件 {#option-2-extract-files-yourself}

**（如果你下载了上面的文件，则无需此操作）**

1. 进入你的安装目录（例如 **$AC_CODE_DIR/env/dist/bin/**），将以下文件复制到你的 World of Warcraft 文件夹（即 Wow.exe 所在的位置）中。
```
map_extractor
mmaps_generator
vmap4_assembler
vmap4_extractor
```

2. 进入 **$AC_CODE_DIR/apps/extractor/**，将 "**extractor.sh**" 与之前的文件一起复制到你的 World of Warcraft 文件夹中。

3. 在你的 World of Warcraft 目录中创建（`mkdir`）**mmaps** 和 **vmaps** 文件夹。

4. 运行 extractor.sh 并选择你的提取选项。

{{site.data.alerts.important}}
</br>

   - 需要 <b>dbc</b>、<b>maps</b> 和 <b>vmaps</b> 才能让服务器正常工作！

   - 不要试图停止 <b>vmaps</b> 提取过程。当它打印出 "Press any key..." 时才算完成。它会创建两个新文件夹：<b>buildings</b> 和 <b>vmaps</b>。<b>buildings</b> 文件夹在运行完毕后完全没有用处，可以安全删除。

   - 在第一个任务完成之前，不要运行另一个任务，否则会出现错误。

   - 如果你在完成之前停止 vmap4extractor，再次开始前需要删除 Buildings 目录。

   - <b>可选但极力推荐：提取 mmaps。</b> 在提取过程中不要试图停止此过程。
{{site.data.alerts.end}}


5. 将提取出的文件 <b>vmaps</b>、<b>maps</b>、<b>dbc</b> 和 <b>Cameras</b> 移动到 <b>$AC_CODE_DIR/env/dist/bin/</b> 文件夹或你选择的目录中（记得更新你的[DataDir](#updating-datadir)）。

完成后你会收到以下消息，可以安全地忽略它。

## 配置文件：Worldserver 和 Authserver {#config-files-worldserver-and-authserver}

首先，你需要找到两个默认配置文件（名为 **worldserver.conf.dist** 和 **authserver.conf.dist**）并复制它们。然后将副本重命名为去掉 .dist 扩展名的对应名称。你可以在安装目录 **$AC_CODE_DIR/env/dist/etc/** 中找到它们。

打开 .conf 文件，向下滚动到 LoginDatabaseInfo、WorldDatabaseInfo 和 CharacterDatabaseInfo，并输入 MySQL 登录信息，以便服务器能够访问你的数据库。

在新编译的配置中，默认会有以下值：
```
LoginDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_auth" worldserver.conf / authserver.conf
WorldDatabaseInfo     = "127.0.0.1;3306;acore;acore;acore_world" worldserver.conf
CharacterDatabaseInfo = "127.0.0.1;3306;acore;acore;acore_characters" worldserver.conf
```

它们遵循以下结构：

```
Variablename = "MySQLIP;Port;Username;Password;database"
```

必须核验以下步骤：

- 如果 AzerothCore 安装在与运行 WoW 相同的计算机上，主机名（127.0.0.1）可以保持不变。
  如果不是，请按照 [Realmlist 表](realmlist)中的说明进行操作。

- 端口（3306）是标准配置值。如果你在 MySQL 设置中更改了默认端口，则必须相应地更改。
  用户名和密码可以是变量。你可以选择：

    - 使用默认的 acore / acore 用户名和密码组合。

    - 在你偏好的数据库管理工具中的用户管理器（通常通过一个像一个人或一群人的图标来标识）中创建唯一登录账号，并赋予其必要的权限（SELECT、INSERT、UPDATE、DELETE 权限就足够了，而且更安全）。

### 更新 DataDir {#updating-datadir}

> **注意：** DataDir 的默认值是 `"."`。这意味着如果你的客户端文件（dbc、maps、mmaps 等）与 worldserver 二进制文件位于同一目录，则无需更新此选项。

1. 在你的 **worldserver.conf** 文件中找到 **DataDir** 选项。

1. 将 DataDir 编辑为你文件夹的绝对路径或相对路径。例如，**/home/acore/azerothcore/data/** 或 **./data**。

{% include tip.html content="对于大多数 **worldserver.conf** 设置更改，你可以直接在游戏中输入 .reload config 来立即生效，无需重启服务器。" %}

{% include warning.html content="AzerothCore 团队和所有者绝不赞助或支持非法的公共服务器。如果你使用这些项目运行非法的公共服务器，而不是用于测试和学习，那是你个人的选择。" %}

### （可选）通过环境变量配置选项

可以通过环境变量加载配置选项，你可以[在此处](config-overrides-with-env-var)阅读相关内容。

## 帮助

{% include help.html %}

| 安装指南                                                                                                                             |                                                                                 |
| :----------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------ |
| 本文是安装指南的一部分。你可以单独阅读本文，或点击上一个链接在各步骤之间轻松跳转。 |
| [<< 第 2 步：核心安装](linux-core-installation)                                                                                      | [第 4 步：数据库安装 >>](database-installation)                                |
