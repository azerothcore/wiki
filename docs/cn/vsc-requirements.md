# VSC 环境要求

{% include note.html content="本指南由社区制作。可能不是最新的，也不受官方支持。" %}

| 安装指南 | |
| :- | :- |
| [<< 开始：安装指南](installation) | [第 2 步：VSC 核心安装 >>](windows-vsc-core-installation) |

| |
| :- |
| Boost ≥ 1.78                 |
| MySQL ≥ 8.0 (Recommended 8.4) |
| OpenSSL ≥ 3.x.x              |
| CMake ≥ 3.27                 |
| MS Visual Studio Build Tools ≥ 2022 |

1. Git 扩展
   
   1. 你需要安装 Git。你可以在这里获取最新版本 https://git-scm.com/download/win
   
1. 安装 [Visual Studio 2022 Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022)

   你需要安装 C++ 编译器。

   为此，请在**工作负载 -> 桌面与移动**下选择 **C++ 桌面开发**。

   <a href="/wiki/images/visualstudio_tools.png" target="_blank">
   <img src="/wiki/images/visualstudio_tools.png" height="50%" width="50%">
   </a>
   
1. [Visual Studio Code](https://code.visualstudio.com/)

	1. 下载并安装**最新版本**
	1. 安装扩展
		1. 点击**查看**->**扩展**
		
			<a href="/wiki/images/vsc_extensions.png.png" target="_blank"><img src="/wiki/images/vsc_extensions.png"></a>
		1. 在搜索栏中输入 **C/C++ Extension Pack**
		1. 点击绿色的安装按钮	
			
			<a href="/wiki/images/visualstudio_tools.png" target="_blank"><img src="/wiki/images/vcs_extension_pack_install.png" height="50%" width="50%"></a>

1. [CMake](https://cmake.org/)

    1. 下载并安装**最新发布版**的 win32-x86.exe 文件，**切勿使用 RC（候选发布版）版本。**
    
    1. 我们建议以 64 位模式编译。 

1. MySQL 开发文件

    1. 这些文件随 MySQL Server 一同提供，请在程序文件目录中查找它们：MySQL\MySQL Server 8.0\lib / MySQL\MySQL Server 5.7\lib。

1. [OpenSSL](http://www.slproweb.com/products/Win32OpenSSL.html) 下载 64 位版本。如果你计划同时编译 32 位和 64 位，也可以两个都下载，它们可以并存。

    1. 通过查找最新且非"light"（精简）版本的 3.x.x Win64 OpenSSL 来获取 64 位版本。（示例：Win64 OpenSSL v3.0.7）
    
    1. 通过查找最新且非"light"（精简）版本的 3.x.x Win32 OpenSSL 来获取 32 位版本。（示例：Win32 OpenSSL v3.0.7）

    1. *注意 #1：如果在安装 OpenSSL 时收到"缺少 Microsoft Visual C++ Redistributable"错误消息，*
       *请下载 [Microsoft Visual C++ 2017/2019/2022 Redistributable Package (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe)（1.7MB 安装程序）并安装它。*
       
    1. *注意 #2：安装 OpenSSL 时，在选择将 OpenSSL DLL 复制到何处时，请选择 The OpenSSL binaries (/bin) 目录（而非"The Windows system directory"）。*
       *这些 DLL 需要易于定位，以便进行[核心安装](windows-core-installation)。*

1. [Boost](https://www.boost.org/)。

    1. 下载适用于 Visual Studio Tools 的预构建 Windows 二进制文件

    1. `1.78.0` 是 Visual Studio Build Tools 所需的最低版本

    1. 64 位：https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-64.exe/download

    1. 32 位：https://sourceforge.net/projects/boost/files/boost-binaries/1.81.0/boost_1_81_0-msvc-14.3-32.exe/download

    1. 在"系统"变量中添加一个名为"BOOST_ROOT"的环境变量，其值为你的 Boost 安装目录，例如 `E:/Programs/boost_1_81_0`。指向目录时务必使用'**/**'，而不是'**\\**'。（确保路径末尾没有斜杠。如果仍有问题，请像下图所示，在`USER`变量部分也添加相同的变量。）

    <a href="/wiki/images/boost.jpg" target="_blank">
    <img src="/wiki/images/boost.jpg" height="50%" width="50%">
    </a>

    1. 请注意，此图片显示的是版本号 `1.72.0`——请在设置中使用你自己的实际版本号。
