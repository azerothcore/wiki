# Windows 环境要求

{% include important.html content="<b>MySQL 26.x.x</b> 不受支持。请改用 <b>MySQL 8.4 LTS</b>。" %}

| 安装指南                                                                                                                        |                                                          |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上一个链接在各步骤之间轻松跳转。                                                |                                                          |
| [<< 开始：安装指南](classic-installation)                                                                                        | [第 2 步：核心安装 >>](windows-core-installation)         |

{% include callout.html content="Windows ≥ 10<br/>
Boost ≥ 1.78<br/>
MySQL ≥ 8.0（推荐 8.4）<br/>
OpenSSL ≥ 3.x.x<br/>
CMake ≥ 3.27<br/>
MS Visual Studio (Community) ≥ 17 (2022)（桌面版）（无预览版）" type="info" %}

1. [Git](https://git-scm.com/download/win)

    1. 下载独立安装程序

        - 在 Git 安装过程中——调整你的 PATH 环境变量。选择"Git from the command line and also from 3rd-party software"。

2. [Github Desktop](https://desktop.github.com/)

    1. 下载安装程序并按照步骤完成设置。

3. 安装编译器 / IDE [Visual Studio Community](https://visualstudio.microsoft.com/downloads/)

   你需要安装 C++ 编译器。

   为此，请在 **Workloads -> Desktop & Mobile** 下选择 **Desktop development for C++**。

   <a href="/wiki/images/visualstudio.jpg" target="_blank">
   <img src="/wiki/images/visualstudio.jpg" height="50%" width="50%">
   </a>

4. [MySQL Server Community Edition](https://dev.mysql.com/downloads/mysql/8.4.html)

    1. 下载 Windows MSI 安装程序。

    2. 向下滚动到底部，点击"No thanks, just take me to the downloads!"。

    3. 当安装即将完成时，确保勾选"Launch the MySQL Instance Configuration Wizard"，然后点击"Finish"。

    4. 当 MySQL Instance Configuration Wizard 启动时，大多数默认选项都没问题，但请记住你使用的用户名和密码（root // 随意）。稍后你需要用它们登录所选的数据库管理工具（见下文），以便导入 SQL 文件。

    5. 要测试 MySQL 是否设置正确，请按下键盘上的 CTRL+ALT+DEL，进入任务管理器，并选择"Services"标签页。在服务列表中，你应该能看到"MySQL"的状态为"Running"。

    6. 将 MySQL 添加到环境变量。

        1. 进入控制面板 -> 系统

        2. 进入高级系统设置

        3. 进入环境变量

        4. 在"系统变量"下选择 **Path**

        5. 编辑并添加你的 MySQL 安装路径，例如 **C:\Program Files\MySQL\MySQL Server 8.4\bin\\**

       请务必找到 MySQL 开发文件；你稍后会用到它们。这些文件随 MySQL Server 一起提供，请在程序文件目录中搜索它们，例如 MySQL\MySQL Server 8.4\lib。

5. 选择数据库管理工具

    - MySQL 命令行（最快）

    - [SQLYog Community Edition](https://github.com/webyog/sqlyog-community/wiki/Downloads)

    - [HeidiSQL](https://www.heidisql.com/download.php)（最适合初学者）

    - [DBeaver](https://dbeaver.io/)（跨平台数据库管理工具）

    1. 尝试连接到你的数据库。根据你使用的程序不同，你可能会看到"Connect to Host"、"New Connection"或"Session Manager"。

    2. 创建一个新的连接/会话。如果你将 MySQL 安装在安装 HeidiSQL 或 SQLYog 的同一台电脑上，Hostname/IP 地址填"127.0.0.1"或"localhost"即可。只需填写你的 root // 随意密码，现在你应该就能连接到数据库了。

6. [CMake](https://cmake.org/download/)

    1. 下载并安装 **Latest Release** 的 windows-x86_64.msi 文件，**绝不要使用 RC（Release Candidate，候选发布版）版本。**

    2. 我们建议进行 64 位编译。

7. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) 下载 64 位版本。

    1. 找到非"light"版本的最新 3.x.x Win64 OpenSSL 即为 64 位版本。（例如：Win64 OpenSSL v3.0.7）

    {{site.data.alerts.note}}
    如果在安装 OpenSSL 时遇到错误'Missing Microsoft Visual C++ .... Redistributable'，请下载 <a href="https://aka.ms/vs/17/release/vc_redist.x64.exe">Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64)（直接下载）</a>（1.7MB 安装程序）并安装它。
    {{site.data.alerts.end}}

    {{site.data.alerts.note}}
    在安装 OpenSSL 时，当被问到将 OpenSSL DLL 复制到哪里时，请选择 The OpenSSL binaries (/bin) 目录（而不是"The Windows system directory"）。这些 DLL 需要易于定位，以便用于 <a href="windows-core-installation">核心安装</a>。
    {{site.data.alerts.end}}

8. [Boost](https://www.boost.org/)。

    1. 下载适用于 Visual Studio 2022 的预编译 Windows 二进制文件。[64bit](https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download)

    2. 在"系统"变量中添加一个名为"BOOST_ROOT"的环境变量，其值是你的 Boost 安装目录，例如 `C:/local/boost_1_81_0`。重要的是在指向该目录时要使用'**/**'，而不是'**\\**'。（确保它没有尾随斜杠（路径末尾）。如果仍有问题，请同时在 `USER` 变量部分添加相同的变量，如下方图片所示。）

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

{% include note.html content="请注意，这张图片显示的是版本号 1.72.0——请在设置中使用你实际的版本号。" %}

<br>

## 帮助

{% include help.html %}

| 安装指南                                                                                                                        |                                                          |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------- |
| 本文是安装指南的一部分。你可以单独阅读，也可以点击上一个链接在各步骤之间轻松跳转。                                                |                                                          |
| [<< 开始：安装指南](classic-installation)                                                                                        | [第 2 步：核心安装 >>](windows-core-installation)         |
