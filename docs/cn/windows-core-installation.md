# Windows 核心安装

| 安装指南                                                                                                                        |                                        |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上一个链接在各步骤之间轻松跳转。                                              |
| [<< 第 1 步：环境要求](windows-requirements)                                                                                     | [第 3 步：服务器设置 >>](windows-server-setup) |

## 所需软件

在继续之前请先阅读 [环境要求](windows-requirements)。

## 拉取并编译源代码

### 拉取代码

1. 创建用于存放源文件的目录。在本指南中，我们将使用 **C:\Azerothcore**。

1. 打开 Github Desktop

1. 点击左上角的 **File** -> **Clone repository...**

1. 点击 **URL**

1. 按如下方式填写数据：

```
Repository URL or GitHub username and repository: https://github.com/azerothcore/azerothcore-wotlk
Local path: C:\Azerothcore
```

点击 **Clone**。几分钟内，Azerothcore 的源文件将被克隆到 **C:\Azerothcore**。

#### 故障排除

如果你遇到类似 **fatal: early EOF** 或 **fatal: fetch-pack: invalid index-pack output** 的错误，可以在此处找到解决方法：[常见错误 ACE00105](common-errors#ace00105)。

### 使用 CMake 配置并生成 Visual C++ 解决方案

在开始之前，创建一个名为 **Build** 的新目录。在本指南中，我们将使用 **C:\Build**。

1. 打开 CMake

1. 点击 **Browse Source...** → 选择源目录（**C:\Azerothcore**）

1. 点击 **Browse Build...** → 选择构建目录（**C:\Build**）

1. 点击 **Configure**。

1. 在下拉菜单中选择你在 [环境要求](windows-requirements) 部分下载的编译器版本。如果你进行的是 64 位编译，请务必选择 **Win64** 版本。

1. 确保 **Use default native compilers** 已勾选。

1. 点击 **Finish**。

1. 确保 **TOOLS_BUILD** 设置为 `all`。这将编译后续设置中所需的提取器（extractor）。

1. 再次点击 **Configure**。只要日志窗口中还有红色字体的错误，你就需要检查参数并重新运行。

1. 点击 **Generate**。这会将所选构建文件安装到你的 **C:\Build** 文件夹中。

{{site.data.alerts.note}}
如果遇到 CMake 错误，请参见 <a href="common-errors#core-installation-errors">常见错误</a>。
{{site.data.alerts.end}}

### 编译源代码 {#compiling-the-source}

1. 在 CMake 中点击 **Open Project**，直接用 Visual Studio 打开 **AzerothCore.sln** 文件。

1. 在顶部菜单中点击 **Build**，然后选择 **Configuration Manager**。

    1. 将 **Active Solution Configuration** 设置为 **RelWithDebInfo**。

    1. 将 **Active Solution Platform** 设置为 **x64**，然后点击关闭（设置会自动保存）。

1. 在右侧边栏的 Solution Explorer 中右键点击 **ALL_BUILD**，选择 **Clean**。

1. 右键点击 **ALL_BUILD**，选择 **Build**。（Ctrl + Shift + B）

    1. 如果你的界面没有显示 Solution Explorer，请点击 Build 菜单并选择 **Clean Solution**，然后再选择 **Build**。

编译时间因机器而异，但预计需要 5 到 30 分钟。

如果在编译期间或编译完成后提示你"Reload build files"（重新加载构建文件），请照做。

构建完成后，你会在输出中看到类似这样的消息：

```
========== Build: 22 succeeded, 0 failed, 0 up-to-date, 1 skipped ==========
```

你会在 **C:\Build\bin\RelWithDebInfo** 或 **C:\Build\bin\Debug** 文件夹中找到刚编译好的二进制文件。在本教程的最后，它们都将用于运行你的服务器。

核心要正常运行，你需要以下文件：

```
\configs\
authserver.exe
authserver.pdb
worldserver.exe
worldserver.pdb
libmysql.dll
legacy.dll
libcrypto-3-x64.dll
libssl-3-x64.dll
```

有四个 DLL 文件需要手动添加到该文件夹中，你需要从以下目录复制它们：

{% include callout.html content="<b>libmysql.dll</b> → C:\Program Files\MySQL\MySQL Server 8.4\lib" type="primary" %}

{% include note.html content="你的 libmysql.dll 版本需要与你运行的 MySQL Server 版本匹配。如果你更新了 MySQL 服务器，则需要重新编译核心并复制新的 dll 文件。" %}

{% include callout.html content="<b>legacy.dll</b>、<b>libcrypto-3-x64.dll</b> 和 <b>libssl-3-x64.dll</b> → C:\OpenSSL-Win64\bin" type="primary" %}

在 **configs** 文件夹中，你应该找到：

```
authserver.conf.dist
worldserver.conf.dist
```

#### 关于编译日志和报告

pdb 文件只有在你使用 Debug 或 RelWithDebInfo 配置编译时才会存在。这不是强制要求，但建议至少使用 RelWithDebInfo 配置编译核心，以便获得正常的崩溃日志。

{% include important.html content="要报告崩溃日志，必须使用 Debug 或 RelWithDebInfo 配置编译。" %}

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                        |                                        |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上一个链接在各步骤之间轻松跳转。                                              |
| [<< 第 1 步：环境要求](windows-requirements)                                                                                     | [第 3 步：服务器设置 >>](windows-server-setup) |
